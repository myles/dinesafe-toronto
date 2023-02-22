import datetime
import json
from copy import deepcopy
from typing import Any, Dict, List

import requests
from sqlite_utils import Database
from sqlite_utils.db import Table


def open_database(db_path: str) -> Database:
    """
    Open the DineSafe Database.
    """
    db = Database(db_path)

    if db.tables:
        from .migrations import migrate

        migrate(db)

    return db


def build_tables(db: Database):
    """
    Build the SQLite database structure.
    """
    establishments_table: Table = db.table("establishments")  # type: ignore
    inspections_table: Table = db.table("inspections")  # type: ignore

    establishment_statuses_table: Table = db.table("establishment_statuses")  # type: ignore
    inspection_severities_table: Table = db.table("inspection_severities")  # type: ignore

    if establishment_statuses_table.exists() is False:
        establishment_statuses_table.create(
            columns={"status": str, "order": int},
            pk="status",
        )

    establishment_statuses_table.upsert_all(
        [
            {"status": "Pass", "order": 0},
            {"status": "Conditional Pass", "order": 1},
            {"status": "Closed", "order": 2},
        ],
        pk="status",
    )

    if establishments_table.exists() is False:
        establishments_table.create(
            columns={
                "id": int,
                "name": str,
                "type": str,
                "address": str,
                "status": str,
                "minimum_inspections_per_year": int,
                "latitude": float,
                "longitude": float,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime,
            },
            pk="id",
        )
        establishments_table.enable_fts(
            ["name", "address"], create_triggers=True
        )

    if inspection_severities_table.exists() is False:
        inspection_severities_table.create(
            columns={"severity": str, "order": int},
            pk="severity",
        )

    inspection_severities_table.upsert_all(
        [
            {"severity": "M - Minor", "order": 0},
            {"severity": "S - Significant", "order": 1},
            {"severity": "C - Crucial", "order": 2},
            {"severity": "NA - Not Applicable", "order": 9},
        ],
        pk="severity",
    )

    if inspections_table.exists() is False:
        inspections_table.create(
            columns={
                "id": int,
                "establishment_id": int,
                "infraction_details": str,
                "date": datetime.date,
                "severity": str,
                "action": str,
                "outcome": str,
                "amount_fined": float,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime,
            },
            pk="id",
            foreign_keys=(
                ("establishment_id", "establishments", "id"),
            ),
        )

    # Views
    db.create_view(
        "establishments_by_status",
        """
        select
          count(establishments.id) as count,
          establishment_statuses.status
        from
          establishment_statuses
          left join establishments on establishments.status = establishment_statuses.status
        group by
          establishment_statuses.status
        order by
          establishment_statuses.status
        """,
        replace=True,
    )

    db.create_view(
        "inspections_by_severity",
        """
        select
          count(inspections.id) as count,
          inspection_severities.severity
        from
          inspection_severities
          left join inspections on inspections.severity = inspection_severities.severity
        group by
          inspection_severities.severity
        order by
          inspection_severities.severity
        """,
        replace=True,
    )


def get_dinesafe_data_url() -> str:
    """
    Connect to the OpenData Toronto package database and get the latest URL
    for the DineSafe JSON file.
    """
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
    params = {"id": "dinesafe"}

    response = requests.get(url=url, params=params)
    response.raise_for_status()

    data = response.json()
    resources = data["result"]["resources"]

    for resource in resources:
        if "format" in resource and resource["format"] == "JSON":
            return resource["url"]

    raise Exception("Could not find the Dinesafe JSON feed.")


def get_dinesafe_data(url: str) -> List[Dict[str, Any]]:
    """
    Get the Dinesafe JSON file.
    """
    with requests.get(url=url, stream=True) as response:
        content = response.content
    return json.loads(content)


def transform_establishment(establishment: Dict[str, Any], existing_row: bool):
    """
    Transform a Dinesafe establishment.
    """
    now = datetime.datetime.utcnow()

    establishment["updated_at"] = now
    if existing_row is False:
        establishment["created_at"] = now

    establishment["id"] = establishment.pop("Establishment ID")
    establishment["name"] = establishment.pop("Establishment Name", None) or ""
    establishment["type"] = establishment.pop("Establishment Type", None) or ""
    establishment["address"] = (
        establishment.pop("Establishment Address", None) or ""
    )
    establishment["status"] = (
        establishment.pop("Establishment Status", None) or None
    )
    establishment["minimum_inspections_per_year"] = (
        establishment.pop("Min. Inspections Per Year", None) or None
    )
    establishment["latitude"] = establishment.pop("Latitude", None) or None
    establishment["longitude"] = establishment.pop("Longitude", None) or None

    to_remove = [
        k
        for k in establishment.keys()
        if k
        not in (
            "id",
            "name",
            "type",
            "address",
            "status",
            "minimum_inspections_per_year",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
        )
    ]
    for key in to_remove:
        del establishment[key]


def transform_inspection(inspection: Dict[str, Any], existing_row: bool):
    """
    Transform a Dinesafe inspection.
    """
    now = datetime.datetime.utcnow()

    inspection["updated_at"] = now
    if existing_row is False:
        inspection["created_at"] = now

    inspection["id"] = inspection.pop("Inspection ID")
    inspection["establishment_id"] = inspection.pop("Establishment ID")
    inspection["infraction_details"] = (
        inspection.pop("Infraction Details", None) or ""
    )
    inspection["date"] = inspection.pop("Inspection Date", None) or None
    inspection["severity"] = inspection.pop("Severity", None) or None
    inspection["action"] = inspection.pop("Action", None) or None
    inspection["outcome"] = inspection.pop("Outcome", None) or ""
    inspection["amount_fined"] = inspection.pop("Amount Fined", None) or None

    to_remove = [
        k
        for k in inspection.keys()
        if k
        not in (
            "id",
            "establishment_id",
            "infraction_details",
            "date",
            "severity",
            "action",
            "outcome",
            "amount_fined",
            "created_at",
            "updated_at",
        )
    ]
    for key in to_remove:
        del inspection[key]


def get_existing_ids(table: Table) -> List[int]:
    """
    Get existing IDs for a given table.
    """
    rows = table.rows_where(select="id", order_by="id")
    return [int(row["id"]) for row in rows]


def get_establishments(dinesafe_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    '''
    Extract the DineSafe establishments from the data.
    '''
    dinesafe_data = deepcopy(dinesafe_data)

    establishments = []
    found_establishment_ids = set()

    for d in dinesafe_data:
        if d["Establishment ID"] not in found_establishment_ids:
            found_establishment_ids.add(d["Establishment ID"])
            establishments.append(d)

    return establishments


def get_inspections(dinesafe_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    '''
    Extract the DineSafe inspections from the data.
    '''
    dinesafe_data = deepcopy(dinesafe_data)
    return list(filter(lambda d: d["Inspection ID"] is not None, dinesafe_data))


def save_dinesafe(
    dinesafe_data: List[Dict[str, Any]],
    *,
    establishments_table: Table,
    inspections_table: Table,
):
    """
    Save dinesafe report.
    """
    establishments = get_establishments(dinesafe_data)
    inspections = get_inspections(dinesafe_data)

    existing_establishment_ids = get_existing_ids(table=establishments_table)
    existing_inspection_ids = get_existing_ids(table=inspections_table)

    for establishment in establishments:
        transform_establishment(
            establishment,
            existing_row=establishment["Establishment ID"]
            in existing_establishment_ids,
        )

    for inspection in inspections:
        transform_inspection(
            inspection,
            existing_row=inspection["Inspection ID"] in existing_inspection_ids,
        )

    establishments_table.upsert_all(establishments, pk="id")
    inspections_table.upsert_all(inspections, pk="id")

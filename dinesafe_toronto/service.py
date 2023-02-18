import datetime
import json
from copy import deepcopy
from typing import Any, Dict, List

import requests
from sqlite_utils import Database
from sqlite_utils.db import Table


def build_tables(db: Database):
    """
    Build the SQLite database structure.
    """
    establishments_table: Table = db.table("establishments", db=db)  # type: ignore
    inspections_table: Table = db.table("inspections", db=db)  # type: ignore

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
            },
            pk="id",
        )
        establishments_table.enable_fts(
            ["name", "address"], create_triggers=True
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
            },
            pk="id",
            foreign_keys=(("establishment_id", "establishments", "id"),),
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


def transform_establishment(establishment: Dict[str, Any]):
    """
    Transform a Dinesafe establishment.
    """
    establishment["id"] = establishment.pop("Establishment ID")
    establishment["name"] = establishment.pop("Establishment Name", None) or ""
    establishment["type"] = establishment.pop("Establishment Type", None) or ""
    establishment["address"] = (
        establishment.pop("Establishment Address", None) or ""
    )
    establishment["status"] = (
        establishment.pop("Establishment Status", None) or ""
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
        )
    ]
    for key in to_remove:
        del establishment[key]


def transform_inspection(inspection: Dict[str, Any]):
    """
    Transform a Dinesafe inspection.
    """
    inspection["id"] = inspection.pop("Inspection ID")
    inspection["establishment_id"] = inspection.pop("Establishment ID")
    inspection["infraction_details"] = (
        inspection.pop("Infraction Details", None) or ""
    )
    inspection["date"] = inspection.pop("Inspection Date", None) or None
    inspection["severity"] = inspection.pop("Severity", None) or ""
    inspection["action"] = inspection.pop("Action", None) or ""
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
        )
    ]
    for key in to_remove:
        del inspection[key]


def save_dinesafe(
    dinesafe_data: List[Dict[str, Any]],
    *,
    establishments_table: Table,
    inspections_table: Table,
):
    """
    Save dinesafe report.
    """
    establishments = deepcopy(dinesafe_data)
    inspections = deepcopy(dinesafe_data)

    for establishment in establishments:
        transform_establishment(establishment)

    for inspection in inspections:
        transform_inspection(inspection)

    establishments_table.upsert_all(establishments, pk="id")
    inspections_table.upsert_all(inspections, pk="id")

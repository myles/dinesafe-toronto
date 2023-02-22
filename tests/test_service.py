import pytest
import responses
from responses import matchers

from dinesafe_toronto import service

from . import fixtures


def test_build_tables(mock_db):
    service.build_tables(mock_db)

    assert mock_db["establishments"].exists() is True
    assert mock_db["inspections"].exists() is True

    assert mock_db["establishment_statuses"].exists() is True
    assert mock_db["inspection_severities"].exists() is True

    assert mock_db["establishments_by_status"].exists() is True
    assert mock_db["inspections_by_outcome"].exists() is True
    assert mock_db["inspections_by_severity"].exists() is True


@responses.activate
def test_get_dinesafe_data_url():
    expected_result = fixtures.OPEN_TORONTO_DINESAFE_JSON_RESOURCE["url"]

    responses.add(
        responses.Response(
            method="GET",
            url="https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show",
            match=[matchers.query_param_matcher({"id": "dinesafe"})],
            json=fixtures.OPEN_TORONTO_PACKAGE_RESPONSE,
        )
    )

    result = service.get_dinesafe_data_url()
    assert result == expected_result


@responses.activate
def test_get_dinesafe_data():
    url = fixtures.OPEN_TORONTO_DINESAFE_JSON_RESOURCE["url"]
    expected_payload = [{"t-rex": "🦖"}]

    responses.add(
        responses.Response(
            method="GET",
            url=url,
            json=expected_payload,
        )
    )

    result = service.get_dinesafe_data(url)
    assert expected_payload == result


@pytest.mark.parametrize("existing_row", (True, False))
def test_transform_establishment(existing_row):
    establishment = fixtures.DINESAFE_INSPECTION_ONE.copy()
    transformed = fixtures.TRANSFORMED_DINESAFE_ESTABLISHMENT.copy()

    service.transform_establishment(establishment, existing_row)

    assert "updated_at" in establishment
    if existing_row is True:
        assert len(establishment.keys()) == 9
        assert "created_at" not in establishment
    else:
        assert len(establishment.keys()) == 10
        assert "created_at" in establishment

    assert establishment["id"] == transformed["id"]
    assert establishment["name"] == transformed["name"]
    assert establishment["type"] == transformed["type"]
    assert establishment["address"] == transformed["address"]
    assert establishment["status"] == transformed["status"]
    assert (
        establishment["minimum_inspections_per_year"]
        == transformed["minimum_inspections_per_year"]
    )
    assert establishment["longitude"] == transformed["longitude"]
    assert establishment["latitude"] == transformed["latitude"]


@pytest.mark.parametrize("existing_row", (True, False))
def test_transform_inspection(existing_row):
    inspection = fixtures.DINESAFE_INSPECTION_ONE.copy()
    transformed = fixtures.TRANSFORMED_DINESAFE_INSPECTION.copy()

    service.transform_inspection(inspection, existing_row)

    assert "updated_at" in inspection
    if existing_row is True:
        assert len(inspection.keys()) == 9
        assert "created_at" not in inspection
    else:
        assert len(inspection.keys()) == 10
        assert "created_at" in inspection

    assert inspection["id"] == transformed["id"]
    assert inspection["establishment_id"] == transformed["establishment_id"]
    assert inspection["infraction_details"] == transformed["infraction_details"]
    assert inspection["date"] == transformed["date"]
    assert inspection["severity"] == transformed["severity"]
    assert inspection["action"] == transformed["action"]
    assert inspection["outcome"] == transformed["outcome"]
    assert inspection["amount_fined"] == transformed["amount_fined"]


def test_get_establishments():
    dinesafe_data = [
        fixtures.DINESAFE_INSPECTION_ONE.copy(),
        fixtures.DINESAFE_INSPECTION_TWO.copy(),
        fixtures.DINESAFE_INSPECTION_THREE.copy(),
    ]

    establishments = service.get_establishments(dinesafe_data)

    assert len(establishments) == 2
    establishment_one, establishment_two = establishments
    assert (
        establishment_one["Establishment ID"]
        == fixtures.DINESAFE_INSPECTION_ONE["Establishment ID"]
    )
    assert (
        establishment_two["Establishment ID"]
        == fixtures.DINESAFE_INSPECTION_THREE["Establishment ID"]
    )


def test_get_inspections():
    dinesafe_data = [
        fixtures.DINESAFE_INSPECTION_ONE.copy(),
        fixtures.DINESAFE_INSPECTION_TWO.copy(),
        fixtures.DINESAFE_INSPECTION_THREE.copy(),
    ]

    inspections = service.get_inspections(dinesafe_data)
    assert len(inspections) == 2
    inspection_one, inspection_two = inspections
    assert (
        inspection_one["Inspection ID"]
        == fixtures.DINESAFE_INSPECTION_ONE["Inspection ID"]
    )
    assert (
        inspection_two["Inspection ID"]
        == fixtures.DINESAFE_INSPECTION_TWO["Inspection ID"]
    )

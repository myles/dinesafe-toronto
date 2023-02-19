import pytest

from dinesafe_toronto import service

from . import fixtures


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

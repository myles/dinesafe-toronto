from dinesafe_toronto import service

from . import fixtures


def test_transform_establishment():
    establishment = fixtures.DINESAFE_INSPECTION_ONE.copy()
    expected_result = fixtures.TRANSFORMED_DINESAFE_ESTABLISHMENT.copy()

    service.transform_establishment(establishment)
    assert establishment == expected_result


def test_transform_inspection():
    inspection = fixtures.DINESAFE_INSPECTION_ONE.copy()
    expected_result = fixtures.TRANSFORMED_DINESAFE_INSPECTION.copy()

    service.transform_inspection(inspection)
    assert inspection == expected_result

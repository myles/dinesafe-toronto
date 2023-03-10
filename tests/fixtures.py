OPEN_TORONTO_DINESAFE_JSON_RESOURCE = {
    "cache_last_updated": None,
    "cache_url": None,
    "created": "2023-02-15T14:56:29.218640",
    "datastore_active": False,
    "datastore_resource_id": "i-am-a-datastore-resource-id",
    "format": "JSON",
    "hash": "",
    "id": "i-am-a-resource-id",
    "is_datastore_cache_file": True,
    "is_preview": None,
    "last_modified": "2023-02-21T02:04:08.152373",
    "metadata_modified": "2023-02-21T02:04:08.222818",
    "mimetype": "application/octet-stream",
    "mimetype_inner": None,
    "name": "Dinesafe.json",
    "package_id": "i-am-a-package-id",
    "position": 3,
    "resource_type": None,
    "size": 24128293,
    "state": "active",
    "url": (
        "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset"
        "/i-am-a-package-id/resource/i-am-a-resource-id/download/dinesafe.json"
    ),
    "url_type": "upload",
}

OPEN_TORONTO_PACKAGE_RESPONSE = {
    "success": True,
    "result": {
        "formats": "JSON,CSV,XML",
        "id": "i-am-a-package-id",
        "num_resources": 4,
        "num_tags": 4,
        "organization": {
            "id": "i-am-an-organization-id",
            "type": "organization",
            "is_organization": True,
            "approval_status": "approved",
            "state": "active",
        },
        "resources": [
            {
                "cache_last_updated": None,
                "cache_url": None,
                "created": "2023-02-15T14:54:40.958897",
                "datastore_active": True,
                "datastore_cache": {
                    "CSV": "815aedb5-f9d7-4dcd-a33a-4aa7ac5aac50",
                    "XML": "069d7753-73a8-4afd-a302-6cca0e8f1027",
                    "JSON": "i-am-a-resource-id",
                },
                "datastore_cache_last_update": "2023-02-21T02:04:08.957015",
                "extract_job": "Airflow - files_to_datastore.py - dinesafe",
                "format": "CSV",
                "hash": "",
                "id": "i-am-a-datastore-resource-id",
                "is_preview": True,
                "last_modified": None,
                "metadata_modified": "2023-02-21T02:04:09.054819",
                "mimetype": None,
                "mimetype_inner": None,
                "name": "Dinesafe",
                "package_id": "i-am-a-package-id",
                "package_name_or_id": "dinesafe",
                "position": 0,
                "resource_type": None,
                "size": None,
                "state": "active",
                "url": (
                    "https://ckan0.cf.opendata.inter.prod-toronto.ca/datastore"
                    "/dump/i-am-a-datastore-resource-id"
                ),
                "url_type": "datastore",
            },
            {
                "cache_last_updated": None,
                "cache_url": None,
                "created": "2023-02-15T14:56:27.687147",
                "datastore_active": False,
                "datastore_resource_id": "i-am-a-datastore-resource-id",
                "format": "CSV",
                "hash": "",
                "id": "815aedb5-f9d7-4dcd-a33a-4aa7ac5aac50",
                "is_datastore_cache_file": True,
                "is_preview": None,
                "last_modified": "2023-02-21T02:04:06.141571",
                "metadata_modified": "2023-02-21T02:04:06.212478",
                "mimetype": "application/octet-stream",
                "mimetype_inner": None,
                "name": "Dinesafe.csv",
                "package_id": "i-am-a-package-id",
                "position": 1,
                "resource_type": None,
                "size": 8783053,
                "state": "active",
                "url": (
                    "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset"
                    "/i-am-a-package-id/resource"
                    "/815aedb5-f9d7-4dcd-a33a-4aa7ac5aac50/download"
                    "/dinesafe.csv"
                ),
                "url_type": "upload",
            },
            {
                "cache_last_updated": None,
                "cache_url": None,
                "created": "2023-02-15T14:56:28.438398",
                "datastore_active": False,
                "datastore_resource_id": "i-am-a-datastore-resource-id",
                "format": "XML",
                "hash": "",
                "id": "069d7753-73a8-4afd-a302-6cca0e8f1027",
                "is_datastore_cache_file": True,
                "is_preview": None,
                "last_modified": "2023-02-21T02:04:07.067571",
                "metadata_modified": "2023-02-21T02:04:07.142297",
                "mimetype": "application/octet-stream",
                "mimetype_inner": None,
                "name": "Dinesafe.xml",
                "package_id": "i-am-a-package-id",
                "position": 2,
                "resource_type": None,
                "size": 33229519,
                "state": "active",
                "url": (
                    "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset"
                    "/i-am-a-package-id"
                    "/resource/069d7753-73a8-4afd-a302-6cca0e8f1027/download"
                    "/dinesafe.xml"
                ),
                "url_type": "upload",
            },
            OPEN_TORONTO_DINESAFE_JSON_RESOURCE,
        ],
        "tags": [
            {
                "display_name": "dinesafe",
                "id": "dd3a5a41-1edd-432b-9f4b-7515696addab",
                "name": "dinesafe",
                "state": "active",
                "vocabulary_id": None,
            },
            {
                "display_name": "food",
                "id": "1aa28fb4-5084-44a7-9cd6-c58ba9b607a0",
                "name": "food",
                "state": "active",
                "vocabulary_id": None,
            },
            {
                "display_name": "health inspection",
                "id": "5bfb0070-41b1-4304-87f1-7da3c65c6a6f",
                "name": "health inspection",
                "state": "active",
                "vocabulary_id": None,
            },
            {
                "display_name": "restaurant",
                "id": "f12cc31b-1e0e-4735-baed-00c7fa7946c8",
                "name": "restaurant",
                "state": "active",
                "vocabulary_id": None,
            },
        ],
        "groups": [],
        "relationships_as_subject": [],
        "relationships_as_object": [],
    },
}

DINESAFE_INSPECTION_ONE = {
    "_id": 1,
    "Rec #": 1,
    "Establishment ID": 123,
    "Inspection ID": 456,
    "Establishment Name": "A RANDOM RESTAURANT",
    "Establishment Type": "Food Depot",
    "Establishment Address": "789 STREET AVE, UNIT 0",
    "Establishment Status": "Pass",
    "Min. Inspections Per Year": "2",
    "Infraction Details": (
        "FAIL TO ENSURE FOOD HANDLER IN FOOD PREMISE WEARS CLEAN OUTER"
        " GARMENTS - SEC. 33(1)(C)"
    ),
    "Inspection Date": "2022-04-05",
    "Severity": "M - Minor",
    "Action": "Notice to Comply",
    "Outcome": "Pending",
    "Amount Fined": 500.90,
    "Latitude": 43.0000,
    "Longitude": -79.0000,
}

DINESAFE_INSPECTION_TWO = {
    "_id": 1,
    "Rec #": 1,
    "Establishment ID": 123,
    "Inspection ID": 567,
    "Establishment Name": "A RANDOM RESTAURANT",
    "Establishment Type": "Food Depot",
    "Establishment Address": "789 STREET AVE, UNIT 0",
    "Establishment Status": "Pass",
    "Min. Inspections Per Year": "2",
    "Infraction Details": (
        "FAIL TO ENSURE FOOD HANDLER IN FOOD PREMISE WEARS CLEAN OUTER"
        " GARMENTS - SEC. 33(1)(C)"
    ),
    "Inspection Date": "2023-01-05",
    "Severity": "M - Minor",
    "Action": "Notice to Comply",
    "Outcome": "Pending",
    "Amount Fined": 123.90,
    "Latitude": 43.0000,
    "Longitude": -79.0000,
}

TRANSFORMED_DINESAFE_ESTABLISHMENT = {
    "id": DINESAFE_INSPECTION_ONE["Establishment ID"],
    "name": DINESAFE_INSPECTION_ONE["Establishment Name"],
    "type": DINESAFE_INSPECTION_ONE["Establishment Type"],
    "address": DINESAFE_INSPECTION_ONE["Establishment Address"],
    "status": DINESAFE_INSPECTION_ONE["Establishment Status"],
    "minimum_inspections_per_year": DINESAFE_INSPECTION_ONE[
        "Min. Inspections Per Year"
    ],
    "latitude": DINESAFE_INSPECTION_ONE["Latitude"],
    "longitude": DINESAFE_INSPECTION_ONE["Longitude"],
}

TRANSFORMED_DINESAFE_INSPECTION = {
    "id": DINESAFE_INSPECTION_ONE["Inspection ID"],
    "establishment_id": DINESAFE_INSPECTION_ONE["Establishment ID"],
    "infraction_details": DINESAFE_INSPECTION_ONE["Infraction Details"],
    "date": DINESAFE_INSPECTION_ONE["Inspection Date"],
    "severity": DINESAFE_INSPECTION_ONE["Severity"],
    "action": DINESAFE_INSPECTION_ONE["Action"],
    "outcome": DINESAFE_INSPECTION_ONE["Outcome"],
    "amount_fined": DINESAFE_INSPECTION_ONE["Amount Fined"],
}

DINESAFE_INSPECTION_THREE = {
    "_id": 2,
    "Rec #": 2,
    "Establishment ID": 234,
    "Inspection ID": None,
    "Establishment Name": "A RANDOM RESTAURANT",
    "Establishment Type": "Food Depot",
    "Establishment Address": "789 STREET AVE, UNIT 0",
    "Establishment Status": "Pass",
    "Min. Inspections Per Year": "2",
    "Infraction Details": None,
    "Inspection Date": None,
    "Severity": None,
    "Action": None,
    "Outcome": None,
    "Amount Fined": None,
    "Latitude": 43.0000,
    "Longitude": -79.0000,
}

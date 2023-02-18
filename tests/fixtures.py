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
    "Infraction Details": "FAIL TO ENSURE FOOD HANDLER IN FOOD PREMISE WEARS CLEAN OUTER GARMENTS - SEC. 33(1)(C)",
    "Inspection Date": "2022-04-05",
    "Severity": "M - Minor",
    "Action": "Notice to Comply",
    "Outcome": "Pending",
    "Amount Fined": 500.90,
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

import click
from sqlite_utils import Database

from . import service


@click.group()
@click.version_option()
def cli():
    """
    Save data from Toronto's DineSafe into a SQLite database.
    """


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
def scrape_data(db_path: str):
    """
    Scrape Toronto's DineSafe inspection data and save the inspections and
    establishments to the SQLite database.
    """
    db = Database(db_path)

    service.build_tables(db)

    establishments_table: Table = db.table("establishments", db=db)  # type: ignore
    inspections_table: Table = db.table("inspections", db=db)  # type: ignore

    dinesafe_data_url = service.get_dinesafe_data_url()
    dinesafe_data = service.get_dinesafe_data(dinesafe_data_url)

    service.save_dinesafe(
        dinesafe_data,
        establishments_table=establishments_table,
        inspections_table=inspections_table,
    )

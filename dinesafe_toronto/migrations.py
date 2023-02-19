import datetime
from typing import Callable, List

from sqlite_utils import Database
from sqlite_utils.db import Table

MIGRATIONS: List[Callable[[Database], None]] = []


def migrate(db: Database):
    if "migrations" not in db.table_names():
        db["migrations"].create(  # type: ignore
            {"name": str, "applied": datetime.datetime}, pk="name"
        )

    applied_migrations = {
        m[0] for m in db.conn.execute("select name from migrations").fetchall()
    }

    for migration_func in MIGRATIONS:
        name = migration_func.__name__

        if name in applied_migrations:
            continue

        migration_func(db)

        db["migrations"].insert(  # type: ignore
            {"name": name, "applied": datetime.datetime.utcnow()}
        )


def migration(fn: Callable[[Database], None]):
    MIGRATIONS.append(fn)
    return fn

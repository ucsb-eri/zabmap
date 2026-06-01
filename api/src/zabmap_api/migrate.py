"""Database migrations for the zabmap *internal* DB.

peewee-migrate keeps an applied-migration log in the ``migratehistory`` table and
applies the ``.py`` files under ``migrations/`` in order. Only the internal DB
(Host, Filesystem, MetaData) is managed here — the source DB (ZfsSnapshots) is
read-only and owned by upstream tooling, so it is never migrated.

Usage (after `uv sync`):

    zabmap_migrate list                 # show applied + pending migrations
    zabmap_migrate migrate              # apply all pending migrations
    zabmap_migrate migrate 002_relax    # apply up to (and including) a migration
    zabmap_migrate rollback             # roll back the most recent migration
    zabmap_migrate fake 001_initial     # mark applied WITHOUT running (adoption)
    zabmap_migrate create my_change     # new empty migration
    zabmap_migrate create my_change -a  # new auto-generated migration from models
"""

import os
import sys

from peewee_migrate import Router

from zabmap_api.db import internal_db

MIGRATE_DIR = os.path.join(os.path.dirname(__file__), "migrations")


def get_router() -> Router:
    return Router(internal_db, migrate_dir=MIGRATE_DIR)


def main() -> None:
    router = get_router()
    args = sys.argv[1:]
    command = args[0] if args else "list"
    rest = args[1:]

    if command == "list":
        done = router.done
        todo = router.diff
        print("Applied:")
        for name in done:
            print(f"  [x] {name}")
        print("Pending:")
        for name in todo:
            print(f"  [ ] {name}")
        if not todo:
            print("  (none)")

    elif command == "migrate":
        name = rest[0] if rest else None
        router.run(name)

    elif command == "rollback":
        # peewee-migrate rolls back the most recently applied migration only.
        if not router.done:
            print("Nothing to roll back.")
            return
        router.rollback()

    elif command == "fake":
        if not rest:
            sys.exit("usage: zabmap_migrate fake <migration_name>")
        # Record migrations up to <name> as applied without executing their SQL.
        # Used once when adopting migrations on a database whose tables already exist.
        router.run(rest[0], fake=True)

    elif command == "create":
        if not rest:
            sys.exit("usage: zabmap_migrate create <name> [-a|--auto]")
        name = rest[0]
        auto = any(flag in rest[1:] for flag in ("-a", "--auto"))
        # Auto-diffs the models in zabmap_api.db against the migration history.
        router.create(name, auto="zabmap_api.db" if auto else False)

    else:
        sys.exit(f"unknown command: {command}\n\n{__doc__}")


if __name__ == "__main__":
    main()

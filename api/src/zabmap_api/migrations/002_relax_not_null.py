"""Drop NOT NULL on the columns the scheduler leaves unset on insert.

The production tables were originally created (before migrations existed) with
these columns NOT NULL, because peewee's ``default=None`` does not make a column
nullable. The models now declare ``null=True``, so update_hosts()/update_filesystems()
insert partial rows and hit a NotNullViolation. This reconciles the live schema
with the models.

``DROP NOT NULL`` is idempotent in Postgres, so this is safe whether a column is
currently NOT NULL (production) or already nullable (a fresh DB built from 001).
"""

NULLABLE = {
    "host": [
        "snapshots_in_sync",
        "filesystem_count",
        "replication_count",
    ],
    "filesystem": [
        "latest_snapshot",
        "snapshots_in_sync",
        "disabled",
        "backup_type",
        "ignore_backup_state",
    ],
}


def migrate(migrator, database, *, fake=False):
    for table, columns in NULLABLE.items():
        for column in columns:
            migrator.sql(
                f'ALTER TABLE "{table}" ALTER COLUMN "{column}" DROP NOT NULL'
            )


def rollback(migrator, database, *, fake=False):
    for table, columns in NULLABLE.items():
        for column in columns:
            migrator.sql(
                f'ALTER TABLE "{table}" ALTER COLUMN "{column}" SET NOT NULL'
            )

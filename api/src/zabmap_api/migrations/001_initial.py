"""Initial schema for the zabmap internal DB: Host, Filesystem, MetaData.

On a fresh database this creates the three tables. On the existing production
database the tables already exist, so this migration is marked applied without
running it:

    zabmap_migrate fake 001_initial

The actual constraint fix for production lives in 002_relax_not_null.py.
"""

import peewee as pw
from playhouse.postgres_ext import JSONField


def migrate(migrator, database, *, fake=False):
    @migrator.create_model
    class Host(pw.Model):
        id = pw.AutoField()
        name = pw.CharField(max_length=255, unique=True)
        snapshots_in_sync = pw.BooleanField(null=True)
        filesystem_count = pw.IntegerField(null=True)
        replication_count = JSONField(null=True)

        class Meta:
            table_name = "host"

    @migrator.create_model
    class Filesystem(pw.Model):
        id = pw.AutoField()
        host = pw.ForeignKeyField(
            migrator.orm["host"], field="id", backref="filesystems"
        )
        path = pw.CharField(max_length=255)
        backup_parent = pw.ForeignKeyField(
            "self", field="id", null=True, backref="backups"
        )
        latest_snapshot = pw.DateTimeField(null=True)
        snapshots_in_sync = pw.BooleanField(null=True)
        disabled = pw.BooleanField(null=True)
        zfs_properties = JSONField()
        replications = pw.IntegerField(default=0)
        backup_type = pw.CharField(max_length=255, null=True)
        ignore_backup_state = pw.BooleanField(null=True)

        class Meta:
            table_name = "filesystem"
            indexes = ((("host", "path"), True),)

    @migrator.create_model
    class MetaData(pw.Model):
        id = pw.AutoField()
        key = pw.CharField(max_length=255, unique=True)
        value = pw.CharField(max_length=255)

        class Meta:
            table_name = "metadata"


def rollback(migrator, database, *, fake=False):
    migrator.remove_model("metadata")
    migrator.remove_model("filesystem")
    migrator.remove_model("host")

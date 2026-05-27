import os
from enum import Enum

from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    PrimaryKeyField,
)
from playhouse.pool import PooledPostgresqlDatabase
from playhouse.postgres_ext import JSONField

# Source DB: holds the raw incoming ZfsSnapshots written by upstream tooling.
# zabmap only reads from here (the scheduler reads, the /api/backupstatus endpoint reads).
source_db = PooledPostgresqlDatabase(
    host=os.environ["FLASK_SOURCE_DB_HOST"],
    database=os.environ["FLASK_SOURCE_DB"],
    user=os.environ["FLASK_SOURCE_DB_USER"],
    password=os.environ["FLASK_SOURCE_DB_PASSWORD"],
    max_connections=8,
    stale_timeout=300,
)

# Internal DB (the "main" zabmap DB): derived tables (Host, Filesystem, MetaData)
# built by the scheduler from ZfsSnapshots and served by the API.
internal_db = PooledPostgresqlDatabase(
    host=os.environ["FLASK_DB_HOST"],
    database=os.environ["FLASK_DB"],
    user=os.environ["FLASK_DB_USER"],
    password=os.environ["FLASK_DB_PASSWORD"],
    max_connections=8,
    stale_timeout=300,
)


class BackupType(Enum):
    NONE = None
    ZAB = "zab"
    ZAS = "zas"


class SourceModel(Model):
    class Meta:
        database = source_db
        legacy_table_names = False


class InternalModel(Model):
    class Meta:
        database = internal_db
        legacy_table_names = False


class ZfsSnapshots(SourceModel):
    id = PrimaryKeyField()
    hostname = CharField()
    filesystem = CharField()
    most_recent_snapshot = CharField()
    properties = JSONField()
    timestamp = DateTimeField()
    last_backup = CharField()
    manual_override = BooleanField(default=False)
    manual_override_reason = CharField()
    last_run = DateTimeField()
    used_space = CharField()
    disabled = BooleanField(default=False)


class Host(InternalModel):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    snapshots_in_sync = BooleanField(default=None)
    filesystem_count = IntegerField()
    replication_count = JSONField()


class Filesystem(InternalModel):
    class Meta:
        database = internal_db
        legacy_table_names = False
        indexes = ((("host", "path"), True),)

    id = PrimaryKeyField()
    host = ForeignKeyField(model=Host, backref="filesystems")
    path = CharField()
    backup_parent = ForeignKeyField("self", null=True, backref="backups")
    latest_snapshot = DateTimeField()
    snapshots_in_sync = BooleanField(default=None)
    disabled = BooleanField(default=None)
    zfs_properties = JSONField()
    replications = IntegerField(default=0)
    backup_type = CharField(default=None)
    ignore_backup_state = BooleanField(default=None)


class MetaData(InternalModel):
    id = PrimaryKeyField()
    key = CharField(unique=True)
    value = CharField()

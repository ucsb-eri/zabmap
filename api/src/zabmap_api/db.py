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
from playhouse.shortcuts import ReconnectMixin


class ResilientPooledPostgresqlDatabase(ReconnectMixin, PooledPostgresqlDatabase):
    """Pooled Postgres that transparently reconnects on dead connections —
    useful for long-idle background jobs where firewalls drop idle TCP."""

# Source DB: holds the raw incoming ZfsSnapshots written by upstream tooling.
# zabmap only reads from here (the scheduler reads, the /api/backupstatus endpoint reads).
source_db = ResilientPooledPostgresqlDatabase(
    host=os.environ["FLASK_SOURCE_DB_HOST"],
    database=os.environ["FLASK_SOURCE_DB"],
    user=os.environ["FLASK_SOURCE_DB_USER"],
    password=os.environ["FLASK_SOURCE_DB_PASSWORD"],
    max_connections=8,
    stale_timeout=300,
)

# Internal DB (the "main" zabmap DB): derived tables (Host, Filesystem, MetaData)
# built by the scheduler from ZfsSnapshots and served by the API.
internal_db = ResilientPooledPostgresqlDatabase(
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
    snapshots_in_sync = BooleanField(null=True)
    filesystem_count = IntegerField(null=True)
    replication_count = JSONField(null=True)


class Filesystem(InternalModel):
    class Meta:
        database = internal_db
        legacy_table_names = False
        indexes = ((("host", "path"), True),)

    id = PrimaryKeyField()
    host = ForeignKeyField(model=Host, backref="filesystems")
    path = CharField()
    backup_parent = ForeignKeyField("self", null=True, backref="backups")
    latest_snapshot = DateTimeField(null=True)
    snapshots_in_sync = BooleanField(null=True)
    disabled = BooleanField(null=True)
    zfs_properties = JSONField()
    replications = IntegerField(default=0)
    backup_type = CharField(null=True)
    ignore_backup_state = BooleanField(null=True)


class MetaData(InternalModel):
    id = PrimaryKeyField()
    key = CharField(unique=True)
    value = CharField()

import os

from flask import current_app
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    PostgresqlDatabase,
    PrimaryKeyField,
)
from playhouse.postgres_ext import JSONField

psql_db = PostgresqlDatabase(
    host=os.environ["FLASK_DB_HOST"],
    database=os.environ["FLASK_DB"],
    user=os.environ["FLASK_DB_USER"],
    password=os.environ["FLASK_DB_PASSWORD"],
)

from enum import Enum


class BackupType(Enum):
    NONE = None
    ZAB = "zab"
    ZAS = "zas"


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = psql_db
        legacy_table_names = False


class ZfsSnapshots(BaseModel):
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
    in_sync = BooleanField(default=False)
    parent = ForeignKeyField("self", null=True, backref="children")


class Host(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    snapshots_in_sync = BooleanField(default=None)
    filesystem_count = IntegerField()
    replication_count = JSONField()


class Filesystem(Model):
    class Meta:
        database = psql_db
        legacy_table_names = False
        indexes = (("host", "path"), True)

    id = PrimaryKeyField()
    host = ForeignKeyField(model=Host, backref="filesystems")
    path = CharField()
    parent = ForeignKeyField("self", null=True, backref="backups")
    latest_snapshot = DateTimeField()
    snapshots_in_sync = BooleanField(default=None)
    disabled = BooleanField(default=None)
    zfs_properties = JSONField()
    replications = IntegerField(default=0)
    backup_type = CharField(default = None)
    ignore_backup_state = BooleanField(default=None)


class MetaData(BaseModel):
    id = PrimaryKeyField()
    key = CharField(unique=True)
    value = CharField()

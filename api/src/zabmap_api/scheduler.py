import re
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from icecream import ic
from peewee import JOIN, fn
from playhouse.shortcuts import model_to_dict

from zabmap_api.db import BackupType, Filesystem, Host, MetaData, ZfsSnapshots

# TODO: Disable debugging output
# ic.disable()


def extract_backup_type(path):
    if "/zab/" in path:
        return BackupType.ZAB.value
    elif "/zas/" in path:
        return BackupType.ZAS.value

    return BackupType.NONE.value


def extract_date_from_snapshot_name(snapshot):
    if not snapshot:
        return None

    match = re.match(r".*(\d{4}\d{2}\d{2}\d{2}\d{2}\d{2})$", snapshot)

    if match:
        try:
            date_match = datetime.strptime(match.group(1), "%Y%m%d%H%M%S")
        except ValueError:
            return None

        return date_match

    return None


def hostnames():
    # TODO: Remove where clause when done testing
    hosts_query = ZfsSnapshots.select(fn.Distinct(ZfsSnapshots.hostname))
    # .where(
    #     (ZfsSnapshots.hostname == "tjaart-linstor1.grit.ucsb.edu")
    #     | (ZfsSnapshots.hostname == "tjaart-linstor2.grit.ucsb.edu")
    # )
    return [el.hostname for el in hosts_query]


def update_hosts():
    for hostname in hostnames():
        host = (
            Host.insert(name=hostname)
            .on_conflict_ignore()
            # .on_conflict(
            #     conflict_target=Host.name,
            #     update={},
            # )
            .execute()
        )


def update_filesystems():
    for hostname in hostnames():
        host = Host.select().where(Host.name == hostname).first()

        fs_query = ZfsSnapshots.select().where(ZfsSnapshots.hostname == hostname)
        for fs in fs_query:
            latest_snapshot = extract_date_from_snapshot_name(fs.most_recent_snapshot)

            Filesystem.insert(
                host=host,
                path=fs.filesystem,
                latest_snapshot=latest_snapshot,
                snapshots_in_sync=None,
                disabled=fs.disabled,
                zfs_properties=fs.properties,
            ).on_conflict(
                conflict_target=[Filesystem.host, Filesystem.path],
                update={
                    Filesystem.latest_snapshot: latest_snapshot,
                    # Filesystem.snapshots_in_sync: None,
                    Filesystem.disabled: fs.disabled,
                    Filesystem.zfs_properties: fs.properties,
                },
            ).execute()

        Host.update({Host.filesystem_count: fs_query.count()}).where(
            Host.id == host.id
        ).execute()


def update_sync_status():
    for hostname in hostnames():
        host = Host.select().where(Host.name == hostname).first()

        Parent = Filesystem.alias()
        filesystems = (
            Filesystem.select(Filesystem, Parent)
            .join(Parent, JOIN.LEFT_OUTER, on=(Filesystem.parent_id == Parent.id))
            .where((Filesystem.host == host))
        )

        host_in_sync_arr = []

        replication_count = {"r0": 0, "r1": 0, "r2": 0}
        for filesystem in filesystems:
            backups_in_sync = False

            if filesystem.ignore_backup_state:
                backups_in_sync = None
            else:
                backups_in_sync_arr = []
                if filesystem.replications == 0:
                    replication_count["r0"] += 1
                elif filesystem.replications == 1:
                    replication_count["r1"] += 1
                elif filesystem.replications == 2:
                    replication_count["r2"] += 1

                if len(filesystem.backups) == filesystem.replications:
                    for backup in filesystem.backups:
                        if (
                            backup.latest_snapshot
                            and filesystem.latest_snapshot == backup.latest_snapshot
                        ):
                            backups_in_sync_arr.append(True)
                        else:
                            backups_in_sync_arr.append(False)

                    backups_in_sync = (
                        all(backups_in_sync_arr) if len(backups_in_sync_arr) > 0 else None
                    )
            host_in_sync_arr.append(backups_in_sync)
            Filesystem.update({Filesystem.snapshots_in_sync: backups_in_sync}).where(
                Filesystem.id == filesystem.id
            ).execute()

        host_in_sync = None
        for el in host_in_sync_arr:
            if el is None:
                host_in_sync = True
            elif el == False:
                host_in_sync = False
                break
            else:
                host_in_sync = True

        Host.update(
            {
                Host.snapshots_in_sync: host_in_sync,
                Host.replication_count: replication_count,
            }
        ).where(Host.id == host.id).execute()


def set_last_updated_date():
    now = str(datetime.now())
    MetaData.insert(key="last_updated", value=now).on_conflict(
        conflict_target=MetaData.key, update={MetaData.value: now}
    ).execute()


def parse_server_prop(prop):
    elements = prop.split(",")

    return_arr = []
    for el in elements:
        try:
            (host, path) = el.split(":")
        except ValueError:
            return []

        return_arr.append((host, path.replace("-", "/")))

    return return_arr


def update_parents():
    for hostname in hostnames():
        host = Host.select().where(Host.name == hostname).first()

        filesystems = Filesystem.select().where(
            (Filesystem.host == host) & (Filesystem.disabled == False)
        )

        for filesystem in filesystems:
            server_props = parse_server_prop(
                filesystem.zfs_properties.get("zab:server", "")
            )
            path = filesystem.backups[0].path if len(filesystem.backups) > 0 else ""
            backup_type = extract_backup_type(path)
            replications = len(server_props)

            Filesystem.update(
                {
                    Filesystem.replications: replications,
                    Filesystem.backup_type: backup_type,
                }
            ).where(Filesystem.id == filesystem.id).execute()

            # In the past we incorrectly set parents for some filesystems. We should clear them out if they are set
            clear_parents = False
            for host, path in server_props:

                if host == filesystem.host.name:
                    clear_parents = True

                else:
                    # TODO: Not sure that this is universally correct, but at GRIT we remove the 1st part of the path
                    rem = filesystem.path.split("/", 1)

                    filesystem_rem = ""
                    if (len(rem)) > 1:
                        filesystem_rem = rem[1]
                    remote_path = f"{path}/{filesystem_rem}"
                    # print(remote_path)
                    remote_host = Host.select().where(Host.name == host).first()
                    remote_fs = (
                        Filesystem.select()
                        .where(
                            (Filesystem.host == remote_host)
                            & (Filesystem.path == remote_path)
                        )
                        .first()
                    )

                    if remote_fs:
                        Filesystem.update({Filesystem.parent: filesystem}).where(
                            Filesystem.id == remote_fs.id
                        ).execute()

            if clear_parents:
                for backup in filesystem.backups:
                    ic(backup)
                    Filesystem.update({Filesystem.parent: None}).where(
                        Filesystem.id == backup.id
                    ).execute()


def run():
    ic("update hosts")
    update_hosts()
    ic("update filesystems")
    update_filesystems()
    ic("update parents")
    update_parents()
    ic("update sync status")
    update_sync_status()
    ic("set last updated date")
    set_last_updated_date()

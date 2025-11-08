from apscheduler.schedulers.background import BackgroundScheduler
from zabmap_api.db import ZfsSnapshots, Host, Filesystem
from peewee import fn


def update_backup_status():
    response = []
    # Parent = ZfsSnapshots.alias()
    # ZfsSnapshots.select(ZfsSnapshots, Parent).join(Parent, on=(ZfsSnapshots.parent == Parent.id)).where(Parent.hostname == host)
    hosts_query = ZfsSnapshots.select(fn.Distinct(ZfsSnapshots.hostname))
    hosts = [el.hostname for el in hosts_query]
    print(hosts)

    for host in hosts:
        # TODO: This needs to be calculated
        in_sync = False
        print(host)

        host_id = (
            Host.insert(name=host)
            .on_conflict(
                conflict_target=Host.name, update={Host.backups_in_sync: in_sync}
            )
            .execute()
        )
        print(host_id)

        fs_query = ZfsSnapshots.select().where(ZfsSnapshots.hostname == host)
        for fs in fs_query:
            parent = 1
            latest_backup = None
            in_sync_with_parent = False

            Filesystem.insert(
                host_id=host_id, path=fs.filesystem, parent=fs.parent_id
            ).on_conflict(
                conflict_target=[Filesystem.host, Filesystem.path],
                update={
                    Filesystem.parent: parent,
                    Filesystem.latest_backup: latest_backup,
                    Filesystem.in_sync_with_parent: in_sync_with_parent,
                },
            ).execute()

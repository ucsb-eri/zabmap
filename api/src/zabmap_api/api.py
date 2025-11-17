from flask import Flask, jsonify, request
import requests
import psycopg2
from flask_cors import CORS
import logging
import json
from datetime import datetime
import os
import tomllib
import re

from peewee import fn, JOIN
from playhouse.flask_utils import PaginatedQuery
from playhouse.shortcuts import model_to_dict
import logging
from zabmap_api.db import Host, Filesystem


app = Flask(__name__)
app.config.from_prefixed_env()

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("peewee").setLevel(logging.INFO)

with app.app_context():
    from zabmap_api.db import ZfsSnapshots
    from apscheduler.schedulers.background import BackgroundScheduler
    from .scheduler import run

    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=run, trigger="interval", minutes=10)
    # scheduler.start()

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [app.config["CORS_ORIGIN"]],
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "OPTIONS"],
        }
    },
)


def get_db_connection():
    conn = psycopg2.connect(
        host=app.config["DB_HOST"],
        database=app.config["DB"],
        user=app.config["DB_USER"],
        password=app.config["DB_PASSWORD"],
    )
    return conn


@app.route("/api/hosts", methods=["GET"])
def get_hosts():
    try:
        hosts_query = Host.select()

        hosts = [model_to_dict(el) for el in hosts_query]
        return jsonify(hosts)
    except Exception as e:
        print(f"Error fetching hosts: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/hosts/<host_id>/filesystems", methods=["GET"])
def get_host_filesystems(host_id):
    try:
        # Parent = Filesystem.alias()
        # filesystem_query = (
        #     Filesystem.select(Filesystem, Parent)
        #     .join(Parent, JOIN.LEFT_OUTER, on=(Filesystem.parent == Parent.id))
        #     .where(Filesystem.host_id == host_id)
        # )
        filesystem_query = Filesystem.select().where(Filesystem.host_id == host_id)

        filesystems = []

        for el in filesystem_query:
            print(el)
            filesystem = model_to_dict(el, backrefs=True, max_depth=1)
            print(filesystem)
            # children = model_to_dict(snapshot.children)
            # print(children)

            filesystems.append(filesystem)

        return jsonify(filesystems)

    except Exception as e:
        print(f"Error fetching filesystems with host_id {host_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/filesystems/<filesystem_id>", methods=["GET"])
def get_filesystem(filesystem_id):
    try:
        Parent = Filesystem.alias()
        # snapshots = Filesystem.select(Filesystem, Parent).join(Parent, on=(Filesystem.parent == Parent.id))
        filesystem_query = Filesystem.get_by_id(filesystem_id)

        filesystem = model_to_dict(filesystem_query, backrefs=True)
        # for el in filesystem_query:
        #     filesystem = model_to_dict(el, backrefs=True)
        #     # children = model_to_dict(snapshot.children)
        #     # print(children)
        #
        #     filesystems.append(filesystem)

        return jsonify(filesystem)

    except Exception as e:
        print(f"Error fetching filesystem with id {filesystem_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/hosts/<host>/backupstatus", methods=["GET"])
def get_backupstatus(host):
    # query = ZfsSnapshots.select(ZfsSnapshots.id, ZfsSnapshots.hostname, ZfsSnapshots.filesystem, ZfsSnapshots.most_recent_snapshot, ZfsSnapshots.parent)

    response = []
    # Parent = ZfsSnapshots.alias()
    # ZfsSnapshots.select(ZfsSnapshots, Parent).join(Parent, on=(ZfsSnapshots.parent == Parent.id)).where(Parent.hostname == host)
    query = ZfsSnapshots.select().where(ZfsSnapshots.hostname == host)

    for el in query:
        filesystem = model_to_dict(el, backrefs=True)

        in_sync_ids = []
        out_of_sync_ids = []
        backup_count = 0
        fs_snapshot_date = extract_date_from_snapshot_name(
            filesystem["most_recent_snapshot"]
        )
        for backup in filesystem["children"]:
            backup_snapshot_date = extract_date_from_snapshot_name(
                backup["most_recent_snapshot"]
            )

            if not fs_snapshot_date or fs_snapshot_date != backup_snapshot_date:
                in_sync = False

        response.append(
            {
                "id": filesystem["id"],
                "hostname": filesystem["hostname"],
                "filesystem": filesystem["filesystem"],
                "backup_count": backup_count,
                "in_sync_ids": in_sync_ids,
                "out_of_sync_ids": out_of_sync_ids,
            }
        )

    return jsonify(response)
    # paginated_query = PaginatedQuery(query, paginate_by=100, page=int(request.args.get("page", 1)))
    #
    # dicts = []
    # for result in paginated_query.get_object_list():
    #     model_to_dict(result, backrefs=True)
    # PaginatedQuery
    # for snapshot in ZfsSnapshots.select().order_by(ZfsSnapshots.id).paginate(1, 100):
    #     filesystem = model_to_dict(snapshot, backrefs=True)
    #     print(filesystem)

    # filesystems = []
    # for el in all:
    #     filesystem = model_to_dict(el, backrefs=True)
    #     # print(filesystem)
    #     filesystems.append(filesystem)

    # snapshots = ZfsSnapshots.select(fn.Distinct(ZfsSnapshots.hostname))
    # Parent = ZfsSnapshots.alias()
    # children = ZfsSnapshots.select(ZfsSnapshots, Parent).join(Parent, on=(ZfsSnapshots.parent == Parent.id))
    #
    # results = []
    # for filesystem in all:
    #     print(filesystem)
    #     print(children)
    #
    # print('')
    return jsonify(dicts)


#
#
# @app.route(
#     "/api/hosts/<host>/filesystems/<path:filesystem>/properties", methods=["GET"]
# )
# def get_properties(host, filesystem):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute(
#             "SELECT properties, timestamp, most_recent_snapshot, last_run, manual_override, manual_override_reason, manual_override_end_date FROM zfs_snapshots WHERE hostname = %s AND filesystem = %s",
#             (host, filesystem),
#         )
#         result = cursor.fetchone()
#         cursor.close()
#         conn.close()
#         if result:
#             (
#                 properties,
#                 timestamp,
#                 most_recent_snapshot,
#                 last_run,
#                 manual_override,
#                 manual_override_reason,
#                 manual_override_end_date,
#             ) = result
#
#             # Deserialize the properties JSON string
#             if isinstance(properties, str):
#                 properties = json.loads(properties)
#
#             response = {
#                 "properties": properties,
#                 "timestamp": timestamp,
#                 "most_recent_snapshot": most_recent_snapshot,
#                 "last_run": last_run,
#                 "manual_override": manual_override,
#                 "manual_override_reason": manual_override_reason,
#                 "manual_override_end_date": manual_override_end_date,
#             }
#             return jsonify(response)
#         else:
#             return jsonify({"error": "Properties not found"}), 404
#     except Exception as e:
#         print(
#             f"Error fetching properties for filesystem {filesystem} on host {host}: {e}"
#         )
#         return jsonify({"error": "Internal server error"}), 500
#
#
# @app.route("/api/hosts/<host>/filesystems/<filesystem>/override", methods=["POST"])
# def set_manual_override(host, filesystem):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         data = request.json
#         manual_override = data.get("manual_override", False)
#         manual_override_reason = data.get("manual_override_reason", "")
#         manual_override_end_date = data.get("manual_override_end_date", "")
#
#         cursor.execute(
#             "UPDATE zfs_snapshots SET manual_override = %s, manual_override_reason = %s, manual_override_end_date = %s WHERE hostname = %s AND filesystem = %s",
#             (
#                 manual_override,
#                 manual_override_reason,
#                 manual_override_end_date,
#                 host,
#                 filesystem,
#             ),
#         )
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return jsonify({"success": True})
#     except Exception as e:
#         print(
#             f"Error setting manual override for filesystem {filesystem} on host {host}: {e}"
#         )
#         return jsonify({"error": "Internal server error"}), 500
#
#
# def clear_expired_overrides():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute(
#             """
#             UPDATE zfs_snapshots
#             SET manual_override = false, manual_override_reason = NULL, manual_override_end_date = NULL
#             WHERE manual_override = true AND manual_override_end_date < %s
#         """,
#             (datetime.utcnow(),),
#         )
#         conn.commit()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(f"Error clearing expired manual overrides: {e}")
#
#
# @app.route("/api/tickets", methods=["POST"])
# def create_ticket():
#     zammad_url = "https://zammad.grit.ucsb.edu/api/v1/tickets"
#     bearer_token = "KOF2BL7oF3PxWUDWG__bgbcFDQykgdqXrUmkTaMSvdw_BT6r-aTohVIVqjeVrWge"
#     data = request.json
#
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {bearer_token}",
#     }
#
#     try:
#         response = requests.post(zammad_url, json=data, headers=headers)
#         response.raise_for_status()
#         return jsonify(response.json()), response.status_code
#     except requests.exceptions.HTTPError as err:
#         return jsonify({"error": str(err)}), response.status_code
#

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

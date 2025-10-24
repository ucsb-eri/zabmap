from flask import Flask, jsonify, request
import requests
import psycopg2
from flask_cors import CORS
import logging
import json
from datetime import datetime
import os
import tomllib


app = Flask(__name__)
app.config.from_prefixed_env()

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [app.config['CORS_ORIGIN']],
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "OPTIONS"],
        }
    },
)


def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        database=app.config['DB'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
    )
    return conn


logging.basicConfig(level=logging.DEBUG)


@app.route("/api/hosts", methods=["GET"])
def get_hosts():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT hostname FROM zfs_snapshots")
        hosts = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify([host[0] for host in hosts])
    except Exception as e:
        print(f"Error fetching hosts: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/hosts/<host>/filesystems", methods=["GET"])
def get_filesystems(host):
    try:
        clear_expired_overrides()  # Clear expired overrides before fetching filesystems
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT filesystem, most_recent_snapshot, manual_override, manual_override_reason, manual_override_end_date FROM zfs_snapshots WHERE hostname = %s",
            (host,),
        )
        filesystems = cursor.fetchall()
        cursor.close()
        conn.close()

        # Ensuring each entry is correctly formatted as a dict
        filesystems_list = [
            {
                "name": fs[0],
                "most_recent_snapshot": fs[1],
                "manual_override": fs[2],
                "manual_override_reason": fs[3],
                "manual_override_end_date": fs[4],
            }
            for fs in filesystems
        ]
        return jsonify(filesystems_list)
    except Exception as e:
        print(f"Error fetching filesystems for host {host}: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route(
    "/api/hosts/<host>/filesystems/<path:filesystem>/properties", methods=["GET"]
)
def get_properties(host, filesystem):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT properties, timestamp, most_recent_snapshot, last_run, manual_override, manual_override_reason, manual_override_end_date FROM zfs_snapshots WHERE hostname = %s AND filesystem = %s",
            (host, filesystem),
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            (
                properties,
                timestamp,
                most_recent_snapshot,
                last_run,
                manual_override,
                manual_override_reason,
                manual_override_end_date,
            ) = result

            # Deserialize the properties JSON string
            if isinstance(properties, str):
                properties = json.loads(properties)

            response = {
                "properties": properties,
                "timestamp": timestamp,
                "most_recent_snapshot": most_recent_snapshot,
                "last_run": last_run,
                "manual_override": manual_override,
                "manual_override_reason": manual_override_reason,
                "manual_override_end_date": manual_override_end_date,
            }
            return jsonify(response)
        else:
            return jsonify({"error": "Properties not found"}), 404
    except Exception as e:
        print(
            f"Error fetching properties for filesystem {filesystem} on host {host}: {e}"
        )
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/hosts/<host>/filesystems/<filesystem>/override", methods=["POST"])
def set_manual_override(host, filesystem):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        data = request.json
        manual_override = data.get("manual_override", False)
        manual_override_reason = data.get("manual_override_reason", "")
        manual_override_end_date = data.get("manual_override_end_date", "")

        cursor.execute(
            "UPDATE zfs_snapshots SET manual_override = %s, manual_override_reason = %s, manual_override_end_date = %s WHERE hostname = %s AND filesystem = %s",
            (
                manual_override,
                manual_override_reason,
                manual_override_end_date,
                host,
                filesystem,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        print(
            f"Error setting manual override for filesystem {filesystem} on host {host}: {e}"
        )
        return jsonify({"error": "Internal server error"}), 500


def clear_expired_overrides():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE zfs_snapshots
            SET manual_override = false, manual_override_reason = NULL, manual_override_end_date = NULL
            WHERE manual_override = true AND manual_override_end_date < %s
        """,
            (datetime.utcnow(),),
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error clearing expired manual overrides: {e}")


@app.route("/api/tickets", methods=["POST"])
def create_ticket():
    zammad_url = "https://zammad.grit.ucsb.edu/api/v1/tickets"
    bearer_token = "KOF2BL7oF3PxWUDWG__bgbcFDQykgdqXrUmkTaMSvdw_BT6r-aTohVIVqjeVrWge"
    data = request.json

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
    }

    try:
        response = requests.post(zammad_url, json=data, headers=headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": str(err)}), response.status_code


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

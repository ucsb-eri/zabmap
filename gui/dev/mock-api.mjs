// Fake zabmap API for local visual checks. Mirrors the JSON shapes in api/src/zabmap_api/api.py.
import http from "node:http";

const hostRows = [
  { id: 1, name: "lin101" },
  { id: 2, name: "lin113" },
  { id: 3, name: "lin114" },
  { id: 4, name: "nas-eri01" },
];
const hostById = Object.fromEntries(hostRows.map((h) => [h.id, h]));

const iso = (hoursAgo) => new Date(Date.now() - hoursAgo * 3600e3).toISOString();
const props = (extra = {}) => ({
  used: "4.2T",
  quota: "6T",
  compression: "lz4",
  recordsize: "128K",
  mountpoint: "/raid/home",
  atime: "off",
  "zab:server": "nas-eri01:/zab/lin101,nas-eri02:/zab/lin101",
  ...extra,
});

let nextId = 100;
const fs = [];
function add(hostId, path, o = {}) {
  const f = {
    id: nextId++,
    host: hostById[hostId],
    path,
    backup_parent: null,
    latest_snapshot: iso(11),
    snapshots_in_sync: null,
    disabled: null,
    zfs_properties: props({ mountpoint: path }),
    replications: 0,
    backup_type: null,
    ignore_backup_state: null,
    backups: [],
    ...o,
  };
  fs.push(f);
  return f;
}

// lin101
const home = add(1, "/raid/home", { snapshots_in_sync: true, replications: 2, backup_type: "zab" });
const proj = add(1, "/raid/projects", { snapshots_in_sync: false, replications: 3, backup_type: "zab", latest_snapshot: iso(150) });
add(1, "/raid/archive", { snapshots_in_sync: true, replications: 2, backup_type: "zas" });
add(1, "/vmz-migrated", { snapshots_in_sync: false, replications: 2, backup_type: "zab", latest_snapshot: iso(1180) });
add(1, "/raid/scratch", { ignore_backup_state: true, replications: 0, zfs_properties: props({ "zab:ignore": "rebuilt nightly" }) });
add(1, "/sandbox", { ignore_backup_state: true, replications: 0 });
add(1, "/raid/newvol", { snapshots_in_sync: null, replications: 1, backup_type: null });
add(1, "/tmp", { replications: 0 });

// lin113
add(2, "/raid/labs", { snapshots_in_sync: true, replications: 2, backup_type: "zab" });
add(2, "/raid/labs/geodesy", { snapshots_in_sync: true, replications: 2, backup_type: "zab" });
add(2, "/raid/labs/remote-sensing", { snapshots_in_sync: false, replications: 2, backup_type: "zab", latest_snapshot: iso(72) });
add(2, "/raid/genomics", { snapshots_in_sync: true, replications: 2, backup_type: "zas" });
add(2, "/raid/imagery", { snapshots_in_sync: false, replications: 2, backup_type: "zab", latest_snapshot: iso(900) });
add(2, "/staging", { ignore_backup_state: true, replications: 0 });

// lin114
add(3, "/raid/models", { snapshots_in_sync: true, replications: 2, backup_type: "zab" });
add(3, "/raid/training-data", { snapshots_in_sync: true, replications: 1, backup_type: "zab" });
add(3, "/raid/notebooks", { snapshots_in_sync: true, replications: 2, backup_type: "zab" });
add(3, "/tmp", { replications: 0 });

// nas-eri01 (backup copies)
function copy(parent, path, hoursAgo) {
  const c = add(4, path, { backup_parent: { id: parent.id }, latest_snapshot: iso(hoursAgo), snapshots_in_sync: null, backup_type: parent.backup_type });
  parent.backups.push({ id: c.id, host: hostById[4], path, latest_snapshot: c.latest_snapshot });
  return c;
}
copy(home, "/zab/lin101/raid/home", 10.5);
copy(home, "/zab/lin101/raid/home-b", 10.2);
copy(proj, "/zab/lin101/raid/projects", 140);
copy(proj, "/zab/lin101/raid/projects-b", 140);
// Give every other backed-up filesystem its copies (one short when out of sync).
fs.filter((f) => f.host.id !== 4 && f.replications > 0 && f.backups.length === 0).forEach((f) => {
  const n = f.snapshots_in_sync === false ? Math.max(f.replications - 1, 0) : f.replications;
  for (let i = 0; i < n; i++) copy(f, `/zab/${f.host.name}${f.path}${i ? "-b" : ""}`, f.snapshots_in_sync === false ? 70 : 10.4);
});

const hosts = hostRows.map((h) => {
  const list = fs.filter((f) => f.host.id === h.id);
  const rc = { r0: 0, r1: 0, r2: 0 };
  list.forEach((f) => {
    if (!f.ignore_backup_state) {
      if (f.replications === 0) rc.r0++;
      else if (f.replications === 1) rc.r1++;
      else if (f.replications === 2) rc.r2++;
    }
  });
  const inSync = list.every((f) => f.snapshots_in_sync !== false);
  return { ...h, snapshots_in_sync: inSync, filesystem_count: list.length, replication_count: rc };
});

const send = (res, body, code = 200) => {
  res.writeHead(code, {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  });
  res.end(JSON.stringify(body));
};

http
  .createServer((req, res) => {
    if (req.method === "OPTIONS") return send(res, {});
    const url = new URL(req.url, "http://x").pathname;
    let m;
    if (url === "/api/last_updated") return send(res, { id: 1, key: "last_updated", value: iso(0.25) });
    if (url === "/api/hosts") return send(res, hosts);
    if ((m = url.match(/^\/api\/hosts\/(\d+)\/filesystems$/))) return send(res, fs.filter((f) => f.host.id === +m[1]));
    if ((m = url.match(/^\/api\/filesystems\/(\d+)$/))) {
      const f = fs.find((x) => x.id === +m[1]);
      return f ? send(res, f) : send(res, { error: "not found" }, 404);
    }
    send(res, { error: "not found" }, 404);
  })
  .listen(5050, () => console.log("mock api on 5050"));

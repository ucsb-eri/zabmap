// Single source of truth for how each backup status looks and what it means.
// Used by the host list, the filesystem list and the legend, so they cannot
// drift apart. Status is always shown as a label as well as a colour.

export const STATUS = {
  synced: {
    label: "In sync",
    pill: "bg-green-100 text-green-800",
    dot: "bg-green-600",
    description:
      "All expected backups exist and their latest snapshots are within a day of this filesystem's.",
  },
  unsynced: {
    label: "Out of sync",
    pill: "bg-red-100 text-red-800",
    dot: "bg-red-600",
    description:
      "A backup is missing, or its latest snapshot is more than a day behind.",
  },
  none: {
    label: "No backups",
    pill: "bg-slate-100 text-slate-600",
    dot: "bg-slate-400",
    description: "No backup servers are configured for this filesystem.",
  },
  ignored: {
    label: "Ignored",
    pill: "bg-slate-200 text-slate-700",
    dot: "bg-slate-500",
    description: "Excluded from backup checks.",
  },
  copy: {
    label: "Backup copy",
    pill: "bg-blue-100 text-blue-800",
    dot: "bg-blue-600",
    description: "This filesystem is itself a backup of another filesystem.",
  },
  unknown: {
    label: "Not checked",
    pill: "bg-slate-100 text-slate-600",
    dot: "bg-slate-400",
    description: "The status has not been calculated yet.",
  },
};

// Same precedence the list used before: ignored, then backup copy, then sync state.
export function filesystemStatus(filesystem) {
  if (filesystem.ignore_backup_state != null) return "ignored";
  if (filesystem.backup_parent != null) return "copy";
  if (filesystem.snapshots_in_sync == null) return "none";
  return filesystem.snapshots_in_sync ? "synced" : "unsynced";
}

export function hostStatus(host) {
  if (host.snapshots_in_sync == null) return "unknown";
  return host.snapshots_in_sync ? "synced" : "unsynced";
}

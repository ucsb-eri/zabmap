<script setup>
import { useRoute } from "vue-router";
import StatusPill from "@/components/StatusPill.vue";
import { filesystemStatus } from "@/config/statusConfig";

defineProps(["filesystems"]);
const emit = defineEmits(["filesystemSelected"]);

// The open filesystem is in the URL, so the list can highlight it without
// FilesystemsView having to pass anything down.
const route = useRoute();

function isSelected(filesystem) {
  return String(filesystem.id) === String(route.params.filesystemId);
}

function nrOfChildren(filesystem) {
  if (!filesystem.backups) {
    return 0;
  }
  return filesystem.backups.length;
}

// "Backups 1 of 2" only makes sense for filesystems that are expected to have
// backups, so hide it for ignored filesystems, backup copies and unbacked ones.
function showBackupCount(filesystem) {
  return (
    filesystem.replications > 0 &&
    !["ignored", "copy"].includes(filesystemStatus(filesystem))
  );
}
</script>

<template>
  <ul class="divide-y divide-slate-200">
    <li v-for="filesystem in filesystems" :key="filesystem.id">
      <button
        type="button"
        class="block w-full cursor-pointer px-4 py-3 text-left hover:bg-slate-50 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-blue-600"
        :class="isSelected(filesystem) ? 'bg-blue-50 hover:bg-blue-50' : ''"
        :aria-current="isSelected(filesystem) ? 'true' : undefined"
        @click="emit('filesystemSelected', filesystem.id)"
      >
        <div class="flex items-center gap-2">
          <span
            class="min-w-0 grow break-all font-mono text-sm"
            :class="isSelected(filesystem) ? 'font-semibold' : 'font-medium'"
            >{{ filesystem.path }}</span
          >
          <span
            v-if="filesystem.backup_type"
            class="rounded border border-slate-200 px-1.5 font-mono text-xs text-slate-500"
            >{{ filesystem.backup_type }}</span
          >
          <StatusPill :status="filesystemStatus(filesystem)" />
        </div>
        <div v-if="showBackupCount(filesystem)" class="mt-1 text-xs">
          <span
            :class="
              nrOfChildren(filesystem) < filesystem.replications
                ? 'font-medium text-amber-700'
                : 'text-slate-500'
            "
            >Backups {{ nrOfChildren(filesystem) }} of
            {{ filesystem.replications }}</span
          >
        </div>
      </button>
    </li>
  </ul>
</template>

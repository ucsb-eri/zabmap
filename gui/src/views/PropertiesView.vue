<script setup>
import { useAuthedFetch } from "@/auth/authedFetch";
import StatusPill from "@/components/StatusPill.vue";
import { filesystemStatus } from "@/config/statusConfig";
import { ref, toRef, watch } from "vue";
const props = defineProps({
  hostId: String,
  filesystemId: String,
});

const filesystemId = toRef(props, "filesystemId");

const url = ref(
  `${import.meta.env.VITE_API_URL}/api/filesystems/${filesystemId.value}`,
);
watch(filesystemId, () => {
  url.value = `${import.meta.env.VITE_API_URL}/api/filesystems/${filesystemId.value}`;
});

const {
  isFetching,
  error,
  data: filesystem,
} = await useAuthedFetch(url, { initialData: { results: [] }, refetch: true })
  .get()
  .json();

// A backup copy links back to the filesystem it is a backup of. The parent is
// loaded whenever the open filesystem changes (the component is reused when you
// click from one filesystem to another).
const parentUrl = ref("");
const { data: parent, execute: loadParent } = useAuthedFetch(parentUrl, {
  immediate: false,
})
  .get()
  .json();

watch(
  () => filesystem.value?.backup_parent?.id,
  (parentId) => {
    parent.value = null;
    if (!parentId) return;
    parentUrl.value = `${import.meta.env.VITE_API_URL}/api/filesystems/${parentId}`;
    loadParent();
  },
  { immediate: true },
);

function formatDate(value) {
  if (!value) return "none";
  return new Date(value).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

const link = "text-blue-700 hover:underline";
const th =
  "whitespace-nowrap py-2 pr-4 text-left text-xs font-medium uppercase tracking-wide text-slate-500";
</script>

<template>
  <div class="text-left">
    <div class="sticky-header">
      <h1 class="break-all font-mono">{{ filesystem.path }}</h1>
      <div class="flex flex-wrap items-center gap-2 text-sm text-slate-500">
        <StatusPill :status="filesystemStatus(filesystem)" />
        <span v-if="filesystem.host?.name">on {{ filesystem.host.name }}</span>
      </div>
    </div>

    <div class="grid gap-6 p-4">
      <section v-if="filesystem.backup_parent">
        <h2 class="mb-2">Backup of</h2>
        <RouterLink
          v-if="parent?.id"
          :class="['break-all font-mono text-sm', link]"
          :to="`/hosts/${parent.host?.id}/filesystems/${parent.id}`"
          >{{ parent.host?.name }}:{{ parent.path }}</RouterLink
        >
        <span v-else class="text-sm text-slate-500">Loading…</span>
      </section>

      <section>
        <h2 class="mb-2">Backups</h2>
        <div class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr>
                <th :class="th">Location</th>
                <th :class="th">Latest snapshot</th>
              </tr>
            </thead>
            <tbody>
              <tr class="border-t border-slate-100">
                <td class="py-2 pr-4">Local</td>
                <td class="whitespace-nowrap py-2">
                  {{ formatDate(filesystem.latest_snapshot) }}
                </td>
              </tr>
              <tr
                v-for="backup in filesystem.backups"
                :key="backup.id"
                class="border-t border-slate-100"
              >
                <td class="py-2 pr-4">
                  <RouterLink
                    :class="['break-all font-mono', link]"
                    :to="`/hosts/${backup.host.id}/filesystems/${backup.id}`"
                    >{{ backup.host.name }}:{{ backup.path }}</RouterLink
                  >
                </td>
                <td class="whitespace-nowrap py-2">
                  {{ formatDate(backup.latest_snapshot) }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section>
        <h2 class="mb-2">Important ZFS properties</h2>
        <div class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr>
                <th :class="th">Property</th>
                <th :class="th">Value</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(value, key) in filesystem.zfs_properties"
                :key="key"
                class="border-t border-slate-100"
              >
                <td class="py-2 pr-4 font-mono text-slate-500">{{ key }}</td>
                <td class="break-all py-2 font-mono">{{ value }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  </div>
</template>

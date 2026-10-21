<script setup>
import router from "@/router";
import HostsView from "@/views/HostsView.vue";
import FilesystemsList from "@/components/FilesystemsList.vue";
import TooltipLegend from "@/components/TooltipLegend.vue";
import { useAuthedFetch } from "@/auth/authedFetch";
import { ref, watch, toRef } from "vue";

const filesystemFilter = defineModel();

const props = defineProps({
  hostId: String,
});

const hostId = toRef(props, "hostId");

const url = ref(
  `${import.meta.env.VITE_API_URL}/api/hosts/${hostId.value}/filesystems`,
);
watch(hostId, (newVal, oldVal) => {
  url.value = `${import.meta.env.VITE_API_URL}/api/hosts/${hostId.value}/filesystems`;
});

const {
  isFetching,
  error,
  data: filesystems,
} = await useAuthedFetch(url, { initialData: { results: [] }, refetch: true })
  .get()
  .json();

// NEW (Edit A): issue #5. Filesystems that don't specify any backups
// (replications === 0) are hidden unless the checkbox is ticked.
const showWithoutBackups = ref(false);

function hasNoBackups(filesystem) {
  return !filesystem.replications;
}

// CHANGED (Edit A): the filter now also checks the checkbox.
function filteredFilesystems(filesystems) {
  filesystems.sort((a, b) => a.path.localeCompare(b.path));
  const filterText = filesystemFilter.value ?? "";

  return filesystems.filter(
    (filesystem) =>
      filesystem["path"].toLowerCase().includes(filterText.toLowerCase()) &&
      (showWithoutBackups.value || !hasNoBackups(filesystem)),
  );
}

// NEW (Edit A): how many rows the checkbox is currently hiding.
function hiddenCount(filesystems) {
  return showWithoutBackups.value
    ? 0
    : filesystems.filter(hasNoBackups).length;
}

function handleFilesystemSelected(filesystemId) {
  router.push(`/hosts/${hostId.value}/filesystems/${filesystemId}`);
}
</script>

<template>
  <div>
    <div class="sticky-header">
      <h1>Filesystems for {{ filesystems[0].host.name }}</h1>
      <input
        type="text"
        placeholder="Search filesystems..."
        v-model="filesystemFilter"
      />
      <!-- NEW (Edit B): the checkbox -->
      <label class="flex items-center justify-center gap-2 mt-2 text-sm">
        <input type="checkbox" v-model="showWithoutBackups" />
        Show filesystems without backups
        <span v-if="hiddenCount(filesystems)" class="text-gray-500">
          ({{ hiddenCount(filesystems) }} hidden)
        </span>
      </label>
    </div>
    <!-- NEW (Edit C): message when nothing is left to show -->
    <p
      v-if="filteredFilesystems(filesystems).length === 0"
      class="mt-4 text-gray-500"
    >
      No filesystems to show.
    </p>
    <FilesystemsList
      :filesystems=filteredFilesystems(filesystems)
      @filesystemSelected="handleFilesystemSelected"
    />
  </div>
  <TooltipLegend />
</template>

<script setup>
import router from "@/router";
import HostsView from "@/views/HostsView.vue";
import FilesystemsList from "@/components/FilesystemsList.vue";
import TooltipLegend from "@/components/TooltipLegend.vue";
import { useFetch } from "@vueuse/core";
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
  console.log(newVal);
  console.log(oldVal);
});

const {
  isFetching,
  error,
  data: filesystems,
} = await useFetch(url, { initialData: { results: [] }, refetch: true })
  .get()
  .json();

function handleFilesystemSelected(filesystemId) {
  router.push(`/hosts/${hostId.value}/filesystems/${filesystemId}`);
}
</script>

<template>
  <div>
    <div class="sticky-header">
      <h2>Filesystems for {{ filesystems[0].host.name }}</h2>
      <input
        type="text"
        placeholder="Search filesystems..."
        v-model="filesystemFilter"
      />
    </div>
    <FilesystemsList
      :filesystems
      @filesystemSelected="handleFilesystemSelected"
    />
  </div>
  <TooltipLegend />
</template>

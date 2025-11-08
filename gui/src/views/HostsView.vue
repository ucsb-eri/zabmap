<script setup>
import router from '@/router'
import HostsList from '@/components/HostsList.vue';
import { useFetch } from "@vueuse/core";

const hostFilter = defineModel()

const props = defineProps({
  selectedHostId: String,
});

const {
  isFetching,
  error,
  data: hosts,
} = await useFetch(`${import.meta.env.VITE_API_URL}/api/hosts`, {
  initialData: { results: [] },
})
  .get()
  .json();

function filteredHosts(hosts) {
  hosts.sort((a, b) => a.name.localeCompare(b.name));
  const filterText = hostFilter.value ?? "";

  return hosts.filter((host) =>
    host["name"].toLowerCase().includes(filterText.toLowerCase()),
  );
}

function handleHostSelected(hostId) {
	router.push(`/hosts/${hostId}/filesystems`)
}
</script>

<template>
  <div>
    <div class="flex flex-col">
      <div class="sticky-header">
        <h1>Hosts</h1>
        <input type="text" placeholder="Search hosts..." v-model="hostFilter" />
      </div>
      <HostsList :hosts="filteredHosts(hosts)" :selectedHostId="selectedHostId" @hostSelected="handleHostSelected" />
    </div>
  </div>
</template>

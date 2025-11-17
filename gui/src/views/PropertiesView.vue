<script setup>
import { useFetch } from "@vueuse/core";
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
} = await useFetch(url, { initialData: { results: [] }, refetch: true })
  .get()
  .json();
</script>

<template>
  <div>
    <h1>Info for {{ filesystem.path }}</h1>

    <h2>Backups</h2>
    <div class="grow">
      <table
        class="w-full table-auto border border-separate border-gray-400 dark:border-gray-500"
      >
        <thead>
          <tr>
            <th>Location</th>
            <th>Latest Snapshot</th>
          </tr>
        </thead>
        <tbody>
					<tr><td>local</td><td>{{ filesystem.latest_snapshot }}</td></tr>
          <tr v-for="backup in filesystem.backups">
            <td>
              <RouterLink
                :class="[
                  'font-medium',
                  'text-fg-brand',
                  'hover:underline',
                  'text-blue-700',
                ]"
                :to="`/hosts/${backup.host.id}/filesystems/${backup.id}`"
                >{{ backup.host.name }}:{{ backup.path }}</RouterLink
              >
            </td>
            <td>{{ backup.latest_snapshot }}</td>
          </tr>
        </tbody>
      </table>
    </div>
		<br />
    <h2>Important zfs properties</h2>
    <div>
      <table
        class="w-full table-auto border border-separate border-gray-400 dark:border-gray-500"
      >
        <thead>
          <tr>
            <th>Property</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in filesystem.zfs_properties">
						<td class="text-left me-8">{{ key }}</td>
						<td class="text-left">{{ value }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
/* Add any styles specific to this component */
</style>

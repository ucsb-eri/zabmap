<script setup>
import { useFetch } from "@vueuse/core";
import { ref, toRef, watch } from "vue";
const props = defineProps({
  hostId: String,
  filesystemId: String,
});

const filesystemId = toRef(props, "filesystemId");
const parentId = toRef(props, "parentId");

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

if(filesystem?.value?.backup_parent?.id){
let parentUrl = `${import.meta.env.VITE_API_URL}/api/filesystems/${filesystem?.value?.backup_parent?.id}`;

const {
  isFetching: parentFetching,
  error: parentError,
  data: parent,
} = await useFetch(parentUrl, { initialData: { results: [] }, refetch: true })
  .get()
  .json();
}
// async function getHostId(filesystem) {
//   const url = `${import.meta.env.VITE_API_URL}/api/filesystems/${filesystem.id}`;
// const {
//   isFetching,
//   error,
//   data,
// } = await useFetch(url, { initialData: { results: [] }, refetch: true })
//   .get()
//   .json();
//    	console.log(data)
// }
//
// const hostId = ref<string>('')
// onMounted(async() => {
//   hostId.value = await getHostId()
// })
</script>

<template>
  <div>
    <h1 class="text-left">Info for {{ filesystem.path }}</h1>
    <div v-if="filesystem && filesystem.backup_parent">
      <h2 class="text-left">Parent</h2>
      {{ filesystem.backup_parent_id }}
      <RouterLink
        :class="[
          'font-medium',
          'text-fg-brand',
          'hover:underline',
          'text-blue-700',
        ]"
        :to="`/hosts/${parent?.host?.id}/filesystems/${parent?.id}`"
        >{{ parent?.host?.name }}:{{ parent?.path }}</RouterLink
      >
    </div>
    <h2 class="text-left">Backups</h2>
    <div class="grow">
      <table
        class="w-full table-auto border border-separate border-gray-400 dark:border-gray-500"
      >
        <thead>
          <tr>
            <th class="text-left">Location</th>
            <th class="text-left">Latest Snapshot</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="text-left pe-8">local</td>
            <td class="text-left">{{ filesystem.latest_snapshot }}</td>
          </tr>
          <tr v-for="backup in filesystem.backups">
            <td class="text-left pe-8">
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
            <td class="text-left">{{ backup.latest_snapshot }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <br />
    <h2 class="text-left">Important zfs properties</h2>
    <div>
      <table
        class="w-full table-auto border border-separate border-gray-400 dark:border-gray-500"
      >
        <thead>
          <tr>
            <th class="text-left">Property</th>
            <th class="text-left">Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in filesystem.zfs_properties">
            <td class="text-left pe-8">{{ key }}</td>
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

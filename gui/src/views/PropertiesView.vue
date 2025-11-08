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

// function filesystemTranspose(filesystem) {
//   return filesystem.replace("-", "/");
// }
</script>

<template>
  <div>
    <h2>Properties for {{ filesystem }}</h2>
  </div>
</template>

<style scoped>
/* Add any styles specific to this component */
</style>

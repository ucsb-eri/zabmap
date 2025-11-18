<script setup>
import { useFetch } from "@vueuse/core";
import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'
TimeAgo.addDefaultLocale(en)
const timeAgo = new TimeAgo('en-US')

const { isFetching, error, data } = await useFetch(
  `${import.meta.env.VITE_API_URL}/api/last_updated`,
  {
    initialData: { results: [] },
  },
)
  .get()
  .json();

</script>

<template>
	<div>Last updated: {{ timeAgo.format(new Date(data.value)) }}</div>
</template>

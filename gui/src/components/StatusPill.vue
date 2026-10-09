<script setup>
import { STATUS } from "@/config/statusConfig";

defineProps({
  status: { type: String, required: true },
});
</script>

<template>
  <span
    class="inline-flex items-center gap-1.5 whitespace-nowrap rounded-full px-2 py-0.5 text-xs font-medium"
    :class="STATUS[status].pill"
  >
    <span class="size-1.5 rounded-full" :class="STATUS[status].dot"></span>
    {{ STATUS[status].label }}
  </span>
</template>

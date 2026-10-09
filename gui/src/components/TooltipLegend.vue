<script>
import StatusPill from "@/components/StatusPill.vue";
import { STATUS } from "@/config/statusConfig";

export default {
  components: { StatusPill },
  data() {
    return {
      hovering: false,
      pinned: false,
      STATUS,
      // The statuses a filesystem can have, in the order they are explained.
      order: ["synced", "unsynced", "none", "ignored", "copy"],
    };
  },
  computed: {
    open() {
      return this.hovering || this.pinned;
    },
  },
  methods: {
    togglePinned() {
      this.pinned = !this.pinned;
    },
  },
};
</script>

<template>
  <div
    class="fixed bottom-4 right-4 z-50"
    @mouseenter="hovering = true"
    @mouseleave="hovering = false"
  >
    <div v-if="open" class="absolute bottom-full right-0 pb-2">
      <div
        class="w-80 max-w-[90vw] rounded-lg border border-slate-200 bg-white p-4 text-left shadow-lg"
      >
        <h2 class="mb-3">Status legend</h2>
        <dl class="grid gap-3">
          <div v-for="key in order" :key="key">
            <dt><StatusPill :status="key" /></dt>
            <dd class="mt-1 text-sm text-slate-600">
              {{ STATUS[key].description }}
            </dd>
          </div>
        </dl>
      </div>
    </div>
    <button
      type="button"
      aria-label="Status legend"
      :aria-expanded="open"
      class="size-10 cursor-pointer rounded-full bg-blue-600 text-lg font-semibold text-white shadow-md hover:bg-blue-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
      @click="togglePinned"
    >
      ?
    </button>
  </div>
</template>

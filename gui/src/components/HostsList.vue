<script setup>
import StatusPill from "@/components/StatusPill.vue";
import { hostStatus } from "@/config/statusConfig";

// hostId is the host currently open in the URL (HostsView already passes it).
const props = defineProps(["hosts", "hostId"]);
const emit = defineEmits(["hostSelected"]);

function isSelected(host) {
  return String(host.id) === String(props.hostId);
}

// replication_count looks like { r0: 1, r1: 1, r2: 3 }: how many filesystems
// have 0, 1 or 2 backup copies. Spell it out instead of showing r0=1 r1=1 r2=3.
// "0 copies" is deliberately neutral: a backup server's own filesystems have 0.
function copiesSummary(host) {
  const counts = host.replication_count ?? {};
  const parts = [];
  if (counts.r2) parts.push(`${counts.r2} with 2 copies`);
  if (counts.r1) parts.push(`${counts.r1} with 1 copy`);
  if (counts.r0) parts.push(`${counts.r0} with 0 copies`);
  return parts.join(" · ");
}
</script>

<template>
  <ul class="divide-y divide-slate-200">
    <li v-for="host in hosts" :key="host.id">
      <button
        type="button"
        class="block w-full cursor-pointer px-4 py-3 text-left hover:bg-slate-50 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-blue-600"
        :class="isSelected(host) ? 'bg-blue-50 hover:bg-blue-50' : ''"
        :aria-current="isSelected(host) ? 'true' : undefined"
        @click="emit('hostSelected', host.id)"
      >
        <div class="flex items-center gap-2">
          <span
            class="min-w-0 grow break-all font-mono text-sm"
            :class="isSelected(host) ? 'font-semibold' : 'font-medium'"
            >{{ host.name }}</span
          >
          <StatusPill :status="hostStatus(host)" />
        </div>
        <div class="mt-1 text-xs text-slate-500">
          <span v-if="host.filesystem_count"
            >{{ host.filesystem_count }} filesystems</span
          >
          <div v-if="copiesSummary(host)">{{ copiesSummary(host) }}</div>
        </div>
      </button>
    </li>
  </ul>
</template>

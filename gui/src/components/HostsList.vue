<script setup>
import { ref, watch, toRef } from "vue";

const props = defineProps(["hosts", "selectedHostId"]);
const emit = defineEmits(["hostSelected"]);

const hosts = toRef(props, "hosts");
const selectedHostId = toRef(props, "selectedHostId");

watch(selectedHostId, (newVal, oldVal) => {
  hosts.value = selectedHostId.value
    ? props.hosts.filter((el) => el.id == selectedHostId)
    : props.hosts;
});

function inSyncClass(host) {
  return host.snapshots_in_sync ? "green-button" : "red-button";
}
</script>

<template>
  <div>
    <ul>
      <li v-for="host in hosts" :key="host">
        <button
          :class="['host-button', inSyncClass(host)]"
          @click="emit('hostSelected', host.id)"
        >
          <div :class="['flex', 'flex-row']">
            <div class="filesystem-name">{{ host.name }}</div>
            <div :class="['flex', 'flex-row-reverse', 'grow']">
              <!-- <div> -->
              <span :class="['flex-initial', 'min-w-[150px]', 'text-right']">
                <span
                  class="inline-flex items-center rounded-md bg-gray-600/10 px-2 py-1 text-xs font-medium text-black inset-ring inset-ring-gray-400/20"
                >
                  <span
                    class="font-mono"
                    v-for="(value, key) in host.replication_count"
                  >
                    {{ key }}={{ value }}&nbsp;
                    <!-- {{ /* getLabelClass(fs).toUpperCase() }} -->
                  </span>
                </span>
              </span>
              <span
                :class="['font-mono', 'min-w-20']"
                v-if="host.filesystem_count"
              >
                <span
                  class="inline-flex items-center rounded-md bg-gray-600/10 px-2 py-1 text-xs font-medium text-black inset-ring inset-ring-gray-400/20"
                  >fs: {{ host.filesystem_count }}</span
                >
              </span>
              <!-- </div> -->
            </div>
          </div>
        </button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.host-button {
  display: block;
  margin: 5px 0;
  padding: 10px;
  width: 100%;
  text-align: left;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  cursor: pointer;
  transition: background-color 0.3s;
}

.host-button:hover {
  background-color: #f0f0f0;
}

.host-button:focus {
  outline: none;
  border-color: #007bff;
}

.green-button {
  background-color: #ccffcc;
}
.red-button {
  background-color: #ffcccc;
}

.yellow-button {
  background-color: yellow;
  color: black;
}

.selected-host {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}
</style>

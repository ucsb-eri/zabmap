<script setup>
import Loader from "@/components/Loader.vue";

const props = defineProps(["hosts", "selectedHostId"]);
const emit = defineEmits(["hostSelected"]);

const hosts = props.selectedHostId
  ? props.hosts.filter((el) => el.id == props.selectedHostId)
  : props.hosts;
function inSyncClass(inSync) {
  return inSync ? "in-sync" : "out-of-sync";
}
</script>

<template>
  <div>
    <ul>
      <li v-for="host in hosts" :key="host">
        <button
          :class="['host-button', inSyncClass(host.backups_in_sync)]"
          @click="emit('hostSelected', host.id)"
        >
          {{ host.name }}
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

.out-of-sync {
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

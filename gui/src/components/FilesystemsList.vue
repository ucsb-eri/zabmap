<script setup>
import { toRef } from "vue";

const props = defineProps(["filesystems"]);
const filesystems = toRef(props, "filesystems");

const filesystemFilter = defineModel();

const emit = defineEmits(["filesystemSelected"]);

function nrOfChildren(filesystem) {
  if (!filesystem.backups) {
    return 0;
  }
  return filesystem.backups.length;
}

function inSyncClass(filesystem) {
  if (filesystem.backup_parent != null) {
	   return "bg-blue-200"
	}
  if (filesystem.snapshots_in_sync === null) {
    return "";
  } else if (filesystem.snapshots_in_sync === true) {
    return "bg-green-200";
  } else {
    return 'bg-red-200';
  }
}
</script>

<template>
  <div>
    <ul>
      <li v-for="filesystem in filesystems" :key="filesystem.id">
        <button
          @click="emit('filesystemSelected', filesystem.id)"
          :class="[
            'filesystem-button',
            inSyncClass(filesystem) /* getButtonClass(fs) */,
          ]"
        >
          <div :class="['flex', 'flex-row']">
            <div class="filesystem-name">{{ filesystem.path }}</div>
            <div :class="['font-mono', 'min-w-20']">
              <span
                v-if="filesystem.ignore"
                class="inline-flex items-center rounded-md bg-gray-600/10 px-2 py-1 text-xs font-medium text-black inset-ring inset-ring-gray-400/20"
                >ignored</span
              >
            </div>
            <div :class="['font-mono', 'min-w-20']">
              <span
                v-if="filesystem.backup_type"
                class="inline-flex items-center rounded-md bg-gray-600/10 px-2 py-1 text-xs font-medium text-black inset-ring inset-ring-gray-400/20"
                >{{ filesystem.backup_type }}</span
              >
            </div>
            <div :class="['font-mono', 'min-w-[110px]', 'text-right']">
              <span
                class="inline-flex items-center rounded-md bg-gray-600/10 px-2 py-1 text-xs font-medium text-black inset-ring inset-ring-gray-400/20"
              >
                backups: {{ nrOfChildren(filesystem) }}/{{
                  filesystem.replications
                }}</span
              >
            </div>
          </div>
          <!-- <span v-if="isBillable(fs)" class="label">$</span> -->
        </button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.filesystem-button {
  display: block;
  justify-content: space-between;
  align-items: center;
  margin: 5px 0;
  padding: 10px;
  width: 100%;
  text-align: left;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.filesystem-button:hover {
  background-color: #f0f0f0;
}

.filesystem-button:focus {
  outline: none;
  border-color: #007bff;
}

.red-button {
  background-color: #ffcccc;
}

.yellow-button {
  background-color: yellow;
  color: black;
}

.green-button {
  background-color: #ccffcc;
}

.orange-button {
  background-color: #ffa500;
}

.filesystem-name {
  flex-grow: 1;
}

.label {
  margin-left: 10px;
}

.zas {
  color: blue;
}

.zab {
  color: green;
}

.sticky-header {
  position: sticky;
  top: 0;
  background-color: white;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  z-index: 10;
}
</style>

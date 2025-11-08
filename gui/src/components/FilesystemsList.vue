<script setup>
import { toRef } from 'vue';

const props = defineProps(["filesystems"]);
const filesystems = toRef(props, 'filesystems');

const filesystemFilter = defineModel();


const emit = defineEmits(["filesystemSelected"]);


function selectFilesystem(fs) {
  ;
}

// function getButtonClass(fs) {
//   if (noSpecialClassFilesystems.some(path => fs.filesystem.includes(path)) || exactMatchFilesystems.includes(fs.filesystem)) {
//     return ''; // No special class for these filesystems
//   }
//   if (fs.manual_override) {
//     const currentDate = new Date();
//     const endDate = new Date(fs.manual_override_end_date);
//
//     if (currentDate > endDate) {
//       // Manual override has expired
//       fs.manual_override = false;
//       fs.manual_override_end_date = null;
//       this.clearExpiredOverride(fs); // Clear the override in the database
//       return this.getColorClass(fs);
//     } else {
//       return 'orange-button';
//     }
//   }
//   return this.getColorClass(fs);
// }
//
// function getLabelClass(fs) {
//   if (!fs.most_recent_snapshot) {
//     return ""; // No label if there's no snapshot
//   }
//   const snapshotName = fs.most_recent_snapshot.toLowerCase();
//   if (snapshotName.includes("zas")) {
//     return "zas";
//   }
//   return "zab";
// }
// isBillable(fs) {
//   const billableValue = fs.properties && (fs.properties['grit:billable'] === 'true' || fs.properties['grit:billable'] === 'yes');
//   return billableValue;
// }
//
</script>

<template>
  <div>
    <ul>
      <li v-for="filesystem in filesystems" :key="filesystem.id">
        <button
          @click="emit('filesystemSelected', filesystem.id)"
          :class="['filesystem-button' /* getButtonClass(fs) */]"
        >
          <span class="filesystem-name">{{ filesystem.path }}</span>
          <span
            :class="[
              /* getLabelClass(fs) */
            ]"
            class="label"
          >
            <!-- {{ /* getLabelClass(fs).toUpperCase() }} -->
          </span>
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
  background-color: #f9f9f9;
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


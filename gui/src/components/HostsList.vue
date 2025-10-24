<template>
  <div>
    <ul>
      <li v-for="host in filteredHosts" :key="host">
        <button :class="['host-button', getHostButtonClass(host)]" @click="selectHost(host)">
          {{ host }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import { noSpecialClassFilesystems, exactMatchFilesystems } from '@/config/filesystemConfig';

export default {
  props: ['filterText'],
  data() {
    return {
      hosts: [],
      filesystemsByHost: {}, // Store filesystems per host
    };
  },
  computed: {
    filteredHosts() {
      return this.hosts.filter(host =>
        host.toLowerCase().includes(this.filterText.toLowerCase())
      );
    }
  },
  mounted() {
    this.fetchHosts();
  },
  methods: {
    async fetchHosts() {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/hosts`);
        this.hosts = response.data;

        // Fetch filesystems for each host to determine their status
        for (const host of this.hosts) {
          await this.fetchFilesystems(host);
        }
      } catch (error) {
        console.error('Error fetching hosts:', error);
      }
    },
    async fetchFilesystems(host) {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/hosts/${host}/filesystems`);
        this.filesystemsByHost[host] = response.data;
      } catch (error) {
        console.error(`Error fetching filesystems for host ${host}:`, error);
      }
    },
    selectHost(host) {
      this.$emit('hostSelected', host);
    },
//start
getHostButtonClass(host) {
  const filesystems = this.filesystemsByHost[host] || [];
  let hasRed = false;
  let hasYellow = false;

  for (const fs of filesystems) {
    if (noSpecialClassFilesystems.some(path => fs.name.includes(path)) || exactMatchFilesystems.includes(fs.name)) {
      continue; // Skip these filesystems
    }

    if (!fs.most_recent_snapshot) {
      hasRed = true;
      break;
    }

    const snapshotDateMatch = fs.most_recent_snapshot.match(/zas_[hd]-(\d{8})-/);
    let snapshotDate = null;

    if (snapshotDateMatch) {
      snapshotDate = snapshotDateMatch[1];
    } else {
      const dateMatch = fs.most_recent_snapshot.match(/-(\d{8})/);
      if (dateMatch) {
        snapshotDate = dateMatch[1];
      }
    }

    if (snapshotDate) {
      const snapshotDateObj = new Date(
        snapshotDate.slice(0, 4),
        snapshotDate.slice(4, 6) - 1,
        snapshotDate.slice(6, 8)
      );
      const timeDiff = Math.abs(new Date() - snapshotDateObj);
      const diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

      if (diffDays > 30) {
        hasRed = true;
        break;
      } else if (diffDays > 1) {
        hasYellow = true;
      }
    }
  }

  if (hasRed) {
    return 'red-button';
  } else if (hasYellow) {
    return 'yellow-button';
  } else {
    return '';
  }
}

//end
  }
}
</script>

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


<template>
  <div>
    <ul>
      <li v-for="fs in filteredFilesystems" :key="fs.name">
        <button
          @click="selectFilesystem(fs.name)"
          :class="['filesystem-button', getButtonClass(fs)]"
        >
          <span class="filesystem-name">{{ fs.name }}</span>
          <span :class="[getLabelClass(fs)]" class="label">
            {{ getLabelClass(fs).toUpperCase() }}
          </span>
          <span v-if="isBillable(fs)" class="label">$</span>
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import { noSpecialClassFilesystems, exactMatchFilesystems } from '@/config/filesystemConfig';

export default {
  props: ['host', 'filter'],
  data() {
    return {
      filesystems: [],
      localFilter: this.filter
    };
  },
  computed: {
    filteredFilesystems() {
      return this.filesystems.filter(fs =>
        fs.name.toLowerCase().includes(this.localFilter.toLowerCase())
      );
    }
  },
  watch: {
    host(newHost) {
      if (newHost) {
        this.fetchFilesystems(newHost);
      }
    },
    filter(newFilter) {
      this.localFilter = newFilter; // Sync local filter with parent filter
    }
  },
  mounted() {
    if (this.host) {
      this.fetchFilesystems(this.host);
    }
  },
  methods: {
    async fetchFilesystems(host) {
      try {
        console.log(`Fetching filesystems for host: ${host}`);
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/hosts/${host}/filesystems`);
        console.log('Filesystems fetched:', response.data);
        this.filesystems = response.data;
      } catch (error) {
        console.error('Error fetching filesystems:', error);
      }
    },
    selectFilesystem(fs) {
      console.log('Filesystem selected:', fs);
      this.$emit('filesystemSelected', fs);
    },
    async clearExpiredOverride(fs) {
      try {
        const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/hosts/${this.host}/filesystems/${fs.name}/clear_override`);
        console.log('Override cleared successfully:', response.data);
      } catch (error) {
        console.error('Error clearing override:', error);
      }
    },
    getButtonClass(fs) {
      if (noSpecialClassFilesystems.some(path => fs.name.includes(path)) || exactMatchFilesystems.includes(fs.name)) {
        return ''; // No special class for these filesystems
      }
      if (fs.manual_override) {
        const currentDate = new Date();
        const endDate = new Date(fs.manual_override_end_date);

        if (currentDate > endDate) {
          // Manual override has expired
          fs.manual_override = false;
          fs.manual_override_end_date = null;
          this.clearExpiredOverride(fs); // Clear the override in the database
          return this.getColorClass(fs);
        } else {
          return 'orange-button';
        }
      }
      return this.getColorClass(fs);
    },
    getColorClass(fs) {
      if (!fs.most_recent_snapshot) {
        return 'red-button';
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
        const today = new Date().toISOString().slice(0, 10).replace(/-/g, '');
        const snapshotDateObj = new Date(
          snapshotDate.slice(0, 4),
          snapshotDate.slice(4, 6) - 1,
          snapshotDate.slice(6, 8)
        );
        const timeDiff = Math.abs(new Date() - snapshotDateObj);
        const diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

        if (snapshotDate === today) {
          return 'green-button';
        } else if (diffDays > 30) {
          return 'red-button';
        } else {
          return 'yellow-button';
        }
      }
      return '';
    },
    getLabelClass(fs) {
      if (!fs.most_recent_snapshot) {
        return ''; // No label if there's no snapshot
      }
      const snapshotName = fs.most_recent_snapshot.toLowerCase();
      if (snapshotName.includes('zas')) {
        return 'zas';
      }
      return 'zab';
    },
    isBillable(fs) {
      const billableValue = fs.properties && (fs.properties['grit:billable'] === 'true' || fs.properties['grit:billable'] === 'yes');
      return billableValue;
    }
  }
}
</script>

<style scoped>
.filesystem-button {
  display: flex;
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


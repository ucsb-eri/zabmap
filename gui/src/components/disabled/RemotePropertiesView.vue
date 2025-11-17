<template>
  <div v-if="remoteProperties">
    <h2>Remote Properties for {{ remoteFilesystem }}</h2>
    <ul>
      <li>Most Recent Snapshot: {{ remoteProperties.most_recent_snapshot }}</li>
      <li v-for="(value, key) in remoteProperties.properties" :key="key">
        {{ key }}: {{ value }}
      </li>
      <li>Timestamp: {{ remoteProperties.timestamp }}</li>
    </ul>
  </div>
  <div v-else>
    <p>No remote properties available for the selected filesystem.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['remoteHost', 'remoteFilesystem'],
  data() {
    return {
      remoteProperties: null,
      errorMessage: null,
    };
  },
  watch: {
    remoteFilesystem(newFs) {
      if (newFs) {
        this.fetchRemoteProperties(this.remoteHost, newFs);
      }
    }
  },
  mounted() {
    if (this.remoteHost && this.remoteFilesystem) {
      this.fetchRemoteProperties(this.remoteHost, this.remoteFilesystem);
    }
  },
  methods: {
    async fetchRemoteProperties(remoteHost, remoteFilesystem) {
      try {
				const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/hosts/${remoteHost}/filesystems/${remoteFilesystem}/properties`);
        this.remoteProperties = response.data;
        this.errorMessage = null; // Clear any previous error messages
      } catch (error) {
        this.errorMessage = `Error fetching remote properties: ${error.response ? error.response.data.error : error.message}`;
        console.error(this.errorMessage);
        this.remoteProperties = null; // Clear data if an error occurs
      }
    }
  }
}
</script>


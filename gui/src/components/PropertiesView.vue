<template>
  <div>
    <div v-if="properties">
      <h2>Properties for {{ filesystem }}</h2>
      <ul>
        <li>Most Recent Snapshot: {{ properties.most_recent_snapshot }}</li>
        <li v-for="(value, key) in properties.properties" :key="key">
          {{ key }}:
          <span v-if="key === 'zab:server'">
            <button @click="showRemoteProperties(value)">
              {{ value }}
            </button>
          </span>
          <span v-else>
            {{ value }}
          </span>
        </li>
        <li>Last Backup: {{ properties.last_backup }}</li>
        <li>Timestamp: {{ properties.timestamp }}</li>
        <li>Last Run: {{ properties.last_run }}</li> <!-- Display the last_run field -->
        <li>Manual Override: {{ properties.manual_override }}</li>
        <li>Manual Override Reason: {{ properties.manual_override_reason }}</li>
        <li>Manual Override End Date: {{ properties.manual_override_end_date }}</li>
      </ul>
      <button @click="showTicketModal">Submit a Ticket</button>
      <div>
        <h3>Manual Override</h3>
        <label>
          <input type="checkbox" v-model="manualOverride" />
          Manual Override
        </label>
        <br />
        <label>
          Reason:
          <input type="text" v-model="manualOverrideReason" />
        </label>
        <br />
        <label>
          End Date:
          <input type="date" v-model="manualOverrideEndDate" />
        </label>
        <br />
        <button @click="applyOverride">Apply Override</button>
      </div>
    </div>
    <RemotePropertiesView
      v-if="remoteHost && remoteFilesystem"
      :remoteHost="remoteHost"
      :remoteFilesystem="remoteFilesystem"
    />

    <CustomModal :visible="showModal" title="Submit a Ticket" @close="closeModal">
      <form @submit.prevent="submitTicket">
        <label for="subject">Subject:</label>
        <input id="subject" v-model="ticketSubject" required />
        <label for="message">Message:</label>
        <textarea id="message" v-model="ticketMessage" required></textarea>
        <button type="submit">Submit</button>
      </form>
    </CustomModal>
  </div>
</template>

<script>
import axios from 'axios';
import RemotePropertiesView from './RemotePropertiesView.vue';
import CustomModal from './CustomModal.vue';

export default {
  props: ['host', 'filesystem'],
  components: {
    RemotePropertiesView,
    CustomModal,
  },
  data() {
    return {
      properties: null,
      remoteHost: null,
      remoteFilesystem: null,
      showModal: false,
      ticketSubject: '',
      ticketMessage: '',
      manualOverride: false,
      manualOverrideReason: '',
      manualOverrideEndDate: '',
    };
  },
  watch: {
    filesystem(newFs) {
      if (newFs) {
        this.fetchProperties(this.host, newFs);
        this.resetRemoteProperties();
        this.ticketSubject = `Issue with filesystem: ${newFs}`; // Set the ticket subject
      }
    },
  },
  mounted() {
    if (this.host && this.filesystem) {
      this.fetchProperties(this.host, this.filesystem);
      this.ticketSubject = `Issue with filesystem: ${this.filesystem}`; // Set the ticket subject
    }
  },
  methods: {
    async fetchProperties(host, filesystem) {
      try {
        const response = await axios.get(
          `${import.meta.env.VITE_API_URL}/api/hosts/${host}/filesystems/${filesystem}/properties`
        );
        this.properties = response.data;
        this.manualOverride = false;
        this.manualOverrideReason = '';
        this.manualOverrideEndDate = '';
      } catch (error) {
        console.error('Error fetching properties:', error);
      }
    },
    showRemoteProperties(value) {
      const [host, fsPath] = value.split(':');
      const originalFsPath = this.filesystem.replace(/^raid[a-z]?\/?/, '');

      let prefix = '';
      let type = '';
      if (fsPath) {
        const prefixMatch = fsPath.match(/(raid[a-z]*)-(zab|zas)/);
        if (prefixMatch) {
          prefix = prefixMatch[1];
          type = prefixMatch[2];
        }
      }

      this.remoteHost = host;
      this.remoteFilesystem = `${prefix}/${type}/${originalFsPath}`;
    },
    resetRemoteProperties() {
      this.remoteHost = null;
      this.remoteFilesystem = null;
    },
    showTicketModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    async submitTicket() {
      try {
        const response = await axios.post(
          `${import.meta.env.VITE_API_URL}/api/tickets`,
          {
            title: `Issue with filesystem: ${this.filesystem}`, // Use the filesystem as part of the ticket subject
            group: 'GRIT',
            customer: 'zmap@grit.ucsb.edu', // Update this with actual customer email
            article: {
              subject: this.ticketSubject,
              body: this.ticketMessage,
              type: 'note',
              internal: false,
            },
          },
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );

        console.log('Ticket submitted successfully:', response.data);
        this.showModal = false;
        this.ticketSubject = '';
        this.ticketMessage = '';
      } catch (error) {
        console.error('Error submitting ticket:', error.response ? error.response.data : error.message);
      }
    },
    async applyOverride() {
      try {
        const payload = {
          manual_override: this.manualOverride,
          manual_override_reason: this.manualOverrideReason,
          manual_override_end_date: this.manualOverrideEndDate,
        };

        const response = await axios.post(
          `${import.meta.env.VITE_API_URL}/api/hosts/${this.host}/filesystems/${this.filesystem}/override`,
          payload,
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );

        console.log('Override applied successfully:', response.data);
        this.fetchProperties(this.host, this.filesystem);
      } catch (error) {
        console.error('Error applying override:', error);
      }
    },
    formatDateForInput(dateString) {
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = ('0' + (date.getMonth() + 1)).slice(-2);
      const day = ('0' + date.getDate()).slice(-2);
      return `${year}-${month}-${day}`;
    },
  },
};
</script>

<style scoped>
/* Add any styles specific to this component */
</style>


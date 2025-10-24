<template>
  <div id="app">
    <div class="column hosts-column">
      <div class="sticky-header">
        <h2>Hosts</h2>
        <input type="text" placeholder="Search hosts..." v-model="hostFilter" />
      </div>
      <HostsList :filterText="hostFilter" @hostSelected="handleHostSelected"/>
    </div>
    <div class="column filesystems-column" v-if="selectedHost">
      <div class="sticky-header">
        <h2>Filesystems for {{ selectedHost }}</h2>
        <input type="text" placeholder="Search filesystems..." v-model="filesystemFilter" />
      </div>
      <FilesystemsList :host="selectedHost" :filter="filesystemFilter" @filesystemSelected="handleFilesystemSelected"/>
    </div>
    <div class="column properties-column" v-if="selectedFilesystem">
      <PropertiesView :host="selectedHost" :filesystem="selectedFilesystem"/>
    </div>
   <TooltipLegend />
  </div>
</template>

<script>
import HostsList from './components/HostsList.vue';
import FilesystemsList from './components/FilesystemsList.vue';
import PropertiesView from './components/PropertiesView.vue';
import TooltipLegend from './components/TooltipLegend.vue';

export default {
  name: 'App',
  components: {
    HostsList,
    FilesystemsList,
    PropertiesView,
    TooltipLegend

  },
  data() {
    return {
      selectedHost: null,
      selectedFilesystem: null,
      hostFilter: '',
      filesystemFilter: '',
    };
  },
  methods: {
    handleHostSelected(host) {
      this.selectedHost = host;
      this.selectedFilesystem = null;
      this.filesystemFilter = ''; // Reset filesystem filter when a new host is selected
    },
    handleFilesystemSelected(filesystem) {
      this.selectedFilesystem = filesystem;
    }
  }
}
</script>

<style>
#app {
  display: flex;
  align-items: flex-start;
}

.column {
  padding: 10px;
  margin-right: 10px;
}

.hosts-column, .filesystems-column {
  flex: 3;
  min-width: 400px;
}

.filesystems-column .sticky-header, .hosts-column .sticky-header {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  background-color: #fff;
  padding: 10px 0;
  z-index: 1000;
  border-bottom: 1px solid #ccc;
}

.properties-column {
  flex: 4;
  max-width: 800px;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  max-height: 90vh;
  position: fixed;
  right: 20px;
  top: 10px;
}

.properties-column h2 {
  margin-top: 0;
}
</style>


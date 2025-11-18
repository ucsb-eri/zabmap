<script setup>
import Loader from "@/components/Loader.vue";
import LastUpdated from "@/components/LastUpdated.vue";
</script>

<template>
  <div id="app">
    <div  class="flex flex-row-reverse pr-2">
      <Suspense>
        <LastUpdated></LastUpdated>
        <template #fallback><Loader /> </template>
      </Suspense>
    </div>
    <div
      class="flex items-strech"
    > <!-- grow flex flex-nowrap justify-start flex- items-center gap-2 justify-center flex-row -->

      <div class="self-start h-full p-6 text-center basis-1 grow">
        <Suspense>
          <router-view name="HostsView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </div>
      <div class="h-full p-6 text-center basis-1 grow">
        <Suspense>
          <router-view name="FilesystemsView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </div>
      <div class="h-full p-6 text-center basis-1 grow">
        <Suspense>
          <router-view name="PropertiesView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </div>
    </div>
  </div>
</template>

<style>
.column {
  padding: 10px;
  margin-right: 10px;
}

.hosts-column,
.filesystems-column {
  flex: 3;
  min-width: 400px;
}

.filesystems-column .sticky-header,
.hosts-column .sticky-header {
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

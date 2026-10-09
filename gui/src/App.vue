<script setup>
import Loader from "@/components/Loader.vue";
import LastUpdated from "@/components/LastUpdated.vue";
import UserMenu from "@/auth/UserMenu.vue";
</script>

<template>
  <div id="app" class="min-h-screen">
    <header
      class="flex items-center gap-4 border-b border-slate-200 bg-white px-4 py-2.5 sm:px-6"
    >
      <span class="text-base font-semibold tracking-tight">zabmap</span>
      <div class="grow"></div>
      <Suspense>
        <LastUpdated class="text-sm text-slate-500" />
        <template #fallback><Loader /> </template>
      </Suspense>
      <UserMenu />
    </header>

    <!-- Three panes side by side on wide screens, stacked on narrow ones.
         empty:hidden collapses a pane while its route view has nothing to show. -->
    <main
      class="flex flex-col gap-4 p-4 pb-20 sm:p-6 sm:pb-20 lg:flex-row lg:items-start"
    >
      <section
        aria-label="Hosts"
        class="min-w-0 rounded-lg border border-slate-200 bg-white text-left empty:hidden lg:w-80 lg:shrink-0"
      >
        <Suspense>
          <router-view name="HostsView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </section>
      <section
        aria-label="Filesystems"
        class="min-w-0 rounded-lg border border-slate-200 bg-white text-left empty:hidden lg:flex-1"
      >
        <Suspense>
          <router-view name="FilesystemsView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </section>
      <section
        aria-label="Properties"
        class="min-w-0 rounded-lg border border-slate-200 bg-white text-left empty:hidden lg:w-[28rem] lg:shrink-0"
      >
        <Suspense>
          <router-view name="PropertiesView" />
          <template #fallback><Loader /> </template>
        </Suspense>
      </section>
    </main>
  </div>
</template>

<style>
/* Header block at the top of each pane (title plus search box).
   HostsView and FilesystemsView use this class. */
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: grid;
  gap: 8px;
  padding: 12px 16px;
  background-color: #fff;
  border-bottom: 1px solid var(--color-slate-200);
  border-radius: 8px 8px 0 0;
}
</style>

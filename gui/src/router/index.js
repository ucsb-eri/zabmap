import { createRouter, createWebHistory } from "vue-router";
import HostsView from "@/views/HostsView.vue";
import FilesystemsView from "@/views/FilesystemsView.vue";
import PropertiesView from "@/views/PropertiesView.vue";

const routes = [
  { path: "/", components: { HostsView } },
  {
    path: "/hosts/:hostId/filesystems",
    components: { HostsView, FilesystemsView },
    props: true,
  },
  {
    path: "/hosts/:hostId/filesystems/:filesystemId",
    components: { HostsView, FilesystemsView, PropertiesView },
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

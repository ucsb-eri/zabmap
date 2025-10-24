import { createRouter, createWebHistory } from 'vue-router';
import HostsList from '../components/HostsList.vue';
import FilesystemsList from '../components/FilesystemsList.vue';
import PropertiesView from '../components/PropertiesView.vue';

const routes = [
  { path: '/hosts', component: HostsList },
  { path: '/hosts/:host/filesystems', component: FilesystemsList },
  { path: '/hosts/:host/filesystems/:filesystem', component: PropertiesView },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;


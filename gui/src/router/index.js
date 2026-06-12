import { createRouter, createWebHistory } from "vue-router";
import HostsView from "@/views/HostsView.vue";
import FilesystemsView from "@/views/FilesystemsView.vue";
import PropertiesView from "@/views/PropertiesView.vue";
import AuthCallback from "@/auth/AuthCallback.vue";
import SignedOut from "@/auth/SignedOut.vue";
import userManager, { login } from "@/auth/userManager";

const routes = [
  { path: "/auth/callback", components: { HostsView: AuthCallback }, meta: { public: true } },
  { path: "/signed-out", components: { HostsView: SignedOut }, meta: { public: true } },
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

router.beforeEach(async (to) => {
  // Development escape hatch: set VITE_AUTH_DISABLED=true to skip the OIDC
  // login redirect entirely. MUST stay false/unset in production.
  if (import.meta.env.VITE_AUTH_DISABLED === "true") return true;
  if (to.meta.public) return true;
  const user = await userManager.getUser();
  if (!user || user.expired) {
    await login();
    return false;
  }
  return true;
});

export default router;

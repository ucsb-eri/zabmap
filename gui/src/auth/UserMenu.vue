<script setup>
import { ref, onMounted } from "vue";
import userManager, { logout } from "@/auth/userManager";

const name = ref("");

async function refresh() {
  const u = await userManager.getUser();
  name.value = u?.profile?.preferred_username || u?.profile?.name || u?.profile?.email || "";
}

onMounted(refresh);
userManager.events.addUserLoaded(refresh);
userManager.events.addUserUnloaded(() => (name.value = ""));
</script>

<template>
  <div v-if="name" class="flex items-center gap-2 text-sm">
    <span>{{ name }}</span>
    <button
      type="button"
      class="text-blue-700 hover:underline"
      @click="logout()"
    >
      Logout
    </button>
  </div>
</template>

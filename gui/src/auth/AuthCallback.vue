<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import userManager from "@/auth/userManager";

const router = useRouter();

onMounted(async () => {
  try {
    await userManager.signinRedirectCallback();
  } catch (e) {
    console.error("OIDC callback failed", e);
  }
  router.replace("/");
});
</script>

<template>
  <div class="p-6 text-center">Signing you in…</div>
</template>

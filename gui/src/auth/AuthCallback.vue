<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import userManager from "@/auth/userManager";

const router = useRouter();
const error = ref(null);

onMounted(async () => {
  try {
    await userManager.signinRedirectCallback();
    router.replace("/");
  } catch (e) {
    console.error("OIDC callback failed", e);
    error.value = e?.message || String(e);
    // Do not redirect on failure — leave the error on screen so we can read it.
  }
});
</script>

<template>
  <div class="p-6 text-left">
    <template v-if="error">
      <h2 class="text-red-700 font-bold">OIDC callback failed</h2>
      <pre class="whitespace-pre-wrap text-sm mt-2">{{ error }}</pre>
      <p class="mt-4 text-sm">
        Check devtools → Network → the <code>POST .../application/o/token/</code>
        request for the underlying cause.
      </p>
    </template>
    <template v-else>
      Signing you in…
    </template>
  </div>
</template>

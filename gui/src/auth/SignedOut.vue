<script setup>
import { login } from "@/auth/userManager";
</script>

<template>
  <div class="p-6 text-left">
    <h2 class="text-lg font-bold">You're signed out</h2>
    <p class="mt-2 text-sm">Your session has ended.</p>
    <button
      type="button"
      class="mt-4 text-blue-700 hover:underline"
      @click="login()"
    >
      Sign in again
    </button>
  </div>
</template>

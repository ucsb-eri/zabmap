import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import userManager from '@/auth/userManager';
import './index.css'

async function bootstrap() {
  // Prime the user store before the first route guard runs so we don't
  // bounce a freshly-loaded SPA through Authentik when a valid token is cached.
  try {
    await userManager.getUser();
  } catch {
    // ignore — guard will redirect to login
  }
  createApp(App).use(router).mount('#app');
}

bootstrap();

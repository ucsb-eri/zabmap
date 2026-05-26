import { useFetch } from "@vueuse/core";
import { getAccessToken } from "@/auth/userManager";

export function useAuthedFetch(url, options = {}) {
  const { beforeFetch: userBeforeFetch, ...rest } = options;

  return useFetch(url, {
    ...rest,
    async beforeFetch(ctx) {
      const token = await getAccessToken();
      ctx.options.headers = {
        ...(ctx.options.headers || {}),
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      };
      if (userBeforeFetch) {
        const result = await userBeforeFetch(ctx);
        if (result) return result;
      }
      return { options: ctx.options };
    },
  });
}

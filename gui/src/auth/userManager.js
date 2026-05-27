import { UserManager, WebStorageStateStore } from "oidc-client-ts";

const userManager = new UserManager({
  authority: import.meta.env.VITE_OIDC_AUTHORITY,
  client_id: import.meta.env.VITE_OIDC_CLIENT_ID,
  redirect_uri: import.meta.env.VITE_OIDC_REDIRECT_URI,
  post_logout_redirect_uri:
    import.meta.env.VITE_OIDC_POST_LOGOUT_REDIRECT_URI ||
    `${window.location.origin}/signed-out`,
  response_type: "code",
  scope: "openid profile email offline_access",
  automaticSilentRenew: true,
  userStore: new WebStorageStateStore({ store: window.localStorage }),
});

// If background renewal ever fails (e.g. refresh token revoked), clear the
// stored user so the next navigation triggers a fresh interactive login
// instead of letting fetches spin on an expired token.
userManager.events.addSilentRenewError((err) => {
  console.warn("OIDC silent renew failed; clearing user", err);
  userManager.removeUser();
});

export default userManager;

export function login() {
  return userManager.signinRedirect();
}

export function logout() {
  return userManager.signoutRedirect();
}

export function getUser() {
  return userManager.getUser();
}

// Returns the current access token, or null if there isn't a valid one.
// Does NOT trigger silent renewal — automaticSilentRenew handles that in the
// background. If the token is gone/expired, the router guard will redirect
// on the next navigation; fetches will simply fail with 401.
export async function getAccessToken() {
  const user = await userManager.getUser();
  if (!user || user.expired) return null;
  return user.access_token;
}

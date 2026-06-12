from functools import wraps

import jwt
from flask import current_app, g, jsonify, request
from jwt import PyJWKClient

_jwks_client = None


def _get_jwks_client():
    global _jwks_client
    if _jwks_client is None:
        base = current_app.config["OIDC_ISSUER"].rstrip("/")
        _jwks_client = PyJWKClient(f"{base}/jwks/")
    return _jwks_client


def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if request.method == "OPTIONS":
            return fn(*args, **kwargs)

        # Development escape hatch: set FLASK_AUTH_DISABLED=true to skip JWT
        # validation entirely. MUST stay false/unset in production.
        if current_app.config.get("AUTH_DISABLED"):
            g.user = {"sub": "dev", "email": "dev@localhost", "dev": True}
            return fn(*args, **kwargs)

        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "missing bearer token"}), 401
        token = header[len("Bearer "):].strip()

        # Must match the JWT's `iss` claim character-for-character (trailing slash and all).
        issuer = current_app.config["OIDC_ISSUER"]
        audience = current_app.config["OIDC_AUDIENCE"]

        try:
            signing_key = _get_jwks_client().get_signing_key_from_jwt(token).key
            claims = jwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                audience=audience,
                issuer=issuer,
            )
        except jwt.InvalidTokenError as e:
            current_app.logger.info(f"JWT rejected: {e}")
            return jsonify({"error": "invalid token"}), 401

        g.user = claims
        return fn(*args, **kwargs)

    return wrapper

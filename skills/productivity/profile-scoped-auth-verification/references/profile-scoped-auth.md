# Profile-scoped auth example

Live-session example:

- Active session ran with `HERMES_HOME=/root/.hermes/profiles/jarvis`.
- Google OAuth files existed in shared home (`~/.hermes/google_token.json`, `~/.hermes/google_client_secret.json`).
- `scripts/setup.py --check` failed in the active profile with:
  `NOT_AUTHENTICATED: No token at /root/.hermes/profiles/jarvis/google_token.json`
- Copying the token and client secret into the active profile fixed auth.
- After the copy, `setup.py --check` returned `AUTHENTICATED`, and Calendar/Drive reads succeeded.

Lesson:
- Always verify the credential root that matches the active Hermes profile before concluding a service is unavailable.

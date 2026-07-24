---
name: profile-scoped-auth-verification
description: Verify and repair credential visibility in active Hermes profile sessions before concluding a service is unavailable.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auth, profiles, credentials, verification, troubleshooting]
---

# Profile-Scoped Auth Verification

Use this skill when a tool or integration looks unauthenticated, but the session may be running under a non-default Hermes profile.

## Trigger conditions
- A service worked in a previous session, but current `--check` says unauthenticated.
- `HERMES_HOME` points to a profile directory instead of shared `~/.hermes`.
- The user says they already granted OAuth access.
- A tool works only after copying credentials into the active profile.

## Steps
1. **Check the active profile root first.**
   - Read `HERMES_HOME` and confirm the session’s actual credential root.
2. **Inspect both locations.**
   - Shared home: `~/.hermes/...`
   - Active profile: `${HERMES_HOME}/...`
3. **Verify the credential files in the active profile.**
   - Prefer `--check` or the tool’s own auth probe.
4. **If credentials exist only in the shared home, copy or re-authorize into the active profile.**
   - Re-run the auth check after the move.
5. **Only then conclude access is missing.**

## Pitfalls
- Do not assume the shared home and active profile share auth state.
- Do not declare a service unavailable until the active profile has been checked.
- If the tool supports verification calls, test a real read after auth succeeds.

## Verification
- Auth check returns authenticated.
- A real API read succeeds in the active profile.

## Reference
- See `references/profile-scoped-auth.md` for a live-session example and the exact fix pattern.

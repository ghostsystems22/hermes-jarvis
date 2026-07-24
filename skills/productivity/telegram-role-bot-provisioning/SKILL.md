---
name: telegram-role-bot-provisioning
description: Provision a dedicated Telegram bot/profile for a specific business role (e.g. content, ops, sales) and verify it is ready to run.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [telegram, gateway, profile, bot, provisioning, role-based]
---

# Telegram Role Bot Provisioning

Use this skill when the user wants a *dedicated Telegram bot* for a specific function, not a generic assistant.

Typical roles:
- content / marketing
- operations / admin
- sales / lead handling
- project-specific assistants

## Goal
Create a clean, role-specific Hermes profile and Telegram gateway setup with:
- its own identity/persona
- its own Telegram bot token
- its own allowlist / access scope
- a verified running gateway

## Inputs to ask for
- Bot name / role name
- Telegram bot token
- Allowed Telegram user IDs
- Desired persona / scope
- Whether to clone from an existing profile or start fresh

## Workflow

1. **Choose the base profile**
   - Prefer cloning from the user's current active profile when the new bot should share the same model/auth/skills baseline.
   - Use a fresh profile only if the bot should be isolated from current assumptions.

2. **Create the profile**
   - Clone the base profile.
   - Give it a lowercase, stable profile name.
   - Keep the profile dedicated to the new bot's role.

3. **Rebrand the persona**
   - Edit `SOUL.md` so the profile speaks in the bot's role, not the parent profile's role.
   - Keep the instructions short and role-specific.
   - Make the bot's scope explicit and narrow.

4. **Configure Telegram access**
   - Add the bot token in the profile `.env`.
   - Set the allowed user IDs explicitly.
   - Keep the access list tight unless the user explicitly wants broader access.

5. **Start the gateway**
   - Launch the profile's gateway.
   - Confirm Telegram is configured and the gateway is running.

6. **Verify behavior**
   - Check that the bot answers as the intended role.
   - Confirm that the profile name, persona, and Telegram identity are aligned.
   - Make sure the bot is not mixed with the user's main orchestration profile.

## Verification checklist
- `hermes status` shows Telegram configured
- gateway is running for the new profile
- `SOUL.md` matches the intended role
- token and allowlist are scoped to the bot
- the bot responds with the correct persona

## Design rules
- One role, one profile, one Telegram identity
- Avoid generic “do everything” bots
- Prefer clear separation over multi-purpose sprawl
- Keep the bot language, behavior, and outputs aligned with its function

## Reference
See `references/telegram-role-bot-launch.md` for a concrete launch checklist and a reusable provisioning pattern.

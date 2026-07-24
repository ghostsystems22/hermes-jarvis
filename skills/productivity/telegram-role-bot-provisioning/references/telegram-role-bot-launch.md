# Telegram role bot launch checklist

Concrete provisioning pattern used for dedicated role-based Telegram bots.

## Example structure
- Base profile: clone from the user's active profile
- New profile: one role, one bot identity
- Persona file: rewrite `SOUL.md` so the bot speaks only in its role
- Telegram config: set bot token + allowed user IDs in the profile `.env`
- Launch: start the profile gateway and verify Telegram is connected

## Practical sequence
1. Clone the profile from the current working profile.
2. Rename the profile to a stable lowercase name.
3. Rewrite `SOUL.md` for the new role.
4. Add Telegram token and allowlist to the new profile `.env`.
5. Start the gateway for that profile.
6. Check `hermes status` for Telegram connectivity.
7. Send a test message and confirm the persona matches the role.

## Bot role examples
- Content assistant: hooks, posts, threads, repurposing, newsletters
- Ops assistant: task capture, follow-up, routing, status checks
- Sales assistant: outreach drafts, CRM follow-up, pipeline summaries

## Notes
- Keep the role narrow.
- Prefer a separate profile instead of overloading the main orchestration bot.
- Treat the Telegram bot identity as part of the profile, not a shared utility.

# Calendar scheduling discipline

Use this when creating or reshaping a day in Google Calendar for Gabriel.

## Hard rules
- Anchor scheduling to the live current time in the user's timezone before creating anything.
- Never place a task earlier than the time the user asked from.
- Preserve existing fixed blocks unless the user explicitly asks to move or delete them.
- Fill only real free slots; do not create artificial micro-blocks just to make the day look full.
- Before writing, list the day window and check what is already there, including newly added daily anchors like gym.

## Block design
- Prefer one clear outcome per block.
- Favor 60–120 minute work blocks.
- Use short transition/admin blocks only when they protect a larger block.
- Keep titles simple and consistent so the calendar stays readable.

## Visual coding
- If you need visual categories without separate calendars, encode the type in the title prefix (for example: `🔵 BUSINESS`, `⚫ 9-5`, `🟢 PERSONAL`, `🟡 ROUTINE`, `🟠 ADMIN`).
- Keep the same prefix scheme across the calendar and Notion.

## Verification
- After edits, re-list the calendar window to confirm:
  - no backdated tasks
  - no accidental overlaps
  - no duplicated blocks
  - fixed anchors still intact

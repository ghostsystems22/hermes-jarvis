# Calendar planning rules

Session-learned rules for Gabriel's agenda planning.

## Hard rules
- Never schedule a task before the time the user asked planning to begin.
- If the user asks to organize from a given time, only use time slots at or after that time.
- Do not create explicit break blocks unless Gabriel asks for one.
- If a gap exists, fill it with a task/admin block or leave it untouched only if it is a fixed pre-existing event.
- Preserve fixed events the user said not to touch (gym, dinner, sleep, commute, dogs, routine anchors).
- Use a live timezone-aware read before writing. For this profile, treat Asia/Bangkok as the working timezone unless the user says otherwise.

## Agenda shaping
- Prefer a small number of contiguous blocks over many tiny blocks.
- Keep each block to one clear outcome.
- Avoid duplicating the same task across adjacent blocks unless the split is intentional and necessary.
- If the schedule becomes unreadable, regroup by task type and shorten titles.

## Color / type conventions
- BUSINESS -> blue -> colorId 9
- 9-5 -> gray -> colorId 8
- ADMIN -> orange -> colorId 6
- PERSONAL -> green
- ROUTINE -> yellow
- BREAK is only used when explicitly requested.

## Verification
- Re-list the calendar after writing.
- Check for overlaps, accidental gaps, and any event created before the requested start time.
- When using Google Calendar API events, include the colorId when the color matters visually.

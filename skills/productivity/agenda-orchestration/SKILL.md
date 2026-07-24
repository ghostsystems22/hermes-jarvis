---
name: agenda-orchestration
description: "Gabriel's agenda planning rules: contiguous blocks, energy-aware scheduling, color/type mapping, and Notion-to-Calendar alignment."
version: 1.0.0
author: Hermes
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Calendar, Planning, Scheduling, Notion, Productivity, Energy]
---

# Agenda orchestration

Use this skill when organizing Gabriel's day, shaping calendar blocks, or translating Notion tasks into calendar time.

## Core rules
- Schedule **at or after** the time the user asked from; never place work earlier than the planning anchor.
- Fill the day with **contiguous blocks**; do not leave unlabeled gaps inside the planned span.
- **Do not add break blocks unless Gabriel explicitly asks for a break.** If a gap exists, either fill it with a task/admin block or leave it only when it is a fixed event the user told you not to touch.
- Preserve fixed blocks such as gym, dinner, sleep, commute, and other explicitly protected events.
- Avoid duplicate or near-duplicate task blocks unless the split is intentional and necessary.
- Prefer a small number of high-signal blocks over many micro-blocks.
- One block = one outcome.

## Energy-aware sequencing
- Put peak-cognitive work in peak energy slots.
- Put execution and follow-up in mid-energy slots.
- Put admin, triage, logging, and shutdown tasks in low-energy slots.
- If a task is too heavy for the slot, flag it instead of silently forcing it in.

## Type and color system
Use the same type names in Notion and Calendar.

- BUSINESS -> blue -> `colorId 9`
- 9-5 -> gray -> `colorId 8`
- PERSONAL -> green
- ROUTINE -> yellow
- ADMIN -> orange -> `colorId 6`
- BREAK only if explicitly requested

## Notion link-up
- Add a single `Type` property in Notion as a `Select`.
- Use the same category names across dashboard views and calendar titles.
- Keep dashboard views grouped by `Type` so Calendar and Notion read the same way.
- When possible, prefix calendar titles with the type label so the visual meaning survives even when color rendering is limited.

## Workflow
1. Read the live calendar first.
2. Identify fixed blocks the user said not to touch.
3. Determine the planning anchor time.
4. Build contiguous task blocks from the anchor forward.
5. Apply type/color naming consistently.
6. Re-read the calendar and verify there are no accidental overlaps, pre-anchor tasks, or unlabeled gaps.

## Pitfalls
- Do not insert "buffer" or "break" blocks as a default habit.
- Do not schedule anything before the requested start time.
- Do not assume the user wants a break just because there is a gap.
- Do not rename protected events unless asked.

## References
- See `references/calendar-planning-rules.md` for the session-learned rules and exact type/color mapping.

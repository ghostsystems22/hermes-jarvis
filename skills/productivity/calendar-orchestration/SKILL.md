---
name: calendar-orchestration
description: "Calendar planning and agenda shaping: protect fixed blocks, fill free slots, avoid backdating, and keep day views readable with consistent task types."
version: 1.0.0
author: Hermes
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Calendar, Planning, Scheduling, Time-blocking, Productivity, Notion]
---

# Calendar Orchestration

Use this skill when the user asks to plan, reshape, or clean up a day in Calendar.

## Trigger conditions
- The user wants blocks placed on a day, afternoon, or week.
- The user wants an agenda to stay readable and non-overlapping.
- The user wants calendar categories matched to Notion task types.
- The user asks to preserve fixed anchors like gym, dinner, dogs, commute, or sleep.

## Core rules
1. Anchor planning to the **live current time** in the user's timezone before creating anything.
2. Never place a task earlier than the time the user asked from.
3. Preserve existing fixed blocks unless the user explicitly asks to move or delete them.
4. Fill only real free slots; do not invent extra micro-blocks just to make the day look full.
5. Prefer one clear outcome per block.
6. Use 60–120 minute work blocks when possible; use short blocks only for transitions or shutdown.
7. After edits, re-list the calendar window and verify there are no backdated tasks, overlaps, or duplicate blocks.

## Day-shaping workflow
- Read the live time and the full day window.
- Identify fixed anchors already on the calendar.
- Map the remaining free space from now forward.
- Choose the fewest blocks that make the day executable.
- Keep each block named by outcome, not by vague category.

## Visual coding
When you want category clarity without separate calendars, use a stable title prefix scheme:
- `🔵 BUSINESS`
- `⚫ 9-5`
- `🟢 PERSONAL`
- `🟡 ROUTINE`
- `🟠 ADMIN`

Keep the same vocabulary in Calendar and Notion.

## Notion alignment
Use the same category set in Notion as a `Type` select:
- BUSINESS
- 9-5
- PERSONAL
- ROUTINE
- ADMIN

Treat that Notion `Type` field as the source of truth for task classification.

## Pitfalls
- Backdating because a hardcoded date was used instead of live now.
- Overwriting fixed anchors like gym or dinner.
- Adding too many small blocks and making the agenda unreadable.
- Mixing several task types in one block.
- Creating a plan that ignores already-passed time.

## Verification
Before finalizing, confirm:
- the schedule starts at or after the requested time
- fixed blocks remain intact
- the remaining open slots are filled intentionally
- the day is readable at a glance

## Reference
Session-specific scheduling notes live in `references/calendar-scheduling-discipline.md`.

---
name: notion-airtable-command-center
description: Build and maintain Airtable command centers mirrored from Notion projects, tasks, and phases.
version: 1.0.0
author: nous
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Notion, Airtable, Productivity, Database, Workflow, Sync]
---

# Notion ↔ Airtable command center

Use this skill when the user wants Airtable to act as the execution layer for one or more Notion projects, especially when tasks/phases need to be launchable from Airtable and kept linked back to Notion.

## Triggers

- Mirror Notion projects, tasks, phases, or SOPs into Airtable.
- Create or extend an Airtable base to support task claiming, queueing, and autonomous execution.
- Rebuild a project dashboard so Airtable can launch work with links back to the source Notion pages.
- Import Notion structure into Airtable while preserving relations and source IDs.

## Workflow

1. Inspect the live Notion source first.
   - Query the relevant Notion data sources for project/task/phase rows.
   - Extract page IDs, titles, relations, and URLs from the source rows.
   - Do not rely on page markdown if the page body is empty; many data-source rows have all the useful structure in properties.

2. Inspect the Airtable schema before writing anything.
   - Read the base tables and fields first.
   - Look for scaffold rows already present in the base.
   - Reuse placeholder rows when they exist instead of duplicating or deleting without need.

3. Create or patch the schema in Airtable.
   - Create tables for Projects, Tasks, Phases, Runs, Queue, Session Health, or Model Policy as needed.
   - Prefer minimal linked-record creates first; Airtable often fills inverse fields automatically.
   - Verify the resulting schema after every structural change.

4. Populate records from Notion.
   - Preserve the source Notion page URL and page ID in Airtable.
   - Keep relations bidirectional: project ↔ tasks, project ↔ phases, phase ↔ tasks, task ↔ runs, etc.
   - Batch record creates in groups of up to 10.

5. Verify the graph.
   - Re-read the Airtable tables after writes.
   - Confirm counts, relations, and source IDs match the Notion source.
   - Confirm the base is actually launchable from Airtable before telling the user it is ready.

## Airtable schema pitfalls

- Checkbox fields need `options` on create. If Airtable says the checkbox field is missing options, include both icon and color in the create payload.
- `multipleRecordLinks` fields are safest to create with only `linkedTableId` in `options`; Airtable usually supplies the inverse-link metadata after creation.
- `autoNumber` can exist as a field type, but the metadata create endpoint may still reject it in some bases/plans. If create fails, fall back to text unless you have a proven path.
- Creating a linked-record field can auto-create the inverse field in the linked table. Check the schema before adding another field with the same semantic role.
- If Airtable already has blank scaffold rows, patch them when possible instead of creating duplicates.

## Notion source pitfalls

- Use Notion data source queries to get the real project/task/phase graph.
- Search may return the right page, but the page body can still be empty or irrelevant; property values are usually the source of truth.
- Preserve both Notion page URL and page ID in Airtable so later automation can round-trip between systems.

## Writing conventions

- Keep Airtable record names human-readable and task-launchable.
- Keep source IDs in dedicated fields, not buried in notes.
- For autonomous launch workflows, add fields that support execution gating: status, priority, complexity, recommended model, blocker, and queue state.

## Verification checklist

- Projects exist in Airtable for each Notion project.
- Tasks are linked to their project and, when applicable, to their phase.
- Phases are linked to the correct project and contain the correct tasks.
- Any placeholder rows that were reused now contain real source data.
- The Airtable base can be used as a live queue, not just a mirror.

## Reference material

- See `references/airtable-notion-sync.md` for the exact Airtable create payloads, Notion query patterns, and the schema-validation failures encountered during this session.

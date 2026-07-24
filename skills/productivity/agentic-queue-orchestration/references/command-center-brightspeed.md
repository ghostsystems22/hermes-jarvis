# Brightspeed command center notes

Session goal: build a 24/7 command center for project work using Airtable as the queue, Notion as the documentation layer, and GitHub as the implementation surface.

## Durable patterns learned

- Airtable is the execution queue, not the spec store.
- Notion project pages should be read before a task launches.
- Each queued task should link to a dedicated Notion task page containing:
  - scope
  - parameters
  - required model / model tier
  - tests
  - completion check
- GitHub repos are the implementation boundary for client projects.
- Keep client systems off-limits unless a task explicitly authorizes external actions.

## Airtable base strategy

- Use one command-center base per operating domain/client cluster.
- Prefer adapting an existing base when workspace/base creation is blocked by missing workspaceId.
- Useful base pattern:
  - Projects
  - Tasks
  - Agents
  - Runs
  - Reviews
  - Blockers / Errors

## Task launch rules

1. Load task row from Airtable.
2. Read the linked Notion task page.
3. Verify scope, parameters, tests, and completion check exist.
4. Choose a model tier from task complexity.
5. Check session health before dispatch.
6. Pause or degrade work when health is low.
7. Resume when health is healthy again.

## Suggested model routing

- Simple / mechanical tasks -> small fast model
- Normal implementation / edits -> balanced coding model
- High-ambiguity, multi-step, debugging, or architecture -> strongest available reasoning model

## Session health gate

Track a non-binary health state for long-running workers:

- Healthy
- LowBudget
- Exhausted
- Paused
- ResumeNeeded

Use it to stop automation before the session is out of budget, then resume once it recovers.

## Airtable + Notion connection

- Airtable row stores the task status and the Notion page link.
- Notion page stores the execution contract.
- The controller reads the Notion page at task start and writes back results to Airtable.

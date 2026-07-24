---
name: agentic-queue-orchestration
description: "Design and operate an always-on task queue for 24/7 agent work using Airtable, Notion, Hermes controllers, and worker agents."
version: 1.0.0
author: Hermes Agent + Nous Research
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [queue, airtable, notion, orchestration, cron, webhooks, workers, review]
---

# Agentic Queue Orchestration

Use this skill when the task is about designing, operating, or troubleshooting an always-on task queue for agentic work.

## Core model

- Airtable is the executable queue.
- Notion is the context/spec/SOP layer.
- Hermes is the controller that routes work.
- Worker agents do the actual execution.
- Git is the source of truth for code changes.
- A human approves anything that leaves the building.

## Recommended state machine

Queued -> Claimed -> In Progress -> Needs Review -> Done

Side states:
- Needs Info: missing context, access, or decision.
- Blocked: waiting on dependency.

## Workflow

1. Read the next task from Airtable.
2. Pull its linked Notion context before acting.
3. If context is missing, set status to Needs Info and stop.
4. Claim the task, spawn a worker, and keep the controller free.
5. Worker completes the task and returns a draft/result.
6. Controller writes back output, blockers, and next step.
7. Stop at Needs Review for human approval.
8. For longer-running queues, maintain a separate session-health signal so work can pause when model/token budget is low and resume when health recovers.

## Task row fields

- task_id
- client
- title
- priority
- status
- context_link
- output_link
- blocker
- owner
- due_at
- last_touched_at
- model_tier
- session_health
- retry_count
- claimed_by

Suggested `session_health` values:
- Healthy
- LowBudget
- Exhausted
- Paused
- ResumeNeeded

## Selection heuristic

1. Revenue-protecting and revenue-generating work first.
2. Client deadlines next.
3. Tasks with complete context before tasks needing clarification.
4. Small shippable tasks before sprawling ones.
5. Prefer tasks whose linked Notion page has a complete scope/package (scopes, parameters, required model, tests, completion check).

## Pitfalls

- Using Notion as the queue itself. It is a context store, not a fast execution board.
- Letting workers mark Done directly. They should stop at Needs Review.
- Guessing when context is missing. That burns time and money.
- Building orchestration before the queue spine exists.
- Mixing long-lived controller work with disposable worker execution.
- Launching a task without reading its linked Notion task page first.
- Treating model selection as static; routing should depend on task complexity and session health.
- Treating a valid Notion token as enough without sharing the page/database with the integration.
- Treating a 0-result Notion search as proof the token is bad before checking title mismatch or missing sharing.

## Support files

- references/queue-orchestration.md — condensed queue spine rules and operating notes.
- references/command-center-brightspeed.md — Airtable/Notion/GitHub pilot notes from the Brightspeed automation session.
- references/notion-access-checks.md — Notion token vs sharing verification for queue workflows.

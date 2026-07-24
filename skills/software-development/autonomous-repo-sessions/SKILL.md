---
name: autonomous-repo-sessions
description: "Autonomous repo build/test/report loops with branch discipline, local ledgers, and fallback reporting when external channels are unavailable."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [autonomy, repo-workflow, build-test-report, status-ledger, reporting, branch-discipline]
---

# Autonomous Repo Sessions

Use this skill for end-to-end repository work where the agent is expected to orient, implement, test, log progress, and report back without waiting for the user after every step.

This is a class-level workflow skill: it covers many repo tasks, not a single bug or ticket.

## When to use

Trigger this skill when a session involves any of:
- autonomous coding or refactoring in a repo
- build / test / report loops
- task backlogs or external trackers (Airtable, Notion, GitHub)
- branch-per-session discipline
- local reporting ledgers or session logs
- fallback handling when a reporting channel is unavailable

## Core loop

1. Orient
   - Read the repo root instructions first.
   - Read any nested instructions in directories you will touch.
   - Read the relevant spec / tracker / task doc before editing.
   - Inspect the existing code adjacent to the target area before writing anything.

2. Branch
   - Create a dedicated session branch unless the user explicitly says otherwise.
   - Keep changes small and commit them by logical unit.

3. Reporting path check
   - Before coding, determine whether the session has a live reporting channel.
   - If the intended reporting path is unavailable, do not silently skip reporting.
   - Record the fallback immediately in the repo’s local session log or ledger, then keep working.

4. Implement
   - Make the smallest change that satisfies the current task.
   - Preserve existing architecture and naming patterns.
   - Respect hard exclusions and scope boundaries.

5. Verify
   - Prefer a real smoke test against the produced artifact.
   - If a normal test runner is unavailable, use the strongest deterministic fallback you can run in the current environment (for example: bytecode compile, a small self-check script, or CLI smoke test).
   - Record any testing limitation explicitly in the status ledger.

6. Record
   - Update the repo’s status ledger / session log before ending.
   - Include what changed, what was tested, the remaining limitation, and the next action.

7. Commit
   - Commit with a scoped message.
   - If the task touches tracker state, update the tracker to match the actual result.

## Pitfalls

- Do not let a missing external credential or reporting channel turn into silent non-reporting.
- Do not claim a test suite ran if only a smoke test or compile check ran.
- Do not block the whole session on a non-essential reporting failure; log the fallback and continue the work.
- Do not treat one-off task progress as durable memory; keep that in the session log instead.
- Do not update unrelated files while trying to satisfy a local task.

## Reporting fallback pattern

If the main reporting channel is not wired, write a plain-text note in the repo session log with:
- session date
- current branch
- reporting path status
- task focus
- result summary

Then continue the build/test loop.

## Verification standard

A task is not done until one of these is true:
- the real artifact was exercised successfully, or
- a deterministic fallback was run and the limitation was recorded clearly.

## Linked detail

See `references/session-loop-checklist.md` for a concise checklist used during autonomous repo sessions.

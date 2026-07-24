---
name: notion-task-routing
description: "Route tasks between human and agent Notion databases, preserving project links and avoiding duplicate active items."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Notion, task-routing, productivity, databases, migration, agents]
---

# Notion Task Routing

Use this skill when a workspace separates **human-authored tasks** from **agent-authored tasks** across different Notion databases, and you need to audit, migrate, or reconcile them safely.

## When to use
- The workspace has an **Agent Tasks** database and a separate **Tasks ( To-Do )** database.
- Some tasks were created by humans and should remain in the original project-linked task base.
- Agent-generated tasks should stay in the agent database.
- You need to avoid duplicates, preserve relations, and verify migrations.

## Routing rule
- **Agent tasks** stay in the Agent Tasks database.
- **Human tasks** belong in the original Tasks ( To-Do ) database.
- If the task naming or metadata clearly indicates agentic work, keep it with agents.
- If the task is user-authored or manually designed, move it back to the human task base.

## Safe migration workflow
1. Identify all task databases involved.
2. Query the Agent Tasks database.
3. Classify each item:
   - agent-shaped: keep in Agent Tasks
   - human-designed: move to Tasks ( To-Do )
4. For tasks being moved:
   - create the destination page in Tasks ( To-Do )
   - preserve project, phase, priority, urgency, status, due date, and completion state when possible
   - set `Executor Type = Human`
   - set `Executor = Gabriel` unless the workspace uses a different human owner
5. Archive the source agent copy only after the destination is verified.
6. Re-run a query to confirm the task exists in the human base and is no longer active in the agent base.

## Verification checklist
- Human tasks exist in Tasks ( To-Do )
- Agent tasks remain in Agent Tasks
- No active duplicates remain in both databases
- Relations to projects and phases still resolve correctly

## Common pitfalls
- Some workspaces have **more than one** Agent Tasks database; inspect the actual schema first.
- Do not flatten relations if the source database already links to project/phase data.
- Do not rely on titles alone when the workspace uses metadata like `Executor Type`.
- If the task is already present in the destination base, do not create a duplicate.

## Reference
See `references/agent-human-task-routing.md` for a concise migration playbook and verification steps.

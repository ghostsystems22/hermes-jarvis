# Queue orchestration notes

This skill covers the always-on task queue pattern for mixed client, content, and 9/5 work.

## Proven operating pattern
- Airtable: queue and state machine.
- Notion: spec/context/SOPs.
- Hermes controller: always-on dispatcher on the VPS.
- Worker agents: disposable execution units.
- Human approval: required at Needs Review.

## Default flow
1. Read queued task.
2. Load linked context.
3. If context is missing, mark Needs Info.
4. Claim the task and dispatch a worker.
5. Worker performs the work and returns a draft/result.
6. Controller records outcome and next step.
7. Stop before Done if the work leaves the building.

## Useful statuses
Queued, Claimed, In Progress, Blocked, Needs Info, Needs Review, Done.

## Selection rules
- Protect revenue first.
- Then client deadlines.
- Then tasks with complete context.
- Then the smallest shippable item.

## Anti-patterns
- Notion as the queue.
- Workers updating Done directly.
- Guessing when context is absent.
- Treating orchestration as the project itself.

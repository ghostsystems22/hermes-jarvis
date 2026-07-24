# Agent ↔ Human Task Routing Playbook

## Goal
Move **human-designed tasks** out of an Agent Tasks database and back into the original project-linked **Tasks ( To-Do )** base, while leaving agent tasks in the Agent Tasks database.

## Typical signals
### Keep in Agent Tasks
- explicit agent naming
- numbered/generated phase tasks
- system work
- tasks already tagged `Executor Type = Agent`

### Move back to Tasks ( To-Do )
- human-authored task names
- manually designed deliverables
- work that was originally linked to projects in the human base
- entries that should be owned by `Executor Type = Human`

## Migration steps
1. Query the Agent Tasks database.
2. Group items by title and inspect metadata.
3. For each human task:
   - create a page in `Tasks ( To-Do )`
   - copy project / phase / due date / priority / urgency / status when present
   - set `Executor Type = Human`
   - set `Executor = Gabriel`
4. Archive the source page in Agent Tasks after the destination is verified.
5. Re-query both databases to ensure only the correct version remains active.

## Verification
- Human task exists in Tasks ( To-Do )
- Agent copy is archived
- No active duplicates remain
- Project relations still point correctly

## Notes
- If more than one Agent Tasks database exists, inspect the schema first.
- Prefer metadata over title-only classification when available.
- Keep the migration reversible until verification is complete.

# Notion access checks for queue systems

Use this when a queue worker or controller needs to read/write Notion during a 24/7 workflow.

## Access model
- Direct Notion API access uses a Notion integration token.
- Hosted Notion MCP uses OAuth and is a separate path.
- For Hermes queue automation, direct API access is usually the simplest stable setup.

## Required setup
1. Store the token in the Hermes environment used by the controller/worker host.
2. Share the target page/database with the integration inside Notion.
3. Verify access by searching for the exact project name.
4. If search returns 0, try shorter fragments and confirm the page/database ID.

## Common pitfall
- A valid token can still see 0 results if the page/database has not been shared with the integration.
- Another common miss is searching by the user’s project label instead of the exact Notion title.

## Operational rule
- Do not mark a queue task as blocked on Notion auth until sharing and title/ID checks are done.

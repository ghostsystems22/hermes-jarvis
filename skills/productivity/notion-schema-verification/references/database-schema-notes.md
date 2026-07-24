# Notion schema notes from live session

Observed against a live integration:

- The target task-manager ID `83745ca2a46282929a2001456cc8afa6` is a **database**.
- `GET /v1/databases/{id}` succeeds and returns database metadata.
- `GET /v1/pages/{id}` on that same ID fails with a validation error saying the ID is a database, not a page.
- A `search` query returned matching pages, which can be used to discover titled pages and then inspect their parent database/data source IDs.

Practical takeaway:
- Verify page vs database before choosing the Notion API endpoint.
- If metadata is sparse, inspect connected pages returned by search to infer schema or confirm integration access.

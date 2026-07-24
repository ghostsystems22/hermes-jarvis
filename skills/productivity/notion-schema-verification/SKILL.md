---
name: notion-schema-verification
description: Verify live Notion object type and schema before querying or writing, especially when IDs could be pages or databases.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Notion, schema, databases, pages, verification, troubleshooting]
---

# Notion Schema Verification

Use this skill when a Notion ID is known, but it is not obvious whether the target is a page, a database, or a data source.

## Trigger conditions
- A Notion URL/ID is provided and the API endpoint is unclear.
- The integration returns sparse metadata or confusing errors.
- A search result points to a page, but the task expects database records.

## Steps
1. **Resolve the object type first.**
   - Try the page endpoint only if the ID is known to be a page.
   - If the ID may be a database, verify with the database endpoint.
2. **Read the live metadata.**
   - Confirm whether the object is a page, database, or data source.
3. **Search before you write.**
   - Use Notion search to find the live page/title and inspect parent IDs.
4. **Only query the exact object type.**
   - Avoid assuming `/pages/{id}` when the ID is actually a database.
5. **If schema is sparse, infer from connected pages and search results.**

## Pitfalls
- A database ID can fail at `/pages/{id}` with a validation error.
- The same public URL can hide a database whose properties are not obvious at first glance.
- A sparse metadata response does not prove the integration has no access; it may just be the wrong endpoint or a minimal object response.

## Verification
- The API endpoint returns the expected object type.
- A search result or page read confirms the live title and parent context.

## Reference
- See `references/database-schema-notes.md` for the live-session example and endpoint behavior.

# Telegram -> Obsidian second-brain capture

Use this pattern when the user wants a Telegram bot or similar inbox to land raw ideas into an Obsidian vault for later triage.

## Canonical vault layout

- `00 Inbox/` — raw captures, one note per message/link
- `00 Inbox/queue.jsonl` — machine-readable triage queue for downstream agents
- `01 Sources/` — source notes grouped by domain (one note per source URL/domain)
- `02 Concepts/` — curated evergreen concept notes
- `90 MOCs/` — map-of-content / navigation notes

## Capture rules

1. Preserve the raw text first; do not over-process on ingest.
2. If a URL is present, also create/update a source note for that domain/path.
3. Write a JSONL queue entry so later agents can filter, score, or connect ideas without reparsing Markdown.
4. Keep the raw capture note immutable; downstream agents create separate concept notes rather than rewriting the inbox item.

## Suggested queue.jsonl schema

One JSON object per line:

- `id`: stable capture id
- `created`: ISO-8601 UTC timestamp
- `chat_id`: Telegram chat id or source channel id
- `message_id`: message id
- `title`: human-readable capture title
- `note_path`: absolute path to the raw note
- `source_url`: original URL, if any
- `source_kind`: `text`, `web`, `youtube`, `instagram`, etc.
- `tags`: normalized tags such as `raw`, `inbox`

## Good ingest behavior

- Accept text-only notes and link-only notes.
- If the source metadata fetch fails, still store the raw note and record the warning in the note body.
- Auto-create a minimal MOC / inbox index so the vault is navigable immediately.
- Prefer deterministic naming: timestamp + slug + short hash.

## Downstream agent handoff

A filtering agent can read `queue.jsonl` first, then open the corresponding raw note and source note, then decide whether to:

- summarize
- extract tasks
- create a concept note
- create backlinks between related ideas
- archive or ignore duplicates

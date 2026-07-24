---
name: second-brain-capture
description: Capture raw ideas, links, and messages into an Obsidian-style inbox for later triage and concept extraction.
platforms: [linux, macos, windows]
---

# Second-Brain Capture

Use this skill when the user wants a raw idea inbox, especially from Telegram or similar chat inputs, with later filtering by agents.

Preferred target: Obsidian vault. Use Notion only if the user explicitly prefers it or the vault path is unavailable.

## Core workflow

1. Capture first, process later.
2. Store every input as a raw Markdown note in an inbox folder.
3. If a URL is present, create a source note for the domain/path.
4. Append a machine-readable queue record for downstream triage agents.
5. Keep concept extraction separate from raw capture so the inbox stays immutable.
6. Create or refresh navigation notes / MOCs so the vault is immediately usable.

## Default vault layout

- `00 Inbox/` — raw captures
- `00 Inbox/queue.jsonl` — triage queue for downstream agents
- `01 Sources/` — source notes grouped by domain
- `02 Concepts/` — curated evergreen notes
- `90 MOCs/` — maps of content / navigation hubs

## Naming rules

- Use deterministic filenames: timestamp + slug + short hash.
- Normalize tags to a small, consistent set such as `raw`, `inbox`, `source`, `concept`.
- Preserve the original text in the note body even when metadata extraction succeeds.

## Ingest behavior

- Accept text-only messages and link-only messages.
- If metadata fetch fails, still save the raw note and record the warning in the note body.
- If the same source is seen again, append a backlink in the source note rather than duplicating the source page.
- Prefer Markdown and JSONL; avoid custom binary formats for the capture layer.

## Downstream triage

Later agents should read `queue.jsonl` first, then open the corresponding raw note and source note, and then decide whether to:

- summarize
- extract tasks
- create a concept note
- connect related ideas with wikilinks
- archive or ignore duplicates

## Support files

- `references/telegram-second-brain.md` — canonical Telegram -> Obsidian inbox pattern, schema, and handoff notes.

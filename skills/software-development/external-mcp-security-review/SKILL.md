---
name: external-mcp-security-review
description: "Review and integrate third-party MCP servers safely, with a bias toward least privilege and read-only first."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mcp, security, review, integration, obsidian, least-privilege]
---

# External MCP Security Review

Use this skill when a user wants to evaluate, connect, or harden a third-party MCP server before wiring it into Hermes.

## Default posture
- Treat every external MCP server as privileged access to user data.
- Prefer read-only or duplicate data sources first.
- Disable server-initiated sampling unless explicitly needed.
- Constrain writes with filesystem permissions, not just prompt instructions.

## Review workflow
1. Identify the transport: stdio (`npx`/`uvx`) or HTTP.
2. Inspect the repo metadata: `package.json`, README, SECURITY.md, AGENTS.md, tests, and source layout.
3. Look specifically for:
   - path traversal / symlink escape
   - arbitrary command execution
   - environment-variable leakage
   - unsafe deserialization or YAML handling
   - over-broad write/delete operations
   - search/indexing that can leak hidden files
4. Verify with real signals when possible:
   - tests pass
   - `npm audit` / dependency scan
   - explicit security docs
5. Recommend a least-privilege Hermes config.

## Hermes integration
Use the native MCP client with a dedicated server entry:

```yaml
mcp_servers:
  external_tool_name:
    command: "npx"
    args: ["-y", "package-name", "/path/to/data"]
    timeout: 120
    connect_timeout: 60
    sampling:
      enabled: false
```

If the server can write or delete data, start it against a test vault or read-only copy first.

## Red flags
- `exec`, `spawn`, `eval`, `Function`, shell string interpolation
- unrestricted path resolution or symlink-following outside the target root
- hidden-file access without explicit deny rules
- write/delete tools with no confirmation step
- `process.env` forwarded wholesale to subprocesses
- sampling enabled by default for an untrusted server

## Good outputs
When reporting back, give:
- verdict: safe / caution / reject
- the specific risks found
- the safest config snippet
- whether read-only mode is possible
- whether the server needs sampling disabled

## Linked notes
- `references/third-party-mcp-review.md` — checklist and an example Obsidian-vault MCP review

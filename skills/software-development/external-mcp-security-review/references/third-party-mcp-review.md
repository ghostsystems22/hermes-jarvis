# Third-party MCP review notes

## Example: Obsidian vault MCP server
Repository reviewed: `bitbonsai/mcpvault`

### What to check
- `package.json` scripts and dependencies
- `README.md` and `SECURITY.md`
- `AGENTS.md` or repo-specific instructions
- `src/` for path filtering, file I/O, and any subprocess usage
- tests for traversal, symlink, and hidden-file coverage

### Findings from the review
- No obvious command execution path was found in the server code reviewed.
- Path traversal and symlink escape defenses are present in the filesystem layer.
- Restricted locations like `.obsidian`, `.git`, and `node_modules` are blocked at any depth.
- `npm audit` still reports a moderate `gray-matter` / `js-yaml` advisory chain.

### Safer Hermes config
```yaml
mcp_servers:
  obsidian:
    command: "npx"
    args: ["-y", "@bitbonsai/mcpvault@latest", "/path/to/your/vault"]
    timeout: 120
    connect_timeout: 60
    sampling:
      enabled: false
```

### Operational guidance
- Prefer a duplicated or read-only vault first.
- Keep writes constrained by OS permissions.
- If the server can delete or move files, require a separate approval workflow.
- Verify behavior in the MCP inspector before connecting it to production notes.

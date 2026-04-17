# Claude Code Tutorial Plugin

A Claude Code plugin that teaches users how to use and extend Claude Code through interactive, hands-on tutorials.

## Repo Map

```
plugins/claude-code-tutorial/     # The actual plugin
├── .claude-plugin/plugin.json    # Plugin metadata (name, version, author)
├── commands/                     # Slash commands (/tutorial, /cheat-sheet-*)
├── skills/create-plugin/         # Auto-activating skill + helper script
└── .mcp.json                     # MCP server configuration
```

Root-level files:
- `install.sh` - One-line installer for end users
- `CHANGELOG.md` - Version history (Keep a Changelog format)
- `README.md` / `QUICKSTART.md` - User documentation

## How to Work Here

**This is a pure Claude Code plugin** - no build, no tests, no linting. Changes are validated by loading the plugin.

### Local Testing

```bash
claude --plugin-dir ./plugins/claude-code-tutorial
```

Then run `/claude-code-tutorial:tutorial` to verify commands work.

### Releasing

1. Update version in `plugins/claude-code-tutorial/.claude-plugin/plugin.json`
2. Add entry to `CHANGELOG.md` following Keep a Changelog format
3. Commit and push

### Creating/Modifying Commands

Commands are markdown files in `plugins/claude-code-tutorial/commands/`:
- Filename becomes the command name (e.g., `tutorial.md` → `/tutorial`)
- YAML frontmatter: `description`, `argument-hint`
- Body: Instructions Claude follows when command is invoked

### Creating/Modifying Skills

Skills live in `plugins/claude-code-tutorial/skills/<skill-name>/SKILL.md`:
- YAML frontmatter: `name`, `description` (triggers auto-activation)
- Body: Domain knowledge Claude uses when skill activates
- Optional `scripts/` subdirectory for helper scripts

## Key Files

| File | Purpose |
|------|---------|
| `plugins/claude-code-tutorial/.claude-plugin/plugin.json` | Plugin manifest - bump version here for releases |
| `CHANGELOG.md` | Version history - add entries here for releases |
| `plugins/claude-code-tutorial/commands/tutorial.md` | Main tutorial entry point |
| `plugins/claude-code-tutorial/skills/create-plugin/SKILL.md` | Plugin scaffolding skill |

## Gotchas

- **Command naming**: Full format is `plugin-name:command` (e.g., `/claude-code-tutorial:tutorial`). Short form `/tutorial` only works if no conflicts.
- **No Python package**: This repo used to have a `uvx` CLI (`src/`). It was removed in v1.2.0. Use the skill or script directly.
- **Marketplace structure**: The `.claude-plugin/marketplace.json` at root defines this as a marketplace; the actual plugin is in `plugins/`.

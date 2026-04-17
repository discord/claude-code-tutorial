# Claude Code Tutorial Plugin - Quick Start

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/discord/claude-code-tutorial/main/install.sh | bash
```

## Start Learning

```bash
claude
/tutorial
```

That's it!

## Use the Tutorial

```bash
# Run the tutorial
/tutorial
```

Claude will ask what you want to work on - pick something real (understand part of the codebase, or build/modify a feature). The tutorial teaches by having you actually do things, not just read concepts.

## Available Commands

| Command | Description |
|---------|-------------|
| `/tutorial` | Main tutorial - learn Claude Code basics |
| `/tutorial-advanced` | Advanced tutorial - extend Claude Code |
| `/cheat-sheet-basic` | Quick reference for basics |
| `/cheat-sheet-advanced` | Quick reference for extensions |

## Plugin Management

```bash
# Inside Claude Code:
/plugin                    # Open plugin manager UI
/plugin list               # See installed plugins
```

## Creating Your Own Plugin

To create your own plugin:

```bash
# Create the directory structure
mkdir -p my-plugin/.claude-plugin
mkdir -p my-plugin/commands
mkdir -p my-plugin/skills

# Create the plugin manifest
cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-plugin",
  "description": "My custom Claude Code plugin",
  "version": "1.0.0",
  "author": {
    "name": "your-github-username"
  }
}
EOF

# Test locally with --plugin-dir
claude --plugin-dir ./my-plugin
```

## Documentation

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
- [MCP Protocol](https://modelcontextprotocol.io)

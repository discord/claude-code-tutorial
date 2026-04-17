---
name: create-plugin
description: Create a new Claude Code plugin skeleton. Use when someone wants to create a plugin, start a new plugin project, or scaffold plugin directories.
---

# Create Plugin Skill

Creates a new Claude Code plugin with the standard directory structure.

## What it creates

```
[plugin-name]/
├── .claude-plugin/
│   └── plugin.json     # Plugin manifest
├── commands/           # Slash commands
├── skills/             # Auto-activating domain knowledge
├── agents/             # Autonomous task performers
├── rules/              # File-pattern guidelines
├── .mcp.json           # MCP configuration (if examples enabled)
└── README.md           # Documentation
```

## Usage

Ask Claude to create a plugin:
- "Create a plugin called my-helper"
- "Scaffold a new plugin for code review"
- "Make a plugin skeleton with examples"

## Required Information

1. **Plugin name** - lowercase with hyphens (e.g., `my-plugin`)
2. **Description** - What the plugin does
3. **Author** - GitHub username (for install instructions)
4. **Include examples?** - Whether to add example command/skill files

## Process

1. Ask for the required information if not provided
2. Run the create-plugin.py script from this skill's scripts directory
3. The script creates all directories and files
4. Tell user how to test: `claude --plugin-dir ./[name]`

## Script Location

The creation script is at: `skills/create-plugin/scripts/create-plugin.py` (relative to the plugin root)

Run it with:
```bash
# With all arguments
python plugins/claude-code-tutorial/skills/create-plugin/scripts/create-plugin.py my-plugin "My plugin description" --author myusername --examples

# Interactive mode (prompts for each value)
python plugins/claude-code-tutorial/skills/create-plugin/scripts/create-plugin.py
```

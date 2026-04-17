---
description: Quick reference for extending Claude Code - commands, skills, agents, hooks, rules, MCP
---

# Claude Code Cheat Sheet - Advanced

Print this cheat sheet for the user:

---

## When to Extend Claude Code

| You have... | Create a... | Example |
|-------------|-------------|---------|
| Repeated workflow | **Command** | `/commit`, `/test` |
| Complex multi-step task | **Agent** | Code reviewer, test writer |
| Domain knowledge Claude lacks | **Skill** | Internal APIs, design systems |
| Auto-run after edits | **Hook** | Format on save, lint |
| File-specific guidelines | **Rules** | Security for auth code |
| Need live external data | **MCP** | Live docs, browser |

---

## Model Selection

| Model | Best For |
|-------|----------|
| **Sonnet** | Flow state coding, rapid iteration |
| **Opus** | Planning, complex tasks, background work |
| **Recommended** | Auto-selected based on task |

---

## Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required manifest
├── commands/                 # Slash commands (*.md)
├── skills/                   # Auto-activating (*/SKILL.md)
├── agents/                   # Task performers (*.md)
├── hooks/                    # Event handlers (*.sh)
├── rules/                    # Guidelines (*.md)
├── .mcp.json                 # External tool connections
└── README.md
```

---

## Creating Extensions

**Commands** - Simplest to create:
```markdown
---
description: Short description shown in /help
argument-hint: [optional-args]
---
Instructions for Claude when command is invoked...
```

**Skills** - Auto-activate based on context:
```markdown
---
name: my-skill
description: When this activates
activation:
  - keyword triggers
---
Domain knowledge and instructions...
```

**Agents** - For complex tasks:
```markdown
---
name: my-agent
description: What this agent does
tools: [Read, Write, Bash(git:*)]
---
Task instructions and output format...
```

---

## Quick Commands

```bash
# Plugin management (inside Claude Code)
/plugin                                    # Open plugin manager UI
/plugin marketplace add owner/repo         # Add marketplace source
/plugin install plugin-name@marketplace    # Install from marketplace

# Creating your own plugin
mkdir -p my-plugin/.claude-plugin
# Create plugin.json with name, description, version, author
# Add commands/, skills/, agents/ directories as needed
```

---

## Context Management

| Command | Purpose |
|---------|---------|
| `/context` | Visualize current context usage (tokens, files, conversation) |
| `/rewind` or `Esc+Esc` | Rewind conversation, code, or both to a checkpoint |
| `/clear` | Start fresh conversation (keeps files) |
| `/compact` | Summarize conversation to reduce context |

**Tip:** Use `/context` to monitor token usage before hitting limits.

---

## Learn More

- `/tutorial-advanced` - Full walkthrough of extending Claude Code
- `/cheat-sheet-basic` - Reference for Claude Code basics

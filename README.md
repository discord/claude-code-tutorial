# Claude Code Tutorial Plugin

**Learn Claude Code by doing.** This plugin provides interactive tutorials that teach you Claude Code through hands-on exercises with your own code.

## Quick Start

**1. Install Claude Code** (if you haven't already):

   See [Claude Code Setup Guide](https://code.claude.com/docs/en/setup)

**2. Install the tutorial plugin:**

```bash
curl -fsSL https://raw.githubusercontent.com/discord/claude-code-tutorial/main/install.sh | bash
```

**3. Start the tutorial:**

```bash
claude
/claude-code-tutorial:tutorial
```

That's it!

## Commands

| Command | Description |
|---------|-------------|
| `/claude-code-tutorial:tutorial` | Main tutorial - learn Claude Code basics with hands-on exercises |
| `/claude-code-tutorial:tutorial-advanced` | Advanced tutorial - learn to extend Claude Code |
| `/claude-code-tutorial:cheat-sheet-basic` | Quick reference for modes, workflow, and key commands |
| `/claude-code-tutorial:cheat-sheet-advanced` | Quick reference for extending Claude Code |

**Note:** The full command format is `plugin-name:command`. You can also try just `/tutorial` if there's no naming conflict with other plugins.

## The Tutorial

### How It Works

Just type `/claude-code-tutorial:tutorial` and Claude will:

1. **Ask what you want to work on** - Pick something real (understand code, build a feature, modify existing code)
2. **Track your progress** - Creates `.claude/tutorial-progress.md` so you can resume anytime
3. **Teach by doing** - You'll apply each concept to your actual project as you learn
4. **Summarize key takeaways** - Quick reference for when to use what

### Basic Tutorial (`/claude-code-tutorial:tutorial`)

Learn how to USE Claude Code:
- Natural interaction in your terminal
- The 4 permission modes and when to use each
- Planning effectively for best results
- Where you'll spend your time (hint: not writing code)
- Hands-on practice with your code

### Advanced Tutorial (`/claude-code-tutorial:tutorial-advanced`)

Learn how to EXTEND Claude Code:
- Create custom slash commands
- Build skills (auto-activating domain knowledge)
- Configure agents for complex tasks
- Set up hooks for automation
- Define rules for your codebase
- Connect external tools via MCP
- Context engineering (SPEC/PLAN/TODO pattern)
- Parallel development with worktrees

## Key Concepts

### The Planning Pattern

```
Plan → Review → Test First → Implement Step by Step → Verify → Commit
```

### Where You'll Spend Your Time

With AI coding, most time goes to THINKING, RESEARCHING, PLANNING, and REVIEWING - not writing. The writing is fast; front-load your thinking.

### Permission Modes (Shift+Tab to cycle)

| Mode | File Edits | Shell Commands | Use When |
|------|------------|----------------|----------|
| Default | Ask | Ask | Learning, sensitive code |
| Accept Edits | Auto | Ask | Active development |
| Plan | Blocked | Blocked | Exploring, designing |
| Agent (YOLO)* | Auto | Auto | Parallel async work |

*Agent mode requires: `claude --dangerously-skip-permissions` on startup

### When to Extend Claude Code

| You have... | Create a... |
|-------------|-------------|
| Repeated workflow you run often | **Slash command** (`/commit`, `/test`) |
| Complex multi-step task | **Agent** (structured output, autonomous) |
| Domain knowledge Claude doesn't have | **Skill** (design system, internal APIs) |
| Something to auto-run after edits | **Hook** (format on save, lint) |
| File-specific guidelines | **Rules** (security rules for auth code) |
| Need live external data | **MCP** (live docs, browser automation) |

## Plugin Structure

```
claude-code-tutorial/
├── plugins/claude-code-tutorial/
│   ├── .claude-plugin/
│   │   └── plugin.json          # Plugin metadata
│   ├── commands/
│   │   ├── tutorial.md          # Main tutorial entry point
│   │   ├── tutorial-advanced.md # Extending Claude Code
│   │   ├── cheat-sheet-basic.md # Quick reference - basics
│   │   └── cheat-sheet-advanced.md
│   ├── skills/
│   │   └── create-plugin/       # Plugin creation skill
│   │       ├── SKILL.md
│   │       └── scripts/
│   │           └── create-plugin.py
│   └── .mcp.json                # MCP config (Context7, Playwright)
├── CHANGELOG.md                 # Version history
├── QUICKSTART.md
└── README.md
```

## Creating Your Own Plugin

Ask Claude to create a plugin for you:

```
> Create a plugin called my-helper for code review
```

Claude will use the `create-plugin` skill to scaffold the directory structure.

Or use the script directly:

```bash
# Interactive mode
python plugins/claude-code-tutorial/skills/create-plugin/scripts/create-plugin.py

# Or with arguments
python plugins/claude-code-tutorial/skills/create-plugin/scripts/create-plugin.py my-plugin "My plugin description" --author myusername --examples
```

Or manually:

```bash
# Create directory structure
mkdir -p my-plugin/.claude-plugin
mkdir -p my-plugin/commands

# Create plugin.json
cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-plugin",
  "description": "My custom plugin",
  "version": "1.0.0",
  "author": { "name": "your-github-username" }
}
EOF

# Test locally
claude --plugin-dir ./my-plugin
```

## Documentation

- [Claude Code Docs](https://code.claude.com/docs)
- [Setup Guide](https://code.claude.com/docs/en/setup)
- [MCP Protocol](https://modelcontextprotocol.io)

## License

MIT

---
description: Quick reference for Claude Code basics - modes, workflow, key commands
---

# Claude Code Cheat Sheet - Basics

Print this cheat sheet for the user:

---

## The Workflow

```
Plan → Review → Test First → Implement Step by Step → Verify → Commit
```

**The shift:** With AI coding, most time goes to THINKING, RESEARCHING, PLANNING, and REVIEWING - not writing. Writing the code is fast; front-load your thinking.
---

## Permission Modes

Press **Shift+Tab** to cycle between modes.

| Mode | File Edits | Shell Commands | Best For |
|------|------------|----------------|----------|
| **Default** | Ask | Ask | Learning, sensitive code |
| **Accept Edits** | Auto | Ask | Active development |
| **Plan** | Blocked | Blocked | Exploration, design |
| **Agent (YOLO)*** | Auto | Auto | Parallel async work |

*Agent mode requires starting Claude with: `claude --dangerously-skip-permissions`

Once enabled on startup, Shift+Tab includes Agent mode in the cycle.

---

## Key Commands & Shortcuts

| Action | How |
|--------|-----|
| Check/change model | `/models` |
| Get help | `/help` |
| Cycle permission modes | `Shift+Tab` |
| Interrupt Claude | `Escape` |
| **Rewind changes** | `Esc + Esc` or `/rewind` |
| View context usage | `/context` |
| Save persistent note | `/memory` + text |
| Resume after interrupt | Say "continue" |

---

## Recovery with Checkpoints

Claude Code automatically tracks file edits, creating checkpoints before each change.

Press **Esc + Esc** (or `/rewind`) to open the rewind menu:
- **Conversation only** - rewind messages, keep code
- **Code only** - revert files, keep conversation
- **Both** - full restore

**Note:** Only tracks Claude's direct file edits (not bash commands like `rm`, `mv`, `cp`).

---

## Quick Tips

1. **Press Escape to interrupt** - say "continue" to resume without losing your place
2. **Start new codebases in Plan mode** - explore safely before making changes
3. **Front-load planning** - be clear about what you want before asking
4. **Review carefully** - Claude writes fast; verify it wrote what you meant
5. **Tests passing ≠ done** - you're responsible for verifying code actually works as intended

---

## Learn More

- `/tutorial` - Full walkthrough of Claude Code basics
- `/cheat-sheet-advanced` - Reference for extending Claude Code (commands, skills, agents, etc.)

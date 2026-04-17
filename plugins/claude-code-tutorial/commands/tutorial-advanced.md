---
description: Learn to extend Claude Code with custom commands, skills, agents, hooks, and more
argument-hint: [commands | skills | agents | hooks | rules | mcp]
---

# Role Definition

You are teaching advanced Claude Code customization. You're helping the user extend Claude Code for their specific workflow.

**Key teaching principles:**
- Emphasize practical application - "when would you actually use this?"
- Show real examples from this plugin
- Connect concepts: "Commands are explicit, skills are automatic, agents are isolated"
- Track which parts they've completed

**Failure modes to avoid:**
- Don't dump all information at once - progressive disclosure
- Don't skip the "when to use this" context
- Don't forget to link back to their workflow goals
- Don't lose track of which parts they've completed

---

# Advanced Tutorial: Extending Claude Code

## No Arguments → Welcome & Offer Guidance

If the user just typed `/tutorial advanced` with no arguments:

---

**Welcome to the Advanced Tutorial!**

You've learned how to USE Claude Code - now let's learn how to EXTEND it.

You can customize Claude with:

- **Commands** - Create your own `/slash-commands`
- **Skills** - Add domain knowledge that activates automatically
- **Agents** - Build autonomous task performers
- **Hooks** - Automate actions on events (format on save, block dangerous commands)
- **Rules** - Define behavioral guidelines for your codebase
- **MCP** - Connect external tools (databases, APIs, browsers)

**Here's what we'll build together:**

Throughout this tutorial, you have two options:

**Option 1: Learn with examples**
- I'll show you each component using the examples in this plugin
- Quick, no commitment, just learning
- You can create your own plugin later when you have a specific need

**Option 2: Build YOUR plugin**
- Create a plugin for YOUR workflow as we learn each component
- By the end, you'll have something useful you can actually use
- We'll create the plugin structure manually
- You'll need to reload Claude (quit and `claude --resume`) after we create it

**Which sounds better?**

Or tell me: what kind of workflow would you like to automate? (Examples: testing workflow, commit helpers, code review checklist, deployment automation, etc.)

[Wait for their response]

[If they choose to build their plugin:]
"Great! Let's start by setting up your plugin structure. First, what should we call it? Think about what workflow you want to automate - the name should be descriptive."

[If they choose examples only:]
"No problem! We'll explore the examples in this tutorial plugin. If you change your mind later and want to build your own plugin, just let me know."

---

**How do you want to proceed?**

1. **Guide me through it** - I'll show you each component with hands-on examples
2. **Let me pick a topic** - Jump to a specific component (commands, skills, agents, hooks, rules, mcp, context)
3. **Build my own plugin** - Walk through each section while building YOUR plugin as we go
4. **I'm impatient, skip to the TL;DR** - Jump straight to the quick reference

[If they say "guide me" → Start guided walkthrough with Part 0, ask if they want to build their plugin along the way]
[If they pick a topic → Jump to that section]
[If they choose option 3 → Start with Part 0, guide them through manual plugin creation, then continue through each part adding components to THEIR plugin]
[If they choose option 4 (TL;DR) → Jump to Part 10 quick reference table, then offer: "Want to dive deeper into any of these? Just pick a topic or say 'guide me' to start the full walkthrough."]

---

## Guided Walkthrough

### Part 0: Plugins (Where Everything Lives)

"Before we dive into individual components, let's talk about **plugins** - they're how you organize and share your Claude Code extensions.

**What's a plugin?**

A plugin is a folder that bundles related extensions together:
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json     # Required manifest
├── commands/           # Slash commands (/commit, /test)
├── skills/             # Auto-activating domain knowledge
├── agents/             # Autonomous task performers
├── hooks/              # Event-driven automation scripts
├── rules/              # File-pattern guidelines
├── .mcp.json           # External tool connections
└── README.md           # Documentation
```

**Why use plugins?**
- **Organization** - Keep related extensions together
- **Sharing** - Share with others via GitHub
- **Portability** - Move between projects easily

---

[If user chose to BUILD their plugin:]

### Creating YOUR Plugin

"Perfect! Let's create your plugin now.

**First, what should we call your plugin?**

[Wait for their suggestion - e.g., "test-helpers", "deployment-tools", "code-review-assistant"]

Great name! This tutorial includes a helper script to create the plugin skeleton. Let me run it:

```bash
# Find and run the create-plugin script from this tutorial plugin
python /path/to/claude-code-tutorial/scripts/create-plugin.py [plugin-name] "[description]" --author [username] --examples
```

[Run the create-plugin.py script with their chosen name, description, and GitHub username]

**Your plugin structure is ready!**

The script created:
- `commands/` - Ready for your commands (with an example)
- `skills/` - Ready for your skills (with an example)
- `agents/` - Ready for your agents
- `rules/` - Ready for your rules
- `.claude-plugin/plugin.json` - Manifest with metadata
- `.mcp.json` - MCP configuration template
- `README.md` - Documentation with install instructions

**Important: Loading your new plugin**

After creating your plugin, you need to reload Claude to see it:

1. **Quit Claude** (Ctrl+C or type `exit`)
2. **Restart with your plugin:**
   ```bash
   claude --plugin-dir ./[plugin-name]
   ```

Or if you want to resume your conversation:
   ```bash
   claude --plugin-dir ./[plugin-name] --resume
   ```

Your new commands/skills won't appear until you reload!

**Testing your plugin locally:**

You can test your plugin by starting Claude with the `--plugin-dir` flag:

```bash
claude --plugin-dir ./my-plugin
```

This loads your plugin for the current session. Great for development!

**Publishing to GitHub (later):**

When you're ready to share, push to GitHub and others can install with:
```
/plugin marketplace add your-username/your-plugin-name
/plugin install your-plugin-name@your-username-your-plugin-name
```

Ready for Part 1: Commands?"

---

[If user chose to LEARN with examples:]

### Understanding Plugin Structure

"Here's how plugins are structured. You can create your own later by making the directory structure manually.

**Plugin manifest** (`.claude-plugin/plugin.json`):
```json
{
  "name": "my-plugin",
  "description": "What this plugin does",
  "version": "1.0.0",
  "author": {
    "name": "your-github-username"
  }
}
```

**Installing plugins:**

In Claude Code, use the `/plugin` command to open the plugin manager:
- **Installed** tab - See what you have enabled
- **Discover** tab - Browse available plugins from marketplaces

Or use commands:
```
/plugin marketplace add owner/repo    # Add a marketplace source
/plugin install plugin-name@marketplace  # Install from marketplace
```

Ready for Part 1: Commands?"

---

### Part 1: Commands (The Easiest Win)

**Note: Commands are now part of Skills**

Recently, Claude Code merged slash commands into the Skills system. Your existing commands in `.claude/commands/` still work exactly the same - no migration needed.

Going forward, Anthropic recommends creating Skills instead of standalone commands. Skills offer more flexibility (subagent support, auto-invocation control, progressive disclosure).

For simple workflows, commands are still fine. Think of them as "workflow-type skills" with explicit `/name` invocation.

Commands still work. Skills are the future. We'll cover both.

---

"Let's start with **commands** - they're the easiest way to extend Claude Code.

A command is just a markdown file. The filename becomes the command name:
- `commit.md` → `/commit`
- `review.md` → `/review`

**Let's create one together.**

What's something you do repeatedly? Examples:
- Run a specific test suite
- Generate boilerplate code
- Check for common issues

Tell me, and I'll help you create a command for it."

Wait for response, then guide them through creating a command:

"Great! Let's create that command. Here's the structure:

```markdown
---
description: What this command does (shows in /help)
argument-hint: <required> [optional]
allowed-tools: Read, Bash(npm test:*)
---

# Your Command

Instructions for Claude go here...
```

**Key parts:**
- `description` - Required, shows in autocomplete
- `argument-hint` - Shows users what to type
- `allowed-tools` - Restrict what Claude can do (safety!)
- `$ARGUMENTS` - User's input after the command name

Let me create this command file for you. Where should I put it?
- `.claude/commands/` - Just for you (not in git)
- Your plugin folder - Shareable with team

Which do you prefer?"

Create the command, then have them try it.

"Now try your new command! Type `/[command-name]` and see it work.

---

[If user is building their plugin:]

### Add This Command to YOUR Plugin

"Now let's add this command to your plugin!

Based on what you want to automate, let's create `[command-name].md`:

**File location:**
`[plugin-path]/commands/[command-name].md`

[Help them write the command file based on their workflow]

**Test it:** Start Claude with your plugin:
```bash
claude --plugin-dir ./my-plugin
```

Then try your new `/<command-name>` command!

**Note:** This same pattern continues for Parts 2-6. After each section, I'll offer to add that component (skill, agent, hook, rule, MCP) to your plugin. By the end, you'll have a complete, working plugin."

---

Ready to learn about skills?"

---

### Part 2: Skills (Domain Knowledge)

"**Skills** are different from commands. Commands are invoked explicitly (`/command`). Skills are *designed* to activate automatically based on context - but this isn't guaranteed.

**The reality:** Auto-activation works best when your description includes phrases people actually say. But Claude might not always pick up on the context, especially for subtle triggers.

**Three ways to use skills:**

1. **Hope for auto-activation** - If your description is good, Claude *should* load the skill when relevant context appears. But don't count on it for critical workflows.

2. **Explicitly invoke** - Mention the skill by name to be sure it's referenced:
   - 'Use the design-system skill to review this component'
   - 'Load my team-conventions skill and check this PR'

   This is a good practice during **planning** or when you want to guarantee Claude has context from a skill you've created.

3. **Pair with a command** - Create a command that explicitly loads the skill:
   - `/antipatterns` loads the skill, gets your diff, runs a systematic check
   - Best of both worlds: explicit invocation with a structured workflow

**Example: The Anti-Patterns Skill**

This plugin includes `avoiding-ai-anti-patterns` - a skill with checklists for common mistakes:
- Silent fallbacks
- Import try/except patterns
- Over-mocking in tests
- Incomplete TODOs

You can:
- Ask naturally: 'Check this code for anti-patterns' (may auto-activate)
- Be explicit: 'Use the anti-patterns skill to review my changes' (guaranteed)
- Use the command: `/antipatterns` (structured workflow)

**Skill structure:**
```
skills/
  my-design-system/
    SKILL.md           # Main file - concise overview (required)
    references/        # Detailed docs loaded on demand
      components.md
      accessibility.md
      tokens.md
    scripts/           # Deterministic automation
      validate-tokens.sh
      check-a11y.py
```

**Progressive disclosure** - This is key to managing context:

Claude's context window is limited. If you dump everything into SKILL.md, you waste tokens on details that might not be relevant. Instead:

1. **SKILL.md** (~500 lines max) - High-level overview, quickstart, guardrails
2. **references/** - Detailed documentation Claude loads *only when needed*
3. **scripts/** - Deterministic steps that don't need AI judgment (validation, linting, API calls)

**Why this matters:**
- Claude reads SKILL.md to understand what's available
- When it needs details on accessibility, it loads `references/accessibility.md`
- When it needs to validate tokens, it runs `scripts/validate-tokens.sh`
- You get comprehensive coverage without blowing your context budget

**The key is the description** - it tells Claude WHEN to activate:

```yaml
---
name: my-design-system
description: Design system components, tokens, and accessibility rules. Use when building UI, reviewing components, or checking design consistency.
---
```

Include trigger phrases people actually say: 'review this component', 'check accessibility', 'use the right tokens'.

**Let's create a skill.** What domain knowledge would help you? Examples:
- Your team's coding conventions
- A framework you use often
- Testing patterns for your project"

Guide them through creating a skill, emphasizing:
- Keep SKILL.md concise (<500 lines)
- Put details in `references/` subdirectory
- Description should include trigger phrases (but don't rely solely on auto-activation)
- Consider pairing with a command for guaranteed access

"Try it! Either:
- Ask me 'Use the anti-patterns skill to check my recent changes' (explicit)
- Run `/antipatterns` (structured workflow)

**Pro tip:** When planning or doing something important, explicitly mention the skill by name. Don't leave it to chance.

Ready for agents?"

---

### Part 3: Agents (Mini Claude Sessions)

"**Agents** are mini Claude sessions - each one gets its own context window, works autonomously, and returns structured results back to the main conversation.

**Command vs Agent:**
- Command: 'Do this one thing'
- Agent: 'Figure out what needs doing, do it systematically, report results'

**Why agents matter - two key benefits:**

1. **Parallel execution** - Claude can dispatch multiple agents simultaneously:
   - Run code review on 5 files at once
   - Research multiple topics in parallel
   - Execute migration steps across different modules

   This is powerful for workflows that would otherwise be sequential.

2. **Context isolation** - Each agent gets its own context window and returns only minimal/structured output to the main Claude:
   - Noisy operations (running builds, large test suites) don't pollute your main context
   - Agent does the heavy lifting, returns a clean summary
   - Your main conversation stays focused

**When to use agents:**
- Code review with structured JSON output
- Test generation across multiple files
- Migration tasks that touch many locations
- Anything with noisy output (build systems, large searches)
- Research tasks you want to run in parallel

**Agent structure:**
```yaml
---
name: code-reviewer
description: Thorough code reviewer. Use after making changes.
tools: Read, Glob, Grep  # Restricted capabilities
---

# Instructions

Detailed multi-step process...
Output schema...
```

**Agent Model Selection**

By default, agents use **Haiku** (claude-3-haiku) - a fast but less capable model. This is fine for simple tasks but may struggle with complex reasoning.

**To use a smarter model:**

Set the `CLAUDE_SUBAGENT_MODEL` environment variable:
```bash
export CLAUDE_SUBAGENT_MODEL=claude-sonnet-4-5
```

Or in your shell profile (~/.zshrc, ~/.bashrc):
```bash
echo 'export CLAUDE_SUBAGENT_MODEL=claude-sonnet-4-5' >> ~/.zshrc
```

**Trade-offs:**
- **Haiku (default)**: Fast, cheap, good for simple/mechanical tasks
- **Sonnet**: Smarter, better for code review, test generation, complex analysis
- **Opus**: Smartest, but slow and expensive for agents

**Downside:** You'll need to manually update this when new model versions release (e.g., when Sonnet 4.6 comes out).

**Key differences from commands:**
- `tools` restricts what the agent can do
- Detailed process instructions
- Structured output format (usually JSON)
- Runs in isolated context, returns clean results

**Three ways to invoke agents:**

1. **Auto-dispatch** - Claude may dispatch agents automatically if the context seems right. This is hit-or-miss; don't rely on it for critical workflows.

2. **Explicit slash command** - Invoke directly with `/@agent-name`:
   ```
   /@code-reviewer
   ```

3. **From within other commands** - Tell Claude to dispatch specific agents in your command's instructions. This lets you combine multiple agents into a single workflow:
   ```markdown
   # /precommit command
   Run these agents in parallel and report results:
   1. Dispatch the `linter` agent on changed files
   2. Dispatch the `type-checker` agent
   3. Dispatch the `test-runner` agent on affected tests

   Summarize all issues found.
   ```

This plugin includes two agents:
- `code-reviewer` - Structured code review
- `test-writer` - Generates comprehensive tests

Want to create an agent, or see how the existing ones work?"

Show them an existing agent or help create one.

---

### Part 4: Hooks (Event-Driven Automation)

"**Hooks** run scripts when specific events occur in Claude Code.

**Important:** Hooks don't run automatically just because a script exists. You must explicitly enable them in `settings.json`. This is intentional - hooks can slow down your workflow or block operations, so you opt-in to each one.

**Two parts to a hook:**

1. **The script** - Lives in your plugin or `.claude/hooks/`:
```bash
#!/bin/bash
# hooks/format-on-write.sh
INPUT=$(cat)
FILE_PATH=$(echo \"$INPUT\" | jq -r '.tool_input.file_path // empty')
[[ -f \"$FILE_PATH\" ]] && prettier --write \"$FILE_PATH\" 2>/dev/null || true
exit 0
```

2. **The configuration** - Enables it in `.claude/settings.json`:
```json
{
  \"hooks\": {
    \"PostToolUse\": [{
      \"matcher\": \"Edit|Write\",
      \"hooks\": [{
        \"type\": \"command\",
        \"command\": \"./.claude/hooks/format-on-write.sh\"
      }]
    }]
  }
}
```

**Hook events:**
- `PreToolUse` - Before a tool runs (can block with exit code 2)
- `PostToolUse` - After a tool completes (great for formatting)
- `Notification` - Permission prompts, idle warnings

**The most common use:** Auto-lint after Claude edits files.

**Performance note:** Hooks run on every matching event. If your hook is slow (e.g., running a full linter), it will slow down your entire workflow. Keep hooks fast or make them selective with the `matcher` pattern.

This plugin includes `hooks/format-on-write.sh` ready to use. Want to add it to your settings?"

Help them configure the hook if interested.

---

### Part 5: Rules (Behavioral Guidelines)

"**Rules** are guidelines that apply based on file patterns. Unlike skills (which activate on context), rules activate on **file paths**.

**Example:**
```yaml
---
paths:
  - \"**/*.py\"
  - \"**/*.js\"
---

# Code Style Rules

When working with these files:
- Use snake_case for Python
- Use camelCase for JavaScript
```

**When to use rules:**
- Code style enforcement
- Security requirements for sensitive paths
- Language-specific conventions

This plugin has rules for `code-style.md` and `security.md`. Take a look!

Rules are simpler than skills - just define `paths` and write guidelines."

---

### Part 6: MCP (External Tools)

"**MCP** (Model Context Protocol) connects Claude to external tools.

**Honest take:** MCPs are NOT a silver bullet that gives Claude the ability to do anything. In most cases, an existing CLI tool works better - Claude can already run shell commands, so wrapping `git` or `docker` in an MCP adds complexity without benefit.

**The three legitimate use cases for MCPs:**

1. **Context augmentation** - Enriching Claude's knowledge with live data (docs, search)
2. **Web automation** - Browser control that requires structured interaction
3. **Custom tooling experiments** - Prototyping new workflows (though a CLI is often easier to build)

**1. Context7 - Up-to-date library docs**

A useful example for a common failure mode: Claude's training data gets stale. Context7 fetches current, versioned documentation so Claude doesn't hallucinate outdated APIs.

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

**Try it:** Ask me to look up something in a library you use:
- 'use context7 to look up the Click library argument parsing'
- 'use context7 for the latest pytest fixtures docs'

Context7 fetches real docs instead of relying on training data.

**2. Playwright - Browser automation**

Essential for web development, E2E testing, and scraping. Uses accessibility trees (not screenshots) so it's fast and reliable.

```bash
claude mcp add playwright -- npx -y @playwright/mcp
```

**What it enables:**
- 'navigate to localhost:3000 and click the login button'
- 'fill out the signup form and submit'
- 'take a snapshot of the current page state'
- Generate E2E test code from interactions

**Other browser MCPs** (if you need them):
```bash
# Puppeteer - screenshot-based, good for visual QA
claude mcp add puppeteer -- npx -y @modelcontextprotocol/server-puppeteer

# Chrome DevTools - raw CDP access for deep debugging
claude mcp add devtools -- npx -y @anthropic/mcp-server-chrome-devtools
```

**Configuration** (`.mcp.json`):
```json
{
  \"mcpServers\": {
    \"context7\": {
      \"type\": \"stdio\",
      \"command\": \"npx\",
      \"args\": [\"-y\", \"@upstash/context7-mcp@latest\"]
    },
    \"playwright\": {
      \"type\": \"stdio\",
      \"command\": \"npx\",
      \"args\": [\"-y\", \"@playwright/mcp\"]
    }
  }
}
```

**MCP management:**
```bash
claude mcp add <name> -- <command>   # Add
claude mcp list                       # List installed
claude mcp remove <name>              # Remove
```

**In Claude Code:** Type `/mcp` to see which MCPs are connected and disconnect ones you don't need.

**Antipattern: Too many MCPs**

Don't load up on MCPs you aren't actively using. Each connected MCP eats into your context window - their tool definitions get loaded at startup. If you have 10 MCPs connected but only use 2, you're wasting context on 8 unused tool definitions.

Only add MCPs you'll actually use for your current workflow.

**Finding more MCPs:**
- [Smithery.ai](https://smithery.ai) - Browse MCP servers
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Community list

Want to try Context7 right now? Tell me a library and I'll look up its docs."

---

### Part 7: Context Engineering

"As you work on bigger tasks, you'll hit **context limits** - conversations get too long and Claude loses track.

**Why this matters:**

Claude's performance degrades as context grows. The longer your conversation:
- The more likely Claude makes mistakes
- The harder it is to follow earlier instructions accurately
- The more "noise" competes with your actual task

When context fills up and gets compacted, information gets summarized or lost. You might lose important decisions, file contents, things Claude already tried, error messages, or why a particular approach didn't work.

**Bottom line:** A fresh, focused context produces better results than a long, sprawling one. Manage context proactively.

Here's how to manage this:

**Spec-Driven Development**

One pattern people find successful: create documentation files that persist your progress.

```
project/
├── SPEC.md                 # What you're building (requirements)
├── IMPLEMENTATION_PLAN.md  # How you'll build it (steps)
└── TODO.md                 # Current progress (checkboxes)
```

**Why this works:**
- When context gets long, `/compact` or start fresh
- Claude reads these files and picks up where you left off
- You have a paper trail of decisions and progress
- Easy to hand off to another person (or Claude instance)

Ask Claude to help draft these - it'll create something reasonable for your task.

**Fresh Context Review**

Claude tends to be overly positive about code it just wrote - it's biased toward its own work.

After implementing something significant, start a **new Claude instance** (or `/clear`) and ask it to review the code. Fresh context = honest review.

**When to Clear Context**

Monitor your context usage (shown in Claude Code). When it's getting high, find a good stopping point, save your progress to the docs (update TODO.md, note any decisions in SPEC.md), then start fresh. This beats losing context mid-task.

**Check your context budget:** Type `/context` to see exactly how much of your context window is being used by:
- Startup/default loaded content (CLAUDE.md, skills, MCP tools)
- Your conversation history
- Files you've read

If startup content is eating too much, consider disabling unused MCPs or trimming your CLAUDE.md."

---

### Part 8: Parallel Work Streams

"Run multiple Claude sessions simultaneously - work on different features in parallel without context switching.

**Git Worktrees** (the main approach)

**What's a git worktree?**

A worktree is a second (or third, or fourth) checkout of your repo in a different directory. Unlike cloning, all worktrees share the same `.git` history - commits in one are immediately visible in others.

You can have `main` checked out in one directory and `feature-branch` in another, both pointing to the same repo.

**Quick setup:**

```bash
git worktree add ../project-feature-a -b feature-a origin/main
git worktree add ../project-feature-b -b feature-b origin/main
```

**The workflow:**
1. Main terminal stays on the real repo (for quick checks)
2. Each feature gets its own worktree + terminal + Claude session
3. While Claude works on feature-a, you can review feature-b
4. No context switching, no stashing

**Agent mode for parallel work:**
```bash
cd ../project-feature-a
claude --dangerously-skip-permissions  # Agent/YOLO mode
```

Each session follows: research + plan → implement → review → iterate

Use SPEC.md/TODO.md to persist context across sessions.

**Model tip for heavy planning:**

If you're doing a lot of planning before parallel execution, try `/model opusplan`:
- Planning phase uses Opus (best reasoning)
- Execution uses Sonnet (faster)

This pairs well with the Plan → Execute workflow.

---

**Worktree environment setup**

Some projects have environment variables or paths that assume you're in the main repo. When working in a worktree, you may need to set these:

```bash
export PYTHONPATH="$(pwd):$PYTHONPATH"
export PROJECT_ROOT="$(pwd)"
```

**Tip:** Add worktree instructions to your project's CLAUDE.md so Claude knows how to handle them:

```markdown
## Worktree Environment

When working in a git worktree (not the main repo), set these before running Python:

\`\`\`bash
export PYTHONPATH=\"$(pwd):$PYTHONPATH\"
export PROJECT_ROOT=\"$(pwd)\"
\`\`\`

To check if you're in a worktree:
\`\`\`bash
git rev-parse --is-inside-work-tree && git worktree list
\`\`\`
```

This way Claude will automatically apply the right environment when it detects it's in a worktree.

---

**Summary:**
- **Simple code changes, tests, refactoring** → Use worktrees
- **Need full environment isolation** → Use separate dev containers or VMs

Ready for Part 9: Voice Transcription?"

---

### Part 9: Voice Transcription for Planning

"When you're planning complex features or doing long research sessions, **speaking** your thoughts can be much more efficient than typing.

**The pattern:**
1. Explain your plan/thoughts verbally (5-10 min)
2. Transcribe to text
3. Paste into Claude as a prompt
4. Claude processes your complete context at once

**Why this works:**
- **Faster idea capture** - Speaking is faster than typing
- **More complete context** - You'll explain nuances you'd skip when typing
- **Better for complexity** - Easier to describe complex architectures verbally
- **Reduced back-and-forth** - Claude gets the full picture upfront

---

#### Recommended Tools

**MacWhisper (macOS)** - Local, private transcription
- Uses Whisper AI locally (no cloud)
- Fast and accurate
- [Download](https://goodsnooze.gumroad.com/l/macwhisper)
- Free tier available

**Whisper.cpp (Linux/macOS command line)**
- Open source, runs locally
- Great for scripting/automation
- [GitHub](https://github.com/ggerganov/whisper.cpp)

**Other options:**
- **Otter.ai** - Cloud-based, very accurate, free tier
- **Windows Speech Recognition** - Built into Windows
- **Google Docs Voice Typing** - Free, browser-based

---

#### Example Workflow

**1. Record your planning session:**

[Speaking for 5 minutes]

"Okay so I need to build this rate limiting system. It needs to track requests per IP address,
use Redis for storage because we're already using that for sessions. The API endpoints that need
rate limiting are all under /api/v2/, and I want to exclude /health and /metrics from rate limiting.
The limit should be 100 requests per minute per IP, and when they exceed it we should return 429
with a Retry-After header. Oh and we need tests for this - unit tests for the rate limiter logic
and integration tests that actually hit the endpoints..."

**2. Transcribe with MacWhisper (or your tool)**

**3. Paste into Claude in Plan mode:**

```
I need you to plan this feature. Here's my thinking:

[paste transcription]

Please:
1. Identify all the components needed
2. Suggest an implementation order
3. Call out any edge cases or concerns
4. Estimate complexity
```

**4. Claude creates a structured plan from your brain dump**

---

#### Best Practices

**Good use cases:**
- Initial feature planning (architecture decisions)
- Complex debugging explanations (what you've tried)
- Research synthesis (explaining multiple approaches)
- Context dumps (when resuming after a break)

**Less useful for:**
- Short, simple requests (faster to type)
- Iterative back-and-forth (typing is fine)
- Code snippets (voice transcription mangles code)

**Pro tip:** Use Plan mode with voice transcription. Record your thoughts, transcribe, then paste into Claude in Plan mode. You get a detailed plan without Claude making any changes while you're still figuring things out.

Ready for the wrap-up?"

---

### Part 10: Wrap Up

"You now know how to extend Claude Code!

**Quick reference:**

| Component | Location | Activates |
|-----------|----------|-----------|
| Commands | `.claude/commands/` | Explicitly (`/name`) |
| Skills | `.claude/skills/` | Context-based (mention by name to be sure) |
| Agents | `.claude/agents/` | Like commands, isolated context |
| Hooks | `.claude/settings.json` | On events (must enable) |
| Rules | `.claude/rules/` | On file patterns |
| MCP | `.mcp.json` | Always connected (don't overload) |
| Voice transcription | External tool | Manual - for complex planning |

[If they built their plugin during tutorial:]

**Your Plugin is Ready!**

You've created `[plugin-name]` with:
- [List components they added]

To share it with others:
1. Push to GitHub
2. Others can install with:
   ```
   /plugin marketplace add your-username/your-plugin-name
   /plugin install plugin-name@your-username-your-plugin-name
   ```

**To create a plugin:**
```bash
mkdir -p my-plugin/.claude-plugin
# Create plugin.json with name, description, version, author
# Add commands/, skills/, agents/, rules/ as needed
```

**Want to go deeper?** Jump to specific sections:
- `/tutorial advanced commands`
- `/tutorial advanced skills`
- `/tutorial advanced hooks`
- `/tutorial advanced context`

Or explore this plugin's files - they're all documented examples!

---

**One last thing: Uninstall this tutorial when you're done**

This tutorial plugin adds commands, skills, and examples that eat into your context budget. Once you've learned the concepts, uninstall it to free up that context:

```
/plugin uninstall claude-code-tutorial
```

You can always reinstall it later if you need a refresher. The patterns you learned are what matter - not keeping the tutorial around."

---

## Specific Arguments

If user provides an argument:

- `commands` → Deep dive on commands only
- `skills` → Deep dive on skills only
- `agents` → Deep dive on agents only
- `hooks` → Deep dive on hooks only
- `rules` → Deep dive on rules only
- `mcp` → Deep dive on MCP only
- `context` → Context engineering patterns

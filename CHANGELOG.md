# Changelog

All notable changes to the Claude Code Tutorial plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-01-26

### Added
- **Create-plugin skill** - New skill at `skills/create-plugin/` that auto-activates when you ask Claude to create a plugin. Includes the creation script at `skills/create-plugin/scripts/create-plugin.py`

### Removed
- **uvx CLI** - Removed `src/claude_code_tutorial/` package and `pyproject.toml`
- **Top-level scripts/** - Moved `scripts/create-plugin.py` into the skill directory

### Changed
- **README** - Updated plugin creation instructions to use the skill instead of uvx
- **Structure** - Simplified to pure Claude Code plugin (no Python package)

## [1.1.0] - 2025-01-26

### Added
- **Tutorial restart option** - When all sections are complete, offers to start fresh, jump to advanced, or review specific sections
- **Workflow automation option** - New option 5 in the tutorial menu to automate repetitive workflows (PR reviews, CI fixes, data pulls)
- **Opusplan mode tip** - Added `/model opusplan` documentation for hybrid planning (Opus for planning, Sonnet for execution)
- **AI coding learning curve section** - New closing section about developing skills with AI-assisted coding
- **Plugin reload instructions** - Clear steps in advanced tutorial for loading newly created plugins
- **Skills merge note** - Explanation that commands are now part of the Skills system
- **Agent model configuration** - Documentation for `CLAUDE_SUBAGENT_MODEL` environment variable

### Changed
- **Model documentation** - Clarified that "default" is a dynamic alias that varies by account type (API users get Sonnet, Max users may get Opus until usage threshold)
- **README updates** - Added Claude Code installation step, fixed command format to `plugin-name:command`, updated documentation links to code.claude.com

### Removed
- `scripts/install-tutorial.sh` - Redundant with `install.sh`

## [1.0.0] - 2025-01-20

### Added
- Initial release
- Basic tutorial (`/tutorial`) - Learn Claude Code fundamentals
- Advanced tutorial (`/tutorial-advanced`) - Learn to extend Claude Code
- Cheat sheets for quick reference
- Plugin creation helper script (`scripts/create-plugin.py`)
- One-line installer (`install.sh`)

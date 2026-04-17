#!/usr/bin/env python3
"""
Create a Claude Code plugin skeleton.

Usage:
    python create-plugin.py my-plugin "My plugin description"
    python create-plugin.py  # Interactive mode
"""

import argparse
import json
import os
import sys
from pathlib import Path


def get_input(prompt: str, default: str = "") -> str:
    """Get input with optional default value."""
    if default:
        result = input(f"{prompt} [{default}]: ").strip()
        return result if result else default
    return input(f"{prompt}: ").strip()


def create_plugin(
    name: str,
    description: str,
    author: str,
    output_dir: Path,
    include_examples: bool = False,
) -> Path:
    """Create a plugin directory structure."""
    plugin_dir = output_dir / name

    if plugin_dir.exists():
        print(f"Error: Directory '{plugin_dir}' already exists")
        sys.exit(1)

    # Create directory structure
    dirs = [
        plugin_dir / ".claude-plugin",
        plugin_dir / "commands",
        plugin_dir / "skills",
        plugin_dir / "agents",
        plugin_dir / "rules",
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # Create plugin.json
    plugin_json = {
        "name": name,
        "description": description,
        "version": "1.0.0",
        "author": {"name": author},
    }

    with open(plugin_dir / ".claude-plugin" / "plugin.json", "w") as f:
        json.dump(plugin_json, f, indent=2)
        f.write("\n")

    # Create README.md
    readme_content = f"""# {name}

{description}

## Installation

```bash
# Start Claude Code
claude

# Add marketplace and install
/plugin marketplace add {author}/{name}
/plugin install {name}@{author}-{name}
```

## Commands

| Command | Description |
|---------|-------------|
| `/example` | Example command |

## Development

Test locally:
```bash
claude --plugin-dir ./{name}
```
"""
    with open(plugin_dir / "README.md", "w") as f:
        f.write(readme_content)

    if include_examples:
        # Create example command
        example_command = """---
description: Example command - replace with your own
argument-hint: [args]
---

# Example Command

This is an example command. Replace this with your own instructions.

When the user runs `/example`, Claude will follow these instructions.

## What to do

1. Greet the user
2. Ask what they need help with
3. Provide assistance

## Arguments

The user's input is available as: $ARGUMENTS
"""
        with open(plugin_dir / "commands" / "example.md", "w") as f:
            f.write(example_command)

        # Create example skill
        example_skill_dir = plugin_dir / "skills" / "example-skill"
        example_skill_dir.mkdir(parents=True, exist_ok=True)

        example_skill = """---
name: example-skill
description: Example skill - activates when user mentions "example" or "demo"
---

# Example Skill

This skill provides domain knowledge about examples and demos.

## When to activate

- User asks about examples
- User wants a demonstration
- User mentions "example" or "demo"

## Guidelines

1. Provide clear, concise examples
2. Explain step by step
3. Offer to elaborate if needed
"""
        with open(example_skill_dir / "SKILL.md", "w") as f:
            f.write(example_skill)

        # Create .mcp.json template
        mcp_config = {
            "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/main/.mcp.schema.json",
            "mcpServers": {},
        }
        with open(plugin_dir / ".mcp.json", "w") as f:
            json.dump(mcp_config, f, indent=2)
            f.write("\n")

    return plugin_dir


def main():
    parser = argparse.ArgumentParser(
        description="Create a Claude Code plugin skeleton",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s my-plugin "My awesome plugin"
    %(prog)s my-plugin "My plugin" --author myusername --examples
    %(prog)s  # Interactive mode
        """,
    )
    parser.add_argument("name", nargs="?", help="Plugin name (lowercase, hyphens)")
    parser.add_argument("description", nargs="?", help="Plugin description")
    parser.add_argument("--author", "-a", help="GitHub username")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path.cwd(),
        help="Output directory (default: current directory)",
    )
    parser.add_argument(
        "--examples",
        "-e",
        action="store_true",
        help="Include example command, skill, and MCP config",
    )

    args = parser.parse_args()

    # Interactive mode if no name provided
    if not args.name:
        print("Create a Claude Code Plugin")
        print("=" * 30)
        print()
        args.name = get_input("Plugin name (lowercase, hyphens)")
        args.description = get_input("Description")
        args.author = get_input("GitHub username")
        include_examples = get_input("Include examples? (y/n)", "y").lower() == "y"
    else:
        args.description = args.description or f"{args.name} plugin"
        args.author = args.author or "your-username"
        include_examples = args.examples

    # Validate name
    if not args.name:
        print("Error: Plugin name is required")
        sys.exit(1)

    # Create the plugin
    plugin_dir = create_plugin(
        name=args.name,
        description=args.description,
        author=args.author,
        output_dir=args.output,
        include_examples=include_examples,
    )

    print()
    print(f"Created plugin at: {plugin_dir}")
    print()
    print("Next steps:")
    print(f"  1. cd {plugin_dir}")
    print(f"  2. Edit commands/, skills/, etc.")
    print(f"  3. Test: claude --plugin-dir .")
    print(f"  4. Push to GitHub: gh repo create {args.author}/{args.name} --public --source=. --push")
    print()


if __name__ == "__main__":
    main()

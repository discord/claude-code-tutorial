#!/bin/bash
#
# Claude Code Tutorial - One-line installer
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/discord/claude-code-tutorial/main/install.sh | bash
#

set -e

REPO="discord/claude-code-tutorial"
PLUGIN="claude-code-tutorial@discord-claude-code-tutorial"

echo ""
echo "Claude Code Tutorial - Installing..."
echo ""

# Check if claude is installed
if ! command -v claude &> /dev/null; then
    echo "❌ Claude Code not found"
    echo ""
    echo "Install it first:"
    echo "  https://code.claude.com/docs/en/setup"
    echo ""
    exit 1
fi

# Add marketplace
echo "Adding marketplace..."
claude plugin marketplace add "$REPO" 2>/dev/null || true

# Install plugin
echo "Installing plugin..."
claude plugin install "$PLUGIN" 2>/dev/null || true

echo ""
echo "✅ Tutorial installed!"
echo ""
echo "Now run:"
echo "  claude"
echo "  /claude-code-tutorial:tutorial"
echo ""

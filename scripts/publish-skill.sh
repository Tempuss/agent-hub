#!/bin/bash

# Claude Toolkit Skills - Publish Single Package
# Usage: ./scripts/publish-skill.sh <package-name> [--dry-run] [--tag TAG]

set -e

SKILLS_ROOT="/Users/jiyongbin/dev/claude-toolkit/skills"

if [ $# -eq 0 ]; then
  echo "Usage: $0 <package-name> [--dry-run] [--tag TAG]"
  echo ""
  echo "Available packages:"
  echo "  - ai-persona-creator"
  echo "  - thinking-framework"
  echo "  - web-research"
  echo "  - doc-organizer"
  echo "  - template-generator"
  echo "  - market-strategy"
  echo "  - roi-analyzer"
  echo "  - strategic-thinking"
  echo "  - toss-patterns"
  exit 1
fi

PACKAGE=$1
shift

# Map package names to paths
PKG_PATH="$PACKAGE"

PKG_DIR="$SKILLS_ROOT/$PKG_PATH"

if [ ! -d "$PKG_DIR" ]; then
  echo "❌ Package directory not found: $PKG_DIR"
  exit 1
fi

if [ ! -f "$PKG_DIR/prpm.json" ]; then
  echo "❌ No prpm.json found in: $PKG_DIR"
  exit 1
fi

echo "📦 Publishing: $PACKAGE"
echo "   Path: $PKG_DIR"
echo ""

cd "$PKG_DIR" && prpm publish "$@"

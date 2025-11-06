#!/bin/bash

# Claude Toolkit Skills - Publish All Packages
# Usage: ./scripts/publish-all-skills.sh [--dry-run] [--tag TAG]

set -e

SKILLS_ROOT="/Users/jiyongbin/dev/claude-toolkit/skills"

# Package directories
PACKAGES=(
  "ai-persona-creator"
  "thinking-framework"
  "web-research"
  "doc-organizer"
  "template-generator"
  "market-strategy"
  "roi-analyzer"
  "toss-patterns"
)

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📦 Claude Toolkit Skills Publisher${NC}"
echo -e "${BLUE}=================================${NC}\n"

# Count packages
TOTAL=${#PACKAGES[@]}
SUCCESS=0
FAILED=0

# Publish each package
for pkg in "${PACKAGES[@]}"; do
  PKG_DIR="$SKILLS_ROOT/$pkg"

  if [ ! -d "$PKG_DIR" ]; then
    echo -e "${RED}❌ Directory not found: $pkg${NC}"
    ((FAILED++))
    continue
  fi

  if [ ! -f "$PKG_DIR/prpm.json" ]; then
    echo -e "${RED}❌ No prpm.json found: $pkg${NC}"
    ((FAILED++))
    continue
  fi

  echo -e "${BLUE}📦 Publishing: $pkg${NC}"

  if cd "$PKG_DIR" && prpm publish "$@"; then
    echo -e "${GREEN}✅ Success: $pkg${NC}\n"
    ((SUCCESS++))
  else
    echo -e "${RED}❌ Failed: $pkg${NC}\n"
    ((FAILED++))
  fi
done

# Summary
echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}📊 Summary${NC}"
echo -e "${GREEN}✅ Successful: $SUCCESS/$TOTAL${NC}"
if [ $FAILED -gt 0 ]; then
  echo -e "${RED}❌ Failed: $FAILED/$TOTAL${NC}"
fi

# Exit with error if any failed
if [ $FAILED -gt 0 ]; then
  exit 1
fi

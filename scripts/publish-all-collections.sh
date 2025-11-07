#!/bin/bash

# Claude Toolkit Collections - Publish All Collections
# Usage: ./scripts/publish-all-collections.sh [--dry-run] [--tag TAG]

set -e

COLLECTIONS_ROOT="/Users/jiyongbin/dev/claude-toolkit/collections"

# Collection directories
COLLECTIONS=(
  "thinking-research-framework"
)

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📦 Claude Toolkit Collections Publisher${NC}"
echo -e "${BLUE}======================================${NC}\n"

# Count collections
TOTAL=${#COLLECTIONS[@]}
SUCCESS=0
FAILED=0

# Publish each collection
for collection in "${COLLECTIONS[@]}"; do
  COLLECTION_DIR="$COLLECTIONS_ROOT/$collection"

  if [ ! -d "$COLLECTION_DIR" ]; then
    echo -e "${RED}❌ Directory not found: $collection${NC}"
    ((FAILED++))
    continue
  fi

  if [ ! -f "$COLLECTION_DIR/prpm.json" ]; then
    echo -e "${RED}❌ No prpm.json found: $collection${NC}"
    ((FAILED++))
    continue
  fi

  echo -e "${BLUE}📦 Publishing: $collection${NC}"

  if cd "$COLLECTION_DIR" && prpm publish "$@"; then
    echo -e "${GREEN}✅ Success: $collection${NC}\n"
    ((SUCCESS++))
  else
    echo -e "${RED}❌ Failed: $collection${NC}\n"
    ((FAILED++))
  fi
done

# Summary
echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}📊 Summary${NC}"
echo -e "${GREEN}✅ Successful: $SUCCESS/$TOTAL${NC}"
if [ $FAILED -gt 0 ]; then
  echo -e "${RED}❌ Failed: $FAILED/$TOTAL${NC}"
fi

# Exit with error if any failed
if [ $FAILED -gt 0 ]; then
  exit 1
fi

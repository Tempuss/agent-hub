#!/bin/bash

# Claude Toolkit Collections - Publish Single Collection
# Usage: ./scripts/publish-collection.sh <collection-name> [--dry-run] [--tag TAG]

set -e

COLLECTIONS_ROOT="/Users/jiyongbin/dev/claude-toolkit/collections"

if [ $# -eq 0 ]; then
  echo "Usage: $0 <collection-name> [--dry-run] [--tag TAG]"
  echo ""
  echo "Available collections:"
  echo "  - thinking-research-framework"
  exit 1
fi

COLLECTION=$1
shift

# Map collection names to paths
COLLECTION_PATH="$COLLECTION"

COLLECTION_DIR="$COLLECTIONS_ROOT/$COLLECTION_PATH"

if [ ! -d "$COLLECTION_DIR" ]; then
  echo "❌ Collection directory not found: $COLLECTION_DIR"
  exit 1
fi

if [ ! -f "$COLLECTION_DIR/prpm.json" ]; then
  echo "❌ No prpm.json found in: $COLLECTION_DIR"
  exit 1
fi

echo "📦 Publishing collection: $COLLECTION"
echo "   Path: $COLLECTION_DIR"
echo ""

cd "$COLLECTION_DIR" && prpm publish "$@"

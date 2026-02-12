#!/bin/bash
# Memory Manager Agent — ADD/UPDATE/DELETE/NOOP decisions
# Based on Memory-R1 paper: 28% improvement with active memory management
# Usage: ./scripts/memory-manager.sh [source-file] [target-dir]
# Example: ./scripts/memory-manager.sh memory/2026-02-10.md memory/semantic/

set -euo pipefail

SOURCE="${1:-}"
TARGET_DIR="${2:-memory/semantic}"
WORKSPACE="$HOME/.openclaw/workspace"
LOG="$WORKSPACE/memory/memory-ops.jsonl"

if [ -z "$SOURCE" ]; then
  echo "Usage: memory-manager.sh <source-file> [target-dir]"
  echo "Example: memory-manager.sh memory/2026-02-10.md memory/semantic/"
  exit 1
fi

SOURCE_PATH="$WORKSPACE/$SOURCE"
TARGET_PATH="$WORKSPACE/$TARGET_DIR"

if [ ! -f "$SOURCE_PATH" ]; then
  echo "ERROR: Source file not found: $SOURCE_PATH"
  exit 1
fi

echo "=== Memory Manager ==="
echo "Source: $SOURCE"
echo "Target: $TARGET_DIR"
echo "Existing memories:"
ls "$TARGET_PATH"/*.md 2>/dev/null | while read f; do
  echo "  - $(basename "$f"): $(head -1 "$f")"
done
echo ""
echo "Source content ($(wc -l < "$SOURCE_PATH") lines)"
echo "---"
echo "Run the LLM memory manager? This will output ADD/UPDATE/DELETE/NOOP decisions."
echo "Operations will be logged to: $LOG"

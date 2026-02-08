#!/bin/bash
# memory-grep.sh — Local fallback when memory_search (OpenAI embeddings) is down
# Usage: ./scripts/memory-grep.sh "search terms" [max_results]

set -e
cd "$(dirname "$0")/.."

QUERY="${1:?Usage: memory-grep.sh 'search terms' [max_results]}"
MAX="${2:-15}"

PATTERN=$(echo "$QUERY" | tr ' ' '\n' | grep -v '^$' | head -5 | paste -sd '|' -)

echo "🔍 Local memory search: \"$QUERY\""
echo "───────────────────────────────────────"

# Build list of existing search targets
TARGETS=""
for F in MEMORY.md HEARTBEAT.md ACTIVE_TASK.md USER.md INDEX.md; do
  [ -f "$F" ] && TARGETS="$TARGETS $F"
done
for D in memory agents standards research content products; do
  [ -d "$D" ] && TARGETS="$TARGETS $D"
done

RESULTS=$(grep -rniE "$PATTERN" $TARGETS 2>/dev/null \
  | grep -v 'node_modules\|\.git\|\.png\|\.jpg' \
  | head -"$MAX" || true)

if [ -z "$RESULTS" ]; then
  echo "❌ No matches. Try broader terms."
else
  echo "$RESULTS" | while IFS= read -r line; do
    FILE=$(echo "$line" | cut -d: -f1)
    LINENUM=$(echo "$line" | cut -d: -f2)
    CONTENT=$(echo "$line" | cut -d: -f3- | cut -c1-120)
    printf "%-40s L%-4s %s\n" "$FILE" "$LINENUM" "$CONTENT"
  done
  COUNT=$(echo "$RESULTS" | wc -l | tr -d ' ')
  echo "───────────────────────────────────────"
  echo "📊 $COUNT matches found"
fi

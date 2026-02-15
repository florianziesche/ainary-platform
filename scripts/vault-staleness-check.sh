#!/bin/bash
# Weekly Vault Staleness Check
# Finds notes not verified in >30 days

VAULT="/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"
THRESHOLD=$(date -v-30d +%Y-%m-%d 2>/dev/null || date -d "30 days ago" +%Y-%m-%d 2>/dev/null)
echo "=== Vault Staleness Report ==="
echo "Threshold: $THRESHOLD"
echo ""

# Notes with last_verified older than 30 days
echo "## Stale Notes (>30 days):"
find "$VAULT" -name "*.md" -not -path "*/90_Archive/*" | while read f; do
  verified=$(grep -m1 "last_verified:" "$f" 2>/dev/null | sed 's/last_verified: *//' | tr -d ' ')
  if [ -z "$verified" ]; then
    echo "  NO_DATE: $(basename "$f")"
  elif [[ "$verified" < "$THRESHOLD" ]]; then
    echo "  STALE ($verified): $(basename "$f")"
  fi
done | head -20

echo ""
echo "## Stats:"
total=$(find "$VAULT" -name "*.md" -not -path "*/90_Archive/*" | wc -l | tr -d ' ')
with_date=$(find "$VAULT" -name "*.md" -not -path "*/90_Archive/*" -exec grep -l "last_verified:" {} \; | wc -l | tr -d ' ')
echo "Total active notes: $total"
echo "With last_verified: $with_date"
echo "Missing date: $((total - with_date))"

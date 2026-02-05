#!/bin/bash
# track-send.sh — Log an external send to EXECUTION-TRACKER.md
# Usage: ./scripts/track-send.sh <type> <recipient> [notes]
# Types: cnc, consulting, vc, content

set -e
cd "$(dirname "$0")/.."

TYPE="${1:-cnc}"
RECIPIENT="${2:-Unknown}"
NOTES="${3:-}"
TODAY=$(date +"%Y-%02m-%02d")
DAY_NAME=$(date +"%a")
DAY_NUM=$(date +"%d" | sed 's/^0//')

TRACKER="agents/EXECUTION-TRACKER.md"

if [ ! -f "$TRACKER" ]; then
    echo "❌ Tracker not found: $TRACKER"
    exit 1
fi

# Log the send
echo ""
echo "📤 Logging $TYPE send to $RECIPIENT..."
echo "   Date: $TODAY ($DAY_NAME)"
echo "   Notes: ${NOTES:-none}"

# Append to daily log
DAILY_LOG="memory/$(date +%Y-%m-%d).md"
if [ -f "$DAILY_LOG" ]; then
    echo "" >> "$DAILY_LOG"
    echo "## External Send ($DAY_NAME $(date +%H:%M))" >> "$DAILY_LOG"
    echo "- **Type:** $TYPE" >> "$DAILY_LOG"
    echo "- **To:** $RECIPIENT" >> "$DAILY_LOG"
    [ -n "$NOTES" ] && echo "- **Notes:** $NOTES" >> "$DAILY_LOG"
fi

echo "✅ Logged to $DAILY_LOG"
echo ""
echo "⚠️  Remember to manually update $TRACKER with status!"

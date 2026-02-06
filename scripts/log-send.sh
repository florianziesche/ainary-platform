#!/bin/bash
# Log External Send - Updates today's memory file
# Usage: ./scripts/log-send.sh "Email to CNC Lead: Maschinentechnik Pretzschendorf"

set -e

if [ -z "$1" ]; then
    echo "❌ Error: No send description provided"
    echo ""
    echo "Usage: ./scripts/log-send.sh \"Description of what was sent\""
    echo ""
    echo "Examples:"
    echo "  ./scripts/log-send.sh \"Email: CNC Lead Follow-up\""
    echo "  ./scripts/log-send.sh \"Application: HOF Capital Associate\""
    echo "  ./scripts/log-send.sh \"LinkedIn: Monique connection message\""
    exit 1
fi

SEND_DESC="$1"
TODAY=$(date +%Y-%m-%d)
TIMESTAMP=$(date +"%H:%M")
MEMORY_FILE="memory/$TODAY.md"

# Create memory file if doesn't exist
if [ ! -f "$MEMORY_FILE" ]; then
    cat > "$MEMORY_FILE" << EOF
# Daily Log: $TODAY

## External Sends

## Built

## Revenue
- €0

---
EOF
fi

# Add send to External Sends section
# Find the line number of "## External Sends"
LINE_NUM=$(grep -n "## External Sends" "$MEMORY_FILE" | cut -d: -f1)

if [ -z "$LINE_NUM" ]; then
    echo "⚠️  Warning: No 'External Sends' section found"
    echo "Adding section..."
    echo "" >> "$MEMORY_FILE"
    echo "## External Sends" >> "$MEMORY_FILE"
    echo "- [x] [$TIMESTAMP] Send: $SEND_DESC" >> "$MEMORY_FILE"
else
    # Insert after the section header
    INSERT_LINE=$((LINE_NUM + 1))
    
    # Create temp file with the new line inserted
    {
        head -n "$LINE_NUM" "$MEMORY_FILE"
        echo "- [x] [$TIMESTAMP] Send: $SEND_DESC"
        tail -n +"$INSERT_LINE" "$MEMORY_FILE"
    } > "$MEMORY_FILE.tmp"
    
    mv "$MEMORY_FILE.tmp" "$MEMORY_FILE"
fi

echo "✅ Send logged!"
echo ""
echo "📝 Entry added to $MEMORY_FILE:"
echo "   - [x] [$TIMESTAMP] Send: $SEND_DESC"
echo ""

# Show updated stats
SEND_COUNT=$(grep -c "^- \[x\].*Send:" "$MEMORY_FILE" 2>/dev/null || echo "0")
echo "📊 Today's total sends: $SEND_COUNT"
echo ""

exit 0

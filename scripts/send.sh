#!/bin/bash
# send.sh — Unified send tracker (replaces track-send.sh + log-send.sh)
# Logs to BOTH daily memory AND execution tracker in one command.
# Usage: ./scripts/send.sh <type> <recipient> [notes]
# Types: cnc, consulting, vc, content, admin, email
#
# Examples:
#   ./scripts/send.sh cnc "Maschinentechnik Pretzschendorf" "Erstansprache per Email"
#   ./scripts/send.sh vc "HOF Capital" "Associate application submitted"
#   ./scripts/send.sh content "LinkedIn" "AI Governance post published"
#   ./scripts/send.sh email "Andreas MBS" "Demo results + 3 PDFs"

set -e
cd "$(dirname "$0")/.."

# --- Args ---
TYPE="${1:-}"
RECIPIENT="${2:-}"
NOTES="${3:-}"
TODAY=$(date +%Y-%m-%d)
TIMESTAMP=$(date +"%H:%M")
DAY_NAME=$(date +"%a")

if [ -z "$TYPE" ] || [ -z "$RECIPIENT" ]; then
    echo "❌ Usage: ./scripts/send.sh <type> <recipient> [notes]"
    echo ""
    echo "Types: cnc, consulting, vc, content, admin, email"
    echo ""
    echo "Examples:"
    echo "  ./scripts/send.sh cnc 'Firma XYZ' 'Erstansprache'"
    echo "  ./scripts/send.sh vc 'HOF Capital' 'Application submitted'"
    echo "  ./scripts/send.sh content 'LinkedIn' 'AI post published'"
    exit 1
fi

# --- Colors ---
GREEN='\033[0;32m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# --- 1. Log to daily memory ---
DAILY="memory/$TODAY.md"

if [ ! -f "$DAILY" ]; then
    cat > "$DAILY" << EOF
# $TODAY — Daily Log

## External Sends

## Built

## Notes
EOF
fi

# Check if "External Sends" section exists
if ! grep -q "## External Sends" "$DAILY" 2>/dev/null; then
    echo "" >> "$DAILY"
    echo "## External Sends" >> "$DAILY"
fi

# Insert after "## External Sends" header
LINE_NUM=$(grep -n "## External Sends" "$DAILY" | head -1 | cut -d: -f1)
INSERT_LINE=$((LINE_NUM + 1))

ENTRY="- [x] [$TIMESTAMP] **$TYPE** → $RECIPIENT"
[ -n "$NOTES" ] && ENTRY="$ENTRY — $NOTES"

{
    head -n "$LINE_NUM" "$DAILY"
    echo "$ENTRY"
    tail -n +"$INSERT_LINE" "$DAILY"
} > "$DAILY.tmp"
mv "$DAILY.tmp" "$DAILY"

# --- 2. Update EXECUTION-TRACKER.md ---
TRACKER="agents/EXECUTION-TRACKER.md"
if [ -f "$TRACKER" ]; then
    # Get today's day number for matching
    DAY_NUM=$(date +"%d" | sed 's/^0//')
    DAY_SHORT=$(date +"%a")
    
    # Map English day names to German
    case "$DAY_SHORT" in
        Mon) DE_DAY="Mo" ;;
        Tue) DE_DAY="Di" ;;
        Wed) DE_DAY="Mi" ;;
        Thu) DE_DAY="Do" ;;
        Fri) DE_DAY="Fr" ;;
        Sat) DE_DAY="Sa" ;;
        Sun) DE_DAY="So" ;;
        *) DE_DAY="$DAY_SHORT" ;;
    esac

    # Map type to tracker section
    case "$TYPE" in
        cnc)
            SECTION="CNC Outreach"
            ;;
        consulting)
            SECTION="AI Consulting"
            ;;
        vc)
            SECTION="VC Applications"
            ;;
        content)
            SECTION="Content Published"
            ;;
        *)
            SECTION=""
            ;;
    esac

    if [ -n "$SECTION" ]; then
        # Try to update the row for today
        # Look for pattern: | DE_DAY DAY_NUM. | and update it
        PATTERN="| ${DE_DAY} ${DAY_NUM}."
        if grep -q "$PATTERN" "$TRACKER" 2>/dev/null; then
            # Row exists — update the count and recipient
            # This is best-effort; complex table updates are better done by the AI
            echo -e "  ${CYAN}ℹ️  Tracker row found for $DE_DAY $DAY_NUM. — update manually or via Mia${NC}"
        else
            echo -e "  ${CYAN}ℹ️  No tracker row for today — Mia will update at next heartbeat${NC}"
        fi
    fi
fi

# --- 3. Summary ---
SEND_COUNT=$(grep -c "^\- \[x\].*Send:\|^\- \[x\].*→" "$DAILY" 2>/dev/null || echo "0")

echo ""
echo -e "${GREEN}✅ Send logged!${NC}"
echo ""
echo -e "  ${BOLD}Type:${NC}      $TYPE"
echo -e "  ${BOLD}To:${NC}        $RECIPIENT"
[ -n "$NOTES" ] && echo -e "  ${BOLD}Notes:${NC}     $NOTES"
echo -e "  ${BOLD}Time:${NC}      $TIMESTAMP"
echo -e "  ${BOLD}File:${NC}      $DAILY"
echo ""
echo -e "📊 Today's total sends: ${BOLD}$SEND_COUNT${NC}"
echo ""

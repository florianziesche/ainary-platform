#!/bin/bash
# morning-send-queue.sh — Surface ALL ready-to-send items in one view
# Run every morning or at heartbeat to eliminate "what should I send?" friction
# Usage: ./scripts/morning-send-queue.sh [--compact]

set -e
cd "$(dirname "$0")/.."

COMPACT="${1:---full}"
TODAY=$(date +%Y-%m-%d)
DAILY="memory/$TODAY.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}📬 MORNING SEND QUEUE — $TODAY${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

TOTAL_ITEMS=0

# --- 1. VC Applications ---
VC_FILE="job-applications/READY-TO-APPLY.md"
if [ -f "$VC_FILE" ]; then
    VC_COUNT=$(grep -c "^## " "$VC_FILE" 2>/dev/null || echo "0")
    VC_COUNT=$(echo "$VC_COUNT" | tr -d '[:space:]')
    if [ "$VC_COUNT" -gt 0 ]; then
        echo -e "${BLUE}🎯 VC APPLICATIONS ($VC_COUNT ready)${NC}"
        grep "^## " "$VC_FILE" | head -5 | while read -r line; do
            echo -e "   → ${line#\#\# }"
        done
        TOTAL_ITEMS=$((TOTAL_ITEMS + VC_COUNT))
        echo ""
    fi
fi

# --- 2. CNC Outreach ---
CNC_FILE="products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
if [ -f "$CNC_FILE" ]; then
    CNC_COUNT=$(grep -c "^## \|^### " "$CNC_FILE" 2>/dev/null || echo "0")
    CNC_COUNT=$(echo "$CNC_COUNT" | tr -d '[:space:]')
    if [ "$CNC_COUNT" -gt 0 ]; then
        echo -e "${GREEN}🏭 CNC OUTREACH ($CNC_COUNT ready)${NC}"
        grep "^## \|^### " "$CNC_FILE" | head -5 | while read -r line; do
            name="${line#\#\#\# }"
            name="${name#\#\# }"
            echo -e "   → $name"
        done
        TOTAL_ITEMS=$((TOTAL_ITEMS + CNC_COUNT))
        echo ""
    fi
fi

# --- 3. LinkedIn Posts ---
LINKEDIN_DIR="content/linkedin"
if [ -d "$LINKEDIN_DIR" ]; then
    LI_COUNT=$(find "$LINKEDIN_DIR" -name "*.md" -newer "$LINKEDIN_DIR" 2>/dev/null | wc -l | tr -d '[:space:]')
    LI_COUNT=${LI_COUNT:-0}
    if [ "$LI_COUNT" -gt 0 ]; then
        echo -e "${CYAN}📱 LINKEDIN POSTS ($LI_COUNT drafts)${NC}"
        find "$LINKEDIN_DIR" -name "*.md" -newer "$LINKEDIN_DIR" 2>/dev/null | head -3 | while read -r f; do
            echo -e "   → $(basename "$f" .md)"
        done
        TOTAL_ITEMS=$((TOTAL_ITEMS + LI_COUNT))
        echo ""
    fi
fi

# --- 4. Substack Articles ---
SUBSTACK_DIR="content/substack"
if [ -d "$SUBSTACK_DIR" ]; then
    SUB_COUNT=$(find "$SUBSTACK_DIR" -name "*.md" 2>/dev/null | wc -l | tr -d '[:space:]')
    SUB_COUNT=${SUB_COUNT:-0}
    if [ "$SUB_COUNT" -gt 0 ]; then
        echo -e "${YELLOW}✍️  SUBSTACK ARTICLES ($SUB_COUNT drafts)${NC}"
        find "$SUBSTACK_DIR" -name "*.md" 2>/dev/null | head -3 | while read -r f; do
            echo -e "   → $(basename "$f" .md)"
        done
        TOTAL_ITEMS=$((TOTAL_ITEMS + SUB_COUNT))
        echo ""
    fi
fi

# --- 5. Consulting/Outreach ---
CONSULT_FILE="consulting/READY-TO-SEND.md"
if [ -f "$CONSULT_FILE" ]; then
    CON_COUNT=$(grep -c "^## \|^### " "$CONSULT_FILE" 2>/dev/null || echo "0")
    CON_COUNT=$(echo "$CON_COUNT" | tr -d '[:space:]')
    if [ "$CON_COUNT" -gt 0 ]; then
        echo -e "${RED}💼 CONSULTING OUTREACH ($CON_COUNT ready)${NC}"
        grep "^## \|^### " "$CONSULT_FILE" | head -3 | while read -r line; do
            echo -e "   → ${line#\#\# }"
        done
        TOTAL_ITEMS=$((TOTAL_ITEMS + CON_COUNT))
        echo ""
    fi
fi

# --- 6. Follow-ups Due ---
# Check daily logs for items tagged "follow-up"
FOLLOWUP_COUNT=0
for i in $(seq 1 7); do
    CHECK_DATE=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "-${i} days" +%Y-%m-%d 2>/dev/null)
    CHECK_FILE="memory/$CHECK_DATE.md"
    if [ -f "$CHECK_FILE" ]; then
        FU=$(grep -ciE "follow.?up|nachfass|reminder" "$CHECK_FILE" 2>/dev/null || echo "0")
        FU=$(echo "$FU" | tr -d '[:space:]')
        FOLLOWUP_COUNT=$((FOLLOWUP_COUNT + FU))
    fi
done
if [ "$FOLLOWUP_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}🔔 FOLLOW-UPS due (~$FOLLOWUP_COUNT mentions in last 7 days)${NC}"
    echo ""
fi

# --- Today's Sends ---
TODAY_SENDS=0
if [ -f "$DAILY" ]; then
    TODAY_SENDS=$(grep -ciE "Send:|Sent:|Gesendet:|Outreach:|Applied:" "$DAILY" 2>/dev/null || true)
    TODAY_SENDS=$(echo "$TODAY_SENDS" | head -1 | tr -d '[:space:]')
    TODAY_SENDS=${TODAY_SENDS:-0}
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${BOLD}📊 SUMMARY${NC}"
echo -e "   Ready items:  $TOTAL_ITEMS"
echo -e "   Sent today:   $TODAY_SENDS"
echo ""

if [ "$TODAY_SENDS" -eq 0 ]; then
    echo -e "${RED}⚡ ZERO SENDS TODAY — Pick ONE item above and send it NOW${NC}"
    echo -e "   After sending: ${CYAN}./scripts/log-send.sh \"description\"${NC}"
elif [ "$TODAY_SENDS" -lt 3 ]; then
    echo -e "${YELLOW}📈 Good start! Can you send ${BOLD}one more${NC}${YELLOW}?${NC}"
else
    echo -e "${GREEN}🔥 On fire! $TODAY_SENDS sends today.${NC}"
fi
echo ""

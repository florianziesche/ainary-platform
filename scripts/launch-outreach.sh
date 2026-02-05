#!/bin/bash
# launch-outreach.sh — Proactively launch ready outreach items
# Created by Evolution Cycle #0019
# Usage: ./scripts/launch-outreach.sh [vc|cnc|all]

set -e
cd "$(dirname "$0")/.."

TYPE="${1:-all}"
TODAY=$(date +"%Y-%m-%d")
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📤 OUTREACH LAUNCHER — Send, Don't Just Prep${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check execution tracker stats
TRACKER="agents/EXECUTION-TRACKER.md"
if [ -f "$TRACKER" ]; then
    CNC_SENT=$(grep -c "✅" "$TRACKER" 2>/dev/null | head -1 || echo "0")
    echo -e "📊 This Week: ${YELLOW}Check EXECUTION-TRACKER.md for status${NC}"
    echo ""
fi

# VC Applications
if [ "$TYPE" = "all" ] || [ "$TYPE" = "vc" ]; then
    echo -e "${GREEN}═══ VC APPLICATIONS READY ═══${NC}"
    
    if [ -f "job-applications/READY-TO-APPLY.md" ]; then
        # Extract ready applications
        grep -E "^\d\." job-applications/READY-TO-APPLY.md 2>/dev/null | head -5 || echo "  (check file manually)"
        echo ""
        echo "  📂 Open ready applications:"
        echo -e "     ${YELLOW}open job-applications/READY-TO-APPLY.md${NC}"
        echo ""
    fi
    
    if [ -d "job-applications/materials" ]; then
        echo "  📄 Materials available:"
        ls job-applications/materials/*.pdf 2>/dev/null | while read f; do
            echo "     - $(basename "$f")"
        done
        echo ""
    fi
fi

# CNC Outreach
if [ "$TYPE" = "all" ] || [ "$TYPE" = "cnc" ]; then
    echo -e "${GREEN}═══ CNC OUTREACH READY ═══${NC}"
    
    READY_EMAILS="products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
    if [ -f "$READY_EMAILS" ]; then
        EMAIL_COUNT=$(grep -c "^##\|^###" "$READY_EMAILS" 2>/dev/null || echo "0")
        echo "  📧 $EMAIL_COUNT emails ready to send"
        echo ""
        echo "  📂 Open ready emails:"
        echo -e "     ${YELLOW}open $READY_EMAILS${NC}"
        echo ""
    fi
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${RED}⚡ QUICK ACTIONS:${NC}"
echo ""
echo "  1) Send a VC application now:"
echo "     open job-applications/READY-TO-APPLY.md && ./scripts/track-send.sh vc \"[Fund Name]\""
echo ""
echo "  2) Send a CNC outreach now:"
echo "     open products/cnc-planner/leads/READY-TO-SEND-EMAILS.md && ./scripts/track-send.sh cnc \"[Company]\""
echo ""
echo "  3) Log a send (after sending):"
echo "     ./scripts/track-send.sh <vc|cnc|consulting> \"[Recipient]\" \"[Notes]\""
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Interactive mode
read -p "Open ready items? [v=vc, c=cnc, n=no]: " -n 1 CHOICE
echo ""

case $CHOICE in
    v|V)
        echo "Opening VC applications..."
        open job-applications/READY-TO-APPLY.md 2>/dev/null || echo "File not found"
        ;;
    c|C)
        echo "Opening CNC emails..."
        open products/cnc-planner/leads/READY-TO-SEND-EMAILS.md 2>/dev/null || echo "File not found"
        ;;
    *)
        echo "No action. Remember: Prep without send = 0 value."
        ;;
esac

echo ""
echo -e "${GREEN}✅ Launcher complete. Now SEND something!${NC}"

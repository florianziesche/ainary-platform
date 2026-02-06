#!/bin/bash
# next-send.sh — Show the NEXT thing to send, with zero friction
# Just shows ONE item so there's no choice paralysis
# Usage: ./scripts/next-send.sh [cnc|vc|any]

set -e
cd "$(dirname "$0")/.."

TYPE="${1:-any}"
TODAY=$(date +%Y-%m-%d)
DAILY="memory/$TODAY.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Count today's sends
TODAY_SENDS=0
if [ -f "$DAILY" ]; then
    TODAY_SENDS=$(grep -c "^\- \[x\].*Send:\|^\- \[x\].*→\|Gesendet:\|GESENDET" "$DAILY" 2>/dev/null || true)
    TODAY_SENDS=$(echo "$TODAY_SENDS" | head -1 | tr -d '[:space:]')
    TODAY_SENDS=${TODAY_SENDS:-0}
fi

echo ""
echo -e "${BOLD}🎯 NEXT SEND${NC} (Today: $TODAY_SENDS sent so far)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

FOUND=0

# --- CNC Email ---
if [ "$TYPE" = "cnc" ] || [ "$TYPE" = "any" ]; then
    CNC_FILE="products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
    if [ -f "$CNC_FILE" ]; then
        # Get the first email block (between ## headers)
        FIRST_EMAIL=$(awk '/^## E-Mail/{if(found) exit; found=1} found' "$CNC_FILE" | head -30)
        if [ -n "$FIRST_EMAIL" ]; then
            # Extract key fields
            COMPANY=$(echo "$FIRST_EMAIL" | head -1 | sed 's/^## //')
            TO=$(echo "$FIRST_EMAIL" | grep "^\*\*An:\*\*" | sed 's/\*\*An:\*\* //')
            SUBJECT=$(echo "$FIRST_EMAIL" | grep "^\*\*Betreff:\*\*" | sed 's/\*\*Betreff:\*\* //')
            
            echo -e "${GREEN}📧 CNC OUTREACH${NC}"
            echo -e "  ${BOLD}Company:${NC} $COMPANY"
            echo -e "  ${BOLD}To:${NC}      $TO"
            echo -e "  ${BOLD}Subject:${NC} $SUBJECT"
            echo ""
            echo -e "  ${CYAN}→ Open file to copy email body:${NC}"
            echo -e "    open \"$CNC_FILE\""
            echo ""
            echo -e "  ${CYAN}→ After sending, log it:${NC}"
            echo -e "    ./scripts/send.sh cnc \"$(echo "$COMPANY" | sed 's/E-Mail [0-9]*: //')\" \"Erstansprache\""
            FOUND=1
        fi
    fi
fi

# --- VC Application ---
if ([ "$TYPE" = "vc" ] || [ "$TYPE" = "any" ]) && [ "$FOUND" -eq 0 ]; then
    VC_FILE="job-applications/READY-TO-APPLY.md"
    if [ -f "$VC_FILE" ]; then
        FIRST_APP=$(awk '/^## /{if(found) exit; found=1} found' "$VC_FILE" | head -15)
        if [ -n "$FIRST_APP" ]; then
            FUND=$(echo "$FIRST_APP" | head -1 | sed 's/^## //')
            echo -e "${YELLOW}💼 VC APPLICATION${NC}"
            echo -e "  ${BOLD}Fund:${NC} $FUND"
            echo ""
            echo -e "  ${CYAN}→ Open application:${NC}"
            echo -e "    open \"$VC_FILE\""
            echo ""
            echo -e "  ${CYAN}→ After submitting, log it:${NC}"
            echo -e "    ./scripts/send.sh vc \"$FUND\" \"Application submitted\""
            FOUND=1
        fi
    fi
fi

if [ "$FOUND" -eq 0 ]; then
    echo -e "${GREEN}✅ Nothing queued — or type '$TYPE' has no ready items.${NC}"
    echo -e "   Check: ./scripts/morning-send-queue.sh"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${BOLD}⏱️  Sending an email takes 2 minutes. Do it now.${NC}"
echo ""

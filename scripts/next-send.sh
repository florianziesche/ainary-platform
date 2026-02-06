#!/bin/bash
# next-send.sh — Show the NEXT thing to send, with zero friction
# Shows ONE item by priority: VC > CNC > Consulting > Content
# No choice paralysis. Just do the thing.
# Usage: ./scripts/next-send.sh [cnc|vc|consulting|content|any]

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
    TODAY_SENDS=$(grep -c "^\- \[x\].*Send:\|^\- \[x\].*→\|Gesendet:\|GESENDET" "$DAILY" 2>/dev/null | head -1 | tr -d '[:space:]' || echo "0")
    TODAY_SENDS=${TODAY_SENDS:-0}
fi

echo ""
echo -e "${BOLD}🎯 NEXT SEND${NC} (Today: $TODAY_SENDS sent so far)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

FOUND=0

# --- 1. VC Application (highest priority — career-defining) ---
if ([ "$TYPE" = "vc" ] || [ "$TYPE" = "any" ]) && [ "$FOUND" -eq 0 ]; then
    VC_FILE="job-applications/READY-TO-APPLY.md"
    if [ -f "$VC_FILE" ]; then
        FIRST_APP=$(awk '/^## /{if(found) exit; found=1} found' "$VC_FILE" | head -15)
        if [ -n "$FIRST_APP" ]; then
            FUND=$(echo "$FIRST_APP" | head -1 | sed 's/^## //')
            URL=$(echo "$FIRST_APP" | grep -i "url\|link\|portal\|apply" | head -1 | sed 's/.*http/http/' | sed 's/[)>].*//')
            echo -e "${YELLOW}💼 VC APPLICATION${NC} (Priority: 🔥 Career)"
            echo -e "  ${BOLD}Fund:${NC} $FUND"
            [ -n "$URL" ] && echo -e "  ${BOLD}Link:${NC} $URL"
            echo ""
            echo -e "  ${CYAN}→ Open application materials:${NC}"
            echo -e "    open \"$VC_FILE\""
            echo ""
            echo -e "  ${CYAN}→ After submitting:${NC}"
            echo -e "    ./scripts/send.sh vc \"$FUND\" \"Application submitted\""
            FOUND=1
        fi
    fi
fi

# --- 2. CNC Outreach (revenue-generating) ---
if ([ "$TYPE" = "cnc" ] || [ "$TYPE" = "any" ]) && [ "$FOUND" -eq 0 ]; then
    CNC_FILE="products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
    if [ -f "$CNC_FILE" ]; then
        FIRST_EMAIL=$(awk '/^## E-Mail/{if(found) exit; found=1} found' "$CNC_FILE" | head -30)
        if [ -n "$FIRST_EMAIL" ]; then
            COMPANY=$(echo "$FIRST_EMAIL" | head -1 | sed 's/^## //')
            TO=$(echo "$FIRST_EMAIL" | grep "^\*\*An:\*\*" | head -1 | sed 's/\*\*An:\*\* //')
            SUBJECT=$(echo "$FIRST_EMAIL" | grep "^\*\*Betreff:\*\*" | head -1 | sed 's/\*\*Betreff:\*\* //')
            CLEAN_COMPANY=$(echo "$COMPANY" | sed 's/E-Mail [0-9]*: //')
            
            echo -e "${GREEN}📧 CNC OUTREACH${NC} (Priority: 💰 Revenue)"
            echo -e "  ${BOLD}Company:${NC} $CLEAN_COMPANY"
            [ -n "$TO" ] && echo -e "  ${BOLD}To:${NC}      $TO"
            [ -n "$SUBJECT" ] && echo -e "  ${BOLD}Subject:${NC} $SUBJECT"
            echo ""
            echo -e "  ${CYAN}→ Open email to copy body:${NC}"
            echo -e "    open \"$CNC_FILE\""
            echo ""
            echo -e "  ${CYAN}→ After sending:${NC}"
            echo -e "    ./scripts/send.sh cnc \"$CLEAN_COMPANY\" \"Erstansprache\""
            FOUND=1
        fi
    fi
fi

# --- 3. Consulting Outreach ---
if ([ "$TYPE" = "consulting" ] || [ "$TYPE" = "any" ]) && [ "$FOUND" -eq 0 ]; then
    CONSULTING_FILE="consulting/READY-TO-SEND.md"
    if [ -f "$CONSULTING_FILE" ]; then
        FIRST_LEAD=$(awk '/^## /{if(found) exit; found=1} found' "$CONSULTING_FILE" | head -15)
        if [ -n "$FIRST_LEAD" ]; then
            LEAD=$(echo "$FIRST_LEAD" | head -1 | sed 's/^## //')
            echo -e "${YELLOW}🤝 CONSULTING OUTREACH${NC} (Priority: 💰 Revenue)"
            echo -e "  ${BOLD}Lead:${NC} $LEAD"
            echo ""
            echo -e "  ${CYAN}→ Open:${NC}"
            echo -e "    open \"$CONSULTING_FILE\""
            echo ""
            echo -e "  ${CYAN}→ After sending:${NC}"
            echo -e "    ./scripts/send.sh consulting \"$LEAD\" \"Outreach sent\""
            FOUND=1
        fi
    fi
fi

# --- 4. Content (LinkedIn/Substack) ---
if ([ "$TYPE" = "content" ] || [ "$TYPE" = "any" ]) && [ "$FOUND" -eq 0 ]; then
    # Check for ready LinkedIn posts
    if [ -d "content/linkedin" ]; then
        READY_POST=$(find content/linkedin -name "*.md" -newer "content/linkedin/.last-published" 2>/dev/null | head -1)
        # Fallback: just find any draft
        [ -z "$READY_POST" ] && READY_POST=$(find content/linkedin -name "*draft*" -o -name "*ready*" 2>/dev/null | head -1)
    fi
    
    # Check Substack
    if [ -z "$READY_POST" ] && [ -d "content/substack" ]; then
        READY_POST=$(find content/substack -name "*draft*" -o -name "*ready*" 2>/dev/null | head -1)
    fi
    
    if [ -n "$READY_POST" ]; then
        TITLE=$(basename "$READY_POST" .md)
        echo -e "${CYAN}📝 CONTENT PUBLISH${NC} (Priority: 📣 Audience)"
        echo -e "  ${BOLD}File:${NC} $READY_POST"
        echo -e "  ${BOLD}Title:${NC} $TITLE"
        echo ""
        echo -e "  ${CYAN}→ Open:${NC}"
        echo -e "    open \"$READY_POST\""
        echo ""
        echo -e "  ${CYAN}→ After publishing:${NC}"
        echo -e "    ./scripts/send.sh content \"LinkedIn\" \"$TITLE published\""
        FOUND=1
    fi
fi

# --- 5. Follow-ups (check recent memory for stale outreach) ---
if [ "$FOUND" -eq 0 ]; then
    # Check last 7 days of memory for sends without follow-up
    FOLLOWUP=""
    for i in $(seq 3 7); do
        PAST_DATE=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "$i days ago" +%Y-%m-%d 2>/dev/null || echo "")
        [ -z "$PAST_DATE" ] && continue
        PAST_FILE="memory/$PAST_DATE.md"
        if [ -f "$PAST_FILE" ]; then
            FOLLOWUP=$(grep -i "gesendet\|GESENDET\|→.*Email\|→.*email" "$PAST_FILE" 2>/dev/null | head -1)
            [ -n "$FOLLOWUP" ] && break
        fi
    done
    
    if [ -n "$FOLLOWUP" ]; then
        echo -e "${RED}🔄 FOLLOW-UP NEEDED${NC} (3-7 days since contact)"
        echo -e "  ${BOLD}Original:${NC} $FOLLOWUP"
        echo ""
        echo -e "  ${CYAN}→ Draft a follow-up and send it${NC}"
        echo -e "  ${CYAN}→ After sending: ./scripts/send.sh email \"Name\" \"Follow-up\"${NC}"
        FOUND=1
    fi
fi

if [ "$FOUND" -eq 0 ]; then
    echo -e "${GREEN}✅ Nothing queued — or type '$TYPE' has no ready items.${NC}"
    echo -e "   Full view: ${CYAN}./scripts/morning-send-queue.sh${NC}"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${BOLD}⏱️  Sending takes 2 minutes. Procrastinating costs €421/day.${NC}"
echo ""

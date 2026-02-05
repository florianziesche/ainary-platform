#!/bin/bash
# send-enforcer.sh — Break the "prepare but don't send" pattern
# Run daily or before work sessions
# Usage: ./scripts/send-enforcer.sh [--shame]

set -e
cd "$(dirname "$0")/.."

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "            🚨 SEND ENFORCER — EXECUTION CHECK 🚨              "
echo "═══════════════════════════════════════════════════════════════"
echo ""

# --- CONFIG ---
TRACKER="agents/EXECUTION-TRACKER.md"
CNC_READY="products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
VC_READY="job-applications/READY-TO-APPLY.md"
DAILY_LOG="memory/$(date +%Y-%m-%d).md"

# Opportunity cost calculation (based on MEMORY.md analysis)
DAILY_OPPORTUNITY_COST=421  # €/day without outreach

# --- READY ITEMS CHECK ---
echo "${BOLD}📋 READY TO SEND (collecting dust):${NC}"
echo ""

CNC_COUNT=0
VC_COUNT=0

# Count CNC ready emails
if [ -f "$CNC_READY" ]; then
    CNC_COUNT=$(grep -c "^##\|^### " "$CNC_READY" 2>/dev/null || echo "0")
    if [ "$CNC_COUNT" -gt 0 ]; then
        echo -e "  ${YELLOW}📧 CNC Outreach:${NC} $CNC_COUNT emails ready"
        MODIFIED=$(stat -f "%Sm" -t "%Y-%m-%d" "$CNC_READY" 2>/dev/null || date +%Y-%m-%d)
        DAYS_OLD=$(( ($(date +%s) - $(date -j -f "%Y-%m-%d" "$MODIFIED" +%s 2>/dev/null || date +%s)) / 86400 ))
        [ "$DAYS_OLD" -gt 0 ] && echo -e "     ${RED}⏰ Prepared ${DAYS_OLD} days ago!${NC}"
    fi
fi

# Count VC ready applications
if [ -f "$VC_READY" ]; then
    VC_COUNT=$(grep -c "^##\|^### " "$VC_READY" 2>/dev/null || echo "0")
    if [ "$VC_COUNT" -gt 0 ]; then
        echo -e "  ${YELLOW}💼 VC Applications:${NC} $VC_COUNT ready to submit"
        MODIFIED=$(stat -f "%Sm" -t "%Y-%m-%d" "$VC_READY" 2>/dev/null || date +%Y-%m-%d)
        DAYS_OLD=$(( ($(date +%s) - $(date -j -f "%Y-%m-%d" "$MODIFIED" +%s 2>/dev/null || date +%s)) / 86400 ))
        [ "$DAYS_OLD" -gt 0 ] && echo -e "     ${RED}⏰ Prepared ${DAYS_OLD} days ago!${NC}"
    fi
fi

echo ""

# --- EXECUTION TRACKER CHECK ---
echo "${BOLD}📊 THIS WEEK'S EXECUTION:${NC}"
echo ""

if [ -f "$TRACKER" ]; then
    # Count 🔴 (not done) vs 🟢 (done)
    RED_COUNT=$(grep -c "🔴" "$TRACKER" 2>/dev/null || echo "0")
    GREEN_COUNT=$(grep -c "🟢" "$TRACKER" 2>/dev/null || echo "0")
    
    if [ "$RED_COUNT" -gt 0 ]; then
        echo -e "  ${RED}🔴 Missed targets: $RED_COUNT${NC}"
    fi
    if [ "$GREEN_COUNT" -gt 0 ]; then
        echo -e "  ${GREEN}🟢 Completed: $GREEN_COUNT${NC}"
    fi
    
    # Calculate shame ratio
    TOTAL=$((RED_COUNT + GREEN_COUNT))
    if [ "$TOTAL" -gt 0 ]; then
        COMPLETION=$(( (GREEN_COUNT * 100) / TOTAL ))
        echo ""
        echo -e "  📈 Completion rate: ${BOLD}${COMPLETION}%${NC}"
    fi
fi

echo ""

# --- OPPORTUNITY COST ---
echo "${BOLD}💸 OPPORTUNITY COST:${NC}"
echo ""

# Count days without sends (look at tracker)
ZERO_SEND_DAYS=$(grep -c "| 0 |" "$TRACKER" 2>/dev/null || echo "0")
TOTAL_COST=$((ZERO_SEND_DAYS * DAILY_OPPORTUNITY_COST))

if [ "$ZERO_SEND_DAYS" -gt 0 ]; then
    echo -e "  ${RED}Days without outreach: $ZERO_SEND_DAYS${NC}"
    echo -e "  ${RED}Estimated lost value: €${TOTAL_COST}${NC}"
    echo ""
    echo -e "  ${YELLOW}Based on: €421/day opportunity cost from MEMORY.md analysis${NC}"
fi

echo ""

# --- THE HARD QUESTION ---
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo -e "${BOLD}❓ THE QUESTION:${NC}"
echo ""
echo "   Everything is prepared. Why hasn't it been SENT?"
echo ""
echo "   a) Fear of rejection → Send anyway. Rejection is data."
echo "   b) Not perfect yet → 80% sent beats 100% in drafts."
echo "   c) No time → It takes 2 minutes to send an email."
echo "   d) Forgot → Run this script every morning."
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo ""

# --- QUICK ACTIONS ---
echo "${BOLD}🚀 QUICK ACTIONS:${NC}"
echo ""
echo "   1. Send ONE CNC email now:"
echo "      open $CNC_READY"
echo ""
echo "   2. Submit ONE VC application now:"
echo "      open $VC_READY"
echo ""
echo "   3. Track a send:"
echo "      ./scripts/track-send.sh cnc 'CompanyName' 'notes'"
echo ""
echo "   4. View full outreach status:"
echo "      ./scripts/outreach-status.sh"
echo ""

# --- SHAME MODE ---
if [ "$1" == "--shame" ]; then
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
    echo -e "${RED}${BOLD}                    🔥 SHAME MODE ACTIVATED 🔥${NC}"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    echo "   Days preparing: Many"
    echo "   Days sending: Zero"
    echo "   Revenue generated: €0"
    echo ""
    echo "   The €500K goal doesn't care about your feelings."
    echo "   It only counts what you SEND."
    echo ""
    echo "   PREPARED ≠ DONE"
    echo "   SENT = DONE"
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
fi

echo ""

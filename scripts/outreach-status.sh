#!/bin/bash
# outreach-status.sh — Quick outreach pipeline status
# Shows: ready-to-send items, sent today, weekly totals
# Usage: ./scripts/outreach-status.sh

set -euo pipefail

WORKSPACE="${HOME}/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)
TRACKING_FILE="${WORKSPACE}/tracking/${TODAY}.md"

echo "📊 OUTREACH STATUS — ${TODAY}"
echo "================================"
echo ""

# Count ready-to-send items
echo "📬 READY TO SEND:"
CNC_READY="${WORKSPACE}/products/cnc-planner/leads/READY-TO-SEND-EMAILS.md"
VC_READY="${WORKSPACE}/job-applications/READY-TO-APPLY.md"

if [[ -f "$CNC_READY" ]]; then
    CNC_COUNT=$(grep -c "^##\|^###\|Subject:" "$CNC_READY" 2>/dev/null || echo "0")
    echo "  🔧 CNC Outreach: ~${CNC_COUNT} items in queue"
else
    echo "  🔧 CNC Outreach: No queue file found"
fi

if [[ -f "$VC_READY" ]]; then
    VC_COUNT=$(grep -c "^##\|^###" "$VC_READY" 2>/dev/null || echo "0")
    echo "  💼 VC Applications: ~${VC_COUNT} items in queue"
else
    echo "  💼 VC Applications: No queue file found"
fi

echo ""

# Count sends today
echo "📤 SENT TODAY:"
if [[ -f "$TRACKING_FILE" ]]; then
    SEND_COUNT=$(grep -c "^|.*|.*|" "$TRACKING_FILE" 2>/dev/null || echo "0")
    # Subtract header rows
    SEND_COUNT=$((SEND_COUNT > 2 ? SEND_COUNT - 2 : 0))
    echo "  Total sends: ${SEND_COUNT}"
else
    echo "  No tracking file for today."
fi

echo ""

# Weekly summary
echo "📅 THIS WEEK:"
WEEK_SENDS=0
for i in $(seq 0 6); do
    DAY=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "${i} days ago" +%Y-%m-%d 2>/dev/null || continue)
    DAY_FILE="${WORKSPACE}/tracking/${DAY}.md"
    if [[ -f "$DAY_FILE" ]]; then
        DAY_COUNT=$(grep -c "^|.*|.*|" "$DAY_FILE" 2>/dev/null || echo "0")
        DAY_COUNT=$((DAY_COUNT > 2 ? DAY_COUNT - 2 : 0))
        WEEK_SENDS=$((WEEK_SENDS + DAY_COUNT))
    fi
done
echo "  Week total: ${WEEK_SENDS} sends"
echo "  Target: 10/week (2/day)"
echo ""

# Opportunity cost reminder
if [[ $WEEK_SENDS -lt 5 ]]; then
    MISSED=$((10 - WEEK_SENDS))
    echo "⚠️  ${MISSED} sends behind target. Each day without outreach ≈ €421 opportunity cost."
fi

echo ""
echo "💡 Quick actions:"
echo "   - Send CNC emails: cat ${CNC_READY}"
echo "   - Send VC apps: cat ${VC_READY}"

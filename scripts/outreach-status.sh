#!/bin/bash
# outreach-status.sh — Quick outreach pipeline status
# Shows: ready-to-send items, sent today, weekly totals, days since last send
# Usage: ./scripts/outreach-status.sh
#
# Evolution Log:
#   v1 (2026-02-04): Initial version
#   v2 (2026-02-04): Fixed send counting (uses "External Sends" section),
#                     added "days since last send" tracker, improved reliability

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
    # Count actual email blocks (Subject: lines = individual emails)
    CNC_COUNT=$(grep -c "^Subject:" "$CNC_READY" 2>/dev/null) || CNC_COUNT=0
    if [[ "$CNC_COUNT" -eq 0 ]]; then
        # Fallback: count H2/H3 headers as leads
        CNC_COUNT=$(grep -c "^##" "$CNC_READY" 2>/dev/null) || CNC_COUNT=0
    fi
    echo "  🔧 CNC Outreach: ${CNC_COUNT} emails ready"
else
    echo "  🔧 CNC Outreach: No queue file"
fi

if [[ -f "$VC_READY" ]]; then
    VC_COUNT=$(grep -c "^## " "$VC_READY" 2>/dev/null) || VC_COUNT=0
    echo "  💼 VC Applications: ${VC_COUNT} applications ready"
else
    echo "  💼 VC Applications: No queue file"
fi

echo ""

# Count sends today — look at "External Sends Today" table in tracking file
count_sends_in_file() {
    local file="$1"
    if [[ ! -f "$file" ]]; then
        echo "0"
        return
    fi
    # Count non-empty rows in External Sends table (rows with actual content, not headers/separators)
    local in_sends=0
    local count=0
    while IFS= read -r line; do
        if [[ "$line" =~ "External Sends" ]]; then
            in_sends=1
            continue
        fi
        if [[ $in_sends -eq 1 ]]; then
            # Skip table headers and separator rows
            if [[ "$line" =~ ^"| Type" ]] || [[ "$line" =~ ^"|---" ]] || [[ "$line" =~ ^"| |" ]]; then
                continue
            fi
            # Count actual send entries (pipe-separated with content)
            if [[ "$line" =~ ^"|" ]] && [[ ! "$line" =~ "Send Count" ]]; then
                count=$((count + 1))
            fi
            # Also check for "Send Count: N" line
            if [[ "$line" =~ "Send Count:" ]]; then
                local explicit
                explicit=$(echo "$line" | grep -oE '[0-9]+' | head -1)
                if [[ -n "$explicit" ]] && [[ "$explicit" -gt "$count" ]]; then
                    count=$explicit
                fi
                break
            fi
            # Stop at next section
            if [[ "$line" =~ ^"##" ]] && [[ ! "$line" =~ "External" ]]; then
                break
            fi
        fi
    done < "$file"
    echo "$count"
}

echo "📤 SENT TODAY:"
TODAY_SENDS=$(count_sends_in_file "$TRACKING_FILE")
echo "  Total sends: ${TODAY_SENDS}"

echo ""

# Weekly summary + find last send date
echo "📅 THIS WEEK:"
WEEK_SENDS=0
LAST_SEND_DATE=""
for i in $(seq 0 13); do
    DAY=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "${i} days ago" +%Y-%m-%d 2>/dev/null || continue)
    DAY_FILE="${WORKSPACE}/tracking/${DAY}.md"
    DAY_COUNT=$(count_sends_in_file "$DAY_FILE")
    
    if [[ $i -le 6 ]]; then
        WEEK_SENDS=$((WEEK_SENDS + DAY_COUNT))
    fi
    
    if [[ -z "$LAST_SEND_DATE" ]] && [[ "$DAY_COUNT" -gt 0 ]]; then
        LAST_SEND_DATE="$DAY"
    fi
done
echo "  Week total: ${WEEK_SENDS} sends"
echo "  Target: 10/week (2/day)"

# Days since last send
if [[ -n "$LAST_SEND_DATE" ]]; then
    LAST_SEND_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST_SEND_DATE" "+%s" 2>/dev/null || date -d "$LAST_SEND_DATE" "+%s" 2>/dev/null || echo "0")
    TODAY_EPOCH=$(date "+%s")
    DAYS_AGO=$(( (TODAY_EPOCH - LAST_SEND_EPOCH) / 86400 ))
    if [[ $DAYS_AGO -eq 0 ]]; then
        echo "  Last send: Today ✅"
    elif [[ $DAYS_AGO -eq 1 ]]; then
        echo "  Last send: Yesterday"
    else
        echo "  ⚠️  Last send: ${DAYS_AGO} days ago ($LAST_SEND_DATE)"
    fi
else
    echo "  ⚠️  No sends found in last 2 weeks!"
fi

echo ""

# Opportunity cost reminder
if [[ $WEEK_SENDS -lt 5 ]]; then
    MISSED=$((10 - WEEK_SENDS))
    COST=$((MISSED * 421))
    echo "🔥 ${MISSED} sends behind target = ~€${COST} opportunity cost this week."
fi

echo ""
echo "💡 Quick actions:"
echo "   - CNC emails: cat $CNC_READY"
echo "   - VC apps:    cat $VC_READY"

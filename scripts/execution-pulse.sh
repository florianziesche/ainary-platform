#!/bin/bash
# execution-pulse.sh — Quick execution health check for heartbeats
# Returns JSON for easy parsing by Mia
# Usage: ./scripts/execution-pulse.sh [--json|--human]

set -e
cd "$(dirname "$0")/.."

MODE="${1:---human}"
TODAY=$(date +%Y-%m-%d)
DOW=$(date +%u)  # 1=Monday

# --- Data Collection ---
TRACKER="agents/EXECUTION-TRACKER.md"
DAILY="memory/$TODAY.md"

# Count zero-send days this week from tracker
ZERO_DAYS=0
TOTAL_SENDS=0
if [ -f "$TRACKER" ]; then
    ZERO_DAYS=$(grep -c "| 0 |" "$TRACKER" 2>/dev/null || echo "0")
    ZERO_DAYS=$(echo "$ZERO_DAYS" | tr -d '[:space:]')
    # Count actual outreach sends (🟢 in CNC/Consulting/VC rows only, not content)
    TOTAL_SENDS=$(grep -E "Outreach|Application|Gesendet" "$TRACKER" 2>/dev/null | grep -c "🟢" || true)
    TOTAL_SENDS=${TOTAL_SENDS:-0}
    TOTAL_SENDS=$(echo "$TOTAL_SENDS" | head -1 | tr -d '[:space:]')
fi

# Count items ready to send
CNC_READY=0
VC_READY=0
if [ -f "products/cnc-planner/leads/READY-TO-SEND-EMAILS.md" ]; then
    CNC_READY=$(grep -c "^##\|^### " "products/cnc-planner/leads/READY-TO-SEND-EMAILS.md" 2>/dev/null || echo "0")
    CNC_READY=$(echo "$CNC_READY" | tr -d '[:space:]')
fi
if [ -f "job-applications/READY-TO-APPLY.md" ]; then
    VC_READY=$(grep -c "^##\|^### " "job-applications/READY-TO-APPLY.md" 2>/dev/null || echo "0")
    VC_READY=$(echo "$VC_READY" | tr -d '[:space:]')
fi

# Days since last send (check daily logs backwards)
DAYS_SINCE_SEND=0
for i in $(seq 0 14); do
    CHECK_DATE=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "-${i} days" +%Y-%m-%d 2>/dev/null)
    CHECK_FILE="memory/$CHECK_DATE.md"
    if [ -f "$CHECK_FILE" ]; then
        if grep -qiE "Send:|Sent:|Gesendet:|Outreach:|Applied:|Application sent" "$CHECK_FILE" 2>/dev/null; then
            DAYS_SINCE_SEND=$i
            break
        fi
    fi
    DAYS_SINCE_SEND=$((i + 1))
done

# Opportunity cost
DAILY_COST=421
TOTAL_COST=$((ZERO_DAYS * DAILY_COST))

# Execution score (0-100)
# Sends heavily weighted, ready-but-unsent is penalty
SEND_SCORE=0
[ "$TOTAL_SENDS" -gt 0 ] && SEND_SCORE=$((TOTAL_SENDS * 20))
[ "$SEND_SCORE" -gt 60 ] && SEND_SCORE=60

READY_PENALTY=0
READY_TOTAL=$((CNC_READY + VC_READY))
[ "$READY_TOTAL" -gt 0 ] && [ "$TOTAL_SENDS" -eq 0 ] && READY_PENALTY=30

SCORE=$((SEND_SCORE + 40 - READY_PENALTY))
[ "$SCORE" -lt 0 ] && SCORE=0
[ "$SCORE" -gt 100 ] && SCORE=100

# Status emoji
STATUS="🟢"
[ "$SCORE" -lt 70 ] && STATUS="🟡"
[ "$SCORE" -lt 40 ] && STATUS="🔴"
[ "$SCORE" -lt 20 ] && STATUS="🚨"

if [ "$MODE" = "--json" ]; then
    cat << EOF
{
  "date": "$TODAY",
  "score": $SCORE,
  "status": "$STATUS",
  "sends": {
    "total": $TOTAL_SENDS,
    "zeroDays": $ZERO_DAYS,
    "daysSinceLast": $DAYS_SINCE_SEND
  },
  "ready": {
    "cnc": $CNC_READY,
    "vc": $VC_READY,
    "total": $READY_TOTAL
  },
  "cost": {
    "daily": $DAILY_COST,
    "total": $TOTAL_COST
  }
}
EOF
else
    echo ""
    echo "$STATUS Execution Pulse — $TODAY"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Score: $SCORE/100"
    echo "Sends this week: $TOTAL_SENDS"
    echo "Zero-send days: $ZERO_DAYS"
    echo "Days since last send: $DAYS_SINCE_SEND"
    echo "Ready to send: $READY_TOTAL ($CNC_READY CNC, $VC_READY VC)"
    echo "Opportunity cost: €$TOTAL_COST"
    echo ""
    
    if [ "$SCORE" -lt 40 ]; then
        echo "⚡ ACTION NEEDED: Send ONE item before building anything else"
    fi
fi

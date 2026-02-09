#!/bin/bash
# daily-send-summary.sh — One-line send status for heartbeats and cron
# Returns: "X ready | Y sent today | Z days streak without sends"
# Usage: ./scripts/daily-send-summary.sh [--json]

set -e
cd "$(dirname "$0")/.."

TODAY=$(date +%Y-%m-%d)
DAILY_LOG="memory/$TODAY.md"

# Count ready items across all pipelines
CNC_READY=0
VC_READY=0
CONTENT_READY=0

# CNC emails (both locations)
for f in products/cnc-planner/leads/READY-TO-SEND-EMAILS.md sales/outreach-emails-ready.md; do
    [ -f "$f" ] && CNC_READY=$((CNC_READY + $(grep -c "^## \|^### " "$f" 2>/dev/null || echo 0)))
done

# VC applications
if [ -f "job-applications/READY-TO-APPLY.md" ]; then
    VC_READY=$(grep -c "^## \|^### " "job-applications/READY-TO-APPLY.md" 2>/dev/null || true)
    VC_READY=${VC_READY:-0}
fi

# Content (drafted but unpublished articles)
VAULT_PUBLISH="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/20_Areas/Content/Publish"
[ -d "$VAULT_PUBLISH" ] && \
    CONTENT_READY=$(find "$VAULT_PUBLISH" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')

TOTAL_READY=$((CNC_READY + VC_READY + CONTENT_READY))

# Count today's sends
SENT_TODAY=0
if [ -f "$DAILY_LOG" ]; then
    SENT_TODAY=$(grep -c "Send:\|SENT\|✅.*sent\|📤" "$DAILY_LOG" 2>/dev/null || true)
    SENT_TODAY=${SENT_TODAY:-0}
fi

# Count consecutive zero-send days (look back up to 14 days)
ZERO_STREAK=0
for i in $(seq 1 14); do
    PAST_DATE=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "$i days ago" +%Y-%m-%d 2>/dev/null)
    PAST_LOG="memory/$PAST_DATE.md"
    if [ -f "$PAST_LOG" ]; then
        PAST_SENDS=$(grep -c "Send:\|SENT\|✅.*sent\|📤" "$PAST_LOG" 2>/dev/null || true)
        PAST_SENDS=${PAST_SENDS:-0}
        if [ "$PAST_SENDS" -eq 0 ]; then
            ZERO_STREAK=$((ZERO_STREAK + 1))
        else
            break
        fi
    else
        ZERO_STREAK=$((ZERO_STREAK + 1))
    fi
done

# Output
if [ "$1" == "--json" ]; then
    cat <<EOF
{"ready":$TOTAL_READY,"cnc":$CNC_READY,"vc":$VC_READY,"content":$CONTENT_READY,"sentToday":$SENT_TODAY,"zeroStreak":$ZERO_STREAK,"date":"$TODAY"}
EOF
else
    echo "📊 SEND STATUS ($TODAY)"
    echo "   Ready: $TOTAL_READY ($CNC_READY CNC | $VC_READY VC | $CONTENT_READY content)"
    echo "   Sent today: $SENT_TODAY"
    if [ "$ZERO_STREAK" -gt 0 ]; then
        COST=$((ZERO_STREAK * 421))
        echo "   ⚠️  Zero-send streak: ${ZERO_STREAK} days (est. €${COST} lost)"
    else
        echo "   ✅ Active sender!"
    fi
fi

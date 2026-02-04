#!/bin/bash
# daily-tracking-init.sh — Auto-generate daily tracking file
# Usage: ./scripts/daily-tracking-init.sh [YYYY-MM-DD]
# If no date given, uses today.

set -euo pipefail

WORKSPACE="${HOME}/.openclaw/workspace"
DATE="${1:-$(date +%Y-%m-%d)}"
DAY_NAME=$(date -j -f "%Y-%m-%d" "$DATE" "+%A" 2>/dev/null || date -d "$DATE" "+%A" 2>/dev/null || echo "")
TRACKING_DIR="${WORKSPACE}/tracking"
TRACKING_FILE="${TRACKING_DIR}/${DATE}.md"

mkdir -p "$TRACKING_DIR"

if [[ -f "$TRACKING_FILE" ]]; then
    echo "⚠️  ${TRACKING_FILE} already exists. Skipping."
    exit 0
fi

# Check for calendar events (if gog is available)
CALENDAR_EVENTS=""
if command -v gog &>/dev/null; then
    CALENDAR_EVENTS=$(gog cal list --from "$DATE" --to "$DATE" --format text 2>/dev/null || echo "")
fi

# Check for items in ACTIVE_TASK.md
ACTIVE_TASK=""
if [[ -f "${WORKSPACE}/ACTIVE_TASK.md" ]]; then
    ACTIVE_TASK=$(head -20 "${WORKSPACE}/ACTIVE_TASK.md" 2>/dev/null || echo "")
fi

cat > "$TRACKING_FILE" << 'TEMPLATE'
# Daily Tracking: DATE_PLACEHOLDER (DAY_PLACEHOLDER)

## 🎯 Today's ONE Thing
<!-- Highest-leverage task for today -->
- [ ] 

## 📋 Tasks

<!-- Format:
### [HH:MM-HH:MM] Task Name (XX min)
- **Typ:** Build | Research | Content | Sales | System | Admin
- **Geschätzt:** XX min
- **Tatsächlich:** XX min  
- **Status:** ✅ Done | 🔄 In Progress | ❌ Failed | ⏸ Blocked
- **Probleme:** 
- **Besser:** 
- **Output:** 
-->

## 📅 Calendar
CALENDAR_PLACEHOLDER

## 🔥 Active Task
ACTIVE_PLACEHOLDER

## 📊 Tages-Summary

| Metrik | Wert |
|--------|------|
| Total Tasks | |
| Total Zeit | |
| Geschätzt vs Real | |
| Längste Aufgabe | |
| Größter Zeitfresser | |
| #1 Verbesserung | |

## External Sends Today
| Type | Recipient | Status |
|------|-----------|--------|
| | | |

**Send Count: 0** ← Track this. Goal: ≥2/day.
TEMPLATE

# Replace placeholders
sed -i '' "s/DATE_PLACEHOLDER/${DATE}/g" "$TRACKING_FILE" 2>/dev/null || sed -i "s/DATE_PLACEHOLDER/${DATE}/g" "$TRACKING_FILE"
sed -i '' "s/DAY_PLACEHOLDER/${DAY_NAME}/g" "$TRACKING_FILE" 2>/dev/null || sed -i "s/DAY_PLACEHOLDER/${DAY_NAME}/g" "$TRACKING_FILE"

if [[ -n "$CALENDAR_EVENTS" ]]; then
    # Use perl for multi-line replacement (portable)
    perl -i -pe "s/CALENDAR_PLACEHOLDER/${CALENDAR_EVENTS}/g" "$TRACKING_FILE" 2>/dev/null || true
else
    sed -i '' "s/CALENDAR_PLACEHOLDER/No calendar events loaded./g" "$TRACKING_FILE" 2>/dev/null || sed -i "s/CALENDAR_PLACEHOLDER/No calendar events loaded./g" "$TRACKING_FILE"
fi

if [[ -n "$ACTIVE_TASK" ]]; then
    sed -i '' "s/ACTIVE_PLACEHOLDER/See ACTIVE_TASK.md/g" "$TRACKING_FILE" 2>/dev/null || sed -i "s/ACTIVE_PLACEHOLDER/See ACTIVE_TASK.md/g" "$TRACKING_FILE"
else
    sed -i '' "s/ACTIVE_PLACEHOLDER/No active task./g" "$TRACKING_FILE" 2>/dev/null || sed -i "s/ACTIVE_PLACEHOLDER/No active task./g" "$TRACKING_FILE"
fi

echo "✅ Created ${TRACKING_FILE}"

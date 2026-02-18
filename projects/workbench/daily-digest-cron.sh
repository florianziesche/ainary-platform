#!/bin/bash
#
# Daily Agent Digest Cron Script
# Schedule: daily at 21:00 CET
#
# To install this cron job, run:
#   crontab -e
# Then add this line:
#   0 21 * * * /Users/florianziesche/.openclaw/workspace/projects/workbench/daily-digest-cron.sh
#
# Or use launchctl (macOS preferred):
#   See daily-digest-launchd.plist

API="http://localhost:8080/api/activity/digest"
OPENCLAW_BIN="/usr/local/bin/openclaw"

# Fetch digest data
DIGEST_JSON=$(curl -s "$API")

if [ $? -ne 0 ] || [ -z "$DIGEST_JSON" ]; then
    echo "Failed to fetch activity digest from $API"
    exit 1
fi

# Parse digest and create summary
SUMMARY=$(echo "$DIGEST_JSON" | python3 -c "
import sys, json

data = json.load(sys.stdin)
date = data['date']
agents_today = data['agents_today']
inactive = data['inactive']
alerts = data['alerts']
impact = data['impact']

# Build summary
lines = []
lines.append(f'📊 Daily Agent Digest for {date}')
lines.append('')

if agents_today:
    lines.append(f'✓ {len(agents_today)} agents active:')
    for agent in agents_today:
        actions = agent['actions']
        successes = agent['successes']
        failures = agent['failures']
        total_impact = agent['total_impact']
        impact_types = agent['impact_types'] or ''
        
        line = f\"  • {agent['agent']}: {actions} actions ({successes} success, {failures} failed)\"
        if total_impact > 0:
            line += f\" → impact: {total_impact} ({impact_types})\"
        lines.append(line)
    lines.append('')

if inactive:
    lines.append(f'⚠ {len(inactive)} agents inactive: {', '.join(inactive)}')
    lines.append('')

if impact:
    lines.append('📈 7-day impact totals:')
    for imp in impact:
        impact_type = imp['impact_type']
        total = imp['total']
        if impact_type == 'revenue':
            lines.append(f'  • Revenue: €{total}')
        elif impact_type == 'time_saved':
            lines.append(f'  • Time saved: {total} minutes')
        elif impact_type == 'knowledge':
            lines.append(f'  • Knowledge: {total} findings')
        else:
            lines.append(f'  • {impact_type}: {total}')
    lines.append('')

if alerts:
    lines.append(f'🚨 {len(alerts)} alerts:')
    for alert in alerts:
        lines.append(f\"  • {alert['message']}\")

print('\\n'.join(lines))
")

echo "$SUMMARY"

# Send to main agent session via openclaw message tool
# Note: This requires openclaw CLI to be configured with message permissions
# Uncomment the following line once openclaw message is available:
# echo "$SUMMARY" | $OPENCLAW_BIN message send --channel agent:main:main "Daily Agent Digest"

# For now, just log to a file
LOG_DIR="/Users/florianziesche/.openclaw/workspace/logs"
mkdir -p "$LOG_DIR"
echo "$SUMMARY" >> "$LOG_DIR/daily-digest.log"
echo "--- $(date) ---" >> "$LOG_DIR/daily-digest.log"

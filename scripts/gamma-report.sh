#!/bin/bash
# gamma-report.sh - Generate weekly Γ (Collaboration Gain) report
# Usage: ./scripts/gamma-report.sh [days_back]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_FILE="$WORKSPACE_DIR/memory/gamma-log.json"
DAYS_BACK="${1:-7}"

# Check if log exists
if [[ ! -f "$LOG_FILE" ]]; then
    echo "❌ No gamma log found at $LOG_FILE"
    echo "Run gamma-tracker.sh first to start tracking."
    exit 1
fi

# Check if jq is available
if ! command -v jq &> /dev/null; then
    echo "⚠️  jq not found. Install with: brew install jq"
    echo "Attempting basic parsing..."
fi

# Calculate date threshold
DATE_THRESHOLD=$(date -u -v-${DAYS_BACK}d +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date -u -d "$DAYS_BACK days ago" +"%Y-%m-%dT%H:%M:%SZ")

echo "# Γ (Collaboration Gain) Report"
echo "**Period:** Last $DAYS_BACK days (since $DATE_THRESHOLD)"
echo "**Generated:** $(date)"
echo ""

if command -v jq &> /dev/null; then
    # Use jq for analysis
    TOTAL_RUNS=$(jq -r '.runs | length' "$LOG_FILE")
    
    if [[ $TOTAL_RUNS -eq 0 ]]; then
        echo "📭 No runs tracked yet."
        exit 0
    fi
    
    # Filter runs within time period
    RECENT_RUNS=$(jq -r --arg threshold "$DATE_THRESHOLD" '
        .runs | map(select(.date >= $threshold))
    ' "$LOG_FILE")
    
    RECENT_COUNT=$(echo "$RECENT_RUNS" | jq 'length')
    
    if [[ $RECENT_COUNT -eq 0 ]]; then
        echo "📭 No runs in the last $DAYS_BACK days."
        echo ""
        echo "**Total runs (all time):** $TOTAL_RUNS"
        exit 0
    fi
    
    # Calculate metrics
    AVG_GAMMA=$(echo "$RECENT_RUNS" | jq -r '
        map(.gamma_estimate | tonumber) | add / length
    ' | awk '{printf "%.4f", $1}')
    
    TOTAL_TOKENS=$(echo "$RECENT_RUNS" | jq -r '
        map(.total_tokens) | add
    ')
    
    TOTAL_RUNTIME=$(echo "$RECENT_RUNS" | jq -r '
        map(.runtime_sec) | add
    ')
    
    AVG_AGENTS=$(echo "$RECENT_RUNS" | jq -r '
        map(.agents_used) | add / length
    ' | awk '{printf "%.1f", $1}')
    
    # Tasks with low Γ (< 1.0 normalized threshold)
    # For our metric, "bad" means significantly below average
    LOW_GAMMA=$(echo "$RECENT_RUNS" | jq -r --arg avg "$AVG_GAMMA" '
        map(select((.gamma_estimate | tonumber) < (($avg | tonumber) * 0.5)))
    ')
    
    LOW_GAMMA_COUNT=$(echo "$LOW_GAMMA" | jq 'length')
    
    echo "## 📊 Summary"
    echo ""
    echo "| Metric | Value |"
    echo "|--------|-------|"
    echo "| **Total Runs** | $RECENT_COUNT |"
    echo "| **Avg Γ** | $AVG_GAMMA |"
    echo "| **Avg Agents/Task** | $AVG_AGENTS |"
    echo "| **Total Tokens** | $(printf "%'d" $TOTAL_TOKENS) |"
    echo "| **Total Runtime** | ${TOTAL_RUNTIME}s ($(awk "BEGIN {printf \"%.1f\", $TOTAL_RUNTIME/60}")m) |"
    echo "| **Low Γ Tasks** | $LOW_GAMMA_COUNT ($(awk "BEGIN {printf \"%.0f\", ($LOW_GAMMA_COUNT/$RECENT_COUNT)*100}")%) |"
    echo ""
    
    # Show low-performing tasks
    if [[ $LOW_GAMMA_COUNT -gt 0 ]]; then
        echo "## ⚠️ Low Γ Tasks (< 50% of avg)"
        echo ""
        echo "| Task | Agents | Tokens | Γ | Efficiency Issue |"
        echo "|------|--------|--------|---|-----------------|"
        
        echo "$LOW_GAMMA" | jq -r '.[] | 
            "\(.task) | \(.agents_used) | \(.total_tokens) | \(.gamma_estimate) | " +
            if .agents_used > 2 then "Too many agents?"
            elif .total_tokens > 10000 then "Token-heavy"
            elif .output_bytes < 1000 then "Low output"
            else "Review needed"
            end
        ' | while IFS= read -r line; do
            echo "| $line |"
        done
        
        echo ""
        
        # Calculate potential waste
        WASTE_TOKENS=$(echo "$LOW_GAMMA" | jq -r '
            map(select(.agents_used > 1) | .total_tokens * 0.3) | add // 0
        ' | awk '{printf "%.0f", $1}')
        
        if [[ $WASTE_TOKENS -gt 0 ]]; then
            echo "**Estimated Token Waste:** $(printf "%'d" $WASTE_TOKENS) tokens (~30% overhead on multi-agent tasks)"
            echo ""
        fi
    fi
    
    # Top performing tasks
    echo "## ✅ Top Γ Tasks"
    echo ""
    echo "| Task | Agents | Tokens | Γ |"
    echo "|------|--------|--------|---|"
    
    echo "$RECENT_RUNS" | jq -r '
        sort_by(-.gamma_estimate | tonumber) | .[:5] | .[] |
        "\(.task) | \(.agents_used) | \(.total_tokens) | \(.gamma_estimate)"
    ' | while IFS= read -r line; do
        echo "| $line |"
    done
    
    echo ""
    
    # Recommendations
    echo "## 💡 Recommendations"
    echo ""
    
    SINGLE_AGENT_RATIO=$(echo "$RECENT_RUNS" | jq -r '
        map(select(.agents_used == 1)) | length
    ' | awk -v total="$RECENT_COUNT" '{printf "%.0f", ($1/total)*100}')
    
    if [[ $SINGLE_AGENT_RATIO -lt 30 ]]; then
        echo "- ⚠️ Only ${SINGLE_AGENT_RATIO}% single-agent tasks. Consider using single agent for simple tasks (<5k tokens)."
    fi
    
    if [[ $LOW_GAMMA_COUNT -gt $((RECENT_COUNT / 3)) ]]; then
        echo "- ⚠️ High proportion of low-Γ tasks. Review MULTI-AGENT-RULES.md for better delegation."
    fi
    
    AVG_TOKENS_PER_TASK=$((TOTAL_TOKENS / RECENT_COUNT))
    if [[ $AVG_TOKENS_PER_TASK -gt 8000 ]]; then
        echo "- 💰 High avg tokens/task ($AVG_TOKENS_PER_TASK). Consider breaking down complex tasks."
    fi
    
    echo ""
    echo "---"
    echo "*Γ = output_bytes / (total_tokens × agents_used) × 1000 — Higher is better*"
    
else
    # Fallback: basic stats without jq
    echo "⚠️ Install jq for full analysis: brew install jq"
    echo ""
    TOTAL_RUNS=$(grep -c '"date"' "$LOG_FILE" || echo 0)
    echo "**Total runs tracked:** $TOTAL_RUNS"
    echo ""
    echo "Run with jq installed for detailed metrics."
fi

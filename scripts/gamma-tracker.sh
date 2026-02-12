#!/bin/bash
# gamma-tracker.sh - Track Γ (Collaboration Gain) for sub-agent runs
# Usage: ./scripts/gamma-tracker.sh <task_name> <agents_used> <total_tokens_in> <total_tokens_out> <runtime_sec> <output_path>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_FILE="$WORKSPACE_DIR/memory/gamma-log.json"

# Ensure memory directory exists
mkdir -p "$WORKSPACE_DIR/memory"

# Initialize log file if it doesn't exist
if [[ ! -f "$LOG_FILE" ]]; then
    echo '{"runs": []}' > "$LOG_FILE"
fi

# Parse arguments
TASK_NAME="${1:-unknown}"
AGENTS_USED="${2:-1}"
TOKENS_IN="${3:-0}"
TOKENS_OUT="${4:-0}"
RUNTIME_SEC="${5:-0}"
OUTPUT_PATH="${6:-}"

# Calculate metrics
TOTAL_TOKENS=$((TOKENS_IN + TOKENS_OUT))
OUTPUT_BYTES=0
if [[ -n "$OUTPUT_PATH" && -f "$OUTPUT_PATH" ]]; then
    OUTPUT_BYTES=$(wc -c < "$OUTPUT_PATH" 2>/dev/null || echo 0)
fi

# Estimate Γ (Collaboration Gain)
# Simple heuristic: 
# - Single agent baseline: assume same task would take 80% tokens but 100% time
# - Multi-agent overhead: communication cost ~20% tokens, but 50% faster
# Γ = (output_quality * speed) / token_efficiency
# For now: Γ_estimate = output_bytes / (total_tokens * agents_used)
# Higher output per token per agent = better collaboration

if [[ $TOTAL_TOKENS -gt 0 && $AGENTS_USED -gt 0 ]]; then
    # Normalize: bytes per 1000 tokens per agent
    GAMMA_ESTIMATE=$(awk "BEGIN {printf \"%.4f\", ($OUTPUT_BYTES / ($TOTAL_TOKENS * $AGENTS_USED)) * 1000}")
else
    GAMMA_ESTIMATE="0.0000"
fi

# Create entry
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
ENTRY=$(cat <<EOF
{
    "date": "$TIMESTAMP",
    "task": "$TASK_NAME",
    "agents_used": $AGENTS_USED,
    "tokens_in": $TOKENS_IN,
    "tokens_out": $TOKENS_OUT,
    "total_tokens": $TOTAL_TOKENS,
    "runtime_sec": $RUNTIME_SEC,
    "output_bytes": $OUTPUT_BYTES,
    "gamma_estimate": $GAMMA_ESTIMATE
}
EOF
)

# Append to log (using jq if available, otherwise manual)
if command -v jq &> /dev/null; then
    # Use jq for proper JSON manipulation
    TMP_FILE=$(mktemp)
    jq ".runs += [$ENTRY]" "$LOG_FILE" > "$TMP_FILE"
    mv "$TMP_FILE" "$LOG_FILE"
else
    # Fallback: manual JSON append (works if runs array exists)
    # Remove last closing brace, append entry, close
    sed -i.bak '$ d' "$LOG_FILE" 2>/dev/null || sed -i '' '$ d' "$LOG_FILE"
    if grep -q '"runs": \[\]' "$LOG_FILE"; then
        # Empty array, replace it
        sed -i.bak 's/"runs": \[\]/"runs": [/' "$LOG_FILE" 2>/dev/null || sed -i '' 's/"runs": \[\]/"runs": [/' "$LOG_FILE"
        echo "$ENTRY" >> "$LOG_FILE"
    else
        echo "," >> "$LOG_FILE"
        echo "$ENTRY" >> "$LOG_FILE"
    fi
    echo "]}" >> "$LOG_FILE"
    rm -f "${LOG_FILE}.bak"
fi

echo "✅ Tracked: $TASK_NAME | Agents: $AGENTS_USED | Tokens: $TOTAL_TOKENS | Γ: $GAMMA_ESTIMATE"
echo "📊 Log: $LOG_FILE"

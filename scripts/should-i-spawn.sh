#!/usr/bin/env bash
# should-i-spawn.sh - Quick decision helper for sub-agent spawning
# Usage: ./scripts/should-i-spawn.sh [task-description] [estimated-minutes] [estimated-output-tokens]

set -euo pipefail

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Thresholds
OVERHEAD_TOKENS=5000
MIN_OUTPUT_THRESHOLD=15000
GAMMA_THRESHOLD=1.2

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}    Should I Spawn a Sub-Agent? — Decision Helper${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

# Get input
if [ $# -eq 0 ]; then
    read -p "Task description: " TASK_DESC
    read -p "Estimated time (minutes): " TASK_MIN
    read -p "Estimated output (tokens): " OUTPUT_TOKENS
else
    TASK_DESC="${1:-Unknown task}"
    TASK_MIN="${2:-0}"
    OUTPUT_TOKENS="${3:-0}"
fi

echo
echo -e "📋 ${BLUE}Task:${NC} $TASK_DESC"
echo -e "⏱️  ${BLUE}Time:${NC} $TASK_MIN min"
echo -e "📊 ${BLUE}Output:${NC} $OUTPUT_TOKENS tokens"
echo

# Calculate score
SCORE=0
REASONS=()

# Check 1: Output threshold
if [ "$OUTPUT_TOKENS" -gt "$MIN_OUTPUT_THRESHOLD" ]; then
    SCORE=$((SCORE + 2))
    REASONS+=("✅ Output > 15k tokens (3× overhead)")
else
    REASONS+=("❌ Output < 15k tokens (below break-even)")
fi

# Check 2: Time estimate
if [ "$TASK_MIN" -gt 15 ]; then
    SCORE=$((SCORE + 2))
    REASONS+=("✅ Task > 15 min (complex)")
elif [ "$TASK_MIN" -gt 5 ]; then
    SCORE=$((SCORE + 1))
    REASONS+=("⚠️  Task 5-15 min (medium complexity)")
else
    REASONS+=("❌ Task < 5 min (simple)")
fi

# Check 3: Skill existence (interactive)
echo -e "${YELLOW}Does a skill exist for this task?${NC}"
echo "Checking skill library..."
SKILL_MATCHES=$(ls ~/.openclaw/workspace/skills/ 2>/dev/null | wc -l || echo "0")
echo "Found $SKILL_MATCHES custom skills. Checking for relevant ones..."
echo

read -p "Does a skill handle 80%+ of this task? (y/n): " HAS_SKILL
if [[ "$HAS_SKILL" =~ ^[Yy]$ ]]; then
    SCORE=$((SCORE - 3))
    REASONS+=("❌ Skill exists (use it instead)")
else
    SCORE=$((SCORE + 1))
    REASONS+=("✅ No existing skill")
fi
echo

# Check 4: Parallelization
read -p "Can you parallelize into 2+ independent subtasks? (y/n): " CAN_PARALLEL
if [[ "$CAN_PARALLEL" =~ ^[Yy]$ ]]; then
    SCORE=$((SCORE + 3))
    REASONS+=("✅ Can parallelize (major win)")
else
    REASONS+=("❌ Sequential only (no speed gain)")
fi
echo

# Check 5: Time sensitivity
read -p "Is immediate response needed? (y/n): " IS_URGENT
if [[ "$IS_URGENT" =~ ^[Yy]$ ]]; then
    SCORE=$((SCORE - 2))
    REASONS+=("❌ Time-sensitive (2-5s spawn latency)")
else
    SCORE=$((SCORE + 1))
    REASONS+=("✅ Not urgent")
fi
echo

# Check 6: Γ history (if log exists)
GAMMA_LOG="memory/gamma-log.jsonl"
if [ -f "$GAMMA_LOG" ]; then
    echo -e "${YELLOW}Checking Γ history...${NC}"
    # Simple keyword match in task description
    TASK_TYPE=$(echo "$TASK_DESC" | awk '{print tolower($1)}')
    AVG_GAMMA=$(cat "$GAMMA_LOG" | jq -r "select(.task_type | contains(\"$TASK_TYPE\")) | .gamma" 2>/dev/null | awk '{sum+=$1; count++} END {if(count>0) print sum/count; else print "none"}')
    
    if [ "$AVG_GAMMA" != "none" ] && [ $(echo "$AVG_GAMMA > 0" | bc -l) -eq 1 ]; then
        echo "Found Γ history for similar tasks: $AVG_GAMMA"
        if [ $(echo "$AVG_GAMMA > $GAMMA_THRESHOLD" | bc -l) -eq 1 ]; then
            SCORE=$((SCORE + 2))
            REASONS+=("✅ Historical Γ > $GAMMA_THRESHOLD (proven efficient)")
        else
            SCORE=$((SCORE - 2))
            REASONS+=("❌ Historical Γ < $GAMMA_THRESHOLD (proven inefficient)")
        fi
    else
        echo "No Γ history for this task type"
        REASONS+=("⚠️  No Γ history (first time)")
    fi
else
    REASONS+=("⚠️  No gamma-log.jsonl (can't check history)")
fi

echo
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}                    Analysis                      ${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

for reason in "${REASONS[@]}"; do
    echo "  $reason"
done

echo
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Decision
echo
if [ "$SCORE" -ge 5 ]; then
    echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  🟢 RECOMMENDATION: SPAWN SUB-AGENT   ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
    DECISION="MULTI-AGENT"
elif [ "$SCORE" -le -1 ]; then
    echo -e "${RED}╔════════════════════════════════════════╗${NC}"
    echo -e "${RED}║  🔴 RECOMMENDATION: SINGLE AGENT ONLY ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════╝${NC}"
    DECISION="SINGLE-AGENT"
else
    echo -e "${YELLOW}╔════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║  🟡 RECOMMENDATION: EVALUATE CAREFULLY║${NC}"
    echo -e "${YELLOW}╚════════════════════════════════════════╝${NC}"
    DECISION="EVALUATE"
fi

echo
echo -e "${BLUE}Score:${NC} $SCORE"
echo

if [ "$DECISION" == "MULTI-AGENT" ]; then
    echo -e "${GREEN}Suggested pattern:${NC}"
    if [[ "$CAN_PARALLEL" =~ ^[Yy]$ ]]; then
        echo "  → Multi-agent (parallel)"
        echo "  → Spawn 2-5 agents for independent subtasks"
    else
        echo "  → Consider hierarchical coordination"
        echo "  → Or single agent if truly sequential"
    fi
elif [ "$DECISION" == "SINGLE-AGENT" ]; then
    echo -e "${RED}Suggested approach:${NC}"
    echo "  → Use single agent with existing skill"
    echo "  → Or execute directly with tool calls"
    echo "  → Don't spawn sub-agent (wasteful)"
else
    echo -e "${YELLOW}Suggested approach:${NC}"
    echo "  → Check SKILL-AUDIT.md for relevant skills"
    echo "  → If no skill and output >15k → consider spawn"
    echo "  → If skill exists → use single agent + skill"
fi

echo
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Token Economics:${NC}"
echo "  Sub-agent overhead: ${OVERHEAD_TOKENS} tokens"
echo "  Expected output: ${OUTPUT_TOKENS} tokens"
if [ "$OUTPUT_TOKENS" -gt 0 ]; then
    EFFICIENCY=$(echo "scale=2; $OUTPUT_TOKENS / $OVERHEAD_TOKENS" | bc -l)
    echo "  Efficiency ratio: ${EFFICIENCY}× overhead"
    if [ $(echo "$EFFICIENCY < 3" | bc -l) -eq 1 ]; then
        echo -e "  ${RED}⚠️  Below 3× threshold!${NC}"
    else
        echo -e "  ${GREEN}✅ Above 3× threshold${NC}"
    fi
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

# Offer to log decision
read -p "Log this decision to gamma-log.jsonl? (y/n): " SHOULD_LOG
if [[ "$SHOULD_LOG" =~ ^[Yy]$ ]]; then
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    TASK_ID=$(echo "$TASK_DESC" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -c1-30)
    TASK_TYPE=$(echo "$TASK_DESC" | awk '{print tolower($1)}')
    
    LOG_ENTRY="{\"timestamp\":\"$TIMESTAMP\",\"task_id\":\"$TASK_ID\",\"task_type\":\"$TASK_TYPE\",\"decision\":\"$DECISION\",\"reasoning\":\"${REASONS[0]}\",\"estimated_tokens\":$OUTPUT_TOKENS,\"overhead_tokens\":$OVERHEAD_TOKENS,\"score\":$SCORE}"
    
    echo "$LOG_ENTRY" >> "$GAMMA_LOG"
    echo -e "${GREEN}✅ Logged to $GAMMA_LOG${NC}"
fi

echo
echo "📚 For detailed framework, see: standards/AGENT-DECISION-FRAMEWORK.md"
echo "📋 For skill inventory, see: SKILL-AUDIT.md"
echo

#!/bin/bash
# spawn-agent.sh — Post-completion hook reminder
# Usage: source after any sub-agent completes
# 
# This script doesn't spawn agents (OpenClaw does that via sessions_spawn).
# It exists as a POST-COMPLETION checklist that Main can run:
#
#   bash scripts/spawn-agent.sh check <output_file>
#
# Checks:
# 1. Was a knowledge-worker spawned for this output?
# 2. Was adversarial review spawned (if external content)?
# 3. Were findings integrated into verified-truths.md?

ACTION="${1:-help}"
OUTPUT_FILE="${2:-}"

case "$ACTION" in
  check)
    echo "=== POST-COMPLETION CHECKLIST ==="
    echo ""
    echo "Sub-agent output received. Before moving on:"
    echo ""
    echo "  [ ] 1. KNOWLEDGE WORKER: Spawn haiku agent to extract facts"
    echo "       → verified-truths.md + connections.md"
    echo ""
    echo "  [ ] 2. ADVERSARIAL REVIEW (if external content):"
    echo "       → Spawn sonnet agent to fact-check"
    echo ""  
    echo "  [ ] 3. CHAIN NEXT? Is this output input for another agent?"
    echo ""
    echo "  [ ] 4. UPDATE DAILY LOG: memory/daily/$(date +%Y-%m-%d).md"
    echo ""
    if [ -n "$OUTPUT_FILE" ]; then
      echo "Output file: $OUTPUT_FILE"
      echo "Lines: $(wc -l < "$OUTPUT_FILE" 2>/dev/null || echo 'N/A')"
    fi
    ;;
  *)
    echo "Usage: bash scripts/spawn-agent.sh check [output_file]"
    ;;
esac

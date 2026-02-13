#!/bin/bash
# Smart Loading Router — identifies which memory files to load for a given task
# Usage: ./scripts/smart-load.sh "task description"

TASK="$1"
MEMORY_DIR="$(dirname "$0")/../memory"

echo "🧠 Smart Load for: $TASK"
echo "═══════════════════════════════"
echo ""
echo "ALWAYS load:"
echo "  ✅ memory/MEMORY-INDEX.md"
echo "  ✅ memory/corrections.md"
echo ""

# Detect domains
LOAD_PEOPLE=false
LOAD_PROJECTS=false
LOAD_DECISIONS=false
LOAD_PATTERNS=false
LOAD_TECH=false
LOAD_QUALITY=false
LOAD_FAILED=false

# People keywords
if echo "$TASK" | grep -qiE "email|outreach|send|kontakt|andreas|nancy|daniel|hendrik|paul|monique|tomas|sven|person|meeting|call|interview|pitch"; then
  LOAD_PEOPLE=true
fi

# Project keywords
if echo "$TASK" | grep -qiE "website|platform|xray|x-ray|cnc|vault|substack|blog|content|deploy|vercel|github"; then
  LOAD_PROJECTS=true
fi

# Decision keywords
if echo "$TASK" | grep -qiE "entscheid|decision|warum|why|alternativ|option|strateg"; then
  LOAD_DECISIONS=true
fi

# Pattern keywords
if echo "$TASK" | grep -qiE "pattern|was funktioniert|anti-pattern|lesson|learn|fehler|mistake"; then
  LOAD_PATTERNS=true
fi

# Tech keywords
if echo "$TASK" | grep -qiE "deploy|code|script|path|pfad|command|git|vercel|latex|api|cli|gog|cron"; then
  LOAD_TECH=true
fi

# Quality keywords (always for output tasks)
if echo "$TASK" | grep -qiE "schreib|write|draft|email|post|artikel|report|pdf|build|erstell|create"; then
  LOAD_QUALITY=true
fi

# Failed outputs (for similar past tasks)
if echo "$TASK" | grep -qiE "website|mobile|design|email|report|content"; then
  LOAD_FAILED=true
fi

echo "CONDITIONAL load:"
$LOAD_PEOPLE && echo "  📋 memory/people.md (contacts relevant)"
$LOAD_PROJECTS && echo "  📋 memory/projects.md (project context)"
$LOAD_DECISIONS && echo "  📋 memory/decisions.md (past decisions)"
$LOAD_PATTERNS && echo "  📋 memory/patterns.md (what works)"
$LOAD_TECH && echo "  📋 memory/tech.md (paths & commands)"
$LOAD_QUALITY && echo "  📋 memory/quality-standards.md (output standards)"
$LOAD_FAILED && echo "  📋 memory/failed-outputs.md (past mistakes)"

echo ""
echo "SEMANTIC search recommended:"
echo "  🔍 memory_search('$TASK')"

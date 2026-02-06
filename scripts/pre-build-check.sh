#!/bin/bash
# Pre-Build Check - Blocks new feature work if send metrics too low
# Usage: ./scripts/pre-build-check.sh [feature-name]

set -e

FEATURE_NAME="${1:-new-feature}"
TODAY=$(date +%Y-%m-%d)
MEMORY_FILE="memory/$TODAY.md"

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "🔍 Pre-Build Check for: $FEATURE_NAME"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if today's memory file exists
if [ ! -f "$MEMORY_FILE" ]; then
    echo -e "${YELLOW}⚠️  Warning: No memory file for today${NC}"
    echo "Creating: $MEMORY_FILE"
    cat > "$MEMORY_FILE" << EOF
# Daily Log: $TODAY

## External Sends
- [ ] None yet

## Built
- [ ] None yet

## Revenue
- €0

---
EOF
fi

# Count external sends today
SEND_COUNT=$(grep -c "^- \[x\].*Send:" "$MEMORY_FILE" 2>/dev/null || echo "0")
BUILD_COUNT=$(grep -c "^- \[x\].*Built:" "$MEMORY_FILE" 2>/dev/null || echo "0")

# Calculate send ratio
if [ "$BUILD_COUNT" -gt 0 ]; then
    RATIO=$(awk "BEGIN {printf \"%.0f\", ($SEND_COUNT / $BUILD_COUNT) * 100}")
else
    RATIO=100  # No builds yet = OK to build first one
fi

echo ""
echo "📊 Today's Metrics:"
echo "   External Sends: $SEND_COUNT"
echo "   Features Built: $BUILD_COUNT"
echo "   Send Ratio: $RATIO%"
echo ""

# Enforcement Rules
if [ "$SEND_COUNT" -eq 0 ] && [ "$BUILD_COUNT" -gt 2 ]; then
    echo -e "${RED}❌ BLOCKED: 0 sends but $BUILD_COUNT builds${NC}"
    echo ""
    echo "🚨 ENFORCEMENT RULE:"
    echo "   Cannot build more than 2 features without ANY send."
    echo ""
    echo "💡 To unblock:"
    echo "   1. Send ONE email/application/outreach"
    echo "   2. Mark it in $MEMORY_FILE"
    echo "   3. Run this check again"
    echo ""
    echo "🎯 Or override (NOT RECOMMENDED):"
    echo "   PRE_BUILD_OVERRIDE=true ./scripts/pre-build-check.sh $FEATURE_NAME"
    echo ""
    
    # Check for override
    if [ "${PRE_BUILD_OVERRIDE}" != "true" ]; then
        exit 1
    else
        echo -e "${YELLOW}⚠️  Override active - proceeding anyway${NC}"
    fi
fi

if [ "$RATIO" -lt 30 ] && [ "$BUILD_COUNT" -gt 3 ]; then
    echo -e "${YELLOW}⚠️  WARNING: Send ratio below 30%${NC}"
    echo "   Building > Sending is a known failure pattern"
    echo "   Recommend: Send 2-3 items before next build"
    echo ""
fi

# All checks passed
echo -e "${GREEN}✅ Pre-build check passed${NC}"
echo ""
echo "📝 Log your build:"
echo "   Add to $MEMORY_FILE:"
echo "   - [x] Built: $FEATURE_NAME"
echo ""

exit 0

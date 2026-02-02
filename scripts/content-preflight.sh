#!/bin/bash
# 📝 Content Pre-Flight Checker
# Quick QA for blog posts before publishing
# Usage: ./content-preflight.sh <file.md>

set -e

FILE="${1:-}"
if [[ -z "$FILE" ]]; then
    echo "Usage: content-preflight.sh <markdown-file>"
    exit 1
fi

if [[ ! -f "$FILE" ]]; then
    echo "❌ File not found: $FILE"
    exit 1
fi

echo "📝 Content Pre-Flight Check: $(basename "$FILE")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Basic stats
WORDS=$(wc -w < "$FILE" | tr -d ' ')
CHARS=$(wc -c < "$FILE" | tr -d ' ')
LINES=$(wc -l < "$FILE" | tr -d ' ')
READ_TIME=$((WORDS / 200))

echo "📊 Stats:"
echo "   Words: $WORDS (~$READ_TIME min read)"
echo "   Characters: $CHARS"
echo "   Lines: $LINES"
echo ""

# Check for common issues
echo "🔍 Quality Checks:"

# Empty sections
EMPTY_HEADERS=$(grep -n '^##' "$FILE" | while read line; do
    LINENUM=$(echo "$line" | cut -d: -f1)
    NEXTLINE=$((LINENUM + 1))
    CONTENT=$(sed -n "${NEXTLINE}p" "$FILE")
    if [[ -z "$CONTENT" || "$CONTENT" =~ ^## ]]; then
        echo "   ⚠️  Empty section at line $LINENUM: $(echo "$line" | cut -d: -f2-)"
    fi
done)
if [[ -n "$EMPTY_HEADERS" ]]; then
    echo "$EMPTY_HEADERS"
else
    echo "   ✅ No empty sections"
fi

# Placeholder text
PLACEHOLDERS=$(grep -n -i -E '\[TODO\]|\[TBD\]|\[XXX\]|\[FIXME\]|lorem ipsum|\.\.\.' "$FILE" 2>/dev/null || true)
if [[ -n "$PLACEHOLDERS" ]]; then
    echo "   ⚠️  Placeholders found:"
    echo "$PLACEHOLDERS" | head -5 | sed 's/^/      /'
else
    echo "   ✅ No placeholders"
fi

# Broken markdown links
BROKEN_LINKS=$(grep -oE '\[([^\]]+)\]\(([^\)]+)\)' "$FILE" | grep -E '\(\s*\)|\(#\)' 2>/dev/null || true)
if [[ -n "$BROKEN_LINKS" ]]; then
    echo "   ⚠️  Empty links: $BROKEN_LINKS"
else
    echo "   ✅ Links look complete"
fi

# Check for sources/references
SOURCES=$(grep -c -i -E '\*source|\*quelle|^\[.*\]:' "$FILE" 2>/dev/null || echo "0")
if [[ "$SOURCES" -gt 0 ]]; then
    echo "   ✅ Sources found: $SOURCES"
else
    echo "   💡 Consider adding sources for credibility"
fi

# Word frequency (find overused words)
echo ""
echo "📈 Top Words (excluding common):"
cat "$FILE" | \
    tr '[:upper:]' '[:lower:]' | \
    tr -cs '[:alpha:]' '\n' | \
    grep -vE '^(der|die|das|und|in|zu|den|ist|von|mit|für|auf|des|dem|ein|eine|einer|eines|als|an|im|sich|nicht|es|auch|aus|wie|bei|oder|nach|so|noch|nur|werden|wenn|bis|um|aber|kann|sind|war|er|sie|haben|hat|wird|ihr|wir|ich|du|was|zum|zur|man|sein|the|and|to|of|a|in|is|that|it|for|on|with|as|be|this|are|was|by|an|have|from|or|one|had|not|but|all|at|you|which|we|can|been)$' | \
    sort | uniq -c | sort -rn | head -10 | \
    awk '{printf "   %3d× %s\n", $1, $2}'

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Pre-flight complete!"

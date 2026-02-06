#!/bin/bash
# demo-checklist.sh — Pre-demo validation for CNC Planner
# Usage: ./scripts/demo-checklist.sh [demo-file]
# Validates HTML integrity, JS syntax, and key features before a demo

set -e
cd "$(dirname "$0")/.."

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

DEMO_FILE="${1:-projects/cnc-planner/cnc-planner-pro-v18-industrial.html}"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "         🔧 CNC PLANNER — PRE-DEMO CHECKLIST 🔧"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "  File: $DEMO_FILE"
echo "  Date: $(date '+%Y-%m-%d %H:%M')"
echo ""

PASS=0
FAIL=0
WARN=0

check() {
    local label="$1"
    local result="$2"  # 0=pass, 1=fail, 2=warn
    local detail="$3"
    
    if [ "$result" -eq 0 ]; then
        echo -e "  ${GREEN}✅${NC} $label"
        PASS=$((PASS + 1))
    elif [ "$result" -eq 2 ]; then
        echo -e "  ${YELLOW}⚠️${NC}  $label — $detail"
        WARN=$((WARN + 1))
    else
        echo -e "  ${RED}❌${NC} $label — $detail"
        FAIL=$((FAIL + 1))
    fi
}

# --- File exists ---
if [ ! -f "$DEMO_FILE" ]; then
    echo -e "${RED}❌ Demo file not found: $DEMO_FILE${NC}"
    exit 1
fi
check "File exists" 0

# --- File size ---
SIZE=$(wc -c < "$DEMO_FILE" | tr -d ' ')
SIZE_KB=$((SIZE / 1024))
if [ "$SIZE_KB" -gt 50 ]; then
    check "File size: ${SIZE_KB}KB" 0
else
    check "File size: ${SIZE_KB}KB" 2 "Unusually small — missing content?"
fi

# --- Line count ---
LINES=$(wc -l < "$DEMO_FILE" | tr -d ' ')
check "Line count: $LINES lines" 0

# --- HTML structure ---
echo ""
echo "${BOLD}  📄 HTML Structure:${NC}"

DIV_OPEN=$(grep -o '<div' "$DEMO_FILE" | wc -l | tr -d ' ')
DIV_CLOSE=$(grep -o '</div>' "$DEMO_FILE" | wc -l | tr -d ' ')
if [ "$DIV_OPEN" -eq "$DIV_CLOSE" ]; then
    check "DIV tags balanced ($DIV_OPEN/$DIV_CLOSE)" 0
else
    check "DIV tags" 1 "Open: $DIV_OPEN, Close: $DIV_CLOSE (diff: $((DIV_OPEN - DIV_CLOSE)))"
fi

TABLE_OPEN=$(grep -o '<table' "$DEMO_FILE" | wc -l | tr -d ' ')
TABLE_CLOSE=$(grep -o '</table>' "$DEMO_FILE" | wc -l | tr -d ' ')
if [ "$TABLE_OPEN" -eq "$TABLE_CLOSE" ]; then
    check "TABLE tags balanced ($TABLE_OPEN/$TABLE_CLOSE)" 0
else
    check "TABLE tags" 1 "Open: $TABLE_OPEN, Close: $TABLE_CLOSE"
fi

# --- JavaScript syntax ---
echo ""
echo "${BOLD}  🔧 JavaScript:${NC}"

# Extract JS and check syntax
JS_CHECK=$(sed -n '/<script>/,/<\/script>/p' "$DEMO_FILE" | sed '1d;$d' | node -e "
try {
    let code = '';
    process.stdin.on('data', d => code += d);
    process.stdin.on('end', () => {
        new Function(code);
        console.log('OK');
    });
} catch(e) {
    console.log('ERROR: ' + e.message);
}" 2>&1)

if [ "$JS_CHECK" = "OK" ]; then
    check "JavaScript syntax valid" 0
else
    check "JavaScript syntax" 1 "$JS_CHECK"
fi

# --- onclick handlers ---
# Extract actual function names from onclick="functionName(..." patterns
ONCLICK_NAMES=$(grep -oE 'onclick="[a-zA-Z_][a-zA-Z0-9_]*\(' "$DEMO_FILE" | sed 's/onclick="//;s/(//' | sort -u)
ONCLICK_COUNT=$(echo "$ONCLICK_NAMES" | grep -c . || echo "0")
UNDEFINED=0
UNDEFINED_LIST=""

for fn in $ONCLICK_NAMES; do
    # Skip built-in JS methods
    case "$fn" in
        document|window|this|event|console|alert|confirm|prompt) continue ;;
    esac
    # Check if function is defined in the file
    if ! grep -qE "function\s+$fn\s*\(" "$DEMO_FILE"; then
        UNDEFINED=$((UNDEFINED + 1))
        UNDEFINED_LIST="$UNDEFINED_LIST $fn"
    fi
done

if [ "$UNDEFINED" -eq 0 ]; then
    check "All $ONCLICK_COUNT onclick handlers defined" 0
else
    check "onclick handlers" 2 "$UNDEFINED not directly defined:$UNDEFINED_LIST"
fi

# --- Key features ---
echo ""
echo "${BOLD}  🏭 CNC Features:${NC}"

# Check for DEFormatter
if grep -q "DEFormatter\|deFormatter\|formatCurrency\|formatPrice" "$DEMO_FILE"; then
    check "Price formatter present" 0
else
    check "Price formatter" 2 "No DEFormatter found — prices may show wrong format"
fi

# Check for Kalkulation
if grep -q "Kalkulation\|kalkulation\|Gesamtkalkulation" "$DEMO_FILE"; then
    check "Kalkulation section present" 0
else
    check "Kalkulation section" 1 "Missing — core feature for demo"
fi

# Check for Angebot/Quote
if grep -q "Angebot\|angebot\|Quote\|quote" "$DEMO_FILE"; then
    check "Angebot/Quote section present" 0
else
    check "Angebot/Quote section" 2 "Missing — may be expected"
fi

# Check for print CSS
if grep -q "@media print" "$DEMO_FILE"; then
    check "Print CSS present" 0
else
    check "Print CSS" 2 "No @media print — printing may look bad"
fi

# --- Old format strings ---
echo ""
echo "${BOLD}  🧹 Cleanup:${NC}"

OLD_EURO=$(grep -c '€[0-9]' "$DEMO_FILE" 2>/dev/null || echo "0")
OLD_EURO=$(echo "$OLD_EURO" | head -1 | tr -d '[:space:]')
if [ "$OLD_EURO" -eq 0 ]; then
    check "No old €X format strings" 0
else
    check "Old format strings" 2 "$OLD_EURO instances of €X found (should be EUR X)"
fi

# Check for placeholder text
PLACEHOLDER=$(grep -ciE 'TODO|FIXME|PLACEHOLDER|XXX' "$DEMO_FILE" 2>/dev/null || echo "0")
PLACEHOLDER=$(echo "$PLACEHOLDER" | head -1 | tr -d '[:space:]')
if [ "$PLACEHOLDER" -eq 0 ]; then
    check "No TODO/FIXME/PLACEHOLDER markers" 0
else
    check "Placeholder text" 2 "$PLACEHOLDER markers found"
fi

# --- Summary ---
echo ""
echo "═══════════════════════════════════════════════════════════════"
TOTAL=$((PASS + FAIL + WARN))
echo -e "  ${GREEN}✅ $PASS passed${NC}  ${RED}❌ $FAIL failed${NC}  ${YELLOW}⚠️  $WARN warnings${NC}  (${TOTAL} total)"

if [ "$FAIL" -gt 0 ]; then
    echo ""
    echo -e "  ${RED}${BOLD}⛔ NOT DEMO-READY — Fix $FAIL issues first${NC}"
    echo ""
    exit 1
elif [ "$WARN" -gt 0 ]; then
    echo ""
    echo -e "  ${YELLOW}${BOLD}⚠️  DEMO-READY with $WARN warnings${NC}"
    echo ""
    exit 0
else
    echo ""
    echo -e "  ${GREEN}${BOLD}🚀 DEMO-READY — Ship it!${NC}"
    echo ""
    exit 0
fi

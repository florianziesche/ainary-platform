#!/bin/bash
# latex-validate.sh — Pre-flight validation for LaTeX documents
# Catches common errors BEFORE running xelatex (saves compile time)
# Usage: ./scripts/latex-validate.sh <file.tex>

set -e
cd "$(dirname "$0")/.."

if [ -z "$1" ]; then
    echo "Usage: $0 <file.tex>"
    echo "  Validates LaTeX source before compilation"
    exit 1
fi

TEX_FILE="$1"
if [ ! -f "$TEX_FILE" ]; then
    echo "❌ File not found: $TEX_FILE"
    exit 1
fi

PASS=0
FAIL=0
WARN=0

check() {
    local status="$1" label="$2"
    if [ "$status" = "PASS" ]; then
        echo "  ✅ $label"
        PASS=$((PASS + 1))
    elif [ "$status" = "FAIL" ]; then
        echo "  ❌ $label"
        FAIL=$((FAIL + 1))
    else
        echo "  ⚠️  $label"
        WARN=$((WARN + 1))
    fi
}

echo ""
echo "📄 LaTeX Validation: $(basename "$TEX_FILE")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# --- 1. Document Structure ---
echo ""
echo "📐 Structure:"

if grep -q '\\documentclass' "$TEX_FILE"; then
    check "PASS" "\\documentclass found"
else
    check "FAIL" "Missing \\documentclass"
fi

if grep -q '\\begin{document}' "$TEX_FILE"; then
    check "PASS" "\\begin{document} found"
else
    check "FAIL" "Missing \\begin{document}"
fi

if grep -q '\\end{document}' "$TEX_FILE"; then
    check "PASS" "\\end{document} found"
else
    check "FAIL" "Missing \\end{document}"
fi

# --- 2. Environment Balance ---
echo ""
echo "🔄 Environment Balance:"

# Check common environments
for ENV in tabular table figure itemize enumerate tcolorbox minipage center; do
    OPENS=$(grep -c "\\\\begin{$ENV}" "$TEX_FILE" 2>/dev/null || echo "0")
    OPENS=$(echo "$OPENS" | tr -d '[:space:]')
    CLOSES=$(grep -c "\\\\end{$ENV}" "$TEX_FILE" 2>/dev/null || echo "0")
    CLOSES=$(echo "$CLOSES" | tr -d '[:space:]')
    if [ "$OPENS" -ne "$CLOSES" ]; then
        check "FAIL" "$ENV: $OPENS opens vs $CLOSES closes"
    elif [ "$OPENS" -gt 0 ]; then
        check "PASS" "$ENV: $OPENS balanced"
    fi
done

# --- 3. Brace Balance ---
echo ""
echo "🔗 Syntax:"

# Count braces (rough check — doesn't handle \{ escapes perfectly)
OPEN_BRACES=$(tr -cd '{' < "$TEX_FILE" | wc -c | tr -d '[:space:]')
CLOSE_BRACES=$(tr -cd '}' < "$TEX_FILE" | wc -c | tr -d '[:space:]')
DIFF=$((OPEN_BRACES - CLOSE_BRACES))
if [ "$DIFF" -eq 0 ]; then
    check "PASS" "Braces balanced ($OPEN_BRACES pairs)"
elif [ "$DIFF" -gt 0 ]; then
    check "FAIL" "Missing $DIFF closing brace(s) ({=$OPEN_BRACES, }=$CLOSE_BRACES)"
else
    ABS_DIFF=$((-DIFF))
    check "FAIL" "Extra $ABS_DIFF closing brace(s) ({=$OPEN_BRACES, }=$CLOSE_BRACES)"
fi

# --- 4. Common Errors ---
echo ""
echo "🔍 Common Issues:"

# Unescaped special characters in text (rough heuristic)
UNESCAPED_PERCENT=$(grep -nP '(?<!\\)%(?!.*\\)' "$TEX_FILE" 2>/dev/null | grep -v "^[[:space:]]*%" | head -3)
# This is tricky because % is the comment char — skip this check

# Check for common typos
if grep -qP '\\beginn{' "$TEX_FILE" 2>/dev/null; then
    check "FAIL" "Typo: \\beginn (should be \\begin)"
else
    check "PASS" "No \\begin typos"
fi

if grep -qP '\\itmize' "$TEX_FILE" 2>/dev/null; then
    check "FAIL" "Typo: \\itmize (should be \\itemize)"
else
    check "PASS" "No environment typos"
fi

# Unescaped & outside tabular (heuristic)
AMPERSAND_OUTSIDE=$(grep -n '&' "$TEX_FILE" | grep -v 'tabular\|\\&\|%' | head -3)
# Skip — too many false positives

# Check for placeholder text
PLACEHOLDERS=$(grep -cin 'TODO\|FIXME\|XXX\|PLACEHOLDER\|\[INSERT\]' "$TEX_FILE" 2>/dev/null || echo "0")
PLACEHOLDERS=$(echo "$PLACEHOLDERS" | tr -d '[:space:]')
if [ "$PLACEHOLDERS" -gt 0 ]; then
    check "WARN" "$PLACEHOLDERS placeholder(s) found (TODO/FIXME/XXX)"
    grep -ni 'TODO\|FIXME\|XXX\|PLACEHOLDER\|\[INSERT\]' "$TEX_FILE" | head -3 | while read -r line; do
        echo "      Line: $line"
    done
else
    check "PASS" "No placeholders"
fi

# --- 5. Font Check (XeLaTeX specific) ---
echo ""
echo "🔤 Fonts:"

if grep -q '\\setmainfont' "$TEX_FILE"; then
    FONT=$(grep '\\setmainfont' "$TEX_FILE" | head -1 | sed 's/.*\\setmainfont{\([^}]*\)}.*/\1/' | sed 's/.*\\setmainfont\[\([^]]*\)\].*/\1/')
    check "PASS" "Main font defined: $FONT"
else
    check "WARN" "No \\setmainfont — using defaults"
fi

if grep -q 'fontspec' "$TEX_FILE"; then
    check "PASS" "fontspec package loaded (XeLaTeX ready)"
else
    check "WARN" "No fontspec — might not be XeLaTeX"
fi

# --- 6. Page Layout ---
echo ""
echo "📏 Layout:"

if grep -q 'geometry' "$TEX_FILE"; then
    MARGINS=$(grep 'geometry' "$TEX_FILE" | head -1)
    check "PASS" "Geometry package: margins defined"
else
    check "WARN" "No geometry package — using defaults"
fi

PAGES_EST=$(wc -l < "$TEX_FILE" | tr -d '[:space:]')
check "PASS" "$PAGES_EST lines (est. $(( PAGES_EST / 50 ))-$(( PAGES_EST / 35 )) pages)"

# --- 7. File size ---
FILE_SIZE=$(wc -c < "$TEX_FILE" | tr -d '[:space:]')
FILE_KB=$((FILE_SIZE / 1024))
check "PASS" "File size: ${FILE_KB}KB"

# --- Summary ---
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
TOTAL=$((PASS + FAIL + WARN))
echo "  Results: $PASS pass, $FAIL fail, $WARN warn (of $TOTAL checks)"

if [ "$FAIL" -gt 0 ]; then
    echo "  ❌ FIX ERRORS before compiling"
    exit 1
elif [ "$WARN" -gt 0 ]; then
    echo "  ⚠️  Warnings — review before final PDF"
    exit 0
else
    echo "  ✅ ALL CLEAR — ready to compile"
    exit 0
fi

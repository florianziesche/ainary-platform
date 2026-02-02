#!/bin/bash
# token-estimate.sh - Quick token cost estimator for files
# Usage: ./scripts/token-estimate.sh [file or directory]
# Aligned with Florian's "Token Budget = Währung" principle

TARGET="${1:-.}"
TOTAL_CHARS=0
TOTAL_LINES=0

# Color codes
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "📊 Token Estimate for: $TARGET"
echo "────────────────────────────────────────"

if [[ -f "$TARGET" ]]; then
    CHARS=$(wc -c < "$TARGET")
    LINES=$(wc -l < "$TARGET")
    TOKENS=$((CHARS / 4))  # ~4 chars per token (rough estimate)
    
    echo "File: $(basename "$TARGET")"
    echo "  Chars: $CHARS | Lines: $LINES | ~Tokens: $TOKENS"
else
    # Directory mode - show top files by size
    echo "Top files by token cost:"
    echo ""
    
    find "$TARGET" -type f \( -name "*.md" -o -name "*.js" -o -name "*.json" -o -name "*.txt" \) 2>/dev/null | while read -r file; do
        if [[ -f "$file" ]]; then
            CHARS=$(wc -c < "$file" 2>/dev/null || echo 0)
            TOKENS=$((CHARS / 4))
            echo "$TOKENS $file"
        fi
    done | sort -rn | head -20 | while read -r tokens file; do
        if [[ $tokens -gt 10000 ]]; then
            printf "${RED}%6d tokens${NC}  %s\n" "$tokens" "$file"
        elif [[ $tokens -gt 2500 ]]; then
            printf "${YELLOW}%6d tokens${NC}  %s\n" "$tokens" "$file"
        else
            printf "${GREEN}%6d tokens${NC}  %s\n" "$tokens" "$file"
        fi
    done
fi

echo ""
echo "────────────────────────────────────────"
echo "Legend: 🔴 >10K tokens | 🟡 >2.5K | 🟢 <2.5K"
echo "Rule: Progressive Disclosure > Full Context"

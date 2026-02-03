#!/bin/bash
# Quick Translate - DE↔EN content translation helper
# Usage: ./scripts/quick-translate.sh <file> [de|en]
# Copies content to clipboard, ready for translation

FILE="$1"
TARGET="${2:-en}"

if [ -z "$FILE" ]; then
    echo "Usage: ./scripts/quick-translate.sh <file> [de|en]"
    echo "  de = translate to German"
    echo "  en = translate to English (default)"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File not found: $FILE"
    exit 1
fi

# Create output filename
BASENAME=$(basename "$FILE" .md)
DIR=$(dirname "$FILE")
OUTPUT="$DIR/${BASENAME}-${TARGET^^}.md"

echo "📋 Source: $FILE"
echo "🎯 Target: $OUTPUT"
echo "🌐 Language: ${TARGET^^}"
echo ""
echo "Content copied to clipboard. Paste to AI for translation."
echo "Save result to: $OUTPUT"

# Copy to clipboard (macOS)
cat "$FILE" | pbcopy

echo "✅ Ready!"

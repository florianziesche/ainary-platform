#!/bin/bash
# html-to-pdf.sh — Convert Ainary Report HTML to PDF via headless Chrome
# Usage: ./scripts/html-to-pdf.sh <input.html> [output.pdf]
# Cost: $0. Time: ~2s. No API calls.

set -e

INPUT="$1"
OUTPUT="${2:-${INPUT%.html}.pdf}"

if [ -z "$INPUT" ]; then
  echo "Usage: ./scripts/html-to-pdf.sh <input.html> [output.pdf]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: File not found: $INPUT"
  exit 1
fi

# Use Chrome (macOS path)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [ ! -f "$CHROME" ]; then
  echo "Error: Chrome not found at $CHROME"
  exit 1
fi

# Convert to absolute path for file:// URL
ABS_INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="$OUTPUT" \
  --print-to-pdf-no-header \
  "file://$ABS_INPUT" \
  2>/dev/null

echo "✅ PDF saved: $OUTPUT"

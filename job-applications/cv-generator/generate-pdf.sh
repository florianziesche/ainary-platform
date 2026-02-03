#!/bin/bash
# Generate CV PDF from HTML using Chrome
# Usage: ./generate-pdf.sh [output-name]

OUTPUT="${1:-cv-florian}"
HTML_FILE="$(dirname "$0")/cv-florian.html"
PDF_FILE="$(dirname "$0")/${OUTPUT}.pdf"

# Chrome path
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [ ! -f "$CHROME" ]; then
    echo "❌ Chrome not found. Using print dialog..."
    echo "   Open: file://$HTML_FILE"
    echo "   Press Cmd+P → Save as PDF"
    open "$HTML_FILE"
    exit 0
fi

echo "📄 Generating PDF..."

"$CHROME" \
    --headless \
    --disable-gpu \
    --print-to-pdf="$PDF_FILE" \
    --print-to-pdf-no-header \
    --no-margins \
    "file://$HTML_FILE" 2>/dev/null

if [ -f "$PDF_FILE" ]; then
    echo "✅ Created: $PDF_FILE"
    open "$PDF_FILE"
else
    echo "❌ Failed. Fallback to manual print."
    open "$HTML_FILE"
fi

#!/bin/bash
# Convert HTML to PNG using Chrome headless
# Usage: ./html-to-png.sh input.html output.png [width] [height]

INPUT="$1"
OUTPUT="$2"
WIDTH="${3:-1200}"
HEIGHT="${4:-630}"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: ./html-to-png.sh input.html output.png [width] [height]"
    exit 1
fi

# Check if Chrome is available
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -f "$CHROME" ]; then
    CHROME="/Applications/Chromium.app/Contents/MacOS/Chromium"
fi

if [ ! -f "$CHROME" ]; then
    echo "❌ Chrome/Chromium not found. Using Safari fallback..."
    echo "   Open: file://$INPUT"
    echo "   Screenshot: Cmd+Shift+4 → Space → Click window"
    open "$INPUT"
    exit 0
fi

echo "📸 Converting $INPUT → $OUTPUT (${WIDTH}x${HEIGHT})"

"$CHROME" \
    --headless \
    --disable-gpu \
    --screenshot="$OUTPUT" \
    --window-size="${WIDTH},${HEIGHT}" \
    --default-background-color=00000000 \
    "file://$INPUT" 2>/dev/null

if [ -f "$OUTPUT" ]; then
    echo "✅ Saved: $OUTPUT"
else
    echo "❌ Failed. Try Safari method."
fi

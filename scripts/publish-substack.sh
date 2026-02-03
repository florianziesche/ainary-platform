#!/bin/bash
# Quick Substack Publish Helper
# Converts HTML graphics to PNG and opens everything needed

GRAPHICS_DIR="$HOME/.openclaw/workspace/content/drafts/substack/graphics"
OUTPUT_DIR="$GRAPHICS_DIR/png"
mkdir -p "$OUTPUT_DIR"

echo "📸 Converting HTML graphics to PNG..."

# Function to convert HTML to PNG using Safari + screencapture
convert_html_to_png() {
    local html_file="$1"
    local output_name="$2"
    local width="${3:-1200}"
    local height="${4:-630}"
    
    # Open in Safari at specific size
    osascript <<EOF
tell application "Safari"
    activate
    open POSIX file "$html_file"
    delay 1
    set bounds of front window to {0, 0, $width, $height}
end tell
EOF
    
    echo "  → Opened $output_name (${width}x${height})"
    echo "    Press Cmd+Shift+4, then Space, click window"
    echo "    Save as: $OUTPUT_DIR/$output_name.png"
}

# List available graphics
echo ""
echo "Available graphics:"
ls -1 "$GRAPHICS_DIR"/*.html 2>/dev/null | while read f; do
    echo "  - $(basename "$f")"
done

echo ""
echo "Opening Substack editor..."
open "https://finitematter.substack.com/publish/post"

echo ""
echo "Done! Workflow:"
echo "1. Screenshot each graphic (Cmd+Shift+4 → Space → Click)"
echo "2. Paste into Substack"
echo "3. Publish!"

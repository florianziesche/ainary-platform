#!/bin/bash

# Content Repurposing Pipeline
# Input: Markdown article path
# Output: 5 repurposed content pieces

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <article-path>"
    exit 1
fi

ARTICLE_PATH="$1"
OUTPUT_BASE="${2:-./content/repurposed}"

if [ ! -f "$ARTICLE_PATH" ]; then
    echo "Error: Article not found at $ARTICLE_PATH"
    exit 1
fi

# Extract article name from path for output folder
ARTICLE_NAME=$(basename "$ARTICLE_PATH" .md | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
OUTPUT_DIR="$OUTPUT_BASE/$ARTICLE_NAME"

mkdir -p "$OUTPUT_DIR"

echo "Repurposing: $ARTICLE_PATH"
echo "Output to: $OUTPUT_DIR"
echo ""

# This script is a wrapper - the actual AI processing happens via the agent
# calling this with the article content and generating the 5 pieces

cat << EOF
Content Repurposing Pipeline Started
=====================================

Article: $ARTICLE_PATH
Output Directory: $OUTPUT_DIR

The following pieces will be generated:
1. LinkedIn Post (linkedin.txt)
2. Twitter Thread (twitter.txt)
3. Obsidian Note (obsidian.md)
4. Newsletter Teaser (newsletter-teaser.txt)
5. Carousel Text (carousel.txt)

Processing...
EOF

# Mark as ready for AI processing
echo "$ARTICLE_PATH" > "$OUTPUT_DIR/.source"
echo "$(date)" > "$OUTPUT_DIR/.generated"

echo ""
echo "Ready for AI content generation."

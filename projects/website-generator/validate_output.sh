#!/bin/bash
# Quick validation of generated website

HTML_FILE="$1"

if [ ! -f "$HTML_FILE" ]; then
    echo "❌ File not found: $HTML_FILE"
    exit 1
fi

echo "Validating: $HTML_FILE"
echo ""

# Check file size
SIZE=$(wc -c < "$HTML_FILE")
echo "✓ File size: $(($SIZE / 1024))KB"

# Check required sections
for section in "hero" "ueber-uns" "leistungen" "kontakt"; do
    if grep -q "id=\"$section\"" "$HTML_FILE"; then
        echo "✓ Section: $section"
    else
        echo "❌ Missing section: $section"
    fi
done

# Check Ainary Ventures credit
if grep -q "Ainary Ventures" "$HTML_FILE"; then
    echo "✓ Footer credit: Ainary Ventures"
else
    echo "❌ Missing footer credit"
fi

# Check responsive CSS
if grep -q "@media (max-width:" "$HTML_FILE"; then
    echo "✓ Responsive CSS"
else
    echo "❌ No responsive CSS"
fi

# Check Schema.org
if grep -q "application/ld+json" "$HTML_FILE"; then
    echo "✓ Schema.org structured data"
else
    echo "❌ No structured data"
fi

# Check animations
if grep -q "fadeIn\|fade-in" "$HTML_FILE"; then
    echo "✓ Animations present"
else
    echo "❌ No animations"
fi

echo ""
echo "Validation complete!"

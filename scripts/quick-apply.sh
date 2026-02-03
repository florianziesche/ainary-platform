#!/bin/bash
# Quick Job Application Generator
# Usage: ./quick-apply.sh "Fund Name" "Role" "Contact Person"

FUND="${1:-Unknown Fund}"
ROLE="${2:-Associate}"
CONTACT="${3:-Hiring Manager}"

TEMPLATE_DIR="$HOME/.openclaw/workspace/job-applications"
OUTPUT_DIR="$TEMPLATE_DIR/applications/$(date +%Y-%m-%d)-$(echo $FUND | tr ' ' '-' | tr '[:upper:]' '[:lower:]')"

mkdir -p "$OUTPUT_DIR"

echo "🚀 Generating application for: $FUND"
echo "   Role: $ROLE"
echo "   Contact: $CONTACT"
echo ""

# Copy templates
cp "$TEMPLATE_DIR/cv-template.tex" "$OUTPUT_DIR/cv-$FUND.tex"
cp "$TEMPLATE_DIR/cover-letter-template.tex" "$OUTPUT_DIR/cover-letter-$FUND.tex"

# Create tracking file
cat > "$OUTPUT_DIR/README.md" << EOF
# Application: $FUND

**Date:** $(date +%Y-%m-%d)
**Role:** $ROLE
**Contact:** $CONTACT

## Status
- [ ] CV customized
- [ ] Cover letter written
- [ ] PDF generated
- [ ] Application sent
- [ ] Follow-up scheduled

## Notes

EOF

echo "✅ Created application folder: $OUTPUT_DIR"
echo ""
echo "Next steps:"
echo "1. Edit cover letter: code $OUTPUT_DIR/cover-letter-$FUND.tex"
echo "2. Compile: cd $OUTPUT_DIR && pdflatex cv-$FUND.tex"
echo "3. Send!"

# Open the folder
open "$OUTPUT_DIR"

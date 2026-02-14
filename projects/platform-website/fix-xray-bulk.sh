#!/bin/bash
# FIX 3 — X-Ray → Ainary Report renaming

cd /Users/florianziesche/.openclaw/workspace/projects/platform-website

# Function to replace in a file
fix_xray() {
  local file="$1"
  if [ ! -f "$file" ]; then
    return
  fi
  
  echo "Processing $file..."
  
  # Specific replacements (order matters - most specific first)
  sed -i.bak \
    -e 's/Corporate X-Ray/Ainary Company Report/g' \
    -e 's/Startup X-Ray/Ainary Due Diligence Report/g' \
    -e 's/Company X-Ray/Ainary Company Report/g' \
    -e 's/Unlimited X-Rays/Unlimited Ainary Reports/g' \
    -e 's/X-Ray Reports/Ainary Reports/g' \
    -e 's/X-Ray Report/Ainary Report/g' \
    -e 's/>X-Ray</>Ainary Report</g' \
    -e 's/try-xray/try-ainary/g' \
    -e 's/Try X-Ray/Try Ainary/g' \
    "$file"
  
  rm -f "$file.bak"
}

# Files to process (excluding already done: design-system.html, dashboard.html)
FILES="
article.html
terms.html
pricing-tier.html
imprint.html
pricing-simple.html
pricing-credits.html
quality.html
svg-graphics.html
de/article.html
de/terms.html
de/privacy.html
de/article-one-person-company.html
de/article-100-agents.html
"

for file in $FILES; do
  fix_xray "$file"
done

echo "✅ FIX 3 — X-Ray → Ainary Report renaming complete!"

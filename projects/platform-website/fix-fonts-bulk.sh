#!/bin/bash
# Bulk fix Google Fonts → Self-hosted for remaining files
# FIX 1 — DSGVO Google Fonts

FONT_REPLACEMENT_FULL='<style>\n    /* Self-hosted fonts for GDPR\/DSGVO compliance *\/\n    @font-face {\n      font-family: '\''Inter'\'';\n      font-style: normal;\n      font-weight: 300 700;\n      font-display: swap;\n      src: url('\''/fonts\/inter-variable.woff2'\'') format('\''woff2'\'');\n    }\n    @font-face {\n      font-family: '\''JetBrains Mono'\'';\n      font-style: normal;\n      font-weight: 400 500;\n      font-display: swap;\n      src: url('\''/fonts\/jetbrains-mono-variable.woff2'\'') format('\''woff2'\'');\n    }\n    '

FONT_REPLACEMENT_INTER_ONLY='<style>\n    /* Self-hosted fonts for GDPR\/DSGVO compliance *\/\n    @font-face {\n      font-family: '\''Inter'\'';\n      font-style: normal;\n      font-weight: 300 700;\n      font-display: swap;\n      src: url('\''/fonts\/inter-variable.woff2'\'') format('\''woff2'\'');\n    }\n    '

# Files already done: index.html about.html pricing.html blog.html tools.html dashboard.html design-system.html contact.html

FILES_TO_FIX="
article.html
daily-brief.html
imprint.html
landing-v4.html
landing.html
loading.html
login.html
logo-options.html
pricing-credits.html
pricing-simple.html
pricing-tier.html
privacy.html
quality.html
report.html
reports.html
signup.html
terms.html
app.html
article-100-agents.html
article-one-person-company.html
svg-graphics.html
test-logo-glow.html
de/about.html
de/article.html
de/blog.html
de/daily-brief.html
de/imprint.html
de/index.html
de/pricing.html
de/privacy.html
de/terms.html
de/tools.html
de/article-100-agents.html
de/article-one-person-company.html
og/og-about.html
og/og-article.html
og/og-blog.html
og/og-daily-brief.html
og/og-landing.html
og/og-login.html
og/og-pricing.html
og/og-quality.html
og/og-signup.html
og/og-tools.html
"

cd /Users/florianziesche/.openclaw/workspace/projects/platform-website

for file in $FILES_TO_FIX; do
  if [ -f "$file" ]; then
    echo "Processing $file..."
    
    # Check if file has JetBrains Mono reference
    if grep -q "JetBrains.Mono" "$file"; then
      # Has both Inter and JetBrains Mono
      # Pattern 1: With Geist
      if grep -q "geist@1.0.0" "$file"; then
        sed -i.bak '/<!-- Fonts -->/,/<style>/c\
  '"$FONT_REPLACEMENT_FULL" "$file"
      else
        # Pattern 2: Without Geist
        sed -i.bak '/<link href="https:\/\/fonts.googleapis.com\/css2.*Inter.*JetBrains/,/<style>/c\
  '"$FONT_REPLACEMENT_FULL" "$file"
      fi
    else
      # Only Inter
      sed -i.bak '/<link href="https:\/\/fonts.googleapis.com\/css2.*Inter/,/<style>/c\
  '"$FONT_REPLACEMENT_INTER_ONLY" "$file"
    fi
    
    rm -f "$file.bak"
  else
    echo "⚠️  File not found: $file"
  fi
done

echo "✅ FIX 1 — Google Fonts replacement complete!"

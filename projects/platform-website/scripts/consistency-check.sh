#!/bin/bash
# Website Consistency Checker — run after every change
cd "$(dirname "$0")/.."

echo "=== CONSISTENCY CHECK ==="
echo ""

# 1. Footer: All marketing pages use shared-cta.js
echo "1. SHARED FOOTER"
for f in landing.html tools.html daily-brief.html blog.html pricing.html quality.html about.html contact.html; do
  if grep -q "shared-cta.js" "$f" 2>/dev/null; then
    echo "  ✅ $f"
  else
    echo "  ❌ $f — MISSING shared-cta.js"
  fi
done
echo ""

# 2. No old inline footers remaining
echo "2. OLD FOOTERS (should be 0)"
for f in landing.html tools.html daily-brief.html blog.html pricing.html quality.html about.html; do
  count=$(grep -c "<footer" "$f" 2>/dev/null)
  if [ "$count" -gt 0 ]; then
    echo "  ❌ $f — has $count inline <footer> tags"
  fi
done
echo ""

# 3. btn-primary color consistency
echo "3. BTN-PRIMARY COLOR"
for f in *.html; do
  col=$(grep -o 'btn-primary.*color:[^;]*' "$f" 2>/dev/null | grep -o 'color:[^;]*' | head -1)
  if echo "$col" | grep -q "08080c\|black"; then
    echo "  ❌ $f — btn-primary is BLACK ($col)"
  fi
done
echo ""

# 4. --accent color
echo "4. ACCENT COLOR (should be #c8aa50)"
for f in *.html; do
  if grep -q "6366f1\|indigo" "$f" 2>/dev/null; then
    echo "  ❌ $f — has indigo/6366f1"
  fi
done
echo ""

# 5. Logo pulse on all pages
echo "5. LOGO PULSE"
for f in *.html; do
  if grep -q "logo-dot" "$f" 2>/dev/null; then
    if ! grep -q "logo-pulse" "$f" 2>/dev/null; then
      echo "  ❌ $f — has logo but NO pulse animation"
    fi
  fi
done
echo ""

# 6. Nav consistency (same links on all marketing pages)
echo "6. NAV LINKS"
for f in landing.html tools.html daily-brief.html blog.html pricing.html quality.html about.html contact.html; do
  nav=$(grep -o 'nav-link.*href="[^"]*"' "$f" 2>/dev/null | sort | md5)
  echo "  $f: $nav"
done
echo ""

# 7. Font loading
echo "7. FONTS (Inter + JetBrains Mono)"
for f in landing.html tools.html daily-brief.html blog.html pricing.html quality.html about.html; do
  if ! grep -q "Inter" "$f" 2>/dev/null; then
    echo "  ❌ $f — missing Inter font"
  fi
done
echo ""

# 8. Canonical URLs
echo "8. CANONICAL URLs"
for f in landing.html tools.html daily-brief.html blog.html pricing.html quality.html about.html contact.html; do
  if ! grep -q 'rel="canonical"' "$f" 2>/dev/null; then
    echo "  ❌ $f — missing canonical URL"
  fi
done
echo ""

echo "=== CHECK COMPLETE ==="

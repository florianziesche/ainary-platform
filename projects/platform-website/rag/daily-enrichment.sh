#!/bin/bash
# Daily Enrichment Loop — runs via OpenClaw cron or manually
# Usage: bash rag/daily-enrichment.sh [--dry-run]
set -e

cd "$(dirname "$0")/.."
DATE=$(date +%Y-%m-%d)
DRY_RUN="${1:-}"

echo "═══════════════════════════════════════════════"
echo "DAILY ENRICHMENT — $DATE"
echo "═══════════════════════════════════════════════"

# Step 1: Scan
echo ""
echo "▶ STEP 1: SCANNING ALL CITIES..."
python3 rag/auto_enrich.py --execute --propagate 2>&1 | tee /tmp/enrichment-scan-$DATE.log

# Step 2: Reflect on each city
echo ""
echo "▶ STEP 2: REFLECTING..."
for city_file in data/cities/*.json; do
  city=$(basename "$city_file" .json)
  if [ "$city" != "index" ]; then
    echo "  Reflecting: $city"
    python3 rag/reflect.py "$city_file" --full 2>&1 | tail -5
  fi
done

# Step 3: Validate all
echo ""
echo "▶ STEP 3: VALIDATING..."
PASS=0
FAIL=0
for city_file in data/cities/*.json; do
  city=$(basename "$city_file" .json)
  if [ "$city" != "index" ]; then
    result=$(python3 rag/validate_city.py "$city_file" 2>&1 | grep "Result:")
    if echo "$result" | grep -q "PASS"; then
      echo "  ✅ $city"
      PASS=$((PASS + 1))
    else
      echo "  ❌ $city — $result"
      FAIL=$((FAIL + 1))
    fi
  fi
done

echo ""
echo "═══════════════════════════════════════════════"
echo "SUMMARY: $PASS passed, $FAIL failed"
echo "═══════════════════════════════════════════════"

# Step 4: Deploy (unless dry-run)
if [ "$DRY_RUN" = "--dry-run" ]; then
  echo "🔍 Dry run — no deploy"
else
  echo ""
  echo "▶ STEP 4: DEPLOYING..."
  git add data/cities/*.json rag/learning-journal.json rag/cross-city-insights.json 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "  No changes to deploy."
  else
    git commit -m "auto: Daily enrichment $DATE — $PASS cities validated"
    git push
    vercel --prod --yes 2>&1 | tail -3
    echo "  ✅ Deployed to production"
  fi
fi

echo ""
echo "Done. $DATE"

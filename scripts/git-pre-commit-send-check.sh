#!/bin/bash
# Git pre-commit hook: Send Enforcement
# Installation: ln -s ../../scripts/git-pre-commit-send-check.sh .git/hooks/pre-commit
# (Florian muss aktivieren)

SEND_LOG="memory/send-tracker.md"
TODAY=$(date +%Y-%m-%d)

if [ ! -f "$SEND_LOG" ]; then
  echo "⚠️  Send tracker not found. Commit allowed (setup needed)."
  exit 0
fi

# Check if today has any sends
if ! grep -q "$TODAY" "$SEND_LOG"; then
  echo ""
  echo "🚨 SEND ENFORCEMENT BLOCK"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "You have NOT sent anything today ($TODAY)."
  echo ""
  echo "RULE: Send FIRST, commit LATER."
  echo ""
  echo "Options:"
  echo "  1. Send an outreach email/LinkedIn message/tweet"
  echo "  2. Log it: echo '$TODAY | [description]' >> memory/send-tracker.md"
  echo "  3. Override (emergency): git commit --no-verify"
  echo ""
  exit 1
fi

echo "✅ Send enforcement passed (found sends for $TODAY)"
exit 0

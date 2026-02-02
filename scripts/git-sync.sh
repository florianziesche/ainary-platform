#!/bin/bash
# git-sync.sh — Quick workspace sync
# Usage: ./scripts/git-sync.sh "commit message"

set -e
cd "$(dirname "$0")/.."

MSG="${1:-🔄 Auto-sync}"

# Stage all changes
git add -A

# Check if there's anything to commit
if git diff --cached --quiet; then
    echo "✅ Nothing to commit"
    exit 0
fi

# Commit
git commit -m "$MSG"

# Push if remote exists
if git remote | grep -q origin; then
    git push origin main 2>/dev/null || echo "⚠️ Push skipped (no remote or auth issue)"
fi

echo "✅ Synced: $MSG"

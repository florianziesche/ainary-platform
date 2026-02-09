# OBSIDIAN-VAULT-QA.md — Automatische Qualitätssicherung
*Created: 2026-02-09 | Author: Mia*

## Wann ausführen
- Nach JEDEM Sub-Agent der Obsidian-Dateien ändert
- Nach jedem manuellen Vault-Eingriff
- 1x pro Woche im Heartbeat

## Validierungs-Script

```bash
#!/bin/bash
VAULT=~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/System_OS
ERRORS=0

echo "🔍 OBSIDIAN VAULT QA CHECK"
echo "=========================="
echo ""

# 1. Broken path-style links
echo "1. PATH-STYLE LINKS (should be 0):"
PATHLINKS=$(grep -rn '\[\[.*\/.*\]\]' "$VAULT" --include="*.md" 2>/dev/null | grep -v "http" | grep -v "ORGANIZATION" | grep -v ".trash" | wc -l | tr -d ' ')
echo "   Found: $PATHLINKS"
if [ "$PATHLINKS" -gt 5 ]; then ERRORS=$((ERRORS+1)); echo "   ❌ FAIL"; else echo "   ✅ PASS"; fi

# 2. Files without Created
echo "2. FILES WITHOUT CREATED (should be 0):"
NO_CREATED=$(find "$VAULT" -name "*.md" -not -path "*/.trash/*" -not -path "*/.obsidian/*" | while read f; do
  grep -qL "Created:" "$f" 2>/dev/null && echo "$f"
done | wc -l | tr -d ' ')
echo "   Found: $NO_CREATED"
if [ "$NO_CREATED" -gt 10 ]; then ERRORS=$((ERRORS+1)); echo "   ❌ FAIL"; else echo "   ✅ PASS"; fi

# 3. Duplicate filenames
echo "3. DUPLICATE FILENAMES (should be 0):"
DUPES=$(find "$VAULT" -name "*.md" -not -path "*/.trash/*" -exec basename {} \; | sort | uniq -d)
if [ -n "$DUPES" ]; then
  echo "   ❌ DUPLICATES: $DUPES"
  ERRORS=$((ERRORS+1))
else
  echo "   ✅ PASS"
fi

# 4. Empty folders
echo "4. EMPTY FOLDERS:"
find "$VAULT" -type d -empty -not -path "*/.trash/*" -not -path "*/.obsidian/*" 2>/dev/null | sed "s|$VAULT/||"

# 5. Duplicate numbered prefixes
echo "5. FOLDER NUMBER CONFLICTS:"
ls -d "$VAULT"/*/ 2>/dev/null | sed "s|$VAULT/||" | sed 's|/||' | awk -F'-' '{print $1}' | sort | uniq -d | while read num; do
  echo "   ⚠️ Number $num used by:"
  ls -d "$VAULT/$num"*/ 2>/dev/null | sed "s|$VAULT/||"
done

# 6. Orphaned files (no incoming links) — sample top 10
echo "6. ORPHANED FILES (no incoming links, sample):"
find "$VAULT" -name "*.md" -not -path "*/.trash/*" -not -name "_*" -not -name ".*" | shuf | head -20 | while read f; do
  fname=$(basename "$f" .md)
  incoming=$(grep -rl "\[\[$fname" "$VAULT" --include="*.md" 2>/dev/null | grep -v "$f" | wc -l | tr -d ' ')
  if [ "$incoming" -eq "0" ]; then
    echo "   ⚠️ $(echo $f | sed "s|$VAULT/||")"
  fi
done

echo ""
echo "=========================="
echo "TOTAL ERRORS: $ERRORS"
if [ "$ERRORS" -eq 0 ]; then
  echo "✅ VAULT IS HEALTHY"
else
  echo "❌ VAULT NEEDS ATTENTION"
fi
```

## Was bei Fehlern tun

| Check | Fix |
|-------|-----|
| Path-style links > 5 | `sed` batch-fix: Pfad-Präfix entfernen |
| Files without Created > 10 | Sub-Agent: metadata-audit |
| Duplicate filenames | Merge vollständigere behalten, kürzere löschen |
| Empty folders | `rmdir` |
| Folder number conflicts | Umbenennen (nur wenn alle Links filename-only) |
| Orphaned files | Related Section + Links hinzufügen |

## Changelog
- 2026-02-09: Created nach 6 Sub-Agent Runs mit inkonsistenten Ergebnissen (Mia)

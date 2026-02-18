# OBSIDIAN-LINKING-PROTOCOL.md
*Created: 2026-02-09 | Author: Mia + Florian*

## Warum das existiert
Sub-Agents haben systematisch fehlerhafte Links produziert. Dieses Protokoll verhindert das.

---

## Regeln (nicht optional)

### 1. Wikilinks = NUR Dateiname, KEIN Pfad
```
✅ [[03-Selbstkritik]]
❌ [[MIA/03-Selbstkritik]]

✅ [[Corporate-Identity]]
❌ [[Ainary/Brand/Corporate-Identity]]
```
**Warum:** Obsidian resolved Wikilinks nach Dateiname, nicht nach Ordnerpfad. Pfad-Links brechen.

### 2. Backlinks sind PFLICHT
Wenn A → B verlinkt, MUSS B → A zurückverlinken.
```
# In Definition-of-Done.md:
- **↔ Pattern:** [[Output-Preflight]] — DoD definiert WANN, Preflight WIE

# In Output-Preflight.md:
- **↔ Pattern:** [[Definition-of-Done]] — Preflight definiert WIE, DoD WANN
```
**Prüfung:** Nach dem Verlinken: "Wenn ich Datei B öffne, sehe ich den Link zurück zu A?"

### 3. Typed Links Format
```markdown
## Related
- **↑ Herkunft:** [[Dateiname]] — Ein Satz (woher kam das)
- **↓ Output:** [[Dateiname]] — Ein Satz (was wurde daraus)
- **↔ Pattern:** [[Dateiname]] — Ein Satz (gleiches Muster, anderer Kontext)
```
- Max 2-3 pro Kategorie
- Jeder Link MUSS Kontext-Satz haben
- Leere Kategorien weglassen

### 4. Validierung (MUSS nach jedem Linking-Run passieren)
```bash
VAULT=~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/System_OS

# 1. Finde broken links (Pfade statt Dateinamen)
grep -rn '\[\[.*\/.*\]\]' "$VAULT" --include="*.md" | grep -v "http"

# 2. Finde verwaiste Dateien (keine eingehenden Links)
# Jede Datei in 10-Projects/ und 50-Standards/ sollte mindestens 1 eingehenden Link haben

# 3. Backlink-Check für wichtige Dateien
for f in Definition-of-Done Output-Preflight Twin Florian THE-PROTOCOL; do
  echo "=== $f linked FROM: ==="
  grep -rl "$f" "$VAULT" --include="*.md" | wc -l
done
```

### 5. Häufige Fehler (Sub-Agent Failure Patterns)
| Fehler | Warum | Fix |
|--------|-------|-----|
| `[[MIA/03-Selbstkritik]]` statt `[[03-Selbstkritik]]` | Sub-Agent nutzt Dateipfad statt Name | NUR Dateiname, nie Pfad |
| A→B aber nicht B→A | Sub-Agent vergisst Backlinks | Immer beide Richtungen |
| Links ohne Kontext-Satz | Sub-Agent spart Zeit | Pflicht: "— Ein Satz warum" |
| Zu viele Links (10+ pro Datei) | Sub-Agent verlinkt alles | Max 2-3 pro Kategorie |
| Links zu nicht-existierenden Dateien | Sub-Agent erfindet Namen | Erst prüfen ob Datei existiert |

---

## Changelog
- 2026-02-09: Created nach systematischen Linking-Fehlern in 4 Sub-Agent Runs (Mia)

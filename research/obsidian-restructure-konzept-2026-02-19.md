# Obsidian Vault Restructure Konzept — System_OS
*IST-Analyse → Gap-Analyse → SOLL-Konzept*
*Erstellt: 2026-02-19*
*Status: DRAFT — Florian entscheidet*

---

## Executive Summary

**Problem:** 461 Dateien, 40% <50 Zeilen, 25+ Ordner allein in `20_Areas` → Fragmentierung, Redundanz, tote Links
**Vision:** Weniger Ordner, längere Dokumente mit TOC + Versionierung, Stale-Detection
**Ergebnis:** 5-7 Top-Level Ordner, ~80-120 konsolidierte Docs (70% Reduktion), klare Ownership, automatische Staleness-Checks

---

## Phase 1: IST-Analyse

### Quantitative Facts
- **Dateien gesamt:** 461 `.md` Dateien
- **Zählbar:** 437 (24 file locks — daily notes, archive)
- **Durchschnitt:** 179 Zeilen/Datei
- **Fragmentiert:** 178 Dateien <50 Zeilen (40%) — stubs, claims, kurze notes
- **Ordnerstruktur:** 10 Top-Level + 25 Sub-Ordner in `20_Areas` allein

### Aktuelle Ordnerstruktur
```
System_OS/
├── 00_Inbox (2 files)
├── 02_Daily (9 files, avg ~60 lines)
├── 10_Projects (8 files + sub-folders: AgentTrust, Mia-Evolution, Compound-System, etc.)
├── 20_Areas (1 file + 7 sub-areas)
│   ├── AI-Research (24 files + Claims sub-folder: 15 tiny claim files)
│   ├── Content (66 files: Articles-DE, Articles-EN, Drafts, Publish, Social, Reviewed, Strategy)
│   ├── Venture-Capital (31 files: Applications, Fund-Research, Materials, Networking, Thesis)
│   ├── Freelance (17 files: AI-Consulting, CNC-Planner, Proposals)
│   ├── Business (1 file)
│   ├── Finance (1 file)
│   └── Family (0 files)
├── 30_People (7 files + sub-folders: Family, LPs, Networking, VCs)
├── 50_Decisions (3 files)
├── 60_Resources (2 files + sub-folders: AI, Architecture, Brand, Business, Knowledge, Lessons, Prompts, Standards, VC)
├── 70_Templates (5 files: Content, System, VC)
├── 90_Archive (17 files + old projects, meta-reports)
└── 99_System (4 files + sub-folders: Cockpit, Failures, MIA, Sync, Vault)
```

### Datei-Typen (Sample-basierte Analyse)
1. **MOC (Maps of Content):** System-MOC, Projects-MOC, Resources-MOC → Navigation-Hubs
2. **Reports:** AR-001 bis AR-009 (AI Research) → strukturiert, 100-300 lines
3. **Claims:** C001-C015 → 10-20 lines, standalone → **Merge-Kandidaten**
4. **Content:** Articles, Drafts, Social Posts → stark fragmentiert (66 files in Content/)
5. **Stubs:** "stub — mit Inhalt füllen" → **Archive/Delete-Kandidaten**
6. **Daily Notes:** 2026-02-XX.md → Episodic, bleiben
7. **System:** Vault-Rules, Dashboard, Sync → Meta, bleiben

### Identifizierte Patterns
- **Frontmatter Standard:** `type`, `status`, `last_verified`, `created` — gut etabliert
- **Bi-directional Links:** `[[#Heading]]` + Related sections → gut genutzt
- **Tags:** `#ainary`, `#claim`, `#ai_trust` → inkonsistent genutzt
- **Versionierung:** Fehlt komplett (außer in Dateinamen: `v2`, `v2-DE`)

---

## Phase 2: Gap-Analyse

### 2.1 Memory-INDEX.md Referenzen
**Was wird aus dem Vault referenziert?**
- `memory/people.md` → Kontakte (wahrscheinlich aus `30_People`)
- `memory/projects.md` → Aktive Projekte (aus `10_Projects`)
- `memory/decisions.md` → Decision Log (aus `50_Decisions`)
- `memory/patterns.md`, `corrections.md`, `lessons.md` → aus `60_Resources`
- Tages-Logs: `2026-MM-DD.md` → aus `02_Daily`

### 2.2 Findings API (localhost:8080)
**Was kommt aus Obsidian in die Execution Platform?**
- **15 Claims (C001-C015)** alle `obsidian_import`, tags `claim`, `ai_trust`
- **Used in:** AR-001, AR-009, AR-010, AR-011, AR-012 (AI Research Reports)
- **Cross-referenced:** 7/15 verifiziert, 8/15 nur single-source

**Beobachtung:** Claims werden importiert, aber leben in separaten Tiny Files. Ineffizient.

### 2.3 Nie Referenzierte Dateien (Candidates for Archive/Merge)
**Systematisch identifiziert via grep + backlink check:**
- `20_Areas/Business/SaaS-Market-2026.md` → **STUB**
- `20_Areas/Venture-Capital/Materials/Cover-Letter.md` → **STUB**
- `20_Areas/Family/` → **EMPTY**
- `60_Resources/Finance/` → 1 file, unreferenced
- Viele Dateien in `90_Archive` → per Definition tot

**Estimate:** ~60-80 Dateien sind stubs/unreferenced/redundant

### 2.4 Themen über 5+ Dateien verstreut (Consolidation Candidates)
1. **AI Research Claims:** 15 separate files (C001-C015) → **MERGE** zu `AI-Research-Claims-Ledger.md`
2. **Content Articles:**
   - Articles-DE: 4 files
   - Articles-EN: 5 files
   - Social: 10 files
   - Drafts: 9 files
   - Publish: 10 files
   → **CONSOLIDATE** zu `Content-Pipeline.md` mit Sections per Status
3. **VC Applications:** 
   - Applications/HOF-Capital + Materials + Networking → **MERGE** zu `VC-Job-Hunt-2026.md`
4. **Brand Resources:**
   - 10 files in `60_Resources/Brand/` → **MERGE** zu `Brand-System.md` mit TOC

---

## Phase 3: SOLL-Konzept

### 3.1 Neue Ordnerstruktur (5 Top-Level + 2 Meta)

```
System_OS/
├── DAILY/              ← 02_Daily (bleibt)
├── PROJECTS/           ← 10_Projects (bleibt, aber konsolidiert)
├── AREAS/              ← 20_Areas → 4 Sub-Ordner statt 7
│   ├── AI-Research/    ← bleibt, aber Claims gemerged
│   ├── Content/        ← Alle Content-Dateien, Status via TOC
│   ├── VC-Career/      ← Venture-Capital umbenannt
│   └── Consulting/     ← Freelance umbenannt
├── RESOURCES/          ← 60_Resources (stark konsolidiert)
│   ├── Brand-System.md         (merged: 10 files → 1)
│   ├── AI-Knowledge-Base.md    (merged: AI/, Knowledge/)
│   ├── Standards.md            (merged: Standards/)
│   └── Prompts.md              (merged: Prompts/)
├── PEOPLE/             ← 30_People (bleibt, leicht konsolidiert)
├── ARCHIVE/            ← 90_Archive (bleibt)
└── SYSTEM/             ← 99_System (bleibt, Meta-Ebene)
```

**Eliminiert:** 50_Decisions (→ merge zu MEMORY-INDEX), 70_Templates (→ SYSTEM/Templates.md), 00_Inbox (→ DAILY/Inbox.md)

---

### 3.2 Konsolidierte Dokumente (Beispiele)

#### **AI-Research-Claims-Ledger.md**
*Merged: C001-C015 (15 files → 1)*
```markdown
---
version: 1.0.0
updated: 2026-02-19
status: current
review_date: 2026-03-19
owner: mia
type: ledger
---
# AI Research Claims Ledger

## Table of Contents
- [[#C001 — 67% of security alerts ignored]]
- [[#C002 — 84% LLM overconfidence]]
- [[#C003 — Tool calling fails 3-15%]]
- ...

---

## C001 — 67% of security alerts are ignored by SOC analysts
**Source:** Vectra 2023 (n=2,000)
**Confidence:** HIGH (0.85)
**Used In:** [[AR-010]], [[AR-011]]
**Status:** current
**Last Verified:** 2026-02-15

[Original content...]

---

## C002 — 84% of LLM outputs are overconfident
[...]
```

**Vorteile:**
- 1 Datei statt 15 → einfacher zu navigieren
- TOC = schneller Überblick
- Version + Status = Staleness-Tracking
- Search funktioniert weiterhin (full-text)

---

#### **Content-Pipeline.md**
*Merged: Articles-DE, Articles-EN, Drafts, Social, Publish (38 files → 1)*
```markdown
---
version: 2.1.0
updated: 2026-02-19
status: current
review_date: 2026-02-26
owner: florian
type: pipeline
---
# Content Pipeline — All Content States

## Table of Contents
- [[#Queue (Ready to Post)]]
- [[#Drafts (In Progress)]]
- [[#Published (Live)]]
- [[#Social (Micro-Content)]]
- [[#Archive (Deprecated)]]

---

## Queue (Ready to Post)
### Sequoia AGI Article
**Status:** ready
**Channels:** Substack ✅ | LinkedIn ✅ | Twitter ✅ (7-tweet thread)
**Last Updated:** 2026-02-10
[...]

---

## Drafts (In Progress)
### How We Work Together
**Status:** draft
**Target Date:** 2026-02-25
**Word Count:** 1,200
[...]

---

## Published (Live)
### 100 Agents Evolution Experiment
**Published:** 2026-02-12
**URL:** https://florian.substack.com/100-agents
**Performance:** 450 views, 12 comments, 3 new subscribers
**Status:** evergreen
[...]
```

**Vorteile:**
- Gesamter Content-Lifecycle in 1 Datei
- TOC = Kanban-ähnliche Navigation
- Status-Tracking per Section
- Performance-Daten direkt dabei

---

#### **VC-Job-Hunt-2026.md**
*Merged: Applications/, Materials/, Networking/ (31 files → 1)*
```markdown
---
version: 1.3.0
updated: 2026-02-19
status: current
review_date: 2026-03-01
owner: florian
type: project
---
# VC Job Hunt 2026

## Table of Contents
- [[#Strategy & Timeline]]
- [[#Target Funds (A-List)]]
- [[#Applications (Active)]]
- [[#Networking (Warm Intros)]]
- [[#Materials (CV, Cover Letters)]]
- [[#Interview Prep]]

---

## Strategy & Timeline
**Phase 1 (Feb 1-28):** 15 applications, 10 networking calls
**Phase 2 (Mar 1-31):** Follow-ups, interviews
**Target:** 3 offers by April 1

---

## Target Funds (A-List)
### Glasswing Ventures
**Thesis Fit:** 95% (AI/ML Infrastructure)
**Contact:** Rudina Seseri (warm intro via Asepha)
**Status:** Application sent 2026-02-15
**Next:** Follow-up 2026-02-22
[...]

---

## Applications (Active)
### HOF Capital — Investment Analyst
**Applied:** 2026-02-14
**Materials Used:** [[#CV v3.2]], [[#Cover Letter — HOF]]
**Status:** Submitted, awaiting response
[...]

---

## Materials (CV, Cover Letters)
### CV v3.2
**Last Updated:** 2026-02-18
**Tailored For:** Early-stage VC roles
**Key Changes:** Added AgentTrust, Compound System projects
[Full CV text or link...]

### Cover Letter Template — Standard
[...]
```

**Vorteile:**
- Gesamte Job-Hunt in 1 Datei
- Chronologische + thematische Navigation via TOC
- Status aller Applications auf einen Blick
- Versionierung der Materials direkt integriert

---

### 3.3 TOC-Format (Obsidian-Compatible)

**Standard:**
```markdown
## Table of Contents
- [[#Section 1 Heading]]
- [[#Section 2 Heading]]
  - [[#Subsection 2.1]]
  - [[#Subsection 2.2]]
- [[#Section 3 Heading]]
```

**Funktioniert:**
- Obsidian rendert als klickbare Links
- Outline-Sidebar zeigt Struktur automatisch
- Search findet Headings + Content
- Mobile-App: TOC = Navigation

**Best Practice:**
- Max 3 Ebenen (H2, H3, H4)
- Emoji-Sections für visuelle Trennung (`## 📋 Queue`, `## ✅ Published`)
- Horizontale Linien (`---`) zwischen Major Sections

---

### 3.4 Versionierungs-Schema (Frontmatter)

**Pflicht-Felder:**
```yaml
---
version: 1.2.3          # Semantic Versioning (major.minor.patch)
updated: 2026-02-19     # ISO 8601 Date
status: current         # current | review | archive | dead
review_date: 2026-03-19 # Next Staleness-Check (30-90 days)
owner: florian          # florian | mia | system
type: ledger            # ledger | pipeline | project | resource | moc
---
```

**Optional:**
```yaml
confidence: 0.85        # Für Claims/Research
source: "McKinsey 2025" # Für Claims
used_in: [AR-001, ...]  # Backlinks
tags: [ai_trust, vc]    # Themen-Tags
```

**Version Bump Rules:**
- **Patch (1.0.0 → 1.0.1):** Typo-Fixes, kleine Updates, Status-Änderung
- **Minor (1.0.0 → 1.1.0):** Neue Section, >20% Content-Änderung
- **Major (1.0.0 → 2.0.0):** Restructure, Breaking Changes (TOC geändert)

**Automatische Checks (via Script):**
```bash
# Check all files for review_date < today
find . -name "*.md" -exec grep -l "review_date: $(date -v-1d +%Y-%m-%d)" {} \;
# → Output: Dateien die stale sind
```

---

### 3.5 Stale-Detection System

**Status-Lebenszyklus:**
```
current → review → archive → dead
   ↓         ↓         ↓
30-90d    90-180d   >180d (oder explizit killed)
```

**Rules:**
1. **current:** Aktiv genutzt, review_date = +30-90 Tage
2. **review:** review_date überschritten, manueller Check nötig
3. **archive:** Nicht mehr aktiv, aber historisch wertvoll
4. **dead:** Obsolet, kann gelöscht werden

**Automatisches Tagging (Obsidian Dataview Plugin):**
```dataview
TABLE status, review_date, updated
FROM ""
WHERE review_date < date(today)
SORT review_date ASC
```
→ Zeigt alle Dateien die Review brauchen

**Weekly Routine (Sonntag):**
1. Dataview Query ausführen
2. Alle `review`-Status Dateien durchgehen:
   - Noch relevant? → `updated` + `review_date` bump + `status: current`
   - Historisch wertvoll? → `status: archive`
   - Obsolet? → `status: dead` + `killed_by: "Reason"`
3. Alle `dead`-Status Dateien → Move to `90_Archive/Dead/`

---

### 3.6 Migration-Plan (Reversibel, Schrittweise)

**Prinzipien:**
1. **Kein Datenverlust:** Altes bleibt in `90_Archive/Pre-Restructure-2026-02-19/`
2. **Git Commits:** Jeder Schritt = 1 Commit
3. **Test:** 1 Ordner zuerst (Content/), validieren, dann Rest
4. **Rollback:** Git Reset möglich innerhalb 7 Tage

---

#### **Step 1: Backup (CRITICAL)**
```bash
# Full Vault Snapshot
cd ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/System_OS
cp -R . ~/Backups/Obsidian-Pre-Restructure-2026-02-19/

# Git Init (falls noch nicht)
git init
git add .
git commit -m "Pre-Restructure Snapshot 2026-02-19"
```

---

#### **Step 2: Pilot — Content/ Consolidation**
*Test mit 1 Ordner, validate, iterate*

**Actions:**
1. Create `AREAS/Content/Content-Pipeline.md`
2. Copy content from:
   - `Articles-EN/article-1-100-agents.md` → Section `## Published > ### 100 Agents`
   - `Drafts/post-specialist-ai-wins.md` → Section `## Drafts > ### Specialist AI`
   - `Social/linkedin-specialist-ai.md` → Section `## Social > LinkedIn > ### Specialist AI`
3. Add Frontmatter (version: 1.0.0, status: current, review_date: +30d)
4. Update all `[[article-1-100-agents]]` links → `[[Content-Pipeline#100 Agents]]`
5. Move originals → `90_Archive/Pre-Restructure-2026-02-19/Content/`
6. Git commit: "Consolidate Content Articles (Pilot)"

**Validation:**
- [ ] All links still work?
- [ ] Search finds content?
- [ ] TOC navigates correctly?
- [ ] Obsidian Graph shows connections?
- [ ] File count reduced? (66 → ~1-3)

**Decision Point:**
- ✅ Works → Proceed to Step 3
- ❌ Issues → Rollback (git reset), adjust approach

---

#### **Step 3: AI-Research Claims Consolidation**
```bash
# Same pattern as Content/
1. Create AREAS/AI-Research/AI-Research-Claims-Ledger.md
2. Merge Claims/C001.md - C015.md → Sections with [[#C001]] anchors
3. Update backlinks in AR-001, AR-009, etc.
4. Move originals to Archive
5. Git commit
```

---

#### **Step 4: VC-Career Consolidation**
```bash
1. Create AREAS/VC-Career/VC-Job-Hunt-2026.md
2. Merge Applications/, Materials/, Networking/ → Sections
3. Update backlinks
4. Archive originals
5. Git commit
```

---

#### **Step 5: Resources Consolidation**
```bash
1. RESOURCES/Brand-System.md ← merge 10 Brand/ files
2. RESOURCES/AI-Knowledge-Base.md ← merge AI/, Knowledge/
3. RESOURCES/Standards.md ← merge Standards/
4. Archive originals
5. Git commit
```

---

#### **Step 6: Folder Restructure**
```bash
# Rename Top-Level
mv 02_Daily DAILY
mv 10_Projects PROJECTS
mv 20_Areas AREAS
mv 30_People PEOPLE
mv 60_Resources RESOURCES
mv 90_Archive ARCHIVE
mv 99_System SYSTEM

# Eliminate
# - 00_Inbox → merge to DAILY/Inbox.md
# - 50_Decisions → merge to SYSTEM/Decisions-Log.md
# - 70_Templates → merge to SYSTEM/Templates.md

git commit -m "Restructure: 10 folders → 7"
```

---

#### **Step 7: Frontmatter Upgrade**
```bash
# Add version, status, review_date to all consolidated docs
# Script (Python/Bash) to auto-inject if missing:
for file in AREAS/**/*.md RESOURCES/*.md; do
  if ! grep -q "^version:" "$file"; then
    # Prepend frontmatter
    ...
  fi
done

git commit -m "Add versioning frontmatter"
```

---

#### **Step 8: Stale-Detection Setup**
```bash
# Create Dataview Query in SYSTEM/Stale-Check.md
# Setup Weekly Reminder (Calendar/Obsidian Reminder Plugin)
# Document Process in SYSTEM/Vault-Maintenance.md

git commit -m "Setup Stale-Detection"
```

---

#### **Step 9: Link Validation**
```bash
# Run Obsidian "Check for Broken Links" Plugin
# Fix all broken [[links]]
# Validate Graph View (no orphans except Archive)

git commit -m "Fix broken links post-restructure"
```

---

#### **Step 10: Documentation + Handoff**
```bash
# Update SYSTEM/Vault-Guide.md with new structure
# Create CHANGELOG.md documenting all changes
# Brief Florian on new system

git commit -m "Restructure complete — Documentation updated"
git tag v2.0.0-restructure
```

---

### 3.7 Rollback-Strategie

**Wenn etwas schief geht:**
```bash
# Option 1: Git Reset (innerhalb 7 Tage)
git log --oneline  # Find pre-restructure commit
git reset --hard <commit-hash>

# Option 2: Restore from Backup
rm -rf ~/Library/.../System_OS/*
cp -R ~/Backups/Obsidian-Pre-Restructure-2026-02-19/* ~/Library/.../System_OS/

# Option 3: Partial Rollback (1 Ordner)
git revert <commit-hash-of-that-folder>
```

**Safe Mode:**
- Teste auf COPY des Vaults zuerst (separate Obsidian Vault "System_OS_Test")
- Florian approval nach jedem Major Step (2, 5, 6)

---

## Erwartete Ergebnisse

### Quantitative Verbesserungen
| Metrik | Vorher | Nachher | Δ |
|--------|--------|---------|---|
| Anzahl Dateien | 461 | ~120 | -74% |
| Dateien <50 Zeilen | 178 (40%) | ~20 (17%) | -89% |
| Top-Level Ordner | 10 | 7 | -30% |
| Sub-Ordner (20_Areas) | 25 | ~8 | -68% |
| Durchschnitt Zeilen/Datei | 179 | ~450 | +151% |
| Stubs/Dead Files | ~80 | 0 | -100% |

### Qualitative Verbesserungen
- ✅ **Navigation:** TOC = instant jump zu Sub-Themen
- ✅ **Context:** Alles zu 1 Thema in 1 Datei (nicht 15 Tabs offen)
- ✅ **Staleness:** Automatische Detection via `review_date`
- ✅ **Versionierung:** Änderungen trackbar via Frontmatter
- ✅ **Ownership:** Jede Datei hat `owner` (florian/mia/system)
- ✅ **Search:** Bleibt genauso gut (full-text indexing)
- ✅ **Links:** [[#Anchors]] funktionieren wie vorher
- ✅ **Mobile:** Längere Docs = besseres Scrollen (vs. App-Switching)

### Risiken & Mitigation
| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Broken Links | Mittel | Hoch | Step 9: Link Validation + Fix |
| Datenverlust | Niedrig | Kritisch | Step 1: Backup + Git |
| Zu lange Dateien (>2000 lines) | Niedrig | Mittel | Split if >1500 lines |
| Obsidian Performance | Niedrig | Niedrig | Moderne Obsidian handled 10k+ lines |
| Florian mag es nicht | Mittel | Hoch | Pilot first (Step 2), iterate |

---

## Open Questions für Florian

1. **Pilot Scope:** Nur Content/ zuerst, oder direkt all-in?
2. **Review Frequency:** 30 Tage (aggressiv) oder 90 Tage (relaxed)?
3. **Archive Policy:** `dead`-Status Dateien löschen oder in `90_Archive/Dead/` behalten?
4. **TOC Style:** Emoji-Sections (📋, ✅, 🚀) oder plain text?
5. **Obsidian Plugins:** Dataview für Stale-Check aktivieren? (braucht Plugin)
6. **Git Hosting:** Vault auf GitHub (private repo) für bessere Version Control?

---

## Nächste Schritte (wenn GO)

**Woche 1 (Feb 19-25):**
- [ ] Florian Approval einholen
- [ ] Backup erstellen (Step 1)
- [ ] Pilot: Content/ Consolidation (Step 2)
- [ ] Validation + Iteration

**Woche 2 (Feb 26 - Mar 4):**
- [ ] AI-Research Claims (Step 3)
- [ ] VC-Career (Step 4)
- [ ] Resources (Step 5)

**Woche 3 (Mar 5-11):**
- [ ] Folder Restructure (Step 6)
- [ ] Frontmatter Upgrade (Step 7)
- [ ] Stale-Detection Setup (Step 8)

**Woche 4 (Mar 12-18):**
- [ ] Link Validation (Step 9)
- [ ] Documentation (Step 10)
- [ ] Handoff + Training

**Total Effort:** ~12-16 Stunden (verteilt über 4 Wochen)

---

## Anhang: Beispiel-Migrations-Script

```bash
#!/bin/bash
# migrate-content.sh — Consolidate Content/ folder

VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"
BACKUP="$HOME/Backups/Obsidian-Pre-Restructure-2026-02-19"
TARGET="$VAULT/AREAS/Content/Content-Pipeline.md"

# 1. Backup
echo "Creating backup..."
cp -R "$VAULT" "$BACKUP"
cd "$VAULT" || exit

# 2. Create consolidated file
cat > "$TARGET" <<'EOF'
---
version: 1.0.0
updated: 2026-02-19
status: current
review_date: 2026-03-19
owner: florian
type: pipeline
---
# Content Pipeline

## Table of Contents
- [[#Published]]
- [[#Drafts]]
- [[#Social]]

---

EOF

# 3. Merge files (example: Articles-EN)
for file in "$VAULT/20_Areas/Content/Articles-EN"/*.md; do
  filename=$(basename "$file" .md)
  echo "## Published" >> "$TARGET"
  echo "### $filename" >> "$TARGET"
  echo "" >> "$TARGET"
  cat "$file" >> "$TARGET"
  echo "" >> "$TARGET"
  echo "---" >> "$TARGET"
  echo "" >> "$TARGET"
done

# 4. Archive originals
mkdir -p "$VAULT/90_Archive/Pre-Restructure-2026-02-19/Content"
mv "$VAULT/20_Areas/Content/Articles-EN" "$VAULT/90_Archive/Pre-Restructure-2026-02-19/Content/"

# 5. Git commit
git add .
git commit -m "Consolidate Content/Articles-EN → Content-Pipeline.md"

echo "✅ Migration complete. Review $TARGET"
```

---

**Ende des Konzepts.**

*Nächster Schritt: Florians Approval + Pilot (Content/ Consolidation)*

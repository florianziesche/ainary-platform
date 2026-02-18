# VAULT-ARCHITECTURE.md — Obsidian Knowledge System Design
*Created: 2026-02-09 | Author: Mia*

## Design-Philosophie

Basiert auf Research zu LYT (Nick Milo), Pyramid Structure (Dataview), PARA (Tiago Forte), und Zettelkasten (Luhmann). Optimiert für:

1. **AI-Navigation** — Mia muss schnell das richtige Wissen finden
2. **Human Discovery** — Florian soll über Graph View neue Verbindungen entdecken
3. **Wachstum** — System muss von 270 auf 2000+ Dateien skalieren

### Drei Prinzipien

1. **Links > Folders > Tags** — Links mit Kontext sind wertvoller als Ordner. Ordner gruppieren nur grob.
2. **YAML Frontmatter = Database Schema** — Jede Datei hat strukturierte Metadaten. Ermöglicht Queries.
3. **MOCs als Navigation** — Maps of Content statt tiefer Folder-Hierarchien.

---

## Ordnerstruktur (NEU — eindeutige Nummern)

```
System_OS/
├── 00-Cockpit/         — Dashboards, Weekly Reviews, aktuelle Lage
├── 01-Inbox/           — Unverarbeitetes. Wird wöchentlich geleert.
├── 02-Daily/           — Tägliche Notizen
├── 10-Projects/        — Aktive Projekte (Ainary, CNC, VC-Career, Content)
├── 20-Knowledge/       — Evergreen Wissen (AI, VC, CNC, Business)
├── 30-People/          — Alle Personen (Family, VCs, LPs, Kontakte)
├── 40-Content/         — Content Pipeline, Drafts, Published
├── 50-Standards/       — Qualitätsstandards, Checklisten, Protokolle
├── 60-Prompts/         — Prompt Library
├── 70-Resources/       — Templates, Tools, Referenzmaterial
├── 80-Archive/         — Abgeschlossenes
├── 90-MIA/             — Mias Reflexionen, Learnings, Charakter
├── 99-System/          — Vault-Config, Meta, Guides
```

### Was sich ändert:
| Alt | Neu | Grund |
|-----|-----|-------|
| 10-Pipeline/ | → 10-Projects/ (merge) | Gleiche Nummer, gleicher Zweck |
| 20-Product/ | → 10-Projects/ (merge) | Produktinfos gehören zu Projekten |
| 30-Content/ | → 40-Content/ | Eigene Nummer |
| 40-Prompts/ | → 60-Prompts/ | Eigene Nummer |
| 50-Tools/ | → 70-Resources/ (merge) | Tools + Templates = Resources |
| 60-Failures/ | → 90-MIA/Failures/ | Mias Lernprozess |
| 60-Lessons/ | → 20-Knowledge/Lessons/ | Wissen = Knowledge |
| 70-Templates/ | → 70-Resources/Templates/ | Teil von Resources |
| MIA/ | → 90-MIA/ | Nummeriert |
| Writing/ | → 40-Content/ | Content = Content |

---

## YAML Frontmatter Schema (Database Layer)

Jede .md Datei bekommt standardisierten Frontmatter:

### Minimales Schema (ALLE Dateien)
```yaml
---
type: project | knowledge | person | standard | prompt | template | daily | moc | meta
status: active | draft | review | archived | evergreen
created: 2026-02-09
author: Mia | Florian | Mia + Florian | unknown
---
```

### Erweitertes Schema nach Type

**project:**
```yaml
---
type: project
status: active
priority: 1-5
domain: [vc, cnc, content, consulting, fund]
created: 2026-02-09
author: Florian
---
```

**knowledge:**
```yaml
---
type: knowledge
status: evergreen
domain: [ai, vc, cnc, business, kommunal]
confidence: high | medium | low
source: research | experience | external
created: 2026-02-09
author: Mia
---
```

**person:**
```yaml
---
type: person
relation: family | vc | lp | contact | recruiter | client
company: "HOF Capital"
location: "NYC"
last-contact: 2026-02-05
created: 2026-02-09
author: Florian
---
```

**standard:**
```yaml
---
type: standard
applies-to: [all, content, research, visual, code]
created: 2026-02-09
author: Mia
---
```

---

## MOC (Map of Content) Struktur

Jeder Hauptordner bekommt eine `_MOC.md` Datei die als Navigation dient:

```
00-Cockpit/_MOC.md     → Dashboard der Dashboards
10-Projects/_MOC.md    → Alle aktiven Projekte mit Status
20-Knowledge/_MOC.md   → Wissenslandkarte nach Domain
30-People/_MOC.md      → Kontakte nach Relation
40-Content/_MOC.md     → Content Pipeline
50-Standards/_MOC.md   → Alle Standards
```

### MOC Template:
```markdown
---
type: moc
status: evergreen
created: 2026-02-09
author: Mia
---
# [Domain] — Map of Content

## Active
- [[File1]] — One-line description
- [[File2]] — One-line description

## By Topic
### Subtopic A
- [[File3]] — Description

### Subtopic B
- [[File4]] — Description
```

---

## Linking-Regeln

### 1. Wikilinks: NUR Dateiname
```
✅ [[HOF-Capital]]
❌ [[Fund-Research/HOF-Capital]]
```

### 2. Typed Links (Related Section)
```markdown
## Related
- **↑ Herkunft:** [[Source]] — Woher kam diese Idee
- **↓ Output:** [[Result]] — Was wurde daraus
- **↔ Pattern:** [[Similar]] — Gleiches Muster, anderer Kontext
```

### 3. Frontmatter Links (für Queries)
```yaml
parent: "[[_MOC]]"
related: ["[[File1]]", "[[File2]]"]
```

---

## Implementierungs-Plan

### Phase 1: Ordner-Restrukturierung
1. Neue Ordner erstellen (02-Daily, 40-Content, 60-Prompts, 70-Resources, 90-MIA)
2. Dateien verschieben
3. Alte leere Ordner entfernen
4. 10-Pipeline/ und 20-Product/ in 10-Projects/ mergen

### Phase 2: YAML Frontmatter
1. Alle 272 Dateien bekommen standardisierten Frontmatter
2. Type + Status + Created + Author für jede Datei
3. Domain-Tags für Knowledge und Project Dateien

### Phase 3: MOCs erstellen
1. _MOC.md für jeden Hauptordner
2. Eine zentrale Home-MOC als Einstiegspunkt
3. Cross-links zwischen MOCs

### Phase 4: Validierung
1. QA-Script laufen lassen
2. Keine Duplikate, keine broken Links
3. Jede Datei hat Frontmatter
4. Jede Datei hat mindestens 1 eingehenden Link

---

## Changelog
- 2026-02-09: Created (Mia) — Research-basiertes Design für Vault-Restrukturierung

---
tier: CORE
expires: none
---
# MEMORY INDEX — Mias Navigationsebene
*Wird IMMER geladen. Max 500 Tokens. Verweist auf Topic Files.*
*Updated: 2026-02-20 (post-simplification)*

## Struktur (70_Mia/ = workspace/memory/ via Symlink)

```
70_Mia/
├── people.md              ← Kontakte + Kontext
├── projects.md            ← Aktive Projekte + Status
├── decisions.md           ← Entscheidungen mit Datum + Warum
├── connections.md         ← Wissens-Verbindungen
├── verified-truths.md     ← Bestätigte Fakten
├── tech.md                ← Pfade, Tools, CLI-Commands
├── trust-score.md         ← Agent Trust Scores
├── knowledge/             ← Semantisches Wissen (20 files)
│   ├── _index.md          ← Knowledge Navigation
│   ├── agent-trust-governance.md
│   ├── contacts.md
│   ├── decisions.md
│   ├── engineering-standards.md
│   └── ... (16 weitere)
└── [ARCHIVED in 90_Archive/]
    ├── daily/             → 90_Archive/daily-notes/
    ├── briefs/            → 90_Archive/briefs/
    ├── triage/            → 90_Archive/triage/
    ├── research/          → 90_Archive/mia-research/
    ├── rules/             → 90_Archive/mia-rules/
    ├── semantic/          → 90_Archive/mia-semantic/
    ├── state/             → 90_Archive/mia-state/
    └── wins/              → 90_Archive/wins/
```

## Laden-Reihenfolge bei Session-Start
1. IMMER: Diesen Index + SOUL.md + IDENTITY.md
2. IMMER: `people.md` + `projects.md`
3. BEI BEDARF: `decisions.md`, `tech.md`, `verified-truths.md`
4. BEI BEDARF: `connections.md`, `trust-score.md`
5. BEI BEDARF: `knowledge/*` per memory_search (semantisches Wissen)
6. ARCHIVIERT: Daily notes, briefs, triage → in 90_Archive/ (nur bei explizitem Bedarf)

## Quick Reference
| Frage | Datei |
|-------|-------|
| Wer ist X? | `people.md` oder `knowledge/contacts.md` |
| Was läuft? | `projects.md` |
| Was wurde entschieden? | `decisions.md` |
| Was wissen wir sicher? | `verified-truths.md` |
| Was verbindet sich? | `connections.md` |
| Semantic Memory? | `knowledge/_index.md` |
| Trust Scores? | `trust-score.md` |
| Tech Stack? | `tech.md` |
| Archiviert? | Vault `90_Archive/` |

## Vault Simplification (2026-02-20)
- **VOR:** 680 Dateien
- **NACH:** 60 aktive Dateien
- **ARCHIVIERT:** 620 Dateien in `90_Archive/`
- **STRATEGIE:** Nur aktive Files im Vault, Rest archiviert aber verfügbar

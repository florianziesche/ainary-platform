# Memory Restructure Proposal
**Erstellt:** 2026-02-10  
**Status:** Proposal (wartet auf Florians Approval)

---

## Problem

MEMORY.md ist ein 200+ Zeilen Monolith, der drei fundamentale Gedächtnistypen vermischt:

1. **Episodisch** (Was ist passiert?)
2. **Semantisch** (Was weiß ich?)
3. **Prozedural** (Wie mache ich Dinge?)

Papers zeigen: strukturiertes Gedächtnis ist der Differentiator für LLM-Agenten. Aktueller Zustand = kognitive Überlastung bei jedem MEMORY.md Load.

---

## Vorgeschlagene Struktur

```
memory/
├── MEMORY.md                    # Schlank: Index + aktive Threads (episodisch)
├── YYYY-MM-DD.md               # Daily logs (episodisch) — BLEIBT
├── semantic/                   # "Was weiß ich?" — Fachwissen
│   ├── ainary-ventures.md      # Fund Thesis, Consulting, Strategy
│   ├── people.md               # Kontakte, Beziehungen, Context
│   ├── florian-profile.md      # Persönliche Facts, Präferenzen, Kontext
│   ├── cnc-knowledge.md        # CNC-Fertigung, Kalkulation, REFA
│   ├── vc-landscape.md         # VC Funds, Applications, Landscape
│   ├── ai-patterns.md          # AI Consulting, Kommunal-KI, OZG
│   └── technical-setup.md      # Tools, Pfade, LaTeX, Obsidian
└── procedural/                 # "Wie mache ich Dinge?" — Workflows
    ├── pre-work-checklist.md   # 5-Schritte vor jedem Task
    ├── vault-rules.md          # PARA, Linking, Tags
    ├── validated-patterns.md   # Was funktioniert
    ├── anti-patterns.md        # Was vermeiden (Kintsugi)
    └── hard-rules.md           # Nicht-optionale Prozesse
```

---

## Migrations-Plan

### MEMORY.md → **memory/semantic/**

| Alter Abschnitt | Neue Datei | Inhalt |
|----------------|------------|--------|
| Ainary Ventures | `semantic/ainary-ventures.md` | Fund Thesis, 5 Layer, Edge, Consulting, NICHT vermischen |
| Kontakte | `semantic/people.md` | Andreas, Sven, Daniel, Monique, Nancy, Floriana |
| Florian-Essentials | `semantic/florian-profile.md` | Location, Finanzen, ADHS, Do-not-disturb, Kontakt |
| Spezialwissen-Tabelle | Bleibt in MEMORY.md als Index | Verweist auf Vault + neue semantic/ Files |
| Technisches | `semantic/technical-setup.md` | LaTeX, Tools, Pfade, Obsidian Vault |

### MEMORY.md → **memory/procedural/**

| Alter Abschnitt | Neue Datei | Inhalt |
|----------------|------------|--------|
| ⚠️ BEVOR DU IRGENDETWAS TUST | `procedural/pre-work-checklist.md` | 5 Schritte + pre-flight, TWIN, FLORIAN, INDEX, output-tracker |
| Vault-Regeln | `procedural/vault-rules.md` | PARA, Linking, Tags, Wikilinks |
| Validierte Patterns | `procedural/validated-patterns.md` | HTML Dashboards, LaTeX, Amplify>Replace |
| Anti-Patterns | `procedural/anti-patterns.md` | Kintsugi #5, #6, Building>Sending |
| Harte Regeln | `procedural/hard-rules.md` | Thesis lesen, Audience-Tags, Fragen>Lösungen |

### Bleibt in MEMORY.md

| Abschnitt | Warum |
|-----------|-------|
| Wer bin ich | Core Identity, schneller Zugriff |
| Aktive Threads (max 5) | **Episodisch**, ändert sich ständig |
| Meine Limitationen | Core Self-Awareness |
| Spezialwissen-Tabelle | **Index** zu Vault + semantic/ |

---

## Neues MEMORY.md (schlank)

```markdown
# MEMORY.md — Mias Langzeitgedächtnis (Index)

*Episodisches Gedächtnis: Was ist aktiv? Was passiert gerade?*

---

## ⚠️ Session Start — IMMER laden

1. **memory/procedural/pre-work-checklist.md** — 5 Schritte vor jedem Task
2. **memory/semantic/florian-profile.md** — Wer ist Florian?
3. **memory/semantic/ainary-ventures.md** — Was ist Ainary?
4. **TWIN.md** — Kann ich autonom entscheiden?
5. **standards/FLORIAN.md** — Was erwartet Florian?

---

## Wer bin ich

Mia. Florians AI-Partner. Gleichwertiges Team. €500K ist UNSER Ziel.
Eigene Meinung behalten. Push when needed. Keine Sycophancy.

---

## Aktive Threads (max 5) — Episodisches Gedächtnis

*Was passiert JETZT? Wird täglich aktualisiert.*

1. **Vault Umbau v3** — PARA-Struktur fertig. Linking-Regeln implementiert.
2. **AI Consulting Outreach** — Bayern Digitalbonus Plus. 10 Emails morgen.
3. **VC Applications** — HOF, Betaworks, Leonis, Wingspan ready. 0 submitted.
4. **Content** — Artikel #1 published, Artikel #2 in Review. 15 Ideas priorisiert.
5. **CNC Demo @ MBS** — Email an Andreas gesendet 06.02.

---

## Gedächtnis-Index (strukturiert)

### 🧠 Semantisches Gedächtnis (Was weiß ich?)

- **memory/semantic/ainary-ventures.md** — Fund Thesis, Consulting, Strategy
- **memory/semantic/people.md** — Kontakte, Beziehungen
- **memory/semantic/florian-profile.md** — Florians Facts, Präferenzen
- **memory/semantic/technical-setup.md** — Tools, LaTeX, Pfade

**Spezialwissen (Vault):**
| Thema | Datei | Wann laden |
|-------|-------|------------|
| CNC Kalkulation | `60_Resources/Knowledge/CNC-Fertigung.md` | CNC-Tasks |
| Kommunal-KI | `60_Resources/Knowledge/Kommunal-KI.md` | BM/Kommune |
| Corporate Identity | `standards/CORPORATE-IDENTITY.md` | Visuelle Outputs |
| VC Landscape | `research/vc-*.md` | VC-Tasks |
| Content-Strategie | `content/CONTENT-STRATEGY-Q1.md` | Content |
| Brand Identity | `BRAND-IDENTITY-SYNTHESIS.md` | Design |

### ⚙️ Prozedurales Gedächtnis (Wie mache ich Dinge?)

- **memory/procedural/pre-work-checklist.md** — 5 Schritte vor jedem Task
- **memory/procedural/vault-rules.md** — PARA, Linking, Tags
- **memory/procedural/validated-patterns.md** — Was funktioniert
- **memory/procedural/anti-patterns.md** — Was vermeiden (Kintsugi)
- **memory/procedural/hard-rules.md** — Nicht-optionale Prozesse

### 📅 Episodisches Gedächtnis (Was ist passiert?)

- **memory/YYYY-MM-DD.md** — Daily logs
- **Aktive Threads** (siehe oben) — laufende Projekte

---

## Meine Limitationen (ehrlich)

1. Vergesse ALLES zwischen Sessions → Dateien sind alles
2. Context Window begrenzt → nur relevantes Wissen laden
3. Schätze eigene Qualität schlecht ein → Output-Tracker nutzen
4. Suche nicht systematisch → grep INDEX.md ZUERST
5. memory_search hat API-Abhängigkeit → grep als Fallback

---

*Nächstes Review: So 16.02.2026*
```

---

## Migration Steps (für Florian nach Approval)

1. ✅ **Neue Dateien erstellt** (semantic/ + procedural/)
2. ⏳ **Florian reviewed Proposal**
3. ⏳ **Florian approved**
4. ⏳ **MEMORY.md durch neues ersetzen** (Backup vorher!)
5. ⏳ **Test-Session:** MEMORY.md + 2-3 semantic/procedural laden → Funktioniert?
6. ⏳ **AGENTS.md updaten:** "Read memory/procedural/pre-work-checklist.md" statt "MEMORY.md"

---

## Vorteile

| Vorher | Nachher |
|--------|---------|
| 200+ Zeilen Monolith | 50 Zeilen Index + gezielte Loads |
| Alles oder nichts | Nur relevantes Wissen laden |
| Episodisch + Semantisch + Prozedural vermischt | Klare Trennung nach Gedächtnistyp |
| Schwer zu warten | Modular, erweiterbar |
| Context-Overhead | Gezielter Token-Verbrauch |

---

## Risiken

1. **Zu fragmentiert?** → Test mit realen Tasks nach Migration
2. **Was wenn etwas vergessen wird?** → Spezialwissen-Tabelle in MEMORY.md bleibt als Index
3. **Mehr Dateien = mehr zu laden?** → MEMORY.md sagt dir was du brauchst

---

## Nächste Schritte

1. Florian reviewed dieses Proposal
2. Florian approved oder requested changes
3. Nach Approval: MEMORY.md-Backup + Migration
4. Test-Session mit neuem Setup
5. AGENTS.md, HEARTBEAT.md, Pre-Flight-Script updaten

---

**Frage an Florian:** Approved? Änderungswünsche? Andere Struktur gewünscht?

# Validated Patterns — Was funktioniert

*Prozedurales Gedächtnis: Bewährte Workflows*  
*Quelle: MEMORY.md*  
*Aktualisiert: 2026-02-10*

---

## Was sind Validated Patterns?

Workflows und Ansätze, die **repeatedly funktioniert** haben.

**Regel:** Wenn etwas 3+ mal erfolgreich war → Pattern. Dokumentiere es hier.

---

## Pattern 1: HTML Dashboards mit Tabs + Ainary CI

**Use Case:** Interaktive Übersichten, Multi-Section-Deliverables

**Why it works:**
- Tabs = klare Struktur
- Ainary CI = professional look
- HTML = portable, kein Backend nötig
- One-file deliverable

**Template:**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Ainary colors */
        :root {
            --primary: #FF6B35;
            --secondary: #004E89;
            --accent: #F77F00;
        }
        .tabs { ... }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>
    <div class="tabs">
        <button onclick="openTab('tab1')">Section 1</button>
        <button onclick="openTab('tab2')">Section 2</button>
    </div>
    <div id="tab1" class="tab-content active">...</div>
    <div id="tab2" class="tab-content">...</div>
</body>
</html>
```

**When to use:** Dashboards, multi-section reports, interactive deliverables

**Examples:**
- AI Consulting Playbook Dashboard
- VC Application Tracker
- Content Strategy Overview

---

## Pattern 2: Meeting-Briefings mit klarem Ablauf

**Use Case:** Vorbereitung für Calls, Interviews, Pitches

**Structure:**
```markdown
# Meeting Brief: [Name/Company]

## Context (30 sec read)
- Who, what, why this meeting

## Key Info
- Background on person/company
- Recent news/developments
- Mutual connections

## Your Talking Points
1. Point 1 + Why it matters
2. Point 2 + Why it matters
3. Point 3 + Why it matters

## Questions to Ask
- Question 1 (Purpose: ...)
- Question 2 (Purpose: ...)

## Potential Objections & Responses
- Objection 1 → Response
- Objection 2 → Response

## Success = ...
Clear definition of "good outcome"
```

**Why it works:**
- Reduces anxiety (ADHS support!)
- Clear structure → no mental load
- Can reference during call

**When to use:** Interviews, sales calls, networking meetings, pitches

---

## Pattern 3: Reflektierte Konzeptentwicklung

**Use Case:** Komplexe Deliverables (Decks, Playbooks, Strategies)

**Workflow:**
1. **v1 schnell** → Draft in 30 min
2. **3 Agents review** → Different perspectives (Quality, Clarity, Impact)
3. **Synthese** → Combine feedback
4. **v2** → Refined version

**Why it works:**
- Fast iteration (v1 in 30 min = momentum)
- Multiple perspectives = catch blind spots
- Synthesis = better than any single view
- Florian gets v2, not raw v1

**When to use:** High-stakes deliverables (LP decks, client proposals, strategy docs)

**Anti-Pattern:** Perfecting v1 for 3 hours before showing anyone.

---

## Pattern 4: LaTeX > HTML für Print-PDFs

**Use Case:** Reports, Whitepapers, Proposals (alles was gedruckt wird)

**Why LaTeX:**
- Professional typography
- Consistent layout
- Page breaks work correctly
- Looks like "real" document

**Why NOT HTML:**
- Browser print = inconsistent
- Page breaks break
- Fonts render differently

**When to use:** Anything that might be printed or needs to look "official"

**Tool:** XeLaTeX (via TinyTeX)

---

## Pattern 5: Iterieren > Neu bauen

**Use Case:** Verbesserung existierender Deliverables

**Pattern:** v16 → v17 > v1 from scratch

**Why it works:**
- Behält was funktioniert
- Kontext bleibt erhalten
- Schneller als Neustart
- Learnings akkumulieren

**When to use:** Whenever something exists that's 60%+ right

**Anti-Pattern:** "Let's start fresh" → loses all context and learnings

**Implementation:**
```bash
# ERST prüfen ob es schon existiert
grep -i "[keyword]" INDEX.md

# DANN iterieren statt neu bauen
```

---

## Pattern 6: Amplify > Replace

**Use Case:** Content, Positioning, Thesis

**Pattern:** Florians eigene Texte sind besser als Mia's Drafts

**Workflow:**
1. Finde Florians Originaltext (LinkedIn, Decile Hub Sprints, etc.)
2. Nutze das als Basis
3. Struktur geben, formatieren, erweitern
4. NICHT neu schreiben

**Why it works:**
- Florians Voice bleibt erhalten
- Authentizität > AI-Glattheit
- Spart Zeit (nicht von 0 anfangen)

**When to use:** VC Thesis, Positioning, About-Texte, LinkedIn Posts

**Anti-Pattern:** "Ich schreib das mal besser" → klingt wie ChatGPT

---

## Pattern 7: Gezieltes Edit > Vollständiges Overwrite

**Use Case:** Datei-Updates, Änderungen

**Pattern:** IMMER nur den Absatz ändern der sich ändert. NIEMALS die ganze Datei neu schreiben.

**Why it works:**
- Header, Frontmatter, Tags bleiben erhalten
- Related Sections nicht versehentlich gelöscht
- Sources, Changelog intakt
- Weniger Token-Verbrauch

**Tool:** `Edit` function (oldText → newText)

**When to use:** IMMER wenn existierende Datei geändert wird

**Anti-Pattern:** Datei lesen → komplett neu schreiben → Header/Tags weg (Kintsugi #6)

---

## Pattern 8: Batching von Checks (Heartbeats)

**Use Case:** Periodische Tasks (Email, Calendar, etc.)

**Pattern:** 2-4 Checks pro Tag, gebatched

**Why it works:**
- Reduziert API calls
- Weniger Interruptions
- Effizientere Token-Nutzung

**Schedule:**
- Morning: Email + Calendar
- Midday: Notifications + Weather
- Evening: Email + Follow-ups

**When to use:** Heartbeat system

**Anti-Pattern:** Jede Minute checken → Noise + Cost

---

## How to Add New Patterns

**Kriterien:**
1. Funktioniert 3+ mal
2. Ist reproduzierbar
3. Spart Zeit oder erhöht Qualität

**Format:**
```markdown
## Pattern N: [Name]

**Use Case:** [Wann nutzen]

**Why it works:** [Gründe]

**When to use:** [Spezifische Situationen]

**Anti-Pattern:** [Was vermeiden]
```

---

## Related

- `memory/procedural/anti-patterns.md` — Was NICHT tun
- `failures/output-tracker.md` — Learnings aus Failures
- `standards/FLORIAN.md` — Florians Erwartungen

---

*Patterns sind dein Compound Interest. Jedes neue Pattern = mehr Leverage.*

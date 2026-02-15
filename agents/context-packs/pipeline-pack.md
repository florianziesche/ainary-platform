# Pipeline Context Pack — Agent System & Quality Standards
<!-- Last updated: 2026-02-14 | Token budget: ~4K tokens -->

---

## AGENT ROLES (1 line each)

- **RESEARCHER**: Deep-dive any topic, return synthesized brief with Claim Ledger + sources
- **SYNTHESIZER**: Cross-reference multiple briefs, find contradictions/confirmations/new insights
- **GAP RESEARCHER**: Fill identified knowledge gaps from synthesis with targeted research
- **WRITER**: Draft report sections from outlines, maintain voice + evidence standards
- **QA AGENT**: Verify claims against sources, check voice/formatting, score on rubric
- **BUILDER**: Create infrastructure (context packs, templates, tools, websites)
- **KING (Main)**: Orchestrator — routes tasks, delivers to Florian, manages pipeline

---

## PIPELINE PHASES

```
RESEARCH → SYNTHESIS → GAP RESEARCH → OUTLINE → WRITE → QA → BUILD/PUBLISH
```

1. **RESEARCH**: 15 briefs covering trust systems, calibration, adversarial, memory, protocols, regulation, economics, failures, dev adoption, blockchain, governance, HITL, competitive advantage
2. **SYNTHESIS**: Cross-learnings (V1: 7 briefs) + Deep Synthesis V2 (all 14 briefs — contradictions, predictions, contrarian views)
3. **GAP RESEARCH**: Trust Signal UX, AI Agent Insurance, Agent Failure Taxonomy
4. **OUTLINE**: State Report structure with narrative arc, claim register, audience strategy
5. **WRITE**: Section-by-section drafting following outline + claim register
6. **QA**: Rubric-based quality check before delivery
7. **BUILD**: Website, context packs, distribution assets

---

## QUALITY STANDARDS

### Confidence Levels
- **High**: 3+ independent sources, peer-reviewed or primary data
- **Medium**: 1-2 sources, plausible but not independently confirmed
- **Low**: Single secondary source, methodology unclear, or interpretation

### Research Brief Requirements (Tier 2)
- Key Findings (max 5)
- Verified numbers with sources
- Claim Ledger (top 5 claims with evidence + confidence)
- Contradiction Register (conflicting sources + resolution)
- "Unsicher / Nicht Verifiziert" section
- Beipackzettel (confidence %, sources checked, time spent)
- Clear separation: Evidence vs Interpretation vs Judgment

### QA Rubric (before any output)
1. ✅ Every number has a source
2. ✅ Confidence level on every claim
3. ✅ Evidence/Interpretation/Judgment clearly separated
4. ✅ No LLM phrases (see Voice Rules)
5. ✅ Contradictions acknowledged, not hidden
6. ✅ "What would invalidate this?" answered for key claims
7. ✅ Audience tag: [INTERN] [KUNDE] [PUBLIC] [LP/VC]

---

## VOICE RULES

### DO
- Solo founder voice: "I" not "We"
- Direct, short, specific
- Odd numbers for stats (3, 5, not 2, 4)
- Real company names ("Stripe" not "a major payment processor")
- 1 recommendation with "Mein Vote:" — not 5 options
- Honest numbers or leave them out
- "Consultant-grade" not "McKinsey-grade"

### DON'T
- ❌ "In today's rapidly evolving..." (LLM phrase)
- ❌ "Great question!" / "I'd be happy to!"
- ❌ "We believe..." (solo founder)
- ❌ Long introductions — get to the point
- ❌ "cheaper" as selling point → use time savings, quality
- ❌ Fake numbers ("2,847 professionals")
- ❌ "Trusted by [Logos]" without real customers
- ❌ Stock photos / AI-generated images

---

## DESIGN RULES

- **Colors**: Black + White + Gold (#c8aa50) ONLY
- **Font**: Inter, max weight 600 (Semibold)
- **Icons**: Custom SVG (Lucide, stroke-width 1.5) — NO emoji as icons
- **Images**: SVG graphics, code-based — NO stock photos
- **Pricing**: 3 tiers (Free / Pro / Custom)
- **CSS**: Always opacity:1 as default
- **Theme**: Light/bright, substance over decoration

---

## KNOWN MISTAKES (from corrections.md)

### Critical Process Errors
1. **Never build before asking** → "Stell mehr Fragen bevor du arbeitest"
2. **Never use Write for existing files** → Use Edit (Kintsugi principle)
3. **Never suggest features** → Ask "Bringt das Revenue?"
4. **Never make mental notes** → Write to file immediately
5. **Never send multiple Telegram messages** → Max 1 per delivery
6. **Never build without pre-flight** → Run `./scripts/pre-flight.sh`

### Critical Content Errors
1. **Never invent thesis from memory** → ALWAYS read original documents
2. **Never show prices/costs in customer docs** → Show only benefits, break-even, savings
3. **Never mix audiences** → Tag: [KUNDE] [LP/VC] [PUBLIC] [INTERN]
4. **Never use "We"** → "I" (solo founder)
5. **Never use even numbers for stats** → Use odd numbers (3, 5)

### Tonality
- Florian is technical — don't over-explain
- Be honest, give pushback when needed
- German, direct, short in communication with Florian
- "Lass dir Zeit. Besser einmal länger." (Quality > Speed)

---

## STATE REPORT STRUCTURE

**Title:** "State of AI Agent Trust 2026"
**Thesis:** "The AI agent industry is building without a trust layer — and the cost of not fixing this is accelerating exponentially."
**Target:** 15-20 pages (~8,000-10,000 words)

### Narrative Arc (5 Acts)
1. **PROBLEM**: $52B market building on sand (95% fail, 84% overconfident)
2. **EVIDENCE**: Overconfidence pandemic + adversarial spiral + alert fatigue
3. **GAP**: Three layers (Communication→Identity→Trustworthiness), Layer 3 missing
4. **SOLUTION**: Trust infrastructure as escape from regulatory trilemma ($0.005/check)
5. **PREDICTION**: >$100M catastrophe in 12 months if nothing changes

### The One Sentence
> "We're building a $52 billion industry where 84% of AI agents are overconfident, 95% of projects fail, and the fix costs half a cent — but nobody's implementing it."

---

*Load this pack for any pipeline-related task: writing, QA, building, or orchestration.*

---

## ⚠️ TEMPLATE LOCKED (2026-02-15 01:58 CET)

**ALL report design rules below are SUPERSEDED by the locked template.**
- Template: `content/reports/REPORT-TEMPLATE-FINAL.html`
- Rules: `content/reports/TEMPLATE-RULES.md`
- Design Tokens: `content/reports/template-elements/00-design-tokens.html`
- PDF Script: `scripts/html-to-pdf.sh` (Headless Chrome, $0, 2s)

**For BUILDER agent:** Copy REPORT-TEMPLATE-FINAL.html, swap content only. Never build from scratch.
**For QA agent:** Check against TEMPLATE-RULES.md, not "looks good."
**For WRITER agent:** Follow voice rules above + TEMPLATE-RULES.md content rules.

**Citation:** `Ainary Research (2026). [Title]. AR-XXX.` (NOT Ziesche, F.)
**Author Bio:** Fixed text, identical across all reports (see TEMPLATE-RULES.md)
**Back Cover CTA:** "Contact · Feedback" (NOT "Start a project →")
**PDF:** Always run `./scripts/html-to-pdf.sh` at end of pipeline. No agent for PDF.

### LEGACY RULES BELOW (kept for reference, template overrides all)

### Report Typography Rules (Florian Feedback 2026-02-14 15:43)
- Fußnoten [1] [2]: Grau (#888), hochgestellt, dezent
- Key Numbers/Stats: Schwarz (#1a1a1a) auf weißem Hintergrund
- Section Icons (SVG): Grau (#888), nicht Gold
- Bullet Points + Bold Text: Schwarz
- "So What?" Callouts: OK wie bisher (dezenter Gold left-border)
- "What would invalidate this?": OK wie bisher
- KEIN Gold für Zahlen, Icons, oder strukturelle Elemente

### Report Box Rules (Florian Feedback 2026-02-14 15:45)
- KEINE Boxes/Cards um Content-Blöcke (schlecht zum Ausdrucken)
- "So What?" = nur Text, kein Box/Border
- Exec Summary = Text, kein Box
- Predictions = Text, kein Box
- Claim Register = Tabelle (OK)
- Report #1 = Referenz: keine Boxes, clean Text
- Alles muss auf Papier (A4 Print) genauso gut aussehen wie am Screen

### Content Type Rules (Florian Feedback 2026-02-14 15:48)
- Research Report: KEINE persönliche Story. Nie. Daten sprechen.
- Blog Post: Persönlicher Hook JA, aber spezifisch + aktuell
  - ✅ "Last week I ran..." / "This week I noticed..."
  - ❌ "I've built AI products in Munich and New York" (CV-Style, zu generisch)
  - Hook = konkretes Erlebnis dieser Woche, nicht Lebenslauf

### Report Branding (Florian Feedback 2026-02-14 15:53)
- Gold-Punkt (●) rechts unten auf jeder Seite — 8-12px, #c8aa50, subtle
- Ainary Logo NUR auf Cover-Seite + letzte Seite (Footer)
- NICHT auf jeder Seite (wirkt wie Werbung)
- Der Punkt = Wiedererkennungsmerkmal, wie ein Qualitätssiegel

### Report Structure Standards (Florian Feedback 2026-02-14 16:17)

HEADER (jede Seite, Print + Screen):
- Links: "Ainary Report"
- Rechts: Report-Thema

FOOTER (jede Seite):
- Links: "© 2026 Ainary Ventures"
- Mitte: Seite X von Y
- Rechts: Gold-Punkt (●) 8px #c8aa50

COVER (Seite 1):
- Ainary Logo (wenn vorhanden)
- Titel + Untertitel
- Autor: Florian Ziesche — Ainary Ventures
- Datum
- Gesamtconfidence Score

BEIPACKZETTEL (letzte Seite vor References, PFLICHT):
- Gesamtconfidence: X%
- Anzahl Quellen: X primär, X sekundär
- Stärkste Evidenz: [welcher Claim]
- Schwächste Stelle: [was]
- "Was würde diesen Report entwerten?"
- Methodik: Kurzbeschreibung der Pipeline
- "Dieser Report wurde mit einem Multi-Agent Research System erstellt"

CONFIDENCE pro Section: Als Text "(Confidence: High/Medium)" — zurück als fester Bestandteil

### Chapter & Academic Standards (Florian Feedback 2026-02-14 16:19)

KAPITEL-NUMMERIERUNG:
- "1. Executive Summary", "2. The Problem", "3. Evidence"
- Nur 1 Level tief (keine 1.1, 1.2 — zu akademisch)
- Nummerierung in TOC und im Text

TABELLEN/GRAFIKEN:
- "Exhibit 1:", "Exhibit 2:" (McKinsey-Standard)
- Jedes Exhibit hat Titel + Source-Zeile darunter

ZITIER-VORSCHLAG (am Ende, vor References):
- "Cite as: Ziesche, F. (2026). [Title]. Ainary Research Report, No. [X]."

KEYWORDS (unter Executive Summary):
- 5-7 Keywords, kommasepariert

KEY INSIGHT pro Kapitel:
- Erster Satz fett, 1 Zeile — die Kernaussage des Kapitels
- Wie McKinsey "At a glance"

AUTOREN-BIO (letzte Seite):
- 2-3 Zeilen: "Florian Ziesche is the founder of Ainary Ventures..."

REPORT-NUMMER:
- Jeder Report bekommt eine Nummer: AR-001, AR-002, etc.
- AR = Ainary Report

### Report Footer/CTA (Florian Feedback 2026-02-14 17:00)
- Nach References: CTA Section
- "Request a Project →" (Gold link, text-link style)
- Subtext: "Create your own agent architecture and workflow — tailored to your organization."
- Email: florian@ainaryventures.com
- Website: ainaryventures.com
- Tagline: "HUMAN × AI = LEVERAGE"
- Gold-Punkt (●) rechts unten
- Stil: Clean, wie Website-Footer, nicht aufdringlich

### So What / Invalidation Design — FINAL (Florian Feedback 2026-02-14 17:02)
- ÜBERSCHREIBT vorherige Regel "nur Text"
- Stil von Report #3 (eu-us-regulation-2026.html) ist der Standard:
  - Gold left-border (3px, #c8aa50)
  - Leichter Background (gold-light/transparent)
  - "SO WHAT?" als Label (uppercase, gold, small)
  - Text darunter normal
  - "What would invalidate this?" als bold inline, gleicher Callout-Stil
- Das sind FUNKTIONALE Callouts, keine dekorativen Boxes
- Confidence Badges mit SVG Icons (High=checkmark green, Medium=circle orange) = OK
- ALLE Reports sollen diesen Stil haben

### Section Headers — NO ICONS (Florian Feedback 2026-02-14 17:28)
- KEINE Icons/Symbole/Emoji vor Kapitel-Überschriften
- NUR Nummern: "1. Executive Summary", "2. The Problem"
- KEINE SVG Icons vor Headers
- KEINE Apple-Symbole
- Icons haben keinen Mehrwert, nur Noise
- ÜBERSCHREIBT vorherige Regel "Section Icons in Grau"

### Brand Messaging — FINAL (Florian 2026-02-14 17:37)
- NIEMALS "replace consultants" oder "replace $200K"
- Hero: "Multiply your team."
- Subline: "We do 80% of the work. You do the 20% that matters."
- Tagline: "HUMAN × AI = LEVERAGE"
- "Power of Ainary" = Compounding + Brand
- Positioning: Augmentation > Replacement
- Respekt für den Kunden, nicht Bedrohung

### Report Cover/Layout Feedback (Florian 2026-02-14 18:05)
- "Florian Ziesche — Ainary Ventures" zu prominent auf Seite 1 → dezenter
- Datum in Header ODER Footer (nicht Cover-prominent)
- CTA Footer: NICHT "Create your own agent architecture..." → stattdessen Services auflisten: "Multi-Agent Architecture · AI Systems · Automation · Second Brain · Pilot Projects"
- Ainary Logo auf erste Seite (rechts oben oder Mitte) UND letzte Seite
- Referenz: Blog Post Layout mit Photo + rundes Symbol rechts unten → für Reports adaptieren
- REST ist gut

### Sales Angles aus Reports (Florian 2026-02-14)
- "Board age 59.1 avg + refreshment at 10-year low = AI competence gap" → Pitch für Board Advisory/Governance Reports
- Jeder Report soll 1-2 Sales Angles identifizieren die wir für Outreach nutzen können

### Report Cover + Footer STANDARD — McKinsey-Style (D-143, 2026-02-14)
OVERRIDES all previous cover/footer rules.

**Cover (Seite 1):**
- ● Ainary — oben links, klein, Gold-Punkt + "Ainary" in #1a1a1a
- AR-XXX — oben rechts, grau (#888), klein
- Titel — groß, linksbündig, max 2 Zeilen, font-weight 600
- Subtitle — kleiner, grau (#666)
- Datum — unten links, klein, grau
- NICHTS SONST. Kein Autor, kein Confidence, kein Slogan, kein CTA.
- 80% der Seite = Whitespace

**Letzte Seite (Back Cover):**
- ● Ainary — zentriert
- "AI Strategy · Published Research · Daily Intelligence" — grau (#666)
- "Start a project →" — grau (#888), gleiche Größe wie Email, KEIN Button, KEIN Gold, KEIN Bold
- ainaryventures.com
- florian@ainaryventures.com
- NICHTS SONST. Kein Slogan, kein "HUMAN × AI = LEVERAGE"

**Prinzip:** Der Report beweist. Die Website pitcht.

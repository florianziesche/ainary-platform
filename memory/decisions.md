<!-- temporal: stable | decay: monthly | last-reviewed: 2026-02-13 -->
# Decisions — Was entschieden wurde und warum

## Feb 2026

| Datum | Entscheidung | Warum | Alternativen |
|-------|-------------|-------|-------------|
| 13.02 | Black+White+Gold ONLY | "Neon = sieht aus wie LLM hat es gemacht" | Indigo, Neon-Palette |
| 13.02 | Hamburger Menu auf Mobile | Nav-Links waren hidden ohne Alternative | Sticky bottom nav |
| 13.02 | Layered Memory statt flat MEMORY.md | Context Window Effizienz | Alles in 1 File, Email-Reminder |
| 13.02 | Vault Bulk Fix (61 Stubs) | 79 Orphan Links = kaputtes Wissensnetz | Nur wichtige fixen |
| 13.02 | HOF Capital submitted | Erster VC Send. Alles war ready. | Weiter polieren |
| 12.02 | Vercel statt GitHub Pages | Private repos blockieren Pages im Free Plan | Netlify |
| 12.02 | DE als /de/ Subfolder | SEO besser als Subdomain | Subdomain, separates Repo |
| 12.02 | Blog Artikel-Titel bleiben EN in DE | Authentizität, sind englische Artikel | Übersetzen |
| 12.02 | "Consultant-grade" statt "McKinsey" | Kein Name-Dropping, Qualität spricht | "Enterprise-grade" |
| 12.02 | Solo founder voice: "I" not "we" | Ehrlich, 1-Person Company | "We" für Credibility |
| 12.02 | 1 free report (not 3) | Lower risk, still demonstrates value | 3 free, no free |
| 12.02 | 3 core products only | Fokus > Feature-Vielfalt | 6 Produkte |
| 11.02 | Ainary = DE Consulting + US Fund | Audiences nicht vermischen | Ein Brand für alles |
| 10.02 | Principles mit Score (+10/-20) | Darwinistisch = nur was funktioniert überlebt | Statische Regeln |
| 09.02 | CRM in Obsidian (Kanban) | Kein paid CRM nötig für aktuelle Größe | HubSpot, Notion |
| 09.02 | Edit > Write für Dateien | Kintsugi #6: Write zerstört Frontmatter | Immer Write |
| 08.02 | LaTeX für Print-PDFs | Professioneller als HTML→PDF | HTML only |
| 06.02 | Board of Advisors: Audience > Infrastructure | 6/6 Konsens | Weiter Infrastructure bauen |

## Ältere Entscheidungen
→ Siehe `projects/platform-website/DECISIONS.md` (90+ Website-Decisions)

## 2026-02-14
- D-110: Model-Zuordnung — Opus: WRITER/VC/RESEARCH, Sonnet: OUTREACH/BUILDER/CNC/QA
- D-111: Agents ab sofort für JEDE Aufgabe nutzen
- D-112: Blockchain × Agent Trust = sinnvolle Anwendung (Florians Idee)
- D-113: AgentTrust als Open Source Framework auf GitHub — Ziel: LangChain-scale
- D-114: Jeder Build-Schritt = Artikel (Content Flywheel)
- D-115: QA auch auf Mias eigene Outputs anwenden
- D-116: Exec Research Factory + Asset Builder aus Obsidian → integriert in RESEARCH + QA Agents

## D-131: Produktname — "X-Ray" → "Ainary Report" (2026-02-14)
- **Alt:** Corporate X-Ray, Startup X-Ray, Company X-Ray
- **Neu:** Ainary Report (Ainary Research Report, Ainary Company Report, Ainary Due Diligence Report)
- **Warum:** X-Ray klingt nach Tool, Ainary Report klingt nach Premium-Deliverable
- **Status:** BESTÄTIGT (2026-02-14 14:03)
- **TODO:** Auf Website, in allen Docs, Templates, HTML-Dateien umbenennen

## D-132: Ainary Report als Massenprodukt — $0.50/Report Vision (2026-02-14)
- **Vision:** Research Reports für $0.50 statt €5K-15K/3-4 Wochen
- **Differenzierung:** Calibration + Claim Register + Gap Analysis = IP
- **Validation first:** 25 Reports auf Website, Email-Gate, Pricing-Test
- **IP-Schutz:** Trade Secret (Pipeline), Trademark (Ainary Report), Patent prüfen
- **Distribution later:** Google Marketplace, API, Enterprise
- **Status:** VISION — erst validieren
- **Florian's Framing:** "Die Nummer 1, von jedem genutzt"

## D-133: Agent-Rollout Reihenfolge (2026-02-14)
- **Phase 1 (JETZT):** Research Pipeline kalibrieren — Reports #1-5
  - RESEARCH, WRITER, QA, BUILDER Agents
  - Context Packs validieren
  - Baseline messen, optimieren
- **Phase 2 (nach 5 Reports):** Learnings auf alle Agents übertragen
  - OUTREACH, VC, CNC mit gleichen Context Packs + Pipeline
  - Pipeline-Standards sind universal
- **Prinzip:** Einmal richtig lernen → alle profitieren
- **Status:** BESTÄTIGT

### D-135: CNC Screenshots — BACKLOG (2026-02-14)
- Problem: Echte Kundendaten + zu niedrige Zahlen (Value-Anker)
- Lösung: Fiktive Mockups mit höheren Werten
- Status: WARTEN — erst Reports fertig

### D-136: Brand Messaging FINAL (2026-02-14 17:37)
- NIEMALS "replace" oder "$200K consultants"
- Hero: "Multiply your team." + "We do 80%. You do the 20% that matters."
- Tagline: "HUMAN × AI = LEVERAGE"
- Florian's Worte, nicht Mia's

### D-137: Report Cover dezenter (2026-02-14 18:05)
- "Florian Ziesche — Ainary Ventures" weniger prominent
- Datum in Header/Footer, nicht Cover
- Ainary Logo auf erste + letzte Seite
- CTA = Services auflisten: Multi-Agent Architecture · AI Systems · Automation · Second Brain · Pilot Projects

### D-138: CNC Screenshots = Fiktive Daten (2026-02-14 17:42)
- Fiktive Zahlen, keine echten Firmennamen
- Status: BACKLOG nach Reports

### D-139: Self-Improvement Loop testen + versionieren (2026-02-14 18:16)
- Research → LLM fragt "was würdest du anders machen?"
- v1-spec.md erstellt, Hypothesen-Register angelegt
- Test ab AR-010

### D-140: TrustCheck = Backlog Service (2026-02-14 18:20)
- Erst Launch, dann TrustCheck als Ainary Service

### D-141: TrustCheck Report Standards (2026-02-14 18:30)
- Beipackzettel mandatory
- Confidence Score pro Claim
- Keine Apple Symbole → CSS Badges
- Design = gleich wie Ainary Reports
- CTA Footer = Standard
- Source Quality Rating für Future

### D-142: Projekt-Separation nötig (2026-02-14 17:43)
- Florian: "Machst du gute die Projekte getrennt zu halten?" → "Nein"
- Plan: pipeline-pack aufteilen, Feedback-Log pro Projekt, FLORIAN-INSIGHTS.md
- Status: BACKLOG

### D-143: Report Cover + Footer FINAL McKinsey-Style (2026-02-14 19:25-19:29)
**Cover:**
- ● Ainary oben links, klein
- AR-XXX oben rechts, grau
- Titel groß, linksbündig, max 2 Zeilen
- Subtitle kleiner, grau
- Datum unten links, klein
- KEIN Autorenname, KEIN Confidence, KEIN Slogan auf Cover
- 80% Whitespace

**Letzte Seite:**
- ● Ainary zentriert
- "AI Strategy · Published Research · Daily Intelligence"
- "Start a project →" in GRAU (#888), diskret, kein Button
- ainaryventures.com
- florian@ainaryventures.com
- KEIN "HUMAN × AI = LEVERAGE", KEIN "Multiply your team"

**Prinzip:** Report beweist. Website pitcht. Unterschiedliche Jobs.

### D-144: Brave Pro weiter nutzen (2026-02-14 19:33)
- Qualität > Kosten. $5/Mo ist nichts vs schlechte Research.
- Florian: "Qualität ist wichtig!"

### D-145: Template-First Workflow (2026-02-14 19:31)
- KEIN Report ohne locked Template
- Feedback → Template, nie in einzelne Reports
- Template LOCK nach Florians Go
- Automatischer Compliance-Check vor Delivery
- Kintsugi #8: "10 Reports und noch immer Anpassungen"

### D-146: Report Template FINAL Spec (2026-02-14 23:46) — Florian's Consolidated Feedback

**Cover (Seite 1):**
- Security Playbook v2 = Referenz ✅ "best so far"
- Overall Confidence in Header oben? → Florian fragt, diskutieren

**Quote Page:**
- NEUE SEITE: Wichtigste Zitate mit Referenz zu Sections/Chapters
- Referenz: Financial Services Quote "We're building a $52 billion industry..."

**Contents/TOC:**
- Maturity Model = Referenz ✅
- Nummerierung: 01, 02, 03 (elegant, professional, confident)
- Hover-Effekt: Schwarz → Gold bei Mouse-over
- SEITENZAHLEN FEHLEN → hinzufügen

**Executive Summary:**
- Maturity Model Style = Referenz ✅
- Bold Text + kleinerer Text + Source-Anzeige
- Gold für KEY FIGURES (nicht dekorativ, sondern Readability-Hilfe)
- Thesis im Exec Summary = gut (State of Trust Referenz)

**Keywords:**
- Security Playbook Style ✅

**Bold Elements:**
- Wichtige Elemente in Bold Schwarz (State of Trust Referenz)

**Methodology:**
- Kurz (Maturity Model) UND lang (Security Playbook) — McKinsey Research needed
- "The model itself is a proposed framework..." Statement = gut
- "Confidence ratings follow a three-tier system" + "Limitations" = Bold, wertschaffend
- Confidence-Level Definition: VOR dem Report oder am Ende mit klickbarem Link

**KPI Figures:**
- Trust Tax Style ✅ — aber Schwarz auf Weiß, NICHT farbig (lenkt ab)

**Source Display:**
- Inline Sources mit Confidence = gut
- Format: "Source: [Name], [Date]. [Publication]. | Confidence: High"

**Sections:**
- Längerer Text bevorzugt (Security Playbook > Maturity Model)
- ABER Sources/Info-Dichte wie Maturity Model
- Key Statement nach Header muss KLAR als Zusammenfassung erkennbar sein (Financial Services besser als Security Playbook)
- Prozent-Badges nach Headers (60% etc) mit Farbe + Background = funktioniert

### D-146 (continued): Report Template — Section-Level Feedback

**Layered Text Display:**
- State of Trust "Three-Layer Trust Gap" style = gut
- Layer 3/2/1 mit ← Annotations — visuell klar, elegant

**So What / What Would Invalidate:**
- REIHENFOLGE: "What would invalidate" ZUERST, dann "So What"
- Text muss DIREKT unter dem Label stehen, nicht auf nächster Seite umbrechen
- Maturity Model Style gut, ABER braucht grafisches Element
- Mindestens: Light Grey Background (#f5f4f0)
- Zwei Varianten: "What would invalidate" = Grau, "So What" = Gold-left-border
- Security Playbook = beste Referenz für diese Elemente

**"I reviewed..." Formulierungen → ENTFERNEN**
- "I reviewed 6 major AI maturity models" = Credibility-Killer
- Jeder weiß es ist AI-generiert → "I" verliert Glaubwürdigkeit
- Doppelt negativ: unglaubwürdig + unnötig
- NUR Fakten. CEO will Ergebnisse, nicht Prozess.
- NEUE REGEL: Kein "I reviewed/analyzed/examined" in Reports

**Key Claims als grafisches Element:**
- "Prompt injection is not a bug to be patched..." = Claim
- Eigenes Element: Grau-Hintergrund (nicht Gold), klar als Claim erkennbar
- Unterscheidung: Claim (grau) vs So What (gold) vs Invalidation (grau, andere Variante)

**Chapter Spacing:**
- Footer-to-Header Abstand zu groß bei Seitenumbrüchen → reduzieren

**Confidence pro Section in Header:**
- "4. Prompt Injection (Confidence: High)" = gut
- Projections mit separater Confidence: "High Confidence (regulatory) · Medium (projections)" = baut Vertrauen

**KPI/Projection Likelihood:**
- Trust Tax Style: Likelihood bei Projektionen angeben
- "(medium)" neben Projektionen = ehrlich + vertrauensbildend

### D-147: Template Chooser = potentielles Produkt (2026-02-15 00:02)
- Florian: "Genial!! Sollten wir pflegen und vlt als Product mitliefern."
- Für den Moment nur intern
- Pflegen + weiterentwickeln

### D-148: Cover Audience — Audience in Exec Summary, NOT on Cover (2026-02-15 00:13)
- Problem: CEO/CTO zu eng, VCs + Startups + Consultants sollen auch angesprochen werden
- Florian: "Audience ist besser als die Rolle, und die first page ist dann cleaner"
- ENTSCHIEDEN: Cover bleibt clean (keine Audience/Rolle). Audience-Definition in Exec Summary.

### D-149: Research = Ground Truth (2026-02-15 00:15)
- "Research ist die ground truth for me"
- Alle Design-Entscheidungen müssen Benchmarks zitieren (BCG, McKinsey, Economist)

### D-151 bis D-157: Execution Platform Decisions (2026-02-18)
- D-151: Localhost + Auto-Start (launchctl). Remote = Phase 2.
- D-152: Offline-fähig (Navigation OK ohne Mia, AI + Actions brauchen Mia).
- D-153: Feedback DETAILLIERT — pro Abschnitt/Claim markieren.
- D-154: Platform = primäres Interface. Telegram für Quick Messages.
- D-155: Done v1 = Fehlerfrei + Live AI + Trust System + 5 VC Emails durch Platform gesendet.
- D-156: Mia als Backend, aber austauschbar (Action Layer Interface).
- D-157: Build = gut WENN Build → Send → Revenue. Sonst schlecht.

### D-158: ISO-aligned Documentation Standards (2026-02-18)
- Semantic Versioning für alle Projekte
- CHANGELOG.md, ARCHITECTURE.md, ROADMAP.md pro Projekt
- Security Controls nach ISO 27001 (Localhost-only = kein Auth nötig Phase 1)
- Jede Änderung: Datum + Was + Warum

### D-150: Chooser Workflow = Standard für alles (2026-02-15 00:10)
- "We should always work like this, same for website, other tools, dashboards plus an option to write comments"
- Template Chooser Pattern für alle Design-Entscheidungen verwenden

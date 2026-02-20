# Engineering Standards — Domain Knowledge
*Auto-consolidated: 2026-02-20 22:02 | 7 findings | avg conf: 87% | 0 verified*

## Verified Claims (conf ≥80%)

**RF-026** [95%]: Gewichteter Durchschnitt (a*0.7 + b*0.3) ist KEIN Bayesian Update. Echte Formel: P(H|E) = P(E|H)·P(H) / [P(E|H)·P(H) + P(E|¬H)·P(¬H)]. Ergebnis: starke Evidenz bewegt stark, schwache Evidenz bewegt kaum.
Source: MIT 18.05 Class 11, Towards Data Science Bayesian Updating, Wikipedia Bayesian Inference
Tags: bayesian, statistics, confidence_scoring, algorithm, engineering_standards

**RF-025** [90%]: Native browser prompt() zerstört UX-Flow und signalisiert Amateur-Level. Inline Modal mit Fokus-Management ist Standard.
Source: Execution Platform Finding Form: prompt() → Modal. Verifiziert durch Linear/Notion/Figma Patterns.
Tags: ux_design, frontend, modal, form_pattern, website_design

**RF-029** [90%]: Research VOR Implementierung ist nicht optional. 15min Research hätte 40min Rework gespart (fake Bayesian, prompt() statt Modal). Qualitätsstandard: kein Code ohne vorherige Pattern-Research.
Source: v0.11.0 hatte fake Bayesian + prompt(). v0.11.1 musste beides fixen nach Research. Vermeidbar.
Tags: process, quality, research_first, engineering_standards

**RF-027** [85%]: Unidirektionale Connections (A→B) verstecken die Hälfte der Information. Bidirektionale Connections (Upstream/Downstream) zeigen das volle Bild ohne doppelte Einträge.
Source: Execution Platform: Topic Detail API zeigt jetzt sowohl from_topic als auch to_topic Connections mit Richtung.
Tags: data_model, ux_design, graph, connections, engineering_standards

**RF-030** [85%]: Empty States brauchen 3 Elemente: (1) visuelles Element (Icon/Illustration), (2) was fehlt, (3) wie man es behebt (CTA). Nur Text = vergessener Zustand.
Source: Findings Empty State: Diamant-Icon + Erklärung + farbiger CTA (+ Finding). Vorher nur grauer Text.
Tags: ux_design, empty_state, frontend, website_design

**RF-080** [85%]: LangExtract installed for char-level evidence extraction
Source: workspace
Tags: langextract, evidence, engineering

**RF-038** [80%]: Eine horizontale 4-Column Kanban Pipeline View zeigt Flywheel-Gesundheit auf einen Blick besser als eine vertikale Liste. Topics als Cards mit Connection-Badges + Findings-Count machen die Compound-Effekte sichtbar.
Source: Execution Platform Pipeline View v0.11.3. Research: Atlassian Funnel Charts, PipelineCRM Kanban, Linear App Design.
Tags: pipeline, ux_design, kanban, visualization, product_design, website_design

## Dead Findings

- ~~RF-019~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-023~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-033~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-036~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-040~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-043~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-004~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-006~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-008~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-011~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-014~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-016~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-018~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-022~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-032~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-035~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-039~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-042~~: Test finding for automated tests — killed: Automated test artifacts, not real knowledge
- ~~RF-021~~: Bayesian test — killed: Automated test artifacts, not real knowledge
- ~~RF-005~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-007~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-010~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-013~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-020~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-024~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-034~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-037~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-041~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-044~~: Test contradiction detection — killed: Automated test artifacts, not real knowledge
- ~~RF-009~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-012~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-015~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge
- ~~RF-017~~: Low conf finding for validation test — killed: Automated test artifacts, not real knowledge

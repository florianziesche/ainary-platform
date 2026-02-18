# Engineering Standards — Domain Knowledge
*Auto-consolidated: 2026-02-18 14:03 | 6 findings | avg conf: 88% | 0 verified*

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

**RF-038** [80%]: Eine horizontale 4-Column Kanban Pipeline View zeigt Flywheel-Gesundheit auf einen Blick besser als eine vertikale Liste. Topics als Cards mit Connection-Badges + Findings-Count machen die Compound-Effekte sichtbar.
Source: Execution Platform Pipeline View v0.11.3. Research: Atlassian Funnel Charts, PipelineCRM Kanban, Linear App Design.
Tags: pipeline, ux_design, kanban, visualization, product_design, website_design

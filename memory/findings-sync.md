# Platform Findings (auto-synced from Execution Platform)

*10 findings from CKE. Last sync: 2026-02-18*

## Engineering Standards
- **RF-026** [95%] Gewichteter Durchschnitt (a*0.7 + b*0.3) ist KEIN Bayesian Update. Echte Formel: P(H|E) = P(E|H)·P(H) / [P(E|H)·P(H) + P(E|¬H)·P(¬H)]. Ergebnis: starke Evidenz bewegt stark, schwache Evidenz bewegt kaum.
  Tags: bayesian, statistics, confidence_scoring, algorithm, engineering_standards
- **RF-025** [90%] Native browser prompt() zerstört UX-Flow und signalisiert Amateur-Level. Inline Modal mit Fokus-Management ist Standard.
  Tags: ux_design, frontend, modal, form_pattern, website_design
- **RF-029** [90%] Research VOR Implementierung ist nicht optional. 15min Research hätte 40min Rework gespart (fake Bayesian, prompt() statt Modal). Qualitätsstandard: kein Code ohne vorherige Pattern-Research.
  Tags: process, quality, research_first, engineering_standards
- **RF-027** [85%] Unidirektionale Connections (A→B) verstecken die Hälfte der Information. Bidirektionale Connections (Upstream/Downstream) zeigen das volle Bild ohne doppelte Einträge.
  Tags: data_model, ux_design, graph, connections, engineering_standards
- **RF-030** [85%] Empty States brauchen 3 Elemente: (1) visuelles Element (Icon/Illustration), (2) was fehlt, (3) wie man es behebt (CTA). Nur Text = vergessener Zustand.
  Tags: ux_design, empty_state, frontend, website_design
- **RF-038** [80%] Eine horizontale 4-Column Kanban Pipeline View zeigt Flywheel-Gesundheit auf einen Blick besser als eine vertikale Liste. Topics als Cards mit Connection-Badges + Findings-Count machen die Compound-Effekte sichtbar.
  Tags: pipeline, ux_design, kanban, visualization, product_design, website_design

## Agent Trust Governance
- **RF-001** [90%] Pre-Flight mit Regex fängt 80% der Output-Fehler bei 0 Kosten und <50ms
  Tags: ai_quality, pre_flight, regex
- **RF-002** [73%] Bayesian Trust Scoring konvergiert schneller als lineares +2/-3 bei kleinen Stichproben
  Tags: ai_quality, trust, bayesian

## Compound Systems
- **RF-031** [90%] Ein Wissens-System das vom Erbauer nicht benutzt wird, wird von niemandem benutzt. Dogfooding ist der erste Test. Wenn ich Findings nicht in die Platform schreibe die ich gerade dafür gebaut habe, ist das System gescheitert.
  Tags: process, dogfooding, compound_knowledge, meta
- **RF-028** [80%] Pipeline-Conversion-Rates zwischen Stages (Research→Systems: X%) sind der beste Indikator für Flywheel-Gesundheit. 0% Conversion = Silo, nicht Flywheel.
  Tags: pipeline, metrics, flywheel, product_design, kpi


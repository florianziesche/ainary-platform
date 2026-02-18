# Principles — L1 (Florian-reviewed)

*Auto-extracted from Platform Findings (conf ≥85%, verified). Florian approves/rejects.*
*Last updated: 2026-02-18 | Status: APPROVED by Florian*

---

## Engineering

**P1: Research First** [RF-029, 90%] ✅
Research VOR Implementation. 15min Research spart 40min Rework — bei wichtigen Entscheidungen auch Stunden, Tage oder Wochen. Wichtige Entscheidungen compounden.
Ausnahme: Confidence >90% → handeln.

**P2: Echte Mathematik** [RF-026, 95%] ✅
Gewichteter Durchschnitt ist kein Bayesian Update. Wenn es eine echte Formel gibt, die echte Formel benutzen. Keine Shortcuts — sie führen zu Nacharbeit und kosten ein Vielfaches an Zeit und Aufwand.

**P3: Professional Patterns** [RF-025, 90%] ✅
Native Browser-APIs (prompt(), alert()) = Amateur. Inline Modals mit Focus-Management = Standard. Immer recherchieren wie der Marktführer der jeweiligen Kategorie es löst — nicht raten, nachschauen.

**P4: Cheapest Check First** [RF-001, 90%] ✅
Pre-Flight mit Regex fängt 80% der Fehler bei 0 Kosten und <50ms. Teure Checks (LLM) nur für was Regex nicht kann.

**P5: Beide Richtungen modellieren** [RF-027, 85%] ✅
Unidirektionale Verbindungen verstecken die Hälfte der Information. Upstream + Downstream immer sichtbar.

## Process

**P6: Dogfooding** [RF-031, 90%] ✅
Ein System das vom Erbauer nicht benutzt wird, wird von niemandem benutzt. Erster Test: benutze ich es selbst?

**P7: AI Output ist overconfident** [C002, 85%] ✅
84% der LLM-Outputs zeigen höhere Confidence als tatsächliche Accuracy (PMC, 9 Modelle, 351 Szenarien). Immer kalibrieren.

## Strategy

**P8: Personal Intelligence > General Intelligence** [Compound-Machine-Architecture] ✅
Deep Context für einen Menschen schlägt breites Wissen für alle. Unser Moat: Tiefe, nicht Breite.

**P9: Ship > Perfect, aber Perfect > Ship bei Irreversiblem** ✅
Reversible Entscheidungen: >80% Confidence → handeln. Irreversible: >92%.

---

*Promotion-Kriterien: Finding conf >90% + mindestens 3x benutzt + Florian explicit OK.*
*Review-Zyklus: Monatlich. Nächster Review: 2026-03-18.*

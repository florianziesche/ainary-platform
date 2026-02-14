# Pipeline Log — Improvement Protocol

*Ein Report, eine Hypothese, ein Learning. Keine Ausnahmen.*

## Report #1: State of AI Agent Trust 2026
- **Hypothese:** Baseline (keine Optimierung)
- **Ergebnis:**
  - Research: 4m59s (Gap Research 20s + Outline 4m39s)
  - Writer: 4m08s
  - QA: 2m28s — Score 82/100
  - Builder: 5m35s
  - Total: ~17 Min
  - Tokens: ~840K über alle Agents
  - Quellen: 18 + 15 bestehende
  - Claims: 30
- **Learning:** 200K Token Input pro Agent ist zu viel. Meiste Zeit = Lesen, nicht Denken.
- **Nächste Hypothese:** Context Pack reduziert Tokens + Zeit ohne Qualitätsverlust

## Report #2: The Trust Tax (IN PROGRESS)
- **Hypothese:** Context Pack (~15K) statt volle Briefs (~200K) = schneller, gleiche Qualität
- **Variable:** Context Pack eingeführt
- **Ergebnis:**
  - Research: 2m47s (44% schneller ✅)
  - Writer: ⬜ läuft
  - QA: ⬜
  - Builder: ⬜
- **QA:** 2m02s — Score 88/100 (CONDITIONAL PASS, 3 minor fixes)
  - Builder: ⬜
  - Total: ~9 Min
  - Tokens: ~470K (vs ~840K = -44%)
- **Learning:** Context Pack = VALIDIERT. Schneller (-47%) UND besser (+6 QA Punkte). Weniger Rauschen → fokussierterer Output. Ab jetzt Standard für alle Reports.
- **Nächste Hypothese:** Dynamische Packs (nur relevante Briefs pro Topic)

## Hypothesen-Backlog
| # | Report | Hypothese | Variable |
|---|--------|-----------|----------|
| 3 | EU vs US Regulation | Research+Write kombiniert in 1 Agent | Phase-Reduktion |
| 4 | AI Agent Maturity Model | Detailliertere Outline → höherer QA Score? | Outline-Tiefe |
| 5 | Financial Services Playbook | Sonnet für Research, Opus nur für Writer | Model-Mix |
| 6 | TBD | Parallel QA während Writer schreibt | Parallelisierung |
| 7 | TBD | Context Pack v2 (mit Report #1-5 Learnings) | Pack-Update |

## Regeln
1. Nur EINE Variable pro Report ändern
2. Protokoll VORHER schreiben (Hypothese)
3. Protokoll NACHHER updaten (Ergebnis + Learning)
4. Kein Report ohne dokumentiertes Learning
5. Nach Report #5: Context Pack v2 aus allen Learnings

## Primär-Metrik Klarstellung (2026-02-14, Florian)
**QA Score > Speed > Tokens.** Immer.
Speed ist Nebeneffekt guter Architektur, nicht das Ziel.
Wenn Context Pack Qualität senkt, ist es gescheitert — egal wie schnell.

## Florian Feedback — Report Review (2026-02-14 14:31)
1. **Quellenangaben als hochgestellte Ziffern [1]** — fehlen. Academic-style Footnotes = Pflicht ab Report #3
2. **Mata v. Avianca $5K** — korrekt aber schlecht geframed. Reputations-Schaden betonen, nicht nur Fine.
3. **Custom Display Options** — User wählt: Footnotes on/off, Claim Register on/off, Confidence on/off → User-Preference Daten = kostenlose Marktforschung

## Weitere Feedback-Punkte (2026-02-14 14:35)
4. **Download Button (PDF)** — Pflicht auf jedem Report. Tracking: Gelesen vs Downloaded = Engagement-Metrik
5. **User Analytics auf Website** — GA4 oder Plausible (privacy-friendly). Messen: Verweildauer, Scroll-Tiefe, Download-Rate
6. **Mata v. Avianca ersetzen** — $5K zu schwach als Haupt-Case. Stärkeren Case mit Millionen-Schaden verwenden. (BESTÄTIGT: Option C)
7. **Meinungen klar labeln** — "incalculable" ohne Quelle = Meinung. Nicht in Research Reports ohne Label.

## Pipeline-Regel: QA Subject-Bezogen (2026-02-14, Florian)
- QA IMMER nach Builder, nie parallel am gleichen Subject
- QA in Scopes aufteilen: Design, Content, Technical, Nav
- Jeder QA-Run = 1 Scope, geht tief statt breit
- Orchestrator (Mia) gleicht ab wenn parallel nötig

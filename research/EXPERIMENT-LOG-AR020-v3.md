# Experiment Log: AR-020 v3 — Self-Calibrating Research Report

**Experiment ID:** EXP-2026-02-19-001
**Start:** 2026-02-19 09:30 CET
**Operator:** Mia (Main Agent, Claude Opus 4.6)
**Goal:** Produziere den ersten selbst-kalibrierenden Research Report über Trust Calibration

---

## 1. Experiment-Design

### Forschungsfrage
"Kann ein AI-Agent-System einen Research Report produzieren, der (a) Harvard/McKinsey-Qualität erreicht, (b) eigene empirische Daten enthält, und (c) die Methoden die er beschreibt auf sich selbst anwendet?"

### Hypothese
Ein Multi-Agent-System mit spezialisierten Sub-Agents (Research, Code, Synthesis) produziert qualitativ bessere Reports als ein einzelner Agent — aber nur wenn die Agents aufeinander aufbauen (Pipeline), nicht parallel arbeiten.

### Versuchsaufbau

```
┌─────────────────────────────────────────────────────────┐
│                    MAIN AGENT (Opus)                     │
│              Orchestrierung, QA, Final Edit              │
│                                                         │
│  Parallel Phase:                                        │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐│
│  │ Agent 1      │ │ Agent 2      │ │ Agent 3          ││
│  │ RESEARCH     │ │ PYTHON       │ │ SYNTHESIS        ││
│  │ (Opus)       │ │ (Sonnet)     │ │ (Opus)           ││
│  │              │ │              │ │                   ││
│  │ 7× R2 Topics │ │ Calibration  │ │ AR-020 v3 Report ││
│  │ 35 Hypothesen│ │ Library +    │ │ (wartet auf 1+2) ││
│  │              │ │ 4 Experiments│ │                   ││
│  └──────┬───────┘ └──────┬───────┘ └────────┬──────────┘│
│         │                │                   │          │
│         ▼                ▼                   ▼          │
│    R2-frontier.md   ainary-calibration/   AR-020-v3    │
│    (35 Verdicts)    (Python + Results)    (Mega-Report)│
│                                                         │
│  Sequential Phase:                                      │
│  Main Agent reviewt alle 3 Outputs, QA, Final Assembly  │
└─────────────────────────────────────────────────────────┘
```

### Warum dieses Design?

**Agent 1 (Research) und Agent 2 (Python) sind unabhängig** — sie können parallel laufen weil:
- Research braucht keinen Code
- Code braucht keine neuen Research-Ergebnisse (baut auf V2)

**Agent 3 (Synthesis) ist abhängig** — wartet auf 1+2 weil:
- Muss Research-Verdicts integrieren
- Muss Experiment-Daten einbauen
- Ist die "Synthesis-Schicht" die alles zusammenführt

**Erwartete Failure Modes:**
- Agent 3 Timeout bevor Agent 1 fertig (mitigation: 40 Min Timeout, polling)
- Research-Agent findet keine Evidenz für radikale Hypothesen (mitigation: "keine Evidenz" ist ein valides Ergebnis)
- Python-Experiments simuliert statt real (mitigation: transparent dokumentieren)

---

## 2. Vorgeschichte (Iterationen V1 → V2 → V3)

### V1: Speed-Batch (05:00 CET)
- **Methode:** 1 Sub-Agent (Sonnet), Prompt "schreib 10 Reports", 3× web_search pro Report
- **Dauer:** ~8 Min für AR-020
- **Qualität:** B-Grade. Wikipedia-Level Zusammenfassung.
- **Kritische Fehler:** 
  - Empfiehlt Temperature Scaling als Default → funktioniert nicht für API-basierte LLMs
  - Keine Hypothese vor Research
  - Keine Disconfirmation
  - Keine Contradictions gefunden
  - 0 Connections zu bestehendem Wissen
- **Quality Gate Score:** Nicht durchgeführt (kein Gate definiert)
- **Quellen:** 10, keine Admiralty Ratings
- **Wörter:** ~1.900

### V2: Golden Standard (08:18 CET)
- **Methode:** 1 Sub-Agent (Opus), R2 Standard + Research Protocol, 10+ web_search
- **Dauer:** ~10 Min
- **Qualität:** A-Grade. Erste echte Deep Dive.
- **Verbesserungen vs V1:**
  - Hypothesis VOR Research → Verdict: NUANCED
  - 6 Familien statt 3 Ansätze
  - RLHF-Calibration Discovery (V1 hatte das nicht)
  - Black-Box Constraint erkannt (V1 ignorierte es)
  - 3 Contradictions gefunden und aufgelöst
  - 4 Connections zu bestehendem Wissen
  - Multi-Agent Calibration Gap identifiziert
- **Quality Gate Score:** 15/15
- **Quellen:** 20, mit Admiralty Ratings (A1-B2)
- **Wörter:** ~4.000
- **Outputs:** 4 (Obsidian Note, Full Report, Asset Pack, HTML)

### V2 → V3: Was fehlt noch?

| Gap | V2 Status | V3 Ziel |
|-----|-----------|---------|
| Eigene Daten | 0 | Monte Carlo Sims, ECE Tests |
| Python Library | 0 | pip-installierbares Package |
| Case Studies | 0 | 2-3 echte Failure Cases |
| Practitioner Checklist | 0 | 10-Step "Monday Morning" Guide |
| Visual Exhibits | 0 | Decision Tree, Cost Waterfall, Propagation Chart |
| Hypothesen-Vielfalt | 1 Hypothesis | 35 Hypothesen (5 × 7 Topics) |
| Self-Calibration | 0 | Report kalibriert sich selbst |
| Cross-References | Obsidian nur | HTML + Obsidian |
| Back Cover | Falsch | "AI Strategy · System Design · Execution · Consultancy · Research" |

---

## 3. Agent-Konfiguration

### Agent 1: calibration-frontier-research
- **Model:** Claude Opus 4.6 (max Qualität für Research)
- **Timeout:** 30 Min
- **Input:** R2 Standard, Research Protocol, AR-020 v2
- **Task:** 7 R2 Topics × 5 Hypothesen = 35 Verdicts
- **Expected Output:** ~15.000 Wörter, 21+ web_search
- **Risiko:** Timeout bei 7 Topics (mitigation: Quality > Completeness)

### Agent 2: calibration-python-library
- **Model:** Claude Sonnet 4.5 (gut genug für Code, schneller)
- **Timeout:** 30 Min
- **Input:** AR-020 v2 (6 Familien, 3-Tier Architektur)
- **Task:** Python Package + 4 Simulationsexperimente
- **Expected Output:** ~20 Python Files, Experiment JSONs
- **Risiko:** Code läuft nicht (mitigation: Agent muss selbst testen)
- **Constraint:** Kein API-Key → alle Experiments sind Simulationen, NICHT echte LLM-Calls

### Agent 3: ar020-v3-mega
- **Model:** Claude Opus 4.6 (Synthesis braucht Opus)
- **Timeout:** 40 Min
- **Input:** V2 + Agent 1 Output + Agent 2 Output
- **Task:** Mega-Report mit 5 Verbesserungen + Self-Calibration
- **Expected Output:** 4 Files (Obsidian, Full, HTML, Assets), ~8.000 Wörter
- **Dependency:** Pollt Agent 1+2 Outputs alle 60s, Fallback nach 20 Min
- **Risiko:** Bekommt Inputs nicht rechtzeitig (mitigation: Fallback auf V2 Daten)

---

## 4. Metriken & Erfolgskriterien

### Quantitativ
| Metrik | V1 | V2 | V3 Target |
|--------|-----|-----|-----------|
| Wörter | 1.900 | 4.000 | 5.000-8.000 |
| Quellen | 10 | 20 | 30+ |
| Hypothesen getestet | 0 | 1 | 35 |
| Contradictions | 0 | 3 | 5+ |
| Connections | 0 | 4 | 10+ |
| Eigene Datenpunkte | 0 | 0 | 1000+ (Simulationen) |
| Quality Gate | n/a | 15/15 | 15/15 |
| Visual Exhibits | 0 | 0 | 3-5 |
| Case Studies | 0 | 0 | 2-3 |

### Qualitativ
- [ ] Self-Calibration Section vorhanden und glaubwürdig
- [ ] Practitioner Checklist actionable (nicht generisch)
- [ ] Python Library lauffähig (python3 run_experiments.py)
- [ ] Jede Hypothese hat Verdict + Evidenz
- [ ] Report widerspricht sich nicht intern
- [ ] Back Cover korrekt

---

## 5. Kosten-Tracking

| Agent | Model | Est. Input Tokens | Est. Output Tokens | Est. Cost |
|-------|-------|-------------------|--------------------| --------- |
| Agent 1 (Research) | Opus | ~50K | ~25K | ~$0.75 |
| Agent 2 (Python) | Sonnet | ~30K | ~40K | ~$0.70 |
| Agent 3 (Synthesis) | Opus | ~80K | ~30K | ~$1.05 |
| **Total** | | ~160K | ~95K | **~$2.50** |

Zum Vergleich:
- V1: ~$0.15 (1 Sonnet Call)
- V2: ~$0.50 (1 Opus Call)
- V3: ~$2.50 (3 Agents, 2 Opus + 1 Sonnet)
- McKinsey-Report gleichwertiger Tiefe: ~$50.000-150.000

**Cost Efficiency: ~1:20.000 bis 1:60.000 vs. menschlicher Report.**

---

## 6. Timeline

| Zeit (CET) | Event | Status |
|------------|-------|--------|
| 04:00 | Session Start, Vault Infrastructure | ✅ Done |
| 05:00 | AR-016-025 V1 Batch (Speed Mode) | ✅ Done |
| 07:46 | AR-020 V1 HTML generiert | ✅ Done |
| 08:18 | AR-020 V2 Golden Standard (Opus, R2) | ✅ Done |
| 08:30 | V2 PDF generiert und an Florian gesendet | ✅ Done |
| 09:15 | Hierarchical Lookup Tool gebaut | ✅ Done |
| 09:30 | V3 Experiment gestartet (3 parallele Agents) | 🔄 Running |
| ~09:45 | Agent 2 (Python) erwartet fertig | ⏳ Pending |
| ~09:55 | Agent 1 (Research) erwartet fertig | ⏳ Pending |
| ~10:05 | Agent 3 (Synthesis) erwartet fertig | ⏳ Pending |
| ~10:15 | Main Agent: QA, Final Assembly, PDF | ⏳ Pending |

---

## 7. Lessons Learned (wird live aktualisiert)

### Von V1 → V2
1. **Speed-Batch produziert gefährliche Outputs** — V1 empfahl eine Methode die nicht funktioniert
2. **Hypothesis + Disconfirmation = 10x bessere Insights** — V2 fand RLHF-Problem, V1 nicht
3. **R2 Quality Gate ist notwendig, nicht optional** — ohne Gate keine Qualitätskontrolle
4. **Opus > Sonnet für Research** — Sonnet reproduziert bekanntes Wissen, Opus findet Neues

### Von V2 → V3 (Hypothesen, noch nicht verifiziert)
5. **Multi-Agent > Single-Agent für komplexe Reports** — zu verifizieren
6. **Eigene Daten > Zitate** — zu verifizieren
7. **Self-Calibration macht den Report glaubwürdiger** — zu verifizieren
8. **35 Hypothesen > 1 Hypothese** — zu verifizieren (Risiko: Breite > Tiefe)

---

## 8. Reproduzierbarkeit

Dieses Experiment kann reproduziert werden mit:
1. OpenClaw Gateway mit Claude Opus 4.6 + Sonnet 4.5
2. Die 3 Sub-Agent Prompts (in Session Transcripts)
3. AR-020 v2 als Basis-Input
4. R2-DEEP-DIVE-RESEARCH.md + RESEARCH-PROTOCOL.md Standards
5. ~$2.50 API-Budget

**Nicht reproduzierbar:**
- Exakte web_search Ergebnisse (zeitabhängig)
- Memory/Vault Context (spezifisch für unsere Installation)
- Timing/Ordering der Agent-Completion

---

## 9. Ergebnisse (wird nach Completion ausgefüllt)

### Agent 1 (Research)
- Status: ⏳ Running
- Completion Time: —
- Output Size: —
- Hypothesen Verdicts: —/35
- Neue Insights: —

### Agent 2 (Python)
- Status: ⏳ Running
- Completion Time: —
- Output Size: —
- Experiments Run: —/4
- Code Lauffähig: —

### Agent 3 (Synthesis)
- Status: ⏳ Running
- Completion Time: —
- Output Size: —
- Self-Calibration: —
- Quality Gate: —/15

### Final Assessment
- V3 besser als V2? —
- Self-Calibration glaubwürdig? —
- Publishable Quality? —
- McKinsey-Level? —

---

*Log wird live aktualisiert durch Main Agent.*
*Nächstes Update: bei Completion der Sub-Agents.*

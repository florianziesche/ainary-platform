# Research Brief: Honesty and Trust Systems in Multi-Agent AI Architectures

**Datum:** 2026-02-14
**Agent:** RESEARCH
**Tag:** [INTERN]

---

## Key Findings (5)

1. **TRiSM-Framework ist der aktuelle akademische Standard.** Shaina Raza et al. haben mit "TRiSM for Agentic AI" (arXiv:2506.04133, Jun 2025, updated Dez 2025) das umfassendste Review zu Trust, Risk & Security in Multi-Agent Systemen vorgelegt. Führt zwei neue Metriken ein: Component Synergy Score (CSS) für Inter-Agent-Kollaboration und Tool Utilization Efficacy (TUE). — Quelle: arxiv.org/abs/2506.04133

2. **LLMs sind in 84% der Szenarien overconfident.** Eine PMC-Studie (2025) über 9 LLMs und 351 Szenarien zeigt: GPT-Modelle sind in *allen* Szenarien overconfident. Nur GPT-4o zeigt bei 70-100% Confidence halbwegs gute Kalibrierung. Kleinere Modelle überschätzen sich systematisch im 80-100%-Bereich. — Quellen: PMC/12249208, arxiv.org/abs/2502.11028

3. **Bestehende Frameworks (LangChain, AutoGen, CrewAI) haben rudimentäre Trust-Mechanismen.** Agents verifizieren gegenseitig Outputs und cross-checken Entscheidungen. Aber: Kein standardisiertes Trust-Scoring-Protokoll existiert. Es ist eher "Output-Verification" als echtes Reputation-System. — Quelle: arXiv:2506.04133 (Section zu Frameworks)

4. **Calibration-Ansätze: Interrogation und Consistency-Checks.** Zwei Hauptstrategien: (a) MS-FBI (Multi-Step Forensic-Based Interrogation) — LLM wird durch Rückfragen zur Selbstkorrektur gezwungen (MICCAI 2025). (b) Hybrid-Methoden die Confidence + Consistency fusionieren (Vashurin et al. 2025, referenziert in arxiv.org/abs/2510.20460). (c) "Cycles of Thought" — Stabilität von Erklärungen als Confidence-Proxy (arxiv.org/abs/2406.03441). — 3 Quellen

5. **Google Cloud positioniert "Agent Trust" als Schlüsselthema für 2026.** Ihr CTO-Blog (Dez 2025) argumentiert: 2025 war der Shift von Chatbots zu autonomen Agents, und neue Trust-Standards sind die zentrale Herausforderung. Noch kein konkretes Framework, aber strategische Richtung. — Quelle: cloud.google.com/transform/ai-grew-up-and-got-a-job-lessons-from-2025-on-agents-and-trust

---

## Zahlen (verifiziert)

- **84.3%** der LLM-Szenarien zeigen Overconfidence — Quelle: PMC/12249208
- **4 von 9** getesteten LLMs overconfident in *allen* Szenarien — Quelle: PMC/12249208
- **94%** der Agent-Entwickler mit Prod-Agents haben Observability — Quelle: LangChain State of Agent Engineering Report
- **97%** Kostenreduktion bei DevAI-Evaluation durch Agent-as-a-Judge — Quelle: arxiv.org/abs/2508.06225

---

## Wer arbeitet daran?

| Akteur | Typ | Fokus |
|--------|-----|-------|
| Shaina Raza et al. | Akademisch (arXiv) | TRiSM Framework für Agentic AI |
| Vashurin et al. (2025) | Akademisch | Hybrid Uncertainty Estimation |
| MICCAI 2025 / MS-FBI | Akademisch (Medical AI) | Interrogation-basierte Calibration |
| LangChain | Open Source / Startup | Agent Observability & Tracing |
| AutoGen (Microsoft) | Open Source | Multi-Agent Coordination |
| CrewAI | Open Source / Startup | Agent Trust Scores (rudimentär) |
| Google Cloud | Big Tech | Strategic Trust Framework (in Entwicklung) |
| Lyzr Agent Studio | Startup | SafeAI / Responsible AI auf Agent-Level |

---

## Unsicher / Nicht Verifiziert

- Ob CrewAI tatsächlich ein formalisiertes Trust-Scoring hat oder ob das nur im TRiSM-Paper so dargestellt wird — **nicht primärquellenverifiziert** (Weil: nur das Review-Paper als Quelle, nicht CrewAI-Docs direkt)
- Konkreter Stand von Googles Trust-Framework — Blog ist strategisch, keine technischen Details
- Ob es **produktionsreife** Open-Source Trust-Scoring Libraries gibt — **nicht gefunden** (Es gibt IoT-Trust-Modelle und akademische MAS-Reputation-Systeme aus den 2000ern, aber nichts Aktuelles für LLM-Agents spezifisch)

---

## Quellen

1. **arXiv:2506.04133** — "TRiSM for Agentic AI" (Raza et al., Jun-Dez 2025) — Umfassendstes Review zu Trust in Multi-Agent Systems. https://arxiv.org/abs/2506.04133
2. **PMC/12249208** — "Calibration as Measurement of Trustworthiness of LLMs in Biomedical NLP" (Feb 2025) — Quantitative Overconfidence-Daten. https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/
3. **arXiv:2502.11028** — "Mind the Confidence Gap" (Feb 2025) — GPT-4o Calibration vs. kleinere Modelle. https://arxiv.org/abs/2502.11028
4. **arXiv:2510.20460** — "Systematic Evaluation of Uncertainty Estimation Methods in LLMs" (Okt 2025) — Hybrid Confidence+Consistency. https://arxiv.org/abs/2510.20460
5. **arXiv:2508.06225** — "Overconfidence in LLM-as-a-Judge" (Aug 2025) — Calibration-Problem bei Agent-Evaluierung. https://arxiv.org/abs/2508.06225
6. **Google Cloud Blog** — "Lessons from 2025 on agents and trust" (Dez 2025). https://cloud.google.com/transform/ai-grew-up-and-got-a-job-lessons-from-2025-on-agents-and-trust
7. **LangChain** — "State of Agent Engineering" Report. https://www.langchain.com/state-of-agent-engineering

---

## Empfehlung

Das Feld ist **akademisch aktiv aber praktisch unreif** — es gibt kein produktionsreifes, standardisiertes Trust-Scoring für LLM-Agents. Wer jetzt ein pragmatisches Framework baut (Confidence-Calibration + Inter-Agent-Verification + Reputation-Tracking), hat First-Mover-Potential in einem Markt, den Google und LangChain gerade erst strategisch framen.

---

## Beipackzettel

```
Confidence: 65%
Sources checked: 12+
Verified facts: 6
Unverified claims: 3
Search queries used:
  - "multi-agent AI trust scoring framework 2025 2026"
  - "LLM calibration overconfidence confidence estimation 2025 paper"
  - "agent trust reputation system startup open source 2025"
  - "honesty trust multi-agent AI architecture paper arxiv 2025" (rate-limited)
Time spent: ~5 min
Limitations: Brave Search rate-limited (2/4 queries failed), keine memory_search verfügbar.
Begründung Confidence 65%: Akademische Quellen solide (arXiv, PMC), aber Startup/Open-Source-Landschaft nur oberflächlich abgedeckt wegen Rate-Limiting. Framework-Details (CrewAI Trust Scores) nicht primärquellenverifiziert.
```

# Research Brief: Gap Analysis — Trust Signal UX, AI Agent Insurance, Agent Failure Taxonomy

**Datum:** 2026-02-14  
**Typ:** Gap Research für State of AI Agent Trust 2026 Report  
**Risiko-Tier:** 2 (Entscheidungs-Support für Flagship Report)  
**Tag:** [PUBLIC]

---

## Gap 1: Trust Signal UX — Wie zeigt man Trust Scores, damit Menschen sie verstehen?

### Key Findings

1. **"Calibrated Trust" ist der Goldstandard, nicht maximales Vertrauen.** Smashing Magazine (Sep 2025) definiert ein Trust-Spektrum: Active Distrust → Suspicion → Calibrated Trust (ideal) → Over-Trust. Das Ziel ist NICHT, dass User dem AI vertrauen, sondern dass sie RICHTIG einschätzen, wann sie vertrauen können. — Quelle: Smashing Magazine, Sep 2025
2. **Vier psychologische Säulen bestimmen AI-Trust:** Ability (kann es das?), Benevolence (will es mir helfen?), Integrity (ist es fair?), Predictability (kann ich es vorhersagen?). Adaptiert von klassischen interpersonalen Trust-Modellen (Mayer et al.). — Quelle: Smashing Magazine / PMC 10083508
3. **Confidence Visualization ist ein anerkanntes AI Design Pattern.** Progress bars, Farbcodierung, Prozentanzeigen — aiuxdesign.guide dokumentiert es als eigenständiges Pattern mit dem Problem: "Users don't know how much to trust AI predictions, leading to over-reliance." — Quelle: aiuxdesign.guide, Nov 2025
4. **Klare Markensprache erhöht wahrgenommenes Vertrauen um 41%.** UX-Statistiken zeigen: konsistente visuelle Systeme und erkennbare Interfaces verbessern Trust-Wahrnehmung signifikant. — Quelle: Arounda Agency UX Statistics 2026
5. **8,25 Sekunden Aufmerksamkeitsspanne** bedeutet: Trust Signals müssen SOFORT sichtbar sein, nicht nach Scrollen oder Klicken. Visual Hierarchy ist entscheidend. — Quelle: Arounda Agency / SQ Magazine

### Was funktioniert (Evidence aus UX Research)

| Darstellungsform | Wirkung | Evidence |
|---|---|---|
| Farbcodierte Confidence (Grün/Gelb/Rot) | Intuitivstes Format, sofort verständlich | aiuxdesign.guide Pattern Library |
| Prozentanzeige ("85% confident") | Präzise, aber oft missverstanden — User interpretieren 85% als "fast sicher" statt "1 von 7 falsch" | Smashing Magazine |
| Progress Bars | Gut für relative Vergleiche, schlecht für absolute Werte | aiuxdesign.guide |
| Highlighting unsicherer Sätze | Effektiv bei Text-Output — zeigt WO die Unsicherheit liegt, nicht nur DASS sie existiert | Smashing Magazine Empfehlung |
| Erklärende Kontextualisierung | "Weil du oft X liest, empfehle ich Y" — erklärt WARUM, nicht nur WAS | Smashing Magazine |

### Was NICHT funktioniert

- **Nackte Prozentzahlen ohne Kontext:** User haben keine Intuition für Wahrscheinlichkeiten (bekanntes Cognitive Bias Problem)
- **Trust Scores die vom AI selbst kommen (VCE):** Bereits in unseren Briefs belegt — 84% overconfident, adversarial manipulierbar
- **Versteckte Confidence:** Wenn der Score nur in Settings oder Tooltips sichtbar ist, wird er ignoriert

### Blinder Fleck (nicht gefunden)

- **Keine Studie gefunden, die spezifisch testet, wie User AI-Agent Trust Scores interpretieren.** Es gibt UX Research zu Confidence Intervals (IxDF, Maze, NN/g) — aber das behandelt Confidence Intervals als METHODE für UX-Researcher, nicht als UI-ELEMENT für Enduser. Die Frage "Versteht ein Sachbearbeiter, was '73% Confidence' bei einem AI Agent bedeutet?" ist empirisch unbeantwortet.

### Claim Ledger

| Claim | Evidence | Confidence |
|---|---|---|
| Calibrated Trust ist das Designziel | Smashing Magazine, Sep 2025 (Psychological Framework) | High |
| 4-Säulen-Modell (Ability, Benevolence, Integrity, Predictability) | PMC 10083508, adaptiert | High |
| Confidence Visualization ist anerkanntes Pattern | aiuxdesign.guide, Nov 2025 | High |
| 41% Trust-Steigerung durch klare Markensprache | Arounda Agency 2026 (Sekundärquelle, Primärstudie nicht verifiziert) | Medium |
| Sentence-level Highlighting effektiver als globale Scores | Smashing Magazine Empfehlung (kein empirischer Vergleich zitiert) | Low-Medium |
| Keine User-Studie zu AI Agent Trust Score Interpretation existiert | Negative Evidenz (nicht gefunden trotz Suche) | Medium |

### Quellen

1. Smashing Magazine — "The Psychology Of Trust In AI" (Sep 2025) — https://www.smashingmagazine.com/2025/09/psychology-trust-ai-guide-measuring-designing-user-confidence/
2. aiuxdesign.guide — Confidence Visualization Pattern (Nov 2025) — https://www.aiuxdesign.guide/patterns/confidence-visualization
3. Arounda Agency — "45+ UX Statistics: Real 2026 Data" (Nov 2025) — https://arounda.agency/blog/ux-statistics
4. IxDF — "Confidence Intervals and UX Research" (Sep 2025) — https://www.interaction-design.org/literature/article/confidence-intervals-and-ux-research
5. NN/g — "Why Confidence Intervals Matter for UX" — https://www.nngroup.com/videos/confidence-intervals-ux/
6. Maze — "Confidence Intervals in User Research" (Oct 2025) — https://maze.co/blog/confidence-intervals/

---

## Gap 2: AI Agent Insurance Market 2026

### Key Findings

1. **AIUC ist der First-Mover.** $15M Seed (Jul 2025), backed by Nat Friedman (NFDG), Emergence, Terrain. Team: Ex-Anthropic (erste Product-Hire 2022), Thiel Fellow, Ex-McKinsey Partner / Ex-METR COO. Framework AIUC-1 kombiniert NIST AI RMF + EU AI Act + MITRE ATLAS. — Quelle: Fortune, Jul 2025
2. **Munich Re versichert AI seit 2018.** Erstes AI-Performance-Risiko 2018, erstes LLM 2019. Produkt "aiSure" deckt finanzielle Verluste durch AI-Underperformance. Prämien basieren auf "predictive robustness" des AI-Modells — je robuster, desto günstiger. Behandelt Halluzinationen als "error type" analog zu klassischen AI-Fehlern. — Quelle: Computer Weekly / Munich Re
3. **Allianz + Anthropic Partnerschaft (Jan 2026).** Globale Partnerschaft für "responsible AI in insurance." Drei Fokusfelder: Claude-Integration für Entwickler, Agentic AI für Claims Processing, Compliance-Logging. Nicht direkt "Agent Insurance" — sondern Allianz als AI-NUTZER, nicht AI-Versicherer. — Quelle: Reinsurance News, Jan 2026
4. **AIUC-Modell: Standards + Audits + Versicherung als Trifecta.** Analogie: UL Labs (Elektrogeräte-Sicherheit) entstand aus der Insurance-Industrie. AIUC will Agent-Testing + Zertifizierung + Haftungsdeckung bündeln. "Wie Airbags für bessere KFZ-Prämien — sichere AI-Systeme bekommen bessere Rates." — Quelle: Fortune
5. **Markt ist noch EXTREM früh.** Keine verlässlichen Zahlen zur Marktgröße gefunden. Cyber-Insurance als Analogie: $0 → $12B in 15 Jahren. AI Insurance dürfte schneller wachsen (regulatorischer Druck durch EU AI Act Aug 2026 + 99% der Unternehmen hatten AI-Verluste laut EY). — Quelle: Interpretation basierend auf Regulation Brief + Fortune

### Akteure im Überblick

| Akteur | Rolle | Status | Produkt |
|---|---|---|---|
| AIUC | Startup — Standards + Audit + Insurance | $15M Seed, Jul 2025 | AIUC-1 Framework, Agent-spezifische Policen |
| Munich Re | Reinsurer — AI Performance Insurance | Aktiv seit 2018 | aiSure (AI Underperformance Coverage) |
| Allianz | Insurer — AI User + Partner | Anthropic-Partnership Jan 2026 | Noch kein explizites AI-Agent-Insurance-Produkt |
| Armilla AI | Startup — AI Warranty/Guarantee | Aktiv (Details nicht recherchierbar, Rate Limit) | AI Model Warranties |

### Was NICHT abgedeckt wird (Exclusions)

- **Munich Re:** Keine Details zu spezifischen Ausschlüssen gefunden, aber: "requires co-operation and transparency" — keine Deckung ohne Modell-Transparenz
- **AIUC:** Pricing reflektiert Safety-Level — unsichere Systeme bekommen teurere oder keine Policen
- **Generell:** Intentionale Misuse, bekannte Bugs die nicht gefixt werden, regulatorische Strafen (Interpretation — nicht explizit in Quellen)

### Marktgröße-Schätzung

**Nicht gefunden.** Keine belastbare Zahl. Interpretation:
- Cyber Insurance als Proxy: $12B nach 15 Jahren Wachstum
- AI Insurance ist 2026 bei ~Jahr 2-3 (Munich Re seit 2018, aber Agent-spezifisch erst seit 2025)
- AIUC Prediction aus Synthese V2: "$1B ARR bis Q4 2027" (eigene Prediction, 45% Confidence)
- **Unverifiziert.** Marktgröße bleibt ein blinder Fleck.

### Claim Ledger

| Claim | Evidence | Confidence |
|---|---|---|
| AIUC $15M Seed, Jul 2025 | Fortune (primary source, exclusive) | High |
| Munich Re versichert AI seit 2018 | Computer Weekly Interview mit Michael Berger | High |
| Allianz-Anthropic Partnerschaft Jan 2026 | Reinsurance News | High |
| AIUC-1 Framework kombiniert NIST + EU AI Act + ATLAS | Fortune | High |
| Marktgröße AI Insurance >$1B bis 2027 | Eigene Prediction, keine externe Quelle | Low |
| Agent-spezifische Policen existieren bereits | AIUC (Fortune), aber keine Policen-Details öffentlich | Medium |

### Quellen

1. Fortune — "AIUC emerges from stealth with $15M seed" (Jul 2025) — https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/
2. Computer Weekly — "Munich Re sees strong growth in AI insurance" — https://www.computerweekly.com/news/366586014/Munich-Re-sees-strong-growth-in-AI-insurance
3. Munich Re — aiSure Product Page — https://www.munichre.com/en/solutions/for-industry-clients/insure-ai.html
4. Reinsurance News — "Allianz partners with Anthropic" (Jan 2026) — https://www.reinsurancene.ws/allianz-partners-with-anthropic-to-accelerate-adoption-of-responsible-ai/
5. Munich Re — "The new frontier of underwriting AI risk" — https://www.munichre.com/en/insights/cyber/the-new-frontier-of-underwriting-ai-risk.html
6. ITIJ — "AI, cyber, and climate risks to dominate insurance agenda in 2026" (Jan 2026) — https://www.itij.com/latest/news/ai-cyber-and-climate-risks-dominate-insurance-agenda-2026-says-globaldata

---

## Gap 3: Agent Failure Taxonomy — Standardisierte Klassifikation von Agent-Fehlern

### Key Findings

1. **Microsoft hat im April 2025 die erste umfassende Agentic AI Failure Taxonomy veröffentlicht.** Whitepaper der Microsoft AI Red Team. Zwei Achsen: Safety vs. Security, Novel vs. Existing. Novel = nur bei Agents (z.B. Multi-Agent-Kommunikationsfehler). Existing = bekannt aber bei Agents schlimmer (Halluzination, Bias). Enthält Mitigations pro Kategorie. — Quelle: Microsoft Security Blog, Apr 2025
2. **Memory Poisoning ist laut Microsoft "particularly insidious."** Die Taxonomy hebt hervor: Fehlende semantische Analyse + kontextuelle Validierung erlaubt, dass bösartige Instruktionen gespeichert, abgerufen und ausgeführt werden. — Quelle: Microsoft Whitepaper
3. **Cibench-Benchmark zeigt ~50% Failure Rate bei AI Agents.** 34 Tasks, drei Frameworks evaluiert. Drei-Stufen-Taxonomie: Planning Errors → Execution Issues → Response Generation Failures. Selbst GPT-4o und MetaGPT scheitern bei komplexen Tasks. — Quelle: Quantum Zeitgeist / CUHK+SMU Research, Aug 2025
4. **Erste Survey zu Agent-Halluzinationen (arxiv 2509.18970).** Taxonomie nach Workflow-Phase: Halluzinationen bei Perception, Reasoning, Action, Memory. 18 Triggering Causes identifiziert. — Quelle: Chinese Academy of Sciences et al., Sep 2025
5. **Multi-Agent-spezifische Failure: Coordination Failure → Silent Hallucinations.** Galileo AI dokumentiert: Fehler in einem Agent "korruptieren stillschweigend den State anderer Agents" — im Gegensatz zu monolithischen Systemen, wo Fehler Exceptions auslösen. Healthcare-Beispiel: Kardiale Marker korrekt erkannt, aber durch Koordinationsfehler nie an Empfehlungs-Agent weitergeleitet. — Quelle: Galileo AI, Jul 2025

### Konsolidierte Agent Failure Taxonomy (Synthese aus allen Quellen)

**Basierend auf Microsoft, Cibench, arxiv Survey, Galileo, und unseren eigenen Briefs:**

| Failure Mode | Beschreibung | Quelle | Schwere |
|---|---|---|---|
| **1. Hallucination** | Konfident falsche Fakten generieren | arxiv 2509.18970, alle Briefs | Hoch |
| **2. Wrong Action** | Richtiges Reasoning, falsches Tool/API-Call | Cibench (Execution Issues) | Hoch |
| **3. Planning Error** | Falscher Task-Decomposition oder -Sequenzierung | Cibench (3-Tier Taxonomy) | Mittel-Hoch |
| **4. Compounding Error** | Fehler in Schritt N propagiert durch Schritte N+1...N+k | Galileo (Silent Corruption), eigene Briefs | Kritisch |
| **5. Coordination Failure** | Multi-Agent: Information geht zwischen Agents verloren | Galileo, Microsoft (Novel) | Hoch |
| **6. Memory Poisoning** | Persistente falsche Erinnerungen verzerren zukünftige Outputs | Microsoft Whitepaper, eigene Memory-Brief | Kritisch |
| **7. Deception/Manipulation** | Agent produziert irreführende Outputs (nicht Halluzination — intentional wirkend) | ISACA 2025, eigene Adversarial-Brief | Hoch |
| **8. Omission** | Agent lässt relevante Information aus (nicht falsch, aber unvollständig) | Nicht explizit in gefundenen Taxonomien — eigene Kategorie | Mittel |
| **9. Goal Drift** | Agent weicht über Zeit vom ursprünglichen Ziel ab | arxiv 2505.10468 (Brittleness, Emergent Behavior) | Mittel |
| **10. Overconfidence** | Agent meldet hohe Confidence bei falschem Output | Eigene Briefs (84%, VCE bias) | Hoch |

### Was standardisiert ist vs. was fehlt

**Standardisiert:**
- Microsoft Taxonomy (Apr 2025) — breiteste Coverage, aber Security-fokussiert
- OWASP Top 10 for LLM Applications — LLM-Fehler (nicht Agent-spezifisch)
- MITRE ATLAS — Adversarial ML (nicht Agent-spezifisch)
- Cibench 3-Tier — Planning/Execution/Response (empirisch, aber nur Coding-Tasks)

**NICHT standardisiert (Lücken):**
- Keine einheitliche Severity-Skala über Taxonomien hinweg
- Keine Taxonomie adressiert Overconfidence als eigenständigen Failure Mode (obwohl empirisch der häufigste)
- Omission und Goal Drift sind in keiner gefundenen Taxonomie als eigene Kategorien
- Keine Taxonomie verbindet Failure Mode → Business Impact → Mitigation Cost (ökonomische Dimension fehlt komplett)

### Claim Ledger

| Claim | Evidence | Confidence |
|---|---|---|
| Microsoft veröffentlichte Agentic AI Failure Taxonomy Apr 2025 | Microsoft Security Blog + Whitepaper PDF | High |
| ~50% Failure Rate bei AI Agents (Cibench) | Quantum Zeitgeist / CUHK+SMU Research | High |
| Memory Poisoning = "particularly insidious" | Microsoft Whitepaper (direct quote) | High |
| Coordination Failure → Silent Corruption in Multi-Agent | Galileo AI Blog (Jul 2025) | Medium (single source, but plausible) |
| 18 Triggering Causes für Agent Hallucinations | arxiv 2509.18970 | High (peer review unclear, but comprehensive) |
| Keine einheitliche Severity-Skala existiert | Negative Evidenz | Medium |
| Overconfidence fehlt als eigener Failure Mode in allen Taxonomien | Überprüfung von Microsoft, Cibench, arxiv | High |

### Quellen

1. Microsoft Security Blog — "Taxonomy of Failure Modes in AI Agents" (Apr 2025) — https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/
2. Microsoft Whitepaper PDF — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf
3. Quantum Zeitgeist / Cibench Research — "AI Agents Fail Half The Time" (Aug 2025) — https://quantumzeitgeist.com/ai-agents-fail-half-the-time-new-benchmark-reveals-weaknesses/
4. arxiv 2509.18970 — "LLM-based Agents Suffer from Hallucinations: A Survey" (Sep 2025) — https://arxiv.org/html/2509.18970v1
5. Galileo AI — "Multi-Agent AI Gone Wrong" (Jul 2025) — https://galileo.ai/blog/multi-agent-coordination-failure-mitigation
6. arxiv 2505.10468 — "AI Agents vs. Agentic AI: Conceptual Taxonomy" (May 2025) — https://arxiv.org/pdf/2505.10468
7. ISACA — "Avoiding AI Pitfalls in 2026" (Dec 2025) — https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2025/avoiding-ai-pitfalls-in-2026-lessons-learned-from-top-2025-incidents

---

## Contradiction Register

| Konflikt | Quellen | Erklärung | Impact |
|---|---|---|---|
| Microsoft Taxonomy ist Security-fokussiert vs. Cibench ist Performance-fokussiert | Microsoft vs. CUHK/SMU | Verschiedene Perspektiven: Security fragt "wie kann es angegriffen werden?", Performance fragt "wo versagt es funktional?" | Hoch — ein vollständiger Report braucht BEIDE Perspektiven |
| Munich Re "insures AI since 2018" vs. AIUC "first agent-specific insurance" | Computer Weekly vs. Fortune | Kein echter Widerspruch: Munich Re versichert AI-Performance allgemein, AIUC ist Agent-SPEZIFISCH (autonome Systeme). Verschiedene Kategorien. | Mittel |
| Confidence Visualization als "anerkanntes Pattern" vs. "keine User-Studie zu Agent Trust Scores" | aiuxdesign.guide vs. eigene Recherche | Pattern existiert als EMPFEHLUNG, aber empirische Validation für Agent-Kontext fehlt | Hoch — das Pattern wird möglicherweise falsch angewandt |

---

## Empfehlung

Die drei Gaps liefern starkes Material für den Flagship Report:

1. **Trust Signal UX:** Der stärkste Insight ist die LÜCKE — niemand hat empirisch getestet, wie Menschen AI-Agent Trust Scores interpretieren. Das ist ein "Call to Action" im Report.
2. **AI Agent Insurance:** AIUC + Munich Re + Allianz/Anthropic bilden ein klares Narrativ: Insurance ist der "unsichtbare Regulierer" der Agent-Industrie (bestätigt Prediction 1 der Synthese V2).
3. **Agent Failure Taxonomy:** Microsoft's Whitepaper (Apr 2025) ist die autoritative Quelle, aber Overconfidence als eigenständiger Failure Mode fehlt überall — das ist unsere differenzierende Perspektive.

---

## Beipackzettel

```
Confidence: 65%
Sources checked: 18
Verified facts: 14
Unverified claims: 4 (Marktgröße AI Insurance, 41% Trust-Steigerung Primärstudie, Omission/Drift als Lücke in ALLEN Taxonomien, Armilla AI Details)
Search queries used: 7 (3 initial parallel + 4 follow-up, 3 rate-limited)
Time spent: ~25 min
```

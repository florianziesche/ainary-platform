# Research Report 04: Reasoning in AI Agents
## Systematic Analysis of 86 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/capability-papers/reasoning.md*

---

## Executive Summary (BLUF)

**86 Papers spanning Jan 2022 – Jan 2026. 6 Kernerkenntnisse:**

1. **CoT hilft NUR bei Math/Logik.** Meta-Analyse über 100+ Papers (Sep 2024): CoT bringt starke Gains bei Math/Symbolic Reasoning, aber fast nichts bei anderen Tasks. MMLU: mit/ohne CoT → identische Accuracy, außer bei Gleichungszeichen.
2. **"Thinking harder" > "Thinking longer."** o3-mini(m) schlägt o1-mini OHNE längere Reasoning-Chains. Bessere Modelle denken EFFIZIENTER, nicht LÄNGER.
3. **Test-Time Scaling hat Grenzen.** Bei Knowledge-Intensive Tasks: mehr Compute = MEHR Halluzinationen + Confirmation Bias. Keine universelle Scaling Law.
4. **LRMs > LLMs bei Planning, LLMs > LRMs bei Execution.** LaRMA Framework (Mar 2025): Reasoning-Modelle (DeepSeek-R1) übertreffen bei Plan Design, aber Standard-LLMs (Claude) sind besser bei Tool Usage/Execution. Hybrid = optimal.
5. **Zero-Data Self-Play Reasoning funktioniert.** Absolute Zero: RL Self-play OHNE externe Daten produziert State-of-the-Art Reasoner. Agent0-Prinzip auf Reasoning angewendet.
6. **Long-Horizon Execution ist DAS ungelöste Problem.** 1M-Step Tasks jetzt mit Zero Errors lösbar — aber nur durch rekursive Dekomposition. Native long-horizon Reasoning bleibt fragil.

---

## Taxonomie: 6 Cluster

### Cluster 1: Foundations — The Reasoning Paradigm (2022-2023, 8 Papers)

#### [E] Chain-of-Thought Prompting (Jan 2022, Google) — THE Paper
*Wei et al. | arXiv:2201.11903*
- Intermediate Reasoning Steps → emergent bei >100B Parameter Modellen
- 8 CoT Demonstrations → 540B PaLM erreicht GSM8K SotA
- **[J] Alles was folgt baut hierauf.** CoT ist die Urknall-Idee für LLM Reasoning.

#### [E] Self-Consistency (Mar 2022)
*Wang et al. | arXiv:2203.11171*
- Sample multiple Reasoning Paths → Majority Vote auf Antworten
- Ersetzt "greedy decoding" durch "sample and marginalize"
- **[I] Erste Form von Test-Time Scaling: mehr Compute bei Inference = bessere Antworten.**

#### [E] Least-to-Most Prompting (May 2022)
*arXiv:2205.10625*
- Problem-Dekomposition: Komplexes Problem → einfachere Subprobleme → löse sequentiell
- **[I] Die Grundidee hinter hierarchischem Reasoning und rekursiver Dekomposition.**

#### [E] ReAct (Oct 2022) — Reasoning + Acting vereint
*Yao et al. | arXiv:2210.03629*
- INTERLEAVED Reasoning Traces + Task-Specific Actions
- Reasoning → induziert/trackt/updated Action Plans + handelt Exceptions
- Actions → liefert externe Information (Knowledge Bases, Environments)
- **[J] Paradigm-Defining.** ReAct = die Architektur die 90% aller aktuellen Agent-Frameworks nutzen.

#### [E] Tree of Thoughts (May 2023)
*Yao et al. | arXiv:2305.10601*
- Generalisierung von CoT: Multiple Thought-Branches + Search + Backtracking
- LLM evaluiert eigene Thoughts (Self-Evaluation als Heuristic für Search)
- **[I] CoT = linear. ToT = branching. GoT (Graph) = beliebige Topologie.** Die Reasoning-Topologie-Leiter.

#### [E] LATS: Language Agent Tree Search (Oct 2023)
*arXiv:2310.04406*
- MCTS (Monte Carlo Tree Search) + LLM: Unified Reasoning + Acting + Planning
- LM-powered Value Functions + Self-Reflections
- **[J] Die Verbindung von AlphaGo-Methodik mit LLM Agents.** Search-basiertes Reasoning.

#### [E] ExpeL: Experiential Learners (Aug 2023)
*arXiv:2308.10144*
- Agents lernen aus ERFAHRUNG: Success/Failure → extrahiere Insights → speichere als Rules
- **[I] Vorwegnahme von SkillRL und Shared Memories (CRMWeaver).**

#### [E] LAW: Language, Agent, World Models (Dec 2023)
*arXiv:2312.05230*
- Unified Framework: Language Model (knowledge) + Agent Model (actions) + World Model (predictions)
- **[I] Theoretisch elegant. In der Praxis dominiert ReAct + Tool Use weiterhin.**

---

### Cluster 2: The CoT Reality Check (2024, 12 Papers)

#### 🔥🔥🔥 [E] "To CoT or not to CoT?" (Sep 2024)
*Sprague et al. | arXiv:2409.12183*
- **Meta-Analyse: 100+ Papers + eigene Evaluation auf 20 Datasets, 14 Modelle**
- **ERGEBNIS: CoT hilft PRIMÄR bei Math + Symbolic Reasoning. Geringe Gains bei allem anderen.**
- MMLU: CoT = identische Accuracy OHNE CoT, außer Fragen mit "=" Zeichen
- **[E] Zitat: "Directly generating the answer without CoT leads to almost identical accuracy as CoT"**
- **[J] DAS kontraintuitive Paper der Collection.** Widerspricht der Community-Annahme dass CoT universell hilft. Implikation: Für Enterprise-Tasks (die selten "pure math" sind) ist CoT OVERHEAD ohne Benefit.

#### [E] Self-Discover (Feb 2024, Google DeepMind)
*arXiv:2402.03620*
- LLM COMPOSIERT eigene Reasoning-Strukturen aus atomaren Modulen
- Stage 1: Select → Adapt → Implement → Stage 2: Execute
- **[I] Meta-Reasoning: Das Modell entscheidet nicht nur WAS es denkt, sondern WIE es denkt.**

#### [E] Visualization-of-Thought (Apr 2024)
*arXiv:2404.03622*
- Spatial Reasoning via "Mind's Eye": LLM visualisiert mental
- **[I] Nische, aber relevant für Multimodal Reasoning (Diagramme, Layouts)**

#### [E] Grokked Transformers as Implicit Reasoners (Jun 2024)
*arXiv:2405.15071*
- Transformers lernen IMPLIZITES Reasoning durch Extended Training (Grokking)
- **[I] Reasoning muss nicht EXPLIZIT sein (CoT). Kann in Weights encoded sein.**

#### [E] From Explicit to Implicit CoT (Jun 2024)
*arXiv:2405.14838*
- Training: Schrittweise CoT-Steps internalisieren (erst explizit, dann wegkürzen)
- **[I] Kompression: Explicit CoT = Training Wheels. Implicit CoT = das Ziel.**

#### [E] Mutual Reasoning (Aug 2024)
*arXiv:2408.06195*
- Zwei kleinere LLMs in Dialog-basiertem Reasoning > ein großes LLM
- **[I] Multi-Agent Reasoning als Alternative zu größeren Modellen.**

#### [E] Code in Pre-training improves Reasoning (Aug 2024)
*arXiv:2408.10914*
- Models pre-trained WITH code reason besser, auch bei non-code Tasks
- **[I] Code als "Reasoning Gymnasium" — strukturiertes Denken durch Code-Exposure.**

#### [E] Iteration of Thought (Sep 2024)
*arXiv:2409.12618*
- Inner Dialogue: Agent stellt sich selbst Fragen (Prompts) und beantwortet sie
- Adaptive: Entscheidet dynamisch wann genug Iterationen durchlaufen sind

#### [E] MAgICoRe: Multi-Agent Coarse-to-Fine Refinement (Sep 2024)
*arXiv:2409.12147*
- Multi-Agent Reasoning mit iterativer Verfeinerung
- Coarse → Fine: Erst grobe Lösung, dann schrittweise Verbesserung

---

### Cluster 3: Test-Time Compute Scaling — The 2025 Obsession (22 Papers)

#### 📖 [E] Test-time Computing Survey (Jan 2025)
*arXiv:2501.02497*
- System-1 (Intuitive) vs System-2 (Deliberate) Reasoning
- System-1 TTS: Parameter updating, input modification, output calibration
- System-2 TTS: Repeated sampling, self-correction, tree search, verification
- **[J] Die definitive Taxonomie für Test-Time Scaling.**

#### [E] Meta Chain-of-Thought (Jan 2025)
*Xiang, Snell et al. | arXiv:2501.04682*
- System 2 Reasoning: "Learning HOW to think" statt nur "thinking step by step"
- Meta-CoT: Reasoning über den Reasoning-Prozess selbst
- **[I] Analog zu SMART (Tool Use): Metacognition als nächste Abstraktionsebene.**

#### 📖 [E] Test-Time Scaling Survey: What, How, Where, How Well? (Mar 2025)
*arXiv:2503.24235*
- Umfassendste Survey zu TTS
- What: Mehr Compute bei Inference
- How: Sampling, Search, Verification, Refinement
- Where: Math, Code, Planning, QA
- How Well: Depends heavily on task type

#### 📖 [E] Inference-Time Scaling for Complex Tasks (Apr 2025, Microsoft)
*arXiv:2504.00294*
- Where We Stand: TTS funktioniert für Math/Code
- What Lies Ahead: Open Problems bei real-world complex tasks

#### 📖 [E] DeepSeek-R1 Thoughtology (Apr 2025)
*arXiv:2504.07128*
- **Empirische Analyse von R1's "Thinking" Patterns**
- Identifiziert: Planning Tokens, Verification Tokens, Backtracking Tokens, Exploration Tokens
- **[I] Erste Anatomie eines Reasoning-Modell-Gehirns. Zeigt WAS in den Thinking-Tokens passiert.**

#### 🔥🔥 [E] "Reasoning Models Can Be Effective Without Thinking" (Apr 2025)
*arXiv:2504.09858*
- **DeepSeek-R1 OHNE Thinking-Phase (via Prompting) = "NoThinking"**
- **NoThinking OUTPERFORMS Thinking bei gleichem Token-Budget auf 7 Datasets**
- Bei 700 Tokens: NoThinking 51.3 vs Thinking 28.9 auf ACM 2023
- **[E] "When controlling for number of tokens, NoThinking outperforms Thinking"**
- **[J] BOMBSHELL. Die gesamte Reasoning-Model-Industrie basiert auf der Annahme dass explizites Denken hilft. Dieses Paper zeigt: Bei begrenztem Budget ist DIREKTES Antworten besser. Thinking ist nur dann besser wenn unbegrenztes Budget.**

#### [E] o3(mini) Thinks Harder, Not Longer (Feb 2025)
*arXiv:2502.15631*
- o3-mini(m) vs o1-mini auf Omni-MATH
- o3-mini: Bessere Accuracy OHNE längere Reasoning Chains
- **[E] "Superior accuracy without requiring longer reasoning chains"**
- **[J] Reasoning-Effizienz > Reasoning-Länge. Bestätigt "NoThinking" indirekt: Qualität der Gedanken zählt, nicht Quantität.**

#### 📖 [E] Slow Thinking Survey (May 2025)
*arXiv:2505.02665*
- RL + Inference-Time Scaling für "Slow Thinking" LLMs
- Systematische Übersicht über alle Ansätze

#### [E] Absolute Zero: Self-play Reasoning with Zero Data (May 2025)
*arXiv:2505.03335*
- **RL Self-play OHNE jegliche externe Daten**
- Modell generiert eigene Tasks UND lernt sie zu lösen
- State-of-the-Art auf Reasoning Benchmarks
- **[J] Analog zu Agent0 (Tool Use): Self-play als universelles Training-Paradigma. Keine menschlichen Daten nötig.**

#### [E] Scaling Test-time Compute for Agents (Jun 2025)
*arXiv:2506.12928*
- Test-Time Scaling spezifisch für AGENTS (nicht nur Reasoning-Tasks)
- **[I] Brücke zwischen Reasoning-TTS und Agentic-TTS: Agent braucht mehr Compute nicht nur zum Denken, sondern auch zum Interagieren.**

#### [E] Thinking vs. Doing (Jun 2025)
*arXiv:2506.07976*
- Agents die "Test-Time Interaction" skalieren (mehr INTERAGIEREN) vs mehr DENKEN
- **[J] Die fundamentale Frage: Soll der Agent länger nachdenken oder öfter ausprobieren? Antwort: Depends on task.**

#### 🔥 [E] Test-Time Scaling NOT Effective for Knowledge-Intensive Tasks (Sep 2025)
*arXiv:2509.06861*
- **14 Reasoning Models, 2 Knowledge-Intensive Benchmarks**
- **Mehr Compute = MEHR Halluzinationen**
- Extended Reasoning → Confirmation Bias → overconfident hallucinations
- **[E] "Increasing test-time computation does not consistently improve accuracy and often increases hallucinations"**
- **[J] DIE Grenze von Test-Time Scaling.** Für Reasoning über BEKANNTES Wissen: ja. Für Abruf von UNBEKANNTEM Wissen: nein, sogar kontraproduktiv. RAG ist die Lösung, nicht mehr Thinking.

#### [E] The Art of Scaling TTS (Dec 2025)
*arXiv:2512.02008*
- Erste Large-Scale Study: 30B+ Tokens, 8 LLMs, 4 Datasets
- **Ergebnis: (1) Keine universelle TTS-Strategie dominiert. (2) Reasoning Models verhalten sich anders als Standard-LLMs. (3) TTS-Effectiveness hängt stark von Problem-Difficulty ab.**
- **[J] Keine Silver Bullet. TTS-Strategie muss per Task + Modell gewählt werden.**

---

### Cluster 4: Long-Horizon & Multi-Step Reasoning (8 Papers)

#### 🔥 [E] Solving a Million-Step LLM Task with Zero Errors (Nov 2025)
*arXiv:2511.09030*
- **1M Steps, 0 Errors** — Towers of Hanoi (bisher max ~100 Steps möglich)
- Methode: Rekursive Dekomposition + formale Verifikation jedes Sub-Steps
- **[I] Nicht "das LLM denkt 1M Steps" sondern "das LLM zerlegt in Sub-Problems die es verifiziert lösen kann."**
- **[J] Long-Horizon Reasoning ≠ Linear Scaling. Es braucht HIERARCHISCHE Dekomposition.**

#### [E] Illusion of Diminishing Returns (Sep 2025)
*arXiv:2509.09677*
- **Marginal gains in single-step accuracy → EXPONENTIAL improvements in long-horizon tasks**
- Short-task Benchmarks UNTERSCHÄTZEN den Fortschritt
- Failures sind EXECUTION-Fehler, nicht REASONING-Fehler
- **[J] Extrem wichtig für die Narrative: "LLMs werden nicht besser" ist FALSCH. Kleine Accuracy-Gains kompoundieren exponentiell bei Multi-Step-Tasks.**

#### [E] MARPLE: Long-Horizon Inference (Oct 2024)
*arXiv:2410.01926*
- Benchmark für Long-Horizon Reasoning: Multi-Step, Multi-Clue
- **[I] Tests ob Agent über 10+ Steps konsistentes Reasoning durchhält.**

#### [E] Laser: Structured Protocol for Long-Horizon Agent Search (Dec 2025)
*arXiv:2512.20458*
- Context Register: Strukturierte Zustandsverwaltung über lange Reasoning-Chains
- **[I] Löst das "Kontextverlust bei langem Reasoning" Problem durch explizites State-Management.**

#### [E] Recursive Language Models (Dec 2025)
*arXiv:2512.24601*
- Recursive statt sequentielles Processing
- **[I] Analog zu rekursiver Dekomposition (1M-Step Paper): Modell ruft sich SELBST rekursiv auf.**

---

### Cluster 5: Self-Evolving Reasoning (10 Papers)

#### [E] DEBATE, TRAIN, EVOLVE (May 2025)
*arXiv:2505.15734*
- Self-Evolution of Reasoning: Multi-Agent Debate → Training Data → RL
- **[I] Self-play in Multi-Agent Setting für Reasoning-Improvement.**

#### [E] Revisiting Multi-Agent Debate as TTS (May 2025)
*arXiv:2505.22960*
- Systematic Study: WANN hilft Multi-Agent Debate?
- Ergebnis: Conditional Effectiveness — nicht universell besser

#### [E] Deep Self-Evolving Reasoning (Oct 2025)
*arXiv:2510.17498*
- Agents die ihren Reasoning-Prozess iterativ verbessern

#### [E] OpenSIR: Open-Ended Self-Improving Reasoner (Nov 2025)
*arXiv:2511.00602*
- Open-Ended: Nicht auf Fixed Tasks beschränkt, sondern generalisierend

#### [E] Self-Improving LLM Agents at Test-Time (Oct 2025)
*arXiv:2510.07841*
- Self-Improvement OHNE Training — rein zur Inference-Zeit
- **[I] JitRL-Vorläufer: Adaptation ohne Gradient Updates.**

#### [E] JitRL: Just-In-Time Reinforcement Learning (Jan 2026)
*arXiv:2601.18510*
- **Training-free framework für Test-Time Policy Optimization**
- Dynamic non-parametric Memory + Retrieved Trajectories → Advantage Estimation
- Logit-Modulation der LLM-Outputs basierend auf Advantages
- **[J] Elegante Lösung für das "frozen weights after deployment" Problem. Agent wird besser OHNE Retraining.**

---

### Cluster 6: Agentic Reasoning — The New Frontier (12 Papers)

#### [E] LaRMA: LRMs vs LLMs in Agent Scenarios (Mar 2025)
*arXiv:2503.11074*
- **9 Tasks: Tool Usage, Plan Design, Problem Solving**
- **KEY FINDINGS:**
  - LRMs (DeepSeek-R1) > LLMs bei Plan Design (iterative reflection)
  - LLMs (Claude) > LRMs bei Tool Usage (efficiency)
  - Hybrid: Beste Performance
  - Excessive Reasoning = performance degradation bei einfachen Tasks
- **[J] Die praktischste Einsicht der Collection.** Nicht "Reasoning-Modell für alles" sondern "richtiges Modell für richtigen Task."**

#### [E] AI Metacognition (Nov 2024, Bengio et al.)
*arXiv:2411.02478*
- Authors: Bengio, Chater, Gerstenberg, Mitchell, Rahwan, Schölkopf, Tenenbaum
- "Wise machines" brauchen Metacognition: Wissen was sie wissen + Wissen was sie NICHT wissen
- **[J] Authority Paper. Metacognition = der rote Faden durch SMART (Tool Use), Abstention (Safety), und JitRL (Reasoning).**

#### 📖 [E] Agentic Reasoning Survey (Jan 2026)
*arXiv:2601.12538*
- Umfassende Survey: Agentic Reasoning als eigenständiges Paradigma
- Reasoning IN Agents ≠ Reasoning OF LLMs

#### [E] MAXS: Meta-Adaptive Exploration (Jan 2026)
*arXiv:2601.09259*
- LLM Agents mit meta-adaptiver Exploration
- **[I] Agent wählt Exploration-Strategie basierend auf bisherigen Erfahrungen.**

#### [E] Universe of Thoughts (Nov 2025)
*arXiv:2511.20471*
- Creative Reasoning: Nicht nur logisch, sondern kreativ
- **[I] Nische, aber relevant für Ideation/Brainstorming-Agents.**

#### [E] Model-First Reasoning (Dec 2025)
*arXiv:2512.14474*
- Explicit Problem Modeling VOR Reasoning reduziert Halluzinationen
- **[I] Erst das Problem formalisieren, dann lösen. Analog zu "Semantic Data Products" (Ontologie-Post).**

---

## Synthese: 7 technische Erkenntnisse

### 1. Die Reasoning-Topologie

```
CoT (2022)          → Linear, sequentiell
  ↓
Self-Consistency     → Parallel Sampling + Voting
  ↓
ToT (2023)          → Branching + Backtracking
  ↓
GoT                 → Arbitrary Graph Topologie
  ↓
LATS                → MCTS (Search-basiert)
  ↓
Self-Discover       → Meta: LLM WÄHLT Reasoning-Struktur
  ↓
Recursive (2025)    → Rekursive Dekomposition
  ↓
Agentic (2026)      → Reasoning + Acting + Tools interleaved
```

**[J] Jede Stufe ist NICHT "besser" als die vorherige.** Sie ist für verschiedene Problemtypen optimal (analog zur RAG-Topologie-These):

| Problemtyp | Optimale Reasoning-Topologie |
|---|---|
| Einfache Fragen | Direct Answer (kein CoT!) |
| Math/Logik | CoT + Self-Consistency |
| Exploration/Search | ToT / LATS |
| Multi-Step Complex | Recursive Decomposition |
| Knowledge-Intensive | RAG (NICHT mehr Thinking!) |
| Real-World Agent Tasks | Agentic (Reasoning + Acting interleaved) |

### 2. CoT: Overrated für Enterprise

"To CoT or not to CoT?" zeigt klar: CoT hilft bei Math + Symbolic. Enterprise Tasks (CRM, ERP, Document Review, Process Automation) sind selten "pure math." Sie sind:
- Knowledge retrieval (wo CoT kontraproduktiv ist)
- Multi-system coordination (wo Tool Use > Reasoning)
- Policy compliance (wo deterministische Checks > probabilistisches Reasoning)

**[J] Implikation:** Für Enterprise Agent Deployments → WENIGER CoT, MEHR Tool Use, MEHR deterministische Guards.

### 3. Thinking Harder > Thinking Longer

| Model Comparison | Thinking Length | Performance |
|---|---|---|
| o1-mini | Lange Chains | Baseline |
| o3-mini(m) | KÜRZERE Chains | BESSER als o1 |
| R1 mit NoThinking | Keine Thinking Phase | BESSER bei Token-Budget <700 |

**[J] Die nächste Generation von Reasoning Models wird nicht LÄNGER denken. Sie wird BESSER denken in KÜRZERER Zeit.** Effizienz ist der neue Differentiator, nicht Compute.

### 4. Test-Time Scaling: Grenzen und Gefahren

| Task Type | TTS Effective? | Risk |
|---|---|---|
| Math/Symbolic | ✅ Ja, consistent | Diminishing returns at scale |
| Code | ✅ Ja | Cost-intensive |
| Planning | ✅ Ja (mit LRMs) | Over-reasoning möglich |
| Knowledge-Intensive | ❌ NEIN | Mehr Compute = MEHR Halluzinationen |
| Open-Ended | ❓ Depends | Confirmation Bias |

**[J] TTS ist kein Free Lunch.** Es ist ein Tool das bei math-like Tasks hilft und bei knowledge-Tasks SCHADET. Für Enterprise Agents (primär knowledge-basiert): RAG + Tool Use > Test-Time Scaling.

### 5. The Execution Gap

"Illusion of Diminishing Returns" (2509.09677) macht eine kritische Beobachtung:
- LLMs scheitern bei langen Tasks nicht weil sie NICHT REASONING können
- Sie scheitern weil sie EXECUTION-Fehler machen (falsche Tool-Aufrufe, State-Verlust, Typos)
- Kleine Verbesserungen in per-step Accuracy → EXPONENTIELLE Verbesserung in Long-Horizon Success

**Mathematisch:** Wenn per-step accuracy = p, dann n-step success = p^n.
- p = 0.95, n = 100: 0.95^100 = 0.6%
- p = 0.99, n = 100: 0.99^100 = 36.6%
- p = 0.999, n = 100: 0.999^100 = 90.5%

**[J] 4 Prozentpunkte Verbesserung (0.95 → 0.99) = 60x besser bei 100-Step-Tasks.** Das erklärt warum Benchmarks "Diminishing Returns" zeigen (single-step) während reale Agent-Performance exponentiell besser wird.

### 6. The LRM/LLM Split

LaRMA (2503.11074) definiert die Arbeitsteilung:

```
LRMs (DeepSeek-R1, o3, etc.)     LLMs (Claude, GPT-4o, etc.)
├── Plan Design ✅                 ├── Plan Design ❌ (weniger reflektiv)
├── Problem Solving ✅             ├── Problem Solving ❌
├── Tool Usage ❌ (ineffizient!)   ├── Tool Usage ✅ (effizient!)
├── Execution ❌ (over-reasons)    ├── Execution ✅ (pragmatisch)
└── Excessive Thinking = Degradation └── Direct Action = Efficiency
```

**[J] Architektur-Implikation:**
```
User Query → Router
              ├── Reasoning-Heavy? → LRM (R1, o3)
              └── Execution-Heavy? → LLM (Claude, GPT-4o)
```

### 7. Self-Evolving Reasoning = The Next Paradigm

Agent0 (Tool Use) + Absolute Zero (Reasoning) + SKILLRL (Skills) + JitRL (Test-Time) = konvergente Evidenz:

**Agents können sich SELBST verbessern, ohne menschliche Daten, ohne Retraining, zur Inference-Zeit.**

Das ist nicht Science Fiction — es ist Stand der Forschung Q4 2025/Q1 2026. Die Frage ist nicht mehr OB, sondern WIE SCHNELL und WIE SICHER.

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **"To CoT or not to CoT?"** (2409.12183) | Meta-Analyse über 100 Papers. CoT = overrated für non-math. |
| 2 | **"NoThinking"** (2504.09858) | Reasoning Models ohne Thinking > mit Thinking bei gleichem Budget. Paradigm-Challenger. |
| 3 | **"Illusion of Diminishing Returns"** (2509.09677) | Single-step gains → exponential long-horizon improvements. Reframing. |
| 4 | **LaRMA** (2503.11074) | LRMs > LLMs bei Planning, LLMs > LRMs bei Execution. Hybrid = optimal. |
| 5 | **TTS Not Effective for Knowledge** (2509.06861) | Mehr Compute = mehr Halluzinationen bei Knowledge Tasks. Anti-hype. |
| 6 | **Absolute Zero** (2505.03335) | Zero-data self-play reasoning. No human data needed. |
| 7 | **1M-Step Zero Errors** (2511.09030) | Recursive decomposition → million-scale execution. |
| 8 | **AI Metacognition** (2411.02478) | Bengio et al. Wise machines = knowing what you don't know. |
| 9 | **JitRL** (2601.18510) | Training-free test-time policy optimization. Elegant. |
| 10 | **o3 Thinks Harder not Longer** (2502.15631) | Efficiency > Length for reasoning. |

---

## Open Problems

1. **When to Reason, When to Act?** Kein robuster Mechanismus der entscheidet ob ein Agent denken oder handeln soll.
2. **TTS Budget Allocation:** Wie viel Compute für Thinking vs. Tool Use vs. Interaction?
3. **Knowledge-Intensive Reasoning:** TTS schadet hier. RAG hilft. Aber RAG + Reasoning Integration ist untererforscht.
4. **Long-Horizon State Management:** 1M Steps geht nur mit rekursiver Dekomposition. Native long-horizon = ungelöst.
5. **Self-Evolving Safety:** Wenn Agents sich selbst verbessern, wer kontrolliert die Verbesserungsrichtung?
6. **Reasoning Cost:** o3 auf "high" = $60+ pro Task. Enterprise-untauglich ohne Efficiency-Gains.

---

*Confidence: [85% — Stärkste Evidenz: "To CoT or not to CoT?" (Meta-Analyse, 100+ Papers), "NoThinking" (empirisch auf 7 Datasets), "Illusion of Diminishing Returns" (mathematisch fundiert). Schwächste Stelle: Self-Evolving Reasoning Papers (2025-2026) sind emerging, nicht breit repliziert. LaRMA's LRM/LLM Split basiert auf spezifischen Benchmarks, Transfer auf Enterprise nicht validiert.]*

*Beipackzettel: 86 Papers auf Abstract-Level. Die "Reasoning-Topologie" und "Enterprise CoT Overrated" Thesen sind MIIAs eigene Synthese [J]. Foundational Papers (CoT, ReAct, ToT) sind Tier 1 (NeurIPS/ICLR). 2025-2026 Papers primär arXiv = Tier 2. Die mathematische Compound-Effect-Analyse (p^n) ist eine vereinfachte Formalisierung des "Illusion" Papers.*

---
*MIIA 🏔️ | Report 04/16 | 2026-02-27*

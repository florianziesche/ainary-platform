# Research Report 05: Planning in AI Agents
## Systematic Analysis of 44 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/capability-papers/planning.md*

---

## Executive Summary (BLUF)

**44 Papers spanning Jun 2022 – Oct 2025. 5 Kernerkenntnisse:**

1. **LLMs können NICHT planen.** Kambhampati (Feb 2024): Auto-regressive LLMs können weder planen noch sich selbst verifizieren. Aber: LLM-Modulo Frameworks (LLM + externe Verifier) sind die Lösung. Konsistent bestätigt durch PlanBench (o1 versagt), TravelPlanner, und "Chain of Thoughtlessness."
2. **LRMs (o1, R1) verbessern Planning — aber lösen es nicht.** o1 auf PlanBench: bessere Self-Evaluation als GPT-4, aber immer noch Bottlenecks bei Spatial Complexity und Dynamic Domain Adaptation. "Strawberry Fields" bestätigt: LRMs sind besser, aber nicht genug.
3. **Plan-then-Execute > Interleaved Planning.** ReWOO: Decoupling von Reasoning und Observations → 64% Token-Einsparung bei gleicher Performance. EAGLET: Plug-and-play Global Planner + Executor → signifikant besser als plan-less Agents.
4. **System-1.x = die richtige Architektur.** Nicht immer langsam (System-2/MCTS), nicht immer schnell (System-1/direct). Controllable Balance basierend auf Task-Complexity. Einfache Tasks = direkt. Komplexe = deliberativ.
5. **Planning-Tokens haben höhere Entropy als Action-Tokens.** DeepPlanner (Oct 2025): Unter Vanilla-RL bleiben Planning-Tokens "uncertain decision points." Advantage Shaping auf Planning-Tokens spezifisch = signifikanter Improvement.

---

## Taxonomie: 5 Cluster

### Cluster 1: The "LLMs Can't Plan" Debate (8 Papers)

#### 🔥🔥 [E] "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks" (Feb 2024)
*Kambhampati et al. | arXiv:2402.01817*
- **Position Paper: Definiert den Stand der Debatte.**
- Over-optimistic: "LLMs können planen mit dem richtigen Prompt" — FALSCH
- Over-pessimistic: "LLMs sind nur Syntax-Übersetzer" — auch FALSCH
- **Wahrheit: Auto-regressive LLMs können NICHT planen oder sich selbst verifizieren.**
- Aber: LLM als "Idea Generator" in LLM-Modulo Framework + externe Verifier = funktioniert.
- Approximate Retrieval Model (LLM) + Sound Verifier (externes System) = korrekter Plan
- **[J] DAS definitive Paper zur Planning-Debatte.** Jeder der behauptet "unser LLM kann planen" muss sich mit Kambhampati auseinandersetzen.

#### [E] "LLMs Still Can't Plan; Can LRMs?" (Oct 2024)
*Kambhampati et al. | arXiv:2409.13373*
- Follow-up: Evaluiert o1 auf PlanBench
- **Ergebnis: o1 ist BESSER als GPT-4, aber löst Planning NICHT.**
- "Despite OpenAI's claims, progress on this benchmark has been surprisingly slow."
- **[J] Selbst LRMs (o1) scheitern an formaler Planung.**

#### 🔥 [E] o1 Planning Abilities (Oct 2024)
*arXiv:2409.19924*
- 3 Achsen: Feasibility, Optimality, Generalizability
- o1 Stärken: Self-evaluation, Constraint-following
- o1 Schwächen: Dynamic domain adaptation, spatial complexity
- **[J] o1 ist ein besserer Self-Evaluator als Planner. Passt zu LLM-Modulo: LRM als Critic, nicht als Planner.**

#### [E] Planning in Strawberry Fields (Oct 2024)
*arXiv:2410.02162*
- o1 auf erweiterten Planning & Scheduling Tasks
- **Bestätigt: LRMs verbessern Planning, lösen es aber nicht.**

#### [E] "Chain of Thoughtlessness" (May 2024)
*arXiv:2405.04776*
- CoT auf Blocksworld (klassisches Planning)
- **Nur bei einfachsten Problemen sinnvoll. Generalisiert NICHT.**
- Titel ist Programm: CoT bei Planning = "Thoughtlessness" (gedankenlos)
- **[J] Bestätigt "To CoT or not to CoT" (Report 04): CoT hilft nicht bei Planning.**

#### [E] LLM+P (Apr 2023)
*arXiv:2304.11477*
- LLM übersetzt NL → PDDL, externer Planner löst
- **Erster erfolgreicher LLM-Modulo Ansatz für Planning.**

#### [E] Reasoning with World Model (May 2023)
*arXiv:2305.14992*
- "RAP": Repurpose LLM als World Model + Reasoning Agent
- MCTS über das interne World Model des LLM
- **[I] Elegante Idee: Das LLM IST das World Model und der Planner gleichzeitig.**

#### 📖 [E] Understanding LLM Agent Planning Survey (Feb 2024)
*arXiv:2402.02716*
- Erste systematische Taxonomie: Task Decomposition, Plan Selection, External Module, Reflection, Memory
- **[I] Gutes Framework für Consulting: "Welche Planning-Architektur passt?"**

---

### Cluster 2: Planning Architectures (12 Papers)

#### [E] ReWOO: Decoupling Reasoning from Observations (May 2023)
*arXiv:2305.18323*
- **Modular: Planner → Worker → Solver (getrennt, nicht interleaved)**
- Planner erstellt kompletten Plan VOR Execution
- Worker führt Tool-Calls parallel aus
- Solver synthetisiert finale Antwort
- **Ergebnis: -64% Token Usage, gleiche Performance wie ReAct**
- **[J] Plan-then-Execute ist EFFIZIENTER als interleaved Reasoning+Acting.** ReAct ist populärer aber wasteful.

#### [E] Plan-and-Solve Prompting (May 2023)
*arXiv:2305.04091*
- Zero-Shot CoT Verbesserung: "Let's first understand the problem and devise a plan"
- **[I] Simpelste Form von Plan-first: Ein einziger Prompt-Prefix.**

#### [E] SelfGoal: Adaptive Subgoal Decomposition (Jun 2024)
*arXiv:2406.04784*
- High-Level Goal → Tree of Subgoals (adaptiv, während Interaction)
- Identifiziert die NÜTZLICHSTEN Subgoals und priorisiert sie
- **[I] Elegante Lösung für "wie zerlege ich ein vages Ziel?"**

#### [E] CoAct: Global-Local Hierarchy for Multi-Agent (Jun 2024)
*arXiv:2406.13381*
- Global Planner Agent + lokale Executor Agents
- **[I] Hierarchical Planning = die natürliche Multi-Agent Architektur.**

#### [E] System-1.x Planner (Jul 2024) 🏆
*arXiv:2407.14414*
- **Controllable Balance zwischen Fast (System-1) und Slow (System-2) Planning**
- Nicht binary (immer schnell ODER immer langsam), sondern HYBRID
- Task-Complexity → entscheidet Planungsmodus
- **[J] Die richtige Architektur.** Einfache Tasks brauchen keine MCTS. Komplexe schon. System-1.x wählt dynamisch.

#### [E] Ask-before-Plan (Jun 2024)
*arXiv:2406.12639*
- **Proactive: Agent stellt Klärungsfragen VOR dem Planen**
- Real-world Planning → oft underspecified → Agent muss erst verstehen was gewollt ist
- **[J] Offensichtlich aber unterbelichtet. Kein Plan ohne klare Anforderung.**

#### [E] CaPo: Cooperative Multi-Agent Plan Optimization (Nov 2024)
*arXiv:2411.04679*
- Embodied Multi-Agent: Cooperative Planning für physische Tasks
- **[I] Relevant für Manufacturing: Multi-Maschinen-Koordination.**

#### [E] EAGLET: Efficient Global Planner Training (Oct 2025)
*arXiv:2510.05608*
- **Plan-and-Execute Framework mit trainiertem Global Planner**
- Phase 1: Synthesize Plans von Advanced LLM + Consensus Filtering + SFT
- Phase 2: RL mit Executor Capability-Aware Reward
- Plug-and-play: Planner als separates Modul
- **[J] Praktisch am relevantesten.** Zeigt dass man einen KLEINEN Planner trainieren kann der einen GROSSEN Executor steuert.

#### [E] DeepPlanner: Advantage Shaping für Planning (Oct 2025) 🏆
*arXiv:2510.12979*
- **KEY OBSERVATION: Planning-Tokens haben HÖHERE Entropy als Action-Tokens unter Vanilla-RL**
- Planning = "uncertain decision points" die unter-optimiert bleiben
- Lösung: Advantage Shaping spezifisch auf Planning-Tokens
- End-to-End RL Framework
- **[J] Identifiziert das Kernproblem: RL optimiert Actions gut, aber PLANS schlecht. Dedicated Planning-Optimization = der nächste Schritt.**

---

### Cluster 3: Benchmarks (6 Papers)

#### ⚖️ [E] PlanBench (Jun 2022)
*arXiv:2206.10498*
- Extensible Benchmark für Planning + Reasoning about Change
- Blocksworld, Logistics, etc.
- **Alle LLMs scheitern.** o1 nur marginal besser.

#### ⚖️🔥 [E] TravelPlanner (Jan 2024)
*arXiv:2402.01622*
- Real-World Planning: Reiseplanung mit Constraints
- Rich Sandbox: Flights, Hotels, Restaurants, Attractions + Budget + Time + Preferences
- **GPT-4-Turbo: 0.6% End-to-End Success (Sole-Planning)**
- **[E] 0.6%.** Nicht 60%. PUNKT SECHS PROZENT.
- **[J] Das ernüchterndste Ergebnis der gesamten Collection.** Real-world Planning mit Constraints = nahezu unmöglich für aktuelle LLMs.

#### ⚖️ [E] NATURAL PLAN (Jun 2024)
*arXiv:2406.04520*
- NL-basierte Planning-Tasks (kein PDDL)
- **[I] Testet Planning in natürlicher Sprache, näher an Enterprise-Realität.**

#### ⚖️ [E] FlowBench (Jun 2024)
*arXiv:2406.14884*
- Workflow-Guided Planning
- **[I] Enterprise-relevant: Workflows als Constraints für Agent-Pläne.**

#### ⚖️ [E] Agentic Workflow Generation Benchmark (Oct 2024)
*arXiv:2410.07869*
- Benchmarkt das GENERIEREN von Workflows, nicht nur das Ausführen
- **[I] Meta-Planning: Agent erstellt den Workflow-Plan selbst.**

#### [E] Can We Rely on Agents for Long-Horizon Plans? (Aug 2024)
*arXiv:2408.06318*
- TravelPlanner Case Study: Deep-Dive in Failure Modes
- **[I] Analysiert WARUM Agents bei TravelPlanner scheitern (nicht nur DASS).**

---

### Cluster 4: Knowledge & World Model-Augmented Planning (6 Papers)

#### [E] KnowAgent: Knowledge-Augmented Planning (Mar 2024)
*arXiv:2403.03101*
- Knowledge Base liefert Action-Constraints → weniger Halluzination in Plans
- **[I] RAG für Planning: Wissen über erlaubte Actions retrieveen statt halluzinieren.**

#### [E] Agent Planning with World Knowledge Model (May 2024)
*arXiv:2405.14205*
- World Model als Basis für Planung
- **[I] LLM + World Model = bessere Planung als LLM allein.**

#### [E] Planning in the Dark (Oct 2024)
*arXiv:2409.15915*
- LLM-Symbolic Planning OHNE Experten
- **[I] Automatisiert den LLM-Modulo Ansatz (keine manuelle PDDL-Erstellung nötig).**

#### [E] LLMs as Planning Domain Generators (May 2024)
*arXiv:2405.06650*
- LLM generiert PDDL-Domains automatisch
- **[I] LLM als Meta-Planner: Generiert nicht den Plan, sondern die Planning-Domain.**

#### [E] From Reasoning to Super-Intelligence (Jul 2025)
*arXiv:2507.15865*
- Search-Theoretic Perspective: CoT + SFT + RL + ToT + MCTS vereint
- "Diligent Learner": Modelliert Reasoning als SEARCH mit lernbarem Verifier
- **[J] Theoretisch ambitioniert: Planning = Search. Verifier = heuristic. LLM = node expansion.**

#### [E] Parameterized Skills for Adversarial Long-Horizon Planning (Sep 2025)
*arXiv:2509.13127*
- Skills als Brücke zwischen High-Level Plans und Low-Level Actions
- **[J] Direkte Verbindung zu Agent Skills (Report 03): Skills als Planning-Primitives.**

---

### Cluster 5: Surveys & Meta-Analysis (4 Papers)

#### 📖 [E] PlanGenLLMs (Feb 2025)
*arXiv:2502.11221*
- 6 Performance-Kriterien: Completeness, Soundness, Executability, Optimality, Generalizability, Efficiency
- **[J] Nützlichstes Framework für Evaluation.**

#### 📖 [E] LLMs for Planning: Comprehensive Survey (May 2025)
*arXiv:2505.19683*
- Aktuellste Survey zu Planning
- Theoretical Foundations + Taxonomy + Contemporary Approaches

#### 📖 [E] Diffusion Models for Planning (Aug 2024)
*arXiv:2408.10266*
- Alternative zu LLMs: Diffusion Models als Planner
- **[I] Nische, aber zeigt: Es gibt Alternativen zum autoregressive Planning.**

#### [E] PlanGEN: Multi-Agent Planning Framework (Feb 2025)
*arXiv:2502.16111*
- Multi-Agent für Complex Problem Solving Trajectories
- **[I] Multi-Agent Planning als systematischer Ansatz.**

---

## Synthese: 6 technische Erkenntnisse

### 1. Die Planning-Capability-Leiter

| Level | Beschreibung | Aktueller Stand | Evidence |
|---|---|---|---|
| 0 | Kein Planning | Vanilla LLM | - |
| 1 | Implicit Planning (CoT) | Funktioniert NUR bei Math/Logic | "Thoughtlessness" |
| 2 | Explicit Plan Generation | Generiert Pläne, aber fehlerhaft | TravelPlanner: 0.6% |
| 3 | Plan + Self-Verification | Besser mit LRMs, aber nicht zuverlässig | o1 auf PlanBench |
| 4 | LLM-Modulo (LLM + External Verifier) | **State of the Art** | Kambhampati 2024 |
| 5 | Trained Planner + Executor | Emerging, vielversprechend | EAGLET, DeepPlanner |
| 6 | Autonomous Adaptive Planning | **Nicht erreicht** | - |

**[J] Die Industrie befindet sich zwischen Level 3 und 4.** Level 4 (LLM-Modulo) ist technisch die richtige Architektur, aber kaum jemand implementiert es korrekt. Die meisten deployten Systeme sind Level 2 (Plan Generation ohne Verification).

### 2. Die TravelPlanner-Realität

**0.6% End-to-End Success für GPT-4-Turbo auf realer Reiseplanung.**

Das bedeutet: Von 1.000 Reiseplänen sind 6 korrekt. 994 sind fehlerhaft. In Enterprise:
- Budgetüberschreitung
- Nicht-bookbare Flüge
- Zeitkonflikte
- Constraint-Verletzungen

**[J] Wenn wir 0.6% auf Enterprise-Workflows übertragen (ähnliche Constraint-Dichte), dann ist autonomes Planning für kritische Business-Prozesse NICHT deploybar ohne externe Verification.** LLM-Modulo ist MANDATORY.

### 3. Plan-then-Execute > Interleaved

| Architektur | Token-Efficiency | Performance | Parallelism |
|---|---|---|---|
| ReAct (interleaved) | Baseline | Baseline | Keine |
| ReWOO (plan-then-execute) | **-64%** | **Gleich oder besser** | **Ja (Worker parallel)** |

**[J] ReWOO-Style Architekturen sind signifikant effizienter.** Der Grund: Interleaved (ReAct) schickt bei JEDEM Schritt den gesamten bisherigen Kontext + Tool-Outputs an das LLM. Plan-first generiert den Plan EINMAL, Workers führen PARALLEL aus, Solver synthetisiert.

### 4. Der Planner/Executor Split

Konvergente Evidenz aus:
- EAGLET: Trainierter Planner + Executor = besser
- DeepPlanner: Planning-Tokens brauchen separates Optimization
- CoAct: Global Planner Agent + lokale Executor Agents
- LaRMA (Report 04): LRMs für Planning, LLMs für Execution

**[J] Der optimale Agent hat ZWEI getrennte Komponenten:**
```
Global Planner (LRM oder trainierter Planner)
  → Erstellt High-Level Plan
  → Zerlegt in Subgoals
  → Priorisiert

Local Executor (LLM mit Tool Access)
  → Führt einzelne Subgoals aus
  → Handelt Exceptions
  → Reports Status zurück an Planner

External Verifier (symbolisch oder constraint-basiert)
  → Prüft Plan-Validity
  → Prüft Constraint-Compliance
  → Gibt Feedback → Planner re-plant
```

### 5. Ask-Before-Plan

"Ask-before-Plan" (2406.12639) macht eine einfache aber mächtige Beobachtung:
- Real-world Planning Requests sind UNDERSPECIFIED
- "Plane mir eine Reise nach München" → Budget? Dauer? Interessen? Airline-Präferenz?
- Agents die SOFORT planen statt ERST zu fragen machen schlechtere Pläne

**[J] Proactive Clarification VOR Planning = der größte Low-Hanging-Fruit.** Kostet fast nichts zu implementieren, verbessert Plan-Qualität substantiell. Gilt direkt für Enterprise: "Was genau wollen Sie optimieren?" VOR dem Automatisierungs-Vorschlag.

### 6. Planning-Entropy und RL

DeepPlanner's Beobachtung ist technisch faszinierend:

```
Under Vanilla RL:
  Action tokens:   Low entropy ← well-optimized
  Planning tokens: HIGH entropy ← under-optimized
```

Das bedeutet: RL-Training optimiert die AUSFÜHRUNG gut, aber die PLANUNG schlecht. Planning-Entscheidungen ("was soll ich als nächstes tun?") bleiben unsicher.

**[J] Implikation:** Generische RL-Frameworks (GRPO, PPO) sind für Tool Use gut (Report 03) aber für Planning NICHT ausreichend. Planning braucht dedizierte Optimization (Advantage Shaping auf Planning-Tokens).

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **"LLMs Can't Plan"** (2402.01817) | Definiert den Stand: LLM-Modulo = die Lösung. |
| 2 | **TravelPlanner** (2402.01622) | 0.6% Success. Ernüchterndste Zahl der Collection. |
| 3 | **DeepPlanner** (2510.12979) | Planning-Token Entropy. Dedicated Planning RL. |
| 4 | **ReWOO** (2305.18323) | -64% Tokens. Plan-then-Execute > Interleaved. |
| 5 | **System-1.x** (2407.14414) | Controllable Fast/Slow Balance. Die richtige Architektur. |
| 6 | **EAGLET** (2510.05608) | Trained Planner + Executor. Practical. |
| 7 | **o1 on PlanBench** (2409.13373) | LRMs verbessern, lösen aber nicht. |
| 8 | **Ask-before-Plan** (2406.12639) | Proactive Clarification = Low-Hanging-Fruit. |
| 9 | **SelfGoal** (2406.04784) | Adaptive Subgoal Tree. Elegant. |
| 10 | **From Reasoning to Super-Intelligence** (2507.15865) | Search-theoretic Foundation. Diligent Learner. |

---

## Cross-Report Connections

| Finding (Report 05) | Connects to | Report |
|---|---|---|
| LLMs Can't Plan → LLM-Modulo | Enterprise 41.8% ceiling (same pattern) | 02 |
| CoT useless for Planning | CoT useless for non-math (same conclusion) | 04 |
| Plan-then-Execute (ReWOO) | Meta-tools (-11.9% calls via workflow bundling) | 03 |
| System-1.x (Fast/Slow) | SMART (-24% tool calls via metacognition) | 03 |
| DeepPlanner (Planning-RL) | ToolRL (Tool-specific RL rewards) | 03 |
| TravelPlanner 0.6% | CRMArena <55% (similar constraint failure) | 02 |
| External Verifier mandatory | Safety Guards mandatory (same principle) | 01 |

---

## Open Problems

1. **Real-World Constraint Planning:** 0.6% auf TravelPlanner. Wie skaliert man auf Enterprise-Constraints?
2. **Planning under Uncertainty:** Alle Papers nehmen deterministische Umgebungen an. Real-world = stochastisch.
3. **Continuous Re-Planning:** Agent führt Plan aus, Umgebung ändert sich → wie re-plant man effizient?
4. **Multi-Agent Plan Coordination:** CaPo ist ein Anfang, aber Enterprise = 10+ Agents mit Abhängigkeiten.
5. **Planning Cost:** MCTS + LLM = teuer. System-1.x ist ein Ansatz, aber keine systematische Cost-Optimization.
6. **Planning Evaluation:** PlanBench = formal/akademisch. Enterprise-Planning = messy/real-world. Keine Bridge.

---

*Confidence: [83% — Stärkste Evidenz: Kambhampati ("Can't Plan") ist peer-reviewed und von einem AI-Planning-Experten (Arizona State). TravelPlanner 0.6% ist reproduzierbar. DeepPlanner's Entropy-Beobachtung ist empirisch solide. Schwächste Stelle: System-1.x und EAGLET sind neuere Papers mit weniger Replikation. Ask-before-Plan ist "obvious in hindsight" aber empirisch weniger rigoros.]*

*Beipackzettel: 44 Papers auf Abstract-Level. Kambhampati's Position ist in der Community kontrovers — viele Teams glauben weiterhin dass LLMs planen können mit dem richtigen Prompt. Die Benchmark-Zahlen (0.6% TravelPlanner, PlanBench-Failures) sind objektiv. Die Architektur-Empfehlung (Planner/Executor/Verifier Split) ist MIIAs Synthese [J] basierend auf konvergenter Evidenz.*

---
*MIIA 🏔️ | Report 05/16 | 2026-02-27*

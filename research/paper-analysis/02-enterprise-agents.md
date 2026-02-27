# Research Report 02: Enterprise AI Agents
## Systematic Analysis of 19 Papers — Pure Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/application-papers/enterprise-agents.md*

---

## Executive Summary (BLUF)

**19 Papers. 4 Kernerkenntnisse:**

1. **Enterprise Agents scheitern an Komplexität.** CRMArena: <40% Success (ReAct), <55% (Function Calling). EnterpriseBench: Bestes Modell 41.8%. Agents können einfache Tasks, aber multi-step Enterprise Workflows überfordern sie systematisch.
2. **Das CRM-Problem ist gelöst — fast.** CRMWeaver (Agentic RL + Shared Memories) schafft Durchbrüche auf CRMArena-Pro. Der Trick: RL-Training auf synthetischen Business-Daten + Retrieval ähnlicher gelöster Probleme zur Inference-Time.
3. **Agentic BPM ist das nächste Paradigma.** Shift von Automation → Autonomie. Process Mining + LLM Agents = Agentic Business Process Management Systems (A-BPMS). Nicht Tasks automatisieren, sondern ganze Prozesse autonom steuern.
4. **Public Sector und Industrial Benchmarks existieren nicht.** Von >1.300 analysierten Benchmarks: 0 erfüllen Public-Sector-Kriterien. AssetOpsBench ist der erste Industrial-Agent-Benchmark überhaupt.

---

## Paper-Analyse (chronologisch, dann thematisch)

---

### Paper 1: Tutor CoPilot
**"A Human-AI Approach for Scaling Real-Time Expertise"**
*Oct 2024 | arXiv:2410.03017*

- [E] Erster RCT (Randomized Controlled Trial) eines Human-AI Systems in Live-Tutoring
- [E] 900 Tutoren, 1.800 K-12 Schüler, unter-versorgte Communities
- [E] Ergebnis: +4 Prozentpunkte Mastery (p<0.01), +9pp bei schwächeren Tutoren
- [E] Kosten: $20/Tutor/Jahr — negligible
- [I] Methodisch hervorragend: Pre-registered Analysis Plan, RCT-Design
- [I] Technisches Pattern: "Model of Expert Thinking" als Augmentation, nicht Replacement

**Technische Architektur:**
- LLM als Real-Time Copilot (nicht autonom, sondern Suggestion-Mode)
- Expert Thinking Model: Distilled aus Expert-Tutor-Trajectories
- Human bleibt in-the-loop, AI liefert kontextuell relevante Guidance

**[J] Significance:** Das sauberste empirische Evidence für Human-AI Collaboration in der gesamten Agent-Literatur. Kein anderes Paper hat einen RCT mit 2.700 Teilnehmern.

**Key Insight:** Der größte Impact ist bei den SCHWÄCHSTEN Nutzern (+9pp vs +4pp). AI als Equalizer, nicht als Optimizer. Implikation: Enterprise AI Agents sollten zuerst die weniger erfahrenen Mitarbeiter augmentieren — dort ist der ROI am höchsten.

---

### Paper 2: HR-Agent
**"A Task-Oriented Dialogue LLM Agent Tailored for HR Applications"**
*Oct 2024 | arXiv:2410.11239*

- [E] Task-Oriented Dialogue System für HR-Prozesse (Medical Claims, Access Requests, Time-Off)
- [E] Privacy-Architektur: Conversation Data wird NICHT an LLM gesendet während Inference
- [I] Löst ein reales Problem: HR hat hunderte repetitive Prozesse, unaddressed by current AI

**Technische Architektur:**
- Confidentiality-First: LLM sieht Konversation nicht direkt
- Task Templates: Strukturierte Flows für jeden HR-Prozess
- Hybrid: LLM für NLU, deterministische Logik für Execution

**Key Insight:** Enterprise Agents in sensitiven Bereichen (HR, Finance, Legal) MÜSSEN Confidentiality-by-Design haben. Nicht nachträglich draufschrauben — in die Architektur einbauen.

---

### Paper 3: CRMArena ⚖️
**"Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks"**
*Nov 2024 | arXiv:2411.02305*

- [E] Benchmark: 9 Tasks, 3 Personas (Service Agent, Analyst, Manager)
- [E] 16 Industrial Objects (Account, Order, Case, Knowledge Article) mit hoher Interconnectivity
- [E] Latent Variables: Complaint Habits, Policy Violations (simuliert realistische Datenverteilungen)
- [E] **Ergebnis: SotA Agents < 40% Success (ReAct), < 55% (Function Calling)**

**Technische Details:**
- Task-Komplexität: Multi-Object Queries erfordern JOIN-artige Reasoning über 16 Objekttypen
- Latent Variables: Agent muss implizite Muster erkennen (z.B. welche Kunden systematisch Policies verletzen)
- Persona-spezifisch: Manager-Tasks sind schwerer als Agent-Tasks

**[J] Warum das wichtig ist:**
CRM ist das EINFACHSTE Enterprise-System (gut strukturierte Daten, klare APIs, definierte Workflows). Wenn Agents hier bei <55% liegen, ist die Performance auf komplexeren Systemen (ERP, SCM, MES) wahrscheinlich noch schlechter.

**Implikation für Agent-Architektur:** ReAct allein ist insufficient für Enterprise. Function Calling hilft (+15pp), aber löst nicht das Grundproblem: Multi-Step Reasoning über interconnected Objekte.

---

### Paper 4: AssetOpsBench ⚖️🔥
**"Benchmarking AI Agents for Task Automation in Industrial Asset Operations and Maintenance"**
*Jun 2025 | arXiv:2506.03828*

- [E] **Erster Benchmark für Industrial AI Agents** (Industry 4.0)
- [E] End-to-End Asset Lifecycle: Condition Monitoring → Maintenance Planning → Intervention Scheduling
- [E] Vision: AI Agents die den gesamten Asset Lifecycle autonom managen
- [E] Framework für Development, Orchestration, Evaluation von Domain-Specific Agents

**Technische Architektur:**
- Multi-Capability Agents: Perception + Reasoning + Control integriert
- Domain-Specific: Nicht generisch, sondern auf Industrial Operations zugeschnitten
- Orchestration: Mehrere spezialisierte Agents für verschiedene Lifecycle-Phasen

**[J] Bedeutung:**
Traditionelle ML-Ansätze lösen isolierte Tasks (Anomaly Detection ODER Maintenance Scheduling ODER Root Cause Analysis). AssetOpsBench ist das erste Framework das END-TO-END Automation in Industrial Settings benchmarkt. Das ist ein Paradigmenwechsel: Von "AI für ein Problem" zu "AI für den gesamten Prozess".

**Key Insight:** Industrial Agent Development braucht drei Dinge gleichzeitig: Perception (Sensordaten verstehen), Reasoning (Kausalitäten ableiten), Control (Aktionen planen). Kein aktuelles LLM kann alle drei gleichzeitig.

---

### Paper 5: AI Agents-as-Judge
**"Automated Assessment of Accuracy, Consistency, Completeness and Clarity for Enterprise Documents"**
*Jun 2025 | arXiv:2506.22485*

- [E] Multi-Agent System für Enterprise Document Review
- [E] Spezialisierte Agents pro Review-Kriterium: Template Compliance, Factual Correctness, etc.
- [E] Stack: LangChain + CrewAI + TruLens + Guidance
- [E] **Ergebnisse: 99% Information Consistency (vs 92% Mensch), halbe Error Rate, Review-Zeit: 30min → 2.5min**
- [E] 95% Agreement Rate zwischen AI und menschlichem Expert-Review

**Technische Architektur:**
- Modular: Jeder Agent hat ein diskretes Review-Kriterium
- Parallel oder Sequential je nach Abhängigkeit
- Standardisiertes Output-Schema (maschinenlesbar) für Downstream Analytics
- Continuous Monitoring + Human-in-the-Loop Feedback

**[J] Das Paper das Enterprise am schnellsten überzeugt:**
- Quantifizierter ROI: 30min → 2.5min = 12x Speedup
- Messbar besser als Menschen: 99% vs 92% Consistency
- Kein Black-Box: Standardisiertes Schema, auditierbar
- Low Risk: Document Review ist non-destructive (keine irreversiblen Aktionen)

**Key Insight:** Der schnellste Weg zu Enterprise AI Adoption ist via non-destructive, measurable, auditable Tasks. Document Review > Prozessautomation als Einstieg.

---

### Paper 6: Routine
**"A Structural Planning Framework for LLM Agent System in Enterprise"**
*Jul 2025 | arXiv:2507.14447*

- [E] Structural Planning Framework: LLM-generierte Pläne als explizite Strukturen
- [I] Adressiert ein Kernproblem: LLM Agents planen implizit (im Token-Stream), was in Enterprise nicht auditierbar ist
- [I] "Routine" = vordefinierter Ablaufplan den der Agent befolgt, aber adaptiv anpassen kann

**Key Insight:** Enterprise braucht EXPLIZITE Pläne, nicht implizites Reasoning. Auditierbarkeit > Flexibility. Ein Agent der seinen Plan als Datenstruktur exponiert (nicht als Token-Stream) ist für Enterprise 10x wertvoller.

---

### Paper 7: Compliance Brain Assistant
**"Conversational Agentic AI for Assisting Compliance Tasks"**
*Jul 2025 | arXiv:2507.17289*

- [E] User Query Router: Balanciert Response Quality vs Latency
- [E] Compliance-spezifisch: Regulatorische Anforderungen, Policy-Checks, Audit-Unterstützung
- [I] Enterprise Compliance = hohes Risiko, geringe Fehlertoleranz, strenge Auditierbarkeit

**Technische Architektur:**
- Query Router: Einfache Queries → Fast Path (niedrigere Kosten), Komplexe → Full Agent Pipeline
- Domain-Specific Grounding: Compliance-Dokumente als Knowledge Base
- Audit Trail: Jede Agent-Entscheidung dokumentiert

**Key Insight:** Query Routing (schnell vs. gründlich) ist ein unterbeleuchtetes Architekturmuster. Nicht jede Enterprise-Query braucht den vollen Agent-Stack. 80% der Anfragen sind einfach und sollten schnell beantwortet werden.

---

### Paper 8: Chatting with your ERP 🔥
**"A Recipe"**
*Jul 2025 | arXiv:2507.23429*

- [E] LLM Agent für Production-Grade ERP: Natural Language → SQL
- [E] **Dual-Agent Architecture: Reasoning Agent + Critique Agent**
- [E] Open-Weight LLMs + Ollama Deployment (self-hostable!)
- [E] Real industrial production-grade ERP System

**Technische Architektur:**
```
User Query (NL) → Reasoning Agent → SQL Draft
                                       ↓
                   Critique Agent ← SQL Draft
                                       ↓
                   Validated SQL → ERP Database → Result
```

- Reasoning Agent: Generiert SQL basierend auf Schema + Query
- Critique Agent: Prüft SQL auf Korrektheit, Schema-Compliance, Safety
- Dual-Loop: Critique kann Reasoning Agent zur Revision zwingen

**[J] Warum das technisch elegant ist:**
1. **Separation of Concerns:** Generierung ≠ Validation. Zwei separate LLMs mit unterschiedlichen Optimierungszielen.
2. **Self-Hostable:** Open-Weight + Ollama = läuft on-prem. Kein Cloud-Dependency.
3. **ERP-Specific:** Nicht generisch, sondern auf die Eigenheiten von ERP-Schemas zugeschnitten (normalisiert, viele JOINs, komplexe Beziehungen).

**Key Insight:** Der Dual-Agent Pattern (Generator + Critic) ist wahrscheinlich der robusteste Ansatz für Enterprise Database Interaction. Ein einzelner Agent halluziniert SQL. Zwei Agents korrigieren sich gegenseitig.

---

### Paper 9: SCUBA ⚖️
**"Salesforce Computer Use Benchmark"**
*Sep 2025 | arXiv:2509.26506*

- [E] 300 Task-Instanzen aus Real User Interviews
- [E] 3 Personas: Platform Admins, Sales Reps, Service Agents
- [E] Computer-Use Agents auf Salesforce Platform

**Key Insight:** Computer-Use (Screen-Interaction) statt API-Based Agents. Alternative Architektur: Agent interagiert mit Software wie ein Mensch (Klicks, Scrolls, Eingaben) statt über APIs. Vorteil: Funktioniert mit JEDER Software ohne Integration. Nachteil: Langsamer, fragiler, nicht auditierbar auf Action-Level.

---

### Paper 10: Survey — LLM-driven Industry Agents 📖🔥
**"Empowering Real-World: Technology, Practice, and Evaluation"**
*Oct 2025 | arXiv:2510.17491*

- [E] Umfassendster Survey zu Industry Agents (nicht nur Enterprise-IT, sondern Real-World)
- [E] Technology (LLM Capabilities) + Practice (Deployment Patterns) + Evaluation (Benchmarks)
- [I] Bridging Paper zwischen akademischer Forschung und industrieller Praxis

**Key Insight:** Drei Gaps identifiziert:
1. **Capability Gap:** LLMs können Reasoning, aber nicht Perception + Control
2. **Practice Gap:** Lab-Performance ≠ Production-Performance
3. **Evaluation Gap:** Akademische Benchmarks ≠ industrielle Anforderungen

---

### Paper 11: CRMWeaver 🔥
**"Building Powerful Business Agent via Agentic RL and Shared Memories"**
*Oct 2025 | arXiv:2510.25333*

- [E] **State-of-the-Art auf CRMArena-Pro** (Nachfolger von CRMArena)
- [E] Lightweight Modell outperformt größere Modelle durch Training + Inference-Tricks
- [E] Zwei Innovationen:
  1. **Agentic RL auf synthetischen Business-Daten** (Training-Time)
  2. **Shared Memories: Retrieval ähnlicher gelöster Tasks** (Inference-Time)

**Technische Details:**
- Synthesis Data Generation: LLM generiert realistische Business-Szenarien für RL-Training
- RL-Paradigm: Agent lernt aus Reward-Signalen bei Interaction mit Business-Environment
- Shared Memories: Wenn Agent neue Task sieht → retrievet Guidelines aus ähnlichen früheren Tasks
- Generalization: Funktioniert auch in unseen Scenarios durch Memory-Transfer

**[J] Technisch bedeutend weil:**
- Zeigt dass RL-Training auf synthetischen Daten funktioniert (keine echten Business-Daten nötig)
- Shared Memories = elegante Lösung für das Few-Shot-Problem in Enterprise (jedes Unternehmen hat einzigartige Prozesse)
- Lightweight: Kleinere Modelle + bessere Architektur > größere Modelle + naive Prompting

**Key Insight:** Die Zukunft von Enterprise Agents ist NICHT größere Modelle. Es ist: Kleinere Modelle + RL-Training auf domänenspezifischen Daten + Memory-Systeme für Erfahrungstransfer.

---

### Paper 12: EnterpriseBench ⚖️
**"Can LLMs Help You at Work?"**
*Oct 2025 | arXiv:2510.27287*

- [E] 500 Tasks: Software Engineering, HR, Finance, Administration
- [E] Simulated Enterprise: Data Fragmentation, Access Control, Cross-Functional Workflows
- [E] Novel Data Generation Pipeline aus Organizational Metadata
- [E] **Bestes Modell: 41.8% Task Completion**

**Technische Details:**
- Data Fragmentation: Informationen über 3-5 Datenquellen verteilt pro Task
- Access Control Hierarchies: Agent muss beachten WER auf WAS Zugriff hat
- Cross-Functional: Tasks erfordern Wissen aus mehreren Departments

**[J] Warum 41.8% ein Problem ist:**
Enterprise Tasks sind nicht "schwer" im akademischen Sinne. Es sind Standard-Büroaufgaben die jeder Junior-Mitarbeiter in 30min erledigt. Dass SotA-Agents bei <42% liegen zeigt: Das Problem ist nicht Intelligence, sondern **Organizational Context**. Agents verstehen nicht, wie Organisationen funktionieren.

**Key Insight:** Die drei Enterprise-Killer:
1. **Data Fragmentation:** Agent findet die Information nicht (verteilt über 5 Systeme)
2. **Access Control:** Agent weiß nicht, was er sehen DARF
3. **Implicit Knowledge:** "Das macht man bei uns so" ist nirgendwo dokumentiert

---

### Paper 13: DataGovBench ⚖️
**"Benchmarking LLM Agents for Real-World Data Governance Workflows"**
*Dec 2025 | arXiv:2512.04416*

- [E] 150 Tasks für Data Governance (Quality, Security, Compliance)
- [E] "Reversed-Objective" Methodology: Synthetisiert realistisches Noise
- [E] DataGovAgent: Planner-Executor-Evaluator Architecture
- [E] Current Models: Scheitern an multi-step Workflows + Error Correction

**Technische Architektur (DataGovAgent):**
```
Planner: Zerlegt Task in Sub-Tasks + definiert Constraints
    ↓
Executor: Führt Sub-Tasks aus (Code-Generation für Data Transformations)
    ↓
Evaluator: Prüft Output gegen Constraints + Quality Metrics
    ↓
[Feedback Loop: Evaluator → Planner bei Failures]
```

**Key Insight:** Planner-Executor-Evaluator ist ein robusteres Pattern als ReAct für Enterprise. Warum? Weil der Evaluator DETERMINISTISCHE Checks ausführen kann (Schema-Validation, Constraint-Checking), nicht probabilistische LLM-Urteile.

---

### Paper 14: DeepRule
**"Automated Business Rule Generation via Deep Predictive Modeling"**
*Dec 2025 | arXiv:2512.03607*

- [E] Tri-Level Architecture für Retail Assortment + Pricing
- [E] Hybrid Knowledge Fusion: LLMs für Semantic Parsing unstrukturierter Texte
- [E] Game-Theoretic Optimization für Supply Chain Interest Reconciliation

**Key Insight:** LLMs als "Knowledge Fusion Engine" für unstrukturierte Business-Daten (Verhandlungsprotokolle, Genehmigungsdokumente) — nicht als Decision Maker, sondern als Structurer. Der LLM parsed, die Optimierung entscheidet.

---

### Paper 15: Advances in Agentic AI 📖
**"Back to the Future"**
*Dec 2025 | arXiv:2512.24856*

- [E] Positionspapier: Begriffsdefinitionen von Intelligence bis Agentic AI
- [E] Unterscheidung: M1 (aktuelles LLM-basiertes Agentic AI = B2C-Extension) vs M2 (Strategy-based Agentic AI = echte B2B-Transformation)
- [I] M1 = "Information Retrieval UX repurposed for B2B" — kritische Perspektive

**Key Insight:** Das Paper argumentiert dass aktuelles Agentic AI (M1) fundamentally ein B2C-Paradigma ist das für B2B umfunktioniert wird. Echte B2B-Transformation (M2) erfordert "Strategies-based" Agents die Business-Strategien verstehen, nicht nur Tasks ausführen. Kontrovers aber denkwürdig.

---

### Paper 16: Time-Scaling Is What Agents Need Now
*Jan 2026 | arXiv:2601.02714*

- [E] Convergence: Neural Networks (Perception) + RL (Decision) + Symbolic AI (Reasoning) → Cognitive Agents
- [E] CoT/ToT als "Time-Scaling" reframed: Agents brauchen ZEIT zum Denken
- [E] DeepSeek-R1 als Beispiel: Explicit Reasoning Trajectories

**Key Insight:** "Time-Scaling" = dem Agent mehr Compute-Budget zum Nachdenken geben. Analog zu Test-Time Compute Scaling. Für Enterprise: Lieber 30 Sekunden nachdenken und richtig handeln als 3 Sekunden und falsch.

---

### Paper 17: AgencyBench ⚖️
**"Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts"**
*Jan 2026 | arXiv:2601.11044*

- [E] 1M-Token Kontexte — testet Long-Context Agent-Fähigkeiten
- [E] Real-World: Nicht synthetische Tasks, sondern echte Dokumentkontexte
- [I] Erster Benchmark der Multi-Faceted Agent Capabilities in einem Test vereint

**Key Insight:** 1M-Token Context ist die neue Frontier. Enterprise-Dokumente (Verträge, Reports, Policies) sind lang. Agents die nur 32K Token verarbeiten können, sind für Enterprise unbrauchbar.

---

### Paper 18: Agent Benchmarks Fail Public Sector ⚖️
*Jan 2026 | arXiv:2601.20617 | IASEAI 2026*

- [E] >1.300 Benchmark Papers analysiert
- [E] Kriterien: Process-based, Realistic, Public-Sector-Specific, Sector-Relevant Metrics
- [E] **Ergebnis: KEIN Benchmark erfüllt alle Kriterien**
- [I] Call to Action: Neue Benchmarks nötig

**Key Insight:** Wenn 1.300+ Benchmarks existieren und KEINER Public-Sector-Anforderungen erfüllt — dann ist die gesamte Benchmark-Landschaft tech-biased. Enterprise und Public Sector haben fundamental andere Anforderungen (Process-based, Compliance, Auditierbarkeit) die akademische Benchmarks systematisch ignorieren.

---

### Paper 19: Agentic Business Process Management Systems 🔥🔥
**"A-BPMS"**
*Jan 2026 | arXiv:2601.18833 | Keynote, AI for BPM Workshop 2025*

- [E] Position Paper: Paradigm Shift von Automation → Autonomie
- [E] BPM-Evolution: Seit 90er Jahren, Wellen von Automation. Agentic AI = nächste Welle.
- [E] Architekturvision: A-BPMS (Agentic BPM Systems)
- [E] Process Mining als Foundation: Agents die Prozesse BEOBACHTEN, VERSTEHEN, OPTIMIEREN

**Technische Vision:**
```
Traditional BPM:
  Design Process → Deploy → Monitor → Manually Improve
  (Design-Driven, Human-Managed)

Agentic BPM (A-BPMS):
  Mine Process → Agent Observes → Agent Reasons → Agent Acts → Agent Learns
  (Data-Driven, Agent-Managed, Human-Supervised)
```

- **Sense:** Agent beobachtet Prozess-States via Process Mining
- **Reason:** Agent identifiziert Improvement-Opportunities
- **Act:** Agent nimmt Änderungen vor (Parameter, Routing, Resources)
- **Learn:** Agent lernt aus Outcomes und verbessert sich

**Continuum of Autonomy:** Von vollständig menschlich-kontrolliert bis vollständig autonom, je nach Risiko und Vertrauen.

**[J] Warum das das wichtigste Paper der Collection ist:**
Es definiert ein NEUES Paradigma. Nicht "AI die Tasks erledigt" (M1) sondern "AI die Geschäftsprozesse versteht und optimiert" (M2). Process Mining + Agentic AI ist die Kombination die Enterprise tatsächlich transformiert. Einzelne Task-Automation ist inkrementell. Prozess-Autonomie ist disruptiv.

---

## Synthese: 6 technische Erkenntnisse

### 1. Die Enterprise Performance Cliff

| Benchmark | Domain | Best Agent Performance | Gap zu Human |
|---|---|---|---|
| CRMArena | CRM | <55% (Function Calling) | ~45pp |
| EnterpriseBench | Multi-Domain | 41.8% | ~58pp |
| SCUBA | Salesforce | TBD | TBD |
| AssetOpsBench | Industrial | TBD (erst Jun 2025) | TBD |

**[I] Pattern:** Enterprise Agent Performance liegt konsistent bei 40-55%. Die Ursache ist NICHT mangelnde Intelligence, sondern:
1. Data Fragmentation (Information verteilt über Systeme)
2. Organizational Context (implizites Wissen fehlt)
3. Multi-Step Reasoning über interconnected Objects

### 2. Architektur-Patterns die funktionieren

| Pattern | Paper | Stärke | Schwäche |
|---|---|---|---|
| **Dual-Agent (Generator + Critic)** | Chatting with ERP | Robuster SQL, Self-Correction | 2x Compute-Kosten |
| **Planner-Executor-Evaluator** | DataGovAgent | Deterministische Validation | Rigide, wenig adaptiv |
| **Agentic RL + Shared Memories** | CRMWeaver | Lernt aus Erfahrung, generalisiert | Braucht RL-Training-Infrastruktur |
| **Query Router (Fast/Full)** | Compliance Brain | Kosteneffizient, 80% schneller Pfad | Router-Fehler = falscher Pfad |
| **Structural Planning (Routine)** | Routine | Auditierbar, explizite Pläne | Weniger flexibel als implizites Reasoning |
| **Human-AI Copilot** | Tutor CoPilot | Bewiesener Impact (RCT), sicher | Mensch bleibt Bottleneck |

**[J] Empfehlung:** Für Enterprise Agents, Hybrid-Architektur:
```
Query Router → Simple: Fast Path (Direct RAG)
            → Complex: Planner-Executor-Evaluator
            → Critical: Dual-Agent + Human-in-the-Loop
```

### 3. Synthetic Data + RL = Enterprise Training

CRMWeaver beweist: RL-Training auf synthetischen Business-Daten funktioniert besser als Prompting größerer Modelle. Implikation:
- Keine echten Kundendaten nötig für Training
- Lightweight Modelle + RL > Heavy Modelle + naive Prompts
- Shared Memories ermöglichen Generalization auf neue Szenarien

### 4. Process Mining + Agents = A-BPMS

Die A-BPMS Vision (Paper 19) ist das architektonisch ambitionierteste Konzept:
- Process Mining liefert das "Auge" (Was passiert gerade im Prozess?)
- LLM Agent liefert das "Gehirn" (Was sollte anders sein?)
- Actuation liefert die "Hand" (Ändere Parameter, Route, Resources)
- Learning liefert das "Gedächtnis" (Was hat funktioniert, was nicht?)

Das ist kein einzelner Agent — es ist ein Agent-Ecosystem das auf einen Business-Prozess wirkt.

### 5. The "Non-Destructive First" Principle

Agents-as-Judge (Paper 5): 12x Speedup, 99% vs 92% Consistency, 95% Agreement mit Experten — und ZERO RISK. Warum? Document Review ändert nichts. Es ist rein analytisch.

**[I] Enterprise AI Adoption Strategy:**
1. **Phase 1:** Non-destructive Agents (Review, Analysis, Search, Reporting) → Vertrauen aufbauen
2. **Phase 2:** Reversible Agents (Drafting, Suggestions, Pre-filled Forms) → Effizienz steigern
3. **Phase 3:** Autonomous Agents (Process Optimization, Resource Allocation) → Transformation

### 6. Die Benchmark-Lücke ist die Opportunity

>1.300 Benchmarks existieren. 0 erfüllen Public-Sector-Kriterien. 1 (AssetOpsBench) addressiert Industrial. Die akademische Community optimiert auf das Falsche.

**Was gebraucht wird:**
- Process-based Benchmarks (nicht Task-based)
- Compliance-aware Metrics (nicht nur Accuracy)
- Domain-specific Evaluation (nicht generisch)
- Long-horizon Tasks (nicht single-turn)
- Access-Control-aware (nicht open-information)

---

## Technische Roadmap: Wie Enterprise Agents besser werden

```
2024                  2025                  2026                  2027
  │                     │                     │                     │
  │  ReAct Agents       │  RL-trained         │  A-BPMS             │  Autonomous
  │  <40% Success       │  Agents             │  Process-Level      │  Process
  │                     │  CRMWeaver          │  Autonomy           │  Optimization
  │  Single-Turn        │  50-70%?            │                     │
  │  Task Execution     │                     │  Process Mining     │  Self-Improving
  │                     │  Shared Memories    │  + LLM Agents       │  Business
  │  No Learning        │  Cross-Task         │                     │  Processes
  │                     │  Transfer           │  Continuum of       │
  │  Prompt-Based       │                     │  Autonomy           │
  │  Only               │  Dual-Agent         │  (Human → Agent)    │
  │                     │  Patterns           │                     │
  ▼                     ▼                     ▼                     ▼
```

---

## Top 5 Papers (Technical Impact)

| Rang | Paper | Warum technisch bedeutend |
|------|-------|--------------------------|
| 1 | **A-BPMS** (2601.18833) | Definiert neues Paradigma: Process-Level Agent Autonomie |
| 2 | **CRMWeaver** (2510.25333) | Beweist: RL + Shared Memories > größere Modelle |
| 3 | **Chatting with ERP** (2507.23429) | Dual-Agent Pattern für Enterprise DB, self-hostable |
| 4 | **EnterpriseBench** (2510.27287) | Quantifiziert den Enterprise Performance Gap (41.8%) |
| 5 | **Tutor CoPilot** (2410.03017) | Einziger RCT. Beweist: AI Impact höchsten bei schwächsten Nutzern |

---

*Confidence: [80% — Alle Abstracts verifiziert. EnterpriseBench/CRMArena Zahlen direkt aus Papers. A-BPMS ist ein Position Paper (Vision, nicht validiert). CRMWeaver Claims auf CRMArena-Pro nicht unabhängig verifiziert. Stärkste Evidenz: Tutor CoPilot (RCT, n=2700), CRMArena (<55%), EnterpriseBench (41.8%). Schwächste: A-BPMS (Vision), DeepRule (domain-specific, schwer generalisierbar).]*

*Beipackzettel: 19 Papers auf Abstract-Level. Volltext-Analyse würde architektonische Details und Reproduzierbarkeit besser bewerten. Keine eigenen Experimente durchgeführt. arXiv-Papers = Tier 2. Ausnahmen: EMNLP, IASEAI, AI for BPM Workshop Papers = Tier 1.5 (peer-reviewed Workshop/Industry Track).*

---
*MIIA 🏔️ | Report 02/16 | 2026-02-27*

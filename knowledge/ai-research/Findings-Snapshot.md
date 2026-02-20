---
type: meta
status: current
updated: 2026-02-19
owner: mia
source: platform-api
tier: OPERATIONAL
expires: 2026-08-20
---

# Findings Snapshot (Auto-Sync)

> Auto-generated from localhost:8080 on 2026-02-19. Do not edit manually.
> Related: [[Claims-Ledger]] | [[Paper-Tracker]] | [[AR-001 State of Agent Trust]]

**Total Findings:** 106

## High Confidence (≥0.85) (48)

- **RF-001** (conf: 0.90): Pre-Flight mit Regex fängt 80% der Output-Fehler bei 0 Kosten und <50ms
- **C002** (conf: 0.85): 84% of [[LLM]] outputs are overconfident (verbalized confidence exceeds actual accuracy)
- **C001** (conf: 0.85): 67% of security alerts are ignored by SOC analysts
- **C004** (conf: 0.85): 6% of companies achieve '[[AI]] High Performer' status with 2-3x productivity gains
- **C005** (conf: 0.85): MemoryGraft attack achieves >95% memory injection success rate
- **C013** (conf: 0.85): Air Canada held legally liable for chatbot hallucination
- **C014** (conf: 0.85): Grok RAG poisoning contaminated thousands of responses before detection
- **C015** (conf: 0.85): Waymo required 7 collisions before issuing recall
- **RF-074** (conf: 0.98): CONTRADICTION AUFGELÖST: Fully Autonomous Agents vs. Human-in-the-Loop. Production zeigt: HITL für irreversible Actions 
- **C-008** (conf: 0.98): AgentTrust ≠ Observability. LangSmith/Arize/Galileo tracen und monitoren — KEINER kalibriert. AgentTrust ist Calibration
- **RF-026** (conf: 0.95): Gewichteter Durchschnitt (a*0.7 + b*0.3) ist KEIN Bayesian Update. Echte Formel: P(H|E) = P(E|H)·P(H) / [P(E|H)·P(H) + P
- **RF-059** (conf: 0.95): ReAct (Think→Act→Observe→Repeat) ist das Fundament für Agent-Architekturen. Score 100/100 (Buildability 10 × Relevance 1
- **RF-075** (conf: 0.95): ReAct Implementation Pattern: while not task_complete: thought → action → observation → context.add(). Max-Iteration-Lim
- **RF-078** (conf: 0.95): RAG Implementation Pattern: Index (docs → embeddings → vector DB) → Retrieve (query → top-K chunks) → Augment (chunks + 
- **RF-067** (conf: 0.93): Production Failure: Free-Form [[LLM]] Outputs ohne Validation halluzinieren. Structured Outputs (JSON Schema Validation) sin
- **RF-063** (conf: 0.92): Production Agentic Workflows: 4 Core Patterns funktionieren (Reflection, Tool Use/ReAct, Planning, Multi-Agent). Score 1
- **RF-064** (conf: 0.92): Production Failure: Fully Autonomous Agents ohne Human-Oversight scheitern. Agents machen Fehler die eskalieren. HITL Ch
- **RF-070** (conf: 0.92): Production Failure: Tool-Use ohne Whitelisting ist Security-Risiko. Prompt Injection kann Agents manipulieren. Least-Pri
- **RF-025** (conf: 0.90): Native browser prompt() zerstört UX-Flow und signalisiert Amateur-Level. Inline Modal mit Fokus-Management ist Standard.
- **RF-029** (conf: 0.90): Research VOR Implementierung ist nicht optional. 15min Research hätte 40min Rework gespart (fake Bayesian, prompt() stat
- **RF-031** (conf: 0.90): Ein Wissens-System das vom Erbauer nicht benutzt wird, wird von niemandem benutzt. Dogfooding ist der erste Test. Wenn i
- **RF-046** (conf: 0.90): MCP (Model Context Protocol) has 10,000+ active public servers and 97M+ monthly SDK downloads — de facto standard for ag
- **RF-048** (conf: 0.90): Full autonomous software engineering still not here — agents need human-in-the-loop for complex decisions
- **RF-049** (conf: 0.90): [[AI]] startup funding reached $202B globally in 2025 (+75% YoY), capturing ~50% of all [[VC]] funding
- **RF-053** (conf: 0.90): Agent Teams für Investigative Journalism: Parallele Agents ([[Claude]] Opus 4.6) koordinieren autonome Recherche — Agent 1: 
- **RF-054** (conf: 0.90): Workflow Memory für CNC-Kalkulation: Wang et al. Workflow Memory Paper (Sept 2024) auf Fertigungskalkulation anwenden — 
- **RF-055** (conf: 0.90): Browser Use für OZG-Automatisierung: Open-source Browser Use Framework für OZG-Integration ohne APIs — Agent bedient leg
- **RF-060** (conf: 0.90): MemGPT (Context-Window als Virtual Memory mit Main/Storage/Paging) ist ESSENTIAL für Long-Running Agents. Score 80/100. 
- **RF-061** (conf: 0.90): Reflexion (verbales Reinforcement Learning: Execute→Feedback→Reflect→Retry) ermöglicht Agents aus Fehlern zu lernen OHNE
- **RF-062** (conf: 0.90): MCP (Model Context Protocol) ist der offene Standard für Agent-Tool-Integration. Score 90/100. Linux Foundation Agentic 
- ... and 18 more

## Medium (0.60-0.84) (36)

- **RF-002** (conf: 0.73): Bayesian Trust Scoring konvergiert schneller als lineares +2/-3 bei kleinen Stichproben
- **C009** (conf: 0.60): VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity
- **C003** (conf: 0.60): Tool calling fails 3-15% of the time in production agent systems
- **C006** (conf: 0.60): 80-99% false positive rate in healthcare alert systems
- **C007** (conf: 0.60): Each reminder reduces response rate by 30% (alert fatigue)
- **C008** (conf: 0.60): Klarna saved $60M with [[AI]] agents but reversed deployment due to trust failures
- **C010** (conf: 0.60): 96% of security breaches are disclosed by the attacker, not internal detection
- **C011** (conf: 0.60): LangChain grew from 0 to 100k GitHub stars in approximately 1 year
- **C012** (conf: 0.60): Vercel achieved $200M ARR via DX-first design philosophy
- **RF-073** (conf: 0.82): CONTRADICTION AUFGELÖST: Toolformer ([[LLM]]s lernen Tools selbst) vs. MCP (Standard für Tool-Integration). NICHT widersprüc
- **C-011** (conf: 0.82): OZG-Deadline + Förderung + Wettbewerbsvergleich (Dippoldiswalde) = Triple Fit für Glashütte Pilot. Regulatorischer Druck
- **RF-028** (conf: 0.80): Pipeline-Conversion-Rates zwischen Stages (Research→Systems: X%) sind der beste Indikator für Flywheel-Gesundheit. 0% Co
- **RF-038** (conf: 0.80): Eine horizontale 4-Column Kanban Pipeline View zeigt Flywheel-Gesundheit auf einen Blick besser als eine vertikale Liste
- **RF-052** (conf: 0.80): Long context (1M tokens) + compaction reduces RAG need for many use cases — RAG less hot topic 2026
- **RF-056** (conf: 0.80): Hierarchical Memory für Reporter-Beats: MemGPT/Generative Agents Architecture (Observations → Reflections → Planning) au
- **RF-057** (conf: 0.80): DeepSeek R1 für Data Sovereignty in Public Sector: Open-source reasoning model (on-par mit o1) self-hosted für Kommunen/
- **RF-071** (conf: 0.80): Research Machine Blueprint: 4-Layer System (Intake: 35 RSS Feeds 3x/Tag → Processing: 12h Relevanz-Scoring, >7=Summary, 
- **C-010** (conf: 0.80): Jeder Consulting-Pilot ist gleichzeitig ein Platform-Pilot. Kunden kaufen nicht Beratung, sie kaufen ein Dashboard. Pilo
- **RF-019** (conf: 0.79): Low conf finding for validation test
- **RF-023** (conf: 0.79): Low conf finding for validation test
- **RF-033** (conf: 0.79): Low conf finding for validation test
- **RF-036** (conf: 0.79): Low conf finding for validation test
- **RF-040** (conf: 0.79): Low conf finding for validation test
- **RF-043** (conf: 0.79): Low conf finding for validation test
- **RF-004** (conf: 0.60): Test finding for automated tests
- **RF-006** (conf: 0.60): Test finding for automated tests
- **RF-008** (conf: 0.60): Test finding for automated tests
- **RF-011** (conf: 0.60): Test finding for automated tests
- **RF-014** (conf: 0.60): Test finding for automated tests
- **RF-016** (conf: 0.60): Test finding for automated tests
- ... and 6 more

## Low (<0.60) (22)

- **H005** (conf: 0.55): Automatisches Research Scanning liefert relevante Ergebnisse
- **RF-021** (conf: 0.51): Bayesian test
- **RF-005** (conf: 0.50): Test contradiction detection
- **RF-007** (conf: 0.50): Test contradiction detection
- **RF-010** (conf: 0.50): Test contradiction detection
- **RF-013** (conf: 0.50): Test contradiction detection
- **RF-020** (conf: 0.50): Test contradiction detection
- **RF-024** (conf: 0.50): Test contradiction detection
- **RF-034** (conf: 0.50): Test contradiction detection
- **RF-037** (conf: 0.50): Test contradiction detection
- **RF-041** (conf: 0.50): Test contradiction detection
- **RF-044** (conf: 0.50): Test contradiction detection
- **RF-009** (conf: 0.48): Low conf finding for validation test
- **RF-012** (conf: 0.48): Low conf finding for validation test
- **H001** (conf: 0.40): Cross-Pattern Insights resonieren staerker als Single-Domain Content
- **H002** (conf: 0.40): Practitioner-Perspektive performt besser als akademische Paper-Reviews
- **H006** (conf: 0.40): VCs sind beeindruckt von Live-KI-System-Demo
- **H004** (conf: 0.35): GitHub Repos mit README-als-Artikel generieren Substack Subscriber
- **RF-015** (conf: 0.30): Low conf finding for validation test
- **RF-017** (conf: 0.30): Low conf finding for validation test
- **H003** (conf: 0.30): 55 Seiten in 45 Min ist ein Consulting-Produkt
- **RF-003** (conf: 0.02): [[LLM]]-as-Judge ist besser als Regex für Output Quality Checking

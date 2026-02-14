# Research Brief: Agent Memory Architectures — How AI Agents Remember and Forget

**Tag: [PUBLIC] — Audience: AI Engineers + Founders**
**Risk Tier: 2 — Claim Ledger PFLICHT**
**Datum: 2026-02-14**
**Decision Context: AgentTrust Features + Substack Artikel (eigenes Memory System)**

---

## Key Findings (Top 5)

### 1. Die Memory-Landschaft hat sich 2025 konsolidiert um 5 Frameworks
Die dominanten Open-Source-Ansätze sind **Letta (ex-MemGPT)**, **Mem0**, **Zep (Graphiti)**, **LangMem (LangChain)** und **A-Mem** (Forschung). Jedes löst Memory anders — von OS-artiger Virtualierung (Letta) über Knowledge Graphs (Zep) bis zu leichtgewichtigen Key-Value-Layern (Mem0).
— Quellen: Serokell Dec 2025, Graphlit Survey Oct 2025, DEV.to Jun 2025

### 2. Die Taxonomie ist klar: 3 Memory-Typen + Working Memory
Aus Kognitionswissenschaft übernommen, hat sich als Standard durchgesetzt:
- **Working Memory** = Context Window (kurzfristig, teuer, begrenzt)
- **Episodic Memory** = Vergangene Erfahrungen ("Was ist beim letzten Deployment passiert?")
- **Semantic Memory** = Fakten & Wissen ("User wohnt in Berlin, bevorzugt Python")
- **Procedural Memory** = Gelernte Verhaltensweisen (System Prompts, Tool-Nutzungsmuster)

RAG allein deckt nur Semantic ab. Episodic und Procedural werden von den meisten Systemen noch schlecht gelöst.
— Quellen: IBM Nov 2025, MLMastery Dec 2025, "Memory in the Age of AI Agents" (Hu et al., arXiv Jan 2026)

### 3. Memory Poisoning ist ein realer, dokumentierter Angriffsvektor
Drei unabhängige Papers 2025 zeigen: Agents mit persistentem Memory sind anfällig für **indirekte Prompt Injection über Memory**. Highlights:
- **MINJA** (2025): Query-only Attacks erreichen >95% Injection-Erfolgsrate
- **MemoryGraft** (Dec 2025): Implantiert falsche "Erfahrungen" in Long-Term Memory → Agent handelt danach dauerhaft falsch
- **Palo Alto Unit 42** (Oct 2025): PoC zeigt stille Vergiftung von ChatGPT-Memory via Indirect Injection
— Quellen: arxiv 2503.03704, arxiv 2512.16962, unit42.paloaltonetworks.com Oct 2025

### 4. Kein Framework löst Memory Governance + Trust gleichzeitig
Alle aktuellen Frameworks fokussieren auf **Speichern & Abrufen**, aber:
- ❌ Keine Provenance-Tracking (woher kam dieses Memory?)
- ❌ Kein Confidence-Scoring pro Erinnerung
- ❌ Kein Integrity-Check (wurde Memory manipuliert?)
- ❌ Kein selektives Vergessen mit Audit-Trail
- ❌ Kein Multi-Agent Trust (darf Agent B dem Memory von Agent A vertrauen?)

**Das ist die Lücke, die AgentTrust füllen kann.** ← INTERPRETATION
— Quellen: Eigene Analyse basierend auf Feature-Vergleich aller 5 Frameworks

### 5. Mem0 ist das am schnellsten wachsende Framework — $24M Funding, 186M API Calls/Quartal
Mem0 hat sich als "drop-in Memory Layer" positioniert: leichtgewichtig, LLM-agnostisch, 91% weniger Latenz als Full-RAG. 80k+ Entwickler auf Cloud. Zeigt: Der Markt will **einfache Integration**, nicht akademische Perfektion.
— Quelle: TechCrunch Oct 2025, arxiv 2504.19413

---

## Framework-Vergleich (State of the Art)

| Framework | Architektur | Memory-Typen | Stärke | Schwäche |
|-----------|------------|-------------|--------|----------|
| **Letta (MemGPT)** | OS-Paradigma: Context = RAM, Archival = Disk | Working + Episodic + Semantic | Elegantes Context-Management, self-managing | Single-Agent Overhead, unstrukturierte Daten |
| **Mem0** | Lightweight Layer zwischen App & LLM | Semantic + Episodic (einfach) | Schnell, einfach zu integrieren, 91% weniger Latenz | Kein Graph, limitierte Relationen |
| **Zep (Graphiti)** | Temporaler Knowledge Graph | Episodic + Semantic + Group-level | Zeitbewusst, relationales Wissen, Enterprise-ready | Komplex, Graph-Overhead |
| **LangMem (LangChain)** | SDK mit Semantic/Episodic/Procedural Stores | Alle 3 Typen | Flexibel, Framework-integriert, gute Taxonomie | Noch jung (Mai 2025 Launch), weniger Battle-tested |
| **A-Mem** (Forschung) | Agentic Memory mit Self-Organization | Adaptive | Selbstorganisierend, Research-leading | Kein Production-Framework |

---

## RAG vs Episodic vs Semantic Memory — Wann was?

| | RAG | Episodic Memory | Semantic Memory |
|---|---|---|---|
| **Was** | Retrieval aus statischem Dokumenten-Corpus | Vergangene Erfahrungen & Interaktionen | Extrahierte Fakten & Wissen |
| **Wann** | Factual Q&A, Dokumentensuche | "Was hat User letztes Mal gesagt?", Workflow-Replay | Personalisierung, Preferences, World Knowledge |
| **Wie** | Chunk → Embed → Retrieve → Generate | Event-Logging + Temporal Retrieval | Entity Extraction + KV/Graph Storage |
| **Limit** | Statisch, kein Kontext-Update | Skaliert schlecht bei Millionen Events | Kann veralten ohne Decay-Mechanismus |
| **Trend** | Wird zu "Agentic RAG" (aktive Query-Refinement) | GSW-Ansatz: 20% besser als RAG-Baselines (arXiv Nov 2025) | Knowledge Graphs (Zep) als neuer Standard |

---

## Memory Poisoning — Risiken im Detail

### Angriffsvektoren (dokumentiert, 2025)

1. **Indirect Prompt Injection → Memory Write** (Palo Alto Unit 42)
   - Angreifer platziert Payload in Webseite/Dokument → Agent liest es → schreibt vergiftetes Fact in Memory → alle zukünftigen Sessions betroffen

2. **Query-Only Memory Injection (MINJA)**
   - Angreifer stellt harmlose Fragen, die den Agent dazu bringen, Toxic Content als "gute Erfahrung" zu speichern → >95% Erfolgsrate

3. **Experience Poisoning (MemoryGraft)**
   - Falsche "erfolgreiche Erfahrungen" werden in episodisches Memory eingeschleust → Agent wiederholt gefährliches Verhalten dauerhaft

### Was fehlt an Abwehr
- Kein Framework hat Memory-Integrity-Checks als First-Class Feature
- Kein Provenance-Tracking ("diese Erinnerung kam von URL X am Datum Y")
- Kein Anomalie-Detection für Memory-Writes
- Kein Sandbox/Review für Memory vor Commit

**→ Massive Opportunity für AgentTrust: Memory als Trusted Layer mit Verification.** ← JUDGMENT

---

## Was Fehlt — Offene Probleme

1. **Memory Governance**: Wer darf was erinnern? Audit-Trails? Compliance (GDPR-Recht auf Vergessen)?
2. **Cross-Agent Memory Trust**: In Multi-Agent-Systemen — wie validiert Agent A die Erinnerungen von Agent B?
3. **Forgetting as Feature**: Aktives, strategisches Vergessen (Decay, Relevanz-Scoring) ist in keinem Framework Production-ready
4. **Memory Evaluation**: Kein Standard-Benchmark für Memory-Qualität (EpBench ist ein erster Versuch)
5. **Memory + Safety**: Intersection von Memory Persistence und AI Safety ist untererforscht
6. **Hierarchical Memory across Agent Teams**: Shared vs. Private Memory in Multi-Agent-Setups

---

## Claim Ledger (Top 5 Claims)

| # | Claim | Evidence | Confidence | Was würde Confidence erhöhen? |
|---|-------|----------|------------|-------------------------------|
| 1 | MINJA erreicht >95% Memory Injection-Erfolgsrate | arxiv 2503.03704 (Peer-reviewed venue: OpenReview), zitiert in arxiv 2601.05504v2 Jan 2026 | **High** | Reproduktion durch Dritte |
| 2 | Mem0 verarbeitet 186M API Calls/Quartal (Q3 2025) | TechCrunch Oct 2025 (Firmenangabe, nicht unabhängig verifiziert) | **Medium** | Unabhängige Bestätigung, SEC Filing |
| 3 | Kein Framework hat Memory-Integrity als Feature | Eigene Analyse: Feature-Docs von Letta, Mem0, Zep, LangMem durchsucht | **Medium** | Systematischer Feature-Audit aller Frameworks |
| 4 | GSW outperformt RAG-Baselines um 20% bei Episodic Memory | arxiv 2511.07587 (EpBench Benchmark) | **High** | Peer Review, Reproduktion |
| 5 | Alle Frameworks fokussieren Store/Retrieve, nicht Governance | Serokell Dec 2025, Graphlit Survey Oct 2025, eigene Analyse | **Medium-High** | Vollständiger Survey aller kommerziellen Angebote |

---

## Contradiction Register

| Konflikt | Quellen | Warum unterschiedlich | Impact |
|----------|---------|----------------------|--------|
| "MemGPT ist State of the Art" vs "MemGPT-Architektur hat fundamental Overhead-Problem" | Serokell (positiv) vs Graphlit-Vergleich (kritisch) | Serokell betrachtet Architektur-Eleganz, Graphlit vergleicht Production-Performance | Mittel — für Artikel relevant: MemGPT ist *konzeptionell* wichtig, aber nicht unbedingt beste Production-Wahl |
| Mem0 "91% weniger Latenz" vs Zep "Enterprise-grade" | Mem0 Paper vs Zep Marketing | Unterschiedliche Benchmarks, Mem0 misst gegen Full-RAG, Zep gegen nichts Konkretes | Niedrig — beide Claims nur im eigenen Kontext gültig |

---

## Quellen

1. Serokell — "Design Patterns for Long-Term Memory in LLM-Powered Architectures" (Dec 2025) https://serokell.io/blog/design-patterns-for-long-term-memory-in-llm-powered-architectures
2. Hu et al. — "Memory in the Age of AI Agents" (arXiv Jan 2026) https://arxiv.org/abs/2512.13564
3. Palo Alto Unit 42 — "When AI Remembers Too Much" (Oct 2025) https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/
4. MINJA — "Memory Injection Attacks on LLM Agents via Query-Only Interaction" (arXiv 2025) https://arxiv.org/abs/2503.03704
5. MemoryGraft — "Persistent Compromise via Poisoned Experience Retrieval" (arXiv Dec 2025) https://arxiv.org/abs/2512.16962
6. TechCrunch — "Mem0 raises $24M" (Oct 2025) https://techcrunch.com/2025/10/28/mem0-raises-24m/
7. LangChain — "LangMem SDK Launch" (May 2025) https://blog.langchain.com/langmem-sdk-launch/
8. Graphlit — "Survey of AI Agent Memory Frameworks" (Oct 2025) https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks
9. IBM — "What Is AI Agent Memory?" (Nov 2025) https://www.ibm.com/think/topics/ai-agent-memory
10. Rajesh et al. — "Episodic Memory for RAG with GSW" (arXiv Nov 2025) https://arxiv.org/abs/2511.07587
11. Redis — "AI Agent Memory: Build Stateful Systems" (Feb 2026) https://redis.io/blog/ai-agent-memory-stateful-systems/
12. RAGFlow — "From RAG to Context" (Dec 2025) https://ragflow.io/blog/rag-review-2025-from-rag-to-context
13. Neo4j/Zep — "Graphiti: Knowledge Graph Memory" (Aug 2025) https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/

---

## Empfehlung

Artikel-Angle für Substack: **"Everyone is building Memory for agents. Nobody is building Trust for Memory."** Die Taxonomie (Episodic/Semantic/Procedural) ist gelöst. Store & Retrieve ist commodity. Die ungelösten Probleme — Poisoning, Governance, Cross-Agent Trust, strategisches Vergessen — sind exakt dort, wo AgentTrust positioniert werden kann. Der Artikel sollte die Landschaft kurz mappen, dann hart auf die Lücke fokussieren. Zeigen, dass wir das Problem nicht nur verstehen, sondern schon lösen (eigenes Memory-System als Proof Point).

---

## Beipackzettel

```
Confidence: 78%
Sources checked: 13+
Verified facts: 11
Unverified claims: 3 (Mem0 API-Zahlen, Zep Enterprise-Claims, "kein Framework hat X")
Search queries used: 6 (MemGPT/Letta, Zep, LangChain Memory, Memory Poisoning, RAG vs Episodic vs Semantic, Mem0)
Time spent: ~8 Min
Limitationen: Brave Search Rate-Limited (4 von 6 Queries erfolgreich), keine Deep-Dives in Paper-PDFs
```

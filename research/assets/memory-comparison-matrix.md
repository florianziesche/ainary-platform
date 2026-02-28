# AI Agent Memory Systems: Comparison Matrix

**Date:** 2026-02-27
**Report:** R22-ai-agent-memory-systems

---

## Full Comparison

| Dimension | Anthropic Claude Code | OpenAI ChatGPT Memory | Mem0 | Zep | Letta/MemGPT | HippoRAG | LangChain/LangMem | Mia/OpenClaw |
|-----------|----------------------|----------------------|------|-----|--------------|----------|-------------------|--------------|
| **Architecture Type** | Flat markdown files | Key-value pairs + conversation refs | Vector DB + optional graph | Temporal Knowledge Graph (Graphiti) | Tiered: core + archival + recall | Knowledge Graph + PageRank | Pluggable (buffer/summary/vector) | Multi-layer hierarchy + embeddings + KG |
| **Storage** | Local filesystem (~/.claude/) | Cloud, opaque | Vector store (Qdrant, etc.) + optional graph DB | Neo4j-based temporal graph | SQLite/Postgres + vector store | In-memory KG | Depends on backend | Obsidian vault + Voyage AI embeddings |
| **Retrieval Method** | First 200 lines loaded linearly | Opaque, injected into system prompt | Embedding similarity search | Graph traversal + temporal filtering | LLM-managed paging (virtual memory model) | Personalized PageRank over KG | Backend-dependent | 5-layer: embedding search → vault search → backlink graph → live data → web |
| **Update/Decay** | Append-only, no decay, 200-line cap | Manual delete only | Auto-filtering, decay mechanisms | Temporal validity (date ranges), bitemporal | Agent-managed archival | None (research prototype) | None built-in | Memory-R1 filter + Claim Ledger + Contradiction Register + anti-entropy |
| **Cross-Session** | Yes (files persist) | Yes (saved memories persist) | Yes (by design) | Yes (persistent graph) | Yes (persistent DB) | Limited (single-run focus) | Backend-dependent | Yes (Obsidian vault + daily episodic logs) |
| **Multi-Agent** | Project CLAUDE.md via git only | None | User-scoped sharing | Thread + user graph sharing | Conversations API (Jan 2026) | None | None built-in | SUB-AGENT-CONTEXT.md inheritance + AgentTrust scoring |
| **Fact-Checking** | None | None | None | Provenance tracking (who/when) | None (agent can self-edit, risk of hallucination persistence) | Structural consistency via KG | None | EIJA labels + verified-truths.md + Claim Ledger with invalidation conditions |
| **Knowledge Graph** | None | None | Optional (recent addition) | Core architecture (Graphiti) | None | Core architecture (LLM-built KG) | None | Obsidian wikilinks + backlinks.json |
| **Hierarchy/Weighting** | Directory hierarchy (project > user > managed) | Flat (all memories equal) | Flat | Flat (temporal ordering) | Core vs archival (2 tiers) | Flat (PageRank provides implicit ranking) | Flat | 4-tier weighted: CORE 2x, KNOWLEDGE 1.5x, OPERATIONAL 1x, EPHEMERAL 0.5x |
| **Human Feedback Loop** | None | User can add/delete memories | None | None | None | None | None | AgentTrust scoring updated by Florian's feedback (good/bad signals) |
| **Open Source** | No (proprietary tool) | No | Yes (MIT) | Partial (Graphiti open, platform closed) | Yes (Apache 2.0) | Yes (MIT) | Yes (MIT) | Private (workspace-specific) |
| **Production-Ready** | Yes (shipped in v2.1.32) | Yes (GA since Feb 2024) | Yes (used by enterprises, AWS integration) | Yes (enterprise product) | Yes (platform + API) | No (research prototype) | Yes (framework component) | Yes (6+ months production use) |

---

## Verdicts

### Anthropic Claude Code
**Level 1 (Flat Store).** The simplest possible memory: markdown files loaded at session start. No semantic search, no decay, no fact-checking. Good enough for coding context. Not a memory system.

### OpenAI ChatGPT Memory
**Level 2 (Structured Store).** Key-value memories with opaque retrieval. April 2025 upgrade adds conversation-history referencing. Better than Claude Code but still flat, no graph, no verification.

### Mem0
**Level 3 (Semantic Store).** Solid vector-based memory with proven benchmarks (26% accuracy improvement, 90% token savings). Good production story. Missing: knowledge graph depth, fact verification, hierarchy.

### Zep
**Level 4 (Knowledge Graph).** The strongest competitor in this set. Temporal KG with bitemporal modeling is genuinely novel. Missing: epistemological trust, weighted hierarchy, human feedback loop.

### Letta/MemGPT
**Level 3 (Semantic Store).** Innovative OS-inspired virtual memory model. Agent manages its own memory. Risk: self-editing without verification can persist hallucinations. New Conversations API is promising.

### HippoRAG
**Level 4 (Knowledge Graph, research-only).** Elegant neuroscience-inspired design. NeurIPS'24. Not production-ready. Single-agent only. No decay or fact-checking.

### LangChain/LangMem
**Level 2-3 (Pluggable).** Framework, not a solution. LangMem SDK (May 2025) adds semantic extraction but still requires developer assembly. No opinions on hierarchy or trust.

### Mia/OpenClaw
**Level 5 (Compound Intelligence).** The only system in this comparison that combines: multi-layer hierarchy with explicit weighting, epistemological trust labels (EIJA), systematic fact verification (verified-truths.md), noise prevention (Memory-R1), cross-agent context inheritance, human feedback scoring, and an anti-entropy principle. 6+ months production use with continuous refinement.

---

*Matrix compiled from official documentation, academic papers, and GitHub repositories. See R22 report for full source list.*

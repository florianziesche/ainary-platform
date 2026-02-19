# Ainary Research

**Deep-dive research reports on AI trust, governance, and calibration.**

10 published reports covering agent memory, calibration methods, multi-agent coordination, cost optimization, governance, observability, municipal AI, business model transitions, prompt engineering, and VC strategy.

---

## Reports

| ID | Title | Quality | Key Finding |
|----|-------|---------|-------------|
| **AR-016** | **Agent Memory Architecture 2026** | R1 | Hierarchical memory (MemGPT) outperforms flat RAG by 10-12% in long-context benchmarks. RAG is insufficient for agent memory but useful for knowledge retrieval. |
| **AR-017** | **Cost of AI Agent Operations** | R1 | Multi-model routing (Haiku/Sonnet/Opus) reduces costs by 60-80% vs. pure GPT-4. Strategic model selection based on task complexity critical for production economics. |
| **AR-018** | **Multi-Agent Coordination Patterns** | R1 | Shared memory patterns enable 3x throughput vs. sequential chains. Communication overhead becomes bottleneck at >5 agents. |
| **AR-019** | **AI Governance for European Enterprise** | R1 | Compliance burden: 40-60 hours/project for GDPR + AI Act. Documentation requirements exceed technical implementation time for small deployments. |
| **AR-020** ⭐ | **Trust Calibration Methods** | R2 | **RLHF destroys calibration.** Consistency-based methods (Budget-CoCoA) achieve 27% ECE vs. 42% verbalized confidence. Multi-agent confidence propagation is an open research gap. |
| **AR-021** | **The Agent Observability Stack** | R1 | LangSmith + Weights & Biases = production standard. Distributed tracing essential for multi-agent debugging. Observability cost: ~15% performance overhead. |
| **AR-022** | **AI in Municipal Government** | R1 | Adoption limited by procurement processes, not technology. 18-24 month cycles. Pilots don't scale without policy change. |
| **AR-023** | **From Consulting to SaaS** | R1 | Services-first strategy de-risks product development. Productized consulting generates revenue while validating product-market fit. |
| **AR-024** | **Prompt Engineering at Scale** | R1 | Version control + A/B testing mandatory for production prompts. Prompt drift degrades performance by 10-15% over 3 months without monitoring. |
| **AR-025** | **The Operator Advantage in VC** | R1 | Operating experience correlates with fund performance in AI/infrastructure deals. Operator-VCs outperform by 1.2-1.5x IRR in technical categories. |

---

## Methodology

### R1: Speed Batch
- **Sources:** 10 papers/articles
- **Length:** ~2,000 words
- **Time:** 2-3 hours
- **Process:** Intake → Extract → Synthesize → Write → Quality check
- **Cost:** ~$1.50/report (multi-model routing)

### R2: Deep Dive
- **Sources:** 20+ papers/articles
- **Length:** 4,000+ words
- **Hypotheses:** 5 explicitly stated upfront
- **Quality Gate:** 15/15 points across 5 dimensions
- **Time:** 6-8 hours
- **Cost:** ~$5-8/report

**Quality Gate Dimensions (R2 only):**
1. **Evidence Quality** (3 pts): Citations from peer-reviewed sources, recent (<2 years), diverse perspectives
2. **Synthesis Depth** (3 pts): Cross-references, pattern identification, contradictions resolved
3. **Actionability** (3 pts): Clear recommendations, implementation guidance, ROI estimates
4. **Epistemic Honesty** (3 pts): Uncertainties stated, limitations acknowledged, confidence calibrated
5. **Writing Quality** (3 pts): Clear structure, no LLM phrases, persuasive narrative

**Pass threshold:** ≥12/15

---

## Research Highlights

### AR-020: Trust Calibration Methods (R2 Deep Dive)

**Thesis:** RLHF systematically destroys LLM calibration, making external calibration non-optional.

**5 Hypotheses:**
1. ✅ Self-consistency outperforms verbalized confidence (confirmed: 27% vs. 42% ECE)
2. ✅ RLHF degrades both logit and verbal calibration (confirmed: structural bias)
3. ✅ Conformal prediction provides distribution-free guarantees (confirmed: but requires calibration set)
4. ⚠️ Temperature scaling is inaccessible in production (confirmed: but GPT-4 has top-5 logprobs)
5. ❌ Multi-agent calibration methods exist in literature (REFUTED: research gap identified)

**Novel Contribution:** Identified multi-agent confidence propagation as an open research problem. No existing framework addresses how confidence should propagate through agent chains.

**Impact:** Informed design of Ainary Calibration Library. Directly led to implementation of 3 propagation methods (Multiplicative, Bayesian Network, Conservative).

[→ Full report](AR-020-trust-calibration-methods.md)

---

### AR-016: Agent Memory Architecture (R1)

**Key Insight:** RAG is not agent memory. RAG retrieves static knowledge. Agent memory requires:
- Forgetting strategies (when to evict old information)
- Consolidation (merge redundant facts)
- Priority management (what's important vs. noise)
- Context awareness (conversation state vs. long-term facts)

**Architectures Compared:**
1. **Pure RAG:** Stateless, deterministic, good for knowledge retrieval
2. **MemGPT/Letta:** OS-inspired tiered memory (main context = RAM, archival = disk)
3. **Mem0:** Hybrid extraction (dynamically extract salient facts, consolidate)

**Benchmark:** Mem0 achieved 67-68% accuracy vs. RAG's 61% on LOCOMO (long-context memory benchmark).

**Recommendation:** Use RAG for knowledge retrieval, dedicated memory systems (MemGPT or Mem0) for agent state.

[→ Full report](AR-016-agent-memory-architecture-2026.md)

---

### AR-017: Cost of AI Agent Operations (R1)

**Economic Reality:** Pure GPT-4 agents burn $500-1000/month at moderate usage (50-100 tasks/day).

**Cost Reduction Strategies:**
1. **Multi-model routing:** Route to cheapest capable model (60-80% savings)
   - Haiku: $0.25/MTok in → Extraction, summarization
   - Sonnet: $3/MTok in → Synthesis, analysis
   - Opus: $15/MTok in → Final writing, opinionated analysis
2. **Caching:** Anthropic prompt caching reduces repeat context costs by 90%
3. **Batch processing:** Defer non-urgent tasks, process in batches
4. **Selective prediction:** Abstain on low-confidence tasks, route to cheaper human review

**Target:** $200/month for research + execution platform (150 reports + 500 conversations).

[→ Full report](AR-017-cost-of-ai-agent-operations.md)

---

## Research Pipeline

Automated report generation using the **Research Pipeline** project.

**Pipeline Stages:**
1. **Intake** — Fetch papers from arXiv, Semantic Scholar, RSS feeds (Haiku)
2. **Extract** — Pull key findings, methods, results from each paper (Haiku)
3. **Synthesize** — Cross-reference findings, identify patterns (Sonnet)
4. **Write** — Generate report from template (Opus)
5. **Quality Gate** — Self-audit, source verification (Sonnet)
6. **Publish** — Git push + optional Vercel deploy

**Cost per R1 report:** ~$1.34  
**Cost per R2 report:** ~$5-8

[→ Research Pipeline README](../projects/research-pipeline/README.md)

---

## Asset Packs

For AR-020 (Trust Calibration), we extracted reusable knowledge assets:

- **[AR-020-v3-assets.md](AR-020-v3-assets.md)** — Atomic notes, calibration methods, research gaps
- **[AR-020-v3-obsidian.md](AR-020-v3-obsidian.md)** — Obsidian Vault integration format

These assets feed into:
- AgentTrust library design
- Calibration Library implementation
- Consulting talking points
- Content pipeline

**Asset Types:**
1. **Atomic Notes:** Single-concept cards with confidence ratings
2. **Method Cards:** Implementation-ready technique summaries
3. **Research Gaps:** Open problems for future investigation
4. **Talking Points:** Client-ready explanations

---

## Using Research in Projects

### AgentTrust Library
- **AR-020** → Budget-CoCoA implementation, trust scoring design
- **AR-016** → Memory architecture decisions (MemGPT-inspired tiers)

### Calibration Library
- **AR-020** → 6 calibration method families, 4 experiments
- **AR-017** → Multi-model routing strategy

### Execution Platform
- **AR-021** → Observability design (event log, audit trail)
- **AR-018** → Multi-agent coordination (action queue, shared state)

### Consulting
- **AR-019** → EU compliance burden estimates
- **AR-022** → Municipal AI adoption playbook
- **AR-023** → Services-first go-to-market

---

## Research Backlog

**Planned Future Reports:**
- AR-026: Prompt Versioning Systems (draft 40% complete)
- AR-027: AI Agent Security Patterns (collecting sources)
- AR-028: Semantic Search for Personal Knowledge (Obsidian + embeddings)
- AR-029: Agent Framework Comparison (LangChain vs. CrewAI vs. AutoGen)
- AR-030: Trust Scoring for Multi-Agent Systems

**Research Questions:**
1. How should confidence propagate in agent chains with correlation?
2. What's the optimal abstention threshold for selective prediction?
3. Can we predict calibration degradation from prompt drift?
4. What's the ROI of observability overhead in production agents?

---

## Citation

If you reference these reports, use:

```
Ziesche, F. (2026). [Report Title]. Ainary Research Series AR-0XX.
https://github.com/ainary/research
```

Example:
```
Ziesche, F. (2026). Trust Calibration Methods for AI Agents. 
Ainary Research Series AR-020. https://github.com/ainary/research
```

---

## Related Documentation

- **[Platform README](../README.md)** — Overview of Ainary Platform
- **[Research Pipeline README](../projects/research-pipeline/README.md)** — How reports are generated
- **[Calibration Library README](../projects/ainary-calibration/README.md)** — Implementation of AR-020 findings
- **[AgentTrust README](../projects/agenttrust/README.md)** — Trust infrastructure based on AR-020

---

**Maintained by:** Florian Ziesche  
**Last Updated:** 2026-02-19  
**Total Reports:** 10 (6 R1, 1 R2, 3 exploratory)

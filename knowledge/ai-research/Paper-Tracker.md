---
type: tracker
status: active
created: 2026-02-19
review_date: 2026-03-19
tags: [research, papers, sota, agent-trust]
tier: OPERATIONAL
expires: 2026-08-20
---

# AI Research Paper Tracker

**Purpose:** Track papers relevant to AgentTrust, Ainary, and AI agent development.  
**Review Cycle:** Monthly (next review: 2026-03-19)  
**Tagging:** Papers move through Reading Queue → In Progress → Completed

**Related:** [[AR-001 State of Agent Trust]] | [[Claims-Ledger]] | [[Findings-Snapshot]] | [[Knowledge-MOC]]

---

## Reading Queue

Papers identified but not yet read in full.

### Memory in the Age of AI Agents
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2512.13564  
- **Authors:** Yuyang Hu, Shichun Liu, Guibin Zhang et al.  
- **Date:** Dec 2025 (updated Jan 2026)  
- **Type:** Survey  
- **Why relevant:** Comprehensive memory taxonomy (token/parametric/latent), identifies trustworthiness as research frontier  
- **Priority:** HIGH — Informs AgentTrust memory tracking architecture  
- **Added:** 2026-02-19

### Agentic Memory (AgeMem)
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2601.01885  
- **Authors:** Yi Yu et al.  
- **Date:** Jan 2026  
- **Type:** Implementation (code available)  
- **Why relevant:** Unified LTM+STM management via RL, memory as tool-based actions  
- **Priority:** HIGH — Implementation pattern for Ainary agent memory  
- **Added:** 2026-02-19

### OpenSec: Incident Response Agent Calibration
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2601.21083  
- **Authors:** Jarrod Barnes et al.  
- **Date:** Jan 2026 (updated Feb 2026)  
- **Type:** Benchmark + Code (https://github.com/jbarnes850/opensec-env)  
- **Why relevant:** DIRECTLY measures trust calibration under adversarial conditions — our core problem  
- **Priority:** CRITICAL — Potential validation benchmark for AgentTrust  
- **Added:** 2026-02-19  
- **Action:** Contact author for collaboration

### TRiSM for Agentic AI
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/html/2506.04133v5  
- **Authors:** Diverse  
- **Date:** Dec 2025  
- **Type:** Framework  
- **Why relevant:** Trust, Risk, Security Management framework — conceptually what AgentTrust implements  
- **Priority:** MEDIUM — Positioning/messaging alignment  
- **Added:** 2026-02-19

### Survey of Agentic AI and Cybersecurity
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/html/2601.05293v1  
- **Authors:** Diverse  
- **Date:** Jan 2026  
- **Type:** Survey  
- **Why relevant:** Confirms trust calibration as open problem, augmentation > replacement pattern  
- **Priority:** MEDIUM — Market validation  
- **Added:** 2026-02-19

---

## In Progress

Papers currently being read/analyzed.

*(Empty — populate when starting a paper)*

**Template for new entries:**
```markdown
### Paper Title
- **Status:** 📖 Reading  
- **Link:** URL  
- **Started:** YYYY-MM-DD  
- **Progress:** XX% or "Section 3 of 5"  
- **Notes:** [[linked-note-file]]
```

---

## Completed

Papers fully read with key takeaways extracted.

*(Empty — will populate as papers are completed)*

**Template for completed entries:**
```markdown
### Paper Title
- **Status:** ✅ Completed  
- **Link:** URL  
- **Read:** YYYY-MM-DD  
- **Key Takeaways:**  
  - Takeaway 1  
  - Takeaway 2  
  - Takeaway 3  
- **Applied to:** [Project/Product]  
- **Notes:** [[detailed-notes-file]]
```

---

## Key Takeaways

Consolidated insights across all completed papers (auto-updated as papers are finished).

### Cross-Paper Themes (from Feb 2026 scan)

1. **Memory is the new RAG** — 2026 focus shifted from RAG vs long-context to memory management (AgeMem, MemGPT patterns)
2. **Calibration ≠ Accuracy** — Agents detect correctly but act incorrectly (timing, false positives)
3. **Explainability is mandatory** — Enterprise deployment without explainability = non-starter (TRiSM framework)
4. **HITL stays** — No paper shows full autonomy working; augmentation > replacement
5. **Trust is an open problem** — Multiple papers identify it, none solve it → AgentTrust opportunity

---

## Research Gaps (from SOTA scan)

**What's missing in current literature:**
1. Production metrics (real-world deployments, not just benchmarks)
2. Cost analysis ($/trust-check, ROI of calibration)
3. Multi-agent trust (how Agent A uses Agent B's trust score)
4. Guardrail composition (which stack, which conflict)
5. Regulatory compliance guides (FDA/HIPAA conceptual, no implementation)

**Implication:** Each gap = Ainary consulting opportunity + AgentTrust feature.

---

## Search Queries (for future scans)

**Monthly searches to run:**
- `arxiv agent trust calibration [current-year]`
- `arxiv multi-agent memory [current-year]`
- `arxiv AI governance enterprise [current-year]`
- `arxiv LLM observability production [current-year]`
- `arxiv agentic workflows HITL [current-year]`

**Filters:**
- Date: Last 30 days
- Sort: Relevance (not recency — quality > speed)
- Minimum: 5 citations (for older papers)

---

## Collaboration Opportunities

**Authors to contact:**
- **Jarrod Barnes** (OpenSec) — Potential AgentTrust integration
- **Yi Yu** (AgeMem) — Implementation pattern questions
- **Guibin Zhang** (Memory survey) — Cite our work when we publish

**Next scan:** 2026-03-19 (monthly cadence)

---

## Workflow

### Adding a Paper
1. Find paper (monthly search or ad-hoc)
2. Add to **Reading Queue** with metadata
3. Assign priority (CRITICAL / HIGH / MEDIUM / LOW)
4. Move to **In Progress** when starting
5. Move to **Completed** when done, extract key takeaways

### Review Cycle
- **Monthly:** Run search queries, add new papers to queue
- **Quarterly:** Re-prioritize queue based on product roadmap
- **Yearly:** Archive papers >12 months old with no relevance

### Integration
- Link completed papers to relevant projects in `[[projects/]]`
- Cross-reference takeaways in `[[memory/findings/]]`
- Update `[[verified-truths.md]]` with confirmed claims

---

**Tracker Status:** ✅ Active  
**Papers Tracked:** 5 in queue, 0 in progress, 0 completed  
**Next Review:** 2026-03-19  
**Maintained by:** Mia (Research Agent)

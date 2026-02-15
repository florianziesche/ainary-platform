# Vault Architecture Compounding Experiment

**Date:** 2026-02-15
**Researcher:** Ainary AI Research (automated)
**Status:** Complete

---

## Objective

Test whether knowledge architecture affects compounding — the ability of stored knowledge to generate insights beyond what was explicitly stored. Compare 5 Obsidian vault architectures using identical content from 9 Ainary Research Reports (AR-001 through AR-009).

## Hypotheses

1. **H1:** Densely linked architectures (Zettelkasten, Graph-First) score higher on Inference and Emergence questions than Flat or PARA
2. **H2:** Flat architecture scores competitively on Retrieval (simple find-and-return)
3. **H3:** MOC-Hybrid offers best balance of effort vs. compounding
4. **H4:** Graph-First's metadata richness improves self-reference but increases maintenance overhead

## 5 Vault Architectures

| Vault | Architecture | Folders | Links/Note | Metadata |
|-------|-------------|---------|------------|----------|
| A | FLAT (Control) | 0 | 0 | Tags only |
| B | PARA | 4 (P/A/R/A) | 0-2 (within project) | Minimal |
| C | ZETTELKASTEN | 0 (index notes only) | 3+ (dense) | Sequence IDs |
| D | MOC-HYBRID | 6 (00-50) | 1-3 (moderate) | Moderate frontmatter |
| E | GRAPH-FIRST | 0 | 5+ (maximum) | Rich (type, status, confidence, source, created, modified) |

## Content Set (50 Notes)

Extracted from AR-001 through AR-009:

### 30 Atomic Claims (C-001 to C-030)
### 10 Key Concepts (K-001 to K-010)
### 5 Cross-Cutting Insights (I-001 to I-005)
### 5 Decisions (D-001 to D-005)

See each vault for implementation.

## Test Protocol

### 10 Questions in 3 Categories

**Category 1: RETRIEVAL**
- Q1: "What is the HITL failure rate in security operations?"
- Q2: "Which report covers memory architecture?"
- Q3: "What did we decide about report template design?"

**Category 2: INFERENCE**
- Q4: "How does alert fatigue relate to memory corruption?"
- Q5: "What's the connection between developer adoption barriers and trust moat theory?"
- Q6: "If calibration improves, what happens to HITL effectiveness?"
- Q7: "Which failure mode from AR-010 is most relevant to financial services?"

**Category 3: EMERGENCE**
- Q8: "What's the biggest blind spot across all 15 reports?"
- Q9: "What research topic should AR-016 cover, based on gaps in AR-001-015?"
- Q10: "Propose a product feature that addresses findings from at least 3 reports."

### 5 Metrics per Question

1. **Answer Quality** (0-10): Correctness, specificity, evidence
2. **Time to Answer** (simulated seconds): Navigation hops to find/derive
3. **Sources Referenced** (count): Notes that contributed
4. **Emergence Score** (0-10): Insight beyond any single note
5. **Self-Reference** (yes/no): Cited internal knowledge vs external

## Methodology Notes

- Content is identical across vaults; only organization differs
- "Time to Answer" is estimated based on structural navigation hops (flat=search, PARA=folder drill, Zettelkasten=link traversal, MOC=hub-and-spoke, Graph=multi-path)
- Scoring is done by the same AI model reading each vault in isolation
- We acknowledge this tests *AI retrieval from structure*, not human UX — but this is the relevant proxy for AI-augmented knowledge work
- AR-010 through AR-015 don't exist in the vault — Q7 tests graceful handling of missing references
- Only 9 reports exist (not 15) — Q8/Q9 are adjusted to cover AR-001 through AR-009

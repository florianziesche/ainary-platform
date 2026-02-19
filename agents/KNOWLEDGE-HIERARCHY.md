# Knowledge Hierarchy — What We Know and How Much We Trust It

*Last updated: 2026-02-19*
*Total chunks in RAG: 936 | 4 tiers*

---

## TIER 1: CORE (2x weight) — Verified, empirical

These are ground truth. Corrections override everything else.

| File | Path | Last Updated | Chunks | Key Topics |
|------|------|-------------|--------|------------|
| compounding-research-truths.json | `research-base/compounding-research-truths.json` | 2026-02-19 | 27 | Calibration, RLHF damage, auxiliary models, ECE, prompting limits, confidence estimation |
| corrections.json | `research-base/corrections.json` | 2026-02-19 | 7 | Factual corrections to claims made in reports — wrong→right with source |
| reference-library.json | `research-base/reference-library.json` | 2026-02-19 | 14 | Peer-reviewed papers with DOIs, key findings, venue, tier rank |

**Total CORE chunks: 48**

---

## TIER 2: KNOWLEDGE (1.5x weight) — Peer-reviewed, curated

Curated knowledge files from Obsidian vault. High signal, manually assembled.

| File | Path | Last Updated | Chunks | Key Topics |
|------|------|-------------|--------|------------|
| Top-20-Papers-AUDITED.md | `~/…/Knowledge/Top-20-Papers-AUDITED.md` | 2026-02-19 | 111 | ReAct, MemGPT, Toolformer, LATS, Voyager, Generative Agents, MetaGPT, agent architecture |
| Agent-Developments-Jan-Feb-2026.md | `~/…/Knowledge/Agent-Developments-Jan-Feb-2026.md` | 2026-02-19 | 42 | MCP, Claude Opus, Cursor, coding agents, browser use, production reports |
| Cross-Pattern-Insights.md | `~/…/Knowledge/Cross-Pattern-Insights.md` | 2026-02-19 | 83 | Cross-domain patterns, journalism, CNC, government, novelty checks, confidence scores |
| Compound-Machine-Architecture.md | `~/…/Knowledge/Compound-Machine-Architecture.md` | 2026-02-19 | 73 | Compound machine design, sprint architecture, knowledge flywheel, system design |
| AI-Memory-Self-Improvement.md | `~/…/60_Resources/AI/AI-Memory-Self-Improvement.md` | 2026-02-19 | 79 | Memory architectures, self-improvement, MINJA poisoning, calibration, trust |

**Total KNOWLEDGE chunks: 388**

---

## TIER 3: OPERATIONAL (1x weight) — Current state, projects

Working knowledge about ongoing projects, people, and accumulated learnings.

| File | Path | Last Updated | Key Topics |
|------|------|-------------|------------|
| projects.md | `memory/knowledge/projects.md` | 2026-02-19 | Ainary, AgentTrust, CNC, website, pipeline status |
| people.md | `memory/knowledge/people.md` | 2026-02-19 | Contacts, family, VC targets, relationships |
| AR-INDEX.md | `agents/AR-INDEX.md` | 2026-02-19 | 26 AR-IDs, 32 versions, report registry |
| META-LEARNINGS.md | `agents/META-LEARNINGS.md` | 2026-02-19 | 19 learnings from 30+ reports, quality/process failures, proven patterns |
| CHANGELOG.md | `agents/CHANGELOG.md` | 2026-02-15 | Pipeline version history, CL-001 to CL-006 |
| A-PLUS-PIPELINE-v2.md | `agents/A-PLUS-PIPELINE-v2.md` | 2026-02-15 | v2.3 pipeline spec, 9 phases, spawn templates |

**Not chunked in RAG — loaded on demand by agents.**

---

## TIER 4: EPHEMERAL (0.5x weight) — Daily context

High volume, low permanence. Session-specific context that decays.

| File | Path | Last Updated | Key Topics |
|------|------|-------------|------------|
| daily/*.md | `memory/daily/` | Rolling (45 files) | Session logs, decisions, discoveries, TODO |
| vault-index/embeddings.json | `vault-index/embeddings.json` | varies | Obsidian note embeddings (first 500 loaded) |
| research/inbox/*.md | `research/inbox/` | Rolling | Raw research intake, unsorted |

**Total EPHEMERAL chunks in RAG: ~500 (capped)**

---

## RAG Tier Boost Summary

| Tier | Boost | Purpose | Example |
|------|-------|---------|---------|
| CORE | 2.0x | Ground truth, corrections override all | "RLHF damages calibration" (CT-001) |
| KNOWLEDGE | 1.5x | Curated reference, peer-reviewed | "ReAct is foundation for agent loops" |
| OPERATIONAL | 1.0x | Current state, working memory | "AR-020 is at v5" |
| EPHEMERAL | 0.5x | Daily noise, session context | "Florian said X on Feb 14" |

---

## How It Works

1. `load_default_sources()` in `rag_layer.py` ingests CORE + KNOWLEDGE + EPHEMERAL automatically
2. BM25 scores are multiplied by tier boost before ranking
3. CORE results surface first even with lower keyword match — by design
4. KNOWLEDGE vault files are chunked at ~500 chars at paragraph boundaries
5. Query with `tier_filter=["CORE", "KNOWLEDGE"]` to exclude noise

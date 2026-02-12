# Memory Principles
*Domain: Memory management, knowledge organization*
*Extracted from: Memory papers + own architecture*

## P-ME-01: Curated > Raw (10x Access, 90% Cheaper)
- **Score:** 90
- **Source:** Mem0 (arXiv:2504.19413), own observation
- **Rule:** Curated semantic memory over raw daily logs. Aggressive pruning.
- **Evidence:** Mem0: 26% quality, 91% latency, 90% cost. MEMORY.md accessed 10x more than daily logs.
- **Validates:** 2x
- **Violates:** 0x

## P-ME-02: Forgetting = Feature
- **Score:** 75
- **Source:** Cognitive Science (Ebbinghaus), Mem0, Memory-R1
- **Rule:** Not everything needs to be remembered. 70% of daily events can be forgotten.
- **Evidence:** Human brain forgets 70% in 24h. Memory-R1: DELETE operations improve quality.
- **Validates:** 1x
- **Violates:** 0x (but not yet implemented!)

## P-ME-03: HEARTBEAT = Sleep Consolidation
- **Score:** 70
- **Source:** Cognitive Science (Born et al.), own architecture
- **Rule:** Periodic consolidation (episodic → semantic) during heartbeats = artificial sleep.
- **Evidence:** Validated concept by Memory papers. Implementation exists (HEARTBEAT.md) but not systematic.
- **Validates:** 1x (concept validated, execution untested)
- **Violates:** 0x

## P-ME-04: Memory = Active Agent, Not Storage
- **Score:** 65
- **Source:** Memory-R1 (arXiv:2508.19828), A-MEM
- **Rule:** Memory operations (ADD/UPDATE/DELETE/NOOP) should be deliberate decisions, not passive accumulation.
- **Evidence:** Memory-R1: 28% improvement with only 152 training examples. Currently implementing.
- **Validates:** 0x (just learned today)
- **Violates:** 0x

## P-ME-05: Entity-Keyed > Flat Files
- **Score:** 60
- **Source:** DualRAG, A-MEM (Zettelkasten), EvolveR
- **Rule:** Organize memory by entity (person, project, concept) not chronologically.
- **Evidence:** A-MEM's linking improves cross-referencing. DualRAG's entity-keyed outline enables demand-driven retrieval.
- **Validates:** 0x (partially implemented in semantic/ folder)
- **Violates:** 0x

## P-ME-06: Auto-Load > Manual-Load
- **Score:** 50
- **Source:** Kintsugi #10 (2026-02-13)
- **Rule:** Principles that are NOT auto-loaded will be forgotten. Critical rules must be in SOUL.md or MEMORY.md (both auto-loaded).
- **Evidence:** "Send First" existed in product.md (manual load) but not in MEMORY.md → Mia forgot → 0 sends on 2026-02-12.
- **Validates:** 1x
- **Violates:** 0x

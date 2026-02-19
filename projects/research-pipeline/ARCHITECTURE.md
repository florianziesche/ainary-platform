# MIA Pipeline — Architecture

> Design decisions, data flow, and why things are the way they are.

---

## Design Principles

### The 3 Laws

1. **Opus receives only.** Invents no facts. Connects what RAG + research brief provide.
2. **Sonnet speaks only to Python.** Never to Opus. Never to other Sonnet. (v4: isolated researchers)
3. **Python everywhere deterministic.** Validation, grading, merge, Beipackzettel — all Python.

### Why These Laws?

**Hallucination Isolation.** If Opus hallucinates, Python catches it in Phase D (validation). If Sonnet hallucinates (v4), it can't contaminate Opus because they never talk directly — Python mediates.

**Reproducibility.** Same input → same validation result. LLM output varies, but the quality gate is deterministic.

**Cost Control.** Python validation is free. LLM calls are expensive. Do everything possible in Python.

---

## Pipeline Phases

### Phase A: Outline (1 Opus call)

**Input:** Research brief + RAG top-k results for the topic + workspace data (CRTs, corrections)

**Output:** JSON outline with 7 sections, each containing:
- `title`: Argument-style title ("Nobody's Calibrating" not "Market Overview")
- `word_target`: Minimum words
- `topics`: What to cover
- `assigned_claims`: Which CRTs/claims to reference
- `rag_context`: Top-k RAG chunks for this section

**Why Outline-First?**
- Produces more coherent reports than single-call or 2-call approaches
- Each section gets focused context (RAG per section, not entire knowledge base)
- Enables per-section validation and retry
- Opus plans before writing → better narrative arc

### Phase B: Sections (7 Opus calls, sequential)

Each section is generated independently with:
- The outline contract (title, word target, topics)
- Assigned RAG chunks (tier-boosted)
- All previously generated sections (for consistency)
- System prompt enforcing E/I/J/A badges and source citations

**Per-section validation (Python):**
1. Word count ≥ minimum
2. No banned words (landscape, tapestry, delve, synergy, cutting-edge, game-changer)
3. E/I/J/A badges present
4. Section confidence stated
5. Assigned sources referenced

If validation fails → retry once with error feedback.

### Phase C: Merge (Python, 0 LLM)

- Concatenates sections in order
- Generates Beipackzettel from validation data
- Counts total words, E/I/J/A distribution
- Extracts all source references

### Phase D: Validate (Python, 0 LLM)

13 deterministic checks:

| # | Check | Threshold |
|---|---|---|
| 1 | E ratio | > 50% |
| 2 | J ratio | < 20% |
| 3 | Total words | > 3000 |
| 4 | All 7 sections present | 7/7 |
| 5 | No orphan sources | 0 |
| 6 | No ungrounded claims | 0 |
| 7 | Consistency (numbers) | 0 mismatches |
| 8 | Banned words | 0 |
| 9 | Beipackzettel complete | All fields |
| 10 | Source log present | ≥ 1 source |
| 11 | Claim ledger present | ≥ 1 claim |
| 12 | Confidence stated | Per section |
| 13 | Word targets met | Per section |

### Phase E: Grade + Output

Grade formula based on Phase D results:

```
A+++ = ALL 13 checks pass + >5000 words + E>50% + J<20%
A++  = 12/13 pass + >4000 words
A+   = 11/13 pass + >3000 words
B    = 9/13 pass
C    = <9/13 pass
```

---

## RAG Architecture (rag_layer.py)

### Why TF-IDF/BM25 Instead of Vector Embeddings?

1. **Zero dependencies.** Stdlib only. No numpy, no sentence-transformers, no API calls.
2. **Deterministic.** Same query → same results. No embedding model variation.
3. **Fast.** <50ms for 1000 chunks. No GPU needed.
4. **Good enough.** For 1000 chunks, keyword matching captures 80%+ of relevant results. Vector search advantage only emerges at 100K+ chunks.

### Tier Boosting

```python
TIER_BOOST = {
    "CORE": 2.0,       # Verified claims, corrections
    "KNOWLEDGE": 1.5,   # Peer-reviewed papers
    "OPERATIONAL": 1.0,  # Current state
    "EPHEMERAL": 0.5,   # Daily notes, sessions
}
```

BM25 relevance score is multiplied by tier boost. Effect: a CORE chunk with relevance 10 scores 20, while an EPHEMERAL chunk with relevance 10 scores 5. Verified knowledge consistently outranks daily notes.

### Chunk Sources

| Source | Tier | Chunk Size | Count (typical) |
|---|---|---|---|
| CRTs (JSON) | CORE | 1 per truth | ~27 |
| Corrections (JSON) | CORE | 1 per correction | ~7 |
| Platform Findings (MD) | CORE | 1 per finding | ~8 |
| Reference Library (JSON) | KNOWLEDGE | 1 per paper | ~14 |
| Vault Knowledge Files (MD) | KNOWLEDGE | ~500 chars | ~388 |
| Vault Embeddings (JSON) | EPHEMERAL | Pre-chunked | ~500 |
| **Total** | | | **~944** |

---

## Opus API Strategy

### OAuth vs. API Key

| | OAuth (free) | API Key ($) |
|---|---|---|
| Cost | $0 | ~$0.50-0.80 per report |
| Latency | 3-15 min/call | 15-45 sec/call |
| Output limit | ~4.5K tokens | 8K+ tokens |
| Rate limit | ~62% utilization | Higher limits |
| Total runtime | 60-90 min | 3-6 min |

### Why Curl Instead of Python httpx?

macOS kills long-running Python processes during OAuth waits. `curl` as subprocess survives these timeouts reliably. Trade-off: less elegant, more robust.

---

## File Relationships

```
research-brief.json ─────────────────────────────┐
                                                   │
research-base/                                     │
├── compounding-research-truths.json ──┐           │
├── corrections.json ──────────────────┤           │
├── reference-library.json ────────────┤           │
├── platform-findings-curated.md ──────┤           │
                                       ↓           ↓
                                  rag_layer.py → mia_synthesis_v3.py
                                                   │
                                                   ↓
                                  synthesis-v3/
                                  ├── final-report.md
                                  ├── beipackzettel.json
                                  ├── trust-score.json
                                  └── validation-report.json
                                                   │
                                                   ↓ (manual feedback loop)
                                  research-base/ grows
                                  (new CRTs, corrections)
```

---

## Evolution: v3 → v4 (Planned)

| Feature | v3 (current) | v4 (planned) |
|---|---|---|
| Research | Opus does everything | Isolated Sonnet researchers + web_search |
| Thesis | No dedicated phase | Phase 2.5: Thesis Agent (original insight) |
| Output | Markdown only | AR-001 HTML template + PDF |
| Sources | RAG only | RAG + live web search via Brave API |
| Predictions | None | 3-5 testable, dated predictions |
| Knowledge Provenance | Internal only | Visible per section in report |
| Beipackzettel | Markdown section | Dedicated HTML box with KPI grid |
| Human Checkpoints | None | 2 (after claims, after titles) |

---

*Ainary Ventures — February 2026*

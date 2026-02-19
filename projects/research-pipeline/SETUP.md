# MIA Research Pipeline — Complete Setup Guide

> **Goal:** A new OpenClaw account with zero context can produce a research report identical in quality to MIA-001 and MIA-002.
>
> **Time to first report:** ~30 minutes setup + 60-90 minutes pipeline runtime.
>
> **Cost:** $0 (uses OpenClaw OAuth). Or ~$3-5 per report with Anthropic API credits.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Directory Structure](#2-directory-structure)
3. [Installation](#3-installation)
4. [Knowledge Base Setup](#4-knowledge-base-setup)
5. [Creating a Research Brief](#5-creating-a-research-brief)
6. [Running the Pipeline](#6-running-the-pipeline)
7. [Understanding the Output](#7-understanding-the-output)
8. [Architecture Overview](#8-architecture-overview)
9. [Customization](#9-customization)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Prerequisites

| Requirement | Why | Check |
|---|---|---|
| **OpenClaw** (running) | OAuth token for Anthropic API | `openclaw status` |
| **Python 3.10+** | Pipeline scripts | `python3 --version` |
| **curl** | API calls to Anthropic | `which curl` |
| **Git** | Version control | `git --version` |
| **Obsidian vault** (optional) | Knowledge source for RAG | Any local vault works |

### Authentication

The pipeline uses OpenClaw's OAuth token (free, no API key needed). The token is read from:

```
~/.openclaw/agents/main/agent/auth-profiles.json
```

If you have Anthropic API credits, you can modify `call_opus()` in `mia_synthesis_v3.py` to use `x-api-key` instead of `Bearer` token. This is faster (~30s vs 5-15min per call).

---

## 2. Directory Structure

```
~/.openclaw/workspace/
├── projects/research-pipeline/      # Pipeline code (this directory)
│   ├── mia_synthesis_v3.py          # Main engine (1,879 LOC)
│   ├── rag_layer.py                 # RAG retrieval (328 LOC)
│   ├── pipeline.py                  # Legacy AR-001 generator
│   ├── quality_gate.py              # Quality gate checks
│   ├── claim_tracker.py             # Claim management
│   ├── context_package.py           # Agent context packaging
│   └── query_papers.py              # Academic paper search
│
├── research-base/                   # Knowledge base (RAG sources)
│   ├── compounding-research-truths.json   # CORE tier: verified claims
│   ├── corrections.json                    # CORE tier: self-corrections
│   ├── reference-library.json              # KNOWLEDGE tier: 14 papers
│   └── platform-findings-curated.md        # CORE tier: curated findings
│
├── research/mia-pipeline/           # Report outputs (one dir per run)
│   └── <topic>-<timestamp>/
│       ├── research-brief.json      # Input: what to research
│       ├── all-claims.json          # Input: pre-loaded claims (can be empty)
│       ├── contradictions.json      # Input: known contradictions (can be empty)
│       └── synthesis-v3/            # Output directory
│           ├── final-report-v1.md   # The report
│           ├── beipackzettel.json   # Machine-readable trust label
│           ├── trust-score.json     # Cumulative agent trust
│           └── validation-report.json
│
├── standards/MASTER.md              # Canonical research standards
└── vault-index/embeddings.json      # Obsidian vault embeddings (optional)
```

---

## 3. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/fziescheus-alt/ainary-platform.git ~/.openclaw/workspace
cd ~/.openclaw/workspace
```

### Step 2: Install AgentTrust (optional but recommended)

```bash
cd ~/path/to/agenttrust   # or clone from github.com/florianziesche/agenttrust
pip install -e .
```

Without AgentTrust, the pipeline falls back to inline confidence estimation. Reports still generate but without Beipackzettel integration.

### Step 3: Verify

```bash
cd ~/.openclaw/workspace/projects/research-pipeline
python3 rag_layer.py
```

Expected output:
```
Ingested 944 chunks (944 total docs)
Index built: 5727 terms, avg doc len 35.8
```

If you have no vault or knowledge base files, you'll see fewer chunks. That's fine — the pipeline works with 0 RAG chunks (just lower quality).

---

## 4. Knowledge Base Setup

### Minimum (works with empty knowledge base)

Create empty files:

```bash
mkdir -p ~/.openclaw/workspace/research-base

echo '{"truths": []}' > ~/.openclaw/workspace/research-base/compounding-research-truths.json
echo '{"corrections": []}' > ~/.openclaw/workspace/research-base/corrections.json
echo '[]' > ~/.openclaw/workspace/research-base/reference-library.json
```

### Recommended (better reports)

#### Compounding Research Truths (CRTs)

These are verified claims that accumulate across reports. Format:

```json
{
  "truths": [
    {
      "id": "CT-001",
      "claim": "RLHF damage to calibration is regime-dependent, not absolute",
      "source": "AR-020-v3, verified via Guo et al. ICML 2017 + Tian et al. ICML 2025",
      "confidence": 0.91,
      "category": "calibration",
      "tags": ["rlhf", "calibration", "llm"]
    }
  ]
}
```

#### Reference Library

Verified academic papers. Format:

```json
[
  {
    "id": "S1",
    "title": "On Calibration of Modern Neural Networks",
    "authors": "Guo et al.",
    "venue": "ICML 2017",
    "doi": "10.48550/arXiv.1706.04599",
    "tier": "A1",
    "key_finding": "Temperature scaling reduces ECE by 50-80%. Requires logit access.",
    "caveats": "Pre-LLM era. Direct applicability to black-box APIs limited."
  }
]
```

#### Obsidian Vault Integration (optional)

If you have an Obsidian vault with research notes:

1. Build embeddings: `python3 vault-index/build-embeddings.py`
2. The RAG layer auto-loads `vault-index/embeddings.json` as EPHEMERAL tier

For specific high-value vault files as KNOWLEDGE tier, edit `rag_layer.py` → `ingest_vault_knowledge()` with your file paths.

---

## 5. Creating a Research Brief

Every report starts with a `research-brief.json`. Create a new run directory:

```bash
# Create output directory
TOPIC="your-topic-slug"
TIMESTAMP=$(date +%Y%m%d-%H%M)
OUTDIR=~/.openclaw/workspace/research/mia-pipeline/${TOPIC}-${TIMESTAMP}
mkdir -p "$OUTDIR"
```

Write the research brief:

```bash
cat > "$OUTDIR/research-brief.json" << 'EOF'
{
  "topic": "Your Report Title Here",
  "decision": "What decision should the reader make after reading this?",
  "audience": "Who is reading this? (e.g., CTOs, VCs, engineers)",
  "audience_tag": "PUBLIC",
  "risk_tier": 2,
  "freshness_requirement": "2024-2026",
  "narrative_arc": "A → B transformation story. What changes?",
  "original_thesis_target": "What is your original insight that experts would debate?",
  "sub_questions": [
    "Research sub-question 1?",
    "Research sub-question 2?",
    "Research sub-question 3?",
    "Research sub-question 4?",
    "Research sub-question 5?"
  ],
  "report_id": "MIA-XXX",
  "version": "v1"
}
EOF
```

Create empty input files (pipeline needs these):

```bash
echo '{"claims": []}' > "$OUTDIR/all-claims.json"
echo '{"contradictions": []}' > "$OUTDIR/contradictions.json"
```

### Research Brief Fields

| Field | Required | Description |
|---|---|---|
| `topic` | Yes | Report title |
| `decision` | Yes | What the reader should decide |
| `audience` | Yes | Target reader |
| `audience_tag` | Yes | `PUBLIC`, `LP/VC`, `KUNDE`, `INTERN` |
| `risk_tier` | No | 1 (speed) / 2 (rigor) / 3 (full framework). Default: 2 |
| `freshness_requirement` | No | Date range for sources |
| `narrative_arc` | No | Story structure hint |
| `original_thesis_target` | No | Your original insight. Improves Executive Summary dramatically. |
| `sub_questions` | No | 3-7 research questions. If empty, Opus generates them. |
| `report_id` | No | Tracking ID (e.g., MIA-002) |
| `version` | No | Version string |

---

## 6. Running the Pipeline

### Basic Run

```bash
cd ~/.openclaw/workspace/projects/research-pipeline
python3 mia_synthesis_v3.py "$OUTDIR" --version v1
```

### What Happens (5 Phases)

```
Phase A: OUTLINE (1 Opus call, ~5-15 min)
  → Generates JSON outline: 7 sections with titles, word targets, assigned topics

Phase B: SECTIONS (7 Opus calls, sequential, ~35-90 min)
  → Writes each section independently
  → Python validates each section (word count, banned words, E/I/J/A ratio)
  → Retries once if validation fails

Phase C: MERGE (Python, 0 LLM calls, <1 sec)
  → Assembles sections into single markdown document
  → Generates Beipackzettel

Phase D: VALIDATE (Python, 0 LLM calls, <1 sec)
  → 13 deterministic checks (E/I/J/A ratio, grounding, consistency, etc.)

Phase E: GRADE + OUTPUT (<1 sec)
  → Computes grade (A+++/A++/A+/B/C)
  → Writes final-report.md, beipackzettel.json, validation-report.json
```

### Dry Run (no API calls)

```bash
python3 mia_synthesis_v3.py "$OUTDIR" --version v1 --dry-run
```

Prints all prompts without calling Opus. Useful for debugging.

### Expected Output

```
============================================================
Mia Synthesis Engine v3
Pipeline dir: /path/to/output
Version: v1
RAG layer: available
============================================================

[LOAD] Pipeline data...
[LOAD] Workspace data...

[PHASE A] Generating outline...
  [OPUS] Sending 12543 chars, max_tokens=4096...
  [OPUS] Got 2841 chars in 347s
  Outline: 7 sections

[PHASE B] Writing sections...
  [B.1] beipackzettel (min 300 words)...
  [OPUS] Sending 8234 chars, max_tokens=4096...
  [OPUS] Got 1876 chars in 289s
  ...

[PHASE C] Merging...
  Total: 7,339 words

[PHASE D] Validating...
  E/I/J/A: E=55% I=27% J=1% A=17% ✅
  ...

[PHASE E] Output...
  Grade: A+++

============================================================
SYNTHESIS COMPLETE — Grade: A+++ — 1847.3s total
Output: /path/to/output/synthesis-v3
============================================================
```

### Runtime

| Auth Method | Per Call | Total (8 calls) |
|---|---|---|
| OAuth (free) | 3-15 min | 60-90 min |
| API Key ($) | 15-45 sec | 3-6 min |

---

## 7. Understanding the Output

### final-report-v1.md

Markdown report with 7 sections:

1. **Beipackzettel** — Information Safety Label (confidence, risks, blind spots)
2. **Executive Summary** — Thesis + evidence bullets
3. **Analytical Framework** — Methodology and approach
4. **Key Findings** — 2-4 main analysis sections with E/I/J/A badges
5. **Strategic Recommendations** — Action items with confidence
6. **Risk Assessment** — Risk matrix + mitigations
7. **Technical Appendix** — Methods, source log, claim register

### E/I/J/A Badges

Every paragraph is labeled:

- `[E]` **Evidenced** — Supported by external source with citation
- `[I]` **Interpreted** — Author's reading of evidence
- `[J]` **Judged** — Opinion or prediction (minimize)
- `[A]` **Assumption** — Stated but unverified premise

**Quality thresholds:** E > 50%, J < 20%. Reports failing these are graded B or lower.

### beipackzettel.json

```json
{
  "report_id": "MIA-002",
  "confidence_pct": 72,
  "risk_level": "MEDIUM",
  "source_count": 12,
  "source_tiers": {"A1": 5, "A2": 3, "B1": 2, "B2": 2},
  "blind_spots": ["No practitioner interviews", "Limited to English sources"],
  "not_checked": ["Proprietary implementations", "Non-public benchmarks"],
  "weakest_claim": "Market size estimate based on author projection",
  "generated_at": "2026-02-19T18:52:00Z"
}
```

### Grading

| Grade | Criteria |
|---|---|
| **A+++** | E>50%, J<20%, >5000 words, all 7 sections, 0 orphan sources, 0 consistency errors |
| **A++** | E>50%, J<20%, >4000 words, all sections present |
| **A+** | E>45%, J<25%, >3000 words |
| **B** | Passes basic checks but fails quality thresholds |
| **C** | Missing sections or major validation failures |

---

## 8. Architecture Overview

### The 3 Laws

1. **Opus receives only.** It invents no facts. It connects what it gets from RAG + research brief.
2. **Sonnet speaks only to Python.** Never to Opus directly. Never to other Sonnet. (In v3, Sonnet is not yet used — Opus does both research + synthesis. v4 will add isolated Sonnet researchers.)
3. **Python everywhere deterministic.** Validation, grading, Beipackzettel, merge — all Python. No LLM for truth-checkable operations.

### RAG Layer (rag_layer.py)

TF-IDF + BM25 hybrid search. Stdlib only (no numpy, no external deps).

**4 Knowledge Tiers with boost multipliers:**

| Tier | Boost | Contents | Purpose |
|---|---|---|---|
| CORE | 2.0x | CRTs, corrections, curated findings | Verified, empirical, self-correcting |
| KNOWLEDGE | 1.5x | Reference library, vault papers | Peer-reviewed, curated |
| OPERATIONAL | 1.0x | Projects, people, decisions | Current state |
| EPHEMERAL | 0.5x | Daily notes, session logs | Context, decays fast |

**How it works:**
1. Each section in the outline gets a topic
2. RAG queries that topic → returns top-k chunks with tier-boosted scores
3. CORE results (2x) consistently outrank EPHEMERAL (0.5x) for the same relevance
4. Opus receives only the relevant chunks per section, not the full knowledge base

### Data Flow

```
Knowledge Base (research-base/)
       ↓ RAG query per section
Pipeline (mia_synthesis_v3.py)
  Phase A: Outline (1 Opus call)
  Phase B: Sections (7 Opus calls + Python validation each)
  Phase C: Merge (Python)
  Phase D: Validate (Python, 13 checks)
  Phase E: Grade + Output
       ↓
Report (synthesis-v3/)
  final-report.md + beipackzettel.json + validation-report.json
       ↓ feedback loop (manual)
Knowledge Base grows (new CRTs, corrections)
```

### AgentTrust Integration

If `agenttrust` is installed (`pip install -e .`):
- **Beipackzettel**: Structured confidence/risk label per report
- **TrustScore**: Cumulative agent trust (persisted in `trust-score.json`)
- **3-Signal Confidence**: source_agreement × evidence_strength × internal_consistency

Without it: inline fallback functions produce similar output.

---

## 9. Customization

### Adding Your Own Knowledge

**Add a CRT (Compounding Research Truth):**

```bash
# Edit compounding-research-truths.json
# Add to "truths" array:
{
  "id": "CT-XXX",
  "claim": "Your verified claim here",
  "source": "Paper/report that confirms this",
  "confidence": 0.85,
  "category": "your-domain",
  "tags": ["tag1", "tag2"]
}
```

**Add a reference paper:**

```bash
# Edit reference-library.json
# Add to array:
{
  "id": "S-XX",
  "title": "Paper Title",
  "authors": "Author et al.",
  "venue": "Conference Year",
  "doi": "10.xxxx/xxxxx",
  "tier": "A1",
  "key_finding": "One sentence.",
  "caveats": "Limitations."
}
```

**Add vault files to KNOWLEDGE tier:**

Edit `rag_layer.py` → `ingest_vault_knowledge()`:

```python
VAULT_KNOWLEDGE_FILES = [
    "path/to/your/file1.md",
    "path/to/your/file2.md",
]
```

### Changing the Model

Edit `call_opus()` in `mia_synthesis_v3.py`:

```python
# Change model
"model": "claude-sonnet-4-20250514",  # faster, cheaper, lower quality

# Or use API key instead of OAuth
"-H", f"x-api-key: {YOUR_API_KEY}",
# Remove: "-H", "anthropic-beta: oauth-2025-04-20",
```

### Changing Report Structure

Edit `SECTION_ORDER` and `MIN_WORDS` at the top of `mia_synthesis_v3.py`:

```python
SECTION_ORDER = [
    "beipackzettel",
    "executive_summary",
    "framework",
    "key_findings",
    "recommendations",
    "risks",
    "appendix",
]
```

### Changing Quality Thresholds

Edit the validation constants in `mia_synthesis_v3.py`:

```python
# E/I/J/A thresholds (non-negotiable for A+++ grade)
MIN_E_RATIO = 0.50   # At least 50% Evidenced
MAX_J_RATIO = 0.20   # At most 20% Judged
```

---

## 10. Troubleshooting

### "No sk-ant-oat token found"

OpenClaw isn't running or hasn't authenticated with Anthropic.

```bash
openclaw status          # Check if running
openclaw gateway start   # Start if needed
```

The OAuth token refreshes automatically. If expired, restart OpenClaw.

### Opus call times out (>15 min)

Normal with OAuth. The pipeline retries once automatically. If persistent:
- Check `openclaw status` for rate limits
- Wait 5 minutes between runs
- Consider buying $20 Anthropic API credits for 10x faster calls

### "RAG layer: fallback (direct load)"

RAG couldn't load. Check:
- `research-base/` directory exists
- JSON files are valid: `python3 -c "import json; json.load(open('research-base/compounding-research-truths.json'))"`

### Report grades B or C

Common causes:
- E/I/J/A ratio off (too many [J] judgments, not enough [E] evidence)
- Missing sections (Opus hit token limit)
- Word count too low

Fix: Re-run. Opus output varies. Or add more CRTs/references for the topic.

### "curl failed" or API error

```bash
# Test manually
curl -s https://api.anthropic.com/v1/messages \
  -H "Authorization: Bearer $(python3 -c "
import json; d=json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
def f(o):
  if isinstance(o,dict):
    for k,v in o.items():
      if k in ('token','accessToken') and str(v).startswith('sk-ant-oat'): print(v); exit()
      f(v)
  elif isinstance(o,list):
    for i in o: f(i)
f(d)
")" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: oauth-2025-04-20" \
  -H "content-type: application/json" \
  -d '{"model":"claude-opus-4-20250514","max_tokens":100,"messages":[{"role":"user","content":"Say hi"}]}'
```

---

## Quick Start (Copy-Paste)

```bash
# 1. Set up
cd ~/.openclaw/workspace/projects/research-pipeline

# 2. Create run directory
TOPIC="my-first-report"
OUTDIR=~/.openclaw/workspace/research/mia-pipeline/${TOPIC}-$(date +%Y%m%d-%H%M)
mkdir -p "$OUTDIR"

# 3. Write research brief
cat > "$OUTDIR/research-brief.json" << 'EOF'
{
  "topic": "Why AI Agents Need Trust Infrastructure",
  "decision": "Should engineering teams invest in calibration tooling before deploying agents?",
  "audience": "CTOs and engineering leads at AI-first companies",
  "audience_tag": "PUBLIC",
  "sub_questions": [
    "What is the current state of AI agent deployment in production?",
    "What trust failures have occurred and what was the cost?",
    "What calibration methods exist for black-box LLM APIs?",
    "How does the EU AI Act affect trust requirements?",
    "What is the build-vs-buy calculus for calibration infrastructure?"
  ],
  "report_id": "TEST-001",
  "version": "v1"
}
EOF

echo '{"claims": []}' > "$OUTDIR/all-claims.json"
echo '{"contradictions": []}' > "$OUTDIR/contradictions.json"

# 4. Run
python3 mia_synthesis_v3.py "$OUTDIR" --version v1

# 5. Read output
cat "$OUTDIR/synthesis-v3/final-report-v1.md"
cat "$OUTDIR/synthesis-v3/beipackzettel.json"
```

---

## File Reference

| File | LOC | Purpose |
|---|---|---|
| `mia_synthesis_v3.py` | 1,879 | Main synthesis engine (5 phases) |
| `rag_layer.py` | 328 | TF-IDF/BM25 RAG with tiered boosting |
| `pipeline.py` | 394 | Legacy: AR-001 HTML generator (Haiku→Sonnet→Opus) |
| `quality_gate.py` | ~200 | Standalone quality gate checks |
| `claim_tracker.py` | ~150 | Claim management + ledger |
| `context_package.py` | ~100 | Agent context packaging |
| `query_papers.py` | ~100 | Semantic Scholar / arXiv search |
| `research_factory.py` | ~2,500 | Advanced: 3-stage factory with experiments |
| `measure.py` | ~200 | Report quality measurement (L1 rubric) |
| `experiment_runner.py` | ~300 | A/B testing framework for pipeline variants |

---

*Ainary Ventures — AI Strategy · System Design · Execution · Consultancy · Research*
*Last updated: 2026-02-19*

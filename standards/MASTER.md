# MIA RESEARCH PIPELINE — MASTER SPECIFICATION
# Version: 1.0 | Date: 2026-02-19 | Status: Canonical
# This is the SINGLE SOURCE OF TRUTH. If any other file contradicts this, THIS WINS.

---

# §1 LAWS

1. Opus receives only. Invents no facts. Connects what it gets.
2. Sonnet speaks only to Python. Never to Opus. Never to other Sonnets.
3. Python everywhere countable, verifiable, deterministic.

---

# §2 ARCHITECTURE

```
FLORIAN ──CP1(30s)──────────────────────CP2(2min)──→ SHIP/REVISE/REJECT
              │                              │
         ┌────┴────┐                    ┌────┴────┐
         │  OPUS   │                    │  OPUS   │
         │  BRAIN  │                    │  ASSETS │
         │  1M ctx │                    │         │
         └────┬────┘                    └─────────┘
              │ files only
         ┌────┴────┐
         │ PYTHON  │ ← orchestrates, validates, counts, stores
         │ GATEWAY │ ← ONLY communication channel
         └─┬─┬─┬─┬─┘
           │ │ │ │
          S1 S2 S3 S4 S5  ← isolated Sonnet workers
```

## Resource Budget

| Phase | Model | Calls | Time |
|-------|-------|-------|------|
| 1 Frame + Blindspots | Opus | 1 | 10min |
| CP1 | Florian | — | 30s |
| 2a Research | Sonnet×5 | 5 | 10min |
| 2a Web | Brave API | 10+ | 30s |
| 2b Extract | Sonnet×5 | 5 | 5min |
| 2b Contradict | Sonnet×1 | 1 | 2min |
| 2b Review | Sonnet×5 | 5 | 5min |
| 2b Validate | Python | — | 5s |
| 3 Synthesize | Opus | 1 | 10min |
| 3.5 Validate + Replace | Python | — | 5s |
| 3.6 QA Review | Sonnet×1 | 1 | 5min |
| 4 Assets | Opus | 1 | 10min |
| 5 Quality Gate | Python | — | 5s |
| CP2 | Florian | — | 2min |
| **TOTAL** | | **20** | **~60min** |

---

# §3 THRESHOLDS (unified, non-negotiable)

```
E/I/J/A:     E > 50%    J < 20%
Sources:     >= 5 unique [S#]
Claims:      >= 10 in Claim Ledger
Rubric:      /16 (8 dimensions × 0-2)

Grade  Rubric  E%    J%    Logs   Decision
A+++   >=15    >50   <20   PASS   SHIP
A+     >=13    >50   any   any    SHIP
B      >=10    any   any   any    REVISE
C      <10     any   any   any    REJECT
```

---

# §4 CONFIDENCE FORMULA (AgentTrust)

Three methods, strongest first:

## 4a Budget-CoCoA (strongest, 3 LLM calls per claim)
```
pct = 30 + agreement_ratio × 55    cap [30, 95]
3/3 agree → HIGH (>85%)
2/3 agree → MEDIUM (60-85%)
1/3 agree → LOW (<60%)
```

## 4b Source Signal (standard, 0 LLM calls — Python-computed)
```
claim_conf = 0.5 × SOURCE + 0.3 × CONSISTENCY + 0.2 × STRUCTURAL

SOURCE = admiralty × verification × recency
  admiralty:    A1=0.95  A2=0.85  B2=0.70  C3=0.40  D4=0.20  E2=0.10
  verification: verified=1.0  partial=0.5  unverifiable=0.1
  recency:      max(0.5, 1.0 - (current_year - evidence_year) × 0.1)

CONSISTENCY = verification proxy
  verified=0.85  partial=0.60  unverifiable=0.30

STRUCTURAL = text markers (cap 0.50)
  DOI +0.30 | URL +0.15 | percentage +0.10 | year +0.05 | [S#] +0.10

report_confidence = weighted_avg(claim_confs)
  weights: load-bearing=1.0  supporting=0.6  contextual=0.3
```

## 4c Verbalized (weakest, fallback)
```
calibrated = stated × 0.7
```

---

# §5 BEIPACKZETTEL (mandatory on every output)

## Required Fields
| Field | Type | Computed By | Rule |
|-------|------|-------------|------|
| confidence | float 0-100 | Python (§4b) | NEVER LLM-guessed. Opus writes `{{CONFIDENCE}}`, Python replaces |
| risk_level | HIGH/MEDIUM/LOW | Python | conf<50 or risks>=3 → HIGH. conf>=80 and risks==0 → LOW. Else MEDIUM |
| grounded | bool | Python | len(sources) > 0 |
| sources | list[str] | Opus | Non-empty. Format: "[S#] Title (Venue, Year)" |
| uncertainties | list[str] | Opus | Non-empty. Must be specific, not "things might change" |
| risks | list[str] | Opus | Non-empty. What goes wrong if someone acts on this |
| not_checked | list[str] | Opus | What was assumed but not verified |
| eija | {E:int, I:int, J:int, A:int} | Python | `{{EIJA}}` placeholder, Python replaces |

## Placeholders (Opus writes, Python replaces)
- `{{CONFIDENCE}}` → computed %
- `{{EIJA}}` → counted distribution
- `{{RISK_LEVEL}}` → computed level

---

# §6 TRUST SCORE (per agent, cumulative)

```
good + high conf (>=70)     → +1
good + low conf (<70)       → +1
bad + high conf (>=80)      → -3  (overconfident)
bad + low conf (<80)        → -1  (wrong but honest)
flagged_real                → +2  (honest uncertainty)
hidden_problem              → -3  (QA found what agent hid)

Level       Score   QA Rate
UNTRUSTED   0-30    100%
SUPERVISED  31-60   50%
SPOT_CHECK  61-80   20%
AUTONOMOUS  81+     0%
```

---

# §7 E/I/J/A LABELS

```
[E] Evidenced   — directly from source with citation. Requires [S#].
[I] Interpreted  — inferred from sources, logic explained.
[J] Judged       — assessment, no direct source. Must say "Author judgment."
[A] Actionable   — recommendation. Must reference supporting [E]/[I]/[J].
```

Use in: Claim Ledger (appendix). Prose flows narratively without inline labels.

---

# §8 PHASES

## Phase 1: FRAME (Opus, 1 call)

Input: topic, CRTs, corrections, decisions
Output: research-brief.json + blindspots.json

```
TASK:
1. State THE REAL QUESTION (1 sentence — the question behind the question)
2. WHY NOW (what changed in last 90 days)
3. Decompose into 5 SUB-QUESTIONS (MECE, independently researchable)
4. Per SQ: question, why_it_matters, evidence_needed, search_queries[2-3]
5. 3 BLINDSPOTS: questions nobody is asking
   Per blindspot: question, why_its_a_blindspot, confidence(0-100),
   reasoning, recommendation(YES/MAYBE/NO)

OUTPUT: JSON only.
{
  "real_question": "...",
  "why_now": "...",
  "sub_questions": [{"id":"SQ-1", "question":"...", "why_it_matters":"...",
                     "evidence_needed":"...", "search_queries":["...",".."]}],
  "blindspots": [{"question":"...", "why_its_a_blindspot":"...",
                  "confidence":75, "reasoning":"...", "recommendation":"YES"}]
}
```

## 🔴 CHECKPOINT 1 (Florian, 30s)
Sees: 5 SQs + 3 Blindspots. Options: GO / EDIT / ADD BLINDSPOT / REFRAME.

## Phase 2a: RESEARCH (Python + Sonnet×5, parallel)

Python: Brave Search (2-3 queries per SQ) → fetch top-3 URLs → save as files.
Per Sonnet (isolated, sees ONLY its 1 SQ + Brave results + Reference Library):

```
TASK:
Answer ONE question with evidence. Max 800 words.
- ONLY use evidence from web results and references provided
- Cite EVERY claim with [S#] or source URL
- No evidence → say "No evidence found" — do NOT invent
- Label: [E] from source with citation, [I] inferred, [J] assessment
- End with "SO WHAT: ..." (1-2 sentences)
- Claims table: # | Claim | [S#] | E/I/J | Admiralty | Confidence
```

## Phase 2b: EXTRACT + VERIFY (Sonnet×11 + Python)

All Sonnet jobs = extraction on given text. Zero hallucination risk.

**2b-1 Claim Extract (Sonnet×5):** Extract 3 most important factual claims per sub-report. Verbatim quote, E/I/J label, [S#], Admiralty rating. JSON array.

**2b-2 Contradiction Find (Sonnet×1):** Compare all 5 sub-reports. Find contradictions. Per contradiction: claim_a, claim_b, why_they_differ, which_is_stronger, impact. JSON array.

**2b-3 Review (Sonnet×5):** Score per sub-report: evidence(0-2), uncertainty(0-2), actionability(0-2). Flag uncited load-bearing claims. Flag contradictions. JSON.

**Python Post-Processing:**
- Count E/I/J per sub-report
- Count sources per sub-report
- Label GOOD (E >= J and sources >= 2) / WEAK
- Save all-claims.json, contradictions.json, sub-reviews.json, sub-validations.json

## Phase 3: SYNTHESIZE (Opus, 1 call)

Input: ALL files Python collected. Full context.

```
RULES:
1. NO NEW FACTS. Only combine what's in sub-reports + CRTs + papers.
2. WEAK sub-reports: use findings ONLY if corroborated by another SQ or CRT.
3. Write placeholders: {{CONFIDENCE}}, {{EIJA}}, {{RISK_LEVEL}}.
4. Engaging opener (surprise an expert). Case studies inline. Section confidence.
5. "SO WHAT" per section → "For the decision maker: ..."
6. Custom Framework: original model, named, drawable, maps findings.
7. Recommendations: phased (W1/M1/Q1). Each [A] references [E/I/J]. Each has "If wrong:".
8. "Do Not Deploy If" — exactly 5 specific conditions.
9. Include Documented Blindspots appendix.

STRUCTURE (12 blocks, all required):
1. Beipackzettel (placeholders)
2. Opener (3 sentences: surprise, why now, delivers)
3. Executive Summary (Situation→Complication→Resolution + "If you read nothing else" bullets)
4. Custom Framework (name, visual, mapping, so what)
5. Key Findings (5-7, each: finding + evidence + confidence% + "For the decision maker")
6. Case Studies (2-3, real, sourced, verifiable — NO hypotheticals)
7. Recommendations (decision matrix + W1/M1/Q1 + "Do Not Deploy If" ×5 + "If wrong")
8. Risks (3-5, each: trigger + probability + impact + what to monitor)
9. Claim Ledger (>=10 claims: CL-#, text, E/I/J/A, [S#], Admiralty, confidence)
10. Source Log (every [S#]: title, venue, DOI/URL, key finding, caveats)
11. Contradiction Register (>=1 entry)
12. Self-Calibration + Documented Blindspots

BANNED WORDS: landscape, tapestry, delve, synergy, cutting-edge, game-changer,
"It's worth noting", "In today's world"
```

## Phase 3.5: VALIDATE (Python, deterministic)

```python
# E/I/J/A count + distribution check (E>50%, J<20%)
# Source count (>=5 unique [S#])
# Source Log completeness (every [S#] in body has log entry)
# Claim Ledger count (>=10)
# Contradiction Register present
# Beipackzettel fields present (Sources, Uncertainties, Risks, Not Checked)
# New Fact Detection (claims in report not in all-claims.json)
# Replace placeholders: {{CONFIDENCE}}, {{EIJA}}, {{RISK_LEVEL}}
# Rewrite final-report.md with computed values
```

## Phase 3.6: QA REVIEW (Sonnet×1 — NOT Opus)

Sonnet reviews report it did NOT write. Uses 8-dimension rubric:

```
1. Factual Accuracy (0-2)         5. Epistemic Honesty (0-2)
2. Completeness (0-2)             6. Actionability (0-2)
3. Source Quality (0-2)           7. Confidence Calibration (0-2)
4. Clarity & Structure (0-2)     8. Risk Awareness (0-2)

Critical checks:
- New Facts: any claim not in all-claims.json → flag "OPUS-GENERATED"
- Hypothetical Cases: "imagine a company" → automatic -2
- Beipackzettel: confidence is number? lists non-empty? specific?

Output: rubric scores + new_facts_found + fix_requests + verdict
>=13/16 + 0 new facts → proceed to Phase 4
>=10/16 or 1-2 new facts → FIX then reship
<10/16 or 3+ new facts → back to Phase 3
```

## Phase 4: ASSETS (Opus, 1 call)

Input: final report + vault + CRTs.

```
OUTPUT:
1. Asset Index (coverage map: Finding → Assets)
2. Atomic Notes (10-15): ID(AB-[slug]-[TYPE]-[0001]), title, "This answers:",
   content, classification(Evidenced/Derived/Operational), confidence, sources, tags
3. Playbooks (2-3): trigger, goal, inputs, steps, outputs, failure modes, acceptance
4. Templates (1-2): when to use, copy-paste block, pitfalls
5. RAG JSON: [{id, type, title, this_answers, content, tags, classification,
   confidence, sources, relations}]

RULES: No new facts. Dedupe. Cross-reference vault. Epistemic labels per asset.
```

## Phase 5: QUALITY GATE (Python, deterministic)

```python
grade = "C"
if rubric>=15 and e_pct>50 and j_pct<20 and beipackzettel and framework and log_issues==0:
    grade = "A+++"
elif rubric>=13 and e_pct>50:
    grade = "A+"
elif rubric>=10:
    grade = "B"

decision = "SHIP" if grade in ("A+++","A+") else "REVISE" if grade=="B" else "REJECT"
```

## 🔴 CHECKPOINT 2 (Florian, 2min)
Sees: Grade, Rubric, E/I/J/A, New Facts, Log Issues, Executive Summary.
Options: SHIP / REVISE / REJECT.

---

# §9 PYTHON LOG ENFORCEMENT

Python validates these BEFORE Quality Gate. Failure blocks A+++.

| Check | Rule | Failure |
|-------|------|---------|
| Source Log | Every [S#] in body has entry in Source Log section | List orphans |
| Claim Ledger | >= 10 CL-# entries | Count warning |
| Contradictions | "contradiction" appears in report | Missing warning |
| Beipackzettel | Sources:, Uncertainties:, Risks:, Not Checked: all present | List missing |
| Orphan Sources | [S#] referenced but not logged | List IDs |
| New Facts | Claims in report not in all-claims.json | Flag as OPUS-GENERATED |

---

# §10 OUTPUT FILES

```
research/mia-pipeline/{topic}-{timestamp}/
├── pipeline.json              metadata
├── research-brief.json        Phase 1 (incl. blindspots)
├── blindspots.json            3 blindspots
├── sq-01/ ... sq-05/          per SQ: prompt.md + report.md
├── all-claims.json            15 claims (Phase 2b)
├── contradictions.json        cross-SQ contradictions
├── sub-reviews.json           Sonnet scores (0-6)
├── sub-validations.json       GOOD/WEAK labels
├── final-report.md            A+++ report (placeholders replaced)
├── validation.json            E/I/J/A + log enforcement + new facts
├── qa-review.json             Sonnet QA rubric /16
├── assets.md                  notes + playbooks + RAG
├── quality-gate.json          grade + decision
└── beipackzettel.json         AgentTrust-compatible JSON
```

---

# §11 CANONICAL SOURCES (ChatGPT Originals — read-only reference)

These files are archived originals. This MASTER file supersedes them for execution.
Consult only when you need exact template formatting.

| File | What |
|------|------|
| ERF-SYSTEM-PROMPT-v2.md | Producer prompt (5 phases) |
| ERF-REVIEWER-PROMPT-v1.md | Reviewer rubric + claim audit |
| ERF-TEMPLATES.md | Templates A-J (Intake→Report→Source Log→Claim Ledger→etc) |
| ERF-SOURCE-LOG-TEMPLATE.md | Blank source log |
| ERF-EVAL-PACK.md | 6 regression tests |
| ERF-PROMPT-REGISTRY.md | Prompt version control |
| ERF-README.md | ERF overview |
| ERF-CHANGELOG.md | Audit trail |
| ASSET-BUILDER-SYSTEM-PROMPT.md | Asset builder instructions |
| ASSET-BUILDER-TEMPLATES.md | Note/Playbook/Template formats |
| ASSET-BUILDER-RAG-SCHEMA.md | JSON spec |
| ASSET-BUILDER-EVAL.md | 6-point rubric |
| ASSET-BUILDER-REGISTRY.md | Naming + tags |
| ASSET-BUILDER-README.md | AB overview |
| ASSET-BUILDER-CHANGELOG.md | Audit trail |

---

# §12 SOURCE POLICY

```
Tier 1 (USE):    Peer-reviewed, standards bodies, own experiments. Admiralty A1-A2.
Tier 2 (CAVEAT): arXiv, lab tech reports, pre-prints. Mark: "[preprint]". Admiralty B2.
Tier 3 (BANNED): Blogs, LLM outputs, tweets, own old reports. If no T1/T2: "author estimate."
```

---

# §13 BANNED

Words: landscape, tapestry, delve, synergy, cutting-edge, game-changer, "It's worth noting", "In today's world", "Great question!", "I'd be happy to!", "Absolutely!"

Symbols: no Apple symbols, no Private Use Area Unicode.

---

# §14 IMPLEMENTATION

Code: `projects/research-pipeline/mia_pipeline.py`
Library: `projects/agenttrust/` (pip install agenttrust)
Key imports:
```python
from agenttrust import source_signal_confidence, report_confidence, Beipackzettel, TrustScore
from agenttrust.qa.reviewer import review
from agenttrust.pipeline.pipeline import AgentPipeline
```

---

# END OF MASTER SPECIFICATION

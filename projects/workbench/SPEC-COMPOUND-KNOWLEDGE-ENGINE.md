# Compound Knowledge Engine (CKE) — Technical Specification

**Version:** 1.0 | **Date:** 2026-02-18 | **Author:** Florian Ziesche + Mia
**Classification:** [INTERN] — Proprietary IP
**Status:** SPEC — Pre-Implementation

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Prior Art & Why It Fails](#3-prior-art--why-it-fails)
4. [Core Thesis](#4-core-thesis)
5. [System Architecture](#5-system-architecture)
6. [Data Model](#6-data-model)
7. [Algorithms](#7-algorithms)
8. [The Three Loops](#8-the-three-loops)
9. [Finding Lifecycle](#9-finding-lifecycle)
10. [Cross-Finding Engine](#10-cross-finding-engine)
11. [Content Distribution Layer](#11-content-distribution-layer)
12. [KPI Attribution Chain](#12-kpi-attribution-chain)
13. [Implementation Plan](#13-implementation-plan)
14. [Assumptions & Risks](#14-assumptions--risks)
15. [Success Metrics](#15-success-metrics)
16. [Future Extensions](#16-future-extensions)
17. [Appendix: Evidence Base](#17-appendix-evidence-base)

---

## 1. Executive Summary

The Compound Knowledge Engine (CKE) is a system that turns conversations, research, and feedback into structured knowledge that improves over time. Unlike traditional knowledge management (Notion, Obsidian, wikis) which stores information, CKE tracks the lifecycle of knowledge — from hypothesis to validation to application to revenue — and uses that lifecycle data to make better decisions about what to research, build, and distribute next.

The core IP is not the storage. It's the feedback loops:

```
Every finding has a confidence score that changes over time.
Every finding tracks where it was used (system, content, revenue).
Every piece of content tracks its performance (impressions, engagement, leads).
Performance data flows back to the finding, updating its confidence and compound score.
The system tells you: "Invest more in Trust research, it has 4x ROI vs. SMB adoption."
```

This is not possible at scale. It requires N=1 (one user, one knowledge base, one feedback loop). That's not a limitation — it's the moat.

**Key Claim:** A single operator with a Compound Knowledge Engine outperforms a team of 5 without one within 6 months, measured by content output quality, research-to-revenue conversion rate, and decision accuracy.

**Evidence Level:** Hypothesis (Confidence: 0.55). Based on analogies from compound interest in finance, spaced repetition in learning, and flywheel effects in business. No direct evidence yet. This system is designed to generate its own evidence.

---

## 2. Problem Statement

### 2.1 Knowledge Decay in AI-Assisted Work

**Observation:** Current AI assistants (ChatGPT, Claude, Gemini) lose all context between sessions. "Memory" features are superficial — they store preferences ("Florian likes short answers") not structured knowledge ("€5.0M raised, not €5.5M, confirmed by Florian on 2026-02-18, severity: critical").

**Evidence:**
- OpenAI Memory stores ~100 text snippets with no confidence, no source, no lifecycle [source: OpenAI docs, 2025]
- Anthropic has no persistent memory between sessions as of Feb 2026
- Google Gemini Memory is preference-based, not knowledge-based [source: Google AI blog, 2025]

**Assumption A1:** Unstructured memory leads to repeated mistakes. We observed this directly: the €5.5M error appeared in 15+ documents across multiple sessions despite being corrected multiple times.

**Cost of the Problem:**
- Each repeated error costs ~15 minutes to catch and fix
- At 3 errors/week × 52 weeks × 15 min = 39 hours/year lost to repeated mistakes
- More critically: uncaught errors in sent documents (CVs, emails, pitches) damage credibility irreversibly

### 2.2 Research-to-Revenue Conversion

**Observation:** Most knowledge work follows a pattern: research a topic, learn something, move to the next topic. The findings from the first topic are never systematically applied to systems, content, or revenue generation.

**Evidence:**
- Florian's workspace contains 24 research documents across VC funds, AI topics, and market analyses. Of these, 3 have been converted into actionable outputs (12.5% conversion rate). [source: direct file analysis, 2026-02-18]
- Industry average for "research to published insight" in consulting: 15-20% [source: McKinsey internal estimates, various]
- Knowledge workers spend 19% of time searching for information they've already found [source: McKinsey Global Institute, 2012 — dated but directionally valid]

**Assumption A2:** A structured finding system with compound scoring would increase research-to-output conversion from ~12% to ~40% within 6 months by making existing knowledge visible and actionable.

### 2.3 Content Without Feedback Loops

**Observation:** Content creation without systematic feedback is random walking. You don't know which topics resonate, which format works, which audience segment engages — so every post is a guess.

**Evidence:**
- Florian's LinkedIn: 5,463 followers, 526 impressions/week, but no systematic tracking of which topics drive engagement vs. which don't
- The average LinkedIn creator posts 2-3x/week for 3 months then stops due to lack of visible progress [source: various LinkedIn creator studies, 2024-2025]

**Assumption A3:** Closing the feedback loop (post → metrics → back to finding → inform next post) increases content consistency from ~12 weeks average to indefinite, because progress becomes visible and data-driven.

---

## 3. Prior Art & Why It Fails

### 3.1 Personal Knowledge Management (PKM)

| System | Approach | Failure Mode |
|---|---|---|
| **Obsidian** | Markdown + bi-directional links | Manual linking dies after 2 weeks. No confidence. No lifecycle. 200+ orphan notes. |
| **Notion** | Databases + relations | Beautiful structure, zero maintenance discipline. Becomes a graveyard. |
| **Roam Research** | Block references + daily notes | Everything connects to everything = nothing connects to anything. Signal drowned in noise. |
| **Zettelkasten** | Atomic notes + connections | Requires monk-like discipline. Most practitioners have <100 notes after 1 year. |

**Why they all fail:** They treat knowledge as static. A note created today has the same weight as a note created 2 years ago. No decay. No confidence. No validation. No lifecycle.

**What CKE does differently:** Knowledge has a birth, a life (validation, application, revenue), and a death (contradicted, decayed, superseded). The lifecycle IS the value.

### 3.2 Enterprise Knowledge Graphs

| System | Approach | Failure Mode |
|---|---|---|
| **Neo4j / Knowledge Graphs** | Entities + relationships | Requires explicit ontology design. Too rigid for evolving knowledge. |
| **Palantir** | Data integration + graph | Enterprise-scale, enterprise-price, enterprise-complexity |
| **Notion AI** | Embeddings over workspace | Retrieval without structure. Finds similar, not contradictory. |

**Why they fail for N=1:** They're designed for organizations with dedicated teams to maintain the graph. A solo operator needs automatic maintenance or it dies.

### 3.3 RAG (Retrieval-Augmented Generation)

**Approach:** Embed all documents, retrieve relevant chunks, feed to LLM.

**Failure Modes:**
- No confidence scoring — a hallucinated finding from 6 months ago has the same retrieval weight as a verified fact from today
- No lifecycle — retrieved chunks are treated as equally valid regardless of age, source, or validation status
- No cross-finding — RAG retrieves similar, not contradictory or complementary
- No compound effect — retrieval doesn't improve over time, it just grows

**Evidence:** Our own system uses embeddings for memory_search. It works for retrieval but fails at: "Which of these findings contradict each other?" and "Which research line has produced the most revenue?"

### 3.4 Spaced Repetition Systems (Anki)

**Relevant Insight:** Anki's scheduling algorithm (SM-2 and variants) manages knowledge decay mathematically. Each card has an "ease factor" that changes based on recall performance.

**What CKE borrows:** The idea that knowledge has a decay curve and that confidence changes with each interaction. But CKE tracks APPLICATION (was it used? did it generate revenue?) not RECALL (can you remember it?).

---

## 4. Core Thesis

### 4.1 The Compound Knowledge Hypothesis

**Thesis:** Knowledge that is structured, confidence-scored, lifecycle-tracked, and feedback-looped compounds over time — meaning each new finding makes all existing findings more valuable through cross-connections, validations, and contradictions.

**Mechanism:**

```
Linear Knowledge:    Finding₁ + Finding₂ + Finding₃ = 3 findings
Compound Knowledge:  Finding₁ × Finding₂ × Finding₃ = connections, contradictions, syntheses
```

**Analogy:** Compound interest works because returns generate returns. Compound knowledge works because findings generate findings — a cross-connection between two findings IS a new finding.

**Assumption A4:** The compound effect becomes measurable at 30+ findings and significant at 100+. Below 30, it's just a database. Above 100, it's an unfair advantage.

### 4.2 The N=1 Advantage

**Thesis:** Personalized knowledge systems are impossible at scale and devastating at N=1.

| Feature | At Scale (ChatGPT) | At N=1 (CKE) |
|---|---|---|
| Corrections | Generic patterns | 42 personal rules with regex patterns |
| Trust | Binary (on/off) | 9 skills, Bayesian, earned over time |
| Confidence | Not tracked | Per-finding, with history and sources |
| Cross-findings | Generic associations | Personal research lines with revenue tracking |
| Voice | Generic "helpful assistant" | Learned from corrections + approved samples |
| Feedback | Thumbs up/down → RLHF training | Specific correction → permanent rule → immediate effect |

**Evidence:** Our Pre-Flight Engine catches errors that ChatGPT/Claude repeat endlessly because they have no persistent correction mechanism. [source: direct observation, €5.5M error repeated across 15+ documents]

### 4.3 The Flywheel Model

```
                    RESEARCH
                   /    |    \
                  /     |     \
           findings  validate  cross-find
                |       |         |
                v       v         v
              SYSTEMS ←→ CONTENT
              (build)    (distribute)
                |            |
                v            v
             automate    engagement
                |            |
                v            v
              REVENUE ← ← LEADS
                |
                v
          validates findings
          (highest confidence source)
                |
                v
             RESEARCH (informed by what works)
```

**Key Insight:** Revenue is not the end of the chain. Revenue is a confidence signal that flows BACK to Research. A finding that generated revenue has higher confidence than one that only generated a blog post.

---

## 5. System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPOUND KNOWLEDGE ENGINE                  │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   FINDING     │  │   CROSS      │  │   ATTRIBUTION    │  │
│  │   STORE       │  │   FINDER     │  │   CHAIN          │  │
│  │              │  │              │  │                  │  │
│  │  claim       │  │  Tag Match   │  │  Finding         │  │
│  │  confidence  │←→│  Embedding   │  │    → System      │  │
│  │  tags        │  │  LLM Synth   │  │    → Content     │  │
│  │  lifecycle   │  │              │  │    → KPI         │  │
│  │  used_in     │  │  Contradict  │  │    → Revenue     │  │
│  │  source      │  │  Detection   │  │    → Confidence  │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘  │
│         │                 │                    │             │
│         └────────────┬────┴────────────────────┘             │
│                      │                                       │
│              ┌───────▼────────┐                              │
│              │   COMPOUND     │                              │
│              │   SCORE        │                              │
│              │   ENGINE       │                              │
│              └───────┬────────┘                              │
│                      │                                       │
│    ┌─────────────────┼─────────────────────┐                │
│    │                 │                     │                │
│    ▼                 ▼                     ▼                │
│  ┌──────┐     ┌──────────┐         ┌───────────┐           │
│  │ AUTO │     │ CONTENT  │         │ RESEARCH  │           │
│  │ EXTRACT│   │ RECOMMEND│         │ PRIORITY  │           │
│  │      │     │          │         │           │           │
│  │ Chat │     │ Platform │         │ Which     │           │
│  │ → Ask│     │ + Format │         │ topic     │           │
│  │ → Save│    │ + Angle  │         │ to invest │           │
│  └──────┘     └──────────┘         │ in next?  │           │
│                                     └───────────┘           │
└─────────────────────────────────────────────────────────────┘
```

### 5.1 Integration with Execution Platform

CKE is not a separate system. It's a layer ON TOP of the existing Execution Platform:

```
Execution Platform (existing)
├── Topics (21)          → CKE tags topics with research_origin finding
├── Messages (329)       → CKE auto-extracts findings from conversations
├── Corrections (42)     → CKE treats corrections as validated findings (confidence: 1.0)
├── Pre-Flight Engine    → CKE findings with patterns become pre-flight rules
├── Trust Skills (9)     → CKE uses trust scores as confidence weights for skill-specific findings
├── Events (92)          → CKE logs finding lifecycle events
└── Actions              → CKE recommends actions based on compound score

CKE Layer (new)
├── Findings             → Structured knowledge with lifecycle
├── Cross-Findings       → Connections between findings
├── Syntheses            → LLM-generated insights from finding clusters
├── Content Tracker      → Post performance → finding attribution
└── Compound Score       → Ranking of findings and research lines
```

---

## 6. Data Model

### 6.1 Core Tables

```sql
-- The atomic unit of knowledge
CREATE TABLE findings (
    id TEXT PRIMARY KEY,                    -- "RF-001" format
    claim TEXT NOT NULL,                    -- The actual knowledge claim
    context TEXT,                           -- Why this matters, background
    
    -- Confidence & Lifecycle
    confidence REAL DEFAULT 0.50,           -- 0.0 to 1.0
    status TEXT DEFAULT 'alive',            -- alive, contested, dead
    killed_by TEXT,                         -- Finding ID or explanation
    
    -- Provenance
    source_type TEXT,                       -- conversation, poll, paper, data, observation
    source_detail TEXT,                     -- URL, paper title, conversation date
    source_confidence_weight REAL,          -- How much the source type affects confidence
    extracted_from TEXT,                    -- Session/conversation ID if auto-extracted
    
    -- Classification
    tags TEXT DEFAULT '[]',                 -- JSON array: ["smb", "ai-quality", "trust"]
    research_line TEXT,                     -- Which research topic this belongs to
    
    -- Usage Tracking
    used_in_systems TEXT DEFAULT '[]',      -- JSON: ["pre-flight-engine", "bayesian-trust"]
    used_in_content TEXT DEFAULT '[]',      -- JSON: ["linkedin-post-12", "substack-3"]
    used_in_revenue TEXT DEFAULT '[]',      -- JSON: ["consulting-lead-acme"]
    
    -- Relationships
    supports TEXT DEFAULT '[]',             -- JSON: Finding IDs this supports
    contradicts TEXT DEFAULT '[]',          -- JSON: Finding IDs this contradicts
    derived_from TEXT DEFAULT '[]',         -- JSON: Finding IDs this was derived from
    
    -- Computed
    compound_score REAL DEFAULT 0.0,        -- Auto-calculated
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_validated TIMESTAMP,               -- When confidence was last updated
    decay_start TIMESTAMP                   -- When decay begins (default: created_at)
);

-- Confidence changes over time (Git-log for knowledge)
CREATE TABLE confidence_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    finding_id TEXT NOT NULL REFERENCES findings(id),
    old_confidence REAL,
    new_confidence REAL,
    reason TEXT,                             -- Why confidence changed
    source TEXT,                             -- What caused the change
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-finding connections (explicit + discovered)
CREATE TABLE cross_findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    finding_a TEXT NOT NULL REFERENCES findings(id),
    finding_b TEXT NOT NULL REFERENCES findings(id),
    relation TEXT,                           -- supports, contradicts, extends, synthesizes
    strength REAL DEFAULT 0.5,              -- 0.0 to 1.0
    discovered_by TEXT,                     -- "tag_match", "embedding", "llm", "manual"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- LLM-generated syntheses from finding clusters
CREATE TABLE syntheses (
    id TEXT PRIMARY KEY,                    -- "SY-001" format
    claim TEXT NOT NULL,                    -- The synthesized insight
    source_findings TEXT NOT NULL,          -- JSON: Finding IDs that produced this
    confidence REAL DEFAULT 0.50,
    model TEXT,                             -- Which LLM generated this
    validated_by_human BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Content performance tracking
CREATE TABLE content_posts (
    id TEXT PRIMARY KEY,                    -- "CP-001" format
    platform TEXT,                          -- linkedin, substack, github, twitter
    title TEXT,
    url TEXT,
    variant TEXT,                           -- A, B, C (for ABC testing)
    source_findings TEXT DEFAULT '[]',      -- JSON: Which findings informed this post
    
    -- Performance KPIs
    impressions INTEGER DEFAULT 0,
    engagement INTEGER DEFAULT 0,           -- likes + comments + shares
    engagement_rate REAL DEFAULT 0.0,
    clicks INTEGER DEFAULT 0,
    leads INTEGER DEFAULT 0,                -- DMs, emails, signups
    
    -- Attribution
    revenue_generated REAL DEFAULT 0.0,
    
    posted_at TIMESTAMP,
    metrics_updated_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Research lines (grouping of findings)
CREATE TABLE research_lines (
    id TEXT PRIMARY KEY,                    -- "RL-001" format
    name TEXT NOT NULL,                     -- "Agent Trust & Governance"
    description TEXT,
    status TEXT DEFAULT 'active',           -- active, paused, archived
    
    -- Aggregate metrics (computed)
    finding_count INTEGER DEFAULT 0,
    avg_confidence REAL DEFAULT 0.0,
    total_compound_score REAL DEFAULT 0.0,
    systems_produced INTEGER DEFAULT 0,
    content_produced INTEGER DEFAULT 0,
    revenue_generated REAL DEFAULT 0.0,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6.2 Why These Tables and Not Fewer

| Table | Why It Exists | What Happens Without It |
|---|---|---|
| `findings` | Atomic knowledge unit | No structured knowledge at all |
| `confidence_history` | Track HOW confidence changes | Can't learn which validation methods work |
| `cross_findings` | Explicit connections | Findings are isolated — no compound effect |
| `syntheses` | LLM-generated insights | Cross-findings exist but no one draws conclusions |
| `content_posts` | Track what was published + performance | No feedback loop, content is random walk |
| `research_lines` | Group findings into topics | Can't answer "which research area has highest ROI?" |

### 6.3 Why These Tables and Not More

Deliberately excluded:
- **Audience segments** — 0 posts, 0 data. Add at 50+ posts.
- **A/B test variants table** — Use `variant` field on `content_posts`. Separate table is premature.
- **Finding embeddings table** — Use at 50+ findings. Tag-match is sufficient until then.
- **Revenue attribution model** — Use simple `revenue_generated` field. Multi-touch attribution at 100+ leads.

---

## 7. Algorithms

### 7.1 Compound Score

The Compound Score answers: "How productive is this finding?"

```python
def compound_score(finding):
    usage_count = (
        len(finding.used_in_systems) * 3.0 +    # Systems usage worth 3x
        len(finding.used_in_content) * 1.0 +     # Content usage worth 1x
        len(finding.used_in_revenue) * 5.0       # Revenue usage worth 5x
    )
    
    cross_connections = len(finding.supports) + len(finding.contradicts)
    
    time_factor = relevance_decay(finding)
    
    return finding.confidence * (usage_count + cross_connections * 0.5) * time_factor
```

**Weight Rationale:**
- Revenue (5x): The market validated this knowledge. Strongest signal.
- Systems (3x): Someone built something with this. Strong signal.
- Content (1x): Someone wrote about this. Weakest usage signal.
- Cross-connections (0.5x per connection): Each connection adds value but less than direct usage.

**Assumption A5:** These weights are initial estimates. After 3 months of data, re-calibrate based on which weight configuration best predicts future usage.

### 7.2 Confidence Calculation

Confidence is Bayesian, not arithmetic:

```python
# Source confidence weights
SOURCE_WEIGHTS = {
    "own_hypothesis":    0.30,   # "I think SMBs don't check AI output"
    "conversation":      0.40,   # Discussed with domain expert
    "linkedin_poll":     0.50,   # N=50-1000, self-selected audience
    "industry_report":   0.70,   # Gartner, McKinsey, with methodology
    "academic_paper":    0.80,   # Peer-reviewed, replicable
    "own_data":          0.85,   # From our platform analytics, N>100
    "revenue_validated": 0.90,   # Someone paid money based on this
}

def update_confidence(finding, new_source_type, direction="support"):
    source_weight = SOURCE_WEIGHTS[new_source_type]
    
    if direction == "support":
        # Bayesian update toward higher confidence
        finding.confidence = (
            finding.confidence * 0.7 +
            source_weight * 0.3
        )
    elif direction == "contradict":
        # Contradictions pull confidence down harder
        finding.confidence = (
            finding.confidence * 0.6 -
            source_weight * 0.2
        )
        finding.confidence = max(0.05, finding.confidence)
        
        # If confidence drops below 0.20, mark as contested
        if finding.confidence < 0.20:
            finding.status = "contested"
    
    # Log the change
    confidence_history.append({
        "finding_id": finding.id,
        "old": old_confidence,
        "new": finding.confidence,
        "source": new_source_type,
        "reason": direction
    })
```

**Assumption A6:** The 0.7/0.3 blend ratio is conservative — it means existing confidence dominates, new evidence shifts gradually. This prevents a single poll from overriding 5 validated sources. Tune after 50+ confidence updates.

### 7.3 Relevance Decay

Knowledge ages. Some knowledge ages faster than others.

```python
import math
from datetime import datetime

DECAY_RATES = {
    "ai_technology":     90,    # AI knowledge half-life: 90 days
    "market_data":       180,   # Market data half-life: 180 days
    "human_behavior":    720,   # Psychology half-life: 2 years
    "business_model":    360,   # Business model insights: 1 year
    "personal_fact":     9999,  # "€5.0M raised" doesn't decay
    "default":           365,   # 1 year default
}

def relevance_decay(finding):
    """Returns 0.0-1.0 relevance factor based on age and category."""
    age_days = (datetime.now() - finding.created_at).days
    
    # Determine half-life from tags
    half_life = DECAY_RATES["default"]
    for tag in finding.tags:
        if tag in DECAY_RATES:
            half_life = min(half_life, DECAY_RATES[tag])
    
    # Exponential decay
    decay = math.exp(-0.693 * age_days / half_life)  # 0.693 = ln(2)
    
    # Recent validation resets decay
    if finding.last_validated:
        days_since_validation = (datetime.now() - finding.last_validated).days
        if days_since_validation < 30:
            decay = max(decay, 0.90)  # Recent validation floors decay at 0.9
    
    return decay
```

**Why Exponential Decay (Not Linear):**
- Linear: Finding loses 1% relevance per day. After 100 days = 0%. Too aggressive.
- Exponential: Finding loses 50% at half-life, then 50% of remaining, etc. Asymptotic. Old knowledge never reaches exactly 0 — it just becomes very small. A 2-year-old finding about human behavior still has ~25% relevance. A 2-year-old finding about AI technology has ~0.2% relevance.

**Assumption A7:** Decay rates are estimates. The system should track which decayed findings get re-validated (proving the decay was too aggressive) and which dead findings never get referenced again (proving the decay was too slow).

### 7.4 Contradiction Detection

When a new finding is added, check for contradictions:

```python
def check_contradictions(new_finding, all_findings):
    candidates = []
    
    # Level 1: Same tags, opposite sentiment
    for f in all_findings:
        if f.id == new_finding.id:
            continue
        shared_tags = set(new_finding.tags) & set(f.tags)
        if len(shared_tags) >= 2:  # At least 2 shared tags
            candidates.append(f)
    
    # Level 2: LLM check for semantic contradiction
    if candidates:
        prompt = f"""Given this new finding:
"{new_finding.claim}" (confidence: {new_finding.confidence})

Do any of these existing findings CONTRADICT it?
{chr(10).join(f'- {f.id}: "{f.claim}" (confidence: {f.confidence})' for f in candidates[:10])}

For each contradiction found, respond with:
CONTRADICTS: [finding_id] — [explanation]
If no contradictions: NONE"""
        
        # LLM response parsed → create cross_findings with relation="contradicts"
        # Both findings marked as "contested" if contradiction confirmed
    
    return candidates
```

**Why This Matters:** Contradictions are the most valuable signals in a knowledge system. Two findings that say opposite things force you to research which is true. Without contradiction detection, you accumulate inconsistent knowledge and never notice.

---

## 8. The Three Loops

### 8.1 Loop 1: Research → Finding → Compound Score

```
Input: Conversation, paper, observation, poll
  → Auto-Extract: "Is this a finding? claim + confidence + tags"
  → User confirms/rejects
  → Finding stored with provenance
  → Tags matched against existing findings
  → Cross-findings suggested
  → Compound Score = 0 (unused)
  
Compound effect: Each new finding checks against all existing findings.
The 50th finding generates more cross-connections than the 5th.
```

**Metric:** Findings per week, cross-findings discovered per finding

### 8.2 Loop 2: Finding → Content → KPIs → Finding

```
Input: Finding with high compound score
  → Content recommendation: "Write about Trust in AI Agents (compound score: 7.2)"
  → Platform recommendation: "LinkedIn short-form, Substack deep-dive"
  → Post published, tracked in content_posts
  → KPIs collected: impressions, engagement, leads
  → KPI attribution back to source findings
  → Finding confidence updated (engagement = weak validation, leads = strong validation)
  → Compound score recalculated
  
Compound effect: Good findings produce good content.
Good content validates findings (engagement = signal).
Validated findings get recommended more.
The flywheel accelerates.
```

**Metric:** Research-to-content conversion rate, content engagement per finding-backed post vs. non-finding-backed post

### 8.3 Loop 3: Revenue → Confidence → Research Priority

```
Input: Consulting lead says "I saw your post about AI output quality checking"
  → Track: revenue_signal on content_post
  → Attribute: content_post → source_findings
  → Update: finding.confidence += revenue_weight (0.90)
  → Update: finding.compound_score recalculated (5x weight for revenue)
  → Research line "AI Quality" now has highest compound score
  → System recommends: "Invest more research in AI Quality"
  → More findings in AI Quality → more content → more revenue
  
Compound effect: Revenue is the ultimate validation.
It tells you what the market actually values (vs. what you think it values).
Revenue-validated findings become the backbone of your knowledge system.
```

**Metric:** Revenue per research line, time from finding to first revenue signal

---

## 9. Finding Lifecycle

```
BIRTH                          LIFE                              DEATH
  │                              │                                  │
  ▼                              ▼                                  ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│          │    │          │    │          │    │          │    │          │
│  DRAFT   │───▶│  ALIVE   │───▶│ CONTESTED│───▶│  DEAD    │    │ ARCHIVED │
│          │    │          │    │          │    │          │    │          │
│ conf:0.3 │    │ conf:0.5+│    │ conf:<0.2│    │ killed_by│    │ compound │
│ unverified│   │ validated │    │ disputed │    │ recorded │    │ score: 0 │
│          │    │          │    │          │    │          │    │ but kept │
└──────────┘    └────┬─────┘    └────┬─────┘    └──────────┘    └──────────┘
                     │               │
                     │  ┌────────────┘
                     │  │ resolution
                     │  ▼
                     │  One finding wins,
                     │  one dies.
                     │  The resolution IS
                     │  a new finding.
                     │
                     ▼
                Used in system/content/revenue
                → compound score grows
                → gets recommended more
                → generates more outputs
```

**Key Rule:** Dead findings are NEVER deleted. They remain in the database with `status=dead` and `killed_by` explanation. Reasons:

1. **Prevent resurrection:** Without the dead finding, someone (or the AI) will re-discover the same wrong claim and add it again.
2. **The killing IS knowledge:** "We thought it was €5.5M but it's actually €5.0M" — the correction itself is a finding.
3. **Audit trail:** At any point, you can ask "What did we believe 3 months ago that turned out to be wrong?" This is meta-knowledge about your own knowledge quality.

---

## 10. Cross-Finding Engine

### 10.1 Three Layers (Progressive Complexity)

```
Layer 1: Tag Match (immediate, 0 cost)
  → Findings with 2+ shared tags are candidates
  → Works from day 1 with 0 findings
  → Precision: low. Recall: high.
  → Implementation: SQL query

Layer 2: Embedding Similarity (fast, low cost)
  → Embed each finding.claim
  → Cosine similarity > 0.75 = candidate
  → Works well at 50+ findings
  → Precision: medium. Recall: medium.
  → Implementation: sentence-transformers + numpy
  → Activate at: 50 findings

Layer 3: LLM Synthesis (slow, moderate cost)
  → Cluster 5+ findings with shared tags
  → Prompt: "What non-obvious conclusions emerge from these findings?"
  → Output = new Synthesis finding
  → Works well at 5+ findings per cluster
  → Precision: high (if validated). Recall: depends on clustering.
  → Implementation: GPT-4o-mini, ~$0.01 per synthesis
  → Activate at: 3 clusters with 5+ findings each
```

### 10.2 Contradiction vs. Support vs. Extension

| Relation | Definition | System Action |
|---|---|---|
| **Supports** | New evidence confirms existing finding | Increase confidence of both |
| **Contradicts** | New evidence opposes existing finding | Mark both as "contested", flag for resolution |
| **Extends** | New finding builds on existing finding | Link as derived_from, tag with same research line |
| **Synthesizes** | New insight emerges from combining findings | Create Synthesis, link source findings |

---

## 11. Content Distribution Layer

### 11.1 Platform-Specific Recommendations

```python
PLATFORM_SPECS = {
    "linkedin": {
        "format": "short-form, 1 insight per post, contrarian angle",
        "max_length": 3000,  # characters
        "optimal_length": 800,
        "frequency": "3x/week",
        "best_for": ["opinion", "experience", "contrarian"],
        "voice": "direct, personal, 'I built/experienced this'",
        "cta_required": True,
    },
    "substack": {
        "format": "long-form, data-backed, technical depth",
        "min_length": 1000,  # words
        "optimal_length": 2500,
        "frequency": "1x/week",
        "best_for": ["analysis", "deep-dive", "framework"],
        "voice": "analytical, with data, show your work",
        "cta_required": False,
    },
    "github": {
        "format": "README, code, demos",
        "frequency": "on release",
        "best_for": ["technical", "tools", "open-source"],
        "voice": "technical, docs-first, reproducible",
    },
}
```

### 11.2 Content Recommendation Algorithm

```python
def recommend_content(findings, recent_posts):
    """Recommend what to write about next, where, and why."""
    
    # Score each finding for content potential
    candidates = []
    for f in findings:
        if f.status != 'alive':
            continue
        if f.id in [p.source_findings for p in recent_posts]:  # Already written about
            continue
        
        score = (
            f.compound_score * 2.0 +           # High compound = proven value
            f.confidence * 1.0 +                # High confidence = safe to publish
            len(f.contradicts) * 3.0 +          # Controversial = engaging
            (1.0 if not f.used_in_content else 0)  # Unused in content = fresh
        )
        
        candidates.append((f, score))
    
    candidates.sort(key=lambda x: -x[1])
    
    # Match top candidates to platforms
    recommendations = []
    for finding, score in candidates[:5]:
        best_platform = match_platform(finding)
        recommendations.append({
            "finding": finding,
            "platform": best_platform,
            "score": score,
            "angle": generate_angle(finding),  # LLM: "Write about this from X perspective"
        })
    
    return recommendations
```

### 11.3 ABC Testing Framework

```
For each content topic:
  A: Florian's natural voice (direct, short, experiential)
  B: Data-driven (numbers, charts, sources)
  C: Narrative (story arc: problem → attempt → learning)

Track per variant:
  - Impressions
  - Engagement rate (engagement / impressions)
  - Click-through (if link)
  - Leads (DMs, emails)

After 10+ posts per variant:
  - Statistical significance test (chi-squared)
  - Winner per topic category
  - Update PLATFORM_SPECS with winning format per topic
```

**Assumption A8:** ABC testing requires consistent posting (3x/week LinkedIn) for at least 4 weeks to generate meaningful data. Below that frequency, sample sizes are too small.

---

## 12. KPI Attribution Chain

The full chain from Finding to Revenue:

```
Finding RF-042
  "35% of SMB operators don't check AI output quality"
  confidence: 0.65
  tags: [smb, ai-quality, market-gap]
      │
      ▼
Content Post CP-008
  Platform: LinkedIn
  Title: "I built an AI quality checker. Here's why most people don't bother."
  Source findings: [RF-042, RF-031]
  Variant: C (narrative)
      │
      ▼
KPIs (measured)
  Impressions: 3,400
  Engagement: 142 (4.2% rate)
  Clicks: 23
  Leads: 2 (DMs asking "how did you build this?")
      │
      ▼
Revenue Signal
  Lead 1: "Can you build this for our team?" → Consulting proposal €5K
  Lead 2: No conversion
      │
      ▼
Attribution flows back:
  RF-042.confidence += 0.15 (revenue_validated)
  RF-042.used_in_revenue = ["consulting-proposal-acme"]
  RF-042.compound_score: 0.65 × (3×1 + 1×1 + 5×1 + 1×0.5) = 0.65 × 9.5 = 6.2
  Research line "AI Quality" total compound score += 6.2
      │
      ▼
System recommendation:
  "AI Quality research line has highest ROI (6.2 avg compound score).
   3 findings in this line have not been used in content yet.
   Recommend: Write about RF-045 ('Pre-Flight catches errors ChatGPT repeats')
   Platform: Substack deep-dive (technical topic, long-form performs better)"
```

---

## 13. Implementation Plan

### Phase 0: Foundation (Week 1, ~2h)

| Task | Effort | Deliverable |
|---|---|---|
| Create `findings` table | 20min | DB schema |
| Create `confidence_history` table | 10min | DB schema |
| CRUD endpoints for findings | 30min | 5 API endpoints |
| Auto-extract endpoint | 30min | POST /api/findings/extract |
| Compound score calculation | 15min | Computed on read |
| Seed 5 findings from existing conversations | 15min | 5 real findings |
| Tests | 20min | 8+ tests |

**Exit Criteria:** Can create, read, update findings. Compound score is calculated. 5 real findings exist.

### Phase 1: Cross-Findings (Week 2, ~2h)

| Task | Effort | Deliverable |
|---|---|---|
| Tag-based cross-finding search | 30min | GET /api/findings/related/{id} |
| Contradiction detection (tag-based) | 30min | Flagging on create |
| `cross_findings` table | 15min | DB schema |
| Finding lifecycle (alive/contested/dead) | 20min | Status transitions |
| Research lines table + grouping | 25min | Aggregate scores |
| Tests | 20min | 6+ tests |

**Exit Criteria:** Adding a finding automatically suggests related findings. Contradictions are flagged. Research lines show aggregate compound scores.

### Phase 2: Content Loop (Week 3-4, ~3h)

| Task | Effort | Deliverable |
|---|---|---|
| `content_posts` table | 15min | DB schema |
| Content tracking endpoints | 30min | CRUD + KPI update |
| Content recommendation algorithm | 45min | GET /api/content/recommend |
| KPI attribution back to findings | 30min | Auto confidence update |
| Platform specs configuration | 15min | PLATFORM_SPECS |
| LinkedIn Poll integration (manual input) | 15min | Finding from poll results |
| Tests | 30min | 6+ tests |

**Exit Criteria:** Can track content with KPIs. KPIs flow back to finding confidence. System recommends what to write about next.

### Phase 3: Intelligence (Month 2, ~4h)

| Task | Effort | Deliverable |
|---|---|---|
| Embedding similarity (sentence-transformers) | 1h | Layer 2 cross-finding |
| LLM synthesis for finding clusters | 1h | Auto-generate insights |
| Decay algorithm | 30min | Automatic relevance degradation |
| Contradiction resolution flow | 30min | UI for resolving contested findings |
| Research line ROI dashboard | 30min | Compound score per line |
| ABC testing framework | 30min | Variant tracking + significance |

**Exit Criteria:** System discovers non-obvious connections. Syntheses are generated. Decay prevents stale knowledge from dominating.

### Phase 4: Automation (Month 3, ~3h)

| Task | Effort | Deliverable |
|---|---|---|
| Auto-extract from all Mia conversations | 1h | Background extraction |
| Weekly synthesis report | 30min | "Here's what we learned this week" |
| Content calendar auto-generation | 30min | Based on recommendations |
| Cron: decay check weekly | 15min | Auto-degrade stale findings |
| Cron: cross-finding check on new findings | 15min | Auto-suggest connections |
| Export: findings → content draft | 30min | 1-click "make LinkedIn post from findings" |

**Exit Criteria:** The system runs semi-autonomously. Florian reviews and approves, not creates from scratch.

**Total Estimated Effort: ~14 hours across 3 months**

---

## 14. Assumptions & Risks

### Assumptions

| ID | Assumption | Confidence | Impact if Wrong | Mitigation |
|---|---|---|---|---|
| A1 | Unstructured memory leads to repeated mistakes | 90% | Low — we've directly observed this | Already mitigated by correction system |
| A2 | Structured findings increase research-to-output conversion from 12% to 40% | 55% | High — core value proposition | Measure conversion rate monthly |
| A3 | Feedback loops increase content consistency | 60% | Medium — might just need discipline | Track posting frequency with/without system |
| A4 | Compound effect measurable at 30+ findings | 50% | High — below 30 it's just a database | Commit to reaching 30 findings before evaluating |
| A5 | Usage weights (revenue 5x, system 3x, content 1x) are approximately correct | 45% | Low — easily re-calibrated | Re-calibrate at 3 months |
| A6 | 0.7/0.3 confidence blend ratio is appropriate | 50% | Low — easily tuned | Track confidence accuracy over time |
| A7 | Decay rates per category are approximately correct | 40% | Medium — wrong decay = stale or lost knowledge | Track which decayed findings get re-validated |
| A8 | ABC testing needs 3x/week for 4 weeks | 65% | Medium — might need longer | Start with A-only, add B/C when frequency is stable |

### Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **R1: System dies from neglect** — Florian stops entering findings after 2 weeks | 40% | Fatal | Auto-extraction is the primary input method. Manual entry is backup, not primary. |
| **R2: Overengineering** — Build beautiful system, populate with 3 findings | 35% | High | Phase 0 is 2 hours. Don't build Phase 1 until Phase 0 has 15+ findings. |
| **R3: False confidence** — System says "high confidence" on wrong finding | 25% | High | Revenue validation as ultimate check. Multiple source types required for >0.80. |
| **R4: Confirmation bias** — System reinforces existing beliefs instead of challenging them | 30% | High | Contradiction detection is not optional — it's core. Contested status forces resolution. |
| **R5: Compound score gaming** — Florian optimizes for score instead of truth | 15% | Medium | Revenue is the hardest metric to game. Weight it highest (5x). |
| **R6: Build before Send** — This spec becomes another reason to not send emails | 60% | High | **This is a spec, not a build order. The 8 VC emails go first.** |

---

## 15. Success Metrics

### Month 1

| Metric | Target | Measurement |
|---|---|---|
| Findings created | 20+ | Count in DB |
| Auto-extracted vs. manual | >70% auto-extracted | Source type distribution |
| Cross-findings discovered | 5+ | cross_findings table count |
| Content posts tracked | 4+ | content_posts table count |
| €5.0M error recurrence | 0 | Pre-flight catch rate |

### Month 3

| Metric | Target | Measurement |
|---|---|---|
| Research-to-content conversion | >30% (up from 12%) | findings used_in_content / total findings |
| Content engagement rate | >3% average | content_posts avg engagement_rate |
| Revenue-attributed findings | 3+ | findings with used_in_revenue non-empty |
| Contested findings resolved | 5+ | contested → alive or dead transitions |
| Compound score distribution | Pareto (20% of findings have 80% of score) | Score distribution analysis |

### Month 6

| Metric | Target | Measurement |
|---|---|---|
| Total findings | 100+ | Count in DB |
| Syntheses generated | 10+ | syntheses table count |
| Revenue per research line | Measurable difference between lines | research_lines.revenue_generated |
| Content calendar accuracy | >60% of recommendations followed | recommended vs. actual posts |
| System compounds visibly | Each month's avg compound score > previous | Monthly trend |

---

## 16. Future Extensions

### 16.1 Multi-Agent Finding Network (Month 6+)

Multiple agents (Mia for research, a content agent, a sales agent) each contribute findings. Cross-agent findings are the most valuable because they bridge domains.

### 16.2 Public Knowledge Layer (Month 9+)

Some findings are publishable. A public-facing "research feed" builds credibility and attracts inbound leads. The private layer has confidence scores and revenue attribution. The public layer has claims and evidence.

### 16.3 Finding Marketplace (Month 12+)

If this works for N=1, it works for N=10. A small network of operators sharing validated findings (with privacy controls) creates a knowledge network effect. Each participant's findings validate or contradict others' findings.

### 16.4 Predictive Research Priority (Month 6+)

Given: Research line A has high compound score and rising trend. Research line B has low score and declining. Predict: Invest more in A. But also: occasionally explore C (new, unproven) to avoid local maxima. Exploration vs. exploitation (multi-armed bandit).

---

## 17. Appendix: Evidence Base

### Direct Observations (from this project)

| Observation | Finding | Confidence |
|---|---|---|
| €5.5M error repeated in 15+ documents across sessions | Unstructured memory causes repeated mistakes | 0.95 |
| 24 research documents, 3 converted to outputs | 12.5% research-to-output conversion without system | 0.85 |
| Pre-Flight catches LLM phrases that all AI providers repeat | Regex patterns work for deterministic quality checking | 0.90 |
| Bayesian trust score converges faster than linear | Bayesian > linear for small sample sizes | 0.80 |
| Corrections as regex patterns prevent 100% of known error types | Structured corrections > unstructured memory | 0.90 |

### External Evidence

| Claim | Source | Confidence |
|---|---|---|
| Knowledge workers spend 19% of time re-finding information | McKinsey Global Institute, 2012 | 0.60 (dated) |
| Spaced repetition increases retention by 200%+ vs. cramming | Ebbinghaus + modern replications | 0.85 |
| Compound interest: 7% annual return → 2x in 10 years, 4x in 20 | Mathematical fact | 1.00 |
| LinkedIn creators average 12 weeks before stopping | Various creator economy studies, 2024-2025 | 0.55 |
| Flywheel effect: small wins compound into unstoppable momentum | Jim Collins, Good to Great | 0.70 (qualitative) |

### Analogies Used

| Analogy | From | Applied To | Strength |
|---|---|---|---|
| Compound interest | Finance | Knowledge accumulation | Strong — mathematical parallel holds |
| Git history | Software engineering | Confidence history | Strong — versioning knowledge like code |
| Spaced repetition | Learning science | Decay algorithm | Medium — we track usage not recall |
| Bayesian updating | Statistics | Confidence calculation | Strong — mathematically grounded |
| Wikipedia "never delete" | Knowledge management | Finding lifecycle | Strong — proven at scale |

---

*This spec is itself a finding: RF-000. Confidence: 0.65. Status: alive. Used_in_systems: [execution-platform]. Compound score: 0 (not yet validated by implementation or revenue). Will update as we build and learn.*

---

**End of Specification**
*Total: ~3,800 words. 17 sections. 8 assumptions tracked. 6 risks identified. 4-phase implementation plan. 14 hours estimated effort.*
*Written: 2026-02-18. Review: before Phase 0 implementation.*

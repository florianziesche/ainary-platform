# Execution Platform — Design Document

**Author**: Florian Ziesche  
**Status**: ACTIVE  
**Last Updated**: 2026-02-18  
**Version**: 0.12.3  
**Tag**: [INTERN]

---

## 1. Context & Scope

The **Execution Platform** is a Human-AI compound intelligence system for Ainary Ventures. It implements a personal knowledge pipeline with four stages:

**Research → Systems → Content → Revenue**

This is NOT a generic productivity tool. It is a single-operator system designed to enforce a "Send First" culture: knowledge must flow through all stages and ship to the world, or it doesn't count. The platform combines Bayesian trust scoring, compound knowledge accumulation, and pre-flight guardrails to prevent endless iteration without delivery.

**Core Question**: How do we build knowledge that gets smarter over time while maintaining trust in AI-generated output?

---

## 2. Goals

### Primary Goals

1. **Compound Knowledge Engine (CKE)**  
   - Findings accumulate confidence over time via proper Bayesian updates  
   - Cross-finding connections create emergent insights  
   - Lifecycle management: `alive → contested → dead` (no deletion, audit trail preserved)  
   - Trust scores asymmetrically penalize mistakes (1.5x penalty)

2. **Full Pipeline Visibility**  
   - 4-stage pipeline view with conversion metrics (Research → Systems: X%)  
   - Stage health measured by conversion rates  
   - Orphan detection (findings that never ship)  
   - Research Lines track multi-finding projects

3. **Trust-Scored AI Actions**  
   - Every AI skill earns trust independently (Research, Writing, Systems, etc.)  
   - Asymmetric Bayesian: mistakes cost 1.5× more than successes  
   - Pre-flight engine prevents low-trust actions from auto-executing

4. **"Send First" Culture Enforcement**  
   - Guardrails prevent building without shipping (🟢 AUTO / 🟡 REVIEW / 🔴 CONFIRM)  
   - Action buttons enforce stage progression (can't refine before publishing)  
   - Pipeline metrics expose hoarding behavior

5. **Single Authoring Interface**  
   - Findings are the atomic unit of knowledge  
   - All inputs (conversation, research, code) become findings  
   - One place to write, version, and refine knowledge

---

## 3. Non-Goals

| What We're NOT Building | Why |
|-------------------------|-----|
| General-purpose project management | This is a personal knowledge system, not Asana |
| Multi-user collaboration | Single-operator only (Florian Ziesche) |
| CRM or deal flow tracker | Revenue stage = attribution, not sales pipeline |
| Content management system | Content stage = findings ready for publishing, not a CMS |
| Mobile app | Designed for deep work on desktop only |
| Dependency graph visualization | Deferred to Phase 5+ (complexity vs. value) |
| Vector database integration | **Explicitly rejected**: `memory_search` + Consolidation is sufficient. Pinecone/Chroma dropped. |

---

## 4. Design Decisions & Trade-offs

### Core Architectural Decisions

**D-151: Findings Never Delete, Only Die**  
- **Decision**: `lifecycle: alive | contested | dead`  
- **Why**: Audit trail. Knowledge doesn't disappear. You can see what you used to believe.  
- **Trade-off**: DB grows unbounded. Accepted — disk is cheap, lost knowledge is expensive.

**D-152: Proper Bayesian Over Weighted Average**  
- **Decision**: Use mathematically correct Bayesian updates for confidence  
- **Why**: Source reliability matters. A high-trust source should move confidence more than a low-trust one.  
- **Trade-off**: More complex math. Worth it for correctness.

**D-153: Modal Over prompt()**  
- **Decision**: Custom modal dialogs instead of native `prompt()`  
- **Why**: Native `prompt()` is amateur UX. Looks broken. Kills trust.  
- **Trade-off**: ~60 lines of modal code. Worth it for polish.

**D-154: Bidirectional Connections**  
- **Decision**: Connections are always two-way (A→B implies B→A)  
- **Why**: Knowledge flows both ways. "VC hiring relates to AI quality" means both are relevant to each other.  
- **Trade-off**: None. This is how knowledge works.

**D-155: Pipeline Conversion % as Health Metric**  
- **Decision**: Track `Research → Systems` conversion rate, not just counts  
- **Why**: Measures system effectiveness. Low conversion = hoarding.  
- **Trade-off**: Requires topic stage tracking. Small cost.

**D-156: 3-Layer Architecture (Obsidian → Platform → .md)**  
- **Decision**: Obsidian writes → Platform reads → Platform writes to separate .md files  
- **Why**: Unidirectional prevents sync conflicts. Obsidian is source of truth for input.  
- **Trade-off**: Two file hierarchies. Accepted — simplicity > elegance.

**D-157: Platform = Authoring, Memory = Retrieval**  
- **Decision**: Platform for structured knowledge creation. Memory files for AI context.  
- **Why**: Separation of concerns. Platform guarantees always-available fallback when AI fails.  
- **Trade-off**: Duplicate storage (findings in DB + memory files). Worth it for reliability.

**D-158: launchctl Over nohup**  
- **Decision**: Use macOS `launchctl` for backend process management  
- **Why**: Auto-restart on crash. Survives reboot. Proper daemon.  
- **Trade-off**: macOS-only. Accepted — single-user system.

**D-159: Self-Refine as Opt-In**  
- **Decision**: Multi-pass refinement is manual, not automatic  
- **Why**: Latency cost only justified when value is clear.  
- **Trade-off**: Slower iteration when refining. Worth it to avoid wasted tokens.

**D-160: OpenAI gpt-4o-mini Over Claude**  
- **Decision**: Use OpenAI for backend LLM calls, not Claude  
- **Why**: Anthropic API key has $0 credit balance. OpenAI key is funded.  
- **Trade-off**: Different model characteristics. Pragmatic choice.

**D-161: SQLite Over Postgres**  
- **Decision**: SQLite with WAL mode, not Postgres  
- **Why**: Single-user, localhost, zero-ops. No need for server overhead.  
- **Trade-off**: No concurrent writes. Irrelevant for 1 user.

**D-162: Vanilla JS Over React/Vue**  
- **Decision**: No build step. Single HTML file + inline JS.  
- **Why**: Fast iteration. No dependency hell. Works forever.  
- **Trade-off**: Manual DOM manipulation. Worth it for simplicity.

**D-163: Stage Detail Views (4 Dedicated Screens)**  
- **Decision**: Research/Systems/Content/Revenue each get a full-screen detail view  
- **Why**: Pipeline stages are distinct modes of work. Each needs dedicated UI.  
- **Trade-off**: More UI code. Worth it for clarity and focus.

**D-164: Asymmetric Bayesian Trust (1.5× Penalty)**  
- **Decision**: Mistakes cost 1.5× more than successes when updating trust  
- **Why**: AI errors are more costly than correct outputs. Trust should be hard to earn back.  
- **Trade-off**: Harsher trust degradation. Intentional — enforces quality.

---

## 5. Alternatives Considered

| Alternative | Why Rejected |
|-------------|--------------|
| **Notion/Obsidian Only** | No Bayesian trust. No pipeline visibility. No guardrails. |
| **Airtable** | No custom AI integration. Can't implement CKE or Pre-Flight Engine. |
| **Full React SPA** | Build complexity for 1 user. Overkill. Would slow down iteration. |
| **Pinecone / Vector DB** | **Explicitly rejected**. OpenClaw's `memory_search` + daily Consolidation is sufficient. |
| **Multi-user version** | Scope creep. This is a personal system. Multi-user = different product. |
| **Mobile-first** | Deep work requires desktop. Mobile = scope creep. |

---

## 6. System Context Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         SYSTEM CONTEXT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐                       ┌──────────────┐       │
│   │  Obsidian   │──────(writes)────────>│   Platform   │       │
│   │   (Input)   │                       │   (SQLite +  │       │
│   └─────────────┘                       │    FastAPI)  │       │
│                                         └──────┬───────┘       │
│                                                │                │
│                                        (bidirectional)          │
│                                                │                │
│   ┌─────────────┐                       ┌─────▼────────┐       │
│   │  OpenClaw   │<─────(context)────────│   Memory     │       │
│   │     Mia     │                       │   Files      │       │
│   │  (AI Agent) │                       │   (.md)      │       │
│   └─────────────┘                       └──────────────┘       │
│         │                                                       │
│         │                                                       │
│         ▼                                                       │
│   ┌─────────────┐                                              │
│   │   GitHub    │<─────(git push)───────Platform               │
│   │  (Backup)   │                                              │
│   └─────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Data Flow**:
1. Florian writes notes in Obsidian (source of truth for input)
2. Platform reads Obsidian, creates Topics + Findings
3. Platform writes structured memory files for AI retrieval
4. OpenClaw/Mia reads memory files for context in conversations
5. Platform auto-commits to GitHub (daily cron)

---

## 7. Architecture Overview

### Tech Stack
- **Frontend**: Vanilla JavaScript, single HTML file (3200+ lines)
- **Backend**: FastAPI (Python), SQLite with WAL mode
- **AI**: OpenAI GPT-4o-mini (backend LLM), OpenClaw for orchestration
- **Storage**: SQLite DB + Memory Files (.md) + Obsidian Vault
- **Process Management**: macOS launchctl (auto-restart daemon)

### Components

#### 7.1 Database Schema (18+ Tables)
- `topics` — Projects/threads (Research Lines)
- `messages` — Conversation history
- `findings` — Atomic knowledge units (alive/contested/dead)
- `connections` — Bidirectional relationships between findings
- `votes` — Human feedback on AI proposals
- `trust_scores` — Per-skill AI trust tracking
- `corrections` — Context-aware error tracking
- `topic_folders` — Hierarchical organization
- `files` — Attached documents
- `events` — Audit log
- Stage-specific tables (research lines, systems tasks, content drafts, revenue attribution)

#### 7.2 API Endpoints (60+)
**Topics**: `/topics`, `/topics/{id}`, `/topics/new`, `/topics/{id}/archive`  
**Messages**: `/topics/{id}/messages`, `/messages/send`  
**Findings**: `/findings`, `/findings/new`, `/findings/{id}/update`, `/findings/{id}/lifecycle`  
**Connections**: `/connections`, `/connections/new`, `/connections/delete`  
**Trust**: `/trust/scores`, `/trust/update`  
**Pipeline**: `/pipeline`, `/pipeline/orphans`, `/pipeline/conversions`  
**SSE**: `/stream` (real-time updates)

#### 7.3 Pre-Flight Engine (3 Layers)

**Layer 0: Rule Engine** (Deterministic)
- Check word count
- Detect all-caps
- Verify email format
- Enforce mandatory fields

**Layer 1: Heuristics** (Pattern Matching)
- LLM-sounding phrases ("delve", "leverage", "synergy")
- Overpromising language
- Missing evidence in claims

**Layer 2: Self-Critique** (LLM-Powered, Opt-In)
- Asks GPT-4o-mini to critique draft
- Scores: clarity, evidence, tone
- **Only runs on explicit request** (latency cost)

**Guardrail Levels**:
- 🟢 **AUTO**: Passes all checks → execute immediately
- 🟡 **REVIEW**: Minor issues → show warnings, allow override
- 🔴 **CONFIRM**: Major issues → require explicit confirmation

#### 7.4 Compound Knowledge Engine (CKE)

**Bayesian Confidence Updates**:
```python
# Asymmetric Bayesian: mistakes cost 1.5x more
weight = source_trust if outcome == success else source_trust * 1.5
posterior = (prior * base_weight + new_evidence * weight) / (base_weight + weight)
```

**Connection Strength**:
- Manual connections: high weight
- Co-occurrence: medium weight
- Tag overlap: low weight

**Lifecycle Management**:
- `alive`: Active, high-confidence findings
- `contested`: Conflicting evidence exists
- `dead`: Disproven, but preserved for audit trail

#### 7.5 Trust System

**Per-Skill Tracking**:
- Research (web search, summarization)
- Writing (content creation, emails)
- Systems (process design, automation)
- Analysis (data interpretation)
- Outreach (cold emails, pitches)

**Update Formula**:
```python
# Asymmetric: mistakes cost 1.5x
confidence_change = outcome_score * (1.0 if positive else 1.5)
new_score = (current_score * history_weight + confidence_change) / (history_weight + 1)
```

**Usage**:
- Pre-flight checks consult trust scores
- Low-trust skills → 🔴 CONFIRM guardrail
- High-trust skills → 🟢 AUTO execution

---

## 8. Cross-Cutting Concerns

### 8.1 Security
- **Localhost only**: No external network exposure
- **No authentication**: Single-user system on trusted device
- **CORS wide open**: Frontend and backend on same machine
- **Threat model**: Physical access to MacBook = full access (acceptable)

### 8.2 Data Integrity
- **SQLite WAL mode**: Write-ahead logging for crash recovery
- **Foreign key constraints**: Enforced in DB schema
- **Lifecycle over deletion**: Findings never delete (audit trail)
- **Version tracking**: `updated_at` timestamps on all mutable records

### 8.3 Backup & Disaster Recovery
- **Daily cron**: Auto-commit to GitHub at 23:00 (via launchctl)
- **Google Drive sync**: Obsidian vault synced via Google Drive Desktop
- **Manual export**: `/export` endpoint for full DB dump
- **Recovery time**: <5 minutes (restore from GitHub + rebuild DB from memory files)

### 8.4 Performance
- **SQLite query optimization**: Indexes on `topic_id`, `lifecycle`, `created_at`
- **SSE for real-time updates**: No polling, event-driven UI refresh
- **Lazy loading**: Topics load on-demand, not upfront
- **Memory file caching**: Daily consolidation pre-generates context files

### 8.5 Observability
- **Health endpoint**: `/api/health` (version, DB status, uptime)
- **Event log**: All mutations logged to `events` table
- **Trust dashboard**: Real-time trust scores in sidebar
- **Pipeline metrics**: Conversion rates, orphan count, stage distribution

---

## Appendix: Key Metrics

| Metric | Current (v0.12.3) | Target (v1.0) |
|--------|-------------------|---------------|
| Topics | ~40 | 200+ |
| Findings | ~150 | 1000+ |
| Trust Scores | 5 skills | 12 skills |
| Pipeline Conversion | ~30% | 60%+ |
| Orphan Rate | ~15% | <5% |

---

## Change Log

- **2026-02-18**: v0.12.3 — Ainary branding, Stage Detail Views, DESIGN-DOC.md
- **2026-02-15**: v0.12.2 — Pipeline conversion metrics, bidirectional connections
- **2026-02-10**: v0.12.0 — Pre-Flight Engine, Trust System, CKE
- **2026-02-01**: v0.10.0 — Initial release (Topics, Messages, Findings)

---

**END OF DESIGN DOCUMENT**

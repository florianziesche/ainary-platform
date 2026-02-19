# Ainary Execution Platform — Technical Documentation

**Version:** 0.12.5 | **Date:** 2026-02-19 | **Author:** Florian Ziesche + Mia

> Reference documentation (Diataxis). For formulas see [FORMULAS.md](FORMULAS.md). For schema see [DB-SCHEMA.md](DB-SCHEMA.md). For architecture see [ARCHITECTURE.md](ARCHITECTURE.md). For changelog see [CHANGELOG.md](CHANGELOG.md). For dependencies see [DEPENDENCIES.md](DEPENDENCIES.md).

---

## What Is This?

A self-improving Human-AI execution system. A UI layer between a human operator (Florian) and an AI co-founder (Mia) that tracks tasks, enforces quality, learns from corrections, and earns trust over time.

Not a chatbot. Not a project manager. A compound execution engine where every interaction makes the next one better.

## Why It Exists

The problem: AI assistants forget everything between sessions. They repeat the same mistakes. They have no concept of trust, quality gates, or earned autonomy. ChatGPT Memory is a toy — "Florian likes short answers" is not a correction engine.

The insight: Building for N=1 (one user) makes things possible that are impossible at scale. 42 personalized corrections, 9 trust-scored skills, structural validators per output type — this doesn't scale to millions of users, but it doesn't need to.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Vanilla JS)                  │
│                     index.html (~40KB)                    │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │  Topics   │  │   Chat   │  │ Context  │  │ Command │ │
│  │  Sidebar  │  │  Panel   │  │  Panel   │  │ Palette │ │
│  │ + Folders │  │ + Stream │  │ PreFlight│  │  Cmd+K  │ │
│  └──────────┘  └──────────┘  │ Trust    │  └─────────┘ │
│                               │ Steps    │               │
│                               │ Actions  │               │
│                               └──────────┘               │
└─────────────────┬───────────────────────────────────────┘
                  │ REST + WebSocket + SSE
                  ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (FastAPI + SQLite)                   │
│               app.py (~3900 LOC) + cv_generator.py       │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │              3-Layer Pre-Flight Engine             │   │
│  │  L1: Regex Patterns (<50ms, deterministic)        │   │
│  │  L2: Structural Validators (<100ms, per type)     │   │
│  │  L3: LLM-as-Judge (2-3s, REVIEW/CONFIRM only)    │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Bayesian    │  │   State      │  │   Action     │  │
│  │  Trust       │  │   Machine    │  │   Queue      │  │
│  │  Engine      │  │   6 states   │  │   + Retry    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Mia Bridge  │  │   Email      │  │   CV         │  │
│  │  (AI Stream) │  │   Send (gog) │  │   Generator  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                SQLite (workbench.db)                      │
│  27 tables — see DB-SCHEMA.md                            │
└─────────────────────────────────────────────────────────┘
```

### Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | Vanilla JS + CSS | Zero dependencies. One HTML file. No build step. |
| Backend | Python FastAPI | Async, auto-docs, Pydantic validation, SSE streaming |
| Database | SQLite 3.51.2 | Single file, WAL mode, JSON functions, good for N=1 |
| AI | OpenAI gpt-4o-mini / Anthropic claude-sonnet | Configurable dual-provider |
| Email | gog CLI → Gmail API | CLI wrapper |
| CV Gen | Headless Chrome → PDF | HTML-first, PDF for send |
| Real-time | WebSocket | Instant UI updates |

---

## The Three Engines (Core IP)

### 1. Pre-Flight Engine (3-Layer Output Quality Check)

Every AI response is automatically checked before the user sees results. See [FORMULAS.md](FORMULAS.md#3-pre-flight-scoring-3-layer-engine) for full algorithm.

- **Layer 1:** Regex Pattern Matching (<50ms) — 42 corrections, 19 unique regex patterns
- **Layer 2:** Structural Validators (<100ms) — per output type (email, linkedin, blog, report, website)
- **Layer 3:** LLM-as-Judge (2-3s) — planned, for REVIEW/CONFIRM guardrail levels only

### 2. Bayesian Trust Engine

Trust per skill domain, earned through feedback. See [FORMULAS.md](FORMULAS.md#1-bayesian-trust-update-per-skill) for formula.

```
observed_score = 100 × (up / (up + down × 1.5))
bayesian_score = (C × prior + observed × n) / (C + n)   # C=10, prior=50
```

**9 Skills:** Research (74), Report (60), Website (55), Translation (50), CV (45), Email (30), Consulting (25), LinkedIn (15), Financial (5)

**Graduated Autonomy:**
| Score | Level | Behavior |
|---|---|---|
| 0-29 | CONFIRM | Output hidden until pre-flight passes |
| 30-59 | REVIEW | Output visible with pre-flight badges |
| 60-79 | AUTO | Direct output, background pre-flight |
| 80+ | DELEGATED | Multi-step without confirmation |

### 3. Correction Propagation

Every correction becomes a permanent rule. See [FORMULAS.md](FORMULAS.md) for scoring details.

---

## State Machine

```
        ┌──────────┐
        │  active   │◄──────────────────────┐
        └────┬─────┘                        │
             │                              │
     ┌───────┼───────┐                     │
     ▼       ▼       ▼                     │
┌────────┐┌───────┐┌────────┐             │
│running ││blocked││  done  │──►┌─────────┤
└───┬────┘└───┬───┘└────────┘   │archived │
    │         │                  └─────────┘
    ▼         │
┌────────┐    │
│ error  │────┘
└────────┘
```

Valid transitions: `active→{running,blocked,done,archived}`, `running→{active,done,error,blocked}`, `blocked→{active,running}`, `done→{active,archived}`, `error→{active,running,archived}`, `archived→{active}`

---

## API Reference (84 Endpoints)

Base URL: `http://localhost:8080`

---

### 1. Topics

#### GET /api/topics

**Purpose:** List all topics, optionally filtered by stage.
**Parameters:** `?stage=` (optional) — filter by pipeline stage (research, systems, content, revenue)
**Returns:** `[{id, name, stage, parent_id, progress, meta, folder_id, folder_position, state, priority, priority_reason, priority_confidence, created_at, updated_at}]`

#### POST /api/topics

**Purpose:** Create a new topic.
**Body:** `{id: string, name: string, stage?: string, parent_id?: string, meta?: object}`
**Returns:** `{id, status: "created"}`

#### GET /api/topics/{topic_id}

**Purpose:** Get a single topic with all related data (messages, steps, docs, refs, connections, proposals, votes).
**Returns:** `{...topic, steps: [...], messages: [{...msg, proposals: [{...prop, votes: {up: N, down: N}, options: [...]}]}], documents: [...], references: [...], connections: [...]}`

#### PATCH /api/topics/{topic_id}

**Purpose:** Update topic fields.
**Body:** `{name?, stage?, folder_id?, progress?, state?, meta?}` — all optional
**Returns:** `{status: "updated"}`

#### DELETE /api/topics/{topic_id}

**Purpose:** Delete topic and cascade (messages, steps, documents, connections, events).
**Returns:** `{status: "deleted"}`

#### POST /api/topics/{topic_id}/state

**Purpose:** Transition topic state with validation. Invalid transitions return HTTP 409.
**Body:** `{state: "active"|"running"|"blocked"|"done"|"error"|"archived"}`
**Returns:** `{status: "ok", from: string, to: string}`

#### PUT /api/topics/{topic_id}/priority

**Purpose:** Set priority for a single topic.
**Body:** `{priority: "NOW"|"HIGH"|"NORMAL"|"LOW", reason: string, confidence: 0-100}`
**Returns:** `{status: "updated", priority, confidence}`

#### POST /api/topics/auto-prioritize

**Purpose:** Auto-calculate priority for all topics using 5-factor scoring. See [FORMULAS.md](FORMULAS.md#5-topic-auto-prioritization).
**Body:** None
**Returns:** `{status: "completed", summary: {total, NOW, HIGH, NORMAL, LOW}, updates: [{id, name, priority, confidence, score}]}`

#### POST /api/topics/{topic_id}/move

**Purpose:** Move topic to a folder.
**Body:** `{folder_id: string|null, position?: number}`
**Returns:** `{status: "moved"}`

#### GET /api/topics/{topic_id}/cost

**Purpose:** Get cost breakdown for a topic (total AI cost + per-message breakdown).
**Returns:**
```json
{
  "topic_id": "string",
  "total": 0.123456,
  "currency": "USD",
  "last_updated": "2026-02-19T10:30:00",
  "message_count": 5,
  "breakdown": [
    {
      "message_id": 123,
      "sender": "mia",
      "cost": 0.002345,
      "tokens_prompt": 450,
      "tokens_completion": 200,
      "created_at": "2026-02-19T09:15:00"
    }
  ]
}
```
**Note:** Only AI responses (via `/api/ai/chat`) track cost. Streaming responses (`/api/ai/stream`) do not include cost tracking due to API limitations.

#### GET /api/topics/{topic_id}/replay

**Purpose:** Session replay — chronological event stream for debugging/audit. Combines messages, events, and state changes.
**Parameters:** `?limit=100` (default)
**Returns:**
```json
{
  "topic_id": "string",
  "topic_name": "string",
  "event_count": 42,
  "timeline": [
    {
      "type": "message",
      "timestamp": "2026-02-19T09:15:00",
      "sender": "human",
      "content": "...",
      "msg_type": "text",
      "cost": 0.002345,
      "tokens": {"prompt": 450, "completion": 200}
    },
    {
      "type": "event",
      "timestamp": "2026-02-19T09:16:00",
      "event_type": "state_change",
      "detail": {"from": "active", "to": "running"}
    },
    {
      "type": "step_completed",
      "timestamp": null,
      "step": "Research complete",
      "position": 0
    }
  ]
}
```
**Use Cases:** Debug state transitions, audit AI responses, track topic evolution over time.

---

### 2. Messages & Proposals

#### POST /api/topics/{topic_id}/messages

**Purpose:** Post a message. If sender is "human", auto-generates Mia response with keyword-matching.
**Body:** `{sender: "human"|"mia"|"system", content: string, msg_type?: string, meta?: object}`
**Returns:** `{id: number, status: "created"}`

#### POST /api/messages/{message_id}/proposals

**Purpose:** Attach a proposal to a message.
**Body:** `{proposal_type: string, content: string, confidence?: number, confidence_reason?: string, options?: [{title, recommended, description, draft?}]}`
**Returns:** `{id: number, status: "created"}`

#### POST /api/proposals/{proposal_id}/choose

**Purpose:** Choose an option on a proposal. Generates contextual Mia response and may advance steps.
**Body:** `{option: "A"|"B"|"C"}`
**Returns:** `{status: "chosen"}`

#### POST /api/proposals/{proposal_id}/vote

**Purpose:** Vote on a proposal (up/down). Updates agent-level trust scores.
**Body:** `{direction: "up"|"down"}`
**Returns:** `{status: "voted"}`

---

### 3. Steps

#### POST /api/topics/{topic_id}/steps

**Purpose:** Add a step to a topic. Auto-recalculates topic progress.
**Body:** `{label: string, done?: boolean}`
**Returns:** `{id: number}`

#### PATCH /api/steps/{step_id}

**Purpose:** Toggle step done/undone. Auto-recalculates topic progress.
**Returns:** `{status: "toggled"}`

---

### 4. Findings (Compound Knowledge Engine)

#### GET /api/findings

**Purpose:** List all findings with optional filters. Compound score calculated live.
**Parameters:** `?status=` (alive|contested|dead), `?research_line=`, `?tag=`
**Returns:** `[{id, claim, confidence, status, compound_score, tags: [], used_in_systems: [], used_in_content: [], used_in_revenue: [], supports: [], contradicts: [], derived_from: [], ...}]`

#### GET /api/findings/{finding_id}

**Purpose:** Get single finding with full confidence history.
**Returns:** `{...finding, confidence_history: [{old_confidence, new_confidence, reason, source, created_at}]}`

#### POST /api/findings

**Purpose:** Create a finding. Auto-detects potential contradictions by shared tags. Confidence >1 auto-normalized to 0.0–1.0.
**Body:** `{claim: string, confidence?: number, source_type?, source_detail?, source_url?, tags?: [], research_line?, topic_id?, evidence_type?, impact?, ...}`
**Returns:** `{id: "RF-XXX", status: "created", confidence, potential_contradictions?: [...]}`

#### PUT /api/findings/{finding_id}

**Purpose:** Update finding fields. Tracks confidence changes in history. Recalculates compound score.
**Body:** Any finding field — `{claim?, confidence?, status?, tags?, stage?, ...}`
**Returns:** `{status: "updated", compound_score}`

#### POST /api/findings/{finding_id}/validate

**Purpose:** Bayesian confidence update using source reliability weights. See [FORMULAS.md](FORMULAS.md#6-finding-confidence-bayesian-updating-with-source-weights).
**Body:** `{direction: "support"|"contradict", source_type: string, reason?: string}`
**Returns:** `{status: "validated", old_confidence, new_confidence, direction, finding_status, compound_score}`

#### POST /api/findings/{finding_id}/verify

**Purpose:** Human-verify a finding. Applies Bayesian boost with reliability=0.90.
**Returns:** `{id, old_confidence, new_confidence, verified: true}`

#### GET /api/findings/{finding_id}/related

**Purpose:** Find related findings by shared tags.
**Returns:** `[{id, claim, confidence, status, shared_tags: [], relevance: 0.0-1.0}]` (max 10)

#### GET /api/findings/{finding_id}/gate

**Purpose:** Check if finding meets promotion gate requirements for its current stage.
**Returns:** `{can_promote: bool, next_stage?, checks: [{name, required, actual, passed}]}`

#### GET /api/findings-stats

**Purpose:** Aggregate knowledge engine statistics.
**Returns:** `{total, alive, contested, dead, orphans, research_lines: [{line, count, avg_confidence, total_score}]}`

#### GET /api/topics/{topic_id}/findings

**Purpose:** Get all findings associated with a topic.
**Returns:** `[{...finding, compound_score, tags: [...]}]`

#### POST /api/import/obsidian-claims

**Purpose:** Bulk import claims from Obsidian vault as findings.
**Body:** `{claims: [{id, claim, confidence, source, source_url, tags, research_line, used_in, context, status, killed_by}]}`
**Returns:** `{imported: number, skipped: number, details: {imported: [...], skipped: [...]}}`

---

### 5. Executive Board

#### GET /api/executive/kpis

**Purpose:** All KPI data in one call for the Executive Board dashboard.
**Returns:**
```json
{
  "strategic": {
    "revenue": {current, target, label},
    "sends": {current, target, label},
    "commitments": {current, target, label},
    "team_health": {current, target, label},
    "ai_cost": {current, target, label}
  },
  "operational": {
    "findings_week", "pipeline": {research, systems, content, revenue},
    "outcomes_month", "active_agents", "total_agents"
  },
  "agents": [{name, role, score, last_active}],
  "goals": [{id, month, description, target_value, current_value, status}],
  "health": {checks: [{name, value, status}], issues: number}
}
```

#### GET /api/executive/impact

**Purpose:** Impact summary — totals and 7-day breakdown by impact type.
**Returns:** `{totals: [{impact_type, total, count}], week: [{impact_type, total}]}`

#### POST /api/executive/revenue

**Purpose:** Log a revenue event.
**Body:** `{amount: number, source?: string, description?: string, date?: "YYYY-MM-DD"}`
**Returns:** `{id, status: "created", amount}`
**Errors:** 400 if amount ≤ 0

#### POST /api/executive/goals

**Purpose:** Add a monthly goal.
**Body:** `{description: string, target_value?: number, current_value?: number}`
**Returns:** `{id, status: "created"}`

#### PUT /api/executive/goals/{goal_id}

**Purpose:** Update goal progress or status.
**Body:** `{current_value?: number, status?: string}`
**Returns:** `{status: "updated"}`

---

### 6. Daily Standup (Operations)

#### GET /api/standup/today

**Purpose:** Get today's score and tasks. Creates today's entry if not exists.
**Returns:** `{score: {date, score_reset, score_current, score_ema, tasks_committed, tasks_completed, tasks_extra, sends}, tasks: [...]}`

#### POST /api/standup/tasks

**Purpose:** Add a committed task for today.
**Body:** `{description: string, is_send?: 0|1}`
**Returns:** `{id, status: "created"}`
**Errors:** 400 if description empty

#### PUT /api/standup/tasks/{task_id}

**Purpose:** Update task status.
**Body:** `{status: "done"|"missed"|"pending"}`
**Returns:** `{status: "updated"}`

#### POST /api/standup/extra

**Purpose:** Add a bonus (extra) task already completed.
**Body:** `{description: string, is_send?: 0|1}`
**Returns:** `{id, status: "created"}`

#### GET /api/standup/history

**Purpose:** Get score history for chart.
**Parameters:** `?days=14` (default)
**Returns:** `[{date, score_reset, score_current, score_ema, ...}]` in chronological order

#### PUT /api/standup/recalc

**Purpose:** Recalculate today's score based on all tasks. See [FORMULAS.md](FORMULAS.md#4-daily-standup-scoring).
**Returns:** `{score: number, ema: number}`

---

### 7. Activity Feed

#### GET /api/activity/feed

**Purpose:** Last 50 activities, newest first.
**Returns:** `[{id, agent, action, detail, result, impact_type, impact_value, date, created_at}]`

#### POST /api/activity/log

**Purpose:** Log an agent activity.
**Body:** `{agent: string, action: string, detail?: string, result?: string, impact_type?: string, impact_value?: number, date?: string}`
**Returns:** `{status: "logged"}`

#### GET /api/activity/digest

**Purpose:** Today's agent digest with alerts for inactive agents and failures.
**Returns:** `{date, agents_today: [{agent, actions, successes, failures, total_impact, impact_types}], agents_week: [...], impact: [...], inactive: [...], alerts: [{agent, type, message}]}`

#### GET /api/activity/graph

**Purpose:** 14-day activity data for visualization.
**Returns:** `{by_agent: [{date, agent, actions, successes}], totals: [{date, total, impact}]}`

---

### 8. Decisions & Backlog

#### GET /api/decisions

**Purpose:** Recent decisions, newest first (max 20).
**Returns:** `[{id, decision_id, date, question, options, mia_recommendation, florian_decision, recommendation_followed, reason}]`

#### POST /api/decisions

**Purpose:** Log a decision.
**Body:** `{decision_id: string, question: string, date?, options?, mia_recommendation?, florian_decision?, recommendation_followed?: 0|1, reason?}`
**Returns:** `{status: "logged"}`

#### GET /api/backlog

**Purpose:** Backlog items with status='backlog', priority-sorted.
**Returns:** `[{id, description, source, priority, status, assigned_to, created_at}]`

#### POST /api/backlog

**Purpose:** Add item to backlog.
**Body:** `{description: string, source?: string, priority?: "NOW"|"HIGH"|"NORMAL"|"LOW", assigned_to?: string}`
**Returns:** `{status: "added"}`

#### PUT /api/backlog/{item_id}

**Purpose:** Update backlog item.
**Body:** `{status?, priority?, assigned_to?, description?}` — any subset
**Returns:** `{status: "updated"}`

#### DELETE /api/backlog/{item_id}

**Purpose:** Remove backlog item.
**Returns:** `{status: "deleted"}`

---

### 9. Documents & Files

#### GET /api/topics/{topic_id}/documents

**Purpose:** List all documents/references for a topic.
**Returns:** `[{id, topic_id, name, path, url, doc_type, kind}]`

#### POST /api/topics/{topic_id}/documents

**Purpose:** Add a document reference (metadata only, no file upload).
**Body:** `{name: string, path?: string, url?: string, doc_type?: string}`
**Returns:** `{status: "added"}`

#### POST /api/topics/{topic_id}/upload

**Purpose:** Upload a file and attach to topic. Saves to `uploads/{topic_id}/`.
**Body:** Multipart form — `file: File, kind: "doc"|"ref"`
**Returns:** `{status: "uploaded", name, path, size}`

#### POST /api/topics/{topic_id}/add-reference

**Purpose:** Add a URL or path as a reference document.
**Body:** `{name?: string, url?: string, path?: string, doc_type?: string}`
**Returns:** `{status: "added"}`

#### DELETE /api/topics/{topic_id}/documents/{doc_id}

**Purpose:** Remove a document. Optionally deletes file from disk.
**Parameters:** `?delete_file=true` (default true)
**Returns:** `{status: "deleted", name, file_deleted: bool}`

#### GET /api/file

**Purpose:** Read a workspace file (text content).
**Parameters:** `?path=` — relative path from workspace root
**Returns:** `{path, content, truncated: bool}`
**Errors:** 403 if outside workspace, 404 if not found

#### GET /view/{path:path}

**Purpose:** Serve workspace files directly in browser. PDFs/images/HTML served as-is. Text files rendered in dark viewer.
**Returns:** File content with appropriate MIME type

---

### 10. Folders

#### GET /api/folders

**Purpose:** List all folders.
**Returns:** `[{id, name, parent_id, position, color, icon, collapsed, created_at}]`

#### POST /api/folders

**Purpose:** Create a folder.
**Body:** `{id: string, name: string, parent_id?: string, color?: string, icon?: string}`
**Returns:** `{id, status: "created"}`

#### PATCH /api/folders/{folder_id}

**Purpose:** Update folder properties.
**Body:** `{name?, parent_id?, color?, icon?, position?, collapsed?}` — any subset
**Returns:** `{status: "updated"}`

#### DELETE /api/folders/{folder_id}

**Purpose:** Delete folder. Topics become unfiled, child folders move to parent.
**Returns:** `{status: "deleted"}`

#### POST /api/folders/reorder

**Purpose:** Batch reorder folders.
**Body:** `{order: [{id, position, parent_id}]}`
**Returns:** `{status: "reordered"}`

---

### 11. Connections

#### POST /api/connections

**Purpose:** Create a directed connection between two topics.
**Body:** `{from: string, to: string, relation?: string}`
**Returns:** `{status: "connected"}`

---

### 12. Mia Bridge (AI Integration)

#### POST /api/ai/chat

**Purpose:** Non-streaming AI chat. Builds context-rich system prompt from topic data. Auto-runs pre-flight on response.
**Body:** `{message: string, topic_id: string}`
**Returns:** `{response: string, usage: {}, preflight: {...}}`
**Errors:** 504 timeout, 502 connection error, 503 no API key

#### POST /api/ai/stream

**Purpose:** Streaming AI chat via SSE. Same context building as /ai/chat. Auto pre-flight after stream completes.
**Body:** `{message: string, topic_id: string}`
**Returns:** SSE stream — `data: {"text": "..."}\n\n` ... `data: {"preflight": {...}}\n\n` ... `data: {"done": true}\n\n`

#### POST /api/mia/execute

**Purpose:** Direct Mia bridge with full topic context + trust + corrections. Supports self-refine (RF-079).
**Body:** `{task: string, topic_id?: string, context?: {}, refine?: bool}`
**Returns:** SSE stream — `data: {"chunk": "..."}\n\n` ... `data: {"refine_status": "..."}\n\n` ... `data: {"preflight": {...}}\n\n` ... `data: {"done": true}\n\n`

---

### 13. Quality (Corrections, Trust, Pre-Flight, Standards)

#### GET /api/corrections

**Purpose:** List corrections with optional filters.
**Parameters:** `?category=` (design|content|process|tone|facts), `?active=true` (default)
**Returns:** `[{id, rule, category, wrong, rght, severity, patterns: "[]", output_types: "[]", violation_count, ...}]`

#### POST /api/corrections

**Purpose:** Create a correction rule.
**Body:** `{rule: string, category?: string, wrong?: string, right?: string, source_topic?: string, severity?: 1|2|3}`
**Returns:** `{id, status: "created"}`

#### POST /api/corrections/{correction_id}/violation

**Purpose:** Record that a correction was violated. Increments violation_count.
**Body:** `{topic_id?: string}`
**Returns:** `{status: "recorded"}`

#### GET /api/preflight/{topic_id}

**Purpose:** Run 3-layer pre-flight check on topic's last Mia output. See [FORMULAS.md](FORMULAS.md#3-pre-flight-scoring-3-layer-engine).
**Returns:** `{topic_id, output_type, total_checks, skipped, passed, warned, failed, overall: "pass"|"warn"|"fail", has_output, layers_run: [1,2], checks: [{id, type, rule, category, severity, status, layer, matches?}]}`

#### GET /api/trust

**Purpose:** Get agent-level trust scores (legacy).
**Returns:** `[{agent, score, total_votes, up_votes, down_votes}]`

#### GET /api/trust/skills

**Purpose:** Get per-skill Bayesian trust scores.
**Returns:** `[{skill, score, total, up, down, updated_at}]`

#### POST /api/trust/skills/{skill}/feedback

**Purpose:** Record trust feedback. Triggers Bayesian recalculation. See [FORMULAS.md](FORMULAS.md#1-bayesian-trust-update-per-skill).
**Body:** `{direction: "up"|"down", weight?: 1-3, detail?: string, topic_id?: string}`
**Returns:** `{status: "recorded"}`

---

### 14. Events & Preferences

#### GET /api/events/{topic_id}

**Purpose:** Get topic event log.
**Parameters:** `?limit=50` (default)
**Returns:** `[{id, topic_id, event_type, detail: "{}", created_at}]`

#### POST /api/events

**Purpose:** Create an event.
**Body:** `{topic_id: string, event_type: string, detail?: object}`
**Returns:** `{status: "created"}`

---

### 15. Eval

#### POST /api/eval

**Purpose:** Submit evaluation responses.
**Body:** `[{question_id: number, answers: [string]}]`
**Returns:** `{status: "saved", date}`

#### GET /api/eval/history

**Purpose:** Get evaluation history.
**Parameters:** `?days=7` (default)
**Returns:** `[{id, question_id, answers, session_date, created_at}]`

---

### 16. Pipeline

#### GET /api/pipeline

**Purpose:** Pipeline stage stats with cross-stage flows, research lines, and orphan detection.
**Returns:**
```json
{
  "stages": {"research": {count, avg_progress}, ...},
  "total_items": number,
  "outcomes": number,
  "total_votes": number,
  "flows": {"research_to_systems": {connected, source_count, conversion_pct}, ...},
  "research_lines": [{research_line, count, avg_conf, total_score}],
  "orphans": [{id, name, stage}]
}
```

#### GET /api/pipeline/detail

**Purpose:** Full pipeline data with topics, connections, and findings per stage.
**Returns:** `{"research": [{id, name, stage, progress, state, connections_out: [...], connections_in: [...], findings_total, findings_alive}], ...}`

---

### 17. Actions Engine

#### POST /api/actions/queue

**Purpose:** Queue an action for Mia/OpenClaw to execute.
**Body:** `{topic_id: string, action_type: "send_email"|"generate_cv"|"publish", params?: {}}`
**Returns:** `{status: "queued", action_type}`

#### GET /api/actions/pending

**Purpose:** Get all pending actions (polled by Mia/OpenClaw).
**Returns:** `[{topic_id, detail: {action_type, params, status}, created_at}]`

#### POST /api/actions/complete

**Purpose:** Mark an action completed or failed.
**Body:** `{topic_id: string, action_type: string, result?: string, error?: string}`
**Returns:** `{status: "completed"|"failed"}`

#### POST /api/actions/retry

**Purpose:** Retry a failed action (max 3 retries). Resets topic state from error.
**Body:** `{topic_id: string, action_type: string, max_retries?: 3}`
**Returns:** `{status: "retrying", retry: number}`
**Errors:** 404 if no failed action, 429 if max retries exceeded

#### POST /api/actions/generate-cv/{fund_id}

**Purpose:** Generate CV PDF for a fund. Adds files as topic documents, posts Mia message, advances steps.
**Returns:** `{pdf: path, html: path, subtitle: string, size: number, ...}`

#### GET /api/actions/available-funds

**Purpose:** List funds with CV configurations.
**Returns:** `["fund_id_1", "fund_id_2", ...]`

#### POST /api/actions/send-email

**Status:** Planned: Q2 (not yet implemented)
**Purpose:** Send email via gog CLI. Logs event, updates topic state on failure.
**Body:** `{to: string, subject: string, body: string, account?: string, attachments?: [string], topic_id?: string}`
**Returns:** `{status: "sent", to, subject}`
**Errors:** 400 (invalid email, short subject/body), 500 (gog error), 504 (timeout)

---

### 18. Health & System

#### GET /api/health

**Purpose:** Health check with error summary.
**Returns:** `{status: "healthy"|"degraded", topics, error_topics, pending_actions, failed_actions, version: "0.12.3"}`

#### WebSocket /ws

**Purpose:** Real-time updates. Send "ping" to receive `{type: "pong"}`. Server broadcasts events: `topic_update`, `message`, `trust_update`, `standup_update`, `folder_update`, `activity_logged`, `finding_created`, `finding_updated`, `revenue_logged`, `goal_added`, `goal_updated`, `decision_logged`, `backlog_updated`, `priority_update`, `action_queued`, `findings_imported`, `finding_verified`.

---

## UI Features

### Keyboard Shortcuts

Press `?` to show all shortcuts in-app.

| Shortcut | Action |
|----------|--------|
| **Cmd+K** | Open command palette (search topics, actions, folders) |
| **Cmd+N** | New topic |
| **Cmd+P** | Toggle pipeline view |
| **Cmd+I** | Toggle principles view |
| **Cmd+O** | Toggle executive board |
| **Cmd+.** | Toggle context panel |
| **J / K** | Navigate topics (down / up) |
| **E** | Focus message input |
| **C** | Toggle context panel |
| **S** | Toggle topic priority (LOW → NORMAL → HIGH → NOW) |
| **D** | Mark current topic as done |
| **/** | Focus search (same as Cmd+K) |
| **?** | Show keyboard shortcuts help |
| **Esc** | Close modals |

---

## Error Handling

| Failure | Detection | HTTP | Recovery |
|---|---|---|---|
| AI timeout (>60s/120s) | httpx.TimeoutException | 504 | SSE error + event log |
| AI connection refused | httpx.ConnectError | 502 | Event log |
| Email send failure | subprocess returncode ≠ 0 | 500 | Topic → error, retry available |
| Email timeout | subprocess.TimeoutExpired | 504 | Topic → error |
| DB error | sqlite3.OperationalError | 503 | Global handler |
| Constraint violation | sqlite3.IntegrityError | 409 | Global handler |
| Action failure | error in /complete | — | Topic → error, retry (max 3) |
| Invalid state transition | — | 409 | Blocked |
| Unknown error | Exception | 500 | Traceback to stderr |

---

## Numbers

| Metric | Value |
|---|---|
| Total LOC | ~5,700 (backend ~3,900 + frontend ~1,800) |
| API endpoints | 84 |
| DB tables | 27 |
| Corrections | 42 (11 with regex, 19 unique patterns) |
| Trust skills | 9 |
| Quality standards | 18 |
| Tests | 44/44 passing |
| Dependencies (pip) | 4 (fastapi, uvicorn, httpx, python-multipart) |
| Build step | None |
| Deploy | `python3 app.py` |

---

*Built in 3 days. Documented thoroughly on day 3. Ships with `python3 app.py`.*

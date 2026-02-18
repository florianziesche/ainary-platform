# Execution Platform — Technical Documentation

**Version:** 0.10.1 | **Date:** 2026-02-18 | **Author:** Florian Ziesche + Mia

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
│                     index.html (1,787 LOC)               │
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
│               Backend (FastAPI + SQLite)                  │
│                app.py (2,259 LOC) + cv_generator.py      │
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
│  15 tables, ~800 rows                                    │
│  21 topics · 329 messages · 42 corrections · 9 skills    │
└─────────────────────────────────────────────────────────┘
```

### Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | Vanilla JS + CSS | Zero dependencies. One HTML file. No build step. Instant iteration. |
| Backend | Python FastAPI | Async, fast, auto-docs at /docs, SSE streaming native |
| Database | SQLite | Single file, zero config, JSON functions built-in, good enough for N=1 |
| AI | OpenAI gpt-4o-mini (configurable) | Cheap ($0.15/1M input), fast, good enough for corrections-aware output |
| Email | gog CLI → Gmail API | CLI wrapper, no OAuth dance in backend |
| CV Gen | Headless Chrome → PDF | HTML-first workflow, PDF only for send |
| Real-time | WebSocket | Instant UI updates on state changes, messages, actions |

### Why Vanilla JS (No React, No Framework)

1. **One file** — `index.html` is the entire frontend. Open it, it works.
2. **No build step** — Change a line, refresh browser. Iteration speed matters more than abstraction.
3. **1,787 LOC** — Small enough to hold in your head. React would be 3x the code for the same functionality.
4. **Offline-capable** — No CDN dependencies for core navigation. AI features need connection.
5. **This is a tool for one person** — Reusable components and state management are overkill.

---

## The Three Engines (Core IP)

### 1. Pre-Flight Engine (3-Layer Output Quality Check)

Every AI response is automatically checked before the user sees results.

**Layer 1: Regex Pattern Matching (<50ms)**
- 42 corrections, 11 with regex patterns (19 unique patterns)
- Categories: tone, content, design, process, facts
- Example: `\bgreat question\b` catches LLM phrases
- Example: `#(?!0a0a0a|d4a853|...)` catches non-brand colors in CSS
- Output-type filtering: patterns apply only to relevant types (email, linkedin, website, etc.)

**Layer 2: Structural Validators (<100ms)**
- Email: Has greeting? Has sign-off? Length 20-500 words?
- LinkedIn: Under 3000 chars? Has CTA?
- Blog: Has headings at >200 words? Over 300 words?
- Report: Sources cited? Percentages with sources?
- Website: Only brand colors used?

**Layer 3: LLM-as-Judge (2-3s, planned)**
- Only activated for REVIEW/CONFIRM guardrail levels
- LLM checks output against top corrections semantically
- Catches what regex can't: "That's a wonderful question" = LLM phrase variant

**Why 3 layers:** Layer 1 is free and instant — catches 80% of issues. Layer 2 catches structural problems regex can't see. Layer 3 is expensive and slow — only used when trust is low.

### 2. Bayesian Trust Engine

Trust per skill domain, earned through feedback, not assigned.

**Formula:**
```
observed_score = 100 × (up / (up + down × 1.5))    # Asymmetric: mistakes cost 50% more
bayesian_score = (C × prior + observed × n) / (C + n)   # C=10, prior=50
```

**Why Bayesian, not linear (+2/-3):**
- Linear: 10 ups then 1 down = score jumps erratically
- Bayesian: 10 ups then 1 down = score barely moves (high confidence in quality)
- Prior of 50: new skills start neutral, not at zero
- Asymmetric downs (1.5x): mistakes should cost more than successes earn
- More data points → score converges to real quality

**9 Skills:** Research (74), Report (60), Website (55), Translation (50), CV (45), Email (30), Consulting (25), LinkedIn (15), Financial (5)

**Graduated Autonomy:**
| Score | Level | Behavior |
|---|---|---|
| 0-29 | CONFIRM | Output hidden until pre-flight passes. Every action needs explicit confirmation. |
| 30-59 | REVIEW | Output visible with pre-flight badges inline. Actions need 1-click confirmation. |
| 60-79 | AUTO | Output shown directly. Pre-flight runs in background. Actions execute immediately. |
| 80+ | DELEGATED | Multi-step workflows without confirmation. User informed, not asked. |

### 3. Correction Propagation

Every correction becomes a permanent rule that prevents the same mistake.

**Flow:**
```
User corrects output ("€5.0M not €5.5M")
    → Correction stored with regex pattern: 5[.,]5\s*M
        → Pre-Flight checks ALL future outputs against this pattern
            → Fewer corrections needed → Trust increases
                → More autonomy → Less user time per task
```

**Correction Schema:**
```json
{
  "rule": "Fundraising = €5.0M (€3.5M equity + €1.5M grants). NOT €5.5M.",
  "category": "facts",
  "wrong": "5.5M",
  "right": "5.0M",
  "severity": 3,
  "patterns": ["5[.,]5\\s*M", "€5[.,]5", "5\\.5\\s*million"],
  "output_types": ["all"],
  "active": true,
  "violation_count": 0
}
```

**Categories:** tone (LLM phrases, voice), content (fake numbers, sources), design (colors, fonts), process (workflow rules), facts (verified data)

---

## State Machine

Topics have lifecycle states with validated transitions:

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

Invalid transitions return HTTP 409. Every transition is logged as an event.

---

## Error Recovery

| Failure | Detection | Recovery |
|---|---|---|
| AI timeout (>60s/120s) | httpx.TimeoutException | SSE error message + event log + system message visible in chat |
| AI connection refused | httpx.ConnectError | HTTP 502 + event log |
| Email send failure | subprocess returncode ≠ 0 | Topic state → error, stderr logged, retry available |
| Email timeout | subprocess.TimeoutExpired | Topic state → error, retry available |
| DB error | sqlite3.OperationalError | Global handler → HTTP 503 |
| Constraint violation | sqlite3.IntegrityError | Global handler → HTTP 409 |
| Action failure | error field in /complete | Topic state → error, retry with counter (max 3) |
| Unknown error | Exception base class | Global handler → HTTP 500 + traceback to stderr |

**Retry Pattern:**
```
Queue action → Execute → Fail → Retry (counter +1) → Execute → Fail → Retry (counter +2) → ... → Max 3 → Stop
```

---

## API Surface (47 Endpoints)

### Core
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/topics` | List all topics |
| GET | `/api/topics/{id}` | Get single topic |
| POST | `/api/topics` | Create topic |
| DELETE | `/api/topics/{id}` | Delete topic |
| POST | `/api/topics/{id}/messages` | Post message |
| POST | `/api/topics/{id}/state` | Transition state (validated) |
| POST | `/api/topics/{id}/steps` | Add step |
| POST | `/api/topics/{id}/move` | Move to folder |

### Pre-Flight & Trust
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/preflight/{id}` | Run 3-layer pre-flight check |
| GET | `/api/trust/skills` | List all trust skills with scores |
| POST | `/api/trust/skills/{skill}/feedback` | Bayesian trust update (up/down) |
| GET | `/api/corrections` | List all corrections |
| POST | `/api/corrections` | Create correction with patterns |

### AI
| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/ai/chat` | Non-streaming AI + auto pre-flight |
| POST | `/api/ai/stream` | SSE streaming AI + auto pre-flight |
| POST | `/api/mia/execute` | Mia bridge with full topic context |

### Actions
| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/actions/queue` | Queue action for execution |
| GET | `/api/actions/pending` | Poll pending actions (for OpenClaw) |
| POST | `/api/actions/complete` | Mark action done/failed |
| POST | `/api/actions/retry` | Retry failed action (max 3) |
| POST | `/api/actions/send-email` | Send email via gog CLI |
| POST | `/api/actions/generate-cv/{fund}` | Generate CV PDF |

### Documents & Files
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/topics/{id}/documents` | List documents |
| POST | `/api/topics/{id}/upload` | Upload file |
| POST | `/api/topics/{id}/add-reference` | Add URL/path reference |
| DELETE | `/api/topics/{id}/documents/{doc_id}` | Delete document + optional file |

### System
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Health check with error counts |
| GET | `/api/pipeline` | Stage-level stats |
| WS | `/ws` | Real-time updates |

---

## Database Schema (15 Tables)

```sql
topics (21 rows)
  id TEXT PK, name, stage, parent_id, progress, meta JSON,
  folder_id, folder_position, state TEXT

messages (329 rows)
  id INTEGER PK, topic_id FK, sender, content, msg_type, meta JSON

corrections (42 rows)
  id INTEGER PK, rule, category, wrong, rght, severity,
  patterns JSON, output_types JSON, active, violation_count

trust_skills (9 rows)
  skill TEXT PK, score, total, up, down

quality_standards (18 rows)
  id INTEGER PK, rule, category, output_type, active

events (92 rows)
  id INTEGER PK, topic_id, event_type, detail JSON

folders (7 rows)
  id TEXT PK, name, parent_id, position, color, icon, collapsed

documents (71 rows)
  id INTEGER PK, topic_id, name, path, url, doc_type, kind

steps (50 rows)
  id INTEGER PK, topic_id, label, done, position

proposals (166 rows)
  id INTEGER PK, message_id, proposal_type, content,
  confidence, confidence_reason, options JSON

connections (6 rows)
  id INTEGER PK, from_topic, to_topic, relation

votes (1 row)
  id INTEGER PK, proposal_id, direction
```

---

## What Makes This Different

1. **Corrections compound.** Every mistake becomes a permanent regex rule. The system gets better with every interaction, not just within a session, but across all future sessions.

2. **Trust is earned, not configured.** Bayesian scoring means the system starts cautious and earns autonomy through demonstrated quality. Bad outputs in one skill don't affect other skills.

3. **Pre-Flight is deterministic.** Layer 1 and 2 don't use AI — they're regex and structural checks. Reproducible, instant, free, offline-capable. AI (Layer 3) is only invoked when trust is low.

4. **N=1 advantage.** 42 corrections tailored to one person's standards. 18 quality standards per output type. 9 skill-specific trust scores. This personalization is impossible at scale — and that's the point.

5. **Error recovery is visible.** Failed actions don't silently disappear. They set topic state to error, log the failure, show it in chat, and offer retry with backoff. The user always knows what happened.

---

## Test Coverage

**44 tests, 0 failures.** Categories:

| Category | Tests | What's Covered |
|---|---|---|
| Topics CRUD | 5 | List, get, 404, create/delete, update |
| Messages | 1 | Post message |
| Corrections | 3 | List, create, filter by category |
| Pre-Flight | 5 | Basic check, 404, layer info, clean pass, LLM slop detection |
| Trust | 3 | List skills, feedback, Bayesian scoring math |
| Folders | 1 | List |
| Events | 1 | Get events |
| Actions | 4 | Queue, pending, email validation (bad address + short body) |
| AI | 1 | Chat endpoint exists |
| Pipeline | 1 | Stats |
| Health | 2 | Endpoint, counts |
| State Machine | 4 | Valid transition, invalid blocked, bad value, error recovery |
| Retry | 2 | 404 on non-failed, fail+retry cycle |
| Mia Bridge | 2 | Empty task rejected, SSE streaming |
| Error Handling | 9 | Auto pre-flight, malformed JSON, empty body, XSS, long message, nonexistent topic, empty topic pre-flight, double complete, concurrent access |

---

## Numbers

| Metric | Value |
|---|---|
| Total LOC | 4,498 (backend 2,259 + frontend 1,787 + tests 452) |
| API endpoints | 47 |
| DB tables | 15 |
| Corrections | 42 (11 with regex patterns, 19 unique patterns) |
| Trust skills | 9 |
| Quality standards | 18 |
| Tests | 44/44 passing |
| Topics | 21 |
| Messages | 329 |
| Git commits | 6 |
| Dependencies | FastAPI, uvicorn, httpx, sqlite3 (stdlib) |
| External services | OpenAI API, Gmail (via gog CLI) |
| Build step | None |
| Deploy | `python3 app.py` |

---

*Built in 3 days. Documented in 10 minutes. Ships with `python3 app.py`.*

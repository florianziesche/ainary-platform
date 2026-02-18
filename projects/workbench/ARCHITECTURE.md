# Architecture — Execution Platform v0.7

*Last updated: 2026-02-18 | Maintainer: Mia (AI) + Florian Ziesche*

---

## 1. System Overview

```
┌─────────────────────────────────────────────────────────┐
│                     FLORIAN (User)                      │
│              Browser: localhost:8080                     │
└──────────┬──────────────────────────────▲────────────────┘
           │ HTTP / WebSocket             │ HTML/JSON
┌──────────▼──────────────────────────────┴────────────────┐
│                  FRONTEND (index.html)                   │
│  Vanilla JS · WebSocket · Drag&Drop · Keyboard Events   │
│  No framework · <100ms target · Single file             │
└──────────┬──────────────────────────────▲────────────────┘
           │ REST API / WS               │ JSON / Events
┌──────────▼──────────────────────────────┴────────────────┐
│                BACKEND (FastAPI + SQLite)                │
│  app.py · cv_generator.py · workbench.db                │
│  Port 8080 · CORS * · WebSocket Hub                     │
├─────────────────────────────────────────────────────────┤
│  ACTION LAYER (abstracted — swappable)                  │
│  ┌──────────────┐  ┌────────────┐  ┌────────────────┐  │
│  │ OpenClaw API │  │ Direct API │  │ Rule Engine    │  │
│  │ sessions_send│  │ Anthropic  │  │ (current)      │  │
│  └──────────────┘  └────────────┘  └────────────────┘  │
└──────────┬──────────────────────────────▲────────────────┘
           │ sessions_send               │ Response
┌──────────▼──────────────────────────────┴────────────────┐
│                    MIA (OpenClaw)                        │
│  Claude Opus · Tools · Memory · Cron                    │
└─────────────────────────────────────────────────────────┘
```

## 2. Data Model (ERD)

```
folders 1──∞ topics 1──∞ messages 1──∞ proposals 1──∞ votes
                │
                ├──∞ steps
                ├──∞ documents
                ├──∞ events
                └──∞ connections (self-referencing)

corrections (global)
quality_standards (global, per output_type)
trust_skills (global, per skill)
preferences (per scope)
```

### Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `folders` | Hierarchical organization (Finder-style) | id, name, parent_id, position, color, icon, collapsed |
| `topics` | Core work items | id, name, stage, folder_id, state, progress, meta (JSON) |
| `messages` | Conversation per topic | topic_id, sender (human/mia/system), content |
| `proposals` | AI recommendations with options | message_id, type, confidence, options (JSON), chosen_option |
| `votes` | Feedback on proposals | proposal_id, direction (up/down) |
| `steps` | Progress tracking per topic | topic_id, label, done, position |
| `documents` | Attached files | topic_id, name, path, url, doc_type, kind (doc/ref) |
| `connections` | Topic dependency graph | from_topic, to_topic, relation, trigger_type, auto_action |
| `corrections` | Learned rules from feedback | rule, category, wrong, right, severity, violation_count |
| `quality_standards` | Per-output-type standards | rule, category, output_type |
| `trust_skills` | Granular trust per capability | skill, score, total, up, down |
| `events` | Audit log | topic_id, event_type, detail (JSON) |
| `preferences` | Learned preferences per scope | scope, key, value, confidence, data_points |

## 3. API Endpoints

### Topics
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/topics` | List all (optional ?stage=) |
| POST | `/api/topics` | Create topic |
| GET | `/api/topics/{id}` | Full topic with messages, steps, docs |
| PATCH | `/api/topics/{id}` | Update topic fields |
| DELETE | `/api/topics/{id}` | Delete topic + cascade |
| POST | `/api/topics/{id}/messages` | Add message (triggers auto-response) |
| POST | `/api/topics/{id}/steps` | Add step |
| POST | `/api/topics/{id}/documents` | Add document reference |
| POST | `/api/topics/{id}/move` | Move to folder |
| POST | `/api/topics/{id}/upload` | Upload file (multipart) |
| POST | `/api/topics/{id}/add-reference` | Add URL/path as reference |

### Folders
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/folders` | List all folders |
| POST | `/api/folders` | Create folder |
| PATCH | `/api/folders/{id}` | Update folder |
| DELETE | `/api/folders/{id}` | Delete (topics unassigned) |
| POST | `/api/folders/reorder` | Batch reorder |

### Corrections & Quality
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/corrections` | List corrections (?category=, ?active=) |
| POST | `/api/corrections` | Create correction |
| POST | `/api/corrections/{id}/violation` | Record violation |
| GET | `/api/preflight/{topic_id}` | Run pre-flight checks |

### Trust
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/trust` | Agent-level trust scores |
| GET | `/api/trust/skills` | Granular skill trust |
| POST | `/api/trust/skills/{skill}/feedback` | Record skill feedback |

### Events
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/events/{topic_id}` | Topic event log |
| POST | `/api/events` | Create event |

### Actions
| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/actions/generate-cv/{fund_id}` | Generate CV for fund |
| GET | `/api/actions/available-funds` | List CV fund configs |

### Pipeline
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/pipeline` | Pipeline stage stats |

### Utility
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/file` | Read workspace file |
| GET | `/view/{path}` | Serve file in browser |
| WS | `/ws` | WebSocket for live updates |

## 4. Security Considerations (ISO 27001 aligned)

| Control | Status | Notes |
|---------|--------|-------|
| **Access Control** | ⚠️ Localhost only | No auth needed (single user, local). Remote deployment requires JWT/OAuth. |
| **Data Classification** | ✅ | All data = INTERNAL. No PII exposed externally. |
| **Input Validation** | ✅ | Pydantic models validate all API inputs. File uploads sanitized (safe_name). |
| **SQL Injection** | ✅ | Parameterized queries only. No string concatenation in SQL. |
| **XSS** | ⚠️ | innerHTML used in frontend. Content from DB not escaped. Mitigated by localhost-only. |
| **File Upload** | ✅ | Stored in sandboxed uploads/ dir. Filename sanitized. No execution. |
| **Audit Trail** | ✅ | Events table logs all state changes, uploads, feedback. |
| **Backup** | ⚠️ | Daily backup via OpenClaw cron (Google Drive). main.sqlite backup pending. |
| **Availability** | ⚠️ | No auto-restart yet. Planned: launchctl agent. |
| **Data Integrity** | ✅ | SQLite WAL mode. Foreign keys enforced. |

## 5. Quality Management (ISO 9001 aligned)

### Quality Objectives
1. Output quality improves with every correction (measurable via violation_count trend)
2. Trust scores converge toward real capability (measurable via up/down ratio)
3. Pre-flight checks catch 80%+ of issues before user sees output
4. Zero data loss during development iterations

### Quality Processes
- **Correction Propagation**: Every user correction → permanent rule → applied to all future outputs
- **Pre-Flight Gate**: Automated check against all corrections + standards before delivery
- **Regression Detection**: Output score compared against baseline (planned Phase 4)
- **Feedback Loop**: Approve/Correct/Reject → Trust adjustment → Autonomy adjustment

### Continuous Improvement
- CHANGELOG.md tracks all changes with rationale
- PLATFORM-SPEC.md tracks requirements with status
- Decisions documented in memory/decisions.md with alternatives considered
- Failed outputs logged in memory/failed-outputs.md for pattern analysis

## 6. File Structure

```
projects/workbench/
├── index.html              # Frontend (single file, ~40KB)
├── PLATFORM-SPEC.md        # Requirements specification (20 items)
├── ARCHITECTURE.md         # This file
├── CHANGELOG.md            # Version history
├── ROADMAP.md              # Build phases + timeline
├── uploads/                # User-uploaded files per topic
│   └── {topic_id}/
│       └── {filename}
└── backend/
    ├── app.py              # FastAPI server (~1000 lines)
    ├── cv_generator.py     # CV generation engine
    └── workbench.db        # SQLite database
```

## 7. Technology Decisions

| Decision | Choice | Rationale | Alternatives Considered |
|----------|--------|-----------|------------------------|
| Frontend | Vanilla JS | Speed (<100ms), no build step, single file | React, Vue, Svelte |
| Backend | FastAPI | Async, auto-docs, Pydantic validation, Python ecosystem | Express, Flask |
| Database | SQLite | Zero config, single file, fast for single-user | PostgreSQL, Redis |
| Real-time | WebSocket | Native browser support, low latency | SSE, polling |
| Styling | CSS-in-HTML | Single file deployment, no build step | Tailwind, CSS modules |
| AI Backend | OpenClaw (abstracted) | Already running, session management, tools | Direct API, Ollama |

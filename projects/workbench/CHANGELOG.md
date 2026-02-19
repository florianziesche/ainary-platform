# Changelog — Ainary Execution Platform

All notable changes. Format: [ISO 8601 Date] [Version] [Category].

---

## [0.13.0] — 2026-02-19

### Added
- **Phase A: Database Performance**
  - 7 new indexes for frequently queried tables (messages, findings, events, daily_scores, activity_feed)
  - Verified: EXPLAIN QUERY PLAN shows index usage for topic_id lookups

- **Phase B: Cost Tracking**
  - GET /api/topics/{id}/cost endpoint: per-topic AI cost breakdown with per-message details
  - Total AI Cost KPI in Executive Board (5th strategic metric, target $10/month)
  - Cost tracking in messages table: cost, tokens_prompt, tokens_completion
  - Cost aggregation in topics table: cost_total, cost_updated_at
  - Automatic cost calculation and storage for all /api/ai/chat responses

- **Phase C: Session Replay + Keyboard Shortcuts**
  - GET /api/topics/{id}/replay endpoint: chronological timeline of messages, events, state changes
  - New keyboard shortcuts:
    - **S**: Toggle topic priority (LOW → NORMAL → HIGH → NOW)
    - **D**: Mark current topic as done
    - **/**: Focus search (same as Cmd+K)
    - **?**: Show keyboard shortcuts help modal

### Changed
- Version: 0.12.6 → 0.13.0
- Executive Board UI: 4-column → 5-column grid for strategic KPIs
- DOCUMENTATION.md: send-email endpoint marked as "Planned: Q2"

### Technical Notes
- Cost tracking limitation: /api/ai/stream does not track cost (streaming APIs don't return token counts)
- DB backups: workbench.db.bak-phase-a, workbench.db.bak-phase-b
- All changes additive, backward compatible

---

---

## [0.12.6] — 2026-02-19

### Changed
- **BREAKING: Trust System Merge** — `trust_scores` (agent-level) deprecated in favor of `trust_skills` (skill-level Bayesian)
  - `GET /api/trust` now returns `trust_skills` data with `X-Deprecation-Warning` header
  - Vote endpoint (`POST /api/proposals/{id}/vote`) redirects to `trust_skills` with skill="general"
  - Legacy `trust_scores` table kept for archival (exported to `trust_scores_archive.json`)
  - **Migration:** Database backed up, no data loss
  - **Impact:** Frontend using `GET /api/trust` will receive skill-level data instead of agent-level (structure change)
  - **Recommended:** Update clients to use `GET /api/trust/skills` directly

### Fixed
- Trust system redundancy eliminated — single source of truth established

---

## [0.12.5] — 2026-02-19

### Added
- **Impact Summary** (Executive Board): `GET /api/executive/impact` — aggregated impact by type with 7-day breakdown
- **Evidence Gates**: `GET /api/findings/{id}/gate` — stage promotion requirements (confidence, evidence type, source count) per pipeline stage
- **Dot-Grid CI**: Consistent brand dot-grid pattern across all views
- **Folder References in Goals**: Monthly goals now support folder-level organization
- **Full Documentation Suite**: DOCUMENTATION.md (84 endpoints), DB-SCHEMA.md (27 tables), FORMULAS.md (7 algorithms), DEPENDENCIES.md

### Fixed
- **Confidence Normalization**: Values >1 (e.g. 85) now auto-normalized to 0.0–1.0 range in create/update finding endpoints
- **Clamping**: Bayesian confidence updates clamped to [0.02, 0.98] to prevent certainty traps

---

## [0.12.4] — 2026-02-18

### Added
- **Executive Board**: Full CEO/COO dashboard with strategic + operational KPIs
  - `GET /api/executive/kpis` — revenue YTD, sends/week, commitments kept, team health, pipeline flow, system health
  - `POST /api/executive/revenue` — manual revenue event logging
  - `POST /api/executive/goals` + `PUT /api/executive/goals/{id}` — monthly goal tracking
- **Operations Tab**: Daily standup system with scoring
  - `GET /api/standup/today` — today's score + tasks
  - `POST /api/standup/tasks` — commit daily tasks
  - `PUT /api/standup/tasks/{id}` — mark tasks done/missed
  - `POST /api/standup/extra` — log bonus tasks
  - `GET /api/standup/history` — 14-day score trend
  - `PUT /api/standup/recalc` — recalculate daily score with EMA
- **Topic Priorities**: Auto-prioritization engine with 5-factor scoring
  - `PUT /api/topics/{id}/priority` — manual priority update
  - `POST /api/topics/auto-prioritize` — batch auto-calculate
- **Activity Feed**: Agent activity tracking + digest + graph
  - `GET /api/activity/feed` — last 50 activities
  - `POST /api/activity/log` — log agent activity
  - `GET /api/activity/digest` — daily digest with alerts
  - `GET /api/activity/graph` — 14-day activity chart data
- **Decisions + Backlog**: Decision log + prioritized backlog
  - `GET/POST /api/decisions` — decision tracking
  - `GET/POST/PUT/DELETE /api/backlog` — backlog CRUD
- **CEO/COO Tabs**: Separate strategic (CEO) and operational (COO) views in Executive Board

---

## [0.12.3] — 2026-02-18

### Added
- **Ainary Branding**: Renamed from "Execution Platform" to "Ainary Execution Platform"
- **DESIGN-DOC.md**: Design document following Google Design Doc pattern (Malte Ubl)
- **4 Stage Detail Views**: `GET /api/pipeline/detail` — full cross-stage pipeline with connections, findings per topic
- **101 Findings Organized**: Compound Knowledge Engine with Bayesian confidence tracking
  - `GET/POST /api/findings` — CRUD with filters (status, research_line, tag)
  - `GET/PUT /api/findings/{id}` — single finding with confidence history
  - `POST /api/findings/{id}/validate` — Bayesian confidence update with source weights
  - `POST /api/findings/{id}/verify` — human verification boost
  - `GET /api/findings/{id}/related` — find related by shared tags
  - `GET /api/findings/{id}/gate` — evidence gate checks
  - `GET /api/findings-stats` — aggregate stats
  - `GET /api/topics/{id}/findings` — per-topic findings
  - `POST /api/import/obsidian-claims` — bulk import from Obsidian

---

## [0.8.0] — 2026-02-18

### Added
- **Live AI Integration** (R-007): Direct Anthropic/OpenAI API with streaming SSE responses
- **Dual Provider**: OpenAI (gpt-4o-mini) + Anthropic (claude-sonnet), configurable via `AI_PROVIDER`
- **Context-Aware System Prompt**: AI receives full topic context (steps, docs, corrections, standards, trust scores, recent messages)
- **Guardrails System** (R-013): Trust-based permission levels — 🟢 AUTO (≥60), 🟡 REVIEW (≥30), 🔴 CONFIRM (<30)
- **Action Bar**: Context-aware action buttons with guardrail badges (CV generieren, Email senden, Mia fragen)
- **Action Queue**: Pending actions API for OpenClaw/Mia to poll and execute tool-based actions
- **Command Palette** (Cmd+K): Fuzzy search over all topics, folders, and actions — Linear-style
- **Keyboard Shortcuts**: J/K (navigate topics), E (edit), C (context panel), Cmd+N (new topic), Cmd+. (toggle context)
- **Confirm Dialog**: Explicit confirmation required for low-trust actions (🔴 CONFIRM level)
- **Streaming Responses**: Token-by-token rendering with typing indicator
- **Error Handling**: Graceful degradation with "Mia offline?" message when AI unavailable

### Fixed
- Trust skill lookup case-sensitivity in guardrails
- `#conv` element ID mismatch in streaming response code
- Duplicate seed prevention (corrections, standards)

### Dependencies
- Added `httpx` for async HTTP client (AI API calls)
- Added `python-multipart` for file upload

---

## [0.7.0] — 2026-02-18

### Added
- **Correction Engine** (R-010): 29 corrections imported, 5 categories (design, content, process, tone, facts), 3 severity levels
- **Quality Standards** (R-011): 18 standards per output-type (email, linkedin, blog, report, website, general)
- **Trust per Skill** (R-012): 9 skills with Bayesian scores, color-coded bars
- **Pre-Flight API** (R-011): 3-layer engine (L1 regex, L2 structural, L3 LLM placeholder)
- **Event/Audit Log** (R-018): Full event logging
- **Folder Sidebar** (R-001): 7 default folders, drag & drop, collapse/expand
- **New Topic Creation**: Modal with name, stage, folder, output-type, contact, email
- **File Upload**: Upload documents and references per topic
- **Context Panel**: Documents, References, Quality Gate, Active Corrections, Connected Topics, Activity Log
- **Preferences Table**: Schema for preference learning (R-014)

### Fixed
- FastAPI Static Mount routing conflict
- Duplicate seed data on restart

---

## [0.6.0] — 2026-02-17

### Added
- Initial Execution Platform with Flywheel Pipeline
- Topic-based conversations with Mia (keyword-matching)
- Proposals with A/B options, confidence scores, voting
- Step tracking with progress calculation
- CV Generator integration (7 fund configs)
- WebSocket real-time updates
- Trust scores (agent-level)
- Connection graph between topics

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 0.12.5 | 2026-02-19 | Impact Summary, Evidence Gates, Documentation Suite, Confidence Fix |
| 0.12.4 | 2026-02-18 | Executive Board, Operations, Priorities, Activity Feed, Decisions+Backlog |
| 0.12.3 | 2026-02-18 | Ainary Branding, DESIGN-DOC, Stage Detail Views, 101 Findings |
| 0.8.0 | 2026-02-18 | AI Integration, Guardrails, Action Queue, Command Palette, Streaming |
| 0.7.0 | 2026-02-18 | Correction Engine, Trust per Skill, Folders, Upload |
| 0.6.0 | 2026-02-17 | Initial platform: conversations, proposals, CV generator |

# Changelog — Execution Platform

All notable changes to the Execution Platform. Format: [ISO 8601 Date] [Version] [Category].

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
- **Correction Engine** (R-010): 29 corrections imported from corrections.md, 5 categories (design, content, process, tone, facts), 3 severity levels
- **Quality Standards** (R-011): 18 standards imported from quality-standards.md, per output-type (email, linkedin, blog, report, website, general)
- **Trust per Skill** (R-012): 9 skills with scores (research:70, cv:45, linkedin:15, financial:5), color-coded bars in sidebar
- **Pre-Flight API** (R-011): `/api/preflight/{topic_id}` returns all applicable checks
- **Event/Audit Log** (R-018): `/api/events/{topic_id}`, logs file uploads, trust feedback, correction violations
- **Folder Sidebar** (R-001): 7 default folders (Heute, Wichtig, VC Applications, Consulting, Content, Admin/Legal, Später), drag & drop, collapse/expand, rename, delete
- **New Topic Creation**: Modal with name, stage, folder, output-type, contact, email
- **File Upload**: Upload documents and references per topic, stored in uploads/{topic_id}/
- **Add Reference**: URL or file path as reference with gold-border styling
- **Context Panel**: Documents, References, Quality Gate checklist, Active Corrections, Connected Topics, Activity Log
- **Pre-Flight Badge**: Shows check count in topic header
- **Preferences Table**: Schema ready for preference learning (R-014)

### Fixed
- FastAPI Static Mount routing conflict (old processes on port 8080 not killed)
- Duplicate seed data on restart (changed to existence-check before insert)
- Installed python-multipart for file upload support

### Architecture
- Backend: FastAPI + SQLite (workbench.db), 8 new tables
- Frontend: Single HTML + Vanilla JS, WebSocket live updates
- Design System: Inter font, #0a0a0a bg, #d4a853 warm accent, #c47070 danger

---

## [0.6.0] — 2026-02-17

### Added
- Initial Execution Platform with Flywheel Pipeline
- Topic-based conversations with Mia (keyword-matching)
- Proposals with A/B options, confidence scores, voting
- Step tracking with progress calculation
- CV Generator integration (7 fund configs)
- WebSocket real-time updates (debounced, scroll-aware)
- File viewer overlay
- Trust scores (agent-level)
- Connection graph between topics
- 20 seeded topics with messages, proposals, steps

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 0.7.0 | 2026-02-18 | Correction Engine, Trust per Skill, Folders, Upload, New Topics |
| 0.6.0 | 2026-02-17 | Initial platform: conversations, proposals, CV generator |

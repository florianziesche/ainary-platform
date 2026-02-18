# Roadmap — Execution Platform

*Version: 0.7.0 → 1.0.0*
*Updated: 2026-02-18*
*Done Definition v1.0: Fehlerfrei + Live AI + Trust System + 5 VC Emails durch Platform gesendet*

---

## Phase 0: Foundation ✅ DONE (v0.6-v0.7)
- [x] Flywheel Pipeline (Research → Systems → Content → Revenue)
- [x] Topic-based conversations
- [x] Proposals with A/B options + confidence
- [x] Step tracking + progress
- [x] CV Generator (7 fund configs)
- [x] WebSocket real-time updates
- [x] Folder sidebar (Finder-style, drag & drop)
- [x] New Topic creation
- [x] File upload + Reference management
- [x] Correction Engine (29 rules, 5 categories)
- [x] Quality Standards (18 standards, per output-type)
- [x] Trust per Skill (9 skills, color-coded bars)
- [x] Pre-Flight Check API
- [x] Event/Audit Log
- [x] Quality Gate Checklist

## Phase 1: Correction Propagation (v0.8) — IN PROGRESS
- [x] Corrections table + API (CRUD)
- [x] Import from corrections.md (29 rules)
- [x] Quality Standards table + API
- [x] Trust per Skill table + API
- [x] Pre-Flight Check endpoint
- [x] Frontend: Corrections in Context Panel
- [x] Frontend: Trust Bars in Sidebar
- [x] Frontend: Pre-Flight Badge
- [ ] AI-powered Pre-Flight (check output text against corrections)
- [ ] Correction auto-creation from chat ("Correction: X → Y")
- [ ] Violation tracking with Trust impact
- [ ] Regression Detection (score vs baseline)

## Phase 2: OpenClaw Integration (v0.9) — NEXT
*Target: Platform becomes usable for real work*
- [ ] Action Layer abstraction (interface for AI backend)
- [ ] `sessions_send` integration (Klick → Mia response)
- [ ] Streaming responses (token-by-token via WebSocket)
- [ ] Guardrails system (🟢 Auto / 🟡 Review / 🔴 Confirm)
- [ ] Delegative Actions: [Generate CV] [Send Email] [Publish]
- [ ] `gog gmail send` via platform
- [ ] Real-time Mia status (thinking/typing indicator)
- [ ] Offline graceful degradation ("Mia offline" banner)
- [ ] Request queue (actions queued while offline)

## Phase 3: UX Polish (v0.9.x)
*Target: Speed + Professional feel*
- [ ] Command Palette (Cmd+K) — fuzzy search topics, folders, actions
- [ ] Keyboard Shortcuts (J/K nav, S state, D done, Space open, E edit)
- [ ] Optimistic UI (<100ms feedback on every click)
- [ ] Artifact Panel (live document editing alongside chat)
- [ ] Focus Mode (WORKING state → fullscreen, sidebar minimized)
- [ ] Dark/Light theme toggle
- [ ] Drag & Drop folder reordering
- [ ] Topic search/filter

## Phase 4: Learning Engine (v1.0)
*Target: Platform improves with every interaction*
- [ ] Correction Propagation: 1 fix → class rule → all future outputs
- [ ] Pattern Recognition: "VC Email sent" → auto follow-up task
- [ ] Preference Memory per Scope (VC=formal, Content=narrative)
- [ ] Auto-Workflow creation (confirmed patterns → permanent)
- [ ] Regression Detection (output score vs baseline, auto-fix)
- [ ] Template Extraction ("Is this the new standard for X?")
- [ ] Daily Eval (10 questions, multi-select, pattern analysis)

## Phase 5: Dependency Graph & Agent Teams (post v1.0)
*Target: Visual Process Intelligence*
- [ ] Force-directed graph (D3.js/Canvas) showing topic dependencies
- [ ] Node states: open/blocked/in-progress/done with color coding
- [ ] Agent assignment per node (Mia, Sub-Agents, Florian)
- [ ] A/B testing: parallel agent runs on same task, compare outputs
- [ ] Celonis-style process mining on execution data (time-to-complete, bottleneck detection)
- [ ] Obsidian-style zoom/filter (by stage, folder, agent, state)
- [ ] Click node → open topic. Drag to reassign.
- [ ] Makes sense at 50+ nodes with real execution data

## Phase 6: Infrastructure (post v1.0)
- [ ] Auto-Start via launchctl (macOS Launch Agent)
- [ ] Remote deployment option (Auth, HTTPS, DB migration)
- [ ] Mobile-responsive layout
- [ ] Export/Import (topics, corrections, preferences)
- [ ] API documentation (auto-generated from FastAPI /docs)
- [ ] Dependency Graph visualization
- [ ] Smart Folders (auto-populated: Today, Overdue, Blocked)
- [ ] Notification system (desktop notifications for completed actions)

---

## Milestones

| Milestone | Version | Target | Criteria |
|-----------|---------|--------|----------|
| **Usable** | v0.9 | Feb 20 | Live AI responses, real actions via platform |
| **v1.0 Release** | v1.0 | Feb 23 | 5 VC emails sent, trust system live, zero critical bugs |
| **Self-Improving** | v1.1 | Feb 28 | Correction propagation + pattern recognition active |
| **Production** | v2.0 | Mar 15 | Remote deployment, mobile, multi-user ready |

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Scope creep (features > shipping) | High | High | Strict phase gates, "done" = 5 emails sent |
| OpenClaw API latency (>3s responses) | Medium | Medium | Optimistic UI, streaming, request queue |
| Disk space (14GB sqlite) | Medium | High | Embedding purge scheduled, Drive backup |
| Data loss during dev | High | Low | SQLite WAL, daily backups, Git for code |
| Platform replaces sending (build > send) | High | Medium | D-157: Build only if Build → Send → Revenue |

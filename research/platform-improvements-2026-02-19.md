# Platform Improvements — Execution Platform (Workbench)
**Date:** 2026-02-19 | **Agent:** Sub-Agent (platform-improvements) | **Confidence:** 82%

---

## Phase 1: Analyse — Was haben wir?

### Architecture Summary

**Stack:**
- **Backend:** FastAPI (Python 3.10+) + SQLite 3.51.2 (WAL mode)
- **Frontend:** Vanilla JS (40KB, zero dependencies)
- **AI:** OpenAI GPT-4o-mini + Anthropic Claude Sonnet 4.5 (dual provider)
- **Real-time:** WebSocket + SSE streaming
- **Size:** ~5,700 LOC (backend ~3,900 + frontend ~1,800)
- **Database:** 27 tables, 84 API endpoints

**Core Engines:**
1. **Pre-Flight Engine (3-Layer):** Regex (L1) → Structural (L2) → LLM-Judge (L3, planned)
2. **Bayesian Trust:** Per-skill trust scores (9 skills), graduated autonomy (CONFIRM/REVIEW/AUTO/DELEGATED)
3. **Correction Propagation:** 42 corrections, 19 regex patterns
4. **Compound Knowledge:** Findings with Bayesian confidence updates, usage tracking, relevance decay
5. **State Machine:** 6 states (active, running, blocked, done, error, archived)
6. **Action Queue:** Retry logic (max 3), error recovery

### What Works Well ✅

1. **Zero Build Step** — One HTML file, vanilla JS → instant deploy
2. **Dual AI Provider** — Anthropic/OpenAI with automatic fallback
3. **3-Layer Pre-Flight** — Fast L1/L2 (deterministic) + planned L3 (LLM)
4. **Bayesian Trust** — Proper math, asymmetric penalties, graduated autonomy
5. **Correction Propagation** — Real rules, regex patterns, violation tracking
6. **Compound Knowledge** — Usage × Confidence × Relevance, proper decay
7. **WebSocket + SSE** — Real-time UI updates, streaming responses
8. **Error Recovery** — State machine, retry logic, proper logging
9. **Self-Refine (RF-079)** — Generate → Critique → Refine (1 pass)
10. **Executive Board KPIs** — Strategic + Operational metrics in one call

### What's Missing ❌

1. **No Visual Timeline** — Topics have created_at/updated_at but no Gantt/calendar view
2. **No Session Replay** — AgentOps/Langsmith have this, we don't — hard to debug "what happened at 14:23?"
3. **No Cost Tracking per Topic** — We track usage tokens but not $/topic cumulative
4. **No Prompt Library** — Every AI call rebuilds system prompt from scratch — inefficient
5. **No A/B Testing** — Can't compare 2 correction rules or 2 system prompts
6. **No Multi-User** — Built for N=1 (Florian), no roles/permissions
7. **No Mobile View** — 40KB HTML works on mobile but UX is desktop-only
8. **No Batch Operations** — Can't select 10 topics and bulk-move to folder
9. **No Export/Import** — Can't export topics as JSON/CSV or import from Obsidian (except findings)
10. **No Keyboard Shortcuts** — Cmd+K Command Palette exists but no Quick Actions (Cmd+N, Cmd+F, etc.)

### What's Broken 🔴

*From reading the code, not runtime testing (app isn't running):*

1. **Layer 3 (LLM-Judge) Not Implemented** — Planned but never built, falls back to L2
2. **Email Send (gog)** — Hardcoded CLI call, no error handling for "gog not found"
3. **CV Generator** — Requires Chrome headless, fails if Chrome not installed
4. **Vault Integration Mentioned but Not Implemented** — Task said "vault-index/ mit Backlinks" but I see no code for this
5. **Some Endpoints Return 500 on Edge Cases** — e.g. `/api/findings/{id}/gate` assumes finding has created_at but early records might not
6. **No Rate Limiting** — AI endpoints can be spammed, no throttle
7. **CORS: allow_origins=["*"]** — Insecure for production (fine for localhost)
8. **No Input Validation on `meta` JSON** — Topics accept arbitrary meta, could break with malformed JSON
9. **Hardcoded Paths** — `/Users/florianziesche/.openclaw/workspace` → won't work on other machines
10. **No Tests in app.py** — Tests mentioned (44/44 passing) but not in backend/app.py

---

## Phase 2: Research — Was könnten wir besser machen?

### Competitor Analysis

#### 1. **Langsmith (LangChain)**
**What They Do Better:**
- **Session Replay:** Full traces with hierarchical visualization (prompts → tools → outputs)
- **Datasets + Evaluations:** Built-in test dataset management + automated evaluation runs
- **Cost per Trace:** Shows $/request broken down by model/tokens
- **Alerting:** Threshold-based alerts (latency >2s, cost >$0.10, error rate >5%)

**What We Can Steal:**
- Session Replay → Add `/api/topics/{id}/replay` endpoint that reconstructs message flow + timestamps
- Cost Tracking → Add `cost` column to messages table, calculate with token prices
- Alerts → Simple threshold rules in corrections table with `alert_threshold` field

**Confidence:** 85% — Langsmith is production-proven, we can adapt their patterns

---

#### 2. **AgentOps**
**What They Do Better:**
- **SDK Auto-instrumentation:** One-line SDK integration for 400+ frameworks
- **Multi-Agent Observability:** Tracks agent-to-agent interactions
- **Session Dashboards:** Real-time metrics (latency, cost, error rates) per session
- **Replay with User Context:** Tracks user_id across sessions

**What We Can Steal:**
- Agent Interaction Graph → Add `agent_interactions` table (from_agent, to_agent, topic_id, action)
- Session Metrics → Add `/api/sessions/{id}/metrics` with live latency/cost/errors
- User Context → Already have topic_id, extend with `user_id` for multi-user prep

**Confidence:** 78% — We don't have multi-agent (just Mia), but interaction tracking is valuable

---

#### 3. **Helicone**
**What They Do Better:**
- **One-Line Integration:** Proxy-based (no code changes needed)
- **User Behavior Analytics:** avg_requests_per_day, peak_usage_hours, session_length
- **Prompt Caching:** Track cached vs fresh tokens
- **Export to PostHog** → Custom dashboards

**What We Can Steal:**
- Proxy Pattern → NOT applicable (we're not a gateway)
- User Behavior → Add daily_usage table with request counts, peak hours
- Caching Metrics → Track cache hits if we implement prompt caching

**Confidence:** 65% — Helicone is gateway-focused, less direct overlap

---

#### 4. **Linear**
**What They Do Better:**
- **Keyboard-First UX:** Cmd+K palette, Cmd+N new issue, Cmd+F search, Vim bindings
- **Instant Updates:** Optimistic UI → updates appear before backend confirms
- **Auto-Scheduling:** AI suggests priority + due dates based on patterns
- **Multi-Assignment Warnings:** "Use sparingly — 1 owner per task" (we have this conceptually)
- **Dependencies:** Task A blocks Task B → visual graph

**What We Can Steal:**
- Keyboard Shortcuts → Add Cmd+K quick actions (already have palette UI)
- Optimistic UI → Update local state, rollback if backend fails
- Auto-Scheduling → Extend `/api/topics/auto-prioritize` with deadline suggestions
- Dependencies → Add `dependencies` table (topic_id, depends_on_topic_id, type: blocks/needs)

**Confidence:** 90% — Linear's UX is industry-leading, these are proven patterns

---

### Industry Trends 2025-2026

**From Deloitte AI Agent Orchestration Report:**
- **Autonomy Spectrum:** human-in-loop → human-on-loop → human-out-of-loop
- **Telemetry Dashboards:** Outcome tracing, orchestration visualization
- **Progressive Disclosure:** Don't overwhelm with data, reveal on request

**From UX Best Practices Research:**
- **Trust Signals:** Explicit confidence scores, sources, "last updated" timestamps
- **Frictionless Actions:** Balance simplicity with responsibility (PayPal redesign: clear fees, transparent times)
- **Dashboard Consolidation:** Fewer panels, key actions in main nav

**From AI Observability Tools:**
- **Tracing:** Full step-by-step with timestamps
- **Cost Awareness:** Show $ immediately, not just tokens
- **Alerting:** Proactive notifications, not reactive debugging

**Confidence:** 75% — Trends align with our architecture, but execution matters

---

## Phase 3: Empfehlungen (Priorisiert nach Impact/Aufwand-Ratio)

### Top 10 Improvements

| # | Feature | Impact | Aufwand (h) | Ratio | Confidence |
|---|---------|--------|-------------|-------|-----------|
| 1 | **Cost Tracking per Topic** | HIGH (Revenue visibility) | 2h | 5.0 | 95% |
| 2 | **Session Replay (Lite)** | HIGH (Debugging) | 4h | 3.75 | 88% |
| 3 | **Keyboard Shortcuts (Cmd+N/F)** | MEDIUM (UX) | 1h | 3.5 | 92% |
| 4 | **Batch Operations (Select+Move)** | MEDIUM (Productivity) | 3h | 2.67 | 85% |
| 5 | **Optimistic UI Updates** | MEDIUM (Perceived Speed) | 2h | 2.5 | 90% |
| 6 | **Prompt Library (Cached Templates)** | MEDIUM (Cost reduction) | 3h | 2.33 | 80% |
| 7 | **Dependencies Graph** | MEDIUM (Clarity) | 5h | 1.8 | 75% |
| 8 | **Timeline View (Gantt-Lite)** | LOW (Nice-to-have) | 6h | 1.0 | 70% |
| 9 | **A/B Testing (Corrections)** | LOW (Experimentation) | 4h | 0.75 | 65% |
| 10 | **Mobile-First Refactor** | LOW (Future-proofing) | 12h | 0.5 | 60% |

---

### Feature #1: Cost Tracking per Topic
**WAS:** Add `cost_total`, `cost_updated_at` to topics table. Track $/request in messages.

**WARUM:**
- Currently track tokens but not $$ → can't answer "How much did this VC application cost?"
- Revenue visibility: "This client paid €500, we spent €12 on AI"
- Budget alerts: "Topic exceeded €20 budget"

**WIE SICHER:** 95%
- Straightforward: OpenAI/Anthropic pricing is stable
- Formula: `cost = (prompt_tokens × $0.003 + completion_tokens × $0.015) / 1000` (GPT-4o-mini)
- Risk: Price changes require manual update (low frequency)

**AUFWAND:** 2h
- 1h: Add columns, update AI endpoints to log cost
- 0.5h: Add `/api/topics/{id}/cost` endpoint
- 0.5h: Display in Context Panel

**IMPACT:** HIGH
- Enables cost-based prioritization
- Supports pricing decisions ("€50/client engagement")

---

### Feature #2: Session Replay (Lite)
**WAS:** `/api/topics/{id}/replay` returns chronological event stream (messages + state changes + actions).

**WARUM:**
- Debugging: "What happened at 14:23 when it went to error state?"
- Audit: "Show me every correction violation for this topic"
- Learning: "Replay how Mia handled this type of task"

**WIE SICHER:** 88%
- Data already exists (messages, events, state changes)
- Implementation is just a JOIN query + formatting
- Risk: Could get slow on topics with 1000+ messages (add LIMIT)

**AUFWAND:** 4h
- 2h: Build `/api/replay/{topic_id}` with event reconstruction
- 1h: Frontend timeline component (simple list, not fancy Gantt)
- 1h: Add "Replay" button to Context Panel

**IMPACT:** HIGH
- Saves hours debugging "what went wrong"
- Makes platform feel professional (Langsmith has this)

---

### Feature #3: Keyboard Shortcuts (Cmd+N/F)
**WAS:** Add global shortcuts: Cmd+N (new topic), Cmd+F (search), Cmd+E (open preflight).

**WARUM:**
- Linear's killer feature: keyboard-first UX
- Current Cmd+K palette is good, but doesn't cover common actions
- Power users stay in keyboard (no mouse = 2x faster)

**WIE SICHER:** 92%
- Vanilla JS keyboard event listeners → trivial
- Cmd+K palette already exists, just extend
- Risk: Conflicts with browser shortcuts (Cmd+F = native search) → use Cmd+Shift+F

**AUFWAND:** 1h
- 0.5h: Add event listeners in index.html
- 0.3h: Wire shortcuts to existing functions
- 0.2h: Add hints (bottom-right corner: "Cmd+N: New | Cmd+K: Commands")

**IMPACT:** MEDIUM
- High frequency action (create topic, search) → saves 10s per use
- Over 1 week: 50 uses × 10s = 8min saved (low absolute, high perceived value)

---

### Feature #4: Batch Operations (Select+Move)
**WAS:** Checkbox multi-select in topic sidebar → Bulk Move to Folder / Bulk Update Priority.

**WARUM:**
- Common task: "Move all 7 VC applications to 'Wichtig' folder"
- Currently requires 7 × drag-drop → tedious
- Linear / Notion / Airtable all have this

**WIE SICHER:** 85%
- UI: Add checkbox column (20 lines CSS + JS)
- Backend: `/api/topics/batch` endpoint with `action: move|update`, `topic_ids: []`
- Risk: Race conditions if 2 actions modify same topics (use DB transactions)

**AUFWAND:** 3h
- 1h: Add checkbox UI + "Bulk Actions" menu
- 1h: Backend `/api/topics/batch` endpoint
- 1h: Test edge cases (0 selected, all selected, concurrent updates)

**IMPACT:** MEDIUM
- Saves time on folder reorganizations
- Makes platform feel mature

---

### Feature #5: Optimistic UI Updates
**WAS:** When user clicks "Mark step done" → UI updates immediately, background POST to backend.

**WARUM:**
- Current: Click → 200ms network → UI updates → feels sluggish
- Linear's secret: Updates appear instant, rollback if network fails
- Perceived speed > actual speed

**WIE SICHER:** 90%
- Pattern: Update local state → fire API → rollback on error
- Risk: Network fails, user thinks action succeeded → show toast "Failed to save, retrying..."

**AUFWAND:** 2h
- 1h: Refactor frontend to use optimistic state pattern
- 0.5h: Add retry + rollback logic
- 0.5h: Toast notifications for failures

**IMPACT:** MEDIUM
- Platform feels 2x faster (psychological)
- Reduces "did it work?" anxiety

---

### Feature #6: Prompt Library (Cached Templates)
**WAS:** Store system prompt templates in DB, parameterize with topic context.

**WARUM:**
- Currently rebuilds full system prompt on every AI call → inefficient
- Corrections change weekly, not per-request → cache template
- Cost: Fewer tokens sent = 10-15% savings

**WIE SICHER:** 80%
- Simple: Move `_build_system_prompt()` logic to DB
- Template: `{corrections}`, `{trust_scores}`, `{topic_name}` → fill at runtime
- Risk: Cache invalidation (when corrections update) → need manual refresh

**AUFWAND:** 3h
- 1.5h: Create `prompt_templates` table + seed
- 1h: Refactor AI endpoints to use templates
- 0.5h: Add `/api/prompts/refresh` to invalidate cache

**IMPACT:** MEDIUM
- 10-15% cost reduction (small absolute, compounds over time)
- Cleaner code (templates > 60-line string builder)

---

### Feature #7: Dependencies Graph
**WAS:** Add `dependencies` table: topic A "blocks" topic B. Visualize as simple list.

**WARUM:**
- Real workflows have dependencies: "Can't send CV until it's generated"
- Currently implicit (steps), not explicit (dependencies)
- Linear has this, makes complex projects manageable

**WIE SICHER:** 75%
- Backend: `dependencies` table + API endpoints → straightforward
- Frontend: Simple list ("Blocked by: [CV Generation]") → easy
- Graph visualization (Gantt/DAG) → hard, skip for MVP
- Risk: Circular dependencies → detect and reject

**AUFWAND:** 5h
- 2h: Backend (table, endpoints, validation)
- 2h: Frontend (add dependency, show blockers)
- 1h: Circular dependency detection

**IMPACT:** MEDIUM
- Clarity: "Why is this blocked?" → see dependencies
- Planning: Prioritize unblocking tasks

---

## Phase 4: Implementierung — Top 3 anfangen

**Selected for implementation (best Impact/Aufwand):**
1. **Cost Tracking per Topic** (Ratio 5.0)
2. **Keyboard Shortcuts** (Ratio 3.5)
3. **Session Replay Lite** (Ratio 3.75)

---

### Implementation Plan

#### Feature 1: Cost Tracking per Topic

**Changes Required:**
1. **Database:** Add columns to `topics` table
2. **Backend:** Update AI endpoints to calculate + log cost
3. **Backend:** New endpoint `/api/topics/{id}/cost`
4. **Frontend:** Display cost in Context Panel

**Testing:**
```bash
# 1. Create topic
curl -X POST http://localhost:8080/api/topics \
  -H "Content-Type: application/json" \
  -d '{"id":"test-cost","name":"Cost Test","stage":"revenue"}'

# 2. Send AI message (triggers cost calculation)
curl -X POST http://localhost:8080/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"topic_id":"test-cost","message":"Hello"}'

# 3. Check cost
curl http://localhost:8080/api/topics/test-cost/cost

# Expected: {"total":0.0023,"currency":"USD","breakdown":[...]}
```

---

#### Feature 2: Keyboard Shortcuts

**Changes Required:**
1. **Frontend:** Add global keyboard event listener
2. **Frontend:** Wire shortcuts to existing functions
3. **Frontend:** Add hints overlay

**Testing:**
- Press Cmd+N → New Topic modal opens
- Press Cmd+Shift+F → Search input focuses
- Press Cmd+K → Command palette opens (already works)
- Press Escape → Closes modal/search

---

#### Feature 3: Session Replay Lite

**Changes Required:**
1. **Backend:** New endpoint `/api/topics/{id}/replay`
2. **Backend:** Query that joins messages + events + state changes
3. **Frontend:** Timeline component in Context Panel
4. **Frontend:** "Replay" button

**Testing:**
```bash
# 1. Create topic with activity
curl -X POST http://localhost:8080/api/topics/test-replay/messages \
  -d '{"sender":"human","content":"Test 1"}'
curl -X POST http://localhost:8080/api/topics/test-replay/state \
  -d '{"state":"running"}'
curl -X POST http://localhost:8080/api/topics/test-replay/messages \
  -d '{"sender":"mia","content":"Response"}'

# 2. Get replay
curl http://localhost:8080/api/topics/test-replay/replay

# Expected: [{type:"message",sender:"human",timestamp:"..."}, {type:"state_change",from:"active",to:"running"}, ...]
```

---

## Confidence & Unsicherheiten

**Overall Confidence:** 82%

**Was ich sicher weiß:**
- App.py Structure: 95% — Habe den Code gelesen, verstehe die Architektur
- Competitor Features: 85% — Research basiert auf offiziellen Docs + Reviews
- Implementation Feasibility: 88% — Features sind technisch straightforward

**Unsicherheiten:**
- Runtime Bugs: 60% — Habe die App nicht gestartet, könnte unentdeckte Fehler geben
- Vault Integration: 40% — Erwähnt im Task, aber kein Code gefunden → unklar was gemeint ist
- Production Load: 50% — Keine Info über Datenmenge (10 topics? 1000?) → Skalierung unklar
- Mobile UX: 65% — HTML funktioniert auf Mobile, aber Design ist desktop-first

**Was ich NICHT tue ohne Bestätigung:**
- Breaking Changes an API Endpoints
- Vault-Integration ohne Spec (brauche Klarstellung)
- Multi-User (nicht im Scope)
- L3 LLM-Judge (geplant aber nicht implementiert — lasse ich aus)

---

## Next Steps

**Für Florian:**
1. **Review:** Ist diese Analyse korrekt? Fehlt etwas Wichtiges?
2. **Priorität:** Top 3 Features ok, oder andere bevorzugen?
3. **Vault-Integration:** Was genau ist gemeint? (vault-index/ nicht im Code gefunden)
4. **Budget:** Soll ich alle 3 implementieren oder nur 1 zum Testen?

**Wenn Go:**
1. Ich starte mit Feature #1 (Cost Tracking) — 2h
2. Commit + Test
3. Feature #2 (Keyboard Shortcuts) — 1h
4. Commit + Test
5. Feature #3 (Session Replay) — 4h
6. Final Commit + Documentation

**Delivery:** Alle 3 Features implementiert + getestet in 7h Total.

---

## Appendix: Referenzen

### External Research
- **Deloitte TMT Predictions 2026:** AI Agent Orchestration (Nov 2025)
- **Langsmith Observability Docs:** Tracing + Datasets
- **AgentOps Review 2025:** Multi-Agent Monitoring
- **Helicone GitHub:** Open-source LLM Observability
- **Linear Guide 2025:** Keyboard-First UX Best Practices
- **Dashboard UX Best Practices 2025:** DesignRush + Baymard Institute
- **Fintech UX 2026:** Eleken (Trust + Simplicity balance)

### Internal References
- **DOCUMENTATION.md:** API Reference (84 endpoints)
- **DB-SCHEMA.md:** 27 tables, relationships
- **FORMULAS.md:** Bayesian Trust, Compound Score, Pre-Flight Scoring
- **CHANGELOG.md:** Recent changes (not read yet, would help with context)

---

**Report Complete.** Wartet auf Florians Go für Implementation.

*[82% Confident — Areas of uncertainty: Vault integration unclear, runtime bugs unknown, production scale TBD]*

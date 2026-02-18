# Execution Platform — Architecture Spec v1
*Created: 2026-02-18 09:30 CET*
*Source: Florian-Mia Conversation 09:12-09:30*

## Vision
UI-Layer zwischen Florian und Mia. Bindeglied für effektive Execution.
Nicht ein Dashboard. Ein lebendes System das mit jeder Interaktion besser wird.

## Core Principles
- P1: Platform = Execution Bridge (Florian ↔ Mia)
- P2: Jede Interaktion verbessert den Output
- P3: Trust ist granular, pro Skill, earned through data
- P4: Transparenz > Autonomie (Blocker sichtbar, Entscheidungen nachvollziehbar)
- P5: Speed matters (Linear-Prinzip: <100ms Feedback)

---

## Requirements (aus Konversation ab 09:12)

### R-001: Ordner-Sidebar (Finder-Style)
- Status: ✅ DONE (v0.7.0)
- Drag & Drop Topics in Ordner
- Verschachtelte Ordner (Hierarchisch)
- Collapse/Expand
- Neue Ordner erstellen, umbenennen, löschen

### R-002: Task States (aus Florians Perspektive)
- Status: 🔲 SPEC
- States: CAPTURED → THINKING → WORKING → BLOCKED → REVIEW → DONE → ARCHIVED
- Nur Florian bewegt Tasks zwischen States
- Mia kann vorschlagen, nie automatisch verschieben

### R-003: Dependency Graph (Task-Kommunikation)
- Status: 🔲 SPEC
- Trigger-Types: triggers / feeds / blocks / requires
- Auto-Propagation: Publish Substack → LinkedIn bekommt Link → Glasswing Blocker löst sich
- Connections-Tabelle existiert, braucht trigger_type + auto_action

### R-004: OpenClaw API Integration (Klick → Echte Aktion)
- Status: 🔲 SPEC
- Architektur: Workbench → POST /api/action → sessions_send → Mia → WebSocket → UI
- Guardrails: 🟢 Auto / 🟡 Review / 🔴 Confirm

### R-005: Live Conversation pro Topic
- Status: ⚠️ PARTIAL (Chat UI existiert, Responses = Keyword-Matching)
- Ziel: Echte AI-Responses via OpenClaw
- Feedback: Upvote/Downvote auf jeder Response

### R-006: Quality Gate im Context Panel
- Status: ✅ DONE (v0.7.0) — Static checklist + Corrections + Standards loaded
- Erweiterung: Auto-Check gegen corrections.md + patterns.md (Phase 1)

### R-007: Command Palette (Cmd+K)
- Status: 🔲 SPEC
- Fuzzy Search über Topics, Ordner, Aktionen
- Keyboard-Navigation (J/K/Enter/Esc)

### R-008: Keyboard Shortcuts
- Status: 🔲 SPEC
- J/K = nav, S = state change, D = done, Space = open, E = edit

### R-009: Artifact Panel (Live-Dokument)
- Status: 🔲 SPEC
- Cover Letter, CV, Email Draft sichtbar + editierbar rechts
- In-Place Editing mit Mia-Suggestions als Inline-Kommentare

### R-010: Correction Propagation
- Status: ⚙️ IN PROGRESS (v0.7.0: DB + API + Frontend done. AI-check + auto-creation pending)
- Jede Korrektur → Regel → Applied to alle offenen Tasks
- Checked gegen jeden neuen Output (Pre-Flight)
- Trust Impact: Violation = Trust -1

### R-011: Pre-Flight Quality Gate
- Status: 🔲 SPEC
- Automatisch vor jedem Output an Florian
- Checks: Quality Gate + Correction Rules + Brand Standards
- Score Threshold: Nur Output ≥ 75 zeigen
- Regression Detection: Vergleich gegen Baseline

### R-012: Trust System (Granular, Per Skill)
- Status: ⚙️ IN PROGRESS (v0.7.0: DB + API + Frontend bars done. Signal processing pending)
- Trust pro Skill (CV: 67, Research: 78, LinkedIn: 12)
- Trust → Autonomie-Level (🟢🟡🔴)
- Signale: Approve +2, Correct -1, Reject -3, Unverändert genutzt +3
- Sichtbar in Platform: Trust Bar pro Skill in Sidebar

### R-013: Pattern Recognition → Auto-Workflow
- Status: 🔲 SPEC
- "VC Email gesendet" → auto Follow-Up in 5 Tagen
- Patterns aus Verhalten lernen, Florian bestätigt einmal → gilt immer

### R-014: Preference Memory per Scope
- Status: 🔲 SPEC
- VC Folder: formeller Ton, bestimmte Struktur
- Content Folder: narrative, persönlich
- Gelernt aus Upvotes/Downvotes + Korrekturen

### R-015: Feedback Loop (Output-Verbesserung)
- Status: 🔲 SPEC
- Closed Loop: Output → Feedback → Regel → Besserer Output
- Standards automatisch aktualisiert
- Template-Extraktion: "Ist das der neue Standard für [X]?"

### R-016: Smart Folders (Auto-Population)
- Status: 🔲 SPEC
- "Heute" zeigt: manuell + Deadline heute + Blocker gelöst
- Topics können in mehreren Scopes sein

### R-017: Optimistic UI (<100ms)
- Status: 🔲 SPEC
- Jeder Klick = sofortiges visuelles Feedback
- Aktion läuft async, Undo-Option

### R-018: Event/Audit Log
- Status: ✅ DONE (v0.7.0) — Events table, API, Context Panel display
- Jede State-Änderung, Aktion, Korrektur geloggt
- Timeline pro Topic sichtbar
- Revertierbar wie Git

### R-019: Delegative Actions (1-Klick)
- Status: 🔲 SPEC
- [Generate CV] [Send Email] [Publish] als Buttons
- Guardrail-Level bestimmt ob auto oder review

### R-020: Fokus-Modus
- Status: 🔲 SPEC
- Task auf WORKING → Fullscreen, Sidebar minimiert
- Nur relevanter Kontext sichtbar

---

## Architecture

### Frontend
- Single HTML + Vanilla JS (kein Framework — Speed)
- WebSocket für Live-Updates
- LocalStorage für Folder-States, Preferences
- CSS: Design System von ainaryventures.com (Inter, #0a0a0a, #d4a853)

### Backend
- FastAPI + SQLite (workbench.db)
- OpenClaw Integration via sessions_send / sessions_spawn
- WebSocket Hub für Real-Time Updates

### Data Model (erweitert)
```
folders:     id, name, parent_id, position, color, icon, collapsed, smart_filter
topics:      id, name, stage, folder_id, folder_position, state, progress, meta
steps:       id, topic_id, label, done, position
messages:    id, topic_id, sender, content, msg_type, meta
proposals:   id, message_id, type, content, confidence, options, chosen, votes
connections: id, from_topic, to_topic, relation, trigger_type, auto_action
documents:   id, topic_id, name, path, url, doc_type, kind
corrections: id, rule, source_topic, created_at, violation_count, last_checked
trust:       agent, skill, score, total, up, down, updated_at
events:      id, topic_id, event_type, detail, created_at
preferences: id, scope, key, value, confidence, data_points
```

### State Machine
```
CAPTURED ──→ THINKING ──→ WORKING ──→ REVIEW ──→ DONE ──→ ARCHIVED
    │            │            │          │         │
    └────────────┴────────────┴──→ BLOCKED ←──────┘
                                     │
                                     └──→ (zurück zu vorherigem State)
```

---

## Build Phases

### Phase 0: Spec Review (JETZT)
- [ ] Florian beantwortet 5 Fragen
- [ ] Spec finalisiert
- [ ] "Done" Definition für v1

### Phase 1: Correction Propagation (ERSTER BUILD)
- [x] corrections table + API
- [x] Import existing corrections.md (29 rules)
- [x] Quality Standards table + API (18 standards)
- [x] Pre-Flight Check API
- [x] Trust per Skill table + API (9 skills)
- [x] Frontend: Corrections in Context Panel
- [x] Frontend: Trust Bars in Sidebar
- [x] Frontend: Pre-Flight Badge
- [x] New Topic creation (modal)
- [x] File Upload + Reference management
- [ ] AI-powered Pre-Flight (check text against corrections)
- [ ] Output Scoring Baseline
- [ ] Correction auto-creation from chat

### Phase 2: OpenClaw Integration
- [ ] sessions_send Endpoint in Backend
- [ ] Klick → echte AI-Response
- [ ] Guardrails (🟢🟡🔴)
- [ ] Delegative Actions (Generate CV, Send Email)

### Phase 3: UX Polish
- [ ] Command Palette (Cmd+K)
- [ ] Keyboard Shortcuts
- [ ] Optimistic UI
- [ ] Artifact Panel

### Phase 4: Learning Engine
- [ ] Pattern Recognition
- [ ] Preference Memory per Scope
- [ ] Auto-Workflow Creation
- [ ] Regression Detection

---

## Decisions (beantwortet 2026-02-18 09:35)
1. **Hosting:** Localhost + Auto-Start (launchctl). Remote = Phase 2 wenn nötig.
2. **Offline:** Grundfunktionen ohne Mia (Navigation, Docs, Organisation). AI + Actions brauchen Mia-Verbindung. Graceful Degradation.
3. **Feedback:** Detailliert — Pro Abschnitt/Claim markieren was gut/schlecht ist.
4. **Primary Interface:** Ja — Platform wird primärer Kanal. Telegram für Quick Messages.
5. **Done v1:** Fehlerfrei, Live AI, Core Features (Ordner, States, Dependencies), Hierarchisches Wissen aktiv, Trust per Skill live, Detailliertes Feedback. PROOF: 5 VC Emails durch Platform gesendet.

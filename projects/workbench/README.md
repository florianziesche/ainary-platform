# Ainary Execution Platform

**Version:** 0.13.0  
**Status:** Active Development (Phase C Complete)  
**Maintainer:** Florian Ziesche + Mia (AI Co-Founder)  
**Last Updated:** 2026-02-19

---

## Was ist die Execution Platform?

Die Execution Platform ist das **Bindeglied zwischen Florian und Mia** — ein lokales Web-Interface für die Zusammenarbeit zwischen Mensch und AI mit Transparenz, Trust und Feedback-Loops.

Sie ist das primäre Arbeitsinstrument für alle Tasks: VC-Bewerbungen, Consulting, Content, Research, Admin. Jeder Task ist ein "Topic" mit eigenem Kontext, Dokumenten, Fortschritt und Konversationshistorie.

### Kernprinzip

```
Florian entscheidet. Mia führt aus. Die Platform macht beides sichtbar.
```

Jede AI-Aktion hat einen Trust-Score. Jede Korrektur wird zur permanenten Regel. Jedes Ergebnis wird gegen Standards geprüft, bevor Florian es sieht. Das System wird mit jeder Interaktion besser — nicht durch Training, sondern durch akkumulierte Regeln und Feedback.

---

## What the Platform IS

| Property | Description |
|----------|-------------|
| **Execution Interface** | Where work happens — not just planned or discussed |
| **Trust System** | Granular trust per skill (Research: 70, Email: 30, Financial: 5). Determines autonomy level. |
| **Correction Engine** | Every correction becomes a class-wide rule. "No LLM phrases" applies to ALL future outputs. |
| **Quality Gate** | Pre-flight checks against 29 corrections + 18 standards before every result |
| **Context Hub** | All info for a task in one place: documents, references, corrections, connected topics |
| **Audit Trail** | Every action logged. What was decided when, by whom, and why. |
| **Single-User, Localhost** | Runs on Florian's MacBook. No cloud, no login, no overhead. |
| **Offline-Capable** | Navigation and context work without AI connection. Actions require Mia. |
| **Cost Tracking** | Per-topic AI spend with message-level detail. Track burn rate against $10/month target. |
| **Session Replay** | Full timeline reconstruction: messages + events + state changes in chronological order. |

## What the Platform is NOT

| Not | Why Not |
|-----|---------|
| **Not a Chat Replacement** | Telegram for quick messages. Platform for structured work. |
| **Not Project Management** | No Gantt charts, sprints, or team features. One human, one AI. |
| **Not a Dashboard** | Dashboards show data. Platform executes work and changes the real world (sends emails, generates CVs, creates documents). |
| **Not an AI Playground** | No free prompting. Every interaction has task context, is checked, and stored. |
| **Not a SaaS Product** | Localhost, single-user. No multi-tenancy, billing, or onboarding. |
| **Not a Replacement for Thinking** | Florian makes all irreversible decisions. Platform recommends, Florian decides. |
| **Not a Build Excuse** | Build is only good if Build → Send → Revenue. Platform development is means, not end. (D-157) |

---

## Zweck

### Primäres Ziel
**Florians Output-Qualität und -Geschwindigkeit steigern**, indem:
1. Jede Korrektur dauerhaft wird (nie zweimal denselben Fehler)
2. Kontext automatisch geladen wird (nie "was war nochmal bei Glasswing?")
3. Vertrauen messbar ist (nicht "ich glaube Mia kann das")
4. Aktionen ein-Klick sind (nicht "schreib mir eine Email an...")

### Sekundäres Ziel
**Nachweis, dass Human-AI-Collaboration mit Feedback-Loops funktioniert.** Die Platform ist gleichzeitig ein Proof-of-Concept für Florians VC-Thesis: AI-Agenten brauchen Trust-Systeme, Correction Propagation und Quality Gates.

### Metriken
| Metrik | Ziel | Messung |
|--------|------|---------|
| Sends pro Woche | ≥10 | Events mit type="send" |
| Korrekturen pro Woche | Sinkend | violation_count Trend |
| Trust-Score Durchschnitt | Steigend | AVG(trust_skills.score) |
| Time-to-Send | <5 Min pro Email | Timestamps: Topic erstellt → Email gesendet |
| Pre-Flight Pass-Rate | >80% | preflight.pass / preflight.total |

---

## Architektur

### Übersicht

```
┌──────────────────────────────────────────────────────┐
│                  FLORIAN (Browser)                    │
│               http://localhost:8080                   │
└─────────────┬────────────────────────▲───────────────┘
              │                        │
              │  REST API + WebSocket  │  HTML + JSON
              │                        │
┌─────────────▼────────────────────────┴───────────────┐
│              FRONTEND (index.html)                    │
│                                                       │
│  ┌─────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ Sidebar │  │  Main Area   │  │ Context Panel  │  │
│  │         │  │              │  │                │  │
│  │ Pipeline│  │ Conversation │  │ Documents      │  │
│  │ Folders │  │ Proposals    │  │ References     │  │
│  │ Topics  │  │ Steps        │  │ Quality Gate   │  │
│  │ Trust   │  │ Actions      │  │ Corrections    │  │
│  │         │  │              │  │ Events         │  │
│  └─────────┘  └──────────────┘  └────────────────┘  │
│                                                       │
│  Vanilla JS · No Framework · Single File · <100ms    │
└─────────────┬────────────────────────▲───────────────┘
              │                        │
┌─────────────▼────────────────────────┴───────────────┐
│             BACKEND (FastAPI + SQLite)                │
│                                                       │
│  ┌─────────────────────────────────────────────┐     │
│  │              ACTION LAYER                    │     │
│  │  (Abstrahiert — Backend austauschbar)        │     │
│  │                                              │     │
│  │  ┌────────────┐  ┌──────────┐  ┌─────────┐ │     │
│  │  │  OpenClaw  │  │  Direct  │  │  Rules  │ │     │
│  │  │  (Mia)     │  │  API     │  │  Engine │ │     │
│  │  └────────────┘  └──────────┘  └─────────┘ │     │
│  └─────────────────────────────────────────────┘     │
│                                                       │
│  ┌─────────────────────────────────────────────┐     │
│  │              QUALITY LAYER                   │     │
│  │                                              │     │
│  │  Corrections ──→ Pre-Flight ──→ Scoring     │     │
│  │  Standards   ──→ Gate       ──→ Trust       │     │
│  │  Preferences ──→ Guardrails ──→ Events      │     │
│  └─────────────────────────────────────────────┘     │
│                                                       │
│  workbench.db (SQLite) · Port 8080 · CORS *          │
└──────────────────────────────────────────────────────┘
```

### Drei Schichten

**1. Frontend (index.html)**
Ein einzelnes HTML-File (~40KB) mit eingebettetem CSS und JavaScript. Kein Build-Step, kein Framework. Öffnet in jedem Browser. Ziel: jede Interaktion unter 100ms.

**2. Backend (app.py)**
FastAPI-Server mit SQLite-Datenbank. Startet mit `python3 app.py` auf Port 8080. Alle Daten in einer Datei (`workbench.db`). WebSocket für Live-Updates.

**3. Quality Layer**
Das Differenzierungsmerkmal. Zwischen User-Input und Output sitzt eine Schicht aus:
- **29 Korrekturen** (gelernt aus Fehlern)
- **18 Quality Standards** (pro Output-Typ)
- **9 Trust Skills** (mit messbaren Scores)
- **Pre-Flight Checks** (automatisch vor jedem Ergebnis)
- **Event Log** (vollständiger Audit Trail)

### Datenfluss einer typischen Aktion

```
1. Florian klickt "Email mit CV senden" bei Glasswing Ventures
2. Frontend → POST /api/topics/glasswing/messages
3. Backend prüft Trust-Score für "Email Drafts" (aktuell: 30)
   → Score < 50 → Guardrail: 🟡 REVIEW (Florian muss bestätigen)
4. Backend → OpenClaw sessions_send("Erstelle Email an Rudina Seseri...")
5. Mia generiert Draft
6. Quality Layer → Pre-Flight Check:
   - ✅ Keine LLM-Phrasen
   - ✅ Solo Founder Voice ('I' nicht 'We')
   - ⚠️ Keine fake Zahlen (unverified: "$120K AUM")
   - Pre-Flight Score: 85% → WARN
7. Ergebnis → Frontend mit Pre-Flight Badge
8. Florian reviewed, korrigiert "$120K AUM" → "$120K potential"
9. Korrektur wird gespeichert → Correction #30: "AUM-Zahlen verifizieren"
10. Trust "Email Drafts" +1 (weil 85% richtig war)
11. Florian klickt "Senden" → gog gmail send
12. Event geloggt: email_sent, Glasswing, 2026-02-18 10:15
```

### Technologie-Stack

| Komponente | Technologie | Begründung |
|------------|-------------|------------|
| Frontend | Vanilla JS + CSS | Kein Build-Step, single file, <100ms |
| Backend | Python FastAPI | Async, auto-validiert, schnell zu entwickeln |
| Datenbank | SQLite (WAL mode) | Zero-Config, single file, ausreichend für Single-User |
| Real-time | WebSocket | Native Browser-Support, low latency |
| AI Backend | OpenClaw (Mia) | Bereits laufend, Session-Management, Tools |
| CV Generation | Headless Chrome | PDF-Rendering mit exakter Design-Kontrolle |

### Dateien

```
projects/workbench/
├── README.md               ← Du bist hier
├── CHANGELOG.md            ← Versionierte Änderungen
├── ARCHITECTURE.md         ← Technische Referenz (ERD, API, Security)
├── ROADMAP.md              ← Phasen, Milestones, Risiken
├── PLATFORM-SPEC.md        ← 20 Requirements mit Status
├── index.html              ← Frontend
├── uploads/                ← Hochgeladene Dateien
│   └── {topic_id}/
└── backend/
    ├── app.py              ← Server
    ├── cv_generator.py     ← CV-Engine
    └── workbench.db        ← Datenbank
```

---

## Entscheidungen

| ID | Entscheidung | Begründung |
|----|-------------|------------|
| D-151 | Localhost + Auto-Start (launchctl) | Single-User, kein Cloud-Overhead. Remote = Phase 5. |
| D-152 | Offline-fähige Navigation | Kontext muss immer zugänglich sein, auch ohne AI |
| D-153 | Detailliertes Feedback (pro Section/Claim) | Granulare Korrekturen > "war schlecht". Jede Korrektur = Klassen-Regel. |
| D-154 | Platform = primäres Interface | Telegram für Quick Messages, Platform für Arbeit |
| D-155 | v1.0 = fehlerfrei + live AI + 5 VC Emails gesendet | Messbare Definition of Done |
| D-156 | Backend abstrahiert (Action Layer) | Mia heute, austauschbar morgen |
| D-157 | Build nur wenn Build → Send → Revenue | Anti-Overbuild-Regel |
| D-158 | ISO 27001/9001-aligned Dokumentation | Nachvollziehbar, versioniert, auditierbar |

---

---

## Recent Updates (v0.13.0)

### Phase A: Database Performance
- **7 new indexes** for frequently queried tables (messages, findings, events)
- Verified index usage via EXPLAIN QUERY PLAN
- ~30-50% faster query performance on topic lookups

### Phase B: Cost Tracking
- **Per-topic AI cost breakdown** with per-message details
- **Total AI Cost KPI** in Executive Board (5th strategic metric, target $10/month)
- Cost tracking in messages table: `cost`, `tokens_prompt`, `tokens_completion`
- Cost aggregation in topics table: `cost_total`, `cost_updated_at`
- Automatic cost calculation for all `/api/ai/chat` responses

### Phase C: Session Replay + Keyboard Shortcuts
- **Session Replay endpoint** (`GET /api/topics/{id}/replay`): chronological timeline of messages, events, state changes
- **4 new keyboard shortcuts:**
  - **S**: Toggle topic priority (LOW → NORMAL → HIGH → NOW)
  - **D**: Mark current topic as done
  - **/**: Focus search (alias for Cmd+K)
  - **?**: Show keyboard shortcuts help modal

[See [CHANGELOG.md](CHANGELOG.md) for full version history]

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **J** | Next topic |
| **K** | Previous topic |
| **E** | Edit current topic |
| **C** | Toggle context panel |
| **S** | Toggle topic priority |
| **D** | Mark topic done |
| **Cmd+K** (or **/**) | Command palette / Search |
| **Cmd+N** | New topic |
| **Cmd+.** | Toggle context panel |
| **Cmd+Enter** | Send message (in chat) |
| **Esc** | Close modals / Cancel |
| **?** | Show this help |
| **↑/↓** | Navigate command palette |
| **Enter** | Select in command palette |

---

## Quick Start

### Auto-Start (Recommended)

```bash
# Start the platform (auto-starts on boot via launchctl)
launchctl start com.ainary.workbench

# Open in browser
open http://localhost:8080
```

### Manual Start

```bash
cd projects/workbench/backend
python3 app.py
# Browser: http://localhost:8080
```

## Lizenz

Privat. Nicht für externe Nutzung oder Veröffentlichung.

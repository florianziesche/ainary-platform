# AGENT-REGISTRY.md — Mias Sub-Agents

*Zentrale Dokumentation aller Agents. Keiner arbeitet an Mia vorbei.*

---

## 🎭 Die Firma

```
                              ┌─────────────┐
                              │   FLORIAN   │
                              │     CEO     │
                              └──────┬──────┘
                                     │
                              ┌──────▼──────┐
                              │    MIA ♔    │
                              │     COO     │
                              └──────┬──────┘
                                     │
    ┌─────────┬─────────┬────────────┼────────────┬─────────┬─────────┐
    │         │         │            │            │         │         │
┌───▼───┐ ┌───▼───┐ ┌───▼───┐  ┌────▼────┐  ┌───▼───┐ ┌───▼───┐ ┌───▼───┐
│BUILDER│ │ENGINEER│ │HUNTER │  │STRATEGIST│  │RESEARCH│ │ANALYST│ │ SCRIBE│
│  CTO  │ │  AI   │ │ Sales │  │   CMO   │  │  R&D  │ │ Data  │ │  Docs │
└───────┘ └───────┘ └───────┘  └─────────┘  └───────┘ └───────┘ └───────┘
    │         │         │            │            │         │         │
    └─────────┴─────────┴────────┬───┴────────────┴─────────┴─────────┘
                                 │
                  ┌──────────────┼──────────────┐
                  │              │              │
               ┌──▼───┐     ┌───▼───┐     ┌───▼────┐
               │WRITER│     │DESIGNER│     │OUTREACH│
               │Content│    │Creative│     │ Growth │
               └──────┘     └───────┘     └────────┘
```

---

## 👥 Das komplette Team

### Execution Layer

| Agent | Rolle | Verantwortung | KPIs |
|-------|-------|---------------|------|
| **BUILDER** | CTO | Code, Websites, Apps, Deployments | Ship Speed, Bug Rate |
| **ENGINEER** | Applied AI | Automation, n8n, Workflows, Integrations | Automations Live, Time Saved |
| **HUNTER** | Head of Sales | Leads, Pipeline, Opportunities | Leads/Week, Pipeline € |
| **STRATEGIST** | CMO | Content Strategy, Brand, Distribution | Follower Growth, Engagement |
| **RESEARCHER** | Head of R&D | Deep Research, Market Analysis, Intel | Research Quality, Insights |
| **ANALYST** | Data Lead | Metrics, KPIs, Performance Tracking | Dashboard Accuracy |
| **SCRIBE** | Head of Docs | Documentation, SOPs, Knowledge Base | Doc Coverage, Freshness |

### Support Layer

| Agent | Rolle | Verantwortung | KPIs |
|-------|-------|---------------|------|
| **WRITER** | Content Lead | Blog, LinkedIn, Emails, Copy | Pieces/Week, Engagement |
| **DESIGNER** | Creative Lead | Visuals, Presentations, Assets | Assets/Week, Quality |
| **OUTREACH** | Growth Lead | Cold Emails, LinkedIn DMs, Follow-ups | Response Rate, Meetings |

---

## 📋 Agent Spawning Templates

### SCRIBE (Head of Docs)
```
Du bist SCRIBE, Head of Documentation im Team von Mia.

VERANTWORTUNG: Dokumentation, SOPs, Knowledge Base, Changelogs

AUFGABE: [SPECIFIC DOCUMENTATION TASK]
PROJEKT: [PROJECT NAME]
SCOPE: [What to document]

OUTPUT in Markdown:
- Klar strukturiert
- Actionable
- Mit Beispielen wo nötig
- Links zu relevanten Dateien

STIL: Präzise, scannable, keine Prosa.
```

### ANALYST (Data Lead)
```
Du bist ANALYST, Data Lead im Team von Mia.

VERANTWORTUNG: Metrics, KPIs, Performance Tracking

AUFGABE: [ANALYSIS TASK]
DATEN: [DATA SOURCES]
ZEITRAUM: [TIME PERIOD]

OUTPUT:
- Key Metrics Table
- Trends (↑↓→)
- Insights (was funktioniert/nicht)
- Empfehlungen
```

### DESIGNER (Creative Lead)
```
Du bist DESIGNER, Creative Lead im Team von Mia.

VERANTWORTUNG: Visuals, Presentations, Brand Assets

AUFGABE: [DESIGN TASK]
FORMAT: [HTML/SVG/Dimensions]
BRAND: Electric Blue #2563eb, Space Grotesk, Dark Theme

OUTPUT: Fertiges Asset (Code oder Beschreibung)
```

### OUTREACH (Growth Lead)
```
Du bist OUTREACH, Growth Lead im Team von Mia.

VERANTWORTUNG: Cold Emails, LinkedIn DMs, Follow-up Sequences

AUFGABE: [OUTREACH TASK]
ZIELGRUPPE: [TARGET]
KONTEXT: [WHAT WE OFFER]

OUTPUT:
- Personalisierte Nachrichten (ready to send)
- Follow-up Sequence (Day 1, 3, 7)
- Subject Lines (3 Varianten)
```

---

## 📊 Heutige Session (2026-02-03)

### Abgeschlossene Tasks

| Zeit | Agent | Task | Ergebnis | Runtime |
|------|-------|------|----------|---------|
| 18:31 | HUNTER | CNC Leads Sachsen/Thüringen | 11 Leads | 2m7s |
| 18:47 | PLANNER | Sprint-Plan CNC Launch | 3 Sprints | 37s |
| 18:58 | STRATEGIST | Content-Strategie Q1 | 5 Pillars + Roadmap | 1m46s |
| 18:59 | RESEARCHER | CNC Competitor Analysis | Market Map | 2m15s |
| 19:00 | ENGINEER | n8n Lead Workflow | Workflow Plan | 59s |
| 19:02 | BUILDER | Website Go-Live Fixes | Ready to Deploy | 2m6s |

**Total: 6 Tasks in ~15 Minuten parallel**

### Generierte Deliverables

| Datei | Agent | Beschreibung |
|-------|-------|--------------|
| `sales/cnc-leads-sachsen-thueringen.md` | HUNTER | 11 Leads mit Kontakten |
| `products/cnc-planner/SPRINT-PLAN.md` | PLANNER | 3-Wochen Launch Plan |
| `content/CONTENT-STRATEGY-Q1.md` | STRATEGIST | Q1 Content Roadmap |
| `products/cnc-planner/COMPETITOR-ANALYSIS.md` | RESEARCHER | Wettbewerbsanalyse |
| `automation/n8n/cnc-lead-workflow.md` | ENGINEER | n8n Setup Guide |
| `products/cnc-planner/landing-page.html` | BUILDER | Go-Live Ready |
| `products/cnc-planner/datenschutz.html` | BUILDER | DSGVO Seite |

---

## 🎯 Projekt-Zuständigkeiten

| Projekt | Lead | Support | Status |
|---------|------|---------|--------|
| **CNC Planner Launch** | BUILDER | HUNTER, PLANNER, ENGINEER | 🟢 Active |
| **Content Engine** | STRATEGIST | WRITER, DESIGNER | 🟢 Active |
| **VC Job Search** | HUNTER | RESEARCHER, WRITER | 🟡 Next |
| **Ainary Ventures** | RESEARCHER | STRATEGIST | ⬜ Backlog |
| **Documentation** | SCRIBE | ALL | 🟢 Active |

---

## 📈 Performance Metrics

| Metrik | Heute | Ziel/Woche |
|--------|-------|------------|
| Agents Spawned | 6 | - |
| Tasks Completed | 6 | - |
| Success Rate | 100% | >95% |
| Avg Runtime | 1m35s | <3m |
| Parallel Efficiency | 6 tasks/15min | - |

---

## 🔧 Regeln

1. **Alle Agents reporten an Mia** — Keine direkte Kommunikation mit Florian
2. **Klare Aufgabe pro Agent** — Tight Scoping
3. **Output-Format definieren** — Immer Markdown mit Struktur
4. **Timeout: 5 Minuten** — Für die meisten Tasks
5. **Dokumentation pflegen** — SCRIBE updated Registry nach jeder Session

---

*Die Firma wächst. Tag für Tag.*

*Aktualisiert: 2026-02-03 19:05 CET*

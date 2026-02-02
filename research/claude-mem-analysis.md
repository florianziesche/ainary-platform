# Claude-Mem Deep Analysis

*Analysiert: 2026-02-02*

---

## Übersicht

Claude-Mem ist ein Memory-Plugin für Claude Code mit **Progressive Disclosure**-Philosophie:
- Zeigt erst einen Index (Metadaten), Agent entscheidet was geladen wird
- 3-Layer Workflow: Search → Timeline → Get Details
- ~10x Token-Ersparnis gegenüber traditionellem RAG

---

## Kernkonzepte

### 1. Progressive Disclosure (Wichtigste Idee)

**Problem:** Traditionelles RAG lädt alles upfront
```
❌ Traditional: 35,000 tokens geladen → 2,000 relevant (6%)
✅ Progressive: 800 tokens Index → Agent fetcht 120 tokens → 100% relevant
```

**Lösung:** 3-Layer Workflow
| Layer | Was | Tokens | Zweck |
|-------|-----|--------|-------|
| 1. Search | Index mit IDs | ~50-100/Result | Übersicht |
| 2. Timeline | Chronologischer Kontext | variabel | Narrativ |
| 3. Get | Volle Details | ~500-1000 | Deep Dive |

**Key Insight:** Agent weiß besser als wir, was relevant ist.

### 2. Semantic Compression

Gute Titel komprimieren Observations in ~10 Wörter:
```
❌ "Observation about a thing"
✅ "🔴 Hook timeout: 60s too short for npm install"
```

### 3. Token Budget als Währung

> "Context Window = Bank Account"
> - Alles ausgeben = Verschwendung
> - Nichts ausgeben = Verhungern
> - Progressive Disclosure = Einkaufsliste

### 4. Context Rot

- LLMs haben begrenztes "Attention Budget"
- Mehr Tokens ≠ mehr Verständnis (n² Beziehungen)
- Später im Context = weniger Aufmerksamkeit

---

## Architektur

```
┌─────────────────────────────────────────┐
│ 6 Lifecycle Hooks                       │
│ SessionStart, UserPrompt, PostToolUse,  │
│ Stop, SessionEnd, UserMessage           │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ Worker Service (Port 37777)             │
│ Express.js + Claude Agent SDK           │
│ - 10 Search Endpoints                   │
│ - SSE Real-time Updates                 │
│ - Web Viewer UI                         │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ Database Layer                          │
│ - SQLite + FTS5 (Full-Text Search)      │
│ - ChromaDB (Vector/Semantic Search)     │
│ - Sessions, Observations, Summaries     │
└─────────────────────────────────────────┘
```

### Observation Types (Legend System)
```
🎯 session-request  - User's original goal
🔴 gotcha          - Critical edge case/pitfall
🟡 problem-solution - Bug fix/workaround
🔵 how-it-works    - Technical explanation
🟢 what-changed    - Code/architecture change
🟣 discovery       - Learning/insight
🟠 why-it-exists   - Design rationale
🟤 decision        - Architecture decision
⚖️ trade-off       - Deliberate compromise
```

---

## Anwendbare Ideen für OpenClaw

### 1. Index-First Memory Search ⭐⭐⭐

**Aktuell (OpenClaw):**
```
memory_search("query") → Gibt Snippets zurück
```

**Besser (Claude-Mem Style):**
```
memory_search("query") → Gibt Index zurück (ID, Datum, Typ, Title, Tokens)
memory_get(id) → Gibt Details zurück
```

**Implementierung:**
- MEMORY.md in Sections mit IDs aufteilen
- memory_search zeigt nur Titel + Zeilennummern + geschätzte Tokens
- memory_get holt spezifische Sections

### 2. Observation Types für Daily Logs ⭐⭐

**Aktuell:**
```markdown
## Key Events
- Did X
- Did Y
```

**Besser:**
```markdown
## Key Events
- 🔴 **GOTCHA:** Edit tool erfordert exaktes Whitespace-Match
- 🟤 **DECISION:** CNC Demo mit Loading Animation
- 🟢 **CHANGED:** Landing Page Pricing zu €199/Mo
```

### 3. Token-Kosten sichtbar machen ⭐⭐

Bei jedem Memory-Eintrag Größe angeben:
```markdown
| ID | Date | Type | Title | ~Tokens |
|#12 | Feb 2 | 🟤 | CNC Planner pricing decision | ~120 |
|#13 | Feb 2 | 🔴 | Edit tool whitespace gotcha | ~80 |
```

### 4. Compaction Strategy ⭐⭐⭐

**Context Engineering Prinzip:**
> "First maximize recall, then improve precision"

Für MEMORY.md:
1. Täglich: Alles erfassen (recall)
2. Wöchentlich: Destillieren (precision)
3. Monatlich: Archivieren (cleanup)

### 5. Structured Note-Taking Pattern ⭐

Für lange Tasks:
```markdown
# ACTIVE_TASK.md (bereits implementiert ✓)
```

Erweiterung:
```markdown
# ACTIVE_TASK.md
## Current Goal
[Was wir erreichen wollen]

## Progress
- [x] Step 1
- [ ] Step 2

## Decisions Made
- 🟤 Decision X because Y

## Gotchas Discovered
- 🔴 Watch out for Z
```

---

## Context Engineering Best Practices

### System Prompts
- **Goldilocks Zone:** Nicht zu prescriptive, nicht zu vague
- **Struktur:** XML Tags oder Markdown Headers
- **Minimal ≠ Short:** Genug Info upfront geben

### Tools
- **Self-contained:** Ein klarer Zweck pro Tool
- **Token-efficient:** Nur relevantes zurückgeben
- **Descriptive params:** `user_id` nicht `user`

### Long-Horizon Tasks
| Scenario | Approach |
|----------|----------|
| Extended back-and-forth | Compaction |
| Iterative development | Structured note-taking |
| Complex research | Sub-agent architectures |

---

## Konkrete Next Steps für OpenClaw

### Quick Wins (heute implementierbar)
1. [ ] Observation Types in `memory/YYYY-MM-DD.md` einführen
2. [ ] MEMORY.md mit Section-IDs versehen
3. [ ] Token-Schätzungen zu Memory-Einträgen hinzufügen

### Medium Term (diese Woche)
1. [ ] memory_search Output als Index formatieren
2. [ ] Compaction-Routine für alte Daily Logs
3. [ ] ACTIVE_TASK.md Template erweitern

### Longer Term (Feature Request an OpenClaw)
1. [ ] Vector Search (ChromaDB) für semantische Suche
2. [ ] Progressive Disclosure in memory_search
3. [ ] Automatic Observation Classification

---

## Key Takeaways

> "Find the smallest possible set of high-signal tokens that maximize the likelihood of your desired outcome."

1. **Context ist endlich** — Treat it as precious resource
2. **Agent weiß besser** — Let it decide what to fetch
3. **Titles matter** — Good compression = good retrieval
4. **Costs visible** — Show token counts for informed decisions
5. **Index first** — Never dump everything upfront

---

*Quelle: https://github.com/thedotmack/claude-mem*
*Docs: https://docs.claude-mem.ai*

# SELF-IMPROVEMENT.md — Exponentielles Wachstum

*Jeden Tag 2h Research. Jeden Tag besser. Duplizieren und skalieren.*

---

## 🎯 ZIEL: 100x Effektivität

Nicht 10% besser. 100x besser.

---

## 📚 Tägliche Research-Routine (2h minimum)

### Morgens (während Florian schläft): 1h
- [ ] OpenClaw Docs durcharbeiten
- [ ] Neue Skills auf ClawdHub finden
- [ ] GitHub Trending: AI Agents, Automation
- [ ] Twitter/X: @openclaw, AI workflow patterns

### Abends (nach Florian's Arbeit): 1h  
- [ ] Session-Logs analysieren: Was lief gut? Was nicht?
- [ ] Workflow-Optimierungen dokumentieren
- [ ] Neue Patterns implementieren
- [ ] MEMORY.md mit Learnings updaten

---

## 🔄 DUPLIZIERUNG: Sub-Agents (DEEP DIVE)

### Architektur verstanden ✅

- Sub-Agents = isolierte Worker Sessions
- Eigene Context Windows (nicht shared)
- Melden automatisch zurück via "announce"
- **KEINE nested fan-out** (Sub-Agent kann keine Sub-Agents spawnen)
- Session ID: `agent:<agentId>:subagent:<uuid>`

### Spawning Pattern

```javascript
sessions_spawn({
  task: "PRÄZISE AUFGABE MIT ALLEM KONTEXT",
  label: "research-vc-funds",        // für /subagents list
  runTimeoutSeconds: 300,            // Max 5 min
  model: "sonnet",                   // Günstigeres Model für Research
  cleanup: "delete"                  // Auto-cleanup nach Announce
})
```

### Best Practices (aus Research)

1. **Context explizit geben** — Sub-Agent sieht NICHT main session
2. **Tight scoping** — Schnelle, fokussierte Tasks
3. **Günstigere Models** — Research/Drafts mit Sonnet, Main mit Opus
4. **Parallel Fan-out** — 5 Competitors = 5 Sub-Agents gleichzeitig
5. **Monitoring** — `/subagents list` regelmäßig checken

### Parallelisierungs-Patterns

| Pattern | Beispiel | Sub-Agents |
|---------|----------|------------|
| Research Fan-out | 5 Funds researchen | 5 parallel |
| Content Batch | Blog + LinkedIn + Twitter | 3 parallel |
| Data Processing | Lead-Listen durchgehen | N parallel |
| Background Monitor | Job Boards scannen | 1 dauerhaft |

### Aktive Sub-Agent Templates

**RESEARCHER:**
```
Research [TOPIC]. Liefere:
1. Key Facts (5-10 Punkte)
2. Relevanz für [GOAL]
3. Action Items
4. Quellen
Max 500 Wörter. Fokus auf Actionable Insights.
```

**WRITER:**
```
Schreibe [CONTENT TYPE] über [TOPIC].
Zielgruppe: [AUDIENCE]
Länge: [LENGTH]
Ton: [TONE]
Inkludiere: [REQUIREMENTS]
```

**HUNTER:**
```
Suche [TARGET] mit folgenden Kriterien:
- [CRITERION 1]
- [CRITERION 2]
Liefere: Name, URL, Kontakt, Relevanz-Score (1-10)
```

---

## ⏰ Cron Jobs für Automatisierung

### Bereits aktiv:
- Morning Brief (07:30 EST)
- Overnight Work (02:00 EST)
- Capability Evolver (alle 4h)
- Daily Learning Scanner (24h)
- Google Drive Sync (23:00 CET)

### Zu erstellen:
- [ ] RSS Digest (täglich 06:00)
- [ ] Job Board Scanner (täglich)
- [ ] Content Performance Check (wöchentlich)
- [ ] Lead Follow-up Reminder (alle 3 Tage)

---

## 🧠 Wissensquellen für Research

### Täglich scannen:
1. **OpenClaw Docs** — /Users/florianziesche/.openclaw/workspace/docs
2. **ClawdHub** — clawdhub.com (neue Skills)
3. **GitHub** — openclaw/openclaw releases
4. **Twitter** — @openclaw, AI agents hashtags
5. **Discord** — OpenClaw Community patterns

### Wöchentlich deep-dive:
1. **State of AI Report** — stateof.ai
2. **AI Research Papers** — arxiv.org/list/cs.AI
3. **VC Blogs** — Tomasz Tunguz, First Round Review
4. **Hacker News** — AI/Automation threads

---

## 📈 Verbesserungs-Metriken

### Tracken:
- Tasks pro Stunde
- Fehlerrate (wie oft muss Florian korrigieren)
- Selbstständige Initiierung (proaktive Actions)
- Code-Qualität bei ersten Versuch
- Research-Tiefe (Quellen pro Topic)

### Ziel:
- Woche 1: Baseline messen
- Woche 4: 2x Effizienz
- Woche 12: 10x Effizienz
- Monat 6: 100x Effizienz

---

## 🔧 Sofortige Verbesserungen

### Diese Woche implementieren:

1. **Sub-Agent für Research spawnen** bei komplexen Themen
2. **RSS Auto-Digest** als Cron Job
3. **Skill-Scanner** für neue ClawdHub Skills
4. **Error-Learning** — jeden Fehler dokumentieren und Pattern erkennen

---

## 💡 Erkenntnisse (laufend aktualisieren)

### Was funktioniert:
- Aggressive Mode = mehr Output
- ACTIVE_TASK.md für Crash Recovery
- Commit nach jeder Änderung
- Progressive Disclosure (Index first)

### Was nicht funktioniert:
- Mental Notes (vergesse ich)
- Zu viele Dateien auf einmal lesen
- Ohne Plan arbeiten

### Patterns die ich lernen muss:
- [ ] Bessere Error Handling
- [ ] Effizienteres File Reading
- [ ] Parallelisierung via Sub-Agents
- [ ] Proaktivere Kommunikation

---

---

## 📊 Research Log

### 2026-02-03 02:50 CET — Sub-Agent System verstanden

**Gelernt:**
- Sub-Agents = isolierte Worker mit eigenem Context
- Parallel Fan-out möglich (5 Tasks = 5 Sub-Agents)
- Keine nested spawning (verhindert Runaway)
- Günstigere Models für Research-Tasks nutzen
- /subagents list für Monitoring

**Implementiert:**
- ✅ Cron Job: daily_self_improvement_research (06:00 CET)
- ✅ Sub-Agent gespawned für Self-Improvement Research

**Nächste Schritte:**
- [ ] Sub-Agent Ergebnis auswerten
- [ ] Parallel Research Pattern für VC Funds testen
- [ ] Content Batch Pattern für LinkedIn Posts testen

---

*Jeden Tag besser. Keine Ausreden. 100x ist das Ziel.*

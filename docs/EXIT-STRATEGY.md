# Exit-Strategie — Unabhängigkeit von OpenClaw

*Ziel: Mia läuft weiter, egal was mit OpenClaw passiert.*
*Created: 2026-02-14*

## Was wir besitzen (portabel, kein Lock-in)

| Asset | Format | Location | Backup |
|-------|--------|----------|--------|
| Memory System | Markdown | workspace/memory/ | Git + Google Drive |
| Agent Configs | Markdown | workspace/agents/ | Git |
| Research Library | Markdown + PDF | experiments/ + Drive | Google Drive |
| Content | Markdown | content/ | Git + Drive |
| Website | Static HTML | projects/platform-website/ | Git + Vercel |
| Soul/Identity | Markdown | SOUL.md, IDENTITY.md | Git |
| Corrections | Markdown | memory/corrections.md | Git |
| Code/Scripts | Bash/JS | scripts/, projects/ | Git |
| Kontakte | Markdown | memory/people.md | Git |
| Entscheidungen | Markdown | memory/decisions.md | Git |

**Risiko: NIEDRIG** — Alles ist Standard-Markdown + Standard-Tools.

## Was von OpenClaw abhängt

| Funktion | OpenClaw Feature | Alternative | Aufwand |
|----------|-----------------|-------------|---------|
| Telegram Bot | Channel Bridge | python-telegram-bot + Claude API | 4h |
| iMessage | imsg CLI | imsg funktioniert standalone | 0h |
| WhatsApp | wacli CLI | wacli funktioniert standalone | 0h |
| Cron Jobs | OpenClaw Cron | System crontab + Script | 2h |
| Heartbeats | OpenClaw Heartbeat | Cron + Claude API Call | 2h |
| Sub-Agents | sessions_spawn | Claude API mit eigener Queue | 8h |
| Memory Search | Embedding Search | Local Embeddings (Ollama) | 4h |
| Web Search | Brave API | Brave API Key direkt | 1h |
| Email | gog CLI | gog funktioniert standalone | 0h |
| Browser | OpenClaw Browser | Playwright direkt | 2h |
| Tool Routing | Multi-tool orchestration | n8n oder eigenes Script | 8h |

**Geschätzter Migrations-Aufwand: 1-2 Tage**

## Migration Plan (wenn nötig)

### Phase 1: Sofort (Tag 1, 4h)

1. **Telegram Bot aufsetzen**
```bash
# python-telegram-bot + Anthropic SDK
pip install python-telegram-bot anthropic
```
- Bot Token haben wir schon
- Claude API Key haben wir
- Memory-Files laden → System Prompt
- Basis-Chat in 2h

2. **Cron ersetzen**
```bash
# System crontab
crontab -e
# 0 8 * * * /path/to/morning-briefing.sh
# 0 21 * * * /path/to/daily-report.sh
```

3. **CLI Tools laufen weiter**
- imsg, wacli, gog, pandoc = unabhängig von OpenClaw
- Nur Wrapper-Scripts anpassen

### Phase 2: Tag 1-2 (8h)

4. **Sub-Agent System**
```python
# Eigene Queue: Main Agent spawnt Tasks
import anthropic
client = anthropic.Anthropic()

def spawn_agent(task, model="claude-sonnet-4-5"):
    response = client.messages.create(
        model=model,
        system=load_file("agents/research/AGENT.md"),
        messages=[{"role": "user", "content": task}]
    )
    return response.content
```

5. **Memory Search**
- Option A: OpenAI Embeddings API (wie jetzt, ohne OpenClaw)
- Option B: Local Embeddings via Ollama
- Option C: Simple grep (80% so gut)

6. **n8n als Orchestrator (optional)**
- Webhook → Claude API → Tool Routing → Response
- Visueller Workflow Builder
- Self-hosted

### Phase 3: Optimierung (Woche 1)

7. **Multi-Channel Hub**
- n8n Workflow: Telegram + iMessage + WhatsApp → Claude → Response → Channel
- Oder: eigener Python Service

8. **Monitoring**
- Uptime Check für Bot
- Error Logging
- Cost Tracking (API Calls)

## Kosten nach Migration

| Service | Kosten/Monat |
|---------|-------------|
| Claude API (Opus) | ~$50-100 (je nach Nutzung) |
| Brave Search API | $0 (free tier) |
| OpenAI Embeddings | ~$1 |
| Telegram Bot | $0 |
| VPS (falls nötig) | ~$5-10 |
| **Total** | **~$60-110/Monat** |

vs. OpenClaw: Kostenlos (Open Source) + Claude API Kosten

## Präventiv-Maßnahmen (JETZT)

### Tägliches Backup (bereits aktiv)
- Git commit + push täglich
- Google Drive Sync für PDFs
- backup.sh Cron

### Monatlicher Export-Check
- [ ] Alle Memory-Files vollständig?
- [ ] Agents-Configs aktuell?
- [ ] Google Drive Sync funktioniert?
- [ ] API Keys dokumentiert (1Password)?

### API Keys sichern
Alle Keys die wir brauchen (in 1Password oder sicher dokumentiert):
- ANTHROPIC_API_KEY
- OPENAI_API_KEY (Embeddings)
- BRAVE_API_KEY
- TELEGRAM_BOT_TOKEN
- Google OAuth Tokens (gog)
- GitHub Token

## Trigger: Wann migrieren?

| Signal | Aktion |
|--------|--------|
| OpenClaw wird eingestellt | Phase 1-3 starten |
| OpenClaw wird acquired + closed | Phase 1-3 starten |
| OpenClaw wird acquired + weitergeführt | Beobachten, Exit vorbereiten |
| Breaking Changes ohne Alternative | Phase 1 vorbereiten |
| Pricing wird zu hoch | Kosten-Vergleich, ggf. migrieren |
| Bessere Alternative erscheint | Evaluieren, nicht sofort wechseln |

## Fazit

**Mia ist nicht OpenClaw. Mia ist die Intelligence in den Files.**

OpenClaw ist das Chassis. Wenn es kaputt geht, bauen wir ein neues.
Was zählt: SOUL.md, MEMORY.md, Agents, Research, Content, Contacts.
Das alles gehört dir. Auf deinem Mac. In deinem Git. In deinem Drive.

---
*Review: Quarterly (nächster Check: Mai 2026)*

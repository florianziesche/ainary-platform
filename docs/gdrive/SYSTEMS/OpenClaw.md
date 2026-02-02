# OpenClaw — System-Dokumentation

*Persönlicher AI-Assistent mit Multi-Channel Support*

---

## Übersicht

OpenClaw ist ein AI-Orchestrierungssystem, das Claude (Anthropic) als Basis nutzt und über verschiedene Kanäle erreichbar ist.

**Installiert:** via npm global
**Location:** `~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/`
**Workspace:** `~/.openclaw/workspace/`

---

## Architektur

```
┌─────────────────────────────────────────────────┐
│                   Channels                       │
│  Telegram │ WhatsApp │ Discord │ Webchat        │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              OpenClaw Gateway                    │
│  - Session Management                           │
│  - Message Routing                              │
│  - Tool Orchestration                           │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              Claude (Anthropic)                  │
│  - Reasoning                                    │
│  - Tool Calls                                   │
│  - Response Generation                          │
└─────────────────────────────────────────────────┘
```

---

## Konfiguration

**Config Location:** `~/.openclaw/config.yaml`

### Wichtige Settings

| Setting | Wert | Beschreibung |
|---------|------|--------------|
| Model | `anthropic/claude-sonnet-4` | Standard-Modell |
| Workspace | `~/.openclaw/workspace` | Arbeitsverzeichnis |
| Memory | `MEMORY.md` + `memory/*.md` | Persistenter Speicher |

---

## Skills

Skills erweitern OpenClaw's Fähigkeiten. Installiert unter:
`~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/skills/`

### Aktive Skills

| Skill | Beschreibung | Status |
|-------|--------------|--------|
| gog | Google Workspace (Gmail, Drive, Calendar) | ✅ |
| github | GitHub CLI Integration | ✅ |
| obsidian | Obsidian Vault Management | ✅ |
| weather | Wetter-Abfragen | ✅ |
| web_search | Brave Search | ⚠️ API Key fehlt |

---

## Memory-System

### Struktur

```
~/.openclaw/workspace/
├── MEMORY.md           ← Langzeit-Gedächtnis (kuratiert)
├── memory/
│   ├── YYYY-MM-DD.md   ← Tägliche Logs
│   └── *.md            ← Thematische Notes
├── SOUL.md             ← Persönlichkeit
├── USER.md             ← User-Kontext
└── AGENTS.md           ← Sub-Agent Definitionen
```

### Memory-Workflow

1. **Täglich:** Ereignisse in `memory/YYYY-MM-DD.md` loggen
2. **Heartbeats:** MEMORY.md mit wichtigen Insights updaten
3. **Recall:** `memory_search` für semantische Suche

---

## Heartbeats

Regelmäßige Check-ins definiert in `HEARTBEAT.md`.

**Schedule:** Konfigurierbar (Default: alle 30 Min)

### Typischer Heartbeat-Flow

1. HEARTBEAT.md lesen
2. Checks durchführen (Email, Calendar, etc.)
3. Bei Bedarf User benachrichtigen
4. Sonst: `HEARTBEAT_OK`

---

## Cron Jobs

Scheduled Tasks über OpenClaw Cron.

### Aktive Jobs

| Job | Schedule | Beschreibung |
|-----|----------|--------------|
| Morning Brief | 08:00 CET | Tägliches Briefing |
| Drive Sync | 23:00 CET | Heavy Files → Google Drive |

---

## Channels

### Telegram (Primary)
- Bot Token in Config
- Primärer Kommunikationskanal

### Webchat
- Local Development UI
- `openclaw chat`

---

## Troubleshooting

### Gateway startet nicht
```bash
openclaw gateway status
openclaw gateway restart
```

### Config prüfen
```bash
openclaw status
```

### Logs
```bash
tail -f ~/.openclaw/logs/gateway.log
```

---

## Updates

```bash
npm update -g openclaw
openclaw gateway restart
```

---

*Erstellt: 2026-02-02*
*Version: OpenClaw v0.x*

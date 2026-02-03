# Moltbot Analysis — Research Notes

**URL:** https://moltbot.you/
**Date:** 2026-02-03
**Relevanz:** Competitor/Alternative zu OpenClaw, Learnings für unsere AI-Workflows

---

## Quick Facts

| Metric | Value |
|--------|-------|
| GitHub Stars | 61,500+ |
| GitHub Forks | 7,400+ |
| Skills | 565+ auf ClawdHub |
| Integrations | 50+ |
| License | MIT |
| Gründer | Peter Steinberger (PSPDFKit) |

---

## Key Features

### 1. Self-Improving AI
> "moltbot can autonomously write and modify its own skills"

**Learning:** Der Agent kann seine eigenen Capabilities erweitern durch:
- Neue Skills schreiben während der Nutzung
- Verhalten anpassen basierend auf Feedback
- "Pushing boundaries of personal AI autonomy"

→ **Relevant für EXPONENTIAL.md** — wir machen ähnliches mit unserem Self-Improvement System

### 2. Skill Structure
- Jeder Skill = Directory mit `SKILL.md`
- YAML Frontmatter für Metadata
- Drei Loading Priorities:
  1. Bundled Skills (lowest)
  2. Managed Skills `~/.clawdbot/skills`
  3. Workspace Skills `<workspace>/skills` (highest)

→ **Sehr ähnlich zu OpenClaw Skills**

### 3. Node Capabilities
- Screen Capture/Recording
- Camera Access
- Location Data
- Voice Wake / TTS
- Shell Access
- Canvas (A2UI)

→ **OpenClaw hat ähnliche Node Capabilities**

### 4. Channel Support
- WhatsApp (via Baileys)
- Telegram (via grammY)
- Discord
- Slack (via Bolt)
- Signal
- iMessage
- Matrix
- MS Teams
- WebChat

→ **Identisch zu OpenClaw Channels**

---

## Interesting Use Cases

1. **Email Triage** — Automatisch sortieren, archivieren, flaggen
2. **Smart Home** — Home Assistant Integration
3. **DevOps** — Tests laufen lassen, Deployments checken
4. **Data Processing** — PDFs extrahieren, Spreadsheets generieren
5. **Travel** — Airline Check-in automatisieren (24h vor Abflug)
6. **Voice Briefings** — Morning Briefing vorlesen lassen
7. **Screen Intelligence** — Screenshot analysieren, debuggen helfen
8. **Location Automation** — Geofence-basierte Triggers

---

## History Note

- Vorher "Clawdbot" genannt
- Umbenannt wegen Anthropic Trademark ("Claude" zu ähnlich)
- "Molt" = was Hummer machen wenn sie Schale abwerfen
- Scam-Warnung: Fake Crypto Tokens wurden erstellt (Moltbot hat KEINE Crypto)

---

## Learnings für uns

### 1. Community Matters
61K Stars zeigt dass Open-Source AI Assistants großes Interesse haben.
ClawdHub mit 565+ Skills = starkes Ecosystem.

### 2. Self-Improving ist der Schlüssel
"The AI learns your patterns and can even suggest automation opportunities you haven't thought of"
→ Genau was wir mit EXPONENTIAL.md anstreben

### 3. Konkrete Use Cases verkaufen
Die Use Case Seite zeigt sehr konkrete Beispiele mit Beispiel-Prompts.
→ Wir könnten ähnliches für CNC Planner machen

### 4. Security ist wichtig für Enterprise
"Enterprise-grade security features" wird prominent erwähnt.
→ Relevant für unsere ISO 27001 Docs bei CNC Planner

---

## Potential Actions

- [ ] ClawdHub Skills anschauen — gibt es welche die wir nutzen können?
- [ ] Skill-Format vergleichen mit OpenClaw
- [ ] Use Case Format für CNC Planner übernehmen
- [ ] Self-Improving Features weiter ausbauen

---

*Research by Mia, 2026-02-03 04:35*

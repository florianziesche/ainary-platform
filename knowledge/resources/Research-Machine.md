---
tags: [research, ai-agents, system]
tier: KNOWLEDGE
expires: 2027-02-19
---

# Research Machine

Automatisiertes Research-System fuer [[AI]] Agent Papers, Breakthroughs und Developments.

## Architektur

```
Layer 4: OUTPUT (Artikel, Briefings, Threads)
    |
Layer 3: SYNTHESIS (Pattern-Erkennung, Connections)
    |
Layer 2: PROCESSING (Lesen, Zusammenfassen, Bewerten)
    |
Layer 1: INTAKE (Automatisch sammeln, filtern)
```

## Layer 1 — INTAKE (AKTIV)

**35 RSS Feeds**, gescannt 3x taeglich (07:00, 13:00, 19:00):

### [[AI]] Research
- ArXiv cs.[[AI]], cs.CL, cs.MA
- HuggingFace Papers (trending)
- Lilian Weng, The Gradient, Interconnects

### [[AI]] Praxis
- Simon Willison, Latent Space, Ahead of [[AI]]
- The Batch (Andrew Ng), One Useful Thing
- The Pragmatic Engineer

### [[VC]] & Strategy
- a16z, Sequoia, First Round Review
- Stratechery, Not Boring, Benedict Evans
- Paul Graham, Sam Altman, Elad Gil

### Ergebnisse
- Inbox: [[Research-Inbox/]] (taeglich, Top 10)
- Alerts: Telegram bei Score 9/10

## Layer 2 — PROCESSING (Heartbeat)
- Alle 12h: Inbox reviewen, Relevanz scoren
- Score > 7: Zusammenfassung schreiben
- Score > 9: Breakthrough Alert

## Layer 3 — SYNTHESIS (woechentlich)
- Sonntags: Weekly Research Brief
- Patterns erkennen, Connections mappen
- Output: [[Research-Weekly/]]

## Layer 4 — OUTPUT
- Substack Artikel aus Research-Basis
- State of [[AI]] Agents (monatlich)

## Key Documents
- [[Top-20-Agent-Papers]] — Foundational Papers
- [[Agent-Developments-Jan-Feb-2026]] — Recent Breakthroughs

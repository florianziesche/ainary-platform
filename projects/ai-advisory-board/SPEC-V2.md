# Advisory Board v2 — Research-Backed Advisors

## Vision
Kunde gibt Frage ein → Research Engine scannt Quellen → Knowledge Structure wird gebaut → 6 Advisors antworten INFORMED mit Quellen → Report + Sources an Kunde.

## Flow

```
1. INPUT:     Kunde gibt strategische Frage ein
2. RESEARCH:  Research Engine scannt ArXiv, HN, Reddit, GitHub, VC Blogs (30s)
3. KNOWLEDGE: AI baut Knowledge Structure (Key Facts, Trends, Counter-Arguments)
4. ADVISORS:  6 Advisors bekommen Research als Context → antworten informed
5. SYNTHESIS: Cross-Advisor Consensus + Dissent + Action Items
6. OUTPUT:    HTML Report + Quellen + Email-Gate Download
```

## Architektur-Änderungen (v1 → v2)

### board.js (Orchestrator)
```
v1: Frage → 6x GPT-4o parallel → Render
v2: Frage → Research Engine → Knowledge Structure → 6x GPT-4o (mit Research Context) → Synthesis → Render
```

### Neue Phase: Research (vor Advisors)
1. Import Research Engine Sources (arxiv, hn, reddit, github, rss)
2. Keyword-Extraktion aus Frage
3. Gefilterte Suche pro Quelle (nur relevante Results)
4. GPT-4o: Knowledge Structure bauen
   - Key Facts (was ist bekannt?)
   - Recent Developments (was ist neu?)
   - Open Questions (was ist unklar?)
   - Counter-Arguments (was spricht dagegen?)

### Advisor Upgrade
- Jeder Advisor bekommt Knowledge Structure als zusätzlichen Context
- System Prompt erweitert: "Base your response on the following research..."
- Advisors MÜSSEN Quellen zitieren wenn sie Research nutzen
- Confidence Indicator pro Advisor (wie sicher basierend auf verfügbaren Daten?)

### Neue Phase: Synthesis (nach Advisors)
- Consensus: Wo sind sich 4+ Advisors einig?
- Dissent: Wo gibt es fundamentale Meinungsverschiedenheiten?
- Action Items: Top 3 nächste Schritte (gewichtet nach Advisor-Consensus)
- Sources: Alle zitierten Quellen mit Links

## Template Änderungen
- Neue Section oben: "Research Context" (collapsible)
  - Zeigt Knowledge Structure
  - Zeigt welche Quellen gescannt wurden + Anzahl Results
- Advisor Cards: + Quellen-Tags unter jeder Antwort
- Confidence Indicator pro Advisor (●●●○○ Stil wie Startup X-Ray)
- Neue Section: "Consensus & Action Items"
- Sources Section am Ende (alle Quellen mit Links)

## Design
- Accent: Gold (#c8aa50) — bleibt gleich
- Neues Icon: Research-Phase bekommt Emerald Sub-Accent
- "Research-Backed" Badge im Header
- Quellen-Links in Advisor-Antworten

## Pricing Integration
- Free: 1 Frage/Monat OHNE Research (v1 Modus)
- Pro $49: 10 Fragen/Monat MIT Research
- Customer Project: Dedizierte Knowledge Base + laufende Beratung

## CLI
```bash
# v1 Modus (schnell, kein Research)
node board.js "Question" --mode=quick

# v2 Modus (mit Research, default)
node board.js "Question"

# v2 mit erweitertem Research
node board.js "Question" --research-days=7
```

## Dependencies
- Research Engine Sources (import aus ../research-engine/sources/)
- OpenAI API Key (GPT-4o)
- Kein neues npm Package nötig

## Aufwand
- Research Integration: ~2h
- Advisor Context Upgrade: ~1h
- Synthesis Phase: ~1h
- Template Update: ~2h
- Testing: ~1h
- **Total: ~7h / 1 Tag**

---
*Created: 2026-02-12*

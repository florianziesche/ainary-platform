# Sub-Agent Playbook — Wie man 20 Researcher ohne Crash spawnt

*Letzte Aktualisierung: 2026-02-04*

---

## Crash-Analyse

### Beobachtete Patterns
| Spawn | Runtime | Ergebnis | Task-Größe |
|-------|---------|----------|------------|
| 5× Agent (Feb 3) | 0s | ❌ Alle gecrasht | Groß, multi-step |
| researcher-sources-1 | 0s | ❌ Crash | 10 Quellen, 5 Themen |
| researcher-sources-2 | 3m3s | ✅ Erfolg (13 Quellen) | 10 Quellen, 6 Themen |

### Hypothesen
1. **Race Condition:** 2 gleichzeitig gestartet → einer crasht
2. **Task zu vage:** "Finde 10 Quellen" ohne klare Struktur → Agent weiß nicht wo anfangen
3. **Kein Kontext:** Agent hat kein SOUL.md, keine Tools-Info → orientierungslos
4. **Model-Limit:** Opus 4.5 als Sub-Agent könnte Timeout haben

### Was funktioniert hat (researcher-sources-2)
- Klare Struktur: 6 nummerierte Themen
- Spezifische Anweisungen: "Für JEDE Quelle: Organisation, Jahr, Datenpunkt, URL"
- Tier-1 Quellen explizit benannt: "Gartner, Forrester, McKinsey..."
- Ausschlusskriterien: "NO blogs, NO random websites"

---

## Optimale Spawn-Strategie: "20 Researcher"

### Regel 1: Sequentiell, nicht parallel
- Max 3 gleichzeitig (reduziert Race Conditions)
- Batch 1: 3 spawnen → warten → Ergebnisse einsammeln
- Batch 2: nächste 3 → usw.

### Regel 2: Ultra-fokussierte Tasks
SCHLECHT: "Recherchiere AI in Manufacturing"
GUT: "Finde die 3 aktuellsten Gartner-Prognosen zu Agentic AI in Manufacturing (2024-2026). Für jede: exaktes Zitat, Datum, URL."

### Regel 3: Ein Thema pro Agent
- Agent 1: "COPQ Statistiken — nur ASQ, McKinsey, Deloitte"
- Agent 2: "Fachkräftemangel — nur Destatis, IAB, WEF"
- Agent 3: "Machine Vision Marktdaten — nur Grand View, MarketsandMarkets"
- → 20 Agents = 20 ultra-spezifische Themen

### Regel 4: Output-Format erzwingen
```
Liefere EXAKT dieses Format:
## [Thema]
1. **[Organisation]** ([Jahr]) — "[exaktes Zitat oder Datenpunkt]" — URL: [link]
2. ...
Maximal 5 Einträge. Nur verifizierte Daten.
```

### Regel 5: Fallback planen
- Wenn Agent crasht → Task selbst erledigen (web_search)
- Crash-Quote aktuell ~50% → immer Backup-Plan haben
- Ergebnisse sofort in Datei schreiben (nicht im Kopf behalten)

---

## Template: Researcher-Spawn

```
Task: "[THEMA] Research — Tier-1 Sources Only"

Finde genau 3-5 Tier-1 Quellen zu: [SPEZIFISCHES THEMA]

Akzeptierte Quellen: [LISTE VON 3-5 ORGANISATIONEN]
Nicht akzeptiert: Blog-Posts, Nachrichtenaggregate, Wikipedia

Für JEDE Quelle liefere:
1. Organisation + Publikationsname
2. Erscheinungsjahr
3. Exakter Datenpunkt (Zahl, Prozent, oder Zitat)
4. URL

Format: Nummerierte Liste, max 5 Einträge.
```

---

## Zusammenführung (nach allen Spawns)

1. Alle Ergebnisse in `research/[projekt]-sources-compiled.md` sammeln
2. Deduplizieren (gleiche Quelle von verschiedenen Agents)
3. Qualitäts-Check: Ist die Quelle wirklich Tier-1?
4. In Report einbauen mit konsistentem Format
5. Lücken identifizieren → gezielt nachrecherchieren

---

*Dieses Playbook wird nach jedem Spawn-Versuch aktualisiert.*

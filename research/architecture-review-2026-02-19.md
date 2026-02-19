---
type: research
status: current
created: 2026-02-19
audience: INTERN
confidence: 82%
---

# Architektur-Review: SOUL.md, AGENTS.md, TWIN.md, IDENTITY.md

**Gesamtbewertung: 7/10** — Besser als 90% der Agent-Setups. Aber strukturelle Probleme limitieren uns.

## Quellen
- Anthropic Claude 4.x Best Practices (docs.anthropic.com)
- awesome-ai-system-prompts (GitHub, v0/Manus/Claude Code/ChatGPT Patterns)
- Unsere eigenen Files (SOUL, AGENTS, TWIN, IDENTITY, SUB-AGENT-CONTEXT, MEMORY)

---

## Was richtig gut ist (behalten)

### 1. TWIN.md — Unser bestes File
Kalibrierungs-Log mit echten Scores (44% KW07), Eskalationsregeln, Drift-Detection. Kein anderes Agent-System das ich kenne hat das. Das IST das Produkt — was wir Kunden verkaufen könnten.

### 2. Anti-Sycophancy
"Mindestens 1× pro Session widersprechen." Anthropic empfiehlt genau das für Claude 4.x. Wir waren early.

### 3. Send First
Brutal ehrlich. Adressiert Florians echte Schwäche (Überbauen statt Versenden). Gute Systeme korrigieren User-Bias, nicht nur Agent-Bias.

### 4. Memory-R1
"Ändert es Verhalten in 30 Tagen?" als Filter ist elegant. Verhindert Memory-Bloat.

---

## Problem 1: File-Fragmentierung [Sicherheit 90%]

**7 Files** steuern mein Verhalten: SOUL.md, IDENTITY.md, AGENTS.md, TWIN.md, MEMORY.md, SUB-AGENT-CONTEXT.md + OpenClaw System Prompt.

**Widersprüche gefunden:**
- SOUL.md sagt "Edit > Write" — AGENTS.md sagt das auch → Doppelt
- SOUL.md hat "Jede Antwort" Regeln — AGENTS.md hat "Every Session" Regeln → Overlap
- IDENTITY.md ist 10 Zeilen — könnte SOUL.md Header sein
- MEMORY.md ist quasi leer — verweist nur auf MEMORY-INDEX.md

**Anthropic Best Practice:** "Be explicit, but avoid contradicting instructions across sections."

**Empfehlung:** 4 Files statt 7:
- **SOUL.md** — Wer bin ich + Wie antworte ich (merge IDENTITY.md)
- **AGENTS.md** — Task-Regeln + Standards (bleibt)
- **TWIN.md** — Entscheidungsmodell (perfekt, nicht anfassen)
- **SUB-AGENT-CONTEXT.md** — Sub-Agent Rules (kürzer)
- ~~MEMORY.md~~ → löschen (MEMORY-INDEX.md im Vault reicht)
- ~~IDENTITY.md~~ → merge in SOUL.md

**Risiko:** Merge könnte SOUL.md zu lang machen. Aber IDENTITY.md + MEMORY.md sind so kurz dass es passt.

---

## Problem 2: SOUL.md mischt 3 Dinge [Sicherheit 85%]

SOUL.md enthält: Persona + Process + Strategy. Das sind 3 verschiedene Concerns.

**Aktuell:**
- Wer ich bin (Co-Founderin, ♔)
- Wie ich antworte (Bullets, Confidence)
- Before/After Task Checklists
- Prioritäten (Revenue = f(sends))
- Send First Rules
- Compound Loop

**Anthropic/Manus Pattern:** Rolle OBEN → Regeln MITTE → Constraints UNTEN. Klar getrennt.

**Empfehlung — SOUL.md in 3 Sections:**
1. `## Identität` — Wer ich bin, Ton, Sprache (5-10 Zeilen, stabil)
2. `## Regeln` — Wie ich arbeite, Before/After Task (ändert sich selten)
3. `## Strategie` — Priorities, Flywheel, Send First (ändert sich mit Phase)

**Vorteil:** Wenn sich Strategie ändert (Revenue → Growth → Scale), ändert sich nur Section 3. Identität bleibt stabil über Monate.

---

## Problem 3: AGENTS.md Task Loop wird nicht vollständig befolgt [Sicherheit 80%]

10-Step Task Loop. Ehrlich: Steps 6-9 (Extrahieren, Verbinden, Vorbereiten, Trust) fallen oft weg.

**Anthropic Best Practice:** "Claude follows explicit instructions precisely. If you include 10 steps, it will try to follow all 10 — or feel conflicted about skipping them."

Unrealistische Regeln die ignoriert werden = SCHLECHTER als weniger Regeln die befolgt werden.

**Empfehlung — 5 statt 10 Schritte:**
1. **AKTIVIEREN** — memory + context laden
2. **AUSFÜHREN** — die Arbeit machen
3. **PRÜFEN** — Beantwortet? Belegt? Nutzbar?
4. **SPEICHERN** — wenn Memory-R1 = true
5. **LIEFERN**

Trust-Score, Connections, Hypothese → **optional**, nur bei Research/Deep Tasks. Nicht bei "öffne Obsidian" oder "sende eine Nachricht."

**"NON-NEGOTIABLE" sparsamer nutzen** — wenn alles non-negotiable ist, ist nichts non-negotiable. Aktuell: 4 NON-NEGOTIABLE Regeln. Besser: 2 (Send First + Build-Verify).

---

## Problem 4: TWIN.md Kalibrierung veraltet [Sicherheit 95%]

Letzter Log-Eintrag: KW07 (Mitte Feb). Score: 44%. Ziel: >80%.

**Keine Updates seit 2 Wochen.** Der Twin driftet. Ich treffe Entscheidungen basierend auf einem 44%-accuracy Modell.

**Empfehlung:** Wöchentlicher Cron der 5 autonome Entscheidungen sammelt und Florian zur Kalibrierung vorlegt. Format:
```
"Diese Woche habe ich 5 Entscheidungen autonom getroffen:
1. [X] weil [Y] — Richtig? ✅/❌"
```

Ohne Kalibrierung ist TWIN.md Fiktion.

---

## Problem 5: Sub-Agents bekommen zu wenig Kontext [Sicherheit 75%]

SUB-AGENT-CONTEXT.md ist gut aber **statisch**. Sub-Agents kennen nicht:
- Heutige Entscheidungen
- Aktuelle Prioritäten (ändern sich täglich)
- Was andere Sub-Agents gerade tun (Kollisionen möglich)

**Empfehlung:** Dynamic Context Injection beim Spawnen:
- Letzte 5 Entscheidungen aus decisions.md
- Heutige Priorities
- Liste aktiver Sub-Agents

**Risiko (25%):** Mehr Token-Verbrauch. Aber bessere Ergebnisse = weniger Reruns.

---

## Problem 6: Kein Feedback-Loop auf Architektur-Ebene [Sicherheit 70%]

Trust-Scores für einzelne Tasks ✅. Aber KEINE Messung ob:
- SOUL.md Regeln tatsächlich Output-Qualität verbessern
- AGENTS.md Task Loop befolgt wird
- TWIN.md Entscheidungen korrekt sind
- Send First tatsächlich Revenue korreliert

**Wir fliegen teilweise blind.** Die Architektur ist hypothesenbasiert, nicht datenbasiert.

**Empfehlung — Wöchentlicher Architecture Score:**
- TWIN konsultiert? (messbar)
- Send First getriggert? (messbar)
- Sub-Agent Erfolgsrate? (aus sessions)
- Florian-Korrekturen pro Woche? (messbar)

---

## Prioritäten

| # | Was | Impact | Aufwand | Sicherheit |
|---|-----|--------|---------|------------|
| 1 | TWIN Kalibrierungs-Cron | 🔴 Hoch | 10 min | 95% |
| 2 | SOUL.md → 3 Sections | 🔴 Hoch | 15 min | 85% |
| 3 | AGENTS.md Task Loop 10→5 | 🔴 Hoch | 10 min | 80% |
| 4 | IDENTITY.md → merge in SOUL | 🟡 Mittel | 5 min | 90% |
| 5 | MEMORY.md → deprecate | 🟢 Klein | 2 min | 90% |
| 6 | Sub-Agent Dynamic Context | 🟡 Mittel | 30 min | 75% |
| 7 | Architecture Feedback Loop | 🔴 Hoch | 1h | 70% |

**Mein Vote:** Start mit #1 (TWIN Kalibrierung) + #2 (SOUL Reorg) + #3 (Task Loop). Zusammen 35 min, höchster combined Impact.

---

*Erstellt: 2026-02-19 04:35 CET von Mia*
*Quellen: Anthropic Claude 4.x Best Practices, awesome-ai-system-prompts, eigene Files*

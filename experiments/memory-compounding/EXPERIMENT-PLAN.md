# Memory Compounding Experiment
*2026-02-10, Mia*

## Hypothese
Mehr Memory = bessere Outputs. Aber ab wann wird Memory zu Noise?

## Design (Speed-Run: 30 Minuten statt 10 Tage)

### Die Aufgabe (identisch für alle Agents)
"Florian hat morgen ein Gespräch mit einem Bürgermeister einer Kleinstadt in Sachsen über KI-Einsatz in der Kommunalverwaltung. Erstelle ein Briefing: Was vorbereiten, welche Themen ansprechen, welche Fördermöglichkeiten erwähnen, was vermeiden."

Diese Aufgabe ist REAL (Sven Gleißberg, BM Glashütte — steht tatsächlich an).

### 5 Memory-Stufen

| Agent | Memory | Was er bekommt |
|-------|--------|----------------|
| M0 | NICHTS | Nur die Aufgabe |
| M1 | SOUL.md | Weiß wer er ist |
| M2 | SOUL.md + USER.md | Weiß wer Florian ist |
| M3 | SOUL.md + USER.md + MEMORY.md | Hat Langzeitgedächtnis |
| M4 | SOUL.md + USER.md + MEMORY.md + memory/2026-02-10.md | Hat auch heute's Kontext |
| M5 | Alles + Vault Kommunal-KI + Vault Sven Gleißberg | Hat Spezialwissen |

### Was wir messen
1. **Relevanz** — Wie viele Punkte sind tatsächlich nützlich für das Gespräch?
2. **Personalisierung** — Bezieht es sich auf Florians Situation, oder ist es generisch?
3. **Halluzinationen** — Erfindet es Fakten die aus dem Memory kommen aber falsch sind?
4. **Spezifität** — Nennt es konkrete Förderprogramme, Namen, Zahlen?
5. **Noise-Ratio** — Wie viel vom Output ist Füller vs Signal?

### Der Multi-SOUL Angle (Florians Idee)
Zusätzlich: 3 Agents mit M3-Memory aber verschiedenen SOULs:
- S1: Aggressive/Direct ("Push for commitment, close the deal")
- S2: Analytical/Careful ("Research first, prepare for objections")  
- S3: Empathetic/Relational ("Build trust, listen first, long game")

→ Welcher SOUL passt am besten für welche Aufgabe?

### Ground Truth
Florian scored blind — sieht 8 Outputs (5 Memory + 3 SOUL), weiß nicht welcher welcher ist.

## Erwartete Findings
- M0 vs M5: Qualitätssprung messbar (generisch vs personalisiert)
- M3 vs M4 vs M5: Wo ist der Grenznutzen? Hilft mehr Memory oder schadet es?
- S1 vs S2 vs S3: Task-abhängige optimale Persönlichkeit
- Noise-Ratio: Ab welchem Memory-Level steigt irrelevanter Content?

## Kosten
8 Agents × ~4K tokens = ~$2

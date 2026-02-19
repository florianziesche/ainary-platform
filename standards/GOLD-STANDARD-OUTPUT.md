# Gold Standard Output — "€200K McKinsey Report" (v1.0)

## Was macht einen A+++ Report aus?

### 1. Der Test
Ein VP of Engineering bei einem DAX-Konzern liest den Report.
- Nach 2 Minuten: Weiss er ob es relevant ist? (Executive Summary)
- Nach 10 Minuten: Kann er eine Entscheidung treffen? (Key Takeaways + Recommendations)
- Nach 30 Minuten: Hat er genug Detail für die Umsetzung? (Findings + Phased Plan)
- Nach dem Meeting: Kann er den Report als Entscheidungsgrundlage zitieren? (Sources + Claim Ledger)

### 2. Die 7 Qualitätsmerkmale

| # | Merkmal | Beschreibung | Test |
|---|---------|-------------|------|
| 1 | **"So What" pro Abschnitt** | Jeder Abschnitt endet mit: "Für den Entscheider bedeutet das: ..." | Jeden Abschnitt lesen → gibt es ein "So What"? |
| 2 | **Insight ≠ Information** | Der Opener muss etwas sagen was ein Experte NICHT schon weiß | 3 Domain-Experten fragen: "Wusstet ihr das?" |
| 3 | **Evidence Chain** | Jede Empfehlung ist zurückverfolgbar: [A] ← [E]+[I]+[J] mit [S#] | Claim Ledger: kann man jeden Claim zur Quelle verfolgen? |
| 4 | **Honest Uncertainty** | Confidence ist kalibriert, nicht geschätzt. Schwächen stehen VOR Stärken | Beipackzettel: Risk Level, Uncertainties, Not Checked |
| 5 | **Custom Framework** | Mindestens 1 eigenes Modell/Framework (nicht generische 2x2) | Gibt es ein Diagramm/Modell das NUR in diesem Report existiert? |
| 6 | **Falsifiability** | "Do Not Deploy If" + "What Would Change This Conclusion" | Sind die Bedingungen spezifisch genug um testbar zu sein? |
| 7 | **Monday Morning Action** | Phase 1 der Empfehlung ist in 1 Woche umsetzbar | Kann der Leser am Montag anfangen? |

### 3. Was ein A+++ Report NICHT ist
- ❌ Lang (30-50 Seiten max, nicht 100)
- ❌ Vollständig (lieber 5 tiefe Insights als 20 oberflächliche)
- ❌ Akademisch (kein Jargon, kein "further research needed" ohne Kontext)
- ❌ Neutral (McKinsey hat IMMER eine Empfehlung, nicht "es kommt darauf an")
- ❌ Sicher (ehrliche Unsicherheit > falsche Zuversicht)

### 4. Struktur (30-50 Seiten equivalent, ~8000-12000 Wörter)

```
Page 1:     Beipackzettel (AgentTrust)
            - Confidence, Risk Level, E/I/J/A Distribution
            - Sources count, Grounded: Yes/No

Page 2-3:   Executive Summary (SCR + "So What")
            - Situation (1 paragraph)
            - Complication (1 paragraph) 
            - Resolution (1 paragraph)
            - "If you read nothing else:" (3-5 bullets)

Page 4:     Custom Framework (visual)
            - Das EINE Modell das diesen Report einzigartig macht
            - Zeigt Zusammenhänge die man nicht googlen kann

Page 5-6:   Key Findings (5-7, each with E/I/J/A label)
            - Finding → Evidence [S#] → So What → If Wrong

Page 7-15:  Deep Dives (3-5 Sections)
            - Jeder Abschnitt: Finding → Evidence → Caveat → Implication → So What
            - Case Studies inline (nicht am Ende)
            - Jeder Abschnitt: Section Confidence %

Page 16-18: Recommendations
            - Decision Matrix (scenarios × options)
            - Phased Plan (Week 1 / Month 1 / Quarter 1)
            - "Do Not Deploy If" (5 specific conditions)
            - Cost/Benefit (ranges, not point estimates)

Page 19-20: Risks & "What Would Change This"
            - Top 5 risks with probability × impact
            - Specific triggers that would invalidate conclusions

Appendix:   Source Log + Claim Ledger + Contradiction Register
            - Self-Calibration Results
            - E/I/J/A Distribution Chart
            - Knowledge Writeback JSON
```

## 6-Prompt Pipeline

### Prompt 1: FRAMER (5 min)
**Input:** Topic + Decision Context
**Output:** Research Brief mit der ECHTEN Frage (nicht die offensichtliche)
**Qualitätscheck:** "Würde ein Partner bei McKinsey diese Frage absegnen?"

### Prompt 2: RESEARCHER (10 min)  
**Input:** Research Brief + Reference Library + Papers + Vault Knowledge
**Output:** Source Log + Claim Ledger (raw) + Contradiction Register
**Qualitätscheck:** ">70% der Claims sind E-labeled mit [S#]"

### Prompt 3: SYNTHESIZER (10 min)
**Input:** Source Log + Claims + CRTs + Corrections + Previous Report
**Output:** Findings (E/I/J/A labeled) + Custom Framework + Case Studies
**Qualitätscheck:** "Jeder Abschnitt hat ein 'So What'"

### Prompt 4: CHALLENGER (5 min)
**Input:** Draft Findings + Claim Ledger
**Output:** Challenges + Counter-Arguments + "What Would Change This"
**Qualitätscheck:** "Hat der Challenger etwas gefunden was den Synthesizer überrascht?"

### Prompt 5: WRITER (10 min)
**Input:** Findings + Challenges + Framework
**Output:** Full Report (Executive Summary, Recommendations, Phased Plan)
**Qualitätscheck:** "2-Minuten Test: Kann ein VP nach dem Executive Summary entscheiden?"

### Prompt 6: CALIBRATOR (5 min)
**Input:** Full Report + Claim Ledger + CRTs
**Output:** Beipackzettel + Self-Calibration Results + E/I/J/A Distribution + Reviewer Score
**Qualitätscheck:** "Rubric ≥13/16 für Tier 2, ≥15/16 für Tier 3"

### Total: ~45 min, 6 Prompts, $0 (OAuth) oder ~$0.10 (API)

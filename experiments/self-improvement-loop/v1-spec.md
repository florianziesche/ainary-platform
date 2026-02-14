# Self-Improvement Loop v1
*Created: 2026-02-14 18:16 CET*
*Status: TESTING*

## Konzept
Nach jedem Report: LLM bekommt den fertigen Report + Research und wird gefragt:
"Was würdest DU an unserer Pipeline anders machen, basierend auf dem was du gerade geschrieben/gelesen hast?"

## Pipeline-Step: Post-Report Reflection
**Wann:** Nach QA PASS, vor Builder
**Input:** Research Brief + Fertiger Report + Pipeline-Pack
**Prompt:**
```
Du hast gerade Report [AR-XXX] geschrieben/reviewt.
Basierend auf dem Inhalt:
1. Was bedeutet das für UNSERE Arbeitsweise?
2. Welche Hypothese können wir daraus ableiten?
3. Was sollten wir beim nächsten Report anders machen?
4. Widerspricht etwas in diesem Report wie wir selbst arbeiten?
```
**Output:** 2-3 Hypothesen → `experiments/hypotheses.md`

## Hypothesen-Register
| ID | Aus Report | Hypothese | Status | Ergebnis |
|----|-----------|-----------|--------|----------|
| H-001 | AR-007 | Simple patterns > Frameworks → Pipeline vereinfachen | OPEN | — |
| H-002 | AR-009 | Eigene QA-Scores kalibrieren (sind wir overconfident?) | OPEN | — |
| H-003 | AR-008 | Board-Audience Reports konvertieren besser als CTO-Reports | OPEN | — |

## Test-Plan
- Nächste 3 Reports (AR-010, AR-011, AR-012) mit Reflection-Step
- Messen: Ändert sich die Pipeline-Qualität?
- Vergleich: Reports MIT vs OHNE Reflection

## Changelog
- v1 (2026-02-14): Initial spec

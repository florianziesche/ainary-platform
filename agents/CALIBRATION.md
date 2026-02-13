# Budget-CoCoA Calibration — Sample Consistency für Agent Outputs

## Methode
Statt 1x fragen → 3x dieselbe Kernfrage an den Agent, unabhängig.
Antworten vergleichen → Consistency = echte Confidence.

## Implementierung
1. Agent liefert Output + Beipackzettel (wie bisher)
2. QA extrahiert die 3 wichtigsten Claims aus dem Output
3. Für jeden Claim: 3 unabhängige Checks (gleiche Frage, neuer Agent)
4. Consistency Score:
   - 3/3 stimmen überein → HIGH Confidence (>85%)
   - 2/3 stimmen überein → MEDIUM Confidence (60-85%)
   - 1/3 oder 0/3 → LOW Confidence (<60%)
5. Gesamtscore = Durchschnitt der Claim-Scores

## Wann nutzen
- IMMER bei Tier 2/3 Research
- IMMER bei VC Applications
- IMMER bei Kunden-Emails mit Fakten
- OPTIONAL bei kreativen Outputs (Blog, LinkedIn)

## Kosten
- 3x API-Calls pro Claim = ~9 extra Calls pro Output
- Akzeptabel für wichtige Outputs, Overkill für triviale

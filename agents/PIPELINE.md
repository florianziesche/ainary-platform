# Agent Pipeline — Pflicht-Ablauf für jeden Task

## Phase 1: PLAN (Mia Prime, IMMER)
Bevor irgendein Agent gespawnt wird:
```
## Task Plan
- Was genau soll erreicht werden?
- Wer ist die Audience? (Kunde/VC/Public/Intern/Familie)
- Welcher Ton? (formell/persönlich/technisch)
- Welcher Agent? (oder Ensemble?)
- Welcher Kontext fehlt? (→ RESEARCH zuerst?)
- Welche corrections.md Regeln greifen?
- Was ist beim letzten ähnlichen Task schiefgegangen? (failed-outputs.md)
- Was ist das Risiko? (zu formal? zu pushy? falsche Fakten?)
- Confidence dass Plan stimmt: [0-100]%
```

## Phase 2: RESEARCH (wenn Kontext fehlt)
- RESEARCH Agent sammelt fehlende Infos
- Output = Brief der an den Haupt-Agent übergeben wird
- Überspringen wenn alles in Memory Files steht

## Phase 3: EXECUTE (spezialisierter Agent)
- Agent bekommt: Plan + Research Brief + relevante Memory Files
- Agent liefert: Output + Beipackzettel + Begründungen

## Phase 4: QA (adversarial)
- QA Agent prüft gegen corrections.md + quality-standards.md + failed-outputs.md
- Score 0-100
- Unter 80 → zurück an Agent mit spezifischen Fixes

## Phase 5: ITERATE (max 2 Runden)
- Agent korrigiert basierend auf QA Feedback
- QA prüft erneut
- Nach 2 Runden: An Florian mit ehrlichem Status ("QA sagt 75, hier sind die offenen Punkte")

## Phase 6: DELIVER
- Output + Beipackzettel + QA Score an Florian
- Florians Feedback → Trust Score Update + Agent Memory Update

## Wann Phasen überspringen?
- Triviale Tasks (< 2 Sätze): Nur PLAN + EXECUTE
- Bekannte Tasks (Trust > 60): EXECUTE + QA Spot-Check
- Kritische Tasks (VC App, Kunden-Email): ALLE Phasen, keine Ausnahme

## Hyperthink Mode (für kritische Tasks)
Vor Phase 3, Mia Prime denkt laut:
```
## Hyperthink
1. Was könnte schiefgehen?
2. Was würde Florian kritisieren?
3. Was würde ein Konkurrent besser machen?
4. Was fehlt das nicht offensichtlich ist?
5. Welche Annahme ist am unsichersten?
```
Ergebnis fließt als Briefing in den Agent.

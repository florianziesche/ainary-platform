# Q4: Compounding Quality — Golden Rule

*Stand: 2026-02-27. "Der letzte Report muss immer besser sein als der beste zuvor."*

## Warum das Sinn macht

Jede Verbesserung an einem Dossier muss in das TEMPLATE fließen, nicht nur in die Daten einer Stadt. Das Template IST das Produkt. Eine Verbesserung am Template multipliziert sich über ALLE Städte. Eine Verbesserung nur an einer Stadt ist linear, nicht exponentiell.

**Compounding = Template-Verbesserung × Anzahl Städte**

Beispiel: Quellenverzeichnis-Section im Template gebaut → wirkt auf 9 Städte sofort. Aber nur wenn ALLE Städte auch `quellenverzeichnis`-Daten haben.

## Die Regel (NICHT VERHANDELBAR)

### 1. Template First
Jede neue Feature/Section die für eine Stadt gebaut wird, MUSS:
- In `normalizeCity()` einen Default bekommen
- Im Rendering-Code universell funktionieren
- Für leere Daten sauber degradieren (hide, nicht "0 Items")

### 2. Data Parity
Wenn Stadt A ein neues Datenfeld bekommt, MUSS ein Plan existieren wie ALLE anderen Städte es auch bekommen. Optionen:
- **Automatisch:** normalizeCity() berechnet es (z.B. Risk Score)
- **Research Sprint:** Opus Agent füllt es für alle Städte
- **Graceful Degradation:** Section versteckt sich wenn Daten fehlen

### 3. Quality Ratchet
Score kann nur steigen, nie sinken. Jedes neue Dossier muss mindestens so gut sein wie das beste existierende. Benchmark = die Stadt mit dem höchsten Score.

**Aktueller Benchmark: Nürnberg (nach Q3 Verification)**
- 9 Kandidaten mit vollen Profilen
- 31 Quellen mit URLs im Quellenverzeichnis
- 15 Claim Ledger Einträge
- 5 Contradiction Register Einträge
- Q3 Verification bestanden
- Alle Sources klickbar

### 4. Parity Check (vor jedem Deploy)
```
Frage: Hat die neue Stadt MINDESTENS:
- [ ] So viele Kandidaten wie die Benchmark-Stadt?
- [ ] Quellenverzeichnis mit URLs?
- [ ] Claim Ledger?
- [ ] Q3 Verification bestanden?
- [ ] Individuellen Risk Score (nicht Default 50)?
- [ ] Alle Elemente klickbar?
```

### 5. Improvement Propagation
Wenn eine Verbesserung für Stadt A gemacht wird:
1. **Sofort:** Template-Code ändern (normalizeCity, Rendering)
2. **Batch:** Daten-Schema in DATA-SCHEMA.md updaten
3. **Sprint:** Opus Agents für fehlende Daten in anderen Städten starten
4. **Verify:** Q3 Pipeline für jede aktualisierte Stadt

## Current Parity Matrix

| Feature | NBG | FDB | RGB | BAM | AUG | ERL | FÜR | PAS | LDH |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Q3 Verified | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Quellenverzeichnis | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claim Ledger | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Contradictions | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Risk Score individuell | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| News clickable | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sources clickable | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## Nächste Aktion: Parity Sprint

Ziel: Alle 9 Städte auf Nürnberg-Niveau bringen.
Methode: 1 Opus Agent pro Stadt, sequentiell.
Priorität: Kundenstädte zuerst (Friedberg, Regensburg, Bamberg, Fürth).

## Integration

- **AGENTS.md:** Trigger "Quality, Parity, Compounding" → Q4
- **CITY-PLAYBOOK.md:** Phase 8: Parity Check gegen Benchmark
- **Q3-VERIFICATION-PIPELINE.md:** Vor Verification: Parity Check
- **DATA-SCHEMA.md:** Neue Pflichtfelder: quellenverzeichnis, claim_ledger, contradictions_register

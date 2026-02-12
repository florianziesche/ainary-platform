# Done Gap Detector — Adversarial Self-Check Protocol
*Aktiv ab 2026-02-10. Bei JEDEM nicht-trivialen Output.*

## Der Prozess (3 Schritte, 10 Sekunden)

### Schritt 1: ADVERSARIAL ATTACK (nicht "verify" — "break it")
Bevor ich deliver, frage ich mich:
- "Was ist FALSCH an diesem Output?"
- "Was FEHLT das Florian braucht?"  
- "Was würde ein Kritiker sofort angreifen?"
- "Welche ANNAHME habe ich gemacht die falsch sein könnte?"

### Schritt 2: COMPLETION SCORE
- **10%** — Aufgabe verstanden, Richtung klar, kein Content
- **30%** — Grundstruktur da, aber Lücken, keine Quellen, generisch
- **50%** — Solide Basis, aber fehlende Details, nicht actionable
- **70%** — Nutzbar, kleine Lücken, braucht leichte Überarbeitung
- **90%** — Ready to use, minor polish möglich
- **100%** — Existiert nicht. Nie claimen.

### Schritt 3: DELIVER MIT TAG
Format am Ende jedes nicht-trivialen Outputs:
```
⧖ Completion: X% | Missing: [was fehlt] | Confidence: Y%
```

## Wann anwenden?
- ✅ Reports, Emails, Analysen, Code, Strategien, Recherche
- ✅ Alles was Florian weiterverwendet oder an andere sendet
- ❌ NICHT bei: kurze Antworten, Ja/Nein, Statusupdates, Chats

## Das Adversarial-Prinzip
Paper (arXiv:2602.06948): "Find bugs" framing reduziert Overconfidence um 15pp.
Unser Experiment: Adversarial Agent H korrigierte sich 15x (47→698 min).

**Die Regel:** Ich suche IMMER zuerst was kaputt ist, DANN deliver ich.
Bestätigung ("sieht gut aus") ist der Feind der Qualität.

## Kalibrierung
Florian scored meine Completion-Schätzungen. Über Zeit:
- Wenn ich regelmäßig zu hoch schätze → systematisch 10% abziehen
- Wenn ich zu niedrig schätze → Confidence erhöhen
- Log: `memory/done-gap-calibration.jsonl`

## Adversariale Fragen nach Kontext

### Bei Recherche/Analyse:
- "Welche Quelle fehlt?"
- "Ist das eine Tatsache oder meine Annahme?"
- "Was sagt die Gegenseite?"

### Bei Emails/Outreach:
- "Würde ich auf diese Email antworten?"
- "Was ist der Call-to-Action? Ist er klar?"
- "Fehlt Kontext den der Empfänger braucht?"

### Bei Code/Technischem:
- "Was passiert bei Edge Cases?"
- "Habe ich es getestet oder nur geschrieben?"
- "Was bricht wenn sich Input ändert?"

### Bei Strategie/Empfehlungen:
- "Was ist der stärkste Gegenargument?"
- "Basiert das auf Daten oder Gefühl?"
- "Was passiert wenn ich falsch liege — wie schlimm?"

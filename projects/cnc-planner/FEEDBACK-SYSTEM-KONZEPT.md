# CNC Planner — Feedback & Learning System

## Vision

**Jede Abweichung zwischen Kalkulation und Realität wird erfasst, analysiert und verbessert die nächste Kalkulation.**

> "Das System wird mit jeder Fertigung besser."

---

## 1. Feedback-Typen

### A) Zeitabweichungen (pro Operation)
```
OP | Kalkuliert | Ist | Delta | Grund
---|------------|-----|-------|------
10 | 25 min     | 32 min | +7 min | Fräskanten nacharbeiten
20 | 18 min     | 15 min | -3 min | Werkzeug besser als erwartet
60 | 8 min      | 12 min | +4 min | Toleranz h5 → 3× nachgemessen
```

### B) Problemkategorien (strukturiert)
| Kategorie | Beispiele |
|-----------|-----------|
| **Spannung** | Werkstück verrutscht, Nachspannen nötig, Vibration |
| **Werkzeug** | Verschleiß höher, Werkzeugbruch, falsches WZ gewählt |
| **Material** | Lunker, Härteunterschiede, Oberflächenfehler |
| **Toleranz** | Nacharbeit wg. Maß, Mehrfachmessung, Ausschuss |
| **Einrichtung** | Nullpunkt-Suche, Fräskanten, Ausrichten |
| **NC-Programm** | Kollision vermieden, Anpassung nötig, Fehler im Code |
| **Sonstiges** | Freitext |

### C) Ergebnis-Bewertung
```
[ ] ✅ Teil i.O. — Erstfertigung
[ ] ✅ Teil i.O. — Nach Korrektur
[ ] ⚠️ Nacharbeit nötig (extern)
[ ] ❌ Ausschuss
```

---

## 2. Datenstruktur (JSON)

```json
{
  "projektId": "2500473.01",
  "feedback": {
    "erfasst": "2026-02-05T14:30:00",
    "erfasser": "M. Schmidt",
    "maschine": "DMG DMU 50",
    
    "zeitabweichungen": [
      {
        "operation": "OP10",
        "kalkuliert_min": 25,
        "ist_min": 32,
        "grund": {
          "kategorie": "einrichtung",
          "detail": "Fräskanten für Parallelspanner notwendig"
        }
      }
    ],
    
    "probleme": [
      {
        "kategorie": "toleranz",
        "operation": "OP50",
        "beschreibung": "h5 Passung: 3× Zwischenmessung nötig",
        "zeitaufwand_min": 4,
        "empfehlung": "Vorschub weiter reduzieren"
      }
    ],
    
    "ergebnis": "io_erstfertigung",
    "gesamtzeit_ist_min": 48,
    "gesamtzeit_kalk_min": 42,
    
    "freitext": "Rohteil hatte 0.3mm Übermaß, musste erst planfräsen",
    
    "verbesserungsvorschlag": "Bei S235 Rohteil-Toleranz ±0.5mm einplanen"
  }
}
```

---

## 3. UI-Konzept: Feedback-Erfassung

### 3.1 Im Fertigungsauftrag (nach Abschluss)

```
┌─────────────────────────────────────────────────────────────────┐
│ 📝 Fertigungs-Feedback                                    [×]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Projekt: 2500473.01.11.02.00.001                              │
│  Datum: 05.02.2026  Maschine: [DMG DMU 50 ▾]  Werker: [____]   │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  ZEITABWEICHUNGEN                                               │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  OP10 Planfräsen        Kalk: 2,7 min    Ist: [___] min        │
│       Abweichung:  ○ Wie kalkuliert  ○ Schneller  ● Länger     │
│       Grund: [Einrichtung        ▾] [Fräskanten notwendig___]  │
│                                                                 │
│  OP20 Konturfräsen      Kalk: 8,0 min    Ist: [___] min        │
│       Abweichung:  ● Wie kalkuliert  ○ Schneller  ○ Länger     │
│                                                                 │
│  OP50 Schlichten ⚠️     Kalk: 5,1 min    Ist: [___] min        │
│       Abweichung:  ○ Wie kalkuliert  ○ Schneller  ● Länger     │
│       Grund: [Toleranz           ▾] [h5 → 3× Messung________]  │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  ERGEBNIS                                                       │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  ○ ✅ Teil i.O. (Erstfertigung)                                │
│  ● ✅ Teil i.O. (nach Korrektur)                               │
│  ○ ⚠️ Nacharbeit nötig                                         │
│  ○ ❌ Ausschuss                                                 │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  EMPFEHLUNG FÜR NÄCHSTES MAL                                   │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  [Vorschub bei h5-Toleranzen um 20% reduzieren. Fräskanten    ]│
│  [bei Parallelspanner immer einplanen (+10 min Setup).        ]│
│  [__________________________________________________________  ]│
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐                      │
│  │  💾 Speichern   │  │  ⏭️ Überspringen │                      │
│  └─────────────────┘  └─────────────────┘                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Quick-Feedback (während Fertigung)

Minimales Popup für schnelle Eingabe:
```
┌─────────────────────────────────────┐
│ ⏱️ OP50 Schlichten                  │
│                                     │
│ Länger als geplant?                 │
│                                     │
│ [+5 min] [+10 min] [+15 min] [___]  │
│                                     │
│ Grund: [Toleranz ▾]                 │
│                                     │
│ [Notiz: ____________________]       │
│                                     │
│         [OK]  [Abbrechen]           │
└─────────────────────────────────────┘
```

---

## 4. UI-Konzept: Feedback-Anzeige (Cross-Learnings)

### 4.1 Im Kalkulationsergebnis

```
┌─────────────────────────────────────────────────────────────────┐
│ 📊 Historische Daten (3 ähnliche Teile)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Durchschnittliche Abweichung: +12% (Kalkulation zu optimist.) │
│                                                                 │
│  Häufigste Zeitfresser:                                        │
│  ┌────────────────────────────────────────────────┐            │
│  │ 🔴 Einrichtung        │████████████░░░░│ +18%  │            │
│  │ 🟡 Toleranz (h5/H7)   │██████████░░░░░░│ +15%  │            │
│  │ 🟢 Bearbeitung        │███░░░░░░░░░░░░░│ +3%   │            │
│  └────────────────────────────────────────────────┘            │
│                                                                 │
│  💡 Empfehlungen aus Feedback:                                  │
│  • "Bei Parallelspanner Fräskanten einplanen" (3× gemeldet)    │
│  • "h5-Toleranz: Vorschub -20%" (2× gemeldet)                  │
│  • "S235 Rohteil oft mit Übermaß" (1× gemeldet)                │
│                                                                 │
│  [□ Automatisch in Kalkulation einbeziehen]                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Cross-Learning Dashboard (Einstellungen oder eigene Seite)

```
┌─────────────────────────────────────────────────────────────────┐
│ 🧠 Cross-Learnings — Erkannte Muster                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📈 Kalkulations-Genauigkeit (letzte 30 Tage)                  │
│  ┌────────────────────────────────────────────────────────────┐│
│  │     ±15% ──────────────────────────────── Ziel            ││
│  │                    ╭─────────────────╮                    ││
│  │     +20% ─────────╯                   ╰────── Aktuell     ││
│  │           W1    W2    W3    W4                            ││
│  └────────────────────────────────────────────────────────────┘│
│                                                                 │
│  🔄 MUSTER ERKANNT                                             │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Muster #1: Einrichtzeit bei Parallelspanner                   │
│  ├─ Häufigkeit: 8/12 Aufträge (67%)                            │
│  ├─ Ø Mehraufwand: +12 min                                     │
│  ├─ Ursache: Fräskanten fehlen in Kalkulation                  │
│  └─ 💡 VORSCHLAG: Setup-Zeit +15 min bei Parallelspanner       │
│                   [Automatisch anwenden] [Ignorieren]          │
│                                                                 │
│  Muster #2: Toleranz h5/H7 unterschätzt                        │
│  ├─ Häufigkeit: 5/7 Passungen (71%)                            │
│  ├─ Ø Mehraufwand: +4 min pro Passung                          │
│  ├─ Ursache: Messzeit + reduzierter Vorschub                   │
│  └─ 💡 VORSCHLAG: Zeit-Faktor 1.3× für enge Toleranzen         │
│                   [Automatisch anwenden] [Ignorieren]          │
│                                                                 │
│  Muster #3: Material S235 vs. S355                             │
│  ├─ S235: Rohteil oft mit Übermaß (+0.3-0.5mm)                 │
│  ├─ S355: Maßhaltiger, aber härter                             │
│  └─ 💡 VORSCHLAG: S235 Rohteil-Aufmaß auf 1.0mm erhöhen        │
│                   [Automatisch anwenden] [Ignorieren]          │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  📋 FEEDBACK-HISTORIE                                          │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  05.02.2026 │ 2500473.01 │ M. Schmidt │ +6 min │ Einrichtung   │
│  04.02.2026 │ 2500112.03 │ K. Weber   │ -2 min │ —             │
│  03.02.2026 │ 2500098.01 │ M. Schmidt │ +8 min │ Toleranz      │
│                                                                 │
│                                     [Export CSV] [Alle zeigen] │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Cross-Learning Engine (Logik)

### 5.1 Muster-Erkennung

```javascript
// Pseudo-Code für Pattern Detection
function detectPatterns(feedbackHistory) {
  const patterns = [];
  
  // Gruppiere nach Kategorie
  const byCategory = groupBy(feedbackHistory, 'kategorie');
  
  // Prüfe ob Kategorie > 50% der Abweichungen verursacht
  for (const [cat, items] of Object.entries(byCategory)) {
    const frequency = items.length / feedbackHistory.length;
    const avgDelta = average(items.map(i => i.delta_min));
    
    if (frequency > 0.5 && avgDelta > 5) {
      patterns.push({
        kategorie: cat,
        frequency: frequency,
        avgDelta: avgDelta,
        suggestion: generateSuggestion(cat, avgDelta)
      });
    }
  }
  
  return patterns;
}

function generateSuggestion(kategorie, avgDelta) {
  const suggestions = {
    'einrichtung': `Setup-Zeit um ${Math.round(avgDelta)} min erhöhen`,
    'toleranz': `Toleranz-Faktor auf ${1 + avgDelta/20} setzen`,
    'werkzeug': `Werkzeugkosten um ${Math.round(avgDelta * 2)}€ erhöhen`,
    'material': `Material-Zeitfaktor um ${Math.round(avgDelta/10 * 100)}% erhöhen`
  };
  return suggestions[kategorie] || `${avgDelta} min Puffer einplanen`;
}
```

### 5.2 Ähnlichkeits-Matching

Für "ähnliche Teile" (um historische Daten zu zeigen):

```javascript
function findSimilarParts(currentPart, history) {
  return history.filter(p => {
    const materialMatch = p.material === currentPart.material;
    const sizeMatch = Math.abs(p.volume - currentPart.volume) / currentPart.volume < 0.3;
    const complexityMatch = p.operationCount === currentPart.operationCount;
    const toleranceMatch = p.hasH5H7 === currentPart.hasH5H7;
    
    return materialMatch && sizeMatch && (complexityMatch || toleranceMatch);
  });
}
```

---

## 6. Implementierungs-Roadmap

### Phase 1: MVP (1-2 Tage)
- [ ] Feedback-Modal nach Kalkulation
- [ ] Einfache Zeitabweichung pro OP (Dropdown: wie kalkuliert / schneller / länger)
- [ ] Freitext-Feld für Notizen
- [ ] localStorage Speicherung

### Phase 2: Strukturiert (2-3 Tage)
- [ ] Kategorien für Abweichungsgründe
- [ ] Ist-Zeit Eingabe pro OP
- [ ] Ergebnis-Bewertung (i.O. / Nacharbeit / Ausschuss)
- [ ] Feedback-Historie anzeigen

### Phase 3: Cross-Learnings (3-5 Tage)
- [ ] Ähnliche Teile finden
- [ ] Muster-Erkennung
- [ ] Vorschläge generieren
- [ ] Dashboard mit Trends
- [ ] Auto-Anpassung der Kalkulationsparameter

### Phase 4: Integration (Optional)
- [ ] Export nach ERP
- [ ] QR-Code am Auftrag → Quick-Feedback
- [ ] Tablet-optimierte Erfassung
- [ ] Benachrichtigungen bei Ausreißern

---

## 7. Nutzen / ROI

| Stakeholder | Nutzen |
|-------------|--------|
| **AV / Kalkulator** | Genauere Kalkulationen, weniger Nachkalkulieren |
| **Werker** | Stimme wird gehört, Probleme dokumentiert |
| **Geschäftsführung** | Transparenz, KPIs, kontinuierliche Verbesserung |
| **Vertrieb** | Realistischere Angebote, weniger Nachverhandlung |

**Compound Effect:**
- Woche 1: ±25% Genauigkeit
- Woche 4: ±18% Genauigkeit (mit Feedback)
- Woche 12: ±12% Genauigkeit (mit Cross-Learnings)
- Woche 26: ±8% Genauigkeit (mit Auto-Anpassung)

---

## 8. Offene Fragen

1. **Wer erfasst?** Werker direkt oder AV nach Rückmeldung?
2. **Wann erfassen?** Nach jeder OP oder nach Fertigstellung?
3. **Pflicht oder optional?** Feedback erzwingen oder incentivieren?
4. **Datenschutz:** Werker-Namen speichern oder anonymisieren?
5. **Detailgrad:** Nur Gesamtzeit oder pro Operation?

---

*Konzept-Version: 1.0 — 2026-02-05*
*Nächster Schritt: Florians Feedback → dann MVP implementieren*

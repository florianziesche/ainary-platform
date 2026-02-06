# V18 - Fertig für Demo morgen (Onkel)

**STATUS:** Florian hat Teile vom Onkel → Ergebnis morgen erwartet → Schnellerer Revenue möglich

**File:** `demo-v18-fertig.html` (basierend auf v17-complete.html)

---

## Änderungen FERTIGUNGSANWEISUNG Tab:

### ✂️ ENTFERNEN:

1. **"Zeichnung ablegen" Button** (rechts oben in Drawing Card)
   - Nur Zeichnung anzeigen, kein Upload-Button mehr

2. **"Arbeitsschritte" Section komplett löschen**
   - Alle OP10-OP60 Detail-Cards mit:
     - params-grid (Werkzeug, Drehzahl, Vorschub, Zustellung)
     - tips-list
     - instruction-content
   - **ABER:** Parameter VORHER in Operations-Tabelle übertragen!

3. **Doppelte "Zeichnung" und "Operationen" darunter**
   - Die zweite Drawing Card löschen
   - Die zweite Operations-Tabelle löschen

4. **Ab "Berechnungsformel..." alles ausschneiden**
   - Info-Box mit Formeln
   - 2-Spalten Grid (Maschine + Material)
   - Zuschlagskalkulation
   - Alles bis Ende Section
   - → Wird in KALKULATION Tab eingefügt

---

### ➕ ERWEITERN:

**Operations-Tabelle (die aufklappbaren Zeilen):**

Aktuell:
```
OP | Beschreibung | Werkzeug | Zeit
```

Neu:
```
OP | Beschreibung | Werkzeug | Drehzahl | Vorschub | Zustellung | Zeit
```

**Daten aus "Arbeitsschritte" übernehmen:**
- OP10: T1 Ø63, 800 U/min, 300 mm/min, 2mm
- OP20: T4 Ø18, 1400 U/min, 450 mm/min, 4mm
- OP30: T6 Ø8, 2200 U/min, 520 mm/min, —
- OP40: T2 Ø20, 1200 U/min, 480 mm/min, 1,5mm
- OP50: T3 Ø16, 1600 U/min, 557 mm/min (red. 280), 0,3mm
- OP60: T11, 1100 U/min, 98 mm/min, —
- OP70: T12, 900 U/min, 75 mm/min, —
- OP80: T5 Ø6,8, 1800 U/min, 320 mm/min, —
- OP90: T13, 1500 U/min, 250 mm/min, —

---

### ✅ BEHALTEN:

1. **Zeichnung Card** (ohne "ablegen" Button)
2. **Operations-Tabelle** (erweitert mit Parametern)
3. **Qualitätsprüfung Section**

---

## Änderungen KALKULATION Tab:

### ➕ EINFÜGEN (am Anfang nach Opening-Card):

**Von FERTIGUNGSANWEISUNG verschieben:**

1. **Info-Box Berechnungsformeln:**
```html
<div class="info-box" style="margin-bottom: var(--space-5);">
    <strong>Berechnungsformel:</strong> t<sub>h</sub> = Verfahrweg L [mm] ÷ Vorschub v<sub>f</sub> [mm/min]
    <strong>Nebenzeit:</strong> Werkzeugwechsel + Positionieren + Zustellung + Späne entfernen
</div>
```

2. **Komplette 2-Spalten Grid:**
   - Maschinenzeitkalkulation Card
   - Materialkalkulation Card
   - Zuschlagskalkulation Card
   - Gesamtkalkulation Card

---

## Ergebnis:

### FERTIGUNGSANWEISUNG (Clean):
```
┌─ Zeichnung Card ─────────────────┐
│ [Drawing preview]                │
└──────────────────────────────────┘

┌─ Operationen und Bearbeitungszeiten ─────────────────────────┐
│ OP | Beschreibung | Werkzeug | n | vf | ap | Zeit          │
│ 10 | Planfräsen   | T1 Ø63   | 800 | 300 | 2mm | 2,7 min  │
│ ... [aufklappbar mit Details]                                │
│ SUMME: th=31,2 | tn=8,0 | 44,2 min                          │
└──────────────────────────────────────────────────────────────┘

┌─ Qualitätsprüfung ───────────────┐
│ - Toleranzen prüfen (h5, H7)     │
│ - Oberfläche kontrollieren       │
└──────────────────────────────────┘
```

### KALKULATION (Komplett):
```
┌─ Berechnungsformeln ─────────────┐
│ th = L ÷ vf | tn = WZ + Pos + ...│
└──────────────────────────────────┘

┌─ Maschinenzeitkalkulation ─┬─ Materialkalkulation ──┐
│ th = 31,2 min               │ Rohmaße: 130×130×47    │
│ tn = 8,0 min                │ Gewicht: 6,23 kg       │
│ Gesamt = 39,2 min           │ Material: €46,62       │
│ × €91/h = €59,47            │                        │
└─────────────────────────────┴────────────────────────┘

┌─ Zuschlagskalkulation ──────────────────────────────┐
│ MGK 10%, AV 8%, VwGK 12%, VtGK 5%, Gewinn 10%       │
└─────────────────────────────────────────────────────┘

┌─ GESAMTKALKULATION ────────────────────────────────┐
│ Endpreis: €184,32                                  │
└────────────────────────────────────────────────────┘
```

---

## Nächste Schritte (Morgen 06:00):

1. ✅ Diese Änderungen in v18 umsetzen
2. ✅ Im Browser testen (alle Tabs)
3. ✅ Mit echten Onkel-Teilen durchspielen
4. ✅ Demo bei Onkel → Feedback → Revenue!

---

**Ziel:** Professional, clean, alle Infos da aber klar strukturiert.
**Prinzip:** Fertigungsanweisung = Produktion (Was machen?), Kalkulation = Zahlen (Was kostet?)

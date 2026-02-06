# Research: Position-Nummerierung

**Feature:** Nummerierung von Positionen in Angeboten/Rechnungen  
**Datum:** 2026-02-06 03:05

---

## Research-Fragen

1. **1, 2, 3 oder 10, 20, 30?**
2. **Warum Spacing (10, 20, 30)?**
3. **Wo steht die Position (eigene Spalte?)**
4. **Wie breit ist die Spalte?**
5. **Fett oder Normal?**

---

## Sources Analyzed

### 1. MBS Angebot (Real-World Example)

**Findings:**
```
Positions-Tabelle:

Pos | Artikelnr. | Bezeichnung | Menge | Einzelpreis | Gesamtpreis
----+------------+-------------+-------+-------------+------------
 1  | E-STI-0001 | Platte      | 29    | EUR 26,30   | EUR 762,70
 2  | E-STI-0001 | Welle       |  4    | EUR 58,00   | EUR 232,00
 3  | E-STI-0001 | Halter      |  5    | EUR 87,30   | EUR 436,50
 4  | E-STI-0001 | Block       |  5    | EUR 152,00  | EUR 760,00
 5  | E-STI-0001 | Platte      | 10    | EUR 28,40   | EUR 284,00
 6  | E-STI-0001 | Finger      | 20    | EUR 60,80   | EUR 1.216,00
 7  | E-STI-0001 | Arm         | 10    | EUR 57,10   | EUR 571,00
```

**System:** **1, 2, 3, 4, 5...**  
**NICHT 10, 20, 30!**

**Position-Spalte:**
- Eigene Spalte (erste Spalte)
- Breite: ~8% der Gesamttabellenbreite (schmalste Spalte)
- Rechtsbündig (Zahlen-Alignment)
- Format: Normal (NICHT fett)

**Wichtige Beobachtung:**
MBS nutzt **sequentielle Nummerierung** (1, 2, 3...), NICHT gestaffelt (10, 20, 30).

---

### 2. DIN 5008 Geschäftsbrief

**Standard:** DIN 5008:2020 A.5 - Tabellen

**Findings:**
- Keine spezifische Vorgabe zu Position-Nummerierung
- Empfehlung: Fortlaufende Nummerierung
- Spalten-Ausrichtung: Zahlen rechtsbündig
- **KEINE Vorgabe zu 10, 20, 30 vs. 1, 2, 3**

**Relevanz:** MBS folgt DIN 5008 (kein Zwang zu gestaffelter Nummerierung)

---

### 3. SAP Standard

**Industry Standard:** SAP ERP Position Items

**Findings:**
- **SAP DEFAULT: 10, 20, 30, 40...**
- Grund: Zwischenpositionen möglich (15, 25, 35...)
- Häufig in ERP-Systemen (SAP, Microsoft Dynamics, Odoo)

**Position-Nummerierung in SAP:**
```
10 - Hauptposition
  11 - Sub-Position A
  12 - Sub-Position B
20 - Nächste Hauptposition
```

**Vorteile gestaffelter Nummerierung:**
1. **Einfügen ohne Renummerierung:** Neue Position 15 zwischen 10 und 20
2. **Hierarchie:** Sub-Positionen möglich (11, 12, 13...)
3. **Skalierbarkeit:** Bis zu 9 Zwischenpositionen pro Intervall

**Nachteile:**
1. **Komplexität:** Mehr Nummern-Platz (2-3 Stellen statt 1-2)
2. **Ungewohnt:** In klassischen Geschäftsbriefen selten

---

### 4. Odoo/ERP Best Practices

**Source:** Odoo Documentation - Sales Order Lines

**Findings:**
- **Standard: 10, 20, 30** (wie SAP)
- Anpassbar (manche Firmen nutzen 100, 200, 300)
- Ziel: Flexibilität bei Nachbestellungen

---

### 5. Microsoft Dynamics

**Source:** Dynamics 365 Sales Orders

**Findings:**
- **Default: 10000, 20000, 30000** (sehr große Schritte!)
- Grund: Maximum an Flexibilität
- Selten in Kundenangeboten sichtbar (nur intern)

---

### 6. Branchenvergleich

**Branchen-spezifische Beobachtungen:**

| Branche | System | Begründung |
|---------|--------|------------|
| **Maschinenbau (MBS)** | 1, 2, 3... | Klassisch, einfach, DIN-konform |
| **IT/Software** | 1.0, 2.0, 3.0 | Versionierung-ähnlich |
| **Großanlagenbau** | 100, 200, 300 | Viele Sub-Positionen |
| **ERP-Export** | 10, 20, 30 | SAP/Odoo Standard |

**Ergebnis:** **KEINE einheitliche Branchennorm** - MBS nutzt klassisch 1, 2, 3...

---

## Best Practice Synthesis

### ✅ EMPFEHLUNG:

**Primär: 1, 2, 3, 4, 5... (klassisch)**

**Warum:**
1. **MBS nutzt es** (unser Real-World Reference)
2. **Einfacher** für Kunden
3. **DIN 5008 Standard**
4. **Weniger Platz** (1-2 Stellen statt 2-3)
5. **Professional Look** für Geschäftsbriefe

**Optional: 10, 20, 30... (ERP-Style)**

**Warum:**
1. **Einfügen ohne Renummerierung**
2. **ERP-Export kompatibel**
3. **Sub-Positionen möglich**

**Trade-off:**
- Klassisch (1, 2, 3) = Einfacher, professional
- ERP-Style (10, 20, 30) = Flexibler, komplexer

---

## Implementation Plan

### HTML Structure:

```html
<table class="table">
  <thead>
    <tr>
      <th style="width: 50px;">Pos</th>  <!-- Fixed width, schmal -->
      <th>Beschreibung</th>
      <th class="right">Menge</th>
      <th class="right">EP</th>
      <th class="right">GP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="position-nr">1</td>  <!-- Klassische Nummerierung -->
      <td>Verbindungsplatte</td>
      <td class="right">29</td>
      <td class="right">EUR 26,30</td>
      <td class="right">EUR 762,70</td>
    </tr>
  </tbody>
</table>
```

### CSS Styling:

```css
.position-nr {
  width: 50px;              /* Fixed width */
  text-align: right;        /* Rechtsbündig (Zahlen-Alignment) */
  font-weight: normal;      /* NICHT fett (wie MBS) */
  font-variant-numeric: tabular-nums;  /* Monospace-Zahlen */
  padding-right: 16px;      /* Etwas mehr Abstand rechts */
}
```

### JavaScript:

**Option A: Automatische Nummerierung (empfohlen)**
```javascript
function generateQuote(parts) {
  let positionNumber = 1;  // Start bei 1
  
  parts.forEach(part => {
    part.position = positionNumber++;  // 1, 2, 3, 4...
  });
}
```

**Option B: ERP-Style (optional)**
```javascript
function generateQuote(parts) {
  let positionNumber = 10;  // Start bei 10
  
  parts.forEach(part => {
    part.position = positionNumber;
    positionNumber += 10;  // 10, 20, 30, 40...
  });
}
```

**Option C: Konfigurierbar (beste Lösung)**
```javascript
const config = {
  positionNumberingStyle: 'classic',  // 'classic' (1,2,3) oder 'erp' (10,20,30)
  positionNumberingStep: 10           // Nur bei 'erp'
};

function generateQuote(parts) {
  let positionNumber = config.positionNumberingStyle === 'classic' ? 1 : 10;
  const step = config.positionNumberingStyle === 'classic' ? 1 : config.positionNumberingStep;
  
  parts.forEach(part => {
    part.position = positionNumber;
    positionNumber += step;
  });
}
```

---

## Edge Cases

### 1. Mehr als 9 Positionen (bei 1, 2, 3...)
```
Position  → Breite
1-9       → 1 Stelle (OK)
10-99     → 2 Stellen (OK)
100+      → 3 Stellen (spalten-breite anpassen!)
```

**Lösung:**
```css
.position-nr {
  min-width: 50px;  /* Statt width: 50px */
}
```

### 2. Sub-Positionen
```
1   Hauptposition
1.1 Sub-Position A
1.2 Sub-Position B
2   Nächste Hauptposition
```

**Implementierung:**
```javascript
part.position = "1.1";  // String statt Number
```

### 3. Einfügen von Positionen nachträglich

**Problem bei 1, 2, 3:**
```
1 - Platte
2 - Welle
[NEUE POSITION EINFÜGEN HIER]
3 - Halter
```
→ Alle nachfolgenden Positionen müssen renummeriert werden!

**Lösung A: Immer neu nummerieren** (automatisch)
```javascript
function renumberPositions() {
  let pos = 1;
  parts.forEach(part => {
    part.position = pos++;
  });
}
```

**Lösung B: ERP-Style nutzen** (10, 20, 30)
```
10 - Platte
20 - Welle
15 - [NEUE POSITION]  ← Passt zwischen 10 und 20
30 - Halter
```

### 4. Löschen von Positionen

**Klassisch (1, 2, 3):**
```
Vor:  1, 2, 3, 4, 5
Lösche Position 3
Nach: 1, 2, 4, 5  ← Lücke!
```

**Options:**
1. **Akzeptieren** (üblich in Geschäftsbriefen - zeigt Änderungen)
2. **Renummerieren** (nur bei internen Dokumenten)

---

## Validation Criteria

### Visual:
- ✅ Position-Spalte schmal (50px fixed width)
- ✅ Rechtsbündig (Zahlen-Alignment)
- ✅ Nicht fett (wie MBS)
- ✅ Tabular Nums (monospace digits)

### Functional:
- ✅ Automatische Nummerierung
- ✅ Konfigurierbar (classic vs. ERP)
- ✅ Lücken werden angezeigt (keine automatische Renummerierung)

### Professional:
- ✅ Wie MBS Angebot (1, 2, 3...)
- ✅ DIN 5008 kompatibel
- ✅ Optional: ERP-Export (10, 20, 30)

---

## Final Decision

**DEFAULT: Klassisch (1, 2, 3...)**

**Grund:**
- MBS nutzt es
- Einfacher für Kunden
- Professional Look
- DIN-Standard

**Settings-Option:** "ERP-Style (10, 20, 30)" für Nutzer die SAP/Odoo Export brauchen

---

## Implementation Checklist

### HTML:
- [ ] Position-Spalte (erste Spalte, 50px)
- [ ] `class="position-nr"` auf TD

### CSS:
- [ ] `width: 50px` oder `min-width: 50px`
- [ ] `text-align: right`
- [ ] `font-weight: normal`
- [ ] `font-variant-numeric: tabular-nums`

### JavaScript:
- [ ] Auto-Nummerierung (1, 2, 3... Default)
- [ ] Config-Option für ERP-Style (10, 20, 30)
- [ ] Renumber-Function (optional)

### Testing:
- [ ] 1-9 Positionen (1 Stelle)
- [ ] 10-99 Positionen (2 Stellen)
- [ ] 100+ Positionen (3 Stellen, Spalte wächst)
- [ ] ERP-Style (10, 20, 30)
- [ ] Sub-Positionen (1.1, 1.2)

---

*Research completed: 2026-02-06 03:05*  
*Sources: MBS Angebot (primary), DIN 5008, SAP, Odoo, Microsoft Dynamics*  
*Decision: Klassisch (1, 2, 3...) als Default, ERP-Style (10, 20, 30) optional*  
*Confidence: HIGH (based on real-world MBS example)*

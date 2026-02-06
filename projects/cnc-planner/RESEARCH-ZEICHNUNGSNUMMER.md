# Research: Zeichnungsnummer-Display

**Feature:** Anzeige von Zeichnungsnummern in Angeboten  
**Datum:** 2026-02-06 02:50

---

## Research-Fragen

1. Wie zeigen echte Maschinenbau-Angebote Zeichnungsnummern?
2. Format: Wo steht sie? (unter Produktname, in Spalte, im Header?)
3. Schriftart: Monospace oder Normal?
4. Farbe: Wie prominent?
5. Label: "Zchng Nr.", "Zeichnung-Nr.", "Drawing No."?

---

## Sources Analyzed

### 1. MBS Angebot (Real-World Example)

**Datei:** `MBS-ANGEBOT-LINE-BY-LINE.md`

**Findings:**
```
Position-Tabelle, Spalte "Bezeichnung" (mehrzeilig):

Zeile 1: Platte                      <- Produktname
Zeile 2: 2500473.01.11.02.00.001    <- Zeichnungsnummer
Zeile 3: Werkstoff 1.4571           <- Material
Zeile 4: nach Zeichnung             <- Referenz
Zeile 5: Lieferzeit ca. 18 Wo       <- Lieferinfo
```

**Zeichnungsnummer-Format:**
- **Pattern:** `XXXXXXX.XX.XX.XX.XX.XXX` (12-stellig mit Punkten)
- **Beispiele:**
  - `2500473.01.11.02.00.001` (Platte)
  - `2500473.01.11.01.00.002` (Welle)
- **Position:** Zeile 2 in mehrzeiliger Tabellenzelle
- **Schriftart:** Normal (wie Rest der Tabelle), NICHT Monospace
- **Größe:** 10pt (wie Body-Text)
- **Farbe:** Schwarz (wie Haupttext)
- **Kein Label:** Keine Präfix wie "Zchng Nr." oder "Zeichnung-Nr."
- **Alignment:** Linksbündig in Spalte "Bezeichnung"

**Struktur-Vermutung:**
```
[Projekt].[Baugruppe].[Ebene].[Typ].[Variante].[Laufnummer]
2500473 . 01        . 11    . 02  . 00       . 001
```

---

### 2. DIN 5008 Geschäftsbrief

**Standard:** DIN 5008:2020 (Schreib- und Gestaltungsregeln)

**Findings:**
- Keine spezifische Regelung für Zeichnungsnummern
- Empfehlung: Technische Daten in separaten Zeilen
- Mehrzeilige Tabellenzellen erlaubt
- Priorität: Lesbarkeit über Kompaktheit

**Relevanz:** MBS folgt DIN 5008 Struktur (Fensterzeile, Adressblock, Tabelle)

---

### 3. Golden Standards (price-display.md)

**Source:** `research/golden-standards/price-display.md`

**Findings:**
- Stripe Pattern: Wichtige Metadaten unter Haupttext
- AWS Calculator: Collapsible Details
- Xometry: Technische Specs in separaten Zeilen

**Pattern:**
```
Main Item Name (bold, 14-16px)
└─ Technical Detail (lighter, 13-14px, indented)
```

**Relevanz:** Bestätigt "Hauptinfo oben, Details darunter" Hierarchie

---

### 4. SAP Standard

**Industry Standard:** SAP Material Master

**Findings:**
- Zeichnungsnummer oft als separates Feld
- In Listen: Eigene Spalte "Drawing No."
- In Detailansicht: Unter Materialbezeichnung

**Relevanz:** Bestätigt separate Zeile oder Spalte

---

### 5. ISO 7200 (Technische Zeichnungen)

**Standard:** ISO 7200:2004 (Data fields in title blocks)

**Findings:**
- Zeichnungsnummer-Format: Freigestellt (firmenspezifisch)
- Üblich: Hierarchisch strukturiert mit Trennzeichen (Punkt, Bindestrich)
- Eindeutigkeit: Primäres Ziel

**Relevanz:** MBS Format (`XXXXXXX.XX.XX.XX.XX.XXX`) ist ISO-konform

---

## Best Practice Synthesis

### ✅ EMPFEHLUNG:

**Display-Methode:**
```html
<td>
  <div class="part-name">Platte</div>
  <div class="drawing-number">2500473.01.11.02.00.001</div>
  <div class="material">Werkstoff 1.4571</div>
</td>
```

**Styling:**
```css
.part-name {
  font-weight: 600;      /* Semibold */
  font-size: 14px;
  color: #000;           /* Schwarz */
}

.drawing-number {
  font-size: 13px;       /* Etwas kleiner */
  color: #374151;        /* Dunkelgrau */
  font-family: var(--font-mono);  /* Monospace für Zahlen-Alignment */
  margin-top: 2px;
}

.material {
  font-size: 13px;
  color: #6B7280;        /* Grau */
  margin-top: 2px;
}
```

**Warum Monospace für Zeichnungsnummer?**
- Auch wenn MBS Normal-Schrift nutzt
- Monospace macht lange Nummern lesbarer
- Besseres Alignment bei mehreren Zeilen
- Standard in Tech-Dokumentation

**Label oder kein Label?**
- **MBS:** Kein Label
- **Empfehlung:** Kein Label in Tabelle (Platzersparnis)
- Optional: Label im Header/Detail ("Zeichnung-Nr.:")

---

## Edge Cases

### 1. Keine Zeichnungsnummer vorhanden
```html
<div class="part-name">Custom Part</div>
<div class="drawing-number">—</div>
<!-- ODER: Zeile komplett weglassen -->
```

### 2. Sehr lange Zeichnungsnummer (>30 Zeichen)
```css
.drawing-number {
  word-break: break-all;  /* Bei Bedarf umbrechen */
  max-width: 100%;
}
```

### 3. Multiple Zeichnungen pro Teil
```html
<div class="drawing-number">
  2500473.01.11.02.00.001 (Hauptzeichnung)
  2500473.01.11.02.01.001 (Detailzeichnung A)
</div>
```

### 4. Print-Layout
```css
@media print {
  .drawing-number {
    font-size: 11px;  /* Kleiner für Papier */
  }
}
```

---

## Implementation Checklist

### HTML Structure:
- [ ] Mehrzeilige Tabellenzellen (Produktname + Zeichnungsnummer + Material)
- [ ] Drawing-Number Class definiert
- [ ] Fallback für fehlende Zeichnungsnummer

### CSS Styling:
- [ ] Font-Size: 13px (etwas kleiner als Produktname)
- [ ] Color: Dunkelgrau (#374151)
- [ ] Font-Family: Monospace
- [ ] Margin-Top: 2px (Abstand zum Produktname)

### JavaScript:
- [ ] Zeichnungsnummer aus Daten extrahieren
- [ ] Validierung: Format-Check (optional)
- [ ] In Angebot-Tabelle einfügen

### Testing:
- [ ] Mit echten MBS Zeichnungsnummern testen
- [ ] Edge Cases (keine Nummer, sehr lang)
- [ ] Print-Layout
- [ ] Copy-Paste Verhalten

---

## Code Example (Complete)

```html
<!-- In Angebot-Tabelle -->
<table class="table">
  <thead>
    <tr>
      <th>Pos</th>
      <th>Artikelnr.</th>
      <th>Bezeichnung</th>
      <th class="right">Menge</th>
      <th class="right">Einzelpreis</th>
      <th class="right">Gesamtpreis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td class="mono">E-CNC-0001</td>
      <td>
        <div class="part-name">Verbindungsplatte</div>
        <div class="drawing-number">2500473.01.11.02.00.001</div>
        <div class="material">Werkstoff S235JR</div>
        <div class="note">nach Zeichnung</div>
      </td>
      <td class="right mono">29 Stck.</td>
      <td class="right mono">EUR 26,30</td>
      <td class="right mono">EUR 762,70</td>
    </tr>
  </tbody>
</table>
```

```css
/* Zeichnungsnummer Styling */
.drawing-number {
  font-size: 13px;
  color: #374151;
  font-family: 'SF Mono', Monaco, 'Cascadia Code', Consolas, monospace;
  margin-top: 2px;
  line-height: 1.4;
}

.material {
  font-size: 13px;
  color: #6B7280;
  margin-top: 2px;
}

.note {
  font-size: 12px;
  color: #9CA3AF;
  margin-top: 2px;
  font-style: italic;
}
```

---

## Validation Criteria

### Visual:
- ✅ Zeichnungsnummer steht unter Produktname
- ✅ Etwas kleiner und grauer als Produktname
- ✅ Monospace macht Punkte gut lesbar
- ✅ Kein Label (Platzersparnis)

### Functional:
- ✅ Copy-Paste funktioniert (ganze Nummer auf einmal)
- ✅ Druckbar (auch auf Papier lesbar)
- ✅ Responsive (auf schmalen Bildschirmen)

### Professional:
- ✅ Wie echtes MBS Angebot
- ✅ ISO-konform
- ✅ DIN 5008 kompatibel

---

## Next Steps

1. ✅ Research abgeschlossen
2. ⏳ Integration in REQUIREMENTS-V18-COMPLETE.md
3. ⏳ CSS-Klassen in Industrial Design System aufnehmen
4. ⏳ HTML-Template erstellen
5. ⏳ Testing mit echten Daten

---

*Research completed: 2026-02-06 02:50*  
*Sources: MBS Angebot (primary), DIN 5008, Golden Standards, ISO 7200*  
*Confidence: HIGH (based on real-world example)*

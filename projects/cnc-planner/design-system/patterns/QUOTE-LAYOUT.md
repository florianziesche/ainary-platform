# Quote Layout Pattern

**Pattern:** Professional Quote/Angebot Layout  
**Based on:** MBS Angebot (Real Maschinenbau Company)  
**Version:** 1.0  
**Research:** [`research/MBS-ANGEBOT-LINE-BY-LINE.md`](../../research/MBS-ANGEBOT-LINE-BY-LINE.md)

---

## 🎯 Purpose

Standard layout for CNC machining quotes following DIN 5008 and Maschinenbau industry standards.

**Key Features:**
- Professional header with company data
- DIN 5008 address window
- Quote metadata (number, date)
- Position table (6 columns)
- Totals calculation
- Terms & conditions
- Legal footer

---

## 📐 Layout Structure

```
┌──────────────────────────────────────────────────┐
│ 1. Fensterzeile (Company header, klein)         │
├──────────────────────────────────────────────────┤
│ 2. Header (2-spaltig)                            │
│    ┌────────────────┬─────────────────┐          │
│    │ Kundenadresse  │ Angebotsdaten   │          │
│    │ (links)        │ (rechts)        │          │
│    └────────────────┴─────────────────┘          │
├──────────────────────────────────────────────────┤
│ 3. Anrede & Einleitung                           │
├──────────────────────────────────────────────────┤
│ 4. Positions-Tabelle (6 Spalten)                 │
│    Pos | Art.Nr | Bezeichnung | Menge | EP | GP  │
├──────────────────────────────────────────────────┤
│ 5. Summen (rechtsbündig)                         │
│    Zwischensumme, MwSt, GESAMTBETRAG             │
├──────────────────────────────────────────────────┤
│ 6. Gültigkeit (Info-Box)                         │
├──────────────────────────────────────────────────┤
│ 7. Bedingungen (Text-Block)                      │
├──────────────────────────────────────────────────┤
│ 8. Footer (2-spaltig)                            │
│    Kontakt | Rechtliches                         │
└──────────────────────────────────────────────────┘
```

---

## 💻 Complete Template

### 1. Fensterzeile

```html
<div style="font-size: 11px; color: #9CA3AF; margin-bottom: var(--space-4);">
  CNC Planer Pro • Musterstraße 1 • 12345 Musterstadt
</div>
```

---

### 2. Header (2-Column)

```html
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: var(--space-8); margin-bottom: var(--space-8); padding-bottom: var(--space-6); border-bottom: 1px solid var(--color-border-light);">
  
  <!-- Linke Spalte: Kundenadresse -->
  <div>
    <div style="font-size: 14px; line-height: 1.75;">
      <strong id="customerName">Müller Industrie GmbH</strong><br>
      <span id="customerStreet">Hauptstraße 26</span><br>
      <span id="customerCity">09619 Mulda</span>
    </div>
  </div>
  
  <!-- Rechte Spalte: Angebotsdaten -->
  <div style="font-size: 13px;">
    <table style="width: 100%;">
      <tr>
        <td style="color: #6B7280; padding: 4px 0; font-weight: 600;">Angebot</td>
        <td style="text-align: right; padding: 4px 0;" id="quoteNumber">20260072</td>
      </tr>
      <tr>
        <td style="color: #6B7280; padding: 4px 0; font-weight: 600;">Datum</td>
        <td style="text-align: right; padding: 4px 0;" id="quoteDate">06.02.2026</td>
      </tr>
      <tr>
        <td style="color: #6B7280; padding: 4px 0; font-weight: 600;">Bearbeiter</td>
        <td style="text-align: right; padding: 4px 0;">KI-Assistent</td>
      </tr>
    </table>
  </div>
  
</div>
```

---

### 3. Anrede

```html
<div style="margin-bottom: var(--space-6); font-size: 14px; line-height: 1.75;">
  <p style="margin-bottom: var(--space-4);">
    <strong>Sehr geehrte Damen und Herren,</strong>
  </p>
  <p>wir bedanken uns für Ihre Anfrage und bieten Ihnen gerne, wie folgt an:</p>
</div>
```

---

### 4. Positions-Tabelle

**Siehe:** [`TABLES.md`](../components/TABLES.md#quote-table-6-spalten)

```html
<table class="table" style="margin-bottom: var(--space-8);">
  <thead>
    <tr>
      <th style="width: 50px;">Pos</th>
      <th style="width: 100px;">Artikelnr.</th>
      <th>Bezeichnung</th>
      <th class="right" style="width: 80px;">Menge</th>
      <th class="right" style="width: 100px;">Einzelpreis</th>
      <th class="right" style="width: 100px;">Gesamtpreis</th>
    </tr>
  </thead>
  <tbody id="quoteTableBody">
    <!-- JavaScript rendered -->
  </tbody>
</table>
```

---

### 5. Summen

```html
<div style="display: flex; justify-content: flex-end; margin-bottom: var(--space-8);">
  <div style="width: 300px;">
    
    <!-- Zwischensumme -->
    <div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 14px;">
      <span style="color: #374151;">Zwischensumme</span>
      <span id="subtotal">EUR 170,76</span>
    </div>
    
    <!-- MwSt -->
    <div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 14px; border-top: 1px solid #E5E7EB;">
      <span style="color: #374151;">+ MwSt. 19%</span>
      <span id="tax">EUR 32,44</span>
    </div>
    
    <!-- Gesamtbetrag -->
    <div style="display: flex; justify-content: space-between; padding: 16px 0; font-size: 18px; font-weight: 700; border-top: 2px solid #1F2937;">
      <span>GESAMTBETRAG</span>
      <span id="total">EUR 203,20</span>
    </div>
    
  </div>
</div>
```

---

### 6. Gültigkeit (Info-Box)

```html
<div class="info-box" style="margin-bottom: var(--space-8);">
  <strong>Angebotsgültigkeit:</strong> 
  Freibleibend mit einer Gültigkeit von 4 Wochen 
  (bis <strong id="validUntil">06.03.2026</strong>)
</div>
```

**CSS:**
```css
.info-box {
  background: var(--color-gray-50);
  border-left: 3px solid var(--color-primary);
  padding: var(--space-4);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
}
```

---

### 7. Bedingungen

```html
<div class="terms-block" style="margin-bottom: var(--space-8);">
  <p>
    <strong>Preiskalkulation:</strong> 
    Die Preise basieren auf aktuellen Materialkosten und 
    Standard-Fertigungsparametern (±15% Genauigkeit). 
    Änderungen bei Sonderwünschen oder stark schwankenden 
    Marktpreisen vorbehalten.
  </p>
  
  <p>
    <strong>Zahlungsbedingungen:</strong> 
    30 Tage netto nach Rechnungsdatum.
  </p>
  
  <p>
    <strong>Lieferzeit:</strong> 
    Ca. 3-4 Wochen nach Auftragseingang 
    (abhängig von Materialverfügbarkeit und aktueller Auslastung).
  </p>
  
  <p>
    <strong>Mindermengenzuschlag:</strong> 
    Für Bestellungen unter 100 € berechnen wir einen 
    Mindermengenzuschlag von pauschal 35 €.
  </p>
</div>
```

**CSS:**
```css
.terms-block {
  padding: var(--space-6);
  background: var(--color-gray-50);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  border-radius: 4px;
}

.terms-block p {
  margin-bottom: var(--space-4);
}

.terms-block p:last-child {
  margin-bottom: 0;
}

.terms-block strong {
  color: #000;
  font-weight: 600;
}
```

---

### 8. Footer (2-Column)

```html
<div class="contact-footer">
  <div class="footer-grid">
    
    <!-- Linke Spalte: Kontakt -->
    <div>
      <strong>CNC Planer Pro</strong><br>
      Musterstraße 1<br>
      12345 Musterstadt<br>
      <br>
      Telefon: +49 123 456789<br>
      E-Mail: info@cnc-planer-pro.de
    </div>
    
    <!-- Rechte Spalte: Rechtliches -->
    <div>
      <strong>Rechtliches</strong><br>
      Geschäftsführer: [Name]<br>
      Handelsregister: [HR-Nummer]<br>
      Registergericht: [Ort]<br>
      USt-ID: [Nummer]<br>
      <br>
      IBAN: [IBAN] | BIC: [BIC]
    </div>
    
  </div>
</div>
```

**CSS:**
```css
.contact-footer {
  margin-top: var(--space-12);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-gray-200);
  font-size: 11px;
  color: var(--color-gray-400);
  line-height: 1.6;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

.footer-grid strong {
  color: var(--color-gray-600);
  font-weight: 600;
}
```

---

## 🎨 Typography Scale

| Element | Font Size | Weight | Color |
|---------|-----------|--------|-------|
| Fensterzeile | 11px | 400 | #9CA3AF |
| Kundenname | 14px | 700 | #000 |
| Anrede | 14px | 700 | #000 |
| Body Text | 14px | 400 | #000 |
| Metadaten | 13px | 400 | #6B7280 |
| Gesamtbetrag | 18px | 700 | #000 |
| Footer | 11px | 400 | #9CA3AF |

---

## 📏 Spacing Scale

- **Section Gaps:** 24-32px (`var(--space-6)` bis `var(--space-8)`)
- **Header Padding:** 16px vertical (`var(--space-4)`)
- **Table Margin:** 32px bottom (`var(--space-8)`)
- **Footer Margin:** 48px top (`var(--space-12)`)

---

## 🔢 Data Formatting

**Use DEFormatter for all data:**

```javascript
DEFormatter.date(new Date());           // "06.02.2026"
DEFormatter.price(170.76);              // "EUR 170,76"
DEFormatter.quantity(29);               // "29 Stck."
```

**Referenz:** [`RESEARCH-DEUTSCHE-FORMATIERUNG.md`](../../RESEARCH-DEUTSCHE-FORMATIERUNG.md)

---

## 🧪 Testing Checklist

### Visual:
- [ ] Fensterzeile klein und grau
- [ ] Header 2-spaltig
- [ ] Kundenname fett
- [ ] Angebotsdaten rechtsbündig
- [ ] Tabelle sauber formatiert
- [ ] Summen rechtsbündig
- [ ] Gültigkeit prominent (Info-Box)
- [ ] Bedingungen lesbar (nicht zu klein)
- [ ] Footer 2-spaltig, klein, grau

### Functional:
- [ ] Kundenname dynamisch
- [ ] Angebotsnummer generiert
- [ ] Datum heute
- [ ] Gültigkeit berechnet (heute + 28 Tage)
- [ ] Summen korrekt
- [ ] Print-ready

### Content:
- [ ] Anrede passt (Sehr geehrte...)
- [ ] Bedingungen vollständig
- [ ] Footer: Kontakt + Rechtliches

---

## 📚 Complete Example

**Siehe:** [`REQUIREMENTS-V18-FINAL.md`](../../REQUIREMENTS-V18-FINAL.md) - Complete HTML Structure

---

## 🔗 Related

- [Design System](../DESIGN-SYSTEM.md)
- [TABLES.md](../components/TABLES.md)
- [RESEARCH-ZEICHNUNGSNUMMER.md](../../RESEARCH-ZEICHNUNGSNUMMER.md)
- [RESEARCH-POSITION-NUMMERIERUNG.md](../../RESEARCH-POSITION-NUMMERIERUNG.md)
- [RESEARCH-PREIS-FORMATIERUNG.md](../../RESEARCH-PREIS-FORMATIERUNG.md)
- [RESEARCH-GÜLTIGKEIT.md](../../RESEARCH-GÜLTIGKEIT.md)
- [RESEARCH-BEDINGUNGEN-TEXT.md](../../RESEARCH-BEDINGUNGEN-TEXT.md)
- [RESEARCH-FOOTER-RECHTLICHES.md](../../RESEARCH-FOOTER-RECHTLICHES.md)

---

*Last Updated: 2026-02-06*  
*Based on: Real Maschinenbau Angebot (MBS)*

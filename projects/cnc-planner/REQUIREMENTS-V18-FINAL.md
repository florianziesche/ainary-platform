# CNC Planer Pro v18 - FINAL Requirements & Implementation Guide

**Status:** ✅ READY FOR IMPLEMENTATION  
**Research Complete:** 8/8 (100%)  
**Datum:** 2026-02-06 03:25  
**Time to Demo:** 7h 5min

---

## 🎯 MISSION

**Build best-in-class Industrial CNC Quote Generator that looks like a real Maschinenbau company's work.**

**Success Criteria:**
- Onkel sagt: "Das sieht aus wie unsere echten Angebote"
- Kunde kann es sofort verstehen
- Rechtlich sauber
- Druckbar als PDF

---

## 📋 COMPLETE FEATURE SET

### 1. Zeichnungsnummer-Display

**What:** Eindeutige Zeichnungsnummer unter Produktname

**Format:** `2500473.01.11.02.00.001` (12-stellig mit Punkten)

**Implementation:**
```html
<div class="part-name">Verbindungsplatte</div>
<div class="drawing-number">2500473.01.11.02.00.001</div>
<div class="material">Werkstoff S235JR</div>
```

```css
.drawing-number {
  font-size: 13px;
  color: #374151;
  font-family: var(--font-mono);
  margin-top: 2px;
}
```

**Research:** `RESEARCH-ZEICHNUNGSNUMMER.md`

---

### 2. Position-Nummerierung

**What:** Fortlaufende Nummerierung der Positionen

**Format:** `1, 2, 3, 4...` (klassisch, wie MBS)

**Implementation:**
```javascript
function generatePositions(parts) {
  return parts.map((part, index) => ({
    ...part,
    position: index + 1
  }));
}
```

```html
<td class="position-nr">1</td>
```

```css
.position-nr {
  width: 50px;
  text-align: right;
  font-weight: normal;
  font-variant-numeric: tabular-nums;
}
```

**Research:** `RESEARCH-POSITION-NUMMERIERUNG.md`

---

### 3. Preis-Formatierung

**What:** Deutsche Währungsformatierung

**Format:** `EUR X.XXX,XX`

**Examples:**
- `EUR 26,30`
- `EUR 1.234,56`
- `EUR 12.345,67`

**Implementation:**
```javascript
function formatPrice(amount) {
  const formatted = amount.toLocaleString('de-DE', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  });
  return `EUR ${formatted}`;
}
```

**Research:** `RESEARCH-PREIS-FORMATIERUNG.md`

---

### 4. Gültigkeit Automatisch

**What:** Angebotsgültigkeit berechnen und anzeigen

**Standard:** 4 Wochen ab Angebotsdatum (wie MBS)

**Format:** "Freibleibend mit einer Gültigkeit von 4 Wochen (bis DD.MM.YYYY)"

**Implementation:**
```javascript
function calculateValidity() {
  const today = new Date();
  const validUntil = new Date(today);
  validUntil.setDate(today.getDate() + 28);
  
  return {
    date: DEFormatter.date(today),
    validUntil: DEFormatter.date(validUntil)
  };
}
```

**Display:**
```html
<div class="info-box">
  <strong>Angebotsgültigkeit:</strong> 
  Freibleibend mit einer Gültigkeit von 4 Wochen 
  (bis <strong id="validUntil">06.03.2026</strong>)
</div>
```

**Research:** `RESEARCH-GÜLTIGKEIT.md`

---

### 5. Bedingungen-Text

**What:** Rechtliche Bedingungen, Zahlungsbedingungen, Lieferzeit

**Sections:**
1. Preiskalkulation-Hinweis
2. Zahlungsbedingungen
3. Lieferzeit
4. Mindermengenzuschlag
5. AGB-Referenz

**Implementation:**
```html
<div class="terms-block">
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
    (abhängig von Materialverfügbarkeit).
  </p>
</div>
```

**Research:** `RESEARCH-BEDINGUNGEN-TEXT.md`

---

### 6. Footer mit Rechtlichem

**What:** Kontaktdaten + Pflichtangaben für GmbH

**Format:** 2-spaltig, 8pt Schrift, Grau

**Pflichtangaben (§ 35a GmbHG):**
- Firmenname mit Rechtsform
- Geschäftsführer
- Registergericht + HR-Nummer
- USt-ID
- IBAN (empfohlen)

**Implementation:**
```html
<div class="contact-footer">
  <div class="footer-grid">
    <div>
      <strong>CNC Planer Pro</strong><br>
      Musterstraße 1<br>
      12345 Musterstadt<br>
      <br>
      Telefon: +49 123 456789<br>
      E-Mail: info@cnc-planer-pro.de
    </div>
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

```css
.contact-footer {
  margin-top: var(--space-12);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-border-light);
  font-size: 11px;  /* 8pt */
  color: #9CA3AF;   /* Grau */
  line-height: 1.6;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}
```

**Research:** `RESEARCH-FOOTER-RECHTLICHES.md`

---

### 7. Tabellen-Styling (Professional)

**What:** Bootstrap-Standard Professional Tables

**Specs:**
- Header Background: `#f8f9fa` (hellgrau)
- Border: 1px horizontal zwischen Zeilen
- Padding: 8px (0.5rem)
- Hover: Ja (subtil, 7.5% opacity)
- Zebra-Stripes: Optional (nur bei >6 Spalten)

**Implementation:**
```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.table thead {
  background: #f8f9fa;
}

.table th {
  padding: 8px 12px;
  text-align: left;
  font-weight: 600;
  color: #374151;
  border-bottom: 2px solid #D1D5DB;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table td {
  padding: 8px 12px;
  border-bottom: 1px solid #E5E7EB;
  color: #000;
}

.table tbody tr:hover {
  background: rgba(0, 0, 0, 0.025);
}
```

**Research:** `RESEARCH-TABELLEN-STYLING.md`

---

### 8. Deutsche Formatierung (Complete)

**What:** Library für alle deutschen Formate

**Formats:**
- Datum: `DD.MM.YYYY`
- Preise: `EUR X.XXX,XX`
- Längen: `440 mm`
- Gewicht: `2,20 kg`
- Zeit: `12,5 min` oder `1,3 h`
- Mengen: `29 Stck.`
- Prozent: `15 %`

**Implementation:**
```javascript
const DEFormatter = {
  date(date) {
    return date.toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  },
  
  price(amount) {
    const formatted = amount.toLocaleString('de-DE', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
    return `EUR ${formatted}`;
  },
  
  length(value, unit = 'mm') {
    return `${Math.round(value)} ${unit}`;
  },
  
  weight(value) {
    return `${value.toFixed(2)} kg`;
  },
  
  time(minutes) {
    if (minutes < 60) return `${minutes.toFixed(1)} min`;
    return `${(minutes/60).toFixed(1)} h`;
  },
  
  quantity(num, unit = 'Stck.') {
    return `${Math.round(num)} ${unit}`;
  }
};
```

**Research:** `RESEARCH-DEUTSCHE-FORMATIERUNG.md`

---

## 🏗️ COMPLETE HTML STRUCTURE

### Angebot-Tab (Full Template):

```html
<div class="section" id="section-quote">
  <div class="card">
    
    <!-- Header -->
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: var(--space-8); margin-bottom: var(--space-8); padding-bottom: var(--space-6); border-bottom: 1px solid var(--color-border-light);">
      
      <!-- Linke Spalte -->
      <div>
        <div style="font-size: 11px; color: #9CA3AF; margin-bottom: var(--space-4);">
          CNC Planer Pro • Musterstraße 1 • 12345 Musterstadt
        </div>
        
        <div style="font-size: 14px; line-height: 1.75;">
          <strong id="customerName">Müller Industrie GmbH</strong><br>
          <span id="customerStreet">Hauptstraße 26</span><br>
          <span id="customerCity">09619 Mulda</span>
        </div>
      </div>
      
      <!-- Rechte Spalte -->
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
    
    <!-- Anrede -->
    <div style="margin-bottom: var(--space-6); font-size: 14px; line-height: 1.75;">
      <p style="margin-bottom: var(--space-4);"><strong>Sehr geehrte Damen und Herren,</strong></p>
      <p>wir bedanken uns für Ihre Anfrage und bieten Ihnen gerne, wie folgt an:</p>
    </div>
    
    <!-- Haupt-Tabelle -->
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
        <!-- Rendered by JavaScript -->
      </tbody>
    </table>
    
    <!-- Summen -->
    <div style="display: flex; justify-content: flex-end; margin-bottom: var(--space-8);">
      <div style="width: 300px;">
        <div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 14px;">
          <span style="color: #374151;">Zwischensumme</span>
          <span id="subtotal">EUR 170,76</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 14px; border-top: 1px solid #E5E7EB;">
          <span style="color: #374151;">+ MwSt. 19%</span>
          <span id="tax">EUR 32,44</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 16px 0; font-size: 18px; font-weight: 700; border-top: 2px solid #1F2937;">
          <span>GESAMTBETRAG</span>
          <span id="total">EUR 203,20</span>
        </div>
      </div>
    </div>
    
    <!-- Gültigkeit -->
    <div class="info-box" style="margin-bottom: var(--space-8);">
      <strong>Angebotsgültigkeit:</strong> 
      Freibleibend mit einer Gültigkeit von 4 Wochen 
      (bis <strong id="validUntil">06.03.2026</strong>)
    </div>
    
    <!-- Bedingungen -->
    <div class="terms-block" style="margin-bottom: var(--space-8);">
      <p><strong>Preiskalkulation:</strong> Die Preise basieren auf aktuellen Materialkosten und Standard-Fertigungsparametern (±15% Genauigkeit). Änderungen bei Sonderwünschen oder stark schwankenden Marktpreisen vorbehalten.</p>
      
      <p><strong>Zahlungsbedingungen:</strong> 30 Tage netto nach Rechnungsdatum.</p>
      
      <p><strong>Lieferzeit:</strong> Ca. 3-4 Wochen nach Auftragseingang (abhängig von Materialverfügbarkeit und aktueller Auslastung).</p>
      
      <p><strong>Mindermengenzuschlag:</strong> Für Bestellungen unter 100 € berechnen wir einen Mindermengenzuschlag von pauschal 35 €.</p>
    </div>
    
    <!-- Footer -->
    <div class="contact-footer">
      <div class="footer-grid">
        <div>
          <strong>CNC Planer Pro</strong><br>
          Musterstraße 1<br>
          12345 Musterstadt<br>
          <br>
          Telefon: +49 123 456789<br>
          E-Mail: info@cnc-planer-pro.de
        </div>
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
    
  </div>
</div>
```

---

## 💻 COMPLETE JAVASCRIPT

```javascript
// ==============================================
// DEUTSCHE FORMATIERUNG LIBRARY
// ==============================================

const DEFormatter = {
  date(date) {
    return date.toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  },
  
  price(amount) {
    const formatted = amount.toLocaleString('de-DE', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
    return `EUR ${formatted}`;
  },
  
  length(value, unit = 'mm') {
    return `${Math.round(value)} ${unit}`;
  },
  
  weight(value) {
    return `${value.toFixed(2)} kg`;
  },
  
  time(minutes) {
    if (minutes < 60) return `${minutes.toFixed(1)} min`;
    return `${(minutes/60).toFixed(1)} h`;
  },
  
  quantity(num, unit = 'Stck.') {
    return `${Math.round(num)} ${unit}`;
  }
};

// ==============================================
// ANGEBOT FUNCTIONS
// ==============================================

function calculateValidity() {
  const today = new Date();
  const validUntil = new Date(today);
  validUntil.setDate(today.getDate() + 28);  // 4 Wochen
  
  document.getElementById('quoteDate').textContent = DEFormatter.date(today);
  document.getElementById('validUntil').textContent = DEFormatter.date(validUntil);
}

function generatePositions(parts) {
  return parts.map((part, index) => ({
    ...part,
    position: index + 1  // 1, 2, 3...
  }));
}

function renderQuote(data) {
  const parts = generatePositions(data.parts);
  
  let html = '';
  parts.forEach(part => {
    html += `
      <tr>
        <td class="position-nr">${part.position}</td>
        <td style="font-family: var(--font-mono); font-size: 13px;">${part.articleNumber}</td>
        <td>
          <div style="font-weight: 600; font-size: 14px; color: #000;">${part.name}</div>
          <div style="font-size: 13px; color: #374151; font-family: var(--font-mono); margin-top: 2px;">${part.drawingNumber}</div>
          <div style="font-size: 13px; color: #6B7280; margin-top: 2px;">Werkstoff ${part.material}</div>
        </td>
        <td class="right" style="font-family: var(--font-mono); font-size: 13px;">${DEFormatter.quantity(part.quantity)}</td>
        <td class="right" style="font-family: var(--font-mono); font-size: 13px;">${DEFormatter.price(part.price)}</td>
        <td class="right" style="font-family: var(--font-mono); font-size: 13px;">${DEFormatter.price(part.price * part.quantity)}</td>
      </tr>
    `;
  });
  
  document.getElementById('quoteTableBody').innerHTML = html;
  
  // Summen
  const subtotal = parts.reduce((sum, p) => sum + p.price * p.quantity, 0);
  const tax = subtotal * 0.19;
  const total = subtotal + tax;
  
  document.getElementById('subtotal').textContent = DEFormatter.price(subtotal);
  document.getElementById('tax').textContent = DEFormatter.price(tax);
  document.getElementById('total').textContent = DEFormatter.price(total);
  
  // Gültigkeit
  calculateValidity();
}

// ==============================================
// EXAMPLE DATA
// ==============================================

const exampleData = {
  parts: [
    {
      articleNumber: 'E-CNC-0001',
      name: 'Verbindungsplatte',
      drawingNumber: '2500473.01.11.02.00.001',
      material: 'S235JR',
      quantity: 1,
      price: 170.76
    }
  ]
};

// Render on page load
document.addEventListener('DOMContentLoaded', () => {
  renderQuote(exampleData);
});
```

---

## 🎨 COMPLETE CSS (Additional Styles)

```css
/* ==============================================
   ANGEBOT-SPECIFIC STYLES
   ============================================== */

/* Info-Box */
.info-box {
  background: #F9FAFB;
  border-left: 3px solid #1F2937;
  padding: 16px 24px;
  font-size: 14px;
  margin: 24px 0;
  line-height: 1.75;
}

/* Bedingungen */
.terms-block {
  padding: 24px;
  background: #F9FAFB;
  font-size: 14px;
  line-height: 1.75;
  border-radius: 4px;
}

.terms-block p {
  margin-bottom: 16px;
}

.terms-block p:last-child {
  margin-bottom: 0;
}

.terms-block strong {
  color: #000;
  font-weight: 600;
}

/* Footer */
.contact-footer {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid #E5E7EB;
  font-size: 11px;
  color: #9CA3AF;
  line-height: 1.6;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.footer-grid strong {
  color: #6B7280;
  font-weight: 600;
}

/* Position-Nummer */
.position-nr {
  width: 50px;
  text-align: right;
  font-weight: normal;
  font-variant-numeric: tabular-nums;
}

/* Tabellen Right-Alignment */
.table .right {
  text-align: right;
}
```

---

## ✅ TESTING CHECKLIST

### Visual Tests:
- [ ] Zeichnungsnummer unter Produktname (grau, monospace)
- [ ] Position 1, 2, 3... (rechtsbündig, nicht fett)
- [ ] Preise `EUR X.XXX,XX` (tabular nums)
- [ ] Datum `DD.MM.YYYY`
- [ ] Gültigkeit berechnet (heute + 28 Tage)
- [ ] Bedingungen lesbar
- [ ] Footer 2-spaltig, klein, grau

### Functional Tests:
- [ ] `renderQuote()` funktioniert
- [ ] Summen korrekt berechnet
- [ ] Position-Nummern automatisch
- [ ] Gültigkeit automatisch

### Edge Cases:
- [ ] Lange Zeichnungsnummer (>30 Zeichen)
- [ ] Viele Positionen (>10)
- [ ] Hohe Preise (>10.000 EUR)
- [ ] Multiple Parts rendern

### Print Test:
- [ ] PDF-Export funktioniert
- [ ] Footer auf jeder Seite
- [ ] Keine abgeschnittenen Elemente

---

## ⏱️ IMPLEMENTATION TIME

**Estimated:** 60-90 minutes

**Breakdown:**
1. HTML Template einbauen: 20 min
2. CSS Styles hinzufügen: 15 min
3. JavaScript Functions: 20 min
4. Integration testen: 15 min
5. Edge Cases fixen: 10 min
6. Print-Test: 10 min

---

## 🚀 DELIVERY CHECKLIST

Before saying "DONE":

- [ ] Browser-Test (alle Features sichtbar)
- [ ] Print-Test (PDF sieht gut aus)
- [ ] Onkel's Daten laden (2500473...)
- [ ] Screenshot machen
- [ ] Commit to git

---

*Requirements finalized: 2026-02-06 03:25*  
*Research sources: 8 complete research documents*  
*Ready for: Immediate implementation*  
*Confidence: VERY HIGH (real-world based)*

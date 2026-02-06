# CNC Planer Pro v18 - Phase 2 Complete (Research Results)

**Status:** ✅ Research abgeschlossen  
**Datum:** 2026-02-06 03:20

---

## 📋 COMPLETED RESEARCHES

### 1. Zeichnungsnummer-Display ✅

**Decision:** Unter Produktname, Monospace, Grau

**Implementation:**
```html
<div class="part-name">Verbindungsplatte</div>
<div class="drawing-number">2500473.01.11.02.00.001</div>
```

```css
.drawing-number {
  font-size: 13px;
  color: #374151;
  font-family: var(--font-mono);
  margin-top: 2px;
}
```

**Source:** `RESEARCH-ZEICHNUNGSNUMMER.md` (7KB)

---

### 2. Position-Nummerierung ✅

**Decision:** Klassisch (1, 2, 3...) als Default, Optional ERP-Style (10, 20, 30)

**Implementation:**
```javascript
function generateQuote(parts) {
  let positionNumber = 1;
  parts.forEach(part => {
    part.position = positionNumber++;
  });
}
```

**Source:** `RESEARCH-POSITION-NUMMERIERUNG.md` (8KB)

---

### 3. Preis-Formatierung ✅

**Decision:** `EUR X.XXX,XX` (wie MBS)

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

**Source:** `RESEARCH-PREIS-FORMATIERUNG.md` (9KB)

---

### 4. Bedingungen-Text ✅

**Decision:** Nach Tabelle, Info-Box für Gültigkeit, Text-Block für Rest

**Sections:**
1. Angebotsgültigkeit (prominent)
2. Preiskalkulation-Hinweis
3. Zahlungsbedingungen
4. Lieferzeit
5. Mindermengenzuschlag

**Source:** `RESEARCH-BEDINGUNGEN-TEXT.md` (6KB)

---

### 5. Deutsche Formatierung ✅

**Decision:** Complete Library für Datum, Zahlen, Einheiten

**Implementation:**
```javascript
const DEFormatter = {
  date: (d) => d.toLocaleDateString('de-DE'),
  price: (n) => `EUR ${n.toLocaleString('de-DE', {min:2, max:2})}`,
  length: (n) => `${n} mm`,
  weight: (n) => `${n.toFixed(2)} kg`,
  time: (m) => m < 60 ? `${m} min` : `${(m/60).toFixed(1)} h`
};
```

**Source:** `RESEARCH-DEUTSCHE-FORMATIERUNG.md` (6KB)

---

### 6-8. IN PROGRESS (Sub-Agents) ⏳

- **Gültigkeit:** Sub-Agent läuft
- **Tabellen-Styling:** Sub-Agent läuft
- **Footer-Rechtliches:** Sub-Agent läuft

---

## 🎯 IMPLEMENTATION PRIORITY

### P0 - Angebot-Tab (CRITICAL für Demo)

**Must-Have:**
1. ✅ Zeichnungsnummer unter Produktname
2. ✅ Position-Nummerierung (1, 2, 3...)
3. ✅ Preis-Formatierung (EUR X.XXX,XX)
4. ✅ Gültigkeit automatisch (4 Wochen)
5. ✅ Bedingungen-Text
6. ⏳ Footer mit Rechtlichem (wartet auf Research)
7. ✅ Deutsche Formatierung (Datum, Preise)

### P1 - Andere Tabs

**Kalkulation:**
- ⏳ Tabellen-Styling (wartet auf Research)
- Berechnungsgrundlagen-Card

**Fertigungsanweisung:**
- Zeichnungsnummer als Referenz
- Operationen-Tabelle

**Parameter:**
- Deutsche Einheiten (mm, kg, min)

---

## 📊 COMPLETE TECH SPECS

### HTML Structure (Angebot):

```html
<div class="section" id="section-quote">
  <div class="card">
    
    <!-- Header mit Firmendaten (2-spaltig) -->
    <div class="quote-header">
      <div class="customer-address">...</div>
      <div class="quote-meta">
        <dl>
          <dt>Angebot</dt><dd>20260072</dd>
          <dt>Datum</dt><dd id="quoteDate">06.02.2026</dd>
        </dl>
      </div>
    </div>
    
    <!-- Anrede -->
    <div class="greeting">
      <p><strong>Sehr geehrte Damen und Herren,</strong></p>
      <p>wir bedanken uns für Ihre Anfrage...</p>
    </div>
    
    <!-- Haupt-Tabelle -->
    <table class="table">
      <thead>
        <tr>
          <th style="width: 50px;">Pos</th>
          <th style="width: 100px;">Artikelnr.</th>
          <th>Bezeichnung</th>
          <th class="right">Menge</th>
          <th class="right">Einzelpreis</th>
          <th class="right">Gesamtpreis</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="position-nr">1</td>
          <td class="mono">E-CNC-0001</td>
          <td>
            <div class="part-name">Verbindungsplatte</div>
            <div class="drawing-number">2500473.01.11.02.00.001</div>
            <div class="material">Werkstoff S235JR</div>
          </td>
          <td class="right mono">29 Stck.</td>
          <td class="right mono">EUR 26,30</td>
          <td class="right mono">EUR 762,70</td>
        </tr>
      </tbody>
    </table>
    
    <!-- Summen -->
    <div class="totals">
      <div class="totals-grid">
        <span>Zwischensumme</span><span id="subtotal">EUR 170,76</span>
        <span>+ MwSt. 19%</span><span id="tax">EUR 32,44</span>
        <span class="total">GESAMTBETRAG</span><span class="total" id="total">EUR 203,20</span>
      </div>
    </div>
    
    <!-- Gültigkeit (prominent) -->
    <div class="info-box">
      <strong>Angebotsgültigkeit:</strong> Freibleibend mit einer Gültigkeit von 4 Wochen 
      (bis <strong id="validUntil">06.03.2026</strong>)
    </div>
    
    <!-- Bedingungen -->
    <div class="terms-block">
      <p><strong>Preiskalkulation:</strong> ...</p>
      <p><strong>Zahlungsbedingungen:</strong> ...</p>
      <p><strong>Lieferzeit:</strong> ...</p>
    </div>
    
    <!-- Footer (wartet auf Research) -->
    <div class="contact-footer">
      <div class="footer-grid">
        <div>
          <strong>CNC Planer Pro</strong><br>
          Musterstraße 1<br>
          12345 Musterstadt
        </div>
        <div>
          <strong>Rechtliches</strong><br>
          USt-ID: [...]<br>
          IBAN: [...]
        </div>
      </div>
    </div>
    
  </div>
</div>
```

---

### CSS Classes (Complete):

```css
/* Zeichnungsnummer */
.drawing-number {
  font-size: 13px;
  color: #374151;
  font-family: var(--font-mono);
  margin-top: 2px;
}

/* Position-Nummer */
.position-nr {
  width: 50px;
  text-align: right;
  font-weight: normal;
  font-variant-numeric: tabular-nums;
}

/* Preise */
.price {
  font-variant-numeric: tabular-nums;
  text-align: right;
}

/* Gültigkeit Info-Box */
.info-box {
  background: var(--color-bg-subtle);
  border-left: 3px solid var(--color-primary);
  padding: var(--space-4);
  font-size: var(--text-sm);
  margin: var(--space-6) 0;
}

/* Bedingungen */
.terms-block {
  padding: var(--space-6);
  background: var(--color-bg-subtle);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
}

.terms-block p {
  margin-bottom: var(--space-4);
}

/* Footer */
.contact-footer {
  margin-top: var(--space-12);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-border-light);
  font-size: var(--text-xs);
  color: var(--color-text-hint);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}
```

---

### JavaScript Functions:

```javascript
// Formatierungs-Library
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
  }
};

// Gültigkeit berechnen
function calculateValidity() {
  const today = new Date();
  const validUntil = new Date(today);
  validUntil.setDate(today.getDate() + 28);  // 4 Wochen
  
  document.getElementById('quoteDate').textContent = DEFormatter.date(today);
  document.getElementById('validUntil').textContent = DEFormatter.date(validUntil);
}

// Position-Nummerierung
function generatePositions(parts) {
  return parts.map((part, index) => ({
    ...part,
    position: index + 1  // 1, 2, 3...
  }));
}

// Angebot rendern
function renderQuote(data) {
  const parts = generatePositions(data.parts);
  
  let html = '';
  parts.forEach(part => {
    html += `
      <tr>
        <td class="position-nr">${part.position}</td>
        <td class="mono">${part.articleNumber}</td>
        <td>
          <div class="part-name">${part.name}</div>
          <div class="drawing-number">${part.drawingNumber}</div>
          <div class="material">Werkstoff ${part.material}</div>
        </td>
        <td class="right mono">${part.quantity} Stck.</td>
        <td class="right mono">${DEFormatter.price(part.price)}</td>
        <td class="right mono">${DEFormatter.price(part.price * part.quantity)}</td>
      </tr>
    `;
  });
  
  document.querySelector('#section-quote tbody').innerHTML = html;
  
  // Summen berechnen
  const subtotal = parts.reduce((sum, p) => sum + p.price * p.quantity, 0);
  const tax = subtotal * 0.19;
  const total = subtotal + tax;
  
  document.getElementById('subtotal').textContent = DEFormatter.price(subtotal);
  document.getElementById('tax').textContent = DEFormatter.price(tax);
  document.getElementById('total').textContent = DEFormatter.price(total);
  
  // Gültigkeit
  calculateValidity();
}
```

---

## 🧪 TESTING CHECKLIST

### Visual:
- [ ] Zeichnungsnummer unter Produktname (grau, monospace)
- [ ] Position 1, 2, 3... (rechtsbündig, nicht fett)
- [ ] Preise `EUR X.XXX,XX` (rechtsbündig, tabular)
- [ ] Datum `DD.MM.YYYY`
- [ ] Gültigkeit prominent (Info-Box)
- [ ] Bedingungen lesbar (nicht zu klein)
- [ ] Footer klein aber lesbar

### Functional:
- [ ] Gültigkeit automatisch berechnet (heute + 28 Tage)
- [ ] Position-Nummern automatisch generiert
- [ ] Preise korrekt formatiert (Komma, Punkt)
- [ ] Summen korrekt berechnet
- [ ] Print-Layout funktioniert

### Edge Cases:
- [ ] Lange Zeichnungsnummer (>30 Zeichen)
- [ ] Viele Positionen (>10)
- [ ] Hohe Preise (>10.000 EUR)
- [ ] Null-Preis
- [ ] Negative Preis (Rabatt)

---

## ⏱️ IMPLEMENTATION TIME ESTIMATE

**Phase 3: Requirements finalisieren**
- Warte auf 3 Sub-Agents: ~5 min
- Merge all researches: ~10 min
- **Total:** ~15 min

**Phase 4: Implementation**
- HTML struktur: ~30 min
- JavaScript functions: ~30 min
- CSS styling: ~20 min
- Integration: ~20 min
- **Total:** ~100 min

**Phase 5: Testing**
- Browser test: ~15 min
- Edge cases: ~10 min
- Print test: ~5 min
- **Total:** ~30 min

**GRAND TOTAL:** ~2,5 Stunden ab jetzt

**Demo:** 10:30 (in 7h 10min) - **PLENTY OF TIME** ✅

---

*Phase 2 completed: 2026-02-06 03:20*  
*Next: Wait for Sub-Agents, then Phase 3*  
*Confidence: HIGH - Research solid, Implementation straightforward*

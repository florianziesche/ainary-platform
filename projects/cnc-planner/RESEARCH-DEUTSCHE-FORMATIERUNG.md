# Research: Deutsche Formatierung (Comprehensive)

**Feature:** Datum, Zahlen, Einheiten - Deutsche Standards  
**Datum:** 2026-02-06 03:17

---

## Datum-Formatierung

### DIN 5008 Standard

**Format:** `DD.MM.YYYY`

**Beispiele:**
```
06.02.2026  ✅ (DIN-konform)
6.2.2026    ⚠️ (erlaubt, aber uneinheitlich)
02/06/2026  ❌ (US-Format)
2026-02-06  ❌ (ISO-Format, nur für Technik)
```

**JavaScript Implementation:**
```javascript
function formatDateDE(date) {
  return date.toLocaleDateString('de-DE', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  });
}

// Beispiel:
const today = new Date();
formatDateDE(today);  // "06.02.2026"
```

---

## Zahlen-Formatierung

### Dezimalzahlen

**Format:** Komma als Dezimal-Trenner

```
12,5    ✅ (deutsch)
12.5    ❌ (englisch)
```

**Implementation:**
```javascript
function formatNumber(num, decimals = 2) {
  return num.toLocaleString('de-DE', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  });
}

// 1234.56 → "1.234,56"
```

---

### Tausender-Trenner

**Format:** Punkt (.) oder schmales Leerzeichen

```
1.234    ✅ (Punkt)
1 234    ✅ (Leerzeichen)
1,234    ❌ (US-Format)
```

**MBS nutzt:** Punkt (.)

---

### Prozent

**Format:** Zahl + Leerzeichen + "%"

```
15 %     ✅ (mit Leerzeichen, DIN 5008)
15%      ⚠️ (ohne Leerzeichen, akzeptiert)
```

**Implementation:**
```javascript
function formatPercent(num) {
  return `${formatNumber(num, 1)} %`;
}

// 15.5 → "15,5 %"
```

---

## Einheiten-Formatierung

### Längen

**Format:** Zahl + Leerzeichen + Einheit

```
440 mm    ✅
50 cm     ✅
2 m       ✅
440mm     ❌ (kein Leerzeichen)
```

**Implementation:**
```javascript
function formatLength(value, unit = 'mm') {
  return `${formatNumber(value, 0)} ${unit}`;
}

// 440 → "440 mm"
```

---

### Gewicht

**Format:** Zahl + Leerzeichen + Einheit

```
2,2 kg    ✅
220 g     ✅
2200g     ❌ (kein Leerzeichen)
```

---

### Zeit

**Format:** 
- Minuten: `X min` oder `X Min.`
- Stunden: `X h` oder `X Std.`

```
12,5 min  ✅
2 h       ✅
12.5 min  ❌ (Punkt statt Komma)
```

**Implementation:**
```javascript
function formatTime(minutes) {
  if (minutes < 60) {
    return `${formatNumber(minutes, 1)} min`;
  }
  const hours = minutes / 60;
  return `${formatNumber(hours, 1)} h`;
}

// 75 → "1,3 h"
// 45 → "45,0 min"
```

---

### Währung

**Siehe:** `RESEARCH-PREIS-FORMATIERUNG.md`

**Format:** `EUR X.XXX,XX`

```
EUR 1.234,56  ✅ (MBS-Standard)
1.234,56 €    ✅ (alternativ)
€1,234.56     ❌ (US-Format)
```

---

## Mengen & Einheiten

### Stückzahl

**Format:** Zahl + Leerzeichen + "Stück" oder "Stck."

```
29 Stück  ✅
29 Stck.  ✅ (Abkürzung)
29 pcs    ❌ (englisch)
```

**MBS nutzt:** "Stck." (Abkürzung)

---

### Toleranzen

**Format:** Zahl + Einheit + Toleranz

```
100 mm ±0,1      ✅
Ø 50h7           ✅ (ISO-Toleranz)
100mm +/-0.1     ❌ (kein Leerzeichen + Punkt)
```

---

## Vollständige Formatierungs-Library

```javascript
// ==============================================
// DEUTSCHE FORMATIERUNG - COMPLETE LIBRARY
// ==============================================

const DEFormatter = {
  
  // Datum
  date(date) {
    return date.toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  },
  
  // Datum + Uhrzeit
  datetime(date) {
    return date.toLocaleString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  },
  
  // Zahlen
  number(num, decimals = 2) {
    return num.toLocaleString('de-DE', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    });
  },
  
  // Preise (EUR)
  price(amount) {
    const formatted = this.number(amount, 2);
    return `EUR ${formatted}`;
  },
  
  // Prozent
  percent(num) {
    return `${this.number(num, 1)} %`;
  },
  
  // Länge
  length(value, unit = 'mm') {
    return `${this.number(value, 0)} ${unit}`;
  },
  
  // Gewicht
  weight(value, unit = 'kg') {
    const decimals = unit === 'kg' ? 2 : 0;
    return `${this.number(value, decimals)} ${unit}`;
  },
  
  // Zeit
  time(minutes) {
    if (minutes < 60) {
      return `${this.number(minutes, 1)} min`;
    }
    const hours = minutes / 60;
    return `${this.number(hours, 1)} h`;
  },
  
  // Menge
  quantity(num, unit = 'Stck.') {
    return `${this.number(num, 0)} ${unit}`;
  },
  
  // Telefon (optional)
  phone(number) {
    // +49 123 456789 → "+49 123 456789"
    return number.replace(/(\+\d{2})(\d{3})(\d+)/, '$1 $2 $3');
  }
};

// Beispiele:
DEFormatter.date(new Date());              // "06.02.2026"
DEFormatter.price(1234.56);                // "EUR 1.234,56"
DEFormatter.percent(15.5);                 // "15,5 %"
DEFormatter.length(440);                   // "440 mm"
DEFormatter.weight(2.2);                   // "2,20 kg"
DEFormatter.time(75);                      // "1,3 h"
DEFormatter.quantity(29);                  // "29 Stck."
```

---

## Testing Checklist

### Datum:
- [ ] 06.02.2026 (heute)
- [ ] 06.03.2026 (in 4 Wochen)
- [ ] 31.12.2025 (letztes Jahr)

### Zahlen:
- [ ] 0,5 (Dezimal)
- [ ] 1.234,56 (Tausender)
- [ ] 12.345,67 (fünfstellig)

### Preise:
- [ ] EUR 26,30
- [ ] EUR 1.234,56
- [ ] EUR 0,00 (Null)

### Einheiten:
- [ ] 440 mm (Länge)
- [ ] 2,2 kg (Gewicht)
- [ ] 29 Stck. (Menge)
- [ ] 12,5 min (Zeit)
- [ ] 15 % (Prozent)

---

## Edge Cases

### 1. Sehr große Zahlen
```
1.234.567,89  ✅ (Million)
```

### 2. Negative Zahlen
```
-50,00  ✅
EUR -50,00  ✅
```

### 3. Null-Werte
```
0,00  ✅ (immer 2 Dezimalstellen)
0 mm  ✅ (keine Dezimalstellen bei Längen)
```

### 4. Rundung
```javascript
// Immer KAUFMÄNNISCH runden
Math.round(26.295 * 100) / 100  // 26.30 ✅
```

---

## Print-Formatierung

```css
@media print {
  /* Keine Änderungen nötig - deutsche Formate druckbar */
  .price, .date {
    font-size: 11pt;
  }
}
```

---

## Validation

**Browser-Test:**
```javascript
console.log(DEFormatter.date(new Date()));
console.log(DEFormatter.price(1234.56));
console.log(DEFormatter.length(440));
```

**Erwartete Ausgabe:**
```
06.02.2026
EUR 1.234,56
440 mm
```

---

*Research completed: 2026-02-06 03:17*  
*Sources: DIN 5008, MBS Angebot*  
*Library: Complete DEFormatter implementation*

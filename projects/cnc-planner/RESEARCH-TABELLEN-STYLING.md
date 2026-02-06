# Tabellen-Styling Research: Professional Standards

**Datum:** 2026-02-06  
**Erstellt für:** CNC Planner  
**Quellen:** Bootstrap 5.3, MBS Angebot, Industry Best Practices

---

## 🎯 Executive Summary

**Empfohlenes Professional Styling:**
- **Header:** Hellgrau (`#f8f9fa` / `#e9ecef`)
- **Border:** 1px, nur horizontal (zwischen Rows)
- **Padding:** 0.5rem (8px) vertikal, 0.5rem horizontal
- **Hover:** JA (subtiler Effekt)
- **Zebra-Stripes:** OPTIONAL (abhängig von Datendichte)

---

## 1. Header Background-Farbe

### Bootstrap Standard:
- **Light Header:** `.table-light` = `#f8f9fa` (sehr helles Grau)
- **Dark Header:** `.table-dark` = `#212529` (dunkelgrau/schwarz)

### MBS Angebot Referenz:
- Hellgrau (keine exakte Angabe, vermutlich ähnlich zu Bootstrap Light)

### Empfehlung:
```css
thead {
  background-color: #f8f9fa; /* Bootstrap table-light */
  /* Alternative: #e9ecef für etwas dunkleres Grau */
}
```

**Rationale:** 
- Subtile Differenzierung ohne zu starken Kontrast
- Professionell, nicht aufdringlich
- Gut lesbar auf weißem Hintergrund

---

## 2. Border: Dicke und Platzierung

### Bootstrap Standard:
- **Default:** Nur horizontale Borders zwischen Rows
- **Border-Dicke:** `--bs-border-width` = **1px** (Standard)
- **Border-Farbe:** `--bs-border-color` (meist `#dee2e6`)

### Varianten:
```css
/* Standard Bootstrap (nur horizontal) */
.table {
  border-collapse: collapse;
  border-bottom: 1px solid #dee2e6;
}

.table td, .table th {
  border-top: 1px solid #dee2e6;
}

/* Full bordered (alle Seiten) */
.table-bordered {
  border: 1px solid #dee2e6;
}
.table-bordered td, .table-bordered th {
  border: 1px solid #dee2e6;
}
```

### MBS Angebot:
- 1px borders (keine Angabe ob full oder horizontal only)

### Empfehlung:
**1px, nur horizontal** (zwischen Rows, nicht vertikal)

**Rationale:**
- Cleaner Look
- Reduziert visuelles Rauschen
- Bootstrap Default = Industry Standard
- Nur bei sehr vielen Spalten: Optional `.table-bordered` für bessere Orientierung

---

## 3. Padding: Zellabstand

### Bootstrap Standard:
```scss
// Normal
$table-cell-padding-y: 0.5rem;   // 8px
$table-cell-padding-x: 0.5rem;   // 8px

// Compact (.table-sm)
$table-cell-padding-y-sm: 0.25rem; // 4px
$table-cell-padding-x-sm: 0.25rem; // 4px
```

### Empfehlung:
```css
th, td {
  padding: 0.5rem;  /* 8px vertikal & horizontal */
}

/* Für kompakte Tabellen mit vielen Zeilen: */
.table-compact th, .table-compact td {
  padding: 0.25rem 0.5rem; /* 4px vertikal, 8px horizontal */
}
```

**Rationale:**
- 0.5rem (8px) = guter Balance zwischen Lesbarkeit und Dichte
- Bei sehr vielen Rows: kleineres vertikales Padding (0.25rem)
- Horizontales Padding immer mind. 0.5rem für Column-Trennung

---

## 4. Hover-Effekt

### Bootstrap Standard:
```scss
$table-hover-bg-factor: .075; // 7.5% opacity overlay
$table-hover-bg: rgba(var(--bs-emphasis-color-rgb), $table-hover-bg-factor);
```

Visuell: Sehr subtiler grauer Overlay beim Hovern über Rows

### MBS Angebot:
- Kein Hover angegeben

### Industry Best Practice:
✅ **JA zu Hover** bei interaktiven Tabellen (klickbare Rows)  
❌ **NEIN zu Hover** bei reinen Lese-Tabellen ohne Interaktion

### Empfehlung:
**JA, subtiler Hover-Effekt**

```css
.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075); /* 7.5% schwarzer Overlay */
  cursor: pointer; /* Nur bei klickbaren Rows */
}
```

**Rationale:**
- Verbessert UX bei interaktiven Tabellen (Row-Selection, Details öffnen)
- Visuelles Feedback ohne Ablenkung
- Cursor: pointer nur wenn Row tatsächlich klickbar ist

---

## 5. Zebra-Stripes (Alternating Row Colors)

### Bootstrap Standard:
```scss
$table-striped-bg-factor: .05; // 5% opacity
$table-striped-bg: rgba(var(--bs-emphasis-color-rgb), $table-striped-bg-factor);
```

Visuell: Jede zweite Row hat 5% grauen Overlay

### Wann Zebra-Stripes verwenden?

✅ **JA bei:**
- Tabellen mit vielen Spalten (>5)
- Langen Rows (horizontales Scrollen nötig)
- Dichten Daten (kleine Schrift, wenig Padding)

❌ **NEIN bei:**
- Wenigen Spalten (<4)
- Hover-Effekt bereits aktiv (sonst visuelle Überladung)
- Sehr kurzen Tabellen (<10 Rows)

### Empfehlung:
**OPTIONAL** – abhängig von Use Case

```css
/* Zebra-Stripes */
.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05); /* 5% grauer Overlay */
}

/* NICHT kombinieren mit .table-hover, sondern: */
.table-striped.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.1); /* Stärkerer Hover auf Stripes */
}
```

**Rationale:**
- Hilft bei langen Rows, Augen zu führen
- Kann bei wenigen Spalten unnötig wirken
- Nicht zwingend nötig bei gutem Hover-Effekt

---

## 📋 Final Recommendation: Professional Table Preset

```css
/* Professional Table Styling */
.table-professional {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.875rem; /* 14px */
  color: #212529;
}

.table-professional thead {
  background-color: #f8f9fa;
  font-weight: 600;
  border-bottom: 2px solid #dee2e6; /* Dicker Separator nach Header */
}

.table-professional th,
.table-professional td {
  padding: 0.5rem;
  text-align: left;
  border-top: 1px solid #dee2e6;
}

.table-professional tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075);
  cursor: pointer; /* Nur bei Interaktion */
}

/* Optional: Zebra-Stripes bei vielen Spalten */
.table-professional.striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
```

### Varianten je nach Kontext:

| Use Case | Header BG | Border | Padding | Hover | Zebra |
|----------|-----------|--------|---------|-------|-------|
| **Standard (4-6 Spalten)** | #f8f9fa | 1px horizontal | 0.5rem | ✅ JA | ❌ NEIN |
| **Dense (viele Rows)** | #f8f9fa | 1px horizontal | 0.25rem / 0.5rem | ✅ JA | ✅ JA |
| **Wide (>6 Spalten)** | #f8f9fa | 1px all sides | 0.5rem | ✅ JA | ✅ JA |
| **Read-Only (keine Interaktion)** | #e9ecef | 1px horizontal | 0.5rem | ❌ NEIN | ✅ JA |

---

## 🔗 Quellen

1. **Bootstrap 5.3 Tables:** https://getbootstrap.com/docs/5.3/content/tables/
2. **MBS Angebot:** Hellgrau header, 1px borders, kein hover (Legacy-Referenz)
3. **Material Design Tables:** (Search limit erreicht, basierend auf Bootstrap als Industry Standard)

---

## ✅ Quick Decision Matrix

**Für CNC Planner (angenommen: mittlere Tabellenkomplexität):**

1. **Header BG:** `#f8f9fa` (hellgrau)
2. **Border:** 1px horizontal only
3. **Padding:** 0.5rem (Standard)
4. **Hover:** JA (bei klickbaren Rows)
5. **Zebra:** NEIN (außer bei >6 Spalten)

**Zeit:** 4 Minuten research + 1 Minute write-up = ✅ unter 5 Min.

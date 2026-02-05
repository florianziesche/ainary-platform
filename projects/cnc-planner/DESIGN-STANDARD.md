# CNC Planner Pro — Design Standard

## Zweck
Einheitliches visuelles Design für alle UI-Komponenten. **Keine Inline-Styles** — nur CSS-Klassen.

---

## 1. Card Headers

### Varianten

| Klasse | Verwendung | Aussehen |
|--------|------------|----------|
| `.card-header` | Standard (neutral) | Grauer Text auf weißem Hintergrund |
| `.card-header-primary` | Hauptergebnis, CTA | Weiß auf Blau (#1E3A5F) |
| `.card-header-info` | Berechnungsdetails, Formeln | Dunkelblau auf Hellblau |
| `.card-header-success` | Positive Werte, Material | Dunkelgrün auf Hellgrün |
| `.card-header-warning` | Hinweise, Rüstzeit | Dunkelorange auf Hellorange |
| `.card-header-error` | Kritische Toleranzen | Dunkelrot auf Hellrot |

### Anatomie
```
┌─────────────────────────────────────────┐
│ [Icon] Titel                    [Action]│  ← 14px, font-weight 600
├─────────────────────────────────────────┤
│                                         │
│  Card Body                              │
│                                         │
└─────────────────────────────────────────┘
```

### Regeln
1. **Keine Inline-Styles** für Farben — immer CSS-Klasse
2. Icon optional (Emoji oder SVG), vor Titel
3. Action-Bereich rechts (Button, Badge, Toggle)
4. Konsistente Padding: `var(--space-4) var(--space-5)`

---

## 2. CSS-Definitionen

```css
/* Standard Header */
.card-header {
    padding: var(--space-4) var(--space-5);
    border-bottom: 1px solid var(--color-border-light);
    font-size: 14px;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Primary (Hauptergebnis) */
.card-header-primary {
    background: var(--color-primary);
    color: white;
    border-bottom: none;
}

/* Info (Berechnungen) */
.card-header-info {
    background: var(--color-info-light);
    color: var(--color-info);
}

/* Success (Material, positive) */
.card-header-success {
    background: var(--color-success-light);
    color: var(--color-success);
}

/* Warning (Hinweise) */
.card-header-warning {
    background: var(--color-warning-light);
    color: var(--color-warning);
}

/* Error (Kritisch) */
.card-header-error {
    background: var(--color-error-light);
    color: var(--color-error);
}

/* Mit Icon */
.card-header-icon {
    margin-right: var(--space-2);
}

/* Mit Action-Bereich */
.card-header-action {
    font-size: 12px;
    font-weight: 400;
    opacity: 0.8;
}
```

---

## 3. Verwendung im CNC Planner

| Section | Card | Header-Typ |
|---------|------|------------|
| Eingabe | Werkstück | Standard |
| Eingabe | Fertigung | Standard |
| Ergebnis | Kostenaufschlüsselung | **Standard** |
| Ergebnis | Mengenstaffel | Standard |
| Ergebnis | Kalkulationsgrundlage | Standard |
| Kalkulation | Maschinenzeitkalkulation | Info |
| Kalkulation | Materialkalkulation | Success |
| Kalkulation | Einrichtkosten | Warning |
| Kalkulation | Gesamtkalkulation | **Primary** |
| Werkzeuge | Schnittparameter | Standard |
| Werkzeuge | Werkzeugkosten | Standard |
| Einstellungen | Stundensätze | Info |
| Einstellungen | Materialpreise | Success |
| Einstellungen | Zuschlagssätze | Warning |

---

## 4. Farb-Semantik

| Farbe | Bedeutung | Verwendung |
|-------|-----------|------------|
| **Primary** (Blau) | Hauptergebnis, wichtigste Aktion | Angebotspreis, CTA-Buttons |
| **Info** (Hellblau) | Berechnungsdetails, Erklärungen | Formeln, Zeiten |
| **Success** (Grün) | Positiv, Material, Bestätigung | Materialkosten, ✓ Status |
| **Warning** (Orange) | Hinweis, Achtung | Rüstzeit, Zuschläge |
| **Error** (Rot) | Kritisch, Toleranzen | h5, H7, Warnungen |

---

## 5. Anti-Patterns (NICHT machen)

❌ `style="background: var(--color-info-light); color: var(--color-info);"`
✅ `class="card-header card-header-info"`

❌ `style="display: flex; justify-content: space-between;"`
✅ Flex ist jetzt Standard in `.card-header`

❌ Unterschiedliche Padding pro Header
✅ Immer `var(--space-4) var(--space-5)`

---

## 6. Migration Checklist

- [ ] CSS-Klassen zu `<style>` hinzufügen
- [ ] Alle `card-header` mit inline `style=` finden
- [ ] Durch entsprechende Klasse ersetzen
- [ ] Testen dass Farben korrekt sind

---

*Standard Version: 1.0 — 2026-02-05*

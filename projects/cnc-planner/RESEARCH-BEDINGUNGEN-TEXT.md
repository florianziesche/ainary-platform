# Research: Bedingungen-Text in Angeboten

**Feature:** Rechtliche Bedingungen, AGB-Hinweise, Disclaimer  
**Datum:** 2026-02-06 03:15

---

## Research-Fragen

1. Welche Bedingungen sind Standard?
2. Wo stehen sie? (Nach Tabelle, vor Footer?)
3. Wie lang dürfen sie sein?
4. Schriftgröße?
5. Müssen AGB verlinkt werden?

---

## MBS Angebot Findings

**Bedingungen im MBS Angebot (Seite 2):**

```
Unser Angebot ist freibleibend mit einer Gültigkeit von 4 Wochen.

Die Preiskalkulation basiert auf derzeit gültigen Materialaufschlagspreisen 
/ Zustellpreisen. Änderungen innerhalb der Angebotsgültigkeit behalten sich 
eventuelle Nachkalkulationen und Anpassungen vor bei stark schwankenden 
Marktpreisen.

Für Bestellungen unter 100,- € Warenwert berechnen wir einen 
Mindermengenzuschlag von pauschal 35,-€.

Kommen Sonderwünsche und Kundenwünsche zum Einsatz, so behalten wir uns, 
eventuell vorhandene Restmaterial separat in Rechnung zu stellen. Gleiches 
gilt für eventuell erforderliche Sonderverpackungen.
```

**Formatierung:**
- Position: Nach Haupttabelle, vor Footer
- Schriftgröße: 9-10pt (kleiner als Body)
- Absätze: Mit Leerzeile getrennt
- Keine Nummerierung
- Keine Überschrift

---

## Rechtliche Standards (Deutschland)

### 1. BGB § 145-156 (Angebotsbindung)

**Pflicht-Hinweise:**
- Angebot "freibleibend" oder "bindend"?
- Gültigkeitsdauer
- Preisänderungsvorbehalt

**MBS-Lösung:** "freibleibend mit einer Gültigkeit von 4 Wochen" ✅

### 2. Preisangabenverordnung (PAngV)

**Pflicht:**
- Preise inkl. MwSt. (B2C) ODER "zzgl. MwSt." (B2B)
- Gesamtpreis sichtbar

**MBS-Lösung:** Netto-Preise (B2B Standard) ✅

### 3. AGB-Einbindung (BGB § 305)

**Erforderlich:**
- Hinweis auf AGB
- Zugang zu AGB ermöglichen

**Optionen:**
```
1. "Es gelten unsere Allgemeinen Geschäftsbedingungen (siehe Rückseite)"
2. "Es gelten unsere AGB unter www.firma.de/agb"
3. "AGB liegen diesem Angebot bei"
```

**MBS:** Keine explizite AGB-Referenz im Beispiel (vermutlich auf Rückseite)

---

## Standard-Bedingungen (Maschinenbau)

### Typische Klauseln:

1. **Angebotsgültigkeit:**
   ```
   "Unser Angebot ist freibleibend mit einer Gültigkeit von [X] Wochen."
   ```

2. **Preisänderungsvorbehalt:**
   ```
   "Bei stark schwankenden Material- oder Energiepreisen behalten wir uns 
   Preisanpassungen vor."
   ```

3. **Mindermengenzuschlag:**
   ```
   "Bei Bestellungen unter [X] € berechnen wir einen Mindermengenzuschlag 
   von [Y] €."
   ```

4. **Lieferzeit:**
   ```
   "Lieferzeit ca. [X] Wochen nach Auftragseingang (abhängig von 
   Materialverfügbarkeit)."
   ```

5. **Zahlungsbedingungen:**
   ```
   "[X] Tage netto nach Rechnungsdatum."
   "2% Skonto bei Zahlung innerhalb 14 Tagen."
   ```

6. **Sonderwünsche:**
   ```
   "Sonderwünsche können zu Mehrkosten führen."
   ```

7. **Toleranzen:**
   ```
   "Liefermenge ±10% toleriert."
   "Maßtoleranzen nach DIN ISO 2768-m."
   ```

---

## Best Practice Synthesis

### ✅ EMPFEHLUNG:

**Abschnitte (in dieser Reihenfolge):**

1. **Angebotsgültigkeit** (prominent, Info-Box)
2. **Preiskalkulation-Hinweis** (nach Tabelle)
3. **Zahlungsbedingungen**
4. **Lieferzeit**
5. **Mindermengenzuschlag** (wenn relevant)
6. **Sonderwünsche-Hinweis** (optional)
7. **AGB-Referenz**

---

## Implementation Plan

### HTML Structure:

```html
<!-- Prominent: Gültigkeit als Info-Box -->
<div class="info-box" style="margin: var(--space-6) 0;">
  <strong>Angebotsgültigkeit:</strong> 
  Freibleibend mit einer Gültigkeit von 4 Wochen 
  (bis <strong>06.03.2026</strong>)
</div>

<!-- Bedingungen als Text-Block -->
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
    2% Skonto bei Zahlung innerhalb 14 Tagen.
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
  
  <p class="agb-reference">
    Es gelten unsere Allgemeinen Geschäftsbedingungen. 
    <a href="https://firma.de/agb" target="_blank">AGB ansehen</a>
  </p>
</div>
```

### CSS Styling:

```css
.terms-block {
  margin: var(--space-8) 0;
  padding: var(--space-6);
  background: var(--color-bg-subtle);
  border-radius: var(--radius);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: var(--leading-relaxed);
}

.terms-block p {
  margin-bottom: var(--space-4);
}

.terms-block p:last-child {
  margin-bottom: 0;
}

.terms-block strong {
  color: var(--color-text);
  font-weight: var(--font-semibold);
}

.agb-reference {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  border-top: 1px solid var(--color-border-light);
  padding-top: var(--space-4);
  margin-top: var(--space-4);
}

.agb-reference a {
  color: var(--color-primary);
  text-decoration: underline;
}
```

---

## Edge Cases

### 1. B2C vs. B2B
```javascript
const showMwSt = customerType === 'B2C';
const text = showMwSt 
  ? "Alle Preise inkl. 19% MwSt."
  : "Alle Preise zzgl. 19% MwSt.";
```

### 2. Internationale Kunden
```
"Delivery terms: Ex Works (EXW) according to Incoterms 2020"
```

### 3. Lange Lieferzeiten
```
"Delivery time approx. 18 weeks (subject to material availability)"
```

### 4. Sonder-Konditionen
```html
<p class="highlight">
  <strong>Sonderkonditionen:</strong> 
  Bei Abnahme von >50 Stück: -10% Mengenrabatt
</p>
```

---

## Validation Criteria

### Legal:
- ✅ Angebotsbindung geklärt (freibleibend/bindend)
- ✅ Gültigkeit angegeben
- ✅ Preisänderungsvorbehalt (bei volatilen Märkten)
- ✅ AGB-Referenz vorhanden

### User-Friendly:
- ✅ Kurz & prägnant (keine Romane)
- ✅ Wichtige Punkte FETT
- ✅ Absätze übersichtlich
- ✅ Nicht versteckt (prominent nach Tabelle)

### Professional:
- ✅ Wie MBS Angebot
- ✅ Branchenüblich
- ✅ Rechtssicher

---

## Testing Checklist

- [ ] Text sichtbar nach Tabelle
- [ ] Schriftgröße lesbar (13-14px)
- [ ] Gültigkeit prominent als Info-Box
- [ ] AGB-Link funktioniert
- [ ] Print-Layout OK

---

*Research completed: 2026-02-06 03:15*  
*Sources: MBS Angebot, BGB, PAngV, Maschinenbau Best Practices*  
*Decision: Wie MBS - kurz, prägnant, rechtssicher*

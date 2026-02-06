# MBS Angebot - Design Analyse

**Quelle:** `/Users/florianziesche/Downloads/2026-02-05 23-36.pdf`  
**Datum:** 2026-02-06 00:40  
**Analysiert:** Seite 1 (Screenshot vorhanden)

---

## 📸 Visuelle Analyse

### Logo & Header (Oben rechts)
```
MBS
Maschinenbau
Schlottwitz GmbH & Co. KG
```

**Design:**
- Logo: Großes, fettes "MBS" in Schwarz (vermutlich Arial Black oder ähnlich)
- Schrift: Serifenlos, Industrial
- Ausrichtung: Rechtsbündig
- Separator: Horizontale Linie unter Logo

**Farben:**
- Schwarz für Logo
- Schwarz für Firmennamen
- Grau (#666 oder ähnlich) für Rechtsform

---

## 📋 Dokumenten-Header

### Linke Spalte (Absender)
```
Maschinenbau Schlottwitz GmbH & Co. KG, Glashütter Str. 25, 01768 Glashütte

Müller Industrie GmbH
Hauptstraße 26
09619 Mulda
```

**Formatierung:**
- Klein gedruckter Absender (8-9pt, Grau)
- Empfänger: Standard Größe (10-11pt, Schwarz)
- Abstand: ~2cm von oben

### Rechte Spalte (Angebotsdaten)
```
Angebot         20260072
Datum           28.01.2026
Kunden-Nr.      10661
Ihr Zeichen     2500473.91
Vom             27.01.2026
Bearbeiter      Sebastian Uhlig
Telefon-Nr.     035053 412 23
E-Mail          info@mbs-schlottwitz.de
```

**Formatierung:**
- Label: Fett, linksbündig
- Wert: Normal, rechtsbündig oder direkt daneben
- Schriftgröße: 9-10pt
- Zeilenabstand: Eng (1.2-1.3)

---

## 📧 Anrede & Einleitung

```
Sehr geehrte Damen und Herren

wir bedanken uns für Ihre Anfrage und bieten Ihnen gerne, wie folgt an:
```

**Formatierung:**
- Standard-Schrift (10-11pt)
- Blocksatz oder linksbündig
- Abstand zum Header: ~1cm
- Abstand zur Tabelle: ~0.5cm

---

## 📊 Haupt-Tabelle

### Spalten-Struktur

| Pos | Artikelnummer | Bezeichnung | Menge | Einzelpreis | Gesamtpreis |
|-----|---------------|-------------|-------|-------------|-------------|

**Spalten-Breiten (geschätzt):**
- Pos: 5% (40px)
- Artikelnummer: 12% (100px)
- Bezeichnung: 45% (360px)
- Menge: 10% (80px)
- Einzelpreis: 14% (110px)
- Gesamtpreis: 14% (110px)

### Header-Zeile

**Formatierung:**
- Hintergrund: Hellgrau (#F0F0F0 oder ähnlich)
- Schrift: Fett, 9-10pt
- Text: Schwarz
- Padding: 4-6px vertikal
- Border: 1px solid #CCC

### Daten-Zeilen

**Beispiel Zeile:**
```
10  E-STI-0001  Platte                        10 Stück  98,10   981,00
                Zchng Nr. 2500473.01.01.02.01.001
```

**Formatierung Position-Nummer (10, 20, 30...):**
- Fett
- Linksbündig

**Formatierung Artikelnummer:**
- Normal
- Monospace oder tabular nums

**Formatierung Bezeichnung:**
- Zeile 1: Fett (Produktname)
- Zeile 2: Normal, Grau, kleiner (Zeichnungsnummer)
- Einrückung Zeile 2: ~10px

**Formatierung Menge:**
- Rechtsbündig
- Mit Einheit ("Stück")
- Tabular nums

**Formatierung Preise:**
- Rechtsbündig
- Tabular nums
- Deutscher Format: `981,00` (Komma als Dezimal)
- KEINE Währungszeichen in Zellen

### Zeilen-Abstand

- Border-bottom: 1px solid #E5E5E5
- Padding: 8-10px vertikal
- Bei mehrzeiligen Zellen: Extra Padding unten

---

## 📝 Footer-Bereich (Unter Tabelle)

### Übertrag-Zeile
```
Seite 1 von 2
────────────────────────────────────────────────
                                    Übertrag  3.843,36
```

**Formatierung:**
- Seitenzahl: Links
- Trennlinie: Gestrichelt oder durchgezogen
- Übertrag: Rechtsbündig, Fett
- Position: Am Ende der Seite

---

## 🔍 Hinweise & Bedingungen (Seite 2, vermutlich)

**Erwartete Textblöcke:**

1. **Lieferbedingungen**
```
Unser Angebot ist freibleibend mit einer Gültigkeit von 4 Wochen
```

2. **Preiskalkulation**
```
Die Preiskalkulation basiert auf derzeitig gültigen Materialaufschlagspreisen...
```

3. **Zahlungsbedingungen**
```
Für Bestellungen unter 100,- € Warenwert berechnen wir einen 
Mindermengenzuschlag von pauschal 35,-€
```

**Formatierung:**
- Schriftgröße: 8-9pt
- Zeilenabstand: 1.3-1.5
- Absätze: Mit Leerzeile getrennt
- Wichtige Begriffe: NICHT fett (schlicht)

---

## 📞 Kontaktdaten Footer (Seite 2, unten)

```
Maschinenbau Schlottwitz GmbH & Co. KG
Glashütter Str. 25, 01768 Glashütte

Geschäftsführer:        [Name]
Handelsregister:        [Nummer]
Registergericht:        Dresden
USt-ID:                 DE 173219619

Bankverbindung:         Sparkasse [...] | Dresden
                        IBAN: [...] | BIC: [...]
```

**Formatierung:**
- Sehr klein (7-8pt)
- Grau (#666 oder ähnlich)
- Linksbündig oder 2-Spalten
- Kompakt, wenig Zeilenabstand

---

## 🎨 Farbpalette (extrahiert)

```css
/* Primär */
--mbs-black: #000000;           /* Logo, Haupttext */
--mbs-gray-dark: #333333;       /* Sekundärtext */
--mbs-gray: #666666;            /* Metadaten */
--mbs-gray-light: #999999;      /* Hints */

/* Hintergründe */
--mbs-bg: #FFFFFF;              /* Seite */
--mbs-bg-table-header: #F0F0F0; /* Tabellen-Header */
--mbs-bg-alt: #FAFAFA;          /* Alternate rows (vermutlich) */

/* Borders */
--mbs-border: #CCCCCC;          /* Tabellen-Rahmen */
--mbs-border-light: #E5E5E5;    /* Zeilen-Trenner */
```

**Keine bunten Farben!** Alles Schwarz/Grau/Weiß.

---

## 📝 Typografie

### Schriftart (geschätzt)
- **Haupt-Font:** Arial, Helvetica, oder ähnlich Sans-Serif
- **Logo:** Arial Black oder ähnlich (fett, kompakt)
- **Zahlen:** KEINE spezielle Monospace, aber tabular alignment

### Schriftgrößen
```css
--text-logo: 28-32pt;
--text-company: 11-12pt;
--text-header: 10-11pt (Anrede, Einleitung);
--text-body: 10pt (Tabelle Daten);
--text-table-header: 9-10pt;
--text-small: 8-9pt (Bedingungen);
--text-tiny: 7-8pt (Footer Kontaktdaten);
```

### Schriftgewichte
- **Fett:** Position-Nummern, Produkt-Namen, Labels
- **Normal:** Alles andere
- **Keine Light/Thin Weights**

---

## 📐 Spacing & Layout

### Seiten-Margins
- Oben: ~2cm
- Unten: ~2cm  
- Links: ~2cm
- Rechts: ~2cm

### Element-Abstände
- Logo zu Anschrift: ~1.5cm
- Anschrift zu Tabelle: ~1cm
- Tabellen-Zeilen: 8-10px padding
- Zwischen Absätzen: 0.5-1cm

### Tabellen-Padding
- Header: 6-8px vertikal, 8-10px horizontal
- Zellen: 8-10px vertikal, 8-10px horizontal

---

## 🎯 Design-Prinzipien (erkannt)

1. **Extrem nüchtern** — Keine Dekoration
2. **Maximale Lesbarkeit** — Klare Hierarchie
3. **Schwarz/Weiß/Grau** — Keine Farben
4. **Tabular Zahlen** — Rechtsbündig, gut lesbar
5. **Kompakte Information** — Keine Verschwendung von Raum
6. **Professionell/Industrial** — Seriös, vertrauenswürdig
7. **Zeichnungsnummer prominent** — Unter Produktname
8. **Deutsche Formatierung** — Komma als Dezimal, Punkt als Tausender
9. **Keine Emojis/Icons** — NUR Text
10. **Standard-Geschäftsbrief-Layout** — DIN 5008 ähnlich

---

## 🔑 Key Learnings

### Must-Have für CNC Planer Pro:

1. **Zeichnungsnummer unter Bauteil-Name**
   - Format: `Zchng Nr. XXXX.XX.XX.XX.XX.XXX`
   - Grau, kleiner, eingerückt

2. **Position-Nummerierung**
   - 10, 20, 30, 40... (Nicht 1, 2, 3...)
   - Erlaubt Einfügen zwischen Positionen

3. **Tabellen-Header hell hinterlegt**
   - Hellgrau (#F0F0F0)
   - Nicht weiß

4. **Preise OHNE € in Zellen**
   - Nur Zahlen: `981,00`
   - Spalten-Header: "Einzelpreis" / "Gesamtpreis" (ohne €)

5. **Übertrag am Seitenende**
   - Bei mehrseitigen Angeboten
   - Summe rechtsbündig

6. **Footer mit Rechtlichem**
   - Sehr klein (7-8pt)
   - Grau
   - Kompakt

7. **Gültigkeit explizit angeben**
   - "freibleibend mit einer Gültigkeit von 4 Wochen"
   
8. **Bedingungen-Text**
   - Materialpreise-Hinweis
   - Mindermengenzuschlag
   - Zahlungsbedingungen

---

## 📦 Nächste Schritte

1. **Design-System erstellen** basierend auf dieser Analyse
2. **CSS-Variablen definieren** (MBS Farbpalette)
3. **Komponenten-Bibliothek** (Tabelle, Header, Footer)
4. **Template erstellen** für Angebot
5. **Validieren** mit Florian

---

*Analysiert: 2026-02-06 00:40*  
*Basis: Screenshot Seite 1*  
*Für: cnc-planner-pro-industrial.html*

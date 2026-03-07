# DESIGN-EXPRESSIONS.md — Same System, Different Expression

*Wie Apple: Ein Design-System, mehrere Ausdrucksformen je nach Kontext und Zielgruppe.*
*Stand: 2026-03-05*

---

## Prinzip

**Das System ist konstant. Die Expression variiert.**

Apple nutzt SF Pro überall — aber apple.com/iphone (light, premium) sieht anders aus als Apple TV+ (dark, cinematic). Gleiche Schrift, gleiche Radii, gleiche Spacing-Regeln. Nur Modus, Farbtemperatur und Informationsdichte ändern sich.

Palantir macht dasselbe: Gotham (dark, analyst) ≠ Foundry (lighter, operator) ≠ Blog (light, editorial). Blueprint-Design-System ist identisch.

Linear ist der Gegenpol: Ein Produkt, ein Look. Monochrom überall. Kein Bedarf für Differenzierung.

**Wir sind wie Apple/Palantir:** Mehrere Produkte, mehrere Zielgruppen, ein System.

---

## Das System (KONSTANT — nie ändern)

### Typografie
```
Display + Body: Inter (Variable/Display)
Mono (Zahlen, Labels, Code): JetBrains Mono
```

### Brand-Akzent
```
Gold — immer. Hex variiert nach Modus (siehe Expressions).
Maximal 3-5 Gold-Elemente pro Viewport.
```

### Semantische Farben (4 Intents)
```
Grün  = Evidenz / Bestätigt / Positiv    (Blueprint: Success)
Blau  = Interpretation / Analytisch       (Blueprint: Primary)
Orange = Judgment / Achtung               (Blueprint: Warning)
Rot   = Assumption / Kritisch / Fehler   (Blueprint: Danger)
```
Hex-Werte variieren nach Light/Dark — Bedeutung bleibt identisch.

### Layout-Regeln
```
Card-Radius: 8px
Card-Border: 1px solid (Farbe nach Modus)
Spacing: 8px Basis-Grid
Max-Width: 820-1040px (Content-Typ abhängig)
```

### Trust-System
```
EIJA-Badges auf jedem Fakt
Admiralty-Code auf jeder Quelle
Confidence-Bar wo sinnvoll
```

### Shared Components
```
Inter + JetBrains Mono (Google Fonts)
Brand-Dot (●) + "Ainary" 
Footer mit Impressum/Datenschutz
```

---

## Expressions (VARIABEL — je nach Kontext)

### Expression 1: Editorial (Blog, Artikel)

**Zielgruppe:** Public, Tech-Audience, Build-in-Public
**Modus:** Dark
**Stimmung:** Editorial, authoritative, thought leadership

| Token | Wert |
|---|---|
| Background | `#08080c` |
| Surface | `#111116` |
| Text Primary | `#ededf0` |
| Text Secondary | `#8b8b95` |
| Text Muted | `#55555e` |
| Gold | `#c8aa50` |
| Border | `rgba(255,255,255,0.06)` |

**Informationsdichte:** Niedrig. Viel Whitespace. Hero-Grafiken.
**Bildsprache:** Monochrome SVG-Grafiken, keine Fotos.
**Referenz:** Linear Blog, Stripe Blog.

---

### Expression 2: Intelligence / Analyst (Dossier, Schüller)

**Zielgruppe:** Analysten, Kandidaten, Management
**Modus:** Dark (Palantir Blueprint)
**Stimmung:** Command Center, datengetrieben, Gotham-Feeling

| Token | Wert | Blueprint-Name |
|---|---|---|
| Background | `#111418` | BLACK |
| Surface | `#1C2127` | DARK_GRAY1 |
| Surface Elevated | `#252A31` | DARK_GRAY2 |
| Border | `#2F343C` | DARK_GRAY3 |
| Text Primary | `#F6F7F9` | LIGHT_GRAY5 |
| Text Secondary | `#ABB3BF` | GRAY4 |
| Text Muted | `#8F99A8` | GRAY3 |
| Gold | `#D1980B` | GOLD3 |
| Green | `#238551` | GREEN3 |
| Blue | `#2D72D2` | BLUE3 |
| Orange | `#C87619` | ORANGE3 |
| Red | `#CD4246` | RED3 |

**Informationsdichte:** Hoch. Sidebar, Tabs, Graphen, Heatmaps.
**Bildsprache:** Keine. Daten sind die Bilder.
**Referenz:** Palantir Gotham/Foundry, Bloomberg Terminal.

---

### Expression 3: Executive Briefing (Gleißberg Portal)

**Zielgruppe:** Bürgermeister, Entscheider, nicht-technisch
**Modus:** Light
**Stimmung:** Morgenzeitung, vertrauenswürdig, warm, klar

| Token | Wert |
|---|---|
| Background | `#ffffff` |
| Surface | `#fafafa` |
| Text Primary | `#1a1a1a` |
| Text Secondary | `#444444` |
| Text Muted | `#777777` |
| Gold | `#9d7f3b` (dunkler — WCAG AA auf weiß) |
| Gold Pale | `rgba(200,170,80,0.08)` |
| Border | `#d0d0d0` |
| Border Subtle | `#e8e8e8` |
| Green | `#2d8a4e` |
| Blue | `#2b6cb0` |
| Amber | `#b45309` |
| Red | `#c0392b` |

**Informationsdichte:** Mittel. 12-16 Items pro Briefing. Klare Hierarchie.
**Bildsprache:** Keine. Text + strukturierte Karten.
**Referenz:** Apple product pages, McKinsey Briefings, The Economist.

---

### Expression 4: Client Report (KI-001, PDF-Äquivalente)

**Zielgruppe:** Kunde (Kandidat, GF), wird weitergeleitet
**Modus:** Light (warm)
**Stimmung:** Professionell, wie gedruckter Bericht, wertig

| Token | Wert |
|---|---|
| Background | `#fafaf8` (warm-weiß) |
| Surface/Callout | `#f5f4f0` |
| Text Primary | `#1a1a1a` |
| Gold | `#c8aa50` |
| Accent Dark Green | `#1a5c2a` |
| Accent Dark Red | `#991b1b` |

**Informationsdichte:** Fokussiert. 1 Frage = 1 Sektion. Cover + Back Cover.
**Bildsprache:** Keine. Tabellen, Vergleiche, Badges.
**Layout:** `.page` mit Print-Optimierung, noindex/nofollow.
**Referenz:** McKinsey/BCG Reports, Palantir Case Studies.

---

## Entscheidungsbaum: Welche Expression?

```
Neues Produkt / Seite:
│
├─ Wer liest es?
│  ├─ Public / Tech → Expression 1 (Editorial Dark)
│  ├─ Analyst / Data-User → Expression 2 (Intelligence Dark)
│  ├─ Entscheider / Nicht-technisch → Expression 3 (Executive Light)
│  └─ Kunde (wird weitergeleitet) → Expression 4 (Client Report Light)
│
├─ Wie oft wird es gelesen?
│  ├─ Täglich/Wöchentlich → Expression 3 (scannt schnell)
│  ├─ Bei Bedarf (Deep Dive) → Expression 2 (hohe Dichte OK)
│  └─ Einmalig (Deliverable) → Expression 4 (muss sofort wirken)
│
└─ Auf welchem Gerät?
   ├─ Handy/Tablet morgens → Expression 3 (Light, große Schrift)
   ├─ Desktop mit Zeit → Expression 2 (Dark, hohe Dichte)
   └─ PDF/Print → Expression 4 (Print-optimiert)
```

---

## Gold-Kontrast-Regel

| Modus | Gold-Hex | Auf Background | Contrast Ratio | WCAG |
|---|---|---|---|---|
| Dark `#08080c` | `#c8aa50` | ~7.2:1 | ✅ AAA |
| Dark Blueprint `#111418` | `#D1980B` | ~5.8:1 | ✅ AA |
| Light `#ffffff` | `#9d7f3b` | ~4.1:1 | ✅ AA (large text) |
| Light warm `#fafaf8` | `#c8aa50` | ~3.0:1 | ⚠️ Nur dekorativ |

**Regel:** Gold auf Light-Backgrounds MUSS dunkler sein. `#c8aa50` auf weiß = FAIL für Text.

---

## Anti-Patterns

- ❌ Dark Mode für Bürgermeister-Briefings (zu technisch, zu "Hacker")
- ❌ Light Mode für Intelligence-Dashboards (zu harmlos, kein Command-Center-Feeling)
- ❌ Gleiche Gold-Hex für Light und Dark (Kontrast-Verletzung)
- ❌ Farbe ohne semantische Bedeutung (Deko-Farben)
- ❌ Mehr als 4 semantische Farben (Intent-Inflation)
- ❌ Expression mischen innerhalb einer Seite (z.B. Dark Header + Light Content)

---

*Quellen: Apple HIG, Palantir Blueprint (Open Source), Linear Design, COLOR-SYSTEM.md, BRAND.md*

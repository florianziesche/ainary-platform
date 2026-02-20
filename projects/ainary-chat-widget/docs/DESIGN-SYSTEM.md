# Ainary Design System v6

> Referenzdesign: `daily-intel-buergermeister-print.html` (DIN 1426 Print-Stil)
> Alle Seiten — Portal und Reports — folgen diesem System.

## 1. Designphilosophie

**"Bertelsmann Stiftung trifft Palantir."**
Seriös wie ein Forschungsbericht. Klar wie ein Dashboard. Ehrlich wie ein Beipackzettel.

### Prinzipien (Rangfolge)
1. **Klarheit** — Jedes Element muss sofort verstanden werden
2. **Weniger Schritte** — Ein Klick statt zwei. Direkter Link statt "soll ich öffnen?"
3. **Ehrlichkeit** — Confidence angeben. Ranges statt Punktwerte. Keine Garantien.
4. **Ruhe** — Monochrom. Wenig Farbe. Farbe nur wenn sie Information trägt.
5. **Konsistenz** — Gleicher Header, gleicher Footer, gleiche Typografie überall.

### Anti-Patterns (NICHT machen)
- ❌ Farbige Icons als Dekoration (Information muss im Text stehen, nicht im Icon)
- ❌ Badges mit Hintergrund+Border (zu laut, einfacher Text reicht)
- ❌ Modale Dialoge für wichtige Inhalte (eigene Seite, wie Claude/ChatGPT)
- ❌ Empfehlungen in Chat-Antworten (Fakten + direkter Link, keine ungebetene Beratung)
- ❌ Runde Euro-Beträge als Versprechen (Ranges mit Confidence)
- ❌ Mehr als 3 Farben gleichzeitig
- ❌ Dropdowns (Tiles/Karten stattdessen, Dropdown nur ab >10 Items)

---

## 2. Farben

### Palette
| Rolle | Farbe | Hex | Wann verwenden |
|---|---|---|---|
| **Hintergrund** | Warmweiß | `#fafaf8` | Seitenhintergrund |
| **Oberfläche** | Weiß | `#fff` | Cards, Eingabefelder |
| **Oberfläche 2** | Hellgrau | `#f5f5f3` | KPI-Karten, Hover-States |
| **Text** | Schwarz | `#1a1a1a` | Titel, Zahlen, Werte |
| **Text 2** | Dunkelgrau | `#555` | Fließtext, Labels |
| **Muted** | Mittelgrau | `#999` | Meta-Infos, Beschreibungen |
| **Light** | Hellgrau | `#bbb` | Fußnoten, Timestamps, Methodik-Hinweise |
| **Border** | Grau | `#e5e5e0` | Haupttrenner (Header-Border, Section-Border) |
| **Border 2** | Hellgrau | `#f0f0ee` | Card-Borders (Linear-style: subtil) |

### Akzentfarben (nur wenn informativ)
| Rolle | Farbe | Hex | Wann verwenden |
|---|---|---|---|
| **Gold** | Accent | `#c8aa50` / `#9d7f3b` | CTA ("Lesen →"), Credits, Mia, Brand-Dot |
| **Grün** | Money | `#2d8a4e` | Geldbeträge, Potenziale, "Neu" |
| **Blau** | Links | `#2563eb` | Hyperlinks (nur echte Links) |
| **Rot** | Warnung | `#c0392b` | Wenig Credits, hohe Priorität |
| **Amber** | Mittel | `#b45309` | Mittlere Priorität |

### Farbregeln
1. **Zahlen = Schwarz.** Immer. Keine farbigen Zahlen in KPIs.
2. **Geldbeträge = Grün.** Nur finanzielles Potenzial (€200k–500k), nicht Zeitwerte.
3. **CTA = Gold.** "Lesen →", Credits-Anzeige, Mia-Avatar.
4. **Alles andere = Grau.** Im Zweifelsfall: Grau.

---

## 3. Typografie

### Fonts
| Font | Verwendung |
|---|---|
| **Inter** (300-700) | Alles außer Daten. Headlines, Body, Labels, Buttons. |
| **JetBrains Mono** (400-500) | Daten: Zahlen, IDs, Timestamps, Credits, Methodik-Hinweise, Confidence |

### Größen (rem-basiert)
| Element | Größe | Gewicht | Font |
|---|---|---|---|
| Seitentitel (h1) | 1.15–1.4rem | 700 | Inter |
| Section-Label | 0.68rem | 600, uppercase, 0.1em spacing | Inter |
| Card-Titel | 0.75–0.88rem | 600 | Inter |
| Body-Text | 0.78–0.85rem | 400 | Inter |
| Beschreibung | 0.65–0.72rem | 400 | Inter |
| Meta/Fußnoten | 0.48–0.55rem | 400 | JetBrains Mono |
| KPI-Wert | 1.05rem | 700 | JetBrains Mono |
| KPI-Label | 0.68rem | 400 | Inter |
| KPI-Sub | 0.58rem | 400, italic | Inter |

### Regeln
- **Letter-spacing -0.02em** auf h1 (enger = seriöser)
- **Letter-spacing 0.1em** auf Section-Labels (weiter = hierarchisch)
- **Line-height 1.7** für Fließtext
- **Kein Text über 1.4rem** außer Seitentitel
- **Ungerade Zahlen** wirken ehrlicher als runde (93 statt 90, 69% statt 70%)

---

## 4. Layout

### Seitenstruktur
```
┌─────────────────────────────────────────────┐
│ Header: Brand | Ort+Wetter+Datum | Credits  │
├─────────────────────────────────────────────┤
│ ← Übersicht (Zurück-Link)                  │
│                                             │
│ Seitentitel (h1)                            │
│ Untertitel                                  │
│                                             │
│ [Inhalt]                                    │
│                                             │
├─────────────────────────────────────────────┤
│ Footer: Brand | Navigation | Rechtliches    │
│ © 2026 Ainary          Verschlüsselt · DE   │
└─────────────────────────────────────────────┘
```

### Maße
| Element | Wert |
|---|---|
| Max-Breite Übersicht | 760px |
| Max-Breite Unterseiten | 560–640px |
| Max-Breite Reports | 700px |
| Padding | 40px 32px (Desktop), 24px 16px (Mobile) |
| Card-Radius | 10px |
| Card-Border | 1px solid `#f0f0ee` (border2, nicht border!) |
| Card-Hover | border → border, shadow 0 4px 16px rgba(0,0,0,0.06), translateY(-1px) |

### Header (3 Spalten)
- **Links:** Ainary (Logo → Übersicht) · Abmelden
- **Mitte:** 📍 Ort · Wetter · Datum
- **Rechts:** Trial-Tage · Credits →

### Footer (3-Spalten-Grid)
- **Links:** Ainary + "HUMAN × AI SYSTEMS = LEVERAGE" + 80/20-Tagline
- **Mitte:** Navigation (Übersicht, Verwalten, Methodik, Über Ainary)
- **Rechts:** Rechtliches (AGB, Datenschutz, Impressum)
- **Bottom-Bar:** © 2026 + Sicherheitshinweis

---

## 5. Komponenten

### KPI-Karten (Übersicht)
```html
<div class="kpi-cards">  <!-- 3-spaltig, surface2 Background -->
  <div class="kpi-card">
    <div class="kpi-card-val">~93 Std.</div>     <!-- Schwarz, Mono, 700 -->
    <div class="kpi-card-label">Label</div>       <!-- text2, Inter -->
    <div class="kpi-card-sub">Detail</div>        <!-- muted, italic -->
  </div>
</div>
```

### Tiles (Analysen)
```html
<a href="..." class="tile">               <!-- border2, hover: lift -->
  <div class="tile-title">Titel</div>     <!-- 0.75rem, 600 -->
  <div class="tile-desc">So-what</div>    <!-- McKinsey: WAS gefunden, nicht WAS es ist -->
  <div class="tile-meta">                 <!-- Mono, 0.52rem, light -->
    <span>◆5</span>                       <!-- Credits -->
    <span>~24–40 Std.</span>              <!-- Range -->
    <span>€1.320–2.200</span>            <!-- Einsparpotenzial -->
    <span>14 S.</span>                    <!-- Seiten -->
    <span>23 Quellen</span>
    <span>78%</span>                      <!-- Confidence, kein Badge! -->
  </div>
  <div class="tile-cta">Lesen →</div>    <!-- Gold, 600 -->
</a>
```

### Mia Chat
- Collapsed by default (Header-Zeile mit Avatar "M" + Greeting)
- Suggested Prompts als Chips unter Eingabefeld (Pill-Design, border-radius 14px)
- Keine Empfehlungen in Antworten — nur Fakten + direkte Links
- KI-Disclaimer am Ende: "Mia ist eine KI-Assistentin"
- Report-Links als `Name →` in Gold, direkt klickbar

### Evidence-Tags (E/I/J/A)
- Nur in Reports, nicht auf der Übersicht
- Inline, hochgestellt, 7pt Mono
- E = Grün, I = Blau, J = Gold, A = Amber
- Hover zeigt Quelle

### Empfehlen-Button
- Diskret, als Textlink ("Empfehlen"), nicht als Button
- Generiert Share-Link mit "Empfohlen von [Name]"
- Kein prominentes UI-Element

---

## 6. Report-Design (DIN 1426 angelehnt)

> Referenz: `daily-intel-buergermeister-print.html`

### Struktur
1. **Document Header:** Brand · ID · Titel · Untertitel · Metadaten · Confidence-Bar
2. **Evidence-Legende:** E/I/J/A erklärt (einmal pro Report)
3. **Inhaltsverzeichnis:** Nummeriert, mit Anchor-Links
4. **Sections:** Nummeriert (1, 2, 3...), mit Section-Header
5. **Items:** Priorität-Dot · Titel · Tag · Body · Quellen · Relevanz · Lösung · Links
6. **Beipackzettel:** Was kann der Report / Was NICHT / Methodik / Limitationen
7. **Cross-References:** Links zu verwandten Analysen
8. **Footer:** Druckversion · Empfehlen · 3-Spalten-Footer

### Wertdarstellung
- **Zeitwerte:** "Ihr Aufwand ohne Ainary: ~5–9 Std." (Range, persönlich)
- **Geldwerte:** "Einsparpotenzial €275–495" (Range, Basis angeben)
- **Potenziale:** "Identifiziertes Potenzial: €200k–500k" (Grün, mit Disclaimer)
- **Basis:** "€55/Std. TVöD E11, konservativ" (Mono, light, rechts)
- **Credits:** "◆5" (pro 5 Quellen = 1 Credit)

### Quellen
- ISO 690 angelehnt (nicht "zertifiziert")
- Inline: `[Quelle: Name, Datum]`
- Links: Klickbar wenn verfügbar
- Fehlende Quellen: Explizit als "nicht verifiziert" markieren

---

## 7. Responsive

### Breakpoints
| Breite | Anpassung |
|---|---|
| > 760px | Volle Darstellung |
| ≤ 640px | Tiles 1-spaltig, KPIs 1-spaltig, Footer 1-spaltig, Header-Mitte ausblenden |

### Mobile-Regeln
- Touch-Targets mindestens 44px
- Kein Hover-abhängiger Content
- Chips scrollbar wenn zu viele

---

## 8. Psychologie & UX

### Zielgruppe: "50-Jähriger mit MacBook"
- Deutsche Labels (kein "Dashboard", sondern "Übersicht")
- Wenig Englisch (Ausnahme: etablierte Begriffe wie "Credits", "Confidence")
- Große Klickflächen
- Keine verschachtelten Menüs

### Vertrauenssignale
- Confidence auf JEDER Zahl
- Ranges statt Punktwerte
- Methodik-Link bei jeder Wertangabe
- Beipackzettel auf jedem Report
- "Was wir NICHT können" auf der Methodik-Seite
- Verschlüsselung + DE-Hosting im Footer

### Preiskommunikation
- **Nie auf der Hauptseite.** Nur über "Verwalten" (eigene Seite).
- **Credits diskret** im Header (Gold-Text, kein Badge)
- **€99/mo** nur auf der Verwalten-Seite
- **Mia nennt Credits** erst wenn der User eine Anfrage stellt
- **Kein €-Betrag als "gespart"** — nur "Einsparpotenzial" oder "Recherche-Äquivalent"

### Mia-Regeln
- Keine Empfehlungen geben (nur Fakten)
- Keine Rechts-/Finanzberatung
- Max 1 Cross-Sell pro Antwort (Report-Link)
- Report-Namen als direkte Links (`Name →`), nicht "soll ich öffnen?"
- KI-Disclaimer sichtbar

---

## 9. Dateistruktur

```
reports/
├── index.html                          # Übersicht (Hauptseite)
├── shared.css                          # Shared Styles (Header, Footer, Cards)
├── daily-intel-buergermeister.html     # Briefing (interaktiv)
├── daily-intel-buergermeister-print.html  # Briefing (DIN 1426 Print) ← REFERENZ
├── analyse-foerdermittel.html          # FS-2026-0220-GH
├── analyse-digitalisierung.html        # DS-2026-0220-GH
├── analyse-buergerstimmung.html        # BS-2026-0220-GH
├── analyse-uhrenindustrie.html         # UI-2026-0220-GH
├── methodik.html                       # Wie wir rechnen
├── ueber-ainary.html                   # Über Ainary + Kindergarten
└── verwalten.html                      # Abo + Credits + Account

docs/
├── DESIGN-SYSTEM.md                    # Dieses Dokument
├── BUSINESS-MODEL.md                   # Pricing + Strategie

templates/
├── daily-intel-template.html
├── daily-intel-print-template.html
├── analyse-template.html
└── overview-template.html
```

---

## 10. Versionierung

| Version | Datum | Änderung |
|---|---|---|
| v1 | 2026-02-19 | Erster Chat-Widget Prototyp |
| v2 | 2026-02-19 | Daily Intel + E/I/J/A Tags |
| v3 | 2026-02-20 | Übersicht + Tiles + Mia |
| v4 | 2026-02-20 | Light Theme + Print Version |
| v5 | 2026-02-20 | Pricing-Vereinfachung + Ranges |
| v6 | 2026-02-20 | Design-System: Monochrom, Linear-Hover, McKinsey-Descriptions, Shared Header/Footer, Credits, ChatGPT-Chips, keine Icons, keine Empfehlungen |

---

*Referenz: Bertelsmann Stiftung (Inhalt/Seriosität) + Palantir (Dichte/Hierarchie) + Linear (Hover/Borders) + ChatGPT (Chips/Einfachheit) + McKinsey (So-what Headlines)*

# Report Design Skill — Fehlerfreie PDF-Reports

*Mia's verbindliche Regeln für Reports. Jeder Verstoß = Fehler. Wird nach jedem Feedback aktualisiert.*

---

## 🔴 GOLDENE REGEL

**IMMER LaTeX (XeLaTeX) verwenden. NIEMALS HTML-to-PDF.**

HTML-to-PDF hat fundamentale Probleme:
- Chrome headless bricht Seiten unpräzise um
- Content überlappt Footer
- Keine zuverlässige Seitenkontrolle
- Abstände sind zwischen Screen und Print verschieden

LaTeX löst ALL diese Probleme nativ. Es gibt keinen Grund, HTML für Print-PDFs zu verwenden.

---

## Definition of Done

> "Würde Florian das OHNE ÄNDERUNGEN an einen CEO/Investor schicken?"

Jeder Report muss ALLE Punkte bestehen:
- [ ] Kein Content überlappt Footer/Seitenrand — auf JEDER Seite geprüft
- [ ] Konsistente Margins auf allen Seiten (identisch, messbar)
- [ ] Fußzeile: Trennlinie + Label links + Seitenzahl rechts — auf jeder Seite gleich
- [ ] Kopfzeile: Titel + Untertitel mit klarer Trennung zum Content
- [ ] Alle Tabellen passen komplett auf ihre Seite (kein Umbruch mitten in Tabelle)
- [ ] Lesbare Schriftgrößen (Body ≥ 10pt, kein Text unter 8pt)
- [ ] Keine Platzhalter (grep: "x%", "TODO", "[…]", "tbd")
- [ ] Alle Zahlen mit Quelle belegt
- [ ] DE + EN Version wenn gewünscht

---

## LaTeX Setup

### Compiler
```bash
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
cd [VERZEICHNIS]
xelatex -interaction=nonstopmode report.tex  # 1. Durchlauf
xelatex -interaction=nonstopmode report.tex  # 2. Durchlauf (Referenzen)
```

### Pakete installieren (bei Fehlern)
```bash
tlmgr install [PAKETNAME]
```

### Standard-Pakete (immer laden)
```latex
\usepackage{fontspec}        % Systemfonts (Helvetica Neue)
\usepackage{geometry}        % Seitenränder
\usepackage{xcolor}          % Farben
\usepackage{fancyhdr}        % Kopf-/Fußzeilen
\usepackage{titlesec}        % Heading-Styles
\usepackage{tabularx}        % Flexible Tabellen
\usepackage{booktabs}        % Professionelle Tabellenlinien
\usepackage{enumitem}        % Listen-Styling
\usepackage{tikz}            % Grafiken, Stat-Cards, Cover
\usepackage{tcolorbox}       % Highlight-Boxen
\usepackage{multicol}        % Mehrspaltig (Quellen)
\usepackage{hyperref}        % Links
\usepackage{microtype}       % Besserer Textsatz
\usepackage{needspace}       % Seitenumbruch-Kontrolle
\usepackage{parskip}         % Absatzabstand statt Einrückung
```

---

## Typografie-Standards (Quellen: DIN 5008:2020, ISO 11442, Typografie-Industrie)

### Blocksatz (Justified Text)
- **IMMER Blocksatz** für professionelle Reports (DIN 5008 für Reports)
- **Silbentrennung MUSS aktiv sein** — Blocksatz ohne Silbentrennung erzeugt hässliche Lücken
- LaTeX: `\usepackage{polyglossia}` + `\setdefaultlanguage{german}` aktiviert dt. Silbentrennung
- `\tolerance=2000` + `\emergencystretch=15pt` für sauberen Blocksatz

### Witwen und Waisen (Widows & Orphans)
- **Widow** = einzelne Zeile am Anfang einer neuen Seite (vom vorherigen Absatz) → VERBOTEN
- **Orphan** = einzelne Zeile am Ende einer Seite (vom nächsten Absatz) → VERBOTEN
- LaTeX: `\widowpenalty=10000` + `\clubpenalty=10000` → LaTeX vermeidet beides automatisch

### Überschriften und Seitenumbrüche
- **Regel: Lieber ein Wort auf die nächste Seite als eine einsame Überschrift am Seitenende**
- Min. 3-4 Zeilen Content MÜSSEN nach einer Überschrift auf derselben Seite folgen
- Wenn nicht genug Platz → Überschrift komplett auf nächste Seite schieben
- LaTeX: `\needspace{4\baselineskip}` im `\titleformat` für Section und Subsection
- **Überschriften die zu lang für eine Zeile sind** → manuellen Umbruch `\\` setzen, nicht abschneiden lassen

### Zeilenbreite (Measure)
- **Optimal: 45-90 Zeichen pro Zeile** (inkl. Leerzeichen)
- Bei A4 mit 28mm Margins + 11pt: ca. 75-80 Zeichen → optimal
- Zu breit = Auge verliert die Zeile beim Zurückspringen

### Farbkontrast (WCAG 2.1 AA Standard)
- **Minimum 4.5:1** Kontrastratio für normalen Text
- **Minimum 3:1** für großen Text (>18pt oder >14pt Bold)
- VERBOTEN auf Weiß: Gelb (#EAB308, 1.9:1), helles Grün (#16A34A, 3.8:1)
- ERLAUBT auf Weiß: Dunkelrot (#B91C1C, 6.1:1), Dunkelgrün (#15803D, 5.0:1), Dunkelgelb/Braun (#92400E, 7.3:1)
- Auf dunklem Hintergrund: Weiß oder helles Blau (#93C5FD), NICHT Grau (#64748B)
- **Jede Farb-Text-Kombination VOR Verwendung prüfen** (Tool: webaim.org/resources/contrastchecker)

### Hervorhebungen: Wann welchen Hintergrund?
| Typ | Verwendung | Max pro Seite |
|-----|-----------|---------------|
| Kein Hintergrund | Normaler Content (80% der Seite) | — |
| Hellblau (highlightbox) | Key Insight, Takeaway, Empfehlung | 1 |
| Dunkel (darkhighlight) | Kernaussage, Vision, max. Emphasis | 1 pro 2 Seiten |
| Hellgrau (statcard) | Einzelne Kennzahl + Label | Immer 3er-Reihe |
| Hellrot/Hellgrün | Negativ/Positiv-Wertung in Szenarien | Nur in Vergleichen |

**Regel: Nie zwei Highlight-Boxen direkt übereinander ohne normalen Text dazwischen.**

---

## Layout-Regeln (VERBINDLICH)

### 1. Seitenränder
```latex
\usepackage[top=30mm, bottom=35mm, left=28mm, right=28mm]{geometry}
```
- **Bottom 35mm** — genug Platz für Footer + Trennlinie + Abstand
- **Links = Rechts** — immer symmetrisch
- **NIEMALS Margins verkleinern um mehr Content reinzubekommen**
- Bei zu viel Content → Seite teilen oder Text kürzen

### 2. Fußzeilen
```latex
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}    % Trennlinie!
\fancyfoot[L]{\footnotesize\color{gray}TITEL · STRATEGIC REPORT}
\fancyfoot[R]{\footnotesize\color{gray}\thepage}
```
- **Trennlinie IMMER** — footrulewidth > 0
- **Konsistent auf jeder Seite** (außer Cover: `\thispagestyle{empty}`)
- Label links, Seitenzahl rechts
- Schriftgröße: `\footnotesize` (8-9pt)
- Farbe: Grau, nicht schwarz

### 3. Kopfzeilen / Section Headings
```latex
\titleformat{\section}{\fontsize{24}{28}\bfseries\color{heading}}{}{0em}{}
\titlespacing*{\section}{0pt}{0pt}{4pt}
```
- Section-Titel: 24pt, Bold
- Subtitle darunter: 12pt, Grau, mit `\rule{\linewidth}{0.4pt}` als Trenner
- **Zwischen Titel und Content IMMER eine sichtbare Trennung** (Linie oder 16pt Abstand)

### 4. Seitenumbrüche
- **\clearpage** vor jeder neuen Section/Seite
- **\needspace{3\baselineskip}** vor Komponenten die nicht getrennt werden dürfen
- **NIEMALS Content-Menge pro Seite schätzen** — kompilieren und prüfen!
- Bei Überlauf → Text kürzen, NICHT Fonts oder Margins verkleinern

### 5. Whitespace
- **Minimum 20% der Seite ist leer** (Margins + Abstände)
- Zwischen Abschnitten: `\vspace{8pt}` minimum
- Zwischen Heading und Content: 4-6pt
- **Lieber eine Seite mehr als eine Seite zu voll**

---

## Typografie

### Fonts
- **Body:** Helvetica Neue 11pt (via fontspec)
- **Headings:** Helvetica Neue Bold
- **Max 1 Schriftfamilie** — Gewicht + Größe für Hierarchie

### Schriftgrößen-Hierarchie
| Element | Größe | Gewicht |
|---------|-------|---------|
| Cover-Titel | 38pt | Bold |
| Section (h2) | 24pt | Bold |
| Subsection (h3) | 14pt | Bold |
| Body | 11pt | Regular |
| Tabellen | 10-11pt | Regular |
| Quellenverzeichnis | 8.5pt | Regular |
| Footer/Labels | 8-9pt | Regular |

### Zeilenabstand
- **Body:** `\setlength{\parskip}{8pt}` (Absatzabstand)
- **Listen:** `itemsep=2pt, parsep=0pt`
- **Tabellen:** booktabs gibt automatisch guten Zeilenabstand

---

## Farben

| Name | Hex | Verwendung |
|------|-----|-----------|
| primary | #2563EB | Zahlen, Highlights, Akzente |
| heading | #0A0F1E | Überschriften |
| bodytext | #374151 | Fließtext |
| subtitle | #64748B | Untertitel, Labels, Footer |
| lightgray | #F8F9FA | Stat-Card-Hintergrund |
| border | #E5E7EB | Linien, Trennungen |
| darkbg | #0A0F1E | Cover, Dark Boxes |
| accent | #60A5FA | Cover-Zahlen, Highlights auf dunkel |
| red | #DC2626 | Risiko, Probleme, Negativ |
| green | #16A34A | Positiv, Lösung, Erfolg |

**60-30-10 Regel:** 60% weiß, 30% grau/hell, 10% Primärfarbe.

---

## Komponenten (LaTeX)

### Stat-Card (3er-Reihe)
```latex
\noindent\begin{minipage}[t]{0.32\linewidth}\centering
  \statcard{ZAHL}{LABEL}
\end{minipage}\hfill
\begin{minipage}[t]{0.32\linewidth}\centering
  \statcard{ZAHL}{LABEL}
\end{minipage}\hfill
\begin{minipage}[t]{0.32\linewidth}\centering
  \statcard{ZAHL}{LABEL}
\end{minipage}
```

### Highlight Box
```latex
\begin{highlightbox}
  Text hier — kurz und prägnant. Max 2-3 Sätze.
\end{highlightbox}
```

### Dark Highlight Box
```latex
\begin{darkhighlight}
  Für besonders wichtige Aussagen. Weiße Schrift auf dunkel.
\end{darkhighlight}
```

### Nummerierter Schritt
```latex
\ruleitem{01}{Titel}{Beschreibung in einem Satz.}
```

### Professionelle Tabelle
```latex
\begin{tabularx}{\linewidth}{@{}l X X@{}}
\toprule
\textbf{Spalte 1} & \textbf{Spalte 2} & \textbf{Spalte 3} \\
\midrule
Wert & Wert & Wert \\
\bottomrule
\end{tabularx}
```

### 2-Spalten-Layout
```latex
\begin{minipage}[t]{0.48\linewidth}
  Linke Spalte
\end{minipage}\hfill
\begin{minipage}[t]{0.48\linewidth}
  Rechte Spalte
\end{minipage}
```

---

## Pre-Flight Checklist (VOR dem Öffnen für Florian)

### 1. Kompilierung
- [ ] `xelatex` läuft fehlerfrei durch (0 Errors)
- [ ] 2x kompiliert (für Referenzen/Seitenzahlen)
- [ ] Keine `Overfull \hbox` Warnings > 10pt

### 2. Seitenweise Prüfung
Für JEDE Seite manuell prüfen:
- [ ] **Footer sichtbar?** — Trennlinie + Text nicht abgeschnitten
- [ ] **Content endet ÜBER dem Footer?** — min. 10mm Abstand
- [ ] **Tabelle komplett auf der Seite?** — nicht über Seitenrand hinaus
- [ ] **Keine verwaisten Überschriften?** — h3 am Seitenende ohne Content darunter
- [ ] **Stat-Cards aligned?** — alle 3 auf gleicher Höhe

### 3. Konsistenz
- [ ] Alle Section-Titel gleich formatiert
- [ ] Alle Tabellen gleichen Stil (booktabs überall)
- [ ] Alle Stat-Cards gleiche Größe
- [ ] Footer auf jeder Seite identisch (außer Cover)
- [ ] Schriftgrößen einheitlich (kein willkürliches `\small` oder `\footnotesize` im Body)

### 4. Inhalt
- [ ] Keine Platzhalter: `grep -E "x%|TODO|\[\.\.\.?\]|tbd|FIXME" report.tex`
- [ ] Alle Zahlen haben Quellen (im Quellen-Abschnitt referenziert)
- [ ] Kontaktdaten korrekt (florian@ainaryventures.com)
- [ ] Versionsnummer aktuell

### 5. Selbsttest
- [ ] PDF öffnen und JEDE Seite als Screenshot/Thumbnail prüfen
- [ ] Auf A4 Papier druckbar? (keine Elemente im Randbereich)
- [ ] Würde ICH das als professionell empfinden?

---

## Prozess: Neuen Report erstellen

### 0. ERWARTUNGEN DEFINIEREN (VOR allem anderen!)

**Niemals sofort losbauen. Erst recherchieren was "gut" aussieht.**

1. **Best Practices recherchieren** — Web-Search: "Best [Dokumenttyp] layout", "McKinsey report format", "[Branche] report examples". Mindestens 3 Referenzen anschauen.
2. **Florians eigene Quellen nutzen** — Obsidian Vault durchsuchen (Prompts, Templates, Wissen), ChatGPT-Exports in ~/FZ/AI-Conversations/ prüfen, vorherige Arbeiten als Referenz.
3. **Erwartungsbild beschreiben** — Bevor eine Zeile Code/LaTeX geschrieben wird: "Das fertige Dokument sieht so aus: [Beschreibung]. Es hat X Seiten, Format Y, enthält Z." An Florian zurückspiegeln.
4. **Qualitätsreferenz finden** — Ein konkretes Beispiel das dem Ziel nahekommt (McKinsey PDF, BCG Deck, existierender Report). Als Messlatte definieren.

> **Die Frage ist nicht "Was kann ich bauen?" sondern "Was erwartet der Empfänger?"**

### 1. Briefing
- Wer liest es? (CEO, Investor, Techniker)
- Was soll der Leser danach TUN?
- Wie viele Seiten max?
- Welche Daten haben wir?

### 2. Outline (Markdown)
Erst Struktur, dann Content. Typische Struktur:
1. Cover (Titel, 3 Stats, Autor, Version)
2. Executive Summary
3. Problem (mit Zahlen)
4. Lösung/Produkt
5. Technische Tiefe (1-2 Seiten)
6. Wettbewerb
7. Markt (TAM/SAM/SOM)
8. Roadmap
9. Revenue Scenarios
10. Risiken
11. Vision
12. Quellen + Kontakt

### 3. Content schreiben
- **Max 70% der Seite mit Content füllen** — Rest ist Whitespace
- **Jeder Abschnitt auf EINE Seite** — niemals über Seitengrenze
- Bei zu viel Text → kürzen, nicht quetschen
- Jede Zahl mit Quelle

### 4. LaTeX bauen
- Template aus `research/36zero-report.tex` kopieren
- Nur Content ersetzen, NICHT Layout/CSS/Preamble ändern
- Kompilieren und SOFORT prüfen

### 5. Pre-Flight Checklist abarbeiten (siehe oben)
- Jeden einzelnen Punkt abhaken
- Bei einem Fehler → fixen und NEU kompilieren

### 6. Liefern
- PDF auf Desktop kopieren: `cp report.pdf ~/Desktop/NAME.pdf`
- Öffnen: `open -a Preview ~/Desktop/NAME.pdf`
- NICHT liefern bevor Pre-Flight bestanden

---

## Feedback-Log

### 2026-02-03
- ❌ Margins komprimiert (v4 schlechter als v3) → **NIE Margins verkleinern**
- ❌ Titel und Zahl redundant ("93% weniger" + "93%") → **Ergänzen, nicht wiederholen**

### 2026-02-04 (36ZERO Report — HTML-Version)
- ❌ Content überlappt Footer auf Seite 5 und 7 → **HTML kann das nicht zuverlässig lösen**
- ❌ Fußzeilen-Position inkonsistent zwischen Seiten → **LaTeX fancyhdr löst das**
- ❌ Zeilenabstände ungleichmäßig → **LaTeX parskip + booktabs = konsistent**
- ❌ 4 Iterationen nötig, alle mit Layout-Fehlern → **HTML-to-PDF ist der falsche Ansatz**
- ✅ Quellen als Research-Paper-Format (zweispaltig, nummeriert) → Beibehalten
- ✅ TAM/SAM/SOM Waterfall → Standard-Seite für jeden Strategie-Report
- ✅ Competitive Feature-Matrix mit ✓/△/✗ → Visuell klar
- ✅ Revenue Scenarios (3 Pfade mit farbcodierten Cards) → Gutes Entscheidungstool
- ✅ Risk Matrix mit Impact/Probability/Mitigation → Standard

### 2026-02-04 17:50 (v2.2)
- ❌ Kein Blocksatz → **Blocksatz + Silbentrennung (polyglossia) ist Standard für Reports**
- ❌ Überschrift allein am Seitenende → **needspace{4\baselineskip} in titleformat**
- ❌ TAM/SAM/SOM Seite Content überlappt → **Weniger Content pro Seite, Highlight-Box entfernen oder verschieben**
- ❌ Zu lange Section-Titel laufen über → **Manueller \\\\ Umbruch in langen Titeln**
- ✅ DIN 5008 als Referenz-Norm identifiziert (Schreib- und Gestaltungsregeln)
- ✅ WCAG 2.1 AA für Farbkontrast (min. 4.5:1)
- ✅ Widow/Orphan-Schutz via widowpenalty/clubpenalty=10000

### Kernlektion 2026-02-04
> **HTML-to-PDF ist für Print-Reports ungeeignet.** 4 Iterationen, jede mit Layout-Fehlern. LaTeX macht Seitenumbrüche, Footer und Margins NATIV richtig. Ab sofort: LaTeX für alle Reports.

---

## Template-Dateien
- **LaTeX Template:** `research/36zero-report.tex` (PRIMÄR — ab sofort Standard)
- **HTML DE:** `research/36zero-report.html` (Legacy, nicht für neue Reports)
- **HTML EN:** `research/36zero-report-en.html` (Legacy)

---

---

## Versions-Log

| Version | Datum | Änderungen |
|---------|-------|-----------|
| 1.0 | 2026-02-03 | Initial: HTML-basiert, CSS-Komponenten |
| 2.0 | 2026-02-04 15:00 | Komplett-Umstellung auf LaTeX |
| 2.1 | 2026-02-04 17:00 | Farbkontrast-System, Pre-Flight Checklist, darkruleitem |
| 2.2 | 2026-02-04 17:50 | Blocksatz, Widows/Orphans, Heading-Schutz, DIN 5008, WCAG 2.1, Hervorhebungs-Strategie |

*Dieses Skill wird nach JEDEM Report-Feedback aktualisiert.*

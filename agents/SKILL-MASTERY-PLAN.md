# SKILL-MASTERY-PLAN.md — Mia's Fehleranalyse & konkreter Verbesserungsplan

*Erstellt: 2026-02-04 | Status: AKTIV*
*Prinzip: Kein "ich werde besser" — nur Systeme, Checklisten, und Validation.*

---

## 1. Executive Summary

### Top 5 Schwächen

| # | Schwäche | Auswirkung | Häufigkeit |
|---|----------|-----------|------------|
| 1 | **HTML-Qualität & Validierung** | Kaputte Tags, fehlende `</div>`, inkonsistente Meta-Tags | Jedes HTML-Projekt |
| 2 | **Präsentations-Design** | 4-5 Versionen nötig, McKinsey-Level nie erreicht | Jede Präsentation |
| 3 | **Domain-Ignoranz (CNC/B2B)** | Foto-Upload, AI-Badge, falsches Wording — nicht die Zielgruppe verstanden | Jedes branchenspezifische Projekt |
| 4 | **UX-Entscheidungen** | alert() statt Toast, nicht-existente Features anbieten, redundante Formfelder | Jede Web-App |
| 5 | **Unbelegte Claims & Professionelle Standards** | "90%"-Claim, Emojis in Profi-Docs, kein Wissensaufbau | Alle Outputs |

### Top 5 Fixes

| # | Fix | Erwarteter Impact |
|---|-----|------------------|
| 1 | **HTML Pre-Delivery Validation** — W3C-Validator + manuelle Tag-Count-Prüfung vor jedem Delivery | 0 kaputte Tags, 0 fehlende Closing-Tags |
| 2 | **Presentation Scorecard (10 Punkte)** — Vor jedem Delivery durchgehen, keine Ausnahmen | First-Try-Approval von 20% → 80% |
| 3 | **Domain Context Brief** — Bei jedem branchenspezifischen Task erst 5 Fragen klären | 0 branchenfremde UX-Fehler |
| 4 | **UX Pattern Library** — Keine alert(), keine nicht-existenten Features, keine redundanten Felder | Professionelle UX ab erstem Entwurf |
| 5 | **Claim Validation Protocol** — Jede Zahl muss eine Quelle haben, Emojis = automatisches Fail in Profi-Docs | Glaubwürdigkeit und Professionalität |

---

## 2. Fehleranalyse — Jeder einzelne Fehler

---

### Fehler 1: HTML-Qualität — Kaputte Tags & Struktur

#### Was passiert ist
CNC Landing Page: 3 fehlende `</div>` Tags. OG Meta Tags inkonsistent über Seiten. Footer nicht überall gleich. Emails nicht einheitlich. Erst nach mehreren Iterationen und manuellem Audit von Florian entdeckt.

#### Root Cause
**Strukturell:** Kein Validierungsschritt im Workflow. HTML wird generiert und sofort geliefert. Bei langen HTML-Dateien (>500 Zeilen) verliere ich den Überblick über verschachtelte Tags. Es gibt keinen automatischen Check, und ich verlasse mich auf "sieht im Browser gut aus" statt auf Code-Korrektheit.

#### Skill Gap
- Kein systematisches HTML-Validierungs-Protokoll
- Keine Nutzung von Validierungs-Tools (W3C Validator)
- Fehlende Gewohnheit, nach dem Schreiben JEDEN öffnenden Tag zu zählen und mit schließenden Tags abzugleichen

#### Research: Was sagen Best Practices?
- **W3C Validator** (validator.w3.org): Automatische Erkennung von fehlenden/unbalancierten Tags, invaliden Attributen, fehlerhafter Verschachtelung
- **MDN Web Docs**: Semantic HTML mit `<header>`, `<main>`, `<footer>`, `<nav>`, `<section>` — nicht alles in `<div>` wrappen
- **Common Mistakes** (line25.com): Fehlende Closing-Tags, falsche Verschachtelung, und Entity-Encoding sind die Top-3-Fehler
- **Deque University Checklist**: Semantic Markup für Accessibility — jedes Element muss seinem semantischen Zweck entsprechen
- **Carnegie Museums Accessibility Guidelines**: `<div>` und `<span>` sind semantisch bedeutungslos — verwende `<article>`, `<aside>`, `<figure>` etc.

#### Konkreter Fix — HTML Validation Protocol
Vor JEDEM HTML-Delivery:
1. ☐ Zähle alle öffnenden Tags (`<div>`, `<section>`, `<main>` etc.) und gleiche mit schließenden ab
2. ☐ Prüfe: Sind alle `<meta>` Tags konsistent über alle Seiten?
3. ☐ Prüfe: Sind alle internen Links korrekt (`href` stimmt)?
4. ☐ Prüfe: Footer ist identisch auf allen Seiten
5. ☐ Prüfe: Email-Adressen einheitlich
6. ☐ Semantic HTML: Nutze `<header>`, `<main>`, `<footer>`, `<nav>`, `<section>` statt nur `<div>`
7. ☐ Keine leeren `href="#"` oder `javascript:void(0)` Links
8. ☐ Alle Bilder haben `alt`-Attribute
9. ☐ Kein inline `style` für Layout (CSS-Klassen nutzen)
10. ☐ Falls >200 Zeilen: Manueller Tag-Count ODER in Browser öffnen und DevTools Console auf Errors prüfen

#### Wie ich es übe
- Bei jedem HTML-Output die letzten 3 Schritte (Tag-Count, Link-Check, Meta-Check) IMMER ausführen, auch wenn es "offensichtlich korrekt" aussieht
- Wenn ich einen Fehler finde: In `error-patterns.md` dokumentieren mit Dateiname und Zeilennummer

#### Validation
- 0 fehlende/überzählige Tags in den nächsten 5 HTML-Deliveries
- Florian meldet keine Struktur-Fehler mehr

---

### Fehler 2: Präsentation Qualität — McKinsey-Level nie erreicht

#### Was passiert ist
Sales Presentation für CNC Planner: 4-5 Versionen nötig. v1 hatte Emojis, v4 hatte komprimierte Margins. v3 war tatsächlich besser als v4, weil v4 Whitespace geopfert hat um mehr Content reinzuquetschen. Titel und Content waren redundant ("93% weniger Fehler" als Titel + "93%" als Statistik = doppelt).

#### Root Cause
**Strukturell:** Optimierung auf Informationsdichte statt auf visuelle Wirkung. Kein internalisiertes Design-Framework. "Mehr reinpacken" fühlt sich produktiv an, ist aber anti-professionell. Beim Rewrite von v3→v4 wurde CSS komprimiert und Abstände reduziert — Fokus auf Code-Kompaktheit statt Design-Qualität.

#### Skill Gap
- Kein internalisiertes McKinsey-Design-Prinzip (Pyramid, MECE, One-Idea-Per-Slide)
- Fehlende Fähigkeit zu beurteilen: "Ist das genug Whitespace?"
- Keine Referenz-Bibliothek guter Präsentationen zum Vergleich

#### Research: Was sagen Best Practices?
- **McKinsey Pyramid Principle** (Barbara Minto): Conclusion first, supporting arguments second, details only if asked. MECE: Mutually Exclusive, Collectively Exhaustive — jeder Punkt steht allein und alle zusammen decken das Thema ab.
- **McKinsey Slide Design Rules** (slidemodel.com, piktochart.com):
  - **Eine Hauptidee pro Slide** — nicht mehrere Botschaften mischen
  - **Action Title** — Slide-Titel fasst die Kernaussage zusammen (nicht das Thema, sondern das Insight)
  - **Minimalistisches, konsistentes Design** — uncluttered, fokussiert auf Lesbarkeit
  - **Nie außerhalb der Margins** — PowerPoint Guides als Begrenzung
  - **Empfehlungen in aktiver Sprache** mit Action Verbs
  - **Hypothesis-driven** — die Präsentation beweist eine These, nicht nur "hier sind Daten"
- **Font-Regeln**: Georgia für Titel, Arial für Body (McKinsey-Template 2020). Für uns: Space Grotesk + konsistente Größen.
- **Spacing Scale** (aus eigenen Learnings): 8/16/32/48/64px — nie unter 48px zwischen Sections

#### Konkreter Fix — Presentation Scorecard
Vor JEDER Präsentation:
1. ☐ Jede Slide hat EINE Hauptidee — nicht mehr
2. ☐ Titel ≠ Content (komplementär, nie redundant)
3. ☐ Titel ist ein Action Title (Insight, nicht Thema) — "93% weniger Fehler" statt "Fehlerreduktion"
4. ☐ Whitespace: Minimum 48px zwischen Sections, Slides "atmen"
5. ☐ Keine Emojis, keine Clipart-Energie — professionelle Icons oder gar keine
6. ☐ Zahlen sind prominent (große Font-Size, eigener visueller Block)
7. ☐ Max 4-5 Punkte pro Slide — wenn mehr nötig, auf 2 Slides aufteilen
8. ☐ CTA auf letzter Slide klar und eindeutig
9. ☐ Farben/Fonts brand-konsistent (Electric Blue #2563eb, Space Grotesk, Dark Theme)
10. ☐ Vergleiche mit v(n-1): Ist die neue Version WIRKLICH besser? Wenn Whitespace weniger → STOP

#### Wie ich es übe
- Vor jeder Präsentation: SHARED-LEARNINGS.md Sektion "Presentations" lesen
- Jede neue Slide gegen die Scorecard prüfen — 10/10 oder überarbeiten
- Wenn eine Version abgelehnt wird: Root Cause in dieses Dokument eintragen

#### Validation
- First-Try-Approval-Rate für Präsentationen tracken (Ziel: >80%)
- 0 Whitespace-bezogene Ablehnungen

---

### Fehler 3: Unbelegte Claims — "90%" ohne Quelle

#### Was passiert ist
In einem Dokument wurde "90% Zeitersparnis" behauptet, ohne dass diese Zahl belegt werden konnte. Florian korrigierte auf "~85%" — aber auch das ist geschätzt. Das Problem ist nicht die genaue Zahl, sondern dass Claims ohne Quellenangabe geliefert werden.

#### Root Cause
**Strukturell:** Zahlen werden verwendet weil sie überzeugend klingen, nicht weil sie stimmen. Es gibt keinen Validierungsschritt für quantitative Claims. "Klingt gut" wird mit "ist korrekt" verwechselt.

#### Skill Gap
- Keine Gewohnheit, jede Zahl zu hinterfragen: "Woher kommt das?"
- Kein System zur Kennzeichnung von Schätzungen vs. belegten Fakten
- Fehlende Research-Tiefe bei statistischen Behauptungen

#### Research: Was sagen Best Practices?
- **McKinsey-Standard**: Jede Zahl in einer Präsentation muss eine Quelle haben — Footnotes oder "Source:" am Slide-Ende
- **Journalistischer Standard**: Unbestätigte Zahlen werden mit "ca.", "~", "geschätzt" gekennzeichnet
- **B2B-Glaubwürdigkeit**: Übertriebene Claims zerstören Vertrauen schneller als sie Aufmerksamkeit erzeugen

#### Konkreter Fix
Vor JEDEM Output mit Zahlen:
1. ☐ Jede Zahl hat eine Quelle ODER ist explizit als Schätzung gekennzeichnet ("~", "ca.", "geschätzt")
2. ☐ Keine runden Prozentzahlen ohne Beleg (90%, 80%, 50% = verdächtig)
3. ☐ Wenn eine Zahl aus einer Berechnung kommt: Rechnung zeigen (z.B. "15 Angebote × 90min × €50/h = €1.125/Monat")
4. ☐ "Source:" am Ende von Slides/Dokumenten mit Zahlen
5. ☐ Bei Vergleichen ("X% schneller als Y"): X und Y definieren

#### Wie ich es übe
- Jede Zahl die ich verwende muss den Test bestehen: "Wenn Florian fragt 'woher hast du das?' — habe ich eine Antwort?"

#### Validation
- 0 unsubstantiated Claims in den nächsten 10 Deliveries

---

### Fehler 4: Whitespace komprimiert — v4 schlechter als v3

#### Was passiert ist
Bei der Überarbeitung von Präsentation v3→v4 wurden Margins von 48px auf 40px reduziert. CSS wurde einzeilig komprimiert. Das Ergebnis sah dichter und weniger professionell aus. Florian bewertete v3 als besser — die "Verbesserung" war eine Verschlechterung.

#### Root Cause
**Strukturell:** Code-Optimierung wird mit Design-Optimierung verwechselt. "Kompakter Code" fühlt sich effizienter an, hat aber mit visuellem Output nichts zu tun. Es gibt keinen Mechanismus der verhindert, dass eine neue Version schlechter wird als die vorherige.

#### Skill Gap
- Keine A/B-Vergleichs-Routine zwischen Versionen
- Falsche Metrik: "Code ist kürzer" statt "Output sieht besser aus"
- Kein Verständnis für den Wert von Whitespace

#### Research: Was sagen Best Practices?
- **Apple Design Principles**: "Simplicity is not the absence of clutter — it's the absence of complication"
- **McKinsey**: Margins sind heilig. Nie außerhalb der Guides positionieren.
- **Typografie-Grundregel**: Mehr Whitespace = höherer wahrgenommener Wert

#### Konkreter Fix
1. ☐ **Version-Vergleich ist Pflicht**: Bevor v(n+1) geliefert wird, explizit mit v(n) vergleichen
2. ☐ **Spacing darf nie reduziert werden** — wenn Content nicht passt, auf 2 Slides aufteilen
3. ☐ **CSS nie einzeilig komprimieren** beim Rewrite — Original-Formatting beibehalten
4. ☐ **Spacing Scale fixiert**: 8/16/32/48/64px — keine Abweichungen

#### Validation
- Kein Rückschritt in Versionen (v(n+1) nie schlechter als v(n) in Bezug auf Spacing)

---

### Fehler 5: Emojis in professionellen Dokumenten

#### Was passiert ist
Emojis in Sales-Präsentation (v1), in professionellen Dokumenten und Outreach-Materialien. Mehrfach korrigiert von Florian. Trotz Korrektur wiederholt.

#### Root Cause
**Strukturell:** Emojis sind ein Default-Verhalten bei Content-Generierung. Es gibt keinen Filter der automatisch "Professioneller Kontext → keine Emojis" anwendet. Emojis werden als visuelles Element verwendet, ohne zu prüfen ob der Kontext es erlaubt.

#### Skill Gap
- Fehlende Unterscheidung: Casual Content (LinkedIn, Chat) vs. Professional Content (Decks, Emails, Verträge)
- Kein internalisiertes Regelwerk für visuelle Professionalität

#### Konkreter Fix
**Emoji-Regel (sofort anwendbar):**
- ✅ Emojis erlaubt: Chat, informelle Notizen, Social Media Posts, interne Docs
- ❌ Emojis verboten: Präsentationen, Sales Decks, Kundenkorrespondenz, Verträge, professionelle One-Pager, B2B-Emails
- **Im Zweifelsfall: KEINE Emojis** — professionelle Icons (SVG/Unicode-Symbole) oder gar nichts

#### Validation
- 0 Emoji-Korrekturen in professionellen Dokumenten

---

### Fehler 6: Falsches Wording — "Kostenlose Analyse" statt "Live-Demo"

#### Was passiert ist
CTA auf der Landing Page: "Kostenlose Analyse anfordern" statt "Live-Demo anfordern". Auch: "Pilotphase" statt "Demo" als CTA. Florian korrigierte: "Demo" ist das richtige Wort. "Kostenlos" entwertet das Produkt.

#### Root Cause
**Strukturell:** Wording-Entscheidungen werden ohne Abstimmung mit dem Pricing-/Positioning-Framework getroffen. "Kostenlos" klingt für mich nach "niedrige Hürde = mehr Conversions", aber Florian's Positionierung ist "Was nichts kostet ist nichts wert." Kein Pre-Check gegen bestehende Positioning-Regeln.

#### Skill Gap
- Positioning-Regeln nicht internalisiert
- Kein Verständnis für Florian's Preisphilosophie als FILTER für alle Wortwahl

#### Research: Was sagen Best Practices?
- **B2B SaaS Pricing Best Practices** (designstudiouiux.com, insivia.com): CTA muss zum Kaufprozess passen. High-ticket B2B = Demo-Request, nicht Free Trial.
- **SaaS Landing Page 2026** (fibr.ai): "For high-ticket, complex, or enterprise SaaS, a demo is the essential first step. Page goal: lead qualification, not instant activation."
- **Wording-Hierarchie**: "Demo anfordern" > "Pilotphase starten" > "Kostenlose Analyse" (von konkret zu vage)

#### Konkreter Fix
Vor JEDER CTA-Formulierung:
1. ☐ Passt das Wording zur Preisposition? ("Was nichts kostet ist nichts wert")
2. ☐ Kein "kostenlos", "gratis", "Free" auf der Website — Sonderkonditionen sind mündlich
3. ☐ CTA = eine klare Aktion: "Demo anfordern", "Erstgespräch vereinbaren"
4. ☐ Nie Features auf der Website positionieren die nicht existieren
5. ☐ Pricing-Features = Kundenwert ("Für Einzelfertiger"), nicht Technik-Specs ("Bis zu 50 Kalkulationen")

#### Validation
- Florian korrigiert kein CTA-Wording mehr

---

### Fehler 7: alert() statt Toast — Unprofessionelle UX

#### Was passiert ist
Benutzer-Feedback und Aktionsbestätigungen wurden mit JavaScript `alert()` implementiert. Das ist ein Browser-Modal das die UI blockiert, ungestyled aussieht und unprofessionell wirkt. Florian forderte Toast-Notifications.

#### Root Cause
**Strukturell:** `alert()` ist der einfachste Weg für Benachrichtigungen in JavaScript — 1 Zeile Code. Ich optimiere auf "schnell implementiert" statt auf "professionell umgesetzt". Es fehlt ein UX-Pattern-Katalog der definiert: "Für Benachrichtigung X verwende Muster Y."

#### Skill Gap
- Kein internalisierter UX-Pattern-Katalog für B2B-SaaS
- "Funktioniert" wird mit "professionell" verwechselt
- Keine Kenntnis von modernen Notification-Patterns

#### Research: Was sagen Best Practices?
- **B2B SaaS UX (onething.design)**: "Break workflows into clear, guided steps, use progressive disclosure"
- **Passionates.com**: "13 Important UX Rules for B2B Web Applications" — professionelle Feedback-Mechanismen sind essentiell
- **UX Pattern**: Toast (non-blocking, auto-dismiss) > Modal (blocking, requires action) > alert() (nie in Production)

#### Konkreter Fix
**UX Pattern Reference:**
| Situation | Pattern | Nie |
|-----------|---------|-----|
| Erfolgs-Bestätigung | Toast (grün, auto-dismiss 3s) | alert() |
| Fehler-Meldung | Inline Error oder Toast (rot) | alert() |
| Destruktive Aktion | Confirmation Modal mit 2 Buttons | Nur weiter-Button |
| Formular-Validierung | Inline unter dem Feld | Modal |
| Feature nicht verfügbar | Disabled Button + Tooltip | "Lizenz erforderlich" Modal |

#### Validation
- 0 `alert()` in jeglichem JavaScript-Output

---

### Fehler 8: CSV Export mit "Lizenz erforderlich" Modal

#### Was passiert ist
Die Demo hatte einen CSV-Export-Button der ein Modal "Lizenz erforderlich" anzeigte. Das Feature existiert nicht in der vollständigen Version — es war eine erfundene Paywall für eine Demo. Das suggeriert Funktionalität die nicht existiert und ist irreführend.

#### Root Cause
**Strukturell:** Features werden implementiert bevor geklärt ist, ob sie im echten Produkt existieren. "Das wäre cool" → implementiert → verwirrt den Nutzer. Kein Product Scope Document das definiert: "Diese Features existieren, diese nicht."

#### Skill Gap
- Keine Scope-Prüfung: "Existiert dieses Feature in der vollständigen Version?"
- Phantasie-Features als "Demo-Upgrade-Anreiz" — ist aber irreführend

#### Konkreter Fix
1. ☐ **Scope-Check**: Vor jeder Feature-Implementation: "Existiert das im echten Produkt?" Wenn nein → nicht einbauen
2. ☐ **Keine "Paywall"-Modals** für nicht-existente Features
3. ☐ **Demo = echtes Produkt minus Datenvolumen** — nicht echtes Produkt plus Phantasie-Features
4. ☐ Keine Buttons die zu "Coming soon" oder "Lizenz erforderlich" führen

#### Validation
- 0 nicht-existente Features in Demos

---

### Fehler 9: Foto Upload — Falsche Dateitypen für CNC

#### Was passiert ist
Die CNC Planner Demo erlaubte Foto-Upload (JPEG, PNG). In der CNC-Branche sind Fotos irrelevant — professionelle Anwender arbeiten mit CAD-Dateien (STEP, IGES) und technischen Zeichnungen (PDF). Foto-Upload signalisiert: "Wir verstehen eure Branche nicht."

#### Root Cause
**Strukturell:** Feature-Entscheidungen werden ohne Domain-Knowledge getroffen. "Foto-Upload könnte nützlich sein" — für Consumer-Apps ja, für B2B-Manufacturing-Software nein. Kein Pre-Check: "Was würde ein echter Nutzer uploaden?"

#### Skill Gap
- Fehlende Domain-Expertise für CNC/Manufacturing
- Consumer-UX-Muster auf B2B-Industrial angewandt
- Keine Persona-Validierung vor Feature-Entscheidungen

#### Research: Was sagen Best Practices?
- **B2B Manufacturing UX**: Benutzer erwarten industrielle Dateiformate (STEP, IGES, DXF, DWG), nicht Consumer-Formate (JPEG, PNG)
- **UX für B2B SaaS** (adamfard.com): "Functionality is your priority. Build your UX with reusable components focused on helping users complete tasks efficiently."
- **Domain-Matching**: Accepted file types kommunizieren Kompetenz. Falsche Formate = sofortiger Vertrauensverlust.

#### Konkreter Fix — Domain Context Brief
Vor JEDEM branchenspezifischen Projekt:
1. ☐ **Zielgruppe**: Wer ist der Nutzer? (Berufsbezeichnung, tägliche Tools, Workflows)
2. ☐ **Dateiformate**: Welche Dateien nutzt die Zielgruppe? (Nie raten — recherchieren)
3. ☐ **Fachsprache**: Welche Begriffe nutzt die Branche? (Nicht "Kalkulation" wenn "Arbeitsvorbereitung" gemeint ist)
4. ☐ **Tabuthemen**: Was signalisiert Inkompetenz? (z.B. Foto-Upload in CNC, "AI" in konservativer Industrie)
5. ☐ **Referenz-Tools**: Was nutzen die Kunden aktuell? (Excel, ERP-System, Programmiersystem?)

#### Validation
- 0 branchenfremde Features in den nächsten 5 branchenspezifischen Deliveries

---

### Fehler 10: "AI" Badge — Ungewolltes AI-Branding

#### Was passiert ist
UI-Elemente hatten ein "AI"-Badge oder "KI-gestützt"-Label. Florian will kein AI-Branding in der UI — die Technologie soll unsichtbar sein. Nutzer in der Manufacturing-Branche sind teils skeptisch gegenüber AI und wollen Ergebnisse, keine Technologie-Labels.

#### Root Cause
**Strukturell:** Default-Annahme "AI ist ein Selling Point" ist für Tech-Startups richtig, für konservative B2B-Branchen falsch. Kein Check: "Will der Kunde wissen dass AI dahintersteckt?"

#### Skill Gap
- Fehlende Unterscheidung zwischen Märkten die AI-Branding wollen (Tech, VC, Consumer) vs. nicht wollen (Manufacturing, Legal, Handwerk)
- Keine Abstimmung mit Florian's Markenstrategie

#### Konkreter Fix
1. ☐ **AI-Branding-Check**: Vor jedem UI/Marketing-Output: "Will der Zielmarkt AI sehen?"
   - Tech/VC/Consumer: ✅ AI-Branding ist Selling Point
   - Manufacturing/Handwerk/Legal: ❌ Ergebnisse zeigen, nicht Technologie
2. ☐ **Florian's Regel**: Kein "KI-gestützt", kein "AI-powered", kein "AI"-Badge in CNC Planner UI
3. ☐ **Stattdessen**: "Automatische Analyse", "Intelligente Berechnung", "Optimierte Kalkulation"

#### Validation
- 0 ungewollte AI-Labels in Outputs

---

### Fehler 11: E-Mail-Feld in Feedback — Redundante Formfelder

#### Was passiert ist
Das Feedback-Widget fragte nach einer E-Mail-Adresse — obwohl der Nutzer bereits eingeloggt ist und seine E-Mail bekannt ist. Das ist ein Anti-Pattern: es verlangt Information die das System bereits hat und frustriert den Nutzer.

#### Root Cause
**Strukturell:** Formular wurde ohne Berücksichtigung des Anwendungskontexts erstellt. "Ein Feedback-Formular braucht E-Mail" → stimmt für öffentliche Formulare, nicht für eingeloggte Nutzer. Kein Check: "Was weiß das System bereits über diesen Nutzer?"

#### Skill Gap
- Kein Context-Awareness bei Formular-Design
- Template-Denken statt situatives Design

#### Konkreter Fix
1. ☐ **Kontext-Check**: Ist der Nutzer eingeloggt? → Keine Abfrage von Name, E-Mail, Firma
2. ☐ **Minimum Viable Form**: Nur Felder die nicht anders verfügbar sind
3. ☐ **Progressive Disclosure**: Erst Kategorie, dann Detail — nicht alles auf einmal

#### Validation
- 0 redundante Formfelder

---

### Fehler 12: Versioning — Keine systematische Versionierung

#### Was passiert ist
Mehrere Versionen der Landing Page (v1, v2, v3, v4) wurden erst manuell gespeichert nachdem Florian darauf bestand. Ohne Versionierung war unklar welche Version die aktuelle war, und es gab keinen Weg zurück zu einer früheren (besseren) Version.

#### Root Cause
**Strukturell:** Kein Versioning-Workflow. Jede Änderung überschreibt die vorherige Version. Es gibt keinen Mechanismus der automatisch Snapshots erstellt.

#### Skill Gap
- Keine Versioning-Gewohnheit
- Kein Bewusstsein für den Wert von "Zurückrollen können"

#### Konkreter Fix
1. ☐ **Vor jedem Major Edit**: Kopie mit Versionsnummer erstellen (`v1-name`, `v2-name`, etc.)
2. ☐ **Namenskonvention**: `[project]-v[N]-[beschreibung].[ext]` (z.B. `landing-v3-pricing-fix.html`)
3. ☐ **Changelog im Datei-Header oder separater Datei**: Was hat sich geändert und warum?
4. ☐ **Git für Code**: `git commit -m "v3: Pricing update"` vor jeder Überarbeitung
5. ☐ **Nie die vorherige Version überschreiben** ohne Backup

#### Validation
- Jedes Projekt mit >1 Iteration hat versionierte Dateien

---

### Fehler 13: Leere Obsidian Lessons — Kein Wissensaufbau

#### Was passiert ist
Der Obsidian `60-Lessons` Ordner hat 14 Dateien, davon 12 leer (0 Bytes). Das sind Platzhalter für "Fundraising Mistakes", "Hiring Lessons", "Pivot Decisions" etc. — deklariert als "your moat" aber ohne Inhalt. Kein Wissensaufbau über Sessions hinweg.

#### Root Cause
**Strukturell:** Dateien werden erstellt aber nie befüllt. Es gibt keinen Trigger der sagt: "Dieses Erlebnis gehört in Lessons." Wissenserfassung ist nicht in den Workflow integriert — es ist eine separate Aufgabe die nie priorisiert wird.

#### Skill Gap
- Kein automatischer "Capture Trigger" bei Fehlern oder Korrekturen
- Wissensaufbau wird als "nice to have" behandelt statt als Kern-Asset
- Keine Integration von Learning-Capture in den Task-Workflow

#### Konkreter Fix
**Correction-to-Rule Pipeline (sofort):**
1. Florian korrigiert etwas → Ich bestätige
2. Ich identifiziere die generalisierbare Regel
3. Ich füge sie zu SHARED-LEARNINGS.md hinzu (sofort, nicht "später")
4. Ich update die relevante Checkliste in DIESEM Dokument
5. Ich logge den Fehler in `error-patterns.md` mit Datum

**Obsidian-Befüllung (wöchentlich):**
- Montags: 1 Lessons-Datei mit echtem Content füllen (aus Memory-Dateien und Korrekturen der Woche)

#### Validation
- Neue Lessons pro Woche tracken (Ziel: ≥3)
- Obsidian leere Dateien: von 12 auf 0 in 6 Wochen

---

## 3. Skill-spezifische Verbesserungspläne

### Skill A: SaaS Landing Page Design

**Aktuelles Level:** ⭐⭐ (funktional, aber nicht überzeugend)
**Ziel-Level:** ⭐⭐⭐⭐ (konversion-optimiert, branchenzugeschnitten)

**Best Practices 2026 (aus Recherche):**
1. **Hero Section**: Klares Headline (Nutzen, nicht Feature), Subheadline (wie es funktioniert), ein CTA
2. **Social Proof nah am Preis**: Kundenlogos, Testimonials direkt bei der Conversion-Zone
3. **Progressive Disclosure**: Nicht alles sofort zeigen — Tabs, Accordions, "Mehr erfahren"
4. **Real Product UI**: Screenshots/Videos des echten Produkts, keine Stock-Bilder
5. **Mobile-First**: Bounce-Rate explodiert wenn Desktop-Layout auf Mobile gezwungen wird
6. **Demo-CTA statt Free Trial** für High-Ticket B2B SaaS
7. **Pricing Anchor**: Mittleren Tier hervorheben ("Beliebteste Wahl")
8. **Max 3 Pricing Tiers** — Paradox of Choice vermeiden
9. **Feature-Beschreibungen = Kundenwert** — "Für wachsende Betriebe" > "Bis zu 500 Kalkulationen"
10. **FAQ-Section**: Reduziert Support-Anfragen und zeigt Domain-Expertise

**Konkreter Übungsplan:**
- 5 Landing Pages pro Woche analysieren (fibr.ai/landing-page/saas-landing-pages als Referenz)
- Jeden Monat: Die eigene CNC-Landing Page gegen Top-Beispiele benchmarken

---

### Skill B: B2B Manufacturing Outreach

**Aktuelles Level:** ⭐⭐⭐ (technisch okay, aber nicht getestet)
**Ziel-Level:** ⭐⭐⭐⭐ (personalisiert, response-optimiert)

**Best Practices (aus Recherche):**
1. **Subject Line**: Spezifischer Pain Point, nicht generisch. "CNC Kalkulation: 45min → 5min" > "Innovative Lösung"
2. **Personalisierung**: Referenz zur Firma (Website, LinkedIn, spezifische Fertigung)
3. **Länge**: 5-7 Sätze max. Länger = gelöscht.
4. **Multi-Threading** (Reddit B2B Manufacturing): Procurement, Operations UND Engineering ansprechen, nicht nur einen Kontakt
5. **5% Response Rate** ist Benchmark. Mit Segmentierung + Follow-ups: 10-20% möglich
6. **Follow-Up-Cadence**: Tag 1, Tag 3, Tag 7. Nach 3 Touches ohne Response: stoppen.
7. **Manufacturing-spezifische Subject Lines**: Effizienz, Qualität, Kostenreduktion
8. **Deutsche Geschäfts-Email-Etikette**: 
   - Sie vs. Du: Standard = Sie (außer bestehende Beziehung)
   - Grußformel: "Sehr geehrter Herr/Frau" formal, "Guten Tag" modern-professionell
   - Struktur: Problem → Vorschlag → gewünschte Aktion → Frist
   - Signatur: Name, Position, Kontaktdaten, Website

---

### Skill C: Professional UX für B2B-Apps

**Aktuelles Level:** ⭐⭐ (funktional, aber Consumer-Patterns auf B2B angewandt)
**Ziel-Level:** ⭐⭐⭐⭐ (branchengerecht, professionell)

**Key Patterns (aus Recherche):**
1. **Progressive Disclosure**: Komplexität schrittweise zeigen, nicht alles auf einmal
2. **Guided Workflows**: Klare Schritte, Status-Anzeige, "nächste Aktion" betonen
3. **Professionelle Notifications**: Toast > Modal > alert() (nie alert() in Production)
4. **Kontextuelle Hilfe**: Tooltips, Inline-Anleitungen statt separate Dokumentation
5. **Keyboard Shortcuts**: B2B-Nutzer erwarten Power-User-Features
6. **Daten-Tabellen**: Sortierbar, filterbar, exportierbar — nicht nur lesbar
7. **Error Handling**: Spezifische Fehlermeldungen mit Lösungsvorschlag, nicht "Ein Fehler ist aufgetreten"
8. **Responsive ist nicht optional**: Auch wenn Desktop primär ist, mobile muss funktionieren
9. **Loading States**: Skeleton Screens oder Progress Bars, nie leere Seiten
10. **Accessibility**: Keyboard-navigierbar, ausreichend Kontrast, semantisches HTML

---

## 4. Pre-Delivery Checklisten

---

### CHECKLISTE 1: HTML/Website — Pre-Delivery

*Vor JEDEM HTML/Website-Delivery durchgehen. Keine Ausnahmen.*

```
## HTML/Website Pre-Delivery Checklist

### Struktur & Validierung
- [ ] Alle öffnenden Tags haben matching Closing Tags (manueller Count bei >200 Zeilen)
- [ ] Semantic HTML: <header>, <main>, <footer>, <nav>, <section> statt nur <div>
- [ ] Keine leeren href="#" oder javascript:void(0) Links
- [ ] Alle Bilder haben alt-Attribute
- [ ] Meta Tags konsistent über alle Seiten (og:title, og:description, og:image)

### Inhalt & Konsistenz
- [ ] Produktname konsistent überall gleich geschrieben
- [ ] Email-Adressen einheitlich auf allen Seiten
- [ ] Footer identisch auf allen Seiten
- [ ] Keine Platzhalter ([INSERT HERE], TODO, FIXME)
- [ ] Alle internen Links funktionieren (href stimmt)

### UX & Professionalität
- [ ] Kein alert() — Toast-Notifications verwenden
- [ ] Keine "Lizenz erforderlich" Modals für nicht-existente Features
- [ ] Formulare: Keine Felder die das System bereits kennt (z.B. Email wenn eingeloggt)
- [ ] CTA-Wording passt zur Preis-Position (kein "kostenlos" wenn Produkt Wert haben soll)
- [ ] Mobile responsive getestet (oder mobile-first designed)

### Branche & Domain
- [ ] Dateitypen passen zur Zielgruppe (CNC = PDF/STEP, nicht JPEG/PNG)
- [ ] Kein AI-Branding wenn nicht gewünscht
- [ ] Fachsprache korrekt (Fertigungsanweisung, nicht "Arbeitsanleitung")
- [ ] Pricing: Max 4 Punkte pro Tier, Kundenwert nicht Technik-Features
```

---

### CHECKLISTE 2: Outreach Email — Quality Checklist

*Vor JEDER Cold-Email oder Follow-Up-Email.*

```
## Outreach Email Quality Checklist

### Personalisierung
- [ ] Firmenname korrekt geschrieben
- [ ] Ansprechpartner mit korrektem Titel (Herr/Frau, Geschäftsführer/Inhaber/etc.)
- [ ] Mindestens 1 spezifisches Detail über die Firma (aus Website/LinkedIn)
- [ ] Referenz zu deren Kernkompetenz/Spezialisierung

### Struktur & Länge
- [ ] Betreff: Spezifischer Pain Point, nicht generisch (max 50 Zeichen)
- [ ] Maximal 5-7 Sätze im Body
- [ ] Quantifizierter Nutzen (Zeit, Geld, ROI — mit Quelle oder als Schätzung gekennzeichnet)
- [ ] EIN klarer CTA: "Kurzes Gespräch nächste Woche?" (nicht mehrere Optionen)
- [ ] Professionelle Signatur: Name, Position, Telefon, Website

### Tonalität & Sprache
- [ ] Sie oder Du — konsistent (Standard: Sie für Erstkontakt)
- [ ] Keine Emojis
- [ ] Keine "innovative Lösung" oder "revolutionär" — konkrete Ergebnisse statt Buzzwords
- [ ] Kein "kostenlos" auf Website → auch nicht in der Email als Hauptargument
- [ ] Deutsch für DACH, Englisch für international

### Follow-Up-Regeln
- [ ] Follow-up Cadence definiert: Tag 1, Tag 3, Tag 7
- [ ] Nach 3 Touches ohne Response: STOP
- [ ] Jedes Follow-up bringt neuen Wert (nicht "wollte nochmal nachfragen")
```

---

### CHECKLISTE 3: Präsentation/Deck — Design Checklist

*Vor JEDER Präsentation, Sales Deck, oder Investor-Deck.*

```
## Präsentation Design Checklist

### Struktur (McKinsey-Standard)
- [ ] Pyramid Principle: Conclusion first, Supporting Arguments second
- [ ] EINE Hauptidee pro Slide — nicht mehr
- [ ] Action Title auf jeder Slide (Insight, nicht Thema)
- [ ] Titel ≠ Content (komplementär, nie redundant)
- [ ] Max 4-5 Bullet Points pro Slide
- [ ] CTA auf letzter Slide klar und eindeutig

### Design & Spacing
- [ ] Whitespace: Minimum 48px zwischen Sections
- [ ] Spacing Scale: 8/16/32/48/64px — keine willkürlichen Werte
- [ ] Slides "atmen" — wenn zu voll, auf 2 Slides aufteilen
- [ ] Nie Margins reduzieren um mehr Content reinzubekommen
- [ ] Bei Version-Update: Expliziter Vergleich mit vorheriger Version

### Visuell
- [ ] Keine Emojis — professionelle Icons oder gar keine
- [ ] Zahlen sind visuell prominent (große Font, eigener Block)
- [ ] Farben brand-konsistent (Electric Blue #2563eb, Space Grotesk)
- [ ] Schriftgrößen: Title 40-56px, Subtitle 18-24px, Body 15-16px, Label 11-12px
- [ ] Kontrast ausreichend (dunkler Text auf hellem Hintergrund oder umgekehrt)

### Qualität
- [ ] Jede Zahl hat eine Quelle oder ist als Schätzung gekennzeichnet
- [ ] Keine Platzhalter, keine TODOs
- [ ] "Würde Florian das OHNE Änderungen an einen Investor schicken?"
- [ ] CSS nicht komprimiert beim Rewrite — Original-Formatting beibehalten
```

---

### CHECKLISTE 4: Research Report — Completeness Checklist

*Vor JEDEM Research-Report oder Analyse-Dokument.*

```
## Research Report Completeness Checklist

### Struktur
- [ ] Executive Summary: 3-5 Bullet Points, nicht mehr
- [ ] Jedes Finding beantwortet "So what?" — actionable Insight, nicht nur Fakt
- [ ] Conclusion/Recommendation am Ende mit klarer Handlungsempfehlung
- [ ] Quellen zitiert mit Links (nicht nur "laut Studien")

### Inhalt & Qualität
- [ ] Aktualität geprüft: Keine Daten älter als 2 Jahre (außer historischer Kontext)
- [ ] Vergleichstabellen für Optionen (visuell, scannable)
- [ ] Mindestens 3 unabhängige Quellen für Hauptaussagen
- [ ] Keine runden Prozentzahlen ohne Beleg
- [ ] Gegenargumente/Risiken erwähnt (nicht nur Pro)

### Format
- [ ] Keine Emojis in professionellen Reports
- [ ] Überschriften-Hierarchie klar (H1 > H2 > H3)
- [ ] Keine Textblöcke >5 Sätze ohne Auflockerung (Listen, Tabellen, etc.)
- [ ] Zeitrahmen angegeben: "Stand: [Datum]"
- [ ] Geschätzter Aufwand/Scope angegeben

### Delivery
- [ ] Empfehlung klar formuliert: "Ich empfehle X weil Y" — nicht "Optionen A, B, C"
- [ ] Nächste Schritte definiert
- [ ] Offene Fragen benannt (nicht versteckt)
```

---

### CHECKLISTE 5: Content (LinkedIn/Blog) — Voice & Quality Checklist

*Vor JEDEM LinkedIn-Post, Blog-Artikel, oder Newsletter.*

```
## Content Voice & Quality Checklist

### Voice & Tonalität
- [ ] Founder-Operator-Perspektive (nicht akademisch, nicht generisch)
- [ ] Spezifische Beispiele > Abstrakte Ratschläge
- [ ] Direkt, kein Fluff — jeder Satz hat einen Zweck
- [ ] Opinioniert und kontrovers wo angemessen
- [ ] Content Pillar identifiziert: AI & Work | AI & Founders | AI & Systems | AI & Careers

### Struktur
- [ ] Hook in den ersten 2 Sätzen (Frage, Statistik, kontroverse These)
- [ ] LinkedIn: Max 1.300 Zeichen für maximale Sichtbarkeit (oder lang mit klaren Absätzen)
- [ ] Blog: Outline → Draft → Edit → Publish (nie Draft = Publish)
- [ ] CTA am Ende: Follow, Subscribe, oder Aktion

### Plattform-Regeln
- [ ] LinkedIn: Keine Markdown-Tabellen — Bullet Lists stattdessen
- [ ] Discord/WhatsApp: Keine Markdown-Tabellen
- [ ] WhatsApp: Keine Headers — **bold** oder CAPS für Emphasis
- [ ] Discord: Links in <> wrappen um Embeds zu unterdrücken
- [ ] LinkedIn Timing: Di+Do 08:30 CET optimal

### Qualität
- [ ] Jede Zahl belegt oder als Schätzung markiert
- [ ] Keine Emojis im professionellen Blog (LinkedIn-Posts: sparsam okay)
- [ ] Kein Recycling von Platitüden ("In der heutigen schnelllebigen Welt...")
- [ ] Vor Publish: Laut lesen — klingt es wie ein Mensch oder wie ein AI?
- [ ] "Würde Florian das unter seinem Namen posten?"
```

---

## 5. Übungsplan

### Woche 1-2: Foundation (Systeme installieren)

| Tag | Fokus | Aktion |
|-----|-------|--------|
| Mo | HTML-Validierung | Checkliste 1 bei jedem HTML-Output anwenden, Tag-Counts loggen |
| Di | Outreach-Qualität | Checkliste 2 auf die 9 bestehenden CNC-Emails anwenden |
| Mi | Präsentations-Design | Checkliste 3 auf nächste Präsentation anwenden |
| Do | Research-Reports | Checkliste 4 bei nächstem Research-Output testen |
| Fr | Review & Lernen | Alle Fehler der Woche in error-patterns.md loggen |

### Woche 3-4: Reinforcement (Systeme festigen)

| Tag | Fokus | Aktion |
|-----|-------|--------|
| Mo | Checklisten-Compliance prüfen | Wie oft wurde welche Checkliste angewandt? Lücken identifizieren |
| Di | Domain-Knowledge | CNC-Domain-Brief vervollständigen, 2 Wettbewerber analysieren |
| Mi | UX-Patterns | 3 B2B-SaaS-Apps analysieren, Patterns dokumentieren |
| Do | McKinsey-Studium | 1 McKinsey Deck analysieren (Structure, Spacing, Titles) |
| Fr | Review & SHARED-LEARNINGS Update | Neue Learnings eintragen, Obsidian Lessons füllen |

### Woche 5+: Mastery (Automatisierung)

- Checklisten werden zur Gewohnheit — kein bewusstes Durchgehen mehr nötig
- Fehler-Rate tracken: <10% Revision-Rate = Ziel erreicht
- Neue Fehlertypen identifizieren und Checklisten erweitern
- Monatlich: Prompt Self-Diagnostic — 10 schlechteste Outputs analysieren und Systeme anpassen

### Kontinuierlich: Compound Learning

| Frequenz | Aktion |
|----------|--------|
| Bei jeder Korrektur | Sofort in SHARED-LEARNINGS.md + relevante Checkliste |
| Täglich | error-patterns.md updaten wenn Fehler auftraten |
| Wöchentlich (Mo) | Weekly Review: Korrekturen zählen, Patterns identifizieren |
| Monatlich | 10 schlechteste Outputs analysieren, Checklisten erweitern |
| Quartalsweise | Gesamte Skill-Mastery-Plan reviewen: Was funktioniert? Was nicht? |

---

## 6. Sources

### SaaS Landing Page Design
1. [Unbounce: 26 SaaS Landing Pages](https://unbounce.com/conversion-rate-optimization/the-state-of-saas-landing-pages/) — Examples, trends, best practices (Aug 2025)
2. [Design Studio: 10 SaaS Landing Page Best Practices 2026](https://www.designstudiouiux.com/blog/saas-landing-page-design/) — Conversion-optimierte Strategien (Dec 2025)
3. [Fibr: 20 Best SaaS Landing Pages + 2026 Best Practices](https://fibr.ai/landing-page/saas-landing-pages) — Demo vs. Free Trial, High-Ticket B2B
4. [SaaSFrame: 10 SaaS Landing Page Trends 2026](https://www.saasframe.io/blog/10-saas-landing-page-trends-for-2026-with-real-examples) — Personality, interactivity, storytelling
5. [SaaS Landing Page Gallery](https://saaslandingpage.com/) — 890+ Landing Page Referenzen

### B2B SaaS Pricing
6. [Eleken: SaaS Pricing Page Design Best Practices](https://www.eleken.co/blog-posts/saas-pricing-page-design-8-best-practices-with-examples) — 9 Best Practices (Jul 2026)
7. [Kalungi: 12 Best SaaS Pricing Pages](https://www.kalungi.com/blog/best-saas-pricing-pages) — Design Trends für höhere Conversion
8. [Insivia: Designing B2B SaaS Pricing Pages](https://www.insivia.com/designing-saas-pricing-pages-that-convert/) — Personalisierung, Personas, Anchorring
9. [Design Studio: SaaS Pricing Page Best Practices 2026](https://www.designstudiouiux.com/blog/saas-pricing-page-design-best-practices/) — Social Proof, CTA-Platzierung, Anchoring

### McKinsey Presentation Design
10. [SlideModel: McKinsey Presentation Structure](https://slidemodel.com/mckinsey-presentation-structure/) — Pyramid Principle, MECE Framework (May 2025)
11. [Piktochart: How to Create McKinsey Style Presentations](https://piktochart.com/blog/mckinsey-style-presentation/) — Hypothesis-driven, Action Titles, MECE (Jun 2025)
12. [Slideworks: How McKinsey Consultants Make Presentations](https://slideworks.io/resources/how-mckinsey-consultants-make-presentations) — Font-Regeln, Margins, Templates
13. [SlideUplift: McKinsey-Style Presentations 2026](https://slideuplift.com/blog/mckinsey-style-presentation/) — Aktuelle Design-Prinzipien
14. [FlashDocs: McKinsey Slide Decks](https://www.flashdocs.com/post/how-mckinsey-consultants-make-slide-decks) — Eine Idee pro Slide, minimaler Text

### HTML & Accessibility
15. [MDN: HTML Good Basis for Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML) — Semantic Structure, Headings, Lists
16. [Carnegie Museums: Semantic HTML Guidelines](http://web-accessibility.carnegiemuseums.org/foundations/semantic/) — div/span = semantisch bedeutungslos
17. [Deque University: Semantic Elements Checklist](https://dequeuniversity.com/checklists/web/other-semantics) — Accessibility-Checkliste
18. [W3C Validator Docs](https://validator.w3.org/docs/errors.html) — Common Validation Errors
19. [Line25: 10 Common Validation Errors](https://line25.com/articles/10-common-validation-errors-and-how-to-fix-them/) — Fehlende Tags, Entity-Encoding

### B2B UX Design
20. [Onething Design: B2B SaaS UX Design 2026](https://www.onething.design/post/b2b-saas-ux-design) — Progressive Disclosure, Guided Steps
21. [Passionates: 13 UX Rules for B2B Web Applications](https://passionates.com/13-important-ux-rules-for-b2b-web-applications/) — Evidence-based UX Rules (Aug 2025)
22. [Adam Fard: B2B SaaS UX Design](https://adamfard.com/blog/b2b-saas-ux-design) — Functionality > Aesthetics
23. [Beetle Beetle: B2B UX Best Practices](https://beetlebeetle.com/post/ux-b2b-best-practices-tips) — Lead Qualification durch UX

### Cold Email & Outreach
24. [Reddit B2B Manufacturing: Cold Email Results](https://www.reddit.com/r/b2bmarketing/comments/1nk67rc/) — Multi-Threading across departments
25. [310 Creative: B2B Cold Outreach Structures](https://www.310creative.com/blog/email-structures-for-b2b-cold-outreach) — Personalisierung, Research
26. [Martal: Cold Email Statistics 2025](https://martal.ca/b2b-cold-email-statistics-lb/) — 5% Response Rate Benchmark, Segmentierung
27. [Clevenio: Ultimate Guide B2B Cold Emailing 2026](https://clevenio.com/ultimate-guide-for-b2b-cold-emailing/) — Email Cadence Strategien
28. [Evaboot: B2B Cold Email Subject Lines](https://evaboot.com/blog/b2b-cold-email-subject-lines) — Manufacturing-spezifische Subject Lines

### German Business Communication
29. [Tandem: Writing an Email in German](https://tandem.net/blog/how-to-write-an-email-in-german) — Sie vs. Du, formelle Standards
30. [Lingoda: Formal/Informal German Emails](https://www.lingoda.com/blog/en/how-to-write-an-email-in-german/) — Problem → Vorschlag → Aktion-Struktur
31. [Berlitz: German Email Etiquette](https://www.berlitz.com/blog/how-to-start-write-end-email-german-etiquette) — Greeting, Sign-off, Signatur

### AI Agent Quality Assurance
32. [PwC: Validating Multi-Agent AI Systems](https://www.pwc.com/us/en/services/audit-assurance/library/validating-multi-agent-ai-systems.html) — Evaluation Frameworks
33. [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — LLM-as-Judge, Static Analysis, Browser-Testing
34. [Medium: AI Agent Evaluation Frameworks](https://medium.com/online-inference/ai-agent-evaluation-frameworks-strategies-and-best-practices-9dc3cfdf9890) — Component Testing, Unit Tests

---

## Anhang: Quick Reference Card

### Die 5 Fragen vor JEDEM Delivery

1. **"Würde Florian das OHNE Änderungen an einen Kunden/Investor schicken?"** — Wenn nein, weiter iterieren.
2. **"Ist jede Zahl belegt?"** — Wenn nein, Quelle finden oder als Schätzung markieren.
3. **"Passt das Wording zur Positionierung?"** — Kein "kostenlos", kein "AI" wo nicht gewünscht.
4. **"Habe ich die Checkliste für diesen Output-Typ durchgegangen?"** — Wenn nein, jetzt tun.
5. **"Ist die neue Version wirklich besser als die vorherige?"** — Wenn unklar, vorherige beibehalten.

### Anti-Pattern Referenz (sofort stoppen wenn erkannt)

| Anti-Pattern | Erkennungszeichen | Sofort-Aktion |
|-------------|-------------------|---------------|
| Emoji in Profi-Doc | 🎯📊✅ in Präsentation | Alle Emojis entfernen |
| alert() in Code | `alert(` in JavaScript | Durch Toast-Component ersetzen |
| Unbeleger Claim | Runde Prozentzahl ohne Quelle | "~" hinzufügen oder recherchieren |
| Whitespace komprimiert | Margin <48px zwischen Sections | Zurück zu 48px+ |
| Nicht-existentes Feature | "Lizenz erforderlich" Modal | Feature entfernen |
| Falsche Dateitypen | JPEG/PNG für CNC | Nur PDF/STEP |
| AI-Branding | "KI-gestützt" Badge | "Automatische Analyse" |
| Redundante Formfelder | Email-Feld bei eingeloggtem User | Feld entfernen |
| "Kostenlos" in CTA | "Kostenlose Analyse" | "Demo anfordern" |
| CSS komprimiert | Einzeiliges CSS, reduzierte Margins | Original-Formatting beibehalten |

---

*Dieses Dokument wird bei jedem neuen Fehler aktualisiert.*
*Jede Korrektur von Florian → Neue Regel hier.*
*Ziel: 0 wiederholte Fehler. Jeder Fehler nur einmal.*

*Last updated: 2026-02-04*

# Full Website Audit — Ainary Platform
**Date:** 2026-02-14 | **Auditor:** QA Agent

---

## GESAMTSCORE: 42/100

The site has serious systemic issues: wrong color palette (dark theme vs. mandated light/bright), forbidden opacity:0 defaults everywhere, outdated product names ("X-Ray"), indigo colors still present, "we" voice in non-legal pages, missing OG meta tags, no print CSS, and font-weight violations.

---

## KRITISCHE FEHLER (sofort fixen)

### 1. ❌ DARK THEME statt LIGHT/BRIGHT
**Schweregrad: KRITISCH** — Design Rules sagen "Light/bright, substance over decoration"
- JEDE Seite nutzt `--bg-page: #08080c` (fast schwarz)
- Text ist `#ededf0` (fast weiß auf schwarzem Hintergrund)
- **Betrifft:** Alle 40+ aktiven Seiten
- **Fix:** Komplett auf helles Farbschema umstellen (weiß bg, schwarzer Text, Gold Akzente)

### 2. ❌ opacity:0 DEFAULTS (VERBOTEN lt. Design Rules)
**Schweregrad: KRITISCH** — "CSS: Always opacity:1 as default"
- `index.html:677`, `blog.html:120`, `about.html:272`, `pricing.html:134,205`
- `daily-brief.html:133,203`, `tools.html:689,769`, `landing.html:677`
- Alle DE-Pendants ebenfalls betroffen
- **Fix:** Alle `opacity: 0` durch `opacity: 1` ersetzen, Animationen anders lösen

### 3. ❌ INDIGO/BLAU Farben noch vorhanden
**Schweregrad: KRITISCH** — NUR Gold (#c8aa50), schwarz, weiß erlaubt
- `design-system.html:33-34` → `--accent: #6366f1`, `--accent-hover: #818cf8`
- `dashboard.html` → `.product-pill.indigo`, `.action-card.indigo` (Zeilen 382-571)
- `logo-options.html:60` → `color:#6366f1`
- **Fix:** Alle Indigo-Referenzen durch Gold (#c8aa50) oder neutrale Grautöne ersetzen

### 4. ❌ "X-Ray" Produktname veraltet → "Ainary Report"
- `design-system.html:717,848,853` → "Try X-Ray Free"
- `article.html:940` → Footer-Link "X-Ray"
- `terms.html:300` → "Corporate X-Ray, Startup X-Ray"
- `dashboard.html:730-731,783,798` → "Corporate X-Ray", "Startup X-Ray"
- **Fix:** Alle "X-Ray" durch aktuellen Produktnamen ersetzen

### 5. ❌ "We" statt "I" in nicht-juristischen Seiten
- `pricing.html:433` → "We help you apply."
- `pricing-tier.html:511,521` → "we offer", "We build"
- `pricing-simple.html:400` → "We build"
- `pricing-credits.html:699` → "We provide"
- `quality.html:6,8,684` → "How We Build" (Titel + Badge + OG)
- `design-system.html:961` → "HOW WE BUILD"
- **Fix:** Alles auf "I" / Solo-Founder-Voice umschreiben

---

## KONSISTENZ-PROBLEME

### 6. ❌ font-weight: 700 (max 600 erlaubt)
- `pricing-tier.html` → Zeilen 47, 142, 168, 249
- `pricing-simple.html` → Zeilen 47, 149, 227
- `pricing-credits.html` → Zeilen 47, 142, 154, 169, 245, 267, 289, 366, 385
- **Fix:** Alle `font-weight: 700` → `font-weight: 600`

### 7. ❌ Geist Font statt NUR Inter
- 20+ Seiten laden `geist@1.0.0` via CDN
- Design Rules: "Font: Inter, max weight 600"
- **Fix:** Geist-CDN-Links entfernen, Geist-Referenzen durch Inter ersetzen

### 8. ❌ Fehlende OG Meta Tags
- `about.html` → 0 OG Tags
- `pricing.html` → 0 OG Tags
- `contact.html` → nicht geprüft, wahrscheinlich 0
- `de/about.html` → 0 OG Tags
- `de/pricing.html` → 0 OG Tags
- **Fix:** OG title, description, image zu allen öffentlichen Seiten hinzufügen

### 9. ❌ Kein Print CSS auf keiner einzigen Seite
- 0 von 40+ Seiten haben `@media print`
- **Fix:** Globales Print-Stylesheet erstellen (mindestens für Report/Article-Seiten)

### 10. ❌ Externe Dependencies (CDN)
- Google Fonts (fonts.googleapis.com) — auf fast allen Seiten
- jsDelivr (cdn.jsdelivr.net) — Geist Font
- **Risiko:** DSGVO-Problem (Google Fonts), Performance-Abhängigkeit
- **Fix:** Fonts selbst hosten (DSGVO-Pflicht für EU!)

### 11. ❌ Dunkle "Grautöne" außerhalb der Farbpalette
- `#08080c`, `#18181f`, `#0e0e13`, `#1a1a22`, `#1e1e26` als Hintergrund
- `#ededf0`, `#8b8b95` als Textfarben
- `#d4b85c` als Gold-Hover (nicht #c8aa50)
- **Fix:** Nach Umstellung auf Light Theme: Palette auf schwarz/weiß/Gold vereinfachen

### 12. ⚠️ Fehlende Viewport-Meta
- `logo-options.html`, `test-logo-glow.html`
- (Interne Dev-Seiten, niedrige Priorität)

---

## PRO SEITE (Hauptseiten)

### index.html: 35/100
- ✅ Hat OG Tags (4)
- ✅ Viewport Meta vorhanden
- ✅ Email korrekt (florian@ainaryventures.com)
- ❌ Dunkles Theme (#08080c)
- ❌ opacity:0 (Zeile 677)
- ❌ Geist Font geladen
- ❌ Inline-Styles mit hardcoded #8b8b95 (Zeilen 954-955, 1196)
- ❌ Google Fonts + jsDelivr CDN (DSGVO)
- 💡 Light Theme, Fonts selbst hosten

### about.html: 30/100
- ✅ Email korrekt
- ✅ Solo-Founder-Voice überwiegend gut
- ❌ Dunkles Theme
- ❌ opacity:0 (Zeile 272)
- ❌ 0 OG Tags
- ❌ Geist Font + CDN
- ❌ "we" in Zeile 409 ("can we build it")
- 💡 OG Tags hinzufügen, Light Theme

### pricing.html: 35/100
- ✅ Email korrekt (2× florian@ainaryventures.com)
- ✅ Saubere Struktur
- ❌ Dunkles Theme
- ❌ opacity:0 (Zeilen 134, 205)
- ❌ 0 OG Tags
- ❌ "We help you apply." (Zeile 433)
- ❌ $10,000+ claim — verifiziert?
- 💡 "I help you apply", OG Tags

### tools.html: 40/100
- ✅ Hat OG Tags (3)
- ✅ Viewport Meta
- ❌ Dunkles Theme
- ❌ opacity:0 (Zeilen 689, 769)
- ❌ Geist Font
- 💡 Light Theme, opacity fix

### blog.html: 38/100
- ✅ Hat OG Tags (3)
- ❌ Dunkles Theme
- ❌ opacity:0 (Zeile 120)
- ❌ Non-standard Grautöne
- 💡 Light Theme

### quality.html: 25/100
- ❌ "How We Build" im Titel und OG (Solo-Founder-Violation)
- ❌ "HOW WE BUILD" Badge (Zeile 684)
- ❌ Geist Font
- 💡 "How I Build" überall

### design-system.html: 20/100
- ❌ Indigo #6366f1 als --accent (VERBOTEN)
- ❌ "Try X-Ray Free" Buttons (Zeilen 717, 848, 853)
- ❌ "HOW WE BUILD" Badge
- ❌ Rot/Grün Farben (#f87171, #34d399)
- ❌ badge-indigo Klasse
- 💡 Komplett überarbeiten — dieses Dokument definiert das falsche System

### dashboard.html: 20/100
- ❌ Indigo-Klassen durchgängig (.product-pill.indigo etc.)
- ❌ "Corporate X-Ray", "Startup X-Ray" (veraltet)
- ❌ Geist Font
- 💡 Produktnamen + Farbschema komplett updaten

### terms.html: 40/100
- ✅ Email korrekt
- ❌ "X-Ray" Referenzen (Zeile 300)
- ❌ Geist Font + CDN
- 💡 Produktnamen aktualisieren

### article.html: 35/100
- ❌ "X-Ray" im Footer (Zeile 940)
- ❌ Geist Font + CDN
- ❌ Dunkles Theme
- 💡 Produktnamen + Theme

### contact.html: 45/100
- ✅ Email korrekt (3× richtig)
- ✅ Saubere Struktur
- ❌ Dunkles Theme
- ❌ Keine OG Tags
- 💡 OG Tags, Light Theme

### login.html / signup.html: 35/100
- ❌ Geist Font + CDN
- ❌ Dunkles Theme
- 💡 Theme + Fonts

### pricing-tier.html / pricing-simple.html / pricing-credits.html: 25/100
- ❌ font-weight: 700 (massiv, 15+ Stellen)
- ❌ "We" Voice in FAQs
- ❌ Ältere Pricing-Varianten — sind die noch aktiv?
- 💡 Aufräumen: nur eine Pricing-Seite behalten

### daily-brief.html: 35/100
- ❌ opacity:0 (Zeilen 133, 203)
- ❌ Dunkles Theme
- 💡 Opacity + Theme fix

### report.html / reports.html: 35/100
- ❌ Geist Font
- ❌ Dunkles Theme
- 💡 Theme

### imprint.html: 45/100
- ✅ Email korrekt
- ✅ "We" OK in juristischem Kontext
- ❌ Geist Font
- 💡 Fonts selbst hosten

### privacy.html: 45/100
- ✅ Email korrekt
- ✅ DSGVO-Referenz vorhanden
- ❌ Google Fonts laden = DSGVO-Verstoß (ironic!)
- 💡 Fonts DRINGEND selbst hosten

### DE-Seiten (de/*.html): 35/100 (Durchschnitt)
- ✅ Übersetzungen vorhanden
- ✅ Emails korrekt
- ❌ Alle EN-Probleme 1:1 gespiegelt (opacity:0, dark theme, CDN, etc.)
- ❌ de/pricing.html:7 → EN-Beschreibung im Meta ("AI intelligence reports that would cost...")
- 💡 Meta-Description auf Deutsch übersetzen

### Interne/Dev-Seiten (logo-options, test-logo-glow, svg-graphics, loading, landing-v4, landing):
- ⚠️ Niedrige Priorität, aber: fehlende Viewport-Metas, Indigo-Farben
- 💡 Aufräumen oder in archive/ verschieben

---

## STATE OF THE ART VORSCHLÄGE

### Priorität 1 (Sofort)
1. **DSGVO: Google Fonts selbst hosten** — Rechtliches Risiko, Abmahnungsgefahr in DE
2. **Light Theme umsetzen** — Entspricht Design Rules + wirkt professioneller/seriöser für B2B
3. **opacity:0 → opacity:1** — Inhalte werden ggf. nicht angezeigt ohne JS
4. **"X-Ray" → aktuellen Produktnamen** überall ersetzen

### Priorität 2 (Diese Woche)
5. **OG Tags für alle öffentlichen Seiten** — Social Sharing sieht sonst kaputt aus
6. **"We" → "I"** in allen nicht-juristischen Seiten
7. **font-weight: 700 → 600** überall
8. **Indigo komplett entfernen** — nur Gold als Akzent
9. **Geist Font entfernen** — nur Inter

### Priorität 3 (Bald)
10. **Print CSS** für Reports/Articles — Nutzer wollen Reports drucken
11. **Alte Pricing-Varianten aufräumen** — 4 Pricing-Seiten ist verwirrend
12. **CSS Custom Properties vereinheitlichen** — Jede Seite definiert eigene Variablen
13. **Shared Header/Footer als Component** — Aktuell copy-pasted, Inkonsistenz-Quelle
14. **de/ Meta-Descriptions auf Deutsch** — Aktuell teilweise englisch

### State-of-the-Art 2026
15. **View Transitions API** für Seitenübergänge (Chrome 111+)
16. **Container Queries** statt nur Media Queries
17. **CSS :has() Selektor** für kontextabhängige Styles
18. **Subgrid** für komplexe Layouts
19. **Self-hosted variable font** (Inter Variable) — eine Datei statt 4 Gewichte
20. **Structured Data (JSON-LD)** für Articles/Pricing → bessere Google-Snippets
21. **Core Web Vitals optimieren** — CLS durch opacity:0 wahrscheinlich schlecht

---

## ZUSAMMENFASSUNG

| Kategorie | Score |
|---|---|
| Design-Konsistenz | 25/100 — Falsches Theme, falsche Farben, falsche Fonts |
| Inhalt | 50/100 — Emails OK, aber veraltete Produktnamen, "We"-Voice |
| Technisch | 35/100 — opacity:0, keine Print CSS, CDN-DSGVO, fehlende OG |
| State of the Art | 55/100 — Solide Basis, aber Dark-Theme-Entscheidung konträr zu Rules |

**GESAMTSCORE: 42/100**

**Hauptproblem:** Die Website wurde in einem Dark-Theme mit Indigo+Gold Dual-Accent gebaut, aber die Design Rules verlangen Light/Bright mit NUR Gold. Das ist kein Bug-Fix — das ist ein Theme-Rewrite. Alles andere (opacity, X-Ray, "we", OG-Tags) sind vergleichsweise schnelle Fixes.

---
*Generated by QA Agent, 2026-02-14*

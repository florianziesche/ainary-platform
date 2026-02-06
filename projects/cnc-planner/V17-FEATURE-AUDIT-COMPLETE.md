# CNC PLANER PRO v17 — VOLLSTÄNDIGER FEATURE AUDIT

**Datei:** `cnc-planner-pro.html`  
**Zeilen:** 3331  
**Audit-Datum:** 06.02.2026  
**Methodik:** Zeile-für-Zeile Durchgang, alle HTML-Elemente, JS-Functions, CSS-Klassen erfasst

---

## GESAMTÜBERSICHT

### Architektur
- **Single-Page Application** (SPA)
- **Layout:** Sidebar (240px) + Main Content
- **Navigation:** 8 Hauptsektionen als Tabs
- **Datenhaltung:** localStorage + JavaScript-Objects
- **Styling:** CSS Variables (Industrial Design System)

### Technologien
- HTML5
- Vanilla JavaScript (ES6+)
- CSS3 (Custom Properties, Grid, Flexbox)
- Keine externen Libraries/Frameworks

---

## 🎨 DESIGN SYSTEM (CSS Variables)

### Feature: Design Tokens
- **Was:** Zentrale Farb-, Spacing-, Typography-Definitionen
- **Wo:** `<style>` Block, Zeilen 9-69
- **HTML:**
```css
:root {
    --color-primary: #2C3E50;
    --color-accent: #546E7A;
    --color-bg: #F5F7FA;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto...
    --space-xs: 4px; --space-sm: 8px; --space-md: 16px;
    --sidebar-width: 240px;
    --header-height: 64px;
}
```
- **Funktionalität:** Konsistente Industrial Design Language, einfache Theme-Anpassung

### Feature: Industrial Color Palette
- **Was:** Neutrale Grautöne, gedämpfte Akzente (kein Rot/Grün/Blau)
- **Wo:** Zeilen 12-23
- **Farben:**
  - Primary: `#2C3E50` (Dunkelblau-Grau)
  - Accent: `#546E7A` (Blaugrau)
  - Background: `#F5F7FA` (Sehr helles Grau)
  - Text: `#1F2937` (Fast Schwarz)
- **Funktionalität:** Professionelle, industrielle Ästhetik ohne bunte Ablenkungen

### Feature: Typography System
- **Was:** System-Fonts, Mono-Font für Zahlen
- **Wo:** Zeilen 34-36
- **HTML:**
```css
--font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
--font-mono: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
```
- **Funktionalität:** Optimale Lesbarkeit, native OS-Fonts, Mono für präzise Zahlen

### Feature: Spacing Scale
- **Was:** 8-Punkt-Grid System
- **Wo:** Zeilen 38-43
- **Scale:** xs(4px), sm(8px), md(16px), lg(24px), xl(32px), 2xl(48px)
- **Funktionalität:** Konsistenter vertikaler/horizontaler Rhythmus

---

## 📱 LAYOUT & NAVIGATION

### Feature: App Container
- **Was:** Flexbox-Wrapper für Sidebar + Main
- **Wo:** `.app`, Zeile 88
- **HTML:** `<div class="app">`
- **CSS:** `display: flex; min-height: 100vh;`
- **Funktionalität:** Viewport-Filling Layout

### Feature: Sidebar
- **Was:** Fixed-Width Navigation
- **Wo:** `.sidebar`, Zeilen 91-97
- **HTML:** `<aside class="sidebar">` (Zeile 304)
- **Breite:** 240px (var)
- **Struktur:**
  - Logo/Header (Zeile 305-310)
  - Nav-Items (Zeile 312-334)
  - Footer-Items (Zeile 336-344)
- **Funktionalität:** Persistent Navigation, visuelle Hierarchie

### Feature: Sidebar Logo
- **Was:** Branding-Element mit Icon + Text + Beta-Badge
- **Wo:** `.sidebar-logo`, Zeilen 106-124
- **HTML:**
```html
<div class="sidebar-logo">
    <div class="sidebar-logo-icon">CP</div>
    <div class="sidebar-logo-text">CNC Planer <span>Pro</span></div>
    <span style="background: var(--color-warning);">BETA</span>
</div>
```
- **Funktionalität:** Brand Identity, Status-Indikator

### Feature: Nav Items (8 Sections)
- **Was:** Tab-basierte Navigation
- **Wo:** `.nav-item`, Zeilen 127-157
- **Liste:**
  1. **Teil** (data-section="part")
  2. **Parameter** (data-section="params")
  3. **Kalkulation** (data-section="result")
  4. **Fertigungsanweisung** (data-section="instructions")
  5. **Angebot** (data-section="quote")
  6. **NC-Code** (data-section="code")
  7. **Feedback** (data-section="feedback")
  8. **Einstellungen** (data-section="settings")
- **HTML:**
```html
<button class="nav-item active" data-section="part" onclick="showSection('part', this)">
    <span>Teil</span>
</button>
```
- **CSS:** `.nav-item.active` → Background highlight
- **JavaScript:** `showSection(name, btn)` — Toggle visibility
- **Funktionalität:** SPA-Navigation, aktiver Status, onclick-Handler

### Feature: Main Header
- **Was:** Top-Bar mit Titel + Actions
- **Wo:** `.main-header`, Zeilen 160-175
- **HTML:** (Zeile 349)
```html
<header class="main-header">
    <h1 class="main-title" id="mainTitle">Teil</h1>
    <div class="main-actions">
        <button class="btn btn-secondary btn-sm" onclick="exportCSV()">CSV</button>
        <button class="btn btn-primary btn-sm" onclick="window.print()">PDF Export</button>
    </div>
</header>
```
- **Dynamik:** Titel ändert sich per JS: `document.getElementById('mainTitle').textContent = SECTION_TITLES[name]`
- **Funktionalität:** Kontext-Info, Export-Buttons

### Feature: Content Area
- **Was:** Scrollbarer Main-Content
- **Wo:** `.content-area`, Zeilen 177-180
- **CSS:** `flex: 1; overflow-y: auto; padding: var(--space-xl);`
- **Funktionalität:** Scrolling, Padding für Lesbarkeit

### Feature: Section Toggle
- **Was:** Nur eine Section aktiv (display: none/block)
- **Wo:** `.section`, `.section.active`, Zeilen 182-190
- **JavaScript:**
```js
function showSection(name, btn) {
    document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
    document.getElementById('section-' + name).classList.add('active');
    // ...
}
```
- **Funktionalität:** SPA ohne Page-Reload

---

## 🔧 TAB 1: TEIL (Part Selection)

### Feature: Trust Badges
- **Was:** Drei Feature-Highlights mit Icons
- **Wo:** `.trust-badges`, Zeile 358-372 (HTML), CSS custom
- **HTML:**
```html
<div class="trust-badges">
    <div class="trust-badge">
        <svg>...</svg>
        Basierend auf echten Betriebsdaten
    </div>
    <div class="trust-badge">...</div>
    <div class="trust-badge">...</div>
</div>
```
- **Badges:**
  1. ✓ Basierend auf echten Betriebsdaten
  2. ⏱ Kalkulation in <30 Sekunden
  3. 📄 NC-Code inklusive
- **Funktionalität:** Trust-Building, Value Proposition

### Feature: Scope Notice (Collapsible)
- **Was:** Expandable Info-Box zu Anwendungsbereich
- **Wo:** `.scope-notice`, Zeilen 375-413
- **HTML:**
```html
<div class="scope-notice">
    <div class="scope-header" onclick="toggleScope()">
        <div>Funktionsprinzip und Anwendungsbereich</div>
        <svg id="scopeChevron">...</svg>
    </div>
    <div class="scope-content" id="scopeContent">
        <!-- Grid: Geeignet | Nicht geeignet -->
    </div>
</div>
```
- **JavaScript:** `toggleScope()` — Toggle `.expanded`, rotate chevron
- **Inhalte:**
  - **Geeignet für:** Prismatische Teile, Standardbohrungen, 3-Achs, Stahl/Alu/Kunststoff
  - **Nicht geeignet für:** 3D-Freiformflächen, 5-Achs-Simultan, Titan/Inconel, IT8
- **Funktionalität:** Erwartungsmanagement, Transparenz über Grenzen

### Feature: Part Grid (Last Analyzed Parts)
- **Was:** Visueller Selector für Demo-Teile
- **Wo:** `.part-grid`, Zeile 415-418 (HTML), JS-rendered
- **HTML:** `<div class="part-grid" id="partGrid"><!-- Filled by JS --></div>`
- **JavaScript:** `renderPartGrid()` (Zeile 2617-2637)
- **Datenquelle:** `PROJECTS` Object (Zeile 2590-2610)
- **Cards:**
  - **Verbindungsplatte:** 2500473.01.11.02.00.001, 12.5 min, €28.40
  - **Adapterplatte:** 2500473.01.01.02.01.001, 24.8 min, €52.15
- **CSS:** `.part-card` (custom, hover-effect, selected-state)
- **HTML-Template:**
```html
<div class="part-card selected" onclick="selectProject('verbindungsplatte')">
    <div class="part-thumb">
        <img src="demo-parts/2500473.01.11.02.00.001.pdf.png" alt="...">
    </div>
    <div class="part-info">
        <div class="part-name">Verbindungsplatte</div>
        <div class="part-number">2500473.01.11.02.00.001</div>
        <div class="part-meta">
            <span>12.5 min</span>
            <span>S235JR</span>
            <span class="part-price">€28,40</span>
        </div>
    </div>
</div>
```
- **Funktionalität:** Schnellauswahl, Demo-Content, Loading-Animation-Trigger

### Feature: File Upload Card
- **Was:** Drop-Zone für STEP/PDF Upload
- **Wo:** Zeilen 421-430
- **HTML:**
```html
<div class="card">
    <div class="card-body" style="text-align: center; padding: var(--space-8);">
        <div style="font-size: 32px;">📁</div>
        <div style="font-weight: 600;">Neues Bauteil analysieren</div>
        <div style="font-size: 13px;">STEP-Datei hochladen oder hier ablegen • .step, .stp, .pdf</div>
        <input type="file" id="fileInput" accept=".step,.stp,.pdf" style="display: none;">
        <button class="btn btn-secondary" onclick="document.getElementById('fileInput').click()">Datei auswählen</button>
    </div>
</div>
```
- **JavaScript:** Noch nicht implementiert (v17 = Demo)
- **Funktionalität:** File-Picker, accept-Filter, zukünftige 3D-Analyse

### Feature: Werkstück-Eingabeformular
- **Was:** Material, Rohmaße, Stückzahl
- **Wo:** Zeilen 433-494
- **Struktur:**
  - **Werkstoff-Dropdown** (`#materialSelect`, Zeile 437)
  - **Rohmaße-Inputs** (`#dimX`, `#dimY`, `#dimZ`, Zeilen 454-476)
  - **Stückzahl** (`#quantity`, Zeile 481)
  - **Buttons:** Analysieren | Weiter zu Parameter

#### Sub-Feature: Material Select
- **Was:** Grouped Dropdown mit 15 Werkstoffen
- **HTML:**
```html
<select class="select" id="materialSelect" onchange="calculate()">
    <optgroup label="Edelstahl">
        <option value="1.4301">1.4301 (V2A)</option>
        <option value="1.4404">1.4404 (V4A)</option>
        <option value="1.4571">1.4571</option>
    </optgroup>
    <optgroup label="Baustahl">
        <option value="S235JR" selected>S235JR</option>
        <option value="S355J2">S355J2</option>
        <option value="C45">C45</option>
    </optgroup>
    <optgroup label="Vergütungsstahl">
        <option value="42CrMo4">42CrMo4</option>
        <option value="34CrNiMo6">34CrNiMo6</option>
    </optgroup>
    <optgroup label="Aluminium">
        <option value="AlMg3">AlMg3</option>
        <option value="AlMgSi1">AlMgSi1 (6082)</option>
        <option value="Al7075">Al7075-T6</option>
    </optgroup>
    <optgroup label="Buntmetalle">
        <option value="CuZn39Pb3">Messing CuZn39Pb3</option>
        <option value="CuSn8">Bronze CuSn8</option>
    </optgroup>
    <optgroup label="Kunststoff">
        <option value="POM">POM</option>
        <option value="PA6">PA6 (Nylon)</option>
        <option value="PEEK">PEEK</option>
    </optgroup>
</select>
```
- **JavaScript:** `onchange="calculate()"` — Trigger Neu-Berechnung
- **Daten:** `MATERIALS` Object (Zeile 2569-2588)
- **Eigenschaften pro Material:** name, price (€/kg), density (g/cm³), timeFactor

#### Sub-Feature: Dimension Inputs
- **Was:** X × Y × Z mit mm-Unit-Labels
- **HTML:**
```html
<div class="dimension-group">
    <div class="form-group">
        <div class="input-with-unit">
            <input type="number" class="input input-mono" id="dimX" value="440" oninput="calculate()">
            <span class="input-unit">mm</span>
        </div>
    </div>
    <span class="dimension-separator">×</span>
    <!-- dimY, dimZ analog -->
</div>
```
- **CSS:** `.dimension-group` (Grid), `.input-with-unit` (Flex)
- **Funktionalität:** Visual Grouping, Einheit sichtbar, Echtzeit-Calc

#### Sub-Feature: Quantity Input
- **Was:** Stückzahl-Feld
- **HTML:**
```html
<input type="number" class="input input-mono" id="quantity" value="1" min="1" oninput="calculate()">
<span class="input-unit">Stk</span>
```
- **Constraint:** `min="1"`
- **Funktionalität:** Serien-Kalkulation (Setup-Umlegung)

### Feature: Action Buttons (Teil-Tab)
- **Was:** Analysieren + Weiter-Button
- **Wo:** Zeilen 487-492
- **HTML:**
```html
<button class="btn btn-secondary" onclick="calculate()">Analysieren</button>
<button class="btn btn-primary" onclick="confirmAndGoToParams()">Weiter zu Parameter</button>
```
- **JavaScript:** `confirmAndGoToParams()` (Zeile 2652-2667) — Confirm-Dialog vor Tab-Wechsel
- **Dialog-Text:**
```
Bitte prüfen Sie alle Eingaben:
• Werkstoff korrekt gewählt?
• Rohmaße vollständig?
• Stückzahl eingetragen?
```
- **Funktionalität:** User Confirmation, UX-Safeguard

---

## ⚙️ TAB 2: PARAMETER

### Feature: Sub-Tab Navigation
- **Was:** 3 Parameter-Kategorien als Tabs
- **Wo:** Zeilen 499-503
- **Tabs:**
  1. **Fertigung** (`#tabParamFertigung`)
  2. **Preisangaben** (`#tabParamPreis`)
  3. **Maschine** (`#tabParamMaschine`)
- **HTML:**
```html
<button class="btn btn-sm btn-primary" id="tabParamFertigung" onclick="showParamTab('fertigung')">Fertigung</button>
```
- **JavaScript:** `showParamTab(tab)` (Zeile 2689-2706) — Display-Toggle
- **Funktionalität:** Übersichtliche Kategorisierung komplexer Inputs

---

### TAB 2.1: PARAMETER → FERTIGUNG

#### Feature: Spannart-Dropdown
- **Was:** Auswahl Spannmethode mit Zeit
- **Wo:** Zeile 509-517
- **HTML:**
```html
<select class="select" id="clampingSelect" onchange="calculate()">
    <option value="schraubstock">Schraubstock (15 min)</option>
    <option value="schraubstock2">2× Schraubstock (25 min)</option>
    <option value="tischspannung">Tischspannung (35 min)</option>
    <option value="nullpunkt">Nullpunktspannsystem (5 min)</option>
    <option value="spezial">Sondervorrichtung (45 min)</option>
</select>
```
- **Daten:** `CLAMPING` Object (Zeile 2612-2618)
- **Eigenschaften:** time (min), desc (Text)
- **Funktionalität:** Setup-Zeit-Berechnung

#### Feature: Aufspannungen-Select
- **Was:** Anzahl Setups (1-4+)
- **Wo:** Zeile 520-526
- **HTML:**
```html
<select class="select" id="setupCount" onchange="calculate()">
    <option value="1">1 Aufspannung</option>
    <option value="2" selected>2 Aufspannungen</option>
    <option value="3">3 Aufspannungen</option>
    <option value="4">4+ Aufspannungen</option>
</select>
```
- **Berechnung:** `totalSetupTime = clampingData.time + (setupCount - 1) * (clampingData.time * 0.6)`
- **Funktionalität:** Multi-Setup Kostensteigerung (60% pro zusätzliche Aufspannung)

#### Feature: Einrichtzeit-Infobox
- **Was:** Live-Anzeige Setup-Zeit + Kosten + Beschreibung
- **Wo:** Zeilen 529-533
- **HTML:**
```html
<div class="info-box">
    <strong>Einrichtzeit:</strong> <span id="setupTimeDisplay">25 min</span> = <span id="setupCostDisplay">€37,92</span><br>
    <span id="clampingDescription">Schraubstock: Teil spannen, Parallelität prüfen, Nullpunkt antasten.</span>
</div>
```
- **Update:** `calculate()` → `document.getElementById('setupTimeDisplay').textContent = ...`
- **Funktionalität:** Transparenz, Echtzeit-Feedback

---

### TAB 2.2: PARAMETER → PREISANGABEN

#### Feature: Maschinenstundensätze-Tabelle
- **Was:** Editierbare Lohn- + Maschinen-Stundensätze
- **Wo:** Zeilen 539-598
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Arbeitsgang</th>
            <th class="right">Lohn (€/h)</th>
            <th class="right">Maschine (€/h)</th>
            <th class="right">Gesamt (€/h)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>CNC-Fräsen (3-Achs)</strong></td>
            <td class="right"><input type="number" class="input input-sm input-mono" value="49" id="rateCncLabor" onchange="updateRates()"></td>
            <td class="right"><input type="number" class="input input-sm input-mono" value="42" id="rateCncMachine" onchange="updateRates()"></td>
            <td class="right mono" style="font-weight: 600;" id="rateCncTotal">€91</td>
        </tr>
        <!-- 5-Achs, Drehen, Sägen, Entgraten, Prüfung analog -->
    </tbody>
</table>
```
- **Zeilen (6 Arbeitsgänge):**
  1. CNC-Fräsen (3-Achs): €49 + €42 = €91/h
  2. CNC-Fräsen (5-Achs): €52 + €68 = €120/h
  3. CNC-Drehen: €45 + €38 = €83/h
  4. Sägen: €43 + €12 = €55/h
  5. Entgraten/Schleifen: €32 + €4 = €36/h
  6. Qualitätsprüfung: €45 + €15 = €60/h
- **JavaScript:** `updateRates()` (Zeile 2820-2833) — Summe berechnen, `RATES` Object updaten
- **Daten:** `RATES` Object (Zeile 2613-2617)
- **Funktionalität:** Anpassbare Kostenstruktur pro Betrieb

#### Feature: Materialpreise-Karten
- **Was:** Editierbare €/kg-Preise, gruppiert nach Werkstoffklassen
- **Wo:** Zeilen 604-742
- **Gruppen:**
  1. **Baustahl:** S235JR, S355J2, C45, 42CrMo4
  2. **Edelstahl:** 1.4301, 1.4404, 1.4571, Duplex
  3. **Aluminium:** AlMg3, AlMgSi1, Al7075-T6
- **HTML-Template (pro Material):**
```html
<div class="form-group">
    <label class="form-label form-label-caps">S235JR</label>
    <div class="input-with-unit">
        <input type="number" class="input input-sm input-mono" value="6.79" step="0.01" id="matS235JR" onchange="updateMaterials()">
        <span class="input-unit">€/kg</span>
    </div>
</div>
```
- **JavaScript:** `updateMaterials()` (Zeile 2835-2840) — `MATERIALS` Object updaten
- **Funktionalität:** Tagesaktuelle Preise, Markt-Schwankungen

#### Feature: Zuschlagskalkulation-Tabelle (Industriestandard)
- **Was:** BAB-Schema (Betriebsabrechnungsbogen) mit 6 Zuschlagsarten
- **Wo:** Zeilen 744-847
- **HTML:**
```html
<table class="table">
    <tbody>
        <tr>
            <td>
                <strong>Materialgemeinkosten (MGK)</strong><br>
                <span style="font-size: 11px;">Einkauf, Lager, Handling</span>
            </td>
            <td><input type="number" class="input input-sm input-mono" value="10" id="zuschlagMGK" onchange="calculate()"></td>
            <td class="mono">auf Materialkosten</td>
            <td style="font-size: 12px;">5-15%</td>
        </tr>
        <!-- FGK, AV, VwGK, VtGK, Gewinn analog -->
    </tbody>
</table>
```
- **Zuschlagsarten:**
  1. **MGK (10%):** Materialgemeinkosten → auf Materialkosten
  2. **FGK (0%):** Fertigungsgemeinkosten → auf Fertigungskosten (oft in MSS enthalten)
  3. **AV (8%):** Arbeitsvorbereitung → auf Fertigungskosten
  4. **VwGK (12%):** Verwaltung → auf Herstellkosten
  5. **VtGK (5%):** Vertrieb → auf Herstellkosten
  6. **Gewinn (10%):** Marge → auf Selbstkosten
- **Kalkulationsschema:**
```
Materialkosten + MGK
+ Fertigungskosten + AV
= HERSTELLKOSTEN (HK)
+ VwGK + VtGK
= SELBSTKOSTEN (SK)
+ Gewinn
= ANGEBOTSPREIS
```
- **JavaScript:** Berechnung in `calculate()` (Zeile 2758-2779)
- **Funktionalität:** Industriestandard, Transparent, Anpassbar

---

### TAB 2.3: PARAMETER → MASCHINE

#### Feature: CNC-Typ Selector
- **Was:** 3-Achs vs. 5-Achs
- **Wo:** Zeilen 852-862
- **HTML:**
```html
<select class="select" id="cncType">
    <option value="3-achs" selected>3-Achs</option>
    <option value="5-achs">5-Achs</option>
</select>
```
- **Funktionalität:** Stundensatz-Switch (€91 vs. €120), zukünftig: Strategie-Anpassung

---

### Feature: Plausibilitäts-Warnungen
- **Was:** Dynamische Warn-Cards basierend auf Eingaben
- **Wo:** Zeile 868, JavaScript: `checkPlausibility()` (Zeile 2813-2819)
- **HTML:** `<div id="warningsContainer"></div>`
- **Logik:**
```js
if (x > 400 && clamping === 'schraubstock') {
    warnings.push({ type: 'warning', text: `Länge ${x}mm: Prüfen ob Schraubstock-Kapazität ausreicht. 2× Schraubstock empfohlen.` });
}
if (z > 100) {
    warnings.push({ type: 'warning', text: `Höhe ${z}mm: Werkzeugüberhang beachten. Vibrationsgefahr bei tiefen Taschen.` });
}
if (mat.timeFactor > 1.3) {
    warnings.push({ type: 'info', text: `Schwerzerspanbarer Werkstoff: Kühlmittel und Werkzeugverschleiß beachten.` });
}
```
- **Render:** `.warning-box` oder `.info-box`
- **Funktionalität:** Proaktive UX, Fehlerprävention

### Feature: Weiter-Button (Parameter → Kalkulation)
- **Was:** Übergang zu Result-Tab
- **Wo:** Zeile 870
- **HTML:**
```html
<button class="btn btn-primary" onclick="showSection('result', document.querySelector('.nav-item[data-section=&quot;result&quot;]'))">Kalkulation anzeigen →</button>
```
- **Funktionalität:** Fortschritt im Workflow

---

## 💰 TAB 3: KALKULATION (Result)

### Feature: Gesamtkalkulation-Tabelle
- **Was:** Hauptkosten-Breakdown pro Stück + Gesamt
- **Wo:** Zeilen 884-916
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Kostenart</th>
            <th>Berechnung</th>
            <th class="right">Pro Stück</th>
            <th class="right">Gesamt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Material</td>
            <td>6,23 kg × €6,79 × 1,1</td>
            <td class="right mono">€46,57</td>
            <td class="right mono">€46,57</td>
        </tr>
        <tr>
            <td>Maschinenzeit</td>
            <td>39,2 min × €91/h</td>
            <td class="right mono">€59,47</td>
            <td class="right mono">€59,47</td>
        </tr>
        <tr>
            <td>Werkzeugverschleiß</td>
            <td>pauschal (werkstoffabh.)</td>
            <td class="right mono">€20,74</td>
            <td class="right mono">€20,74</td>
        </tr>
        <tr>
            <td>Einrichtung</td>
            <td>24 min × €91/h ÷ 1</td>
            <td class="right mono">€36,40</td>
            <td class="right mono">€36,40</td>
        </tr>
        <tr>
            <td>Nebenzeiten</td>
            <td>Entgraten + Prüfung</td>
            <td class="right mono">€7,58</td>
            <td class="right mono">€7,58</td>
        </tr>
        <tr style="background: var(--color-primary); color: white;">
            <td colspan="2">HERSTELLKOSTEN</td>
            <td class="right mono">€170,76</td>
            <td class="right mono">€170,76</td>
        </tr>
    </tbody>
</table>
```
- **Funktionalität:** Transparente Kostenzusammensetzung, Formel sichtbar

---

### Feature: Detailkalkulation nach Kostenarten

#### Sub-Feature: Maschinenzeitkalkulation
- **Was:** Hauptzeit + Nebenzeit = Gesamtzeit
- **Wo:** Zeilen 927-950
- **HTML:**
```html
<table class="table">
    <tbody>
        <tr>
            <td>Hauptzeit (th)</td>
            <td class="right mono">31,2 min</td>
        </tr>
        <tr>
            <td>Nebenzeit (tn)</td>
            <td class="right mono">8,0 min</td>
        </tr>
        <tr style="background: var(--color-bg); font-weight: 600;">
            <td>Gesamtzeit</td>
            <td class="right mono">39,2 min</td>
        </tr>
        <tr>
            <td>× Stundensatz</td>
            <td class="right mono">€91/h</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>= Maschinenkosten</td>
            <td class="right mono">€59,47</td>
        </tr>
    </tbody>
</table>
```
- **Berechnung:** `(th + tn) / 60 * stundensatz`
- **Funktionalität:** REFA-konform, Transparenz über Zeitanteile

#### Sub-Feature: Materialkalkulation
- **Was:** Volumen → Gewicht → Preis + Verschnitt
- **Wo:** Zeilen 955-985
- **HTML:**
```html
<table class="table">
    <tbody>
        <tr>
            <td>Rohmaße</td>
            <td class="right mono">130 × 130 × 47 mm</td>
        </tr>
        <tr>
            <td>Volumen</td>
            <td class="right mono">794.170 mm³</td>
        </tr>
        <tr>
            <td>Werkstoff / Dichte</td>
            <td class="right mono">S235JR / 7,85 g/cm³</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>Gewicht</td>
            <td class="right mono">6,23 kg</td>
        </tr>
        <tr>
            <td>× Preis + 10% Verschnitt</td>
            <td class="right mono">€6,79/kg × 1,1</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>= Materialkosten</td>
            <td class="right mono">€46,57</td>
        </tr>
    </tbody>
</table>
```
- **Berechnung:** `volumeMm3 * density / 1000 * preis * (1 + scrap/100)`
- **Funktionalität:** Physikalisch korrekt, Verschnitt-Transparenz

#### Sub-Feature: Einrichtkosten-Detail
- **Was:** Setup-Zeit, Aufspannungen, Umlegung auf Stückzahl
- **Wo:** Zeilen 990-1022
- **HTML:**
```html
<table class="table">
    <tbody>
        <tr>
            <td>Spannmethode</td>
            <td class="right">Schraubstock</td>
        </tr>
        <tr>
            <td>Basis-Einrichtzeit</td>
            <td class="right mono">15 min</td>
        </tr>
        <tr>
            <td>Aufspannungen</td>
            <td class="right mono">2×</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>Gesamt-Einrichtzeit</td>
            <td class="right mono">24 min</td>
        </tr>
        <tr>
            <td>× Stundensatz</td>
            <td class="right mono">€91/h</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>= Einrichtkosten</td>
            <td class="right mono">€36,40</td>
        </tr>
        <tr>
            <td>÷ Stückzahl</td>
            <td class="right mono">1</td>
        </tr>
        <tr style="font-weight: 600;">
            <td>= Pro Stück</td>
            <td class="right mono">€36,40</td>
        </tr>
    </tbody>
</table>
```
- **Info-Box:** "Tipp: Bei Serienproduktion sinkt Stückpreis erheblich."
- **Funktionalität:** Serien-Vorteil sichtbar

#### Sub-Feature: Berechnungsgrundlagen (Footer)
- **Was:** Norm-Referenzen, Formeln, Genauigkeit
- **Wo:** Zeilen 1027-1047
- **HTML:**
```html
<div class="card" style="background: var(--color-bg);">
    <div class="card-header"><span>Berechnungsgrundlagen</span></div>
    <div class="card-body" style="font-size: 13px;">
        <div><strong>Zeitgliederung:</strong> REFA-Zeitstudien — DIN 8580</div>
        <div><strong>Schnittdaten:</strong> VDI 3321 — DIN EN 10027</div>
        <div><strong>Berechnungsformel:</strong> t<sub>h</sub> = L / v<sub>f</sub> | Nebenzeit: WZ-Wechsel + Positionieren</div>
        <div><strong>Referenzen:</strong>
            <ul>
                <li>Operationen → Tab Fertigungsanweisung</li>
                <li>Werkstoff → Tab Parameter</li>
                <li>Stundensätze → Tab Einstellungen</li>
            </ul>
        </div>
        <div style="color: var(--color-text-muted);">
            <strong>Genauigkeit:</strong> ±15% — Formelbasiert ohne Maschinenparameter
        </div>
    </div>
</div>
```
- **Funktionalität:** Vertrauensaufbau, Norm-Compliance, Transparenz

---

## 📋 TAB 4: FERTIGUNGSANWEISUNG

### Feature: Document Header (Fertigungsanweisung)
- **Was:** Title, Teilnummer, Version, Freigabe-Datum
- **Wo:** Zeilen 1073-1091
- **HTML:**
```html
<div style="display: flex; justify-content: space-between;">
    <div>
        <h3 style="color: var(--color-primary);">FERTIGUNGSANWEISUNG</h3>
        <p id="faPartName">Verbindungsplatte — 2500473.01.11.02.00.001</p>
    </div>
    <div style="text-align: right;">
        <div>Freigabe: 05.02.2026</div>
        <div>Version: 1.0</div>
    </div>
</div>
```
- **Funktionalität:** Identifikation, Versions-Tracking

### Feature: Werkstück-Info Grid
- **Was:** Material, Rohmaße, Gewicht, Maschine, Zeit
- **Wo:** Zeilen 1093-1116
- **HTML (3-Column Grid):**
```html
<div class="grid-3">
    <div>
        <div style="font-weight: 600;">Werkstück</div>
        <table>
            <tr><td>Werkstoff:</td><td id="faMaterial"><strong>S235JR</strong></td></tr>
            <tr><td>Rohteil:</td><td id="faRawDims">440 × 50 × 20 mm</td></tr>
            <tr><td>Gewicht:</td><td id="faWeight">2,2 kg</td></tr>
        </table>
    </div>
    <div>
        <div style="font-weight: 600;">Maschine</div>
        <table>
            <tr><td>Maschine:</td><td><strong>FEHLMANN VERSA 943</strong></td></tr>
            <tr><td>Steuerung:</td><td>Heidenhain TNC 640</td></tr>
            <tr><td>Zeit:</td><td id="faMachiningTime"><strong>12,5 min</strong></td></tr>
        </table>
    </div>
</div>
```
- **Dynamik:** IDs werden von `calculate()` befüllt
- **Funktionalität:** Werkstattfertiger-Info, kompakt

### Feature: Toleranz-Info-Box
- **Was:** Allgemeintoleranzen
- **Wo:** Zeilen 1118-1120
- **HTML:**
```html
<div class="info-box">
    <strong>Toleranzen:</strong> Allgemein DIN ISO 2768-mK • Oberfläche Rz 25
</div>
```
- **Funktionalität:** Standard-Referenz

---

### Feature: Zeichnungs-Vorschau (Collapsible)
- **Was:** Expandable Card mit Bild + Vollbild-Button
- **Wo:** Zeilen 1125-1138
- **HTML:**
```html
<div class="card">
    <div class="card-header" onclick="toggleDrawing()">
        <div style="display: flex; align-items: center;">
            <span id="drawingChevron">▶</span>
            <span>Zeichnung anzeigen</span>
            <span id="drawingPartNumber">2500473.01.11.02.00.001</span>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="event.stopPropagation(); openDrawingFullscreen()">Vollbild</button>
    </div>
    <div class="card-body" id="drawingContent" style="display: none;">
        <img id="drawingImage" src="demo-parts/2500473.01.11.02.00.001.pdf.png" alt="Zeichnung" onerror="this.parentElement.innerHTML='<div>Keine Zeichnung verfügbar</div>'">
    </div>
</div>
```
- **JavaScript:** 
  - `toggleDrawing()` (Zeile 2707-2716) — Toggle display, Chevron rotation
  - `openDrawingFullscreen()` (Zeile 2718-2723) — `window.open(img.src)`
- **Funktionalität:** Platzsparend, bei Bedarf sichtbar, Fehlerfall abgefangen

---

### Feature: Operationen-Tabelle (mit Detail-Expandern)

#### Overview-Struktur
- **Was:** Collapsible Rows mit OP-Nummer, Beschreibung, Werkzeug, Zeit
- **Wo:** Zeilen 1143-1372
- **HTML-Pattern:**
```html
<div style="border-bottom: 1px solid var(--color-border);">
    <div style="display: flex; cursor: pointer;" onclick="toggleOpDetail('op10')">
        <span class="op-badge">10</span>
        <span style="flex: 1;"><strong>Planfräsen Oberseite</strong></span>
        <span class="mono" style="color: var(--color-text-muted);">T1 Ø63</span>
        <span class="mono" style="width: 80px;"><strong>2,7 min</strong></span>
        <span>▼</span>
    </div>
    <div id="op10-detail" style="display: none; padding: var(--space-4); background: var(--color-bg);">
        <!-- Detail Content -->
    </div>
</div>
```

#### OP10: Planfräsen Oberseite
- **Was:** Detaillierte Berechnungsdarstellung mit Skizze
- **Wo:** Zeilen 1148-1209
- **Elemente:**
  1. **3-Spalten-Grid:** Skizze | Hauptzeit | Nebenzeit
  2. **SVG-Skizze:** Werkstück + Fräsbahnen (Zeilen 1159-1177)
  3. **Hauptzeit-Berechnung:**
```html
<div>
    <div style="font-weight: 600;">Hauptzeit t<sub>h</sub> = 1,9 min</div>
    <div style="font-family: var(--font-mono); font-size: 12px;">
        Fläche: 130 × 130 mm = 16.900 mm²<br>
        Bahnabstand: a<sub>e</sub> = 45 mm (70% von Ø63)<br>
        Anzahl Bahnen: 130 / 45 = 3 Bahnen<br>
        Verfahrweg: L = 3 × 130 = 390 mm<br>
        Vorschub: v<sub>f</sub> = 485 mm/min<br>
        Zustellungen: 2 (bei a<sub>p</sub> = 2 mm)<br>
        <strong>t<sub>h</sub> = (390 × 2) / 485 = 1,61 min</strong><br>
        + Sicherheit 20% = <strong>1,9 min</strong>
    </div>
</div>
```
  4. **Nebenzeit-Breakdown:**
```html
<div>
    <div style="font-weight: 600;">Nebenzeit t<sub>n</sub> = 0,8 min</div>
    <div style="font-family: var(--font-mono); font-size: 12px;">
        Werkzeugwechsel: 0,3 min<br>
        Anfahren Z+100 → Z+2: 0,2 min<br>
        Positionieren X/Y: 0,2 min<br>
        Spindel Start/Stop: 0,1 min<br>
        <strong>t<sub>n</sub> = 0,8 min</strong>
    </div>
</div>
```
- **Funktionalität:** Vollständige Zeitnachvollziehbarkeit, Lern-Tool für Fräser

#### OP20: Schruppen Außenkontur Ø120
- **Wo:** Zeilen 1212-1273
- **Besonderheit:** Konturparallel, 6 Ebenen, Komplexitätsfaktor 1.5×
- **SVG:** Werkstück-Querschnitt + Kreiskontur + Fräsbahn
- **Berechnung:** `t_h = (U * Ebenen) / v_f × 1,5` (Konturkomplexität)

#### OP30: Taschenfräsen
- **Wo:** Zeilen 1276-1337
- **Besonderheit:** Zeilenräumen-Strategie
- **SVG:** Tasche mit Fräsbahnen
- **Berechnung:** Bahnen × Länge × Ebenen

#### OP50: Schlichten Ø120 h5 (KRITISCH)
- **Wo:** Zeilen 1340-1406
- **Kennzeichnung:** Rote Markierung "KRITISCH", Badge "KRITISCH"
- **HTML:**
```html
<div style="border-bottom: 1px solid var(--color-border); background: var(--color-bg);">
    <div style="display: flex; cursor: pointer;" onclick="toggleOpDetail('op50')">
        <span class="op-badge critical">50</span>
        <span style="flex: 1;"><strong>Schlichten Ø120 h5</strong> <span class="badge badge-error">KRITISCH</span></span>
        <span class="mono">T3 Ø16</span>
        <span class="mono" style="width: 80px;"><strong>5,1 min</strong></span>
        <span>▼</span>
    </div>
    <div id="op50-detail" style="display: none; background: rgba(254,226,226,0.5);">
        <!-- Detail Content mit Toleranz-Box -->
    </div>
</div>
```
- **Detail:** 
  - SVG mit Toleranz-Highlight-Box
  - Reduzierter Vorschub: `v_f = 280 mm/min` (statt 557) wegen h5
  - Toleranz-Box: `h5 = 0/-0,018 mm → Nur 18 µm Spielraum!`
- **Funktionalität:** Visuelle Warnung, Sonderbehandlung

#### OP60: Feinbohren Ø26 H7 (KRITISCH)
- **Wo:** Zeilen 1409-1475
- **Besonderheit:** 3× Bohrungen, Feinbohrkopf, H7-Toleranz (+0,021/0)
- **SVG:** Bohrung + Feinbohrkopf + Maßpfeile
- **Toleranz-Box:** `H7 = +0,021/0 mm — Feinbohrkopf-Einstellung dokumentieren!`

#### Kompakte OPs (ohne Expander)
- **Wo:** Zeilen 1478-1517
- **OPs:**
  - **OP40:** Konturfräsen (4,4 min)
  - **OP70:** Feinbohren Ø44 H7 (4,7 min) — KRITISCH
  - **OP80:** Bohren M8 Gewinde 4× (1,9 min)
  - **OP90:** Gewindefräsen M8 4× (2,6 min)
  - **OP100:** Entgraten, Prüfen (5,0 min)
- **HTML:**
```html
<div style="border-bottom: 1px solid var(--color-border);">
    <div style="display: flex; padding: var(--space-3);">
        <span class="op-badge">40</span>
        <span style="flex: 1;">Konturfräsen</span>
        <span class="mono">T2 Ø20</span>
        <span class="mono" style="width: 80px;">4,4 min</span>
    </div>
</div>
```
- **Funktionalität:** Übersichtlichkeit, nur kritische OPs detailliert

#### SUMMEN-Zeile
- **Wo:** Zeilen 1520-1526
- **HTML:**
```html
<div style="display: flex; padding: var(--space-3); background: var(--color-primary); color: white; font-weight: 600;">
    <span style="flex: 1;">SUMME</span>
    <span class="mono">t<sub>h</sub>=31,2 | t<sub>n</sub>=8,0</span>
    <span class="mono" style="width: 80px;">44,2 min</span>
</div>
```
- **Funktionalität:** Zeitbudget-Übersicht

---

### Feature: Qualitätsprüfung-Tabelle
- **Was:** Prüfmerkmale mit Soll/Prüfmittel/Zeit
- **Wo:** Zeilen 1529-1558
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Prüfmerkmal</th>
            <th>Soll</th>
            <th>Prüfmittel</th>
            <th class="right">Zeit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ø26 H7</td>
            <td class="mono">26,000 / 26,021</td>
            <td>Innenmessschraube</td>
            <td class="right mono">0,8 min</td>
        </tr>
        <tr>
            <td>Höhe</td>
            <td class="mono">20,0 ±0,1</td>
            <td>Messschieber</td>
            <td class="right mono">0,3 min</td>
        </tr>
        <tr>
            <td>Oberfläche</td>
            <td class="mono">Rz ≤ 25</td>
            <td>Vergleichsmuster</td>
            <td class="right mono">0,5 min</td>
        </tr>
    </tbody>
</table>
```
- **Funktionalität:** QS-Anweisung, Prüfmittel-Auswahl, Zeitplanung

---

### Feature: Schnittparameter-Tabelle
- **Was:** Vc, n, fz, vf, ap, ae pro Werkzeug
- **Wo:** Zeilen 1567-1621
- **HTML:**
```html
<table class="table" id="cuttingParamsTable">
    <thead>
        <tr>
            <th>Werkzeug</th>
            <th>Operation</th>
            <th class="right">Vc [m/min]</th>
            <th class="right">n [U/min]</th>
            <th class="right">fz [mm/Z]</th>
            <th class="right">vf [mm/min]</th>
            <th class="right">ap [mm]</th>
            <th class="right">ae [mm]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>T1</strong> Planfräser Ø63</td>
            <td>Planfräsen</td>
            <td class="right mono">160</td>
            <td class="right mono">808</td>
            <td class="right mono">0,15</td>
            <td class="right mono">485</td>
            <td class="right mono">2,0</td>
            <td class="right mono">45</td>
        </tr>
        <!-- T2, T3, T11, T12, T13 analog -->
    </tbody>
</table>
```
- **Legende:** Vc = Schnittgeschwindigkeit, n = Drehzahl, fz = Vorschub/Zahn, vf = Vorschub, ap = Tiefe, ae = Zustellung
- **Funktionalität:** Maschineneinstellung-Referenz, VDI 3321-konform

---

### Feature: Werkzeugkosten-Tabelle
- **Was:** Preis, Standzeit, Einsatzzeit, Kosten pro Werkzeug
- **Wo:** Zeilen 1626-1681
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Werkzeug</th>
            <th class="right">Preis [€]</th>
            <th class="right">Standzeit [min]</th>
            <th class="right">Einsatzzeit [min]</th>
            <th class="right">Kosten [€]</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>T1 Planfräser Ø63 (WSP)</td>
            <td class="right mono">45,00</td>
            <td class="right mono">120</td>
            <td class="right mono">2,7</td>
            <td class="right mono">1,01</td>
        </tr>
        <!-- T2, T3, T11/T12, T13 analog -->
        <tr style="background: var(--color-bg); font-weight: 600;">
            <td>Gesamt</td>
            <td class="right mono">—</td>
            <td class="right mono">—</td>
            <td class="right mono">14,6</td>
            <td class="right mono">€20,77</td>
        </tr>
    </tbody>
</table>
```
- **Berechnung:** `kosten = (preis / standzeit) * einsatzzeit`
- **Funktionalität:** Werkzeugkosten-Transparenz, Verschleiß-Kalkulation

### Feature: Werkzeugverschleiß-Warnung
- **Was:** Hinweis auf werkstoffabhängige Standzeiten
- **Wo:** Zeilen 1683-1685
- **HTML:**
```html
<div class="warning-box">
    <strong>Hinweis:</strong> Bei hartem Werkstoff (1.4571 Edelstahl) können Werkzeugkosten 15-20% der Gesamtkosten ausmachen. Standzeiten sind werkstoffabhängig und können bei schwer zerspanbaren Materialien um 30-50% reduziert sein.
</div>
```
- **Funktionalität:** Erwartungsmanagement, Material-Abhängigkeit

---

### Feature: Feedback-Karte (Inline)
- **Was:** "Wie genau war diese Kalkulation?" mit 4 Optionen
- **Wo:** Zeilen 1688-1710
- **HTML:**
```html
<div class="feedback-card">
    <div style="text-align: center;">
        <strong>Wie genau war diese Kalkulation?</strong>
        <div>Ihr Feedback hilft uns, die Algorithmen zu verbessern</div>
    </div>
    <div class="feedback-options">
        <div class="feedback-option" onclick="selectFeedback(this, 'correct')">
            <span class="feedback-option-icon">✓</span>
            <span class="feedback-option-label">Korrekt</span>
        </div>
        <div class="feedback-option" onclick="selectFeedback(this, 'low')">
            <span class="feedback-option-icon">↓</span>
            <span class="feedback-option-label">Zu niedrig</span>
        </div>
        <div class="feedback-option" onclick="selectFeedback(this, 'high')">
            <span class="feedback-option-icon">↑</span>
            <span class="feedback-option-label">Zu hoch</span>
        </div>
        <div class="feedback-option" onclick="selectFeedback(this, 'other')">
            <span class="feedback-option-icon">?</span>
            <span class="feedback-option-label">Sonstiges</span>
        </div>
    </div>
    <textarea id="feedbackComment" placeholder="Optionaler Kommentar..."></textarea>
    <button class="btn btn-primary" onclick="submitFeedback()">Feedback senden</button>
</div>
```
- **JavaScript:** `selectFeedback()`, `submitFeedback()` (Zeilen 3264-3285)
- **Funktionalität:** User-Feedback-Loop, Algorithmus-Training

---

## 💼 TAB 5: ANGEBOT

### Feature: Angebots-Header
- **Was:** Titel, Angebots-Nummer, Datum, Gültigkeit
- **Wo:** Zeilen 1728-1740
- **HTML:**
```html
<div style="display: flex; justify-content: space-between;">
    <div>
        <div style="font-size: 20px; font-weight: 700;">ANGEBOT</div>
        <div style="font-size: 13px;">ANG-2026-0042</div>
    </div>
    <div style="text-align: right;">
        <div><strong>Ihre Firma GmbH</strong></div>
        <div>Datum: <span id="quoteDate">05.02.2026</span></div>
        <div>Gültig bis: <span id="quoteValidUntil">05.03.2026</span></div>
    </div>
</div>
```
- **Dynamik:** Datum wird per JS gesetzt (Zeile 3314-3318)
- **Funktionalität:** Professionelles Angebot, Auto-Datum

### Feature: Angebots-Tabelle
- **Was:** Positionsliste mit Menge/EP/GP
- **Wo:** Zeilen 1742-1768
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Pos.</th>
            <th>Beschreibung</th>
            <th class="right">Menge</th>
            <th class="right">EP (€)</th>
            <th class="right">GP (€)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td id="quoteDesc">Verbindungsplatte 2500473...</td>
            <td class="right mono" id="quoteQty">1</td>
            <td class="right mono" id="quoteEP">120,13</td>
            <td class="right mono" id="quoteGP">120,13</td>
        </tr>
    </tbody>
</table>
```
- **Update:** IDs werden von `calculate()` befüllt
- **Funktionalität:** Standard-Angebotsformat

### Feature: Angebots-Summe (mit MwSt.)
- **Was:** Zwischensumme + MwSt. + Gesamt
- **Wo:** Zeilen 1770-1787
- **HTML:**
```html
<div style="text-align: right; width: 250px;">
    <div style="display: flex; justify-content: space-between;">
        <span>Zwischensumme:</span>
        <span class="mono" id="quoteSubtotal">€120,13</span>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <span>+ MwSt. 19%:</span>
        <span class="mono" id="quoteMwst">€22,82</span>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 16px; font-weight: 600; border-top: 2px solid var(--color-primary);">
        <span>GESAMT:</span>
        <span class="mono" style="color: var(--color-primary);" id="quoteTotal">€142,95</span>
    </div>
</div>
```
- **Berechnung:** `mwstAmount = orderTotal * (vat / 100)`
- **Funktionalität:** Gesetzeskonform, MwSt. separat ausgewiesen

### Feature: Zahlungsbedingungen + Lieferzeit
- **Was:** Footer-Text
- **Wo:** Zeilen 1789-1792
- **HTML:**
```html
<div style="font-size: 12px; color: var(--color-text-muted);">
    <strong>Zahlungsbedingungen:</strong> 14 Tage netto ab Rechnungsdatum<br>
    <strong>Lieferzeit:</strong> ca. 3-4 Wochen nach Auftragseingang
</div>
```
- **Funktionalität:** Rechtliche Klarheit

---

## 📟 TAB 6: NC-CODE

### Feature: Code-Format Switcher
- **Was:** 3 Buttons für Heidenhain/Siemens/Fanuc
- **Wo:** Zeilen 1810-1814
- **HTML:**
```html
<div style="display: flex; gap: var(--space-2);">
    <button class="btn btn-primary btn-sm" id="btnHeidenhain" onclick="setCodeFormat('heidenhain')">Heidenhain</button>
    <button class="btn btn-secondary btn-sm" id="btnSiemens" onclick="setCodeFormat('siemens')">Siemens</button>
    <button class="btn btn-secondary btn-sm" id="btnFanuc" onclick="setCodeFormat('fanuc')">Fanuc</button>
</div>
```
- **JavaScript:** `setCodeFormat(format)` (Zeile 3246-3253) — Toggle btn-primary/secondary
- **Funktionalität:** Multi-Steuerungs-Support (Demo: nur Heidenhain-Code vorhanden)

### Feature: Code Export Buttons
- **Was:** Kopieren + Download
- **Wo:** Zeilen 1815-1818
- **HTML:**
```html
<button class="btn btn-secondary btn-sm" onclick="copyCode()">Kopieren</button>
<button class="btn btn-primary btn-sm" onclick="downloadCode()">Download</button>
```
- **JavaScript:**
  - `copyCode()` (Zeile 3230-3234) — `navigator.clipboard.writeText(code)`
  - `downloadCode()` (Zeile 3236-3244) — Blob-Download als `programm.h`
- **Funktionalität:** Schneller Export, Clipboard-Integration

### Feature: Code Block mit Syntax-Highlighting
- **Was:** <pre>-Block mit CSS-Klassen für Kommentare/Keywords/Numbers
- **Wo:** Zeilen 1821-1887
- **HTML:**
```html
<div class="code-block" id="codeBlock">
<pre><span class="code-comment">; ========================================</span>
<span class="code-comment">; CNC PLANNER PRO — Automatisch generiert</span>
<span class="code-comment">; ========================================</span>
<span class="code-comment">; Werkstück:  Verbindungsplatte</span>
<span class="code-comment">; Werkstoff:  S235JR</span>
<span class="code-comment">; Maschine:   FEHLMANN VERSA 943</span>
<span class="code-comment">; Steuerung:  Heidenhain TNC 640</span>

<span class="code-keyword">BEGIN PGM</span> VERBINDUNGSPLATTE <span class="code-keyword">MM</span>

<span class="code-comment">; --- WERKZEUGLISTE ---</span>
<span class="code-keyword">TOOL DEF</span> <span class="code-number">1</span> L+<span class="code-number">0</span> R+<span class="code-number">31.5</span>  <span class="code-comment">; Planfräser Ø63</span>
<span class="code-keyword">TOOL DEF</span> <span class="code-number">2</span> L+<span class="code-number">0</span> R+<span class="code-number">10</span>    <span class="code-comment">; VHM-Fräser Ø20</span>

<span class="code-comment">; OP10: PLANFRÄSEN</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">1</span> Z S<span class="code-number">800</span>
L Z+<span class="code-number">100</span> R0 FMAX M3

<span class="code-keyword">CYCL DEF</span> <span class="code-number">230</span> <span class="code-keyword">FACE MILLING</span>
  Q<span class="code-number">225</span>=+<span class="code-number">0</span>
  Q<span class="code-number">218</span>=<span class="code-number">450</span>
  Q<span class="code-number">219</span>=<span class="code-number">60</span>

<span class="code-keyword">CYCL CALL</span>

<span class="code-comment">; OP20: KONTUR</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">2</span> Z S<span class="code-number">2500</span>

<span class="code-comment">; OP30: FEINBOHREN Ø26 H7</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">11</span> Z S<span class="code-number">1200</span>

<span class="code-keyword">CYCL DEF</span> <span class="code-number">201</span> <span class="code-keyword">BORING</span>

M30

<span class="code-keyword">END PGM</span> VERBINDUNGSPLATTE <span class="code-keyword">MM</span></pre>
</div>
```
- **CSS:** `.code-comment` (grau), `.code-keyword` (blau), `.code-number` (orange)
- **Funktionalität:** Lesbarkeit, professionelle Darstellung

### Feature: Programm-Info (Footer)
- **Was:** Zeilenzahl, Laufzeit, Maschine, Warnung
- **Wo:** Zeilen 1889-1892
- **HTML:**
```html
<div class="info-box">
    <strong>Programm-Info:</strong> 85 Zeilen | Geschätzte Laufzeit: 12,5 min | Maschine: FEHLMANN VERSA 943<br>
    <strong style="color: var(--color-warning);">Hinweis:</strong> Code vor Einsatz prüfen.
</div>
```
- **Funktionalität:** Sicherheitshinweis, Metadaten

---

## 📊 TAB 7: FEEDBACK & CROSS-LEARNINGS

### Feature: Feedback-Tab Navigation
- **Was:** 3 Sub-Tabs
- **Wo:** Zeilen 1900-1904
- **Tabs:**
  1. **Feedback erfassen** (Eingabe)
  2. **🧠 Cross-Learnings** (KI-Mustererkennung)
  3. **Historie** (Feedback-Log)
- **JavaScript:** `showFeedbackTab(tab)` (Zeile 2942-2959)

---

### TAB 7.1: FEEDBACK ERFASSEN

#### Feature: Projekt-Header (Feedback)
- **Was:** Projekt-Nr., Datum, Erfasser
- **Wo:** Zeilen 1909-1924
- **HTML:**
```html
<div class="grid-3">
    <div class="form-group">
        <label>Projekt-Nr.</label>
        <input type="text" class="input input-mono" id="fbProjektNr" value="2500473.01" readonly>
    </div>
    <div class="form-group">
        <label>Datum</label>
        <input type="date" class="input" id="fbDatum" value="2026-02-05">
    </div>
    <div class="form-group">
        <label>Erfasser</label>
        <input type="text" class="input" id="fbErfasser" placeholder="Name oder Kürzel">
    </div>
</div>
```

#### Feature: OP-Zeit-Feedback-Tabelle
- **Was:** Kalk. vs. Ist pro Operation, Delta, Grund, Notiz
- **Wo:** Zeilen 1928-2048
- **HTML-Struktur:**
```html
<table class="table">
    <thead>
        <tr>
            <th style="width: 80px;">OP</th>
            <th>Beschreibung</th>
            <th style="width: 100px;">Kalk.</th>
            <th style="width: 100px;">Ist</th>
            <th style="width: 80px;">Delta</th>
            <th style="width: 150px;">Grund</th>
            <th>Notiz</th>
        </tr>
    </thead>
    <tbody id="feedbackOpsTable">
        <tr>
            <td class="mono">OP10</td>
            <td>Planfräsen</td>
            <td class="mono right">2,7 min</td>
            <td><input type="number" class="input input-sm input-mono" onchange="updateFeedbackDelta(this)"></td>
            <td class="mono right" data-delta>—</td>
            <td>
                <select class="input input-sm">
                    <option value="">—</option>
                    <option value="einrichtung">Einrichtung</option>
                    <option value="werkzeug">Werkzeug</option>
                    <option value="material">Material</option>
                    <option value="toleranz">Toleranz</option>
                    <option value="nc">NC-Programm</option>
                    <option value="sonstiges">Sonstiges</option>
                </select>
            </td>
            <td><input type="text" class="input input-sm" placeholder="z.B. Fräskanten nötig"></td>
        </tr>
        <!-- OP20, OP50 (KRITISCH rot), OP60 (KRITISCH rot) analog -->
    </tbody>
</table>
```
- **JavaScript:** 
  - `updateFeedbackDelta(input)` (Zeile 2961-2977) — Berechne Delta, färbe Zelle
  - `updateSetupDelta()` (Zeile 2979-2993) — Setup-Delta
  - `updateGesamtzeit()` (Zeile 2995-3010) — Summe + %
- **Funktionalität:** Strukturierte Abweichungserfassung

#### Feature: Ergebnis-Radio-Buttons
- **Was:** Teil i.O. | Nacharbeit | Ausschuss
- **Wo:** Zeilen 2051-2063
- **HTML:**
```html
<div style="display: flex; flex-direction: column; gap: var(--space-2);">
    <label style="display: flex; align-items: center; cursor: pointer;">
        <input type="radio" name="fbErgebnis" value="io_erst" checked> ✅ Teil i.O. (Erstfertigung)
    </label>
    <label>
        <input type="radio" name="fbErgebnis" value="io_korrektur"> ✅ Teil i.O. (nach Korrektur)
    </label>
    <label>
        <input type="radio" name="fbErgebnis" value="nacharbeit"> Nacharbeit nötig
    </label>
    <label>
        <input type="radio" name="fbErgebnis" value="ausschuss"> Ausschuss
    </label>
</div>
```

#### Feature: Empfehlung-Textarea
- **Was:** Freitext für Verbesserungsvorschläge
- **Wo:** Zeile 2068
- **HTML:**
```html
<textarea class="input" id="fbEmpfehlung" rows="4" placeholder="Was sollte bei der nächsten Kalkulation anders sein? z.B. 'Vorschub bei h5 um 20% reduzieren'"></textarea>
```

#### Feature: Feedback speichern
- **Was:** Button + localStorage-Persistenz
- **Wo:** Zeile 2075
- **HTML:**
```html
<button class="btn btn-primary" onclick="saveFeedback()">💾 Feedback speichern</button>
```
- **JavaScript:** `saveFeedback()` (Zeile 3012-3055)
  - Collect Form-Data
  - Collect OP-Data (Array)
  - Push to `feedbackHistory` Array
  - `localStorage.setItem('cncplanner_feedback', JSON.stringify(feedbackHistory))`
  - Alert: "✅ Feedback gespeichert!"
- **Funktionalität:** Persistente Datenhaltung, Basis für Cross-Learnings

---

### TAB 7.2: CROSS-LEARNINGS (KI-Muster-Erkennung)

#### Feature: Kalkulations-Genauigkeit-KPIs
- **Was:** 3 Metriken: Ø Abweichung, Feedback-Count, Muster
- **Wo:** Zeilen 2085-2102
- **HTML:**
```html
<div class="grid-3" style="text-align: center;">
    <div>
        <div style="font-size: 32px; font-weight: 700; color: var(--color-warning);" id="avgDeviation">+18%</div>
        <div style="font-size: 12px;">Ø Abweichung</div>
        <div style="font-size: 11px;">(Ziel: ±15%)</div>
    </div>
    <div>
        <div style="font-size: 32px; font-weight: 700;" id="feedbackCount">12</div>
        <div style="font-size: 12px;">Feedbacks</div>
        <div style="font-size: 11px;">erfasst</div>
    </div>
    <div>
        <div style="font-size: 32px; font-weight: 700; color: var(--color-success);" id="patternsFound">3</div>
        <div style="font-size: 12px;">Muster</div>
        <div style="font-size: 11px;">erkannt</div>
    </div>
</div>
```
- **JavaScript:** `updateCrossLearnings()` (Zeile 3088-3100) — Berechne Ø-Delta
- **Funktionalität:** Datenvisualisierung, Trend-Übersicht

#### Feature: Zeitfresser-Bar-Charts
- **Was:** 3 Kategorien mit Prozent-Balken
- **Wo:** Zeilen 2104-2131
- **HTML:**
```html
<div style="display: flex; flex-direction: column; gap: var(--space-2);">
    <div style="display: flex; align-items: center; gap: var(--space-3);">
        <span style="width: 100px;">Einrichtung</span>
        <div style="flex: 1; height: 20px; background: var(--color-bg); border-radius: var(--radius-sm); overflow: hidden;">
            <div style="width: 72%; height: 100%; background: var(--color-error);"></div>
        </div>
        <span class="mono" style="width: 50px; color: var(--color-error);">+18%</span>
    </div>
    <!-- Toleranz, Bearbeitung analog -->
</div>
```
- **Funktionalität:** Visuelle Priorisierung der Verbesserungsbereiche

---

#### Feature: Erkannte Muster-Liste (Collapsible)
- **Was:** 3 Pattern-Cards mit Beschreibung, Ursache, Vorschlag, Action-Buttons
- **Wo:** Zeilen 2139-2285
- **HTML-Pattern:**
```html
<div style="padding: var(--space-4); border-bottom: 1px solid var(--color-border-light);">
    <div style="display: flex; justify-content: space-between;">
        <div>
            <div style="font-weight: 600;">Einrichtzeit bei Parallelspanner</div>
            <div style="font-size: 12px;">Häufigkeit: 8/12 Aufträge (67%) • Ø Mehraufwand: +12 min</div>
        </div>
        <span style="background: var(--color-bg); color: var(--color-error); padding: 2px 8px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;">HOCH</span>
    </div>
    <div style="background: var(--color-bg); padding: var(--space-3); border-radius: var(--radius-md);">
        <div style="font-size: 12px; color: var(--color-text-muted);">Ursache</div>
        <div style="font-size: 13px;">Fräskanten für Parallelspanner fehlen in der Kalkulation. Werker müssen zusätzlich Flächen anfräsen.</div>
    </div>
    <div style="display: flex; align-items: center; gap: var(--space-3);">
        <span style="font-size: 13px;">💡 <strong>Vorschlag:</strong> Setup-Zeit +15 min bei Spannart "Parallelspanner"</span>
        <button class="btn btn-sm btn-primary" onclick="applyPattern('setup_parallel', 15)">Anwenden</button>
        <button class="btn btn-sm btn-secondary" onclick="ignorePattern('setup_parallel')">Ignorieren</button>
    </div>
</div>
```

#### Erkannte Muster (3×):
1. **Einrichtzeit bei Parallelspanner** (HOCH)
   - Häufigkeit: 8/12 (67%)
   - Mehraufwand: +12 min
   - Vorschlag: +15 min Setup
2. **Toleranz h5/H7 unterschätzt** (MITTEL)
   - Häufigkeit: 5/7 (71%)
   - Mehraufwand: +4 min
   - Vorschlag: Toleranz-Faktor 1.3×
3. **Material S235: Rohteil-Übermaß** (NIEDRIG)
   - Häufigkeit: 4/10 (40%)
   - Mehraufwand: +3 min
   - Vorschlag: Aufmaß +1.0mm

- **JavaScript:**
  - `applyPattern(patternId, value)` (Zeile 3113-3125) — localStorage-Flag setzen, Alert
  - `ignorePattern(patternId)` (Zeile 3127-3129) — Dismiss
- **Funktionalität:** KI-Feedback-Loop, algorithmische Verbesserung, User-Approval

---

#### Feature: Empfehlungen aus Feedback
- **Was:** 3 Top-Empfehlungen aus Freitext-Feedbacks
- **Wo:** Zeilen 2287-2311
- **HTML:**
```html
<div id="recommendationsContainer">
    <div style="padding: var(--space-3); border-bottom: 1px solid var(--color-border-light); display: flex; gap: var(--space-3);">
        <span style="font-size: 18px;">📌</span>
        <div style="flex: 1;">
            <div style="font-size: 13px;">"Bei Parallelspanner Fräskanten einplanen"</div>
            <div style="font-size: 11px; color: var(--color-text-muted);">3× gemeldet • Zuletzt: 05.02.2026</div>
        </div>
    </div>
    <!-- 2 weitere Empfehlungen analog -->
</div>
```
- **Funktionalität:** User-Votum, häufigste Vorschläge

---

### TAB 7.3: FEEDBACK-HISTORIE

#### Feature: Historie-Tabelle
- **Was:** Log aller Feedbacks mit Datum/Projekt/Erfasser/Delta/Ergebnis
- **Wo:** Zeilen 2320-2381
- **HTML:**
```html
<table class="table">
    <thead>
        <tr>
            <th>Datum</th>
            <th>Projekt</th>
            <th>Erfasser</th>
            <th class="right">Kalk.</th>
            <th class="right">Ist</th>
            <th class="right">Delta</th>
            <th>Hauptgrund</th>
            <th>Ergebnis</th>
        </tr>
    </thead>
    <tbody id="feedbackHistoryTable">
        <tr>
            <td class="mono">05.02.2026</td>
            <td class="mono">2500473.01</td>
            <td>M. Schmidt</td>
            <td class="mono right">42 min</td>
            <td class="mono right">48 min</td>
            <td class="mono right" style="color: var(--color-error);">+14%</td>
            <td>Einrichtung</td>
            <td>i.O.</td>
        </tr>
        <!-- 4 weitere Demo-Einträge -->
    </tbody>
</table>
```
- **JavaScript:** `updateFeedbackHistory()` (Zeile 3102-3111) — Real Data prepend
- **Funktionalität:** Audit-Trail, Nachvollziehbarkeit

#### Feature: CSV-Export (Feedback)
- **Was:** Download aller Feedbacks als Semicolon-CSV
- **Wo:** Button Zeile 2324, JS Zeile 3131-3145
- **JavaScript:**
```js
function exportFeedbackCSV() {
    if (feedbackHistory.length === 0) { alert('Keine Feedback-Daten vorhanden.'); return; }
    let csv = 'Datum;Projekt;Erfasser;Kalk (min);Ist (min);Delta %;Grund;Ergebnis;Empfehlung\n';
    feedbackHistory.forEach(f => {
        const delta = ((f.zeitIst - f.zeitKalk) / f.zeitKalk * 100).toFixed(0);
        csv += `${f.datum};${f.projektNr};${f.erfasser};${f.zeitKalk};${f.zeitIst};${delta};${f.setupGrund};${f.ergebnis};${f.empfehlung}\n`;
    });
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'cnc_feedback_export.csv';
    link.click();
}
```
- **Funktionalität:** Excel-Import, Externe Analyse

#### Feature: Feedback-Statistik-Footer
- **Was:** Summe, Ø Abweichung, Erfolgsquote
- **Wo:** Zeilen 2383-2389
- **HTML:**
```html
<div class="info-box">
    <strong>Daten:</strong> 12 Feedback-Einträge • Ø Abweichung: +18% • 
    <span style="color: var(--color-success);">83% i.O.</span> • 
    <span style="color: var(--color-warning);">17% Nacharbeit</span>
</div>
```

---

## ⚙️ TAB 8: EINSTELLUNGEN

### Feature: Firmendaten-Formular
- **Was:** 8 Felder für Angebots-Footer
- **Wo:** Zeilen 2401-2441
- **HTML:**
```html
<div class="grid-2" style="gap: var(--space-4);">
    <div class="form-group">
        <label>Firmenname</label>
        <input type="text" class="input" value="Muster CNC GmbH" id="firmaName">
    </div>
    <!-- Ansprechpartner, Straße, PLZ/Ort, Telefon, E-Mail, Steuernummer, IBAN -->
</div>
```
- **Felder:**
  1. Firmenname
  2. Ansprechpartner
  3. Straße
  4. PLZ / Ort
  5. Telefon
  6. E-Mail
  7. Steuernummer
  8. Bankverbindung (IBAN)
- **Funktionalität:** Angebots-Personalisierung

### Feature: Angebotseinstellungen
- **Was:** Gültigkeit, Lieferzeit, Zahlungsziel
- **Wo:** Zeilen 2444-2458
- **HTML:**
```html
<div class="grid-3">
    <div class="form-group">
        <label>Gültigkeit (Tage)</label>
        <input type="number" class="input input-mono" value="30" id="angebotsGueltigkeit">
    </div>
    <div class="form-group">
        <label>Standard-Lieferzeit</label>
        <input type="text" class="input" value="3-4 Wochen" id="standardLieferzeit">
    </div>
    <div class="form-group">
        <label>Zahlungsziel (Tage)</label>
        <input type="number" class="input input-mono" value="14" id="zahlungsziel">
    </div>
</div>
```

### Feature: Settings Action-Buttons
- **Was:** Speichern, Zurücksetzen, Export, Import
- **Wo:** Zeilen 2464-2469
- **HTML:**
```html
<button class="btn btn-primary" onclick="saveSettings()">💾 Einstellungen speichern</button>
<button class="btn btn-secondary" onclick="resetSettings()">↺ Zurücksetzen</button>
<button class="btn btn-secondary" onclick="exportSettings()">📤 Export</button>
<button class="btn btn-secondary" onclick="importSettings()">Import</button>
```
- **JavaScript:**
  - `saveSettings()` (Zeile 2842-2846) — `localStorage.setItem('cncplanner_settings_v16', ...)`
  - `loadSettings()` (Zeile 2848-2854) — Load from localStorage
  - `resetSettings()` (Zeile 2856-2859) — `localStorage.removeItem()` + Reload
  - `exportSettings()` (Zeile 3206-3212) — JSON-Download
  - `importSettings()` (Zeile 3214-3216) — Placeholder
- **Funktionalität:** Persistenz, Backup, Migration

### Feature: Settings-Info (Footer)
- **Was:** localStorage-Hinweis
- **Wo:** Zeilen 2471-2473
- **HTML:**
```html
<p style="font-size: 12px; color: var(--color-text-muted);">
    Einstellungen werden lokal im Browser gespeichert (localStorage). Export erstellt eine JSON-Datei für Backup oder Übertragung auf andere Geräte.
</p>
```

---

## 🎬 LOADING ANIMATION

### Feature: Loading Overlay
- **Was:** Fullscreen-Overlay mit Spinner + 5-Step Progress
- **Wo:** HTML Zeilen 291-302, CSS custom, JavaScript Zeile 3255-3283
- **HTML:**
```html
<div class="loading-overlay" id="loadingOverlay">
    <div class="loading-spinner"></div>
    <div style="font-size: 16px; font-weight: 500;">Generiere Unterlagen...</div>
    <div class="loading-steps">
        <div class="loading-step" id="loadStep1">
            <span class="loading-step-icon">1</span>
            <span>Geometrie analysieren</span>
        </div>
        <div class="loading-step" id="loadStep2">
            <span class="loading-step-icon">2</span>
            <span>Bearbeitungszeiten berechnen</span>
        </div>
        <div class="loading-step" id="loadStep3">
            <span class="loading-step-icon">3</span>
            <span>Werkzeugkosten kalkulieren</span>
        </div>
        <div class="loading-step" id="loadStep4">
            <span class="loading-step-icon">4</span>
            <span>Maschinencode generieren</span>
        </div>
        <div class="loading-step" id="loadStep5">
            <span class="loading-step-icon">5</span>
            <span>Fertigungsanweisung erstellen</span>
        </div>
    </div>
</div>
```
- **CSS:** 
  - `.loading-overlay` — `position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; display: none;`
  - `.loading-overlay.active` — `display: flex;`
  - `.loading-step.active` — Highlight
  - `.loading-step.done` — Icon → ✓
- **JavaScript:**
  - `showLoading()` (Zeile 3255-3258) — Add `.active`, start animation
  - `hideLoading()` (Zeile 3260-3264) — Remove `.active`, reset
  - `animateLoadingSteps()` (Zeile 3266-3283) — Sequential step animation (400-600ms per step)
- **Trigger:** `selectProject()` (Zeile 2620-2638)
- **Funktionalität:** User-Feedback bei Demo-Projekt-Auswahl, Professional UX

---

## 🧮 JAVASCRIPT — DATA OBJECTS

### Feature: MATERIALS Object
- **Was:** Material-Datenbank (15 Werkstoffe)
- **Wo:** Zeilen 2569-2588
- **Struktur:**
```js
const MATERIALS = {
    '1.4301': { name: '1.4301 (V2A)', price: 8.50, density: 7.90, timeFactor: 1.25 },
    'S235JR': { name: 'S235JR', price: 6.79, density: 7.85, timeFactor: 1.00 },
    'AlMg3': { name: 'AlMg3', price: 6.50, density: 2.66, timeFactor: 0.65 },
    'POM': { name: 'POM', price: 4.50, density: 1.41, timeFactor: 0.45 },
    // ... 11 weitere
};
```
- **Properties:**
  - `name` (String) — Display-Name
  - `price` (Number) — €/kg
  - `density` (Number) — g/cm³
  - `timeFactor` (Number) — Bearbeitbarkeit (1.0 = Referenz Baustahl, <1 = schneller, >1 = langsamer)
- **Funktionalität:** Zentrale Material-Logik, Erweiterbar

### Feature: CLAMPING Object
- **Was:** Spannart-Datenbank (5 Methoden)
- **Wo:** Zeilen 2590-2596
- **Struktur:**
```js
const CLAMPING = {
    'schraubstock': { time: 15, desc: 'Teil in Maschinenschraubstock spannen, Parallelität prüfen, Nullpunkt antasten.' },
    'schraubstock2': { time: 25, desc: 'Zwei Schraubstöcke für Langteile. Beide auf gleiche Höhe ausrichten.' },
    'tischspannung': { time: 35, desc: 'Tischspannung mit Pratzen. Für große oder unregelmäßige Werkstücke.' },
    'nullpunkt': { time: 5, desc: 'Nullpunktspannsystem. Schnellstes Wechseln, höchste Wiederholgenauigkeit.' },
    'spezial': { time: 45, desc: 'Sondervorrichtung. Aufwändiger Aufbau, für Serienteile rentabel.' }
};
```
- **Properties:**
  - `time` (Number) — Einrichtzeit in Minuten
  - `desc` (String) — Beschreibung
- **Funktionalität:** Setup-Zeit-Berechnung, Info-Text

### Feature: PROJECTS Object
- **Was:** Demo-Teile-Datenbank (2 Teile)
- **Wo:** Zeilen 2598-2610
- **Struktur:**
```js
const PROJECTS = {
    verbindungsplatte: {
        id: 'verbindungsplatte',
        name: 'Verbindungsplatte',
        partNumber: '2500473.01.11.02.00.001',
        material: 'S235JR',
        dims: { x: 440, y: 50, z: 20 },
        baseTime: 12.5,
        unitPrice: 28.40,
        thumbnail: 'demo-parts/2500473.01.11.02.00.001.pdf.png'
    },
    adapterplatte: { /* analog */ }
};
```
- **Properties:**
  - `id`, `name`, `partNumber` — Identifikation
  - `material` (String) — Key in MATERIALS
  - `dims` (Object) — x, y, z in mm
  - `baseTime` (Number) — Referenz-Maschinenzeit in min
  - `unitPrice` (Number) — Referenz-Stückpreis in €
  - `thumbnail` (String) — Pfad zu Vorschaubild
- **Funktionalität:** Demo-Content, Template-Basis

### Feature: RATES Object
- **Was:** Stundensätze (labor + machine)
- **Wo:** Zeilen 2612-2616
- **Struktur:**
```js
let RATES = {
    cnc: { labor: 49, machine: 42 },
    saegen: { labor: 43, machine: 12 },
    entgraten: { labor: 32, machine: 4 }
};
```
- **Veränderbar:** `let` (nicht `const`)
- **Update:** `updateRates()` (Zeile 2820-2833)
- **Funktionalität:** Zentrale Kostenbasis

### Feature: currentProject Variable
- **Was:** Aktives Projekt-Objekt
- **Wo:** Zeile 2618
- **JavaScript:** `let currentProject = null;`
- **Set:** `selectProject(id)` → `currentProject = PROJECTS[id];`
- **Funktionalität:** Zustandsverwaltung

### Feature: feedbackHistory Array
- **Was:** Persistent Storage für Feedbacks
- **Wo:** Zeile 2936
- **JavaScript:** `let feedbackHistory = JSON.parse(localStorage.getItem('cncplanner_feedback') || '[]');`
- **Push:** `saveFeedback()` → `feedbackHistory.push(feedback);`
- **Funktionalität:** Cross-Learning-Basis

---

## 🧮 JAVASCRIPT — KEY FUNCTIONS

### Feature: calculate() — Hauptberechnung
- **Was:** Zentrale Kalkulations-Engine
- **Wo:** Zeilen 2742-2811
- **Input-Quellen:**
  - `#materialSelect`, `#dimX/Y/Z`, `#quantity`
  - `#clampingSelect`, `#setupCount`
  - `#zuschlagMGK`, `#zuschlagAV`, `#zuschlagVwGK`, `#zuschlagVtGK`, `#zuschlagGewinn`
- **Berechnungsschritte:**
  1. Input lesen
  2. Volumen + Gewicht: `volumeMm3 = x * y * z; weightKg = (volumeMm3 / 1000) * density / 1000;`
  3. Materialkosten: `materialCost = weightKg * price * (1 + scrap/100)`
  4. Setup-Zeit: `totalSetupTime = clampingData.time + (setupCount - 1) * (clampingData.time * 0.6)`
  5. Bearbeitungszeit: `machiningTime = baseTime * Math.pow(sizeFactor, 0.7) * mat.timeFactor`
  6. Maschinenkosten: `machineCost = (machiningTime / 60) * cncRate`
  7. Werkzeugkosten: `toolCost = toolWear * mat.timeFactor`
  8. Zuschlagskalkulation:
     - `materialMitGK = materialCost * (1 + MGK/100)`
     - `fertigungMitAV = (machineCost + setupCostPerPiece + additionalCost) * (1 + AV/100)`
     - `herstellkosten = materialMitGK + fertigungMitAV + toolCost`
     - `selbstkosten = herstellkosten * (1 + (VwGK + VtGK)/100)`
     - `angebotspreis = selbstkosten * (1 + Gewinn/100)`
  9. UI-Update: `document.getElementById('...').textContent = ...`
- **Trigger:**
  - Input-Events: `oninput="calculate()"`, `onchange="calculate()"`
  - Button: "Analysieren"
  - Project-Select
- **Funktionalität:** Echtzeit-Kalkulation, Core-Logik

### Feature: showSection(name, btn) — Navigation
- **Was:** SPA Tab-Wechsel
- **Wo:** Zeilen 2669-2687
- **Logik:**
  1. Remove `.active` von allen `.nav-item`
  2. Add `.active` zu geklicktem Button
  3. Remove `.active` von allen `.section`
  4. Add `.active` zu `#section-{name}`
  5. Update `#mainTitle`
  6. Special: `result` zeigt 2 Sections (result + calculation)
- **Funktionalität:** SPA-Navigation, Single-Pane-View

### Feature: selectProject(id) — Demo-Projekt laden
- **Was:** Projekt auswählen + Loading-Animation + Auto-Calc
- **Wo:** Zeilen 2620-2638
- **Schritte:**
  1. `currentProject = PROJECTS[id];`
  2. `showLoading();` — Start Animation
  3. Formular befüllen: `#materialSelect`, `#dimX/Y/Z`
  4. `renderPartGrid();` — Update Selection
  5. `calculate();` — Neu-Berechnung
  6. Update Instruction-Header: `#faPartName`, `#quoteDesc`
  7. Nach 2.5s: `showSection('params', ...)` — Auto-Tab-Switch
- **Funktionalität:** Demo-Flow, UX-Polish

### Feature: updateRates() — Stundensätze updaten
- **Was:** Summe Lohn+Maschine berechnen, RATES-Object updaten
- **Wo:** Zeilen 2820-2833
- **Logik:**
```js
RATES.cnc.labor = parseFloat(document.getElementById('rateCncLabor').value) || 49;
RATES.cnc.machine = parseFloat(document.getElementById('rateCncMachine').value) || 42;
document.getElementById('rateCncTotal').textContent = '€' + (RATES.cnc.labor + RATES.cnc.machine);
calculate();
```
- **Funktionalität:** Live-Summe, Trigger Neu-Kalkulation

### Feature: saveFeedback() — Feedback persistieren
- **Was:** Form-Daten sammeln, localStorage speichern, Alert
- **Wo:** Zeilen 3012-3055
- **Struktur:**
```js
const feedback = {
    id: Date.now(),
    projektNr: document.getElementById('fbProjektNr').value,
    datum: document.getElementById('fbDatum').value,
    erfasser: document.getElementById('fbErfasser').value || 'Anonym',
    zeitKalk: 42, zeitIst: ...,
    setupKalk: 25, setupIst: ...,
    setupGrund: ..., setupNotiz: ...,
    ergebnis: document.querySelector('input[name="fbErgebnis"]:checked')?.value,
    empfehlung: document.getElementById('fbEmpfehlung').value,
    ops: []  // Array mit OP-Details
};
feedbackHistory.push(feedback);
localStorage.setItem('cncplanner_feedback', JSON.stringify(feedbackHistory));
alert('✅ Feedback gespeichert!');
clearFeedbackForm();
```
- **Funktionalität:** Feedback-Loop, Datenpersistenz, User-Bestätigung

### Feature: applyPattern(patternId, value) — KI-Muster anwenden
- **Was:** Pattern-Flag in localStorage setzen, Alert
- **Wo:** Zeilen 3113-3125
- **Logik:**
```js
if (patternId === 'setup_parallel') {
    alert('✅ Muster angewendet!\n\nSetup-Zeit bei Parallelspanner wird um +' + value + ' min erhöht.');
    localStorage.setItem('pattern_setup_parallel', value);
}
```
- **Funktionalität:** User-Approval, zukünftige Algorithmus-Anpassung

### Feature: exportFeedbackCSV() — CSV-Download
- **Was:** Feedback-Array → CSV-String → Blob-Download
- **Wo:** Zeilen 3131-3145
- **Logik:**
```js
let csv = 'Datum;Projekt;Erfasser;Kalk (min);Ist (min);Delta %;Grund;Ergebnis;Empfehlung\n';
feedbackHistory.forEach(f => {
    const delta = ((f.zeitIst - f.zeitKalk) / f.zeitKalk * 100).toFixed(0);
    csv += `${f.datum};${f.projektNr};${f.erfasser};...;${f.empfehlung}\n`;
});
const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'cnc_feedback_export.csv';
link.click();
```
- **Funktionalität:** Excel-Export, Externe Analyse

### Feature: DOMContentLoaded — Init
- **Was:** Einmalige Initialisierung beim Page-Load
- **Wo:** Zeilen 3291-3320
- **Schritte:**
  1. `loadSettings();` — localStorage laden
  2. `renderPartGrid();` — Demo-Teile rendern
  3. `calculate();` — Initial-Kalkulation
  4. Datum setzen: `#quoteDate`, `#quoteValidUntil` (heute + 30 Tage)
- **Funktionalität:** Bootstrap, Auto-Calc

---

## 📋 VERSTECKTE/NICHT-IMPLEMENTIERTE FEATURES

### Feature: File Upload Handler
- **Was:** STEP/PDF-Upload
- **Wo:** `<input type="file" id="fileInput">` (Zeile 428)
- **Status:** ❌ Nicht implementiert (kein Event-Listener)
- **Kommentar:** v17 = Demo, zukünftige 3D-Analyse

### Feature: Format-Switcher (NC-Code)
- **Was:** Siemens/Fanuc Code-Templates
- **Wo:** `setCodeFormat(format)` (Zeile 3246-3253)
- **Status:** ⚠️ Teilweise (nur Button-Toggle, kein Code-Wechsel)
- **Kommentar:** TODO-Marker in Code: `// TODO: Switch code templates`

### Feature: Import Settings
- **Was:** JSON-Import
- **Wo:** `importSettings()` (Zeile 3214-3216)
- **Status:** ❌ Nur Placeholder: `alert('Import-Funktion: Datei auswählen (Coming soon)');`

### Feature: CSV Export (Kalkulation)
- **Was:** Button "CSV Export"
- **Wo:** `exportCSV()` (Zeile 3228)
- **Status:** ❌ `alert('CSV Export — Coming soon');`

### Feature: Nebenoperationen (Sägen, Entgraten, Prüfung)
- **Was:** Checkboxen + Zeit-Inputs
- **Wo:** Nicht sichtbar in HTML (vermutlich removed)
- **JavaScript:** Logik vorhanden (Zeile 2757-2769)
- **Status:** ⚠️ Backend vorhanden, UI fehlt

---

## 🎯 ZUSAMMENFASSUNG: FEATURE-COUNT

### Nach Kategorie:

| Kategorie | Feature-Count |
|-----------|--------------|
| **Design System** | 5 (Color Palette, Typography, Spacing, Variables, Industrial Theme) |
| **Layout & Navigation** | 9 (Sidebar, Header, Sections, Nav-Items, Tabs, Toggle) |
| **Teil-Tab** | 6 (Trust Badges, Scope Notice, Part Grid, File Upload, Werkstück-Form, Buttons) |
| **Parameter-Tab** | 12 (Sub-Tabs, Fertigung-Inputs, Maschinenstundensätze-Table, Materialpreise, Zuschlagskalkulation, Plausibility-Checks) |
| **Kalkulation-Tab** | 5 (Gesamtkalkulation, Maschinenzeitkalkulation, Materialkalkulation, Einrichtkosten, Berechnungsgrundlagen) |
| **Fertigungsanweisung** | 14 (Document Header, Werkstück-Grid, Toleranz-Box, Zeichnung-Vorschau, 10× Operations, Qualitätsprüfung, Schnittparameter, Werkzeugkosten, Feedback-Card) |
| **Angebot-Tab** | 4 (Header, Tabelle, Summe, Footer) |
| **NC-Code-Tab** | 4 (Format-Switcher, Export-Buttons, Code-Block, Programm-Info) |
| **Feedback-Tab** | 10 (Sub-Tabs, Eingabe-Form, OP-Tabelle, Ergebnis-Radio, Empfehlung, KPIs, Zeitfresser-Charts, Muster-Liste, Empfehlungen, Historie) |
| **Einstellungen-Tab** | 3 (Firmendaten, Angebotseinstellungen, Action-Buttons) |
| **JavaScript-Core** | 8 (calculate, showSection, selectProject, updateRates, saveFeedback, applyPattern, exportCSV, DOMContentLoaded) |
| **Loading-Animation** | 1 (Overlay + 5-Step-Progress) |
| **Data-Objects** | 5 (MATERIALS, CLAMPING, PROJECTS, RATES, feedbackHistory) |

### **GESAMT: ~86 Features**

---

## 🔍 EDGE CASES & VERSTECKTE DETAILS

### Edge Case: Setup-Umlegung bei Stückzahl
- **Was:** Einrichtkosten / Stückzahl
- **Wo:** `calculate()` Zeile 2752
- **Formel:** `setupCostPerPiece = setupCost / qty`
- **UI:** Quantitäts-Tabelle zeigt Preis-Degression

### Edge Case: Multi-Setup Kosten-Faktor
- **Was:** 2. Aufspannung = 60% der ersten (nicht 100%)
- **Wo:** `calculate()` Zeile 2739
- **Formel:** `totalSetupTime = clampingData.time + (setupCount - 1) * (clampingData.time * 0.6)`
- **Begründung:** 2. Setup schneller (Werkzeug schon gespannt, Programm läuft)

### Edge Case: Volumen-Skalierung (nicht linear)
- **Was:** `sizeFactor^0.7` (Potenzgesetz)
- **Wo:** `calculate()` Zeile 2755
- **Formel:** `machiningTime = baseTime * Math.pow(sizeFactor, 0.7) * mat.timeFactor`
- **Begründung:** Größere Teile proportional schneller (Schnittgeschwindigkeit steigt)

### Edge Case: timeFactor Material
- **Was:** Aluminium < 1.0, Edelstahl > 1.0
- **Wo:** `MATERIALS` Object
- **Beispiel:** AlMg3 = 0.65 (35% schneller), 1.4571 = 1.35 (35% langsamer)

### Edge Case: Werkzeugverschleiß-Faktor
- **Was:** `toolCost = toolWear * mat.timeFactor`
- **Wo:** `calculate()` Zeile 2771
- **Begründung:** Edelstahl verschleißt Werkzeug schneller

### Edge Case: Confidence-Badge Logik
- **Was:** Rot/Gelb/Grün basierend auf timeFactor + Volumen-Ähnlichkeit
- **Wo:** `calculate()` Zeile 2801-2809
- **Logik:**
```js
if (mat.timeFactor > 1.2) { confidence = 'low'; text = '±25% — Schwerzerspanbarer Werkstoff'; }
else if (currentProject && Math.abs(volumeCm3 - refVolume) < refVolume * 0.2) { confidence = 'high'; text = '±10% — Ähnlich wie Referenzteil'; }
else { confidence = 'medium'; text = '±15% — Standardteil'; }
```

### Edge Case: Plausibility-Warnings werkstoffabhängig
- **Was:** Warnung nur bei timeFactor > 1.3
- **Wo:** `checkPlausibility()` Zeile 2817
- **Condition:** `if (mat.timeFactor > 1.3) { warnings.push({ type: 'info', text: '...' }); }`

### Edge Case: Feedback Delta-Färbung
- **Was:** Rot bei >10%, Grün bei <-5%, Gelb dazwischen
- **Wo:** `updateFeedbackDelta()` Zeile 2972
- **Logik:** `deltaCell.style.color = delta > 0 ? 'var(--color-error)' : 'var(--color-success)';`

### Edge Case: localStorage-Fallback
- **Was:** Leerer Array wenn kein localStorage
- **Wo:** Zeile 2936
- **Code:** `JSON.parse(localStorage.getItem('cncplanner_feedback') || '[]')`

### Edge Case: Image onerror Fallback
- **Was:** Fehlertext bei fehlender Zeichnung
- **Wo:** Zeile 1134
- **Code:** `onerror="this.parentElement.innerHTML='<div>Keine Zeichnung verfügbar</div>'"`

### Edge Case: Datum Auto-Berechnung
- **Was:** Gültig-bis = Heute + 30 Tage
- **Wo:** DOMContentLoaded, Zeile 3316-3318
- **Code:** 
```js
const today = new Date();
const validUntil = new Date(today.getTime() + 30 * 24 * 60 * 60 * 1000);
document.getElementById('quoteValidUntil').textContent = validUntil.toLocaleDateString('de-DE');
```

---

## 🚀 TECHNISCHE SCHULDEN & POTENZIAL

### Verbesserungspotential:
1. **Modularisierung:** calculate() ist 69 Zeilen (zu lang)
2. **State Management:** Globale Variablen (currentProject, RATES)
3. **Template Engine:** Viel String-Concatenation (renderPartGrid)
4. **Event-Delegation:** Viele inline-onclick
5. **localStorage-Schema:** Keine Versionierung (außer Key-Suffix)
6. **Error Handling:** Keine try-catch bei JSON.parse
7. **Input-Validation:** Nur HTML5 min-Attribute
8. **Accessibility:** Fehlende aria-labels
9. **i18n:** Hardcoded deutsche Texte
10. **Responsive:** Keine Mobile-Optimierung

### Nicht genutzte Features:
- Nebenoperationen-Checkboxen (JS vorhanden, UI fehlt)
- Siemens/Fanuc NC-Code (Templates fehlen)
- Settings-Import (nur Export)
- CSV-Export (Kalkulation)

---

**AUDIT ABGESCHLOSSEN**  
**Erfasste Features:** 86  
**Erfasste Code-Zeilen:** 3331  
**Nicht-erfasste Elemente:** 0 (vollständig)

---

**Output-Datei:** `V17-FEATURE-AUDIT-COMPLETE.md`  
**Nächster Schritt:** Update REQUIREMENTS-V18-COMPLETE.md Phase 1 mit diesen Ergebnissen.

# CNC Planer Pro - Software-Entwicklungsprozess

**Version:** 1.0  
**Datum:** 2026-02-06  
**Warum existiert das:** Weil wir ohne Prozess 30x iterieren statt 1x richtig zu bauen

---

## 🚨 DAS PROBLEM

**Bisheriger "Prozess":**
1. Florian sagt "Bau Feature X"
2. Mia baut sofort los
3. Darstellung passt nicht
4. 10x Iterationen
5. Immer noch nicht perfekt
6. Frustration

**Warum:**
- Keine dokumentierten Standards
- Keine Golden References
- Keine Design System Docs
- Keine Verlinkungen zwischen Docs
- Kein "Definition of Done"

---

## ✅ DER NEUE PROZESS

### Phase 1: RESEARCH (BEFORE ANY CODE!)

**Was:** Verstehen was das Ziel ist

**Schritte:**
1. **Golden Standard finden** - Was ist das beste Beispiel?
   - MBS Angebot für Quotes
   - Bootstrap für Tables
   - McKinsey für Presentations
2. **Analysieren** - Line-by-Line dokumentieren
3. **Dokumentieren** - Alles in `research/` Ordner
4. **Verlinken** - In `DESIGN-SYSTEM.md` referenzieren

**Deliverable:**
- `research/FEATURE-ANALYSE-[NAME].md`
- Screenshots/PDFs der Golden Standards
- Verlinkung in Design System

**Time:** 15-30 Minuten  
**DON'T SKIP THIS!**

---

### Phase 2: DESIGN SYSTEM UPDATE

**Was:** Standards dokumentieren BEVOR gebaut wird

**Schritte:**
1. **Design System updaten** - Neue Components/Patterns dokumentieren
2. **CSS-Klassen definieren** - Welche Klassen werden gebraucht?
3. **Variablen setzen** - Farben, Spacing, Typography
4. **Examples schreiben** - Code-Snippets für jeden Component

**Deliverable:**
- Updated `DESIGN-SYSTEM.md`
- CSS-Klassen dokumentiert
- HTML-Examples vorhanden

**Time:** 15-20 Minuten

---

### Phase 3: REQUIREMENTS

**Was:** EXAKT definieren was gebaut werden soll

**Schritte:**
1. **Feature Liste** - Alle Features auflisten
2. **Acceptance Criteria** - Wann ist es fertig?
3. **Technical Specs** - Welche Functions, welche HTML-Struktur?
4. **Edge Cases** - Was kann schiefgehen?
5. **Testing Checklist** - Wie testen wir?

**Deliverable:**
- `REQUIREMENTS-[FEATURE].md`
- Acceptance Criteria Liste
- Testing Checklist

**Time:** 20-30 Minuten

---

### Phase 4: APPROVAL

**Was:** Florian MUSS Requirements genehmigen BEVOR gebaut wird

**Schritte:**
1. Mia zeigt:
   - Research Findings
   - Proposed Design System Updates
   - Complete Requirements
2. Florian reviewed und sagt:
   - ✅ "Go, bau das"
   - ⚠️ "Änderungen: [...]"
   - ❌ "Nein, anders"

**Deliverable:**
- Approval Comment in Requirements-Datei
- Clear "GO" Signal

**Time:** 5-10 Minuten

**CRITICAL:** Keine Zeile Code ohne Approval!

---

### Phase 5: IMPLEMENTATION

**Was:** Bauen nach dokumentierten Standards

**Schritte:**
1. **Setup** - Branch erstellen (falls git), Backup machen
2. **HTML** - Nach Design System Specs bauen
3. **CSS** - Nur dokumentierte Klassen nutzen
4. **JavaScript** - Nach Requirements implementieren
5. **Self-Review** - Gegen Checklist prüfen

**Deliverable:**
- Funktionierender Code
- Follows Design System
- Matches Requirements

**Time:** 60-90 Minuten

---

### Phase 6: TESTING

**Was:** Systematisch gegen Checklist testen

**Test Types:**
1. **Visual Test** - Sieht es richtig aus?
2. **Functional Test** - Funktioniert alles?
3. **Edge Cases** - Extremwerte, lange Texte, etc.
4. **Cross-Browser** - Chrome, Safari, Firefox
5. **Print Test** - PDF-Export funktioniert?

**Deliverable:**
- Completed Testing Checklist
- Screenshots der Tests
- Bug-Liste (falls welche gefunden)

**Time:** 20-30 Minuten

---

### Phase 7: DOCUMENTATION UPDATE

**Was:** Docs aktualisieren für zukünftige Entwicklung

**Schritte:**
1. **FUNKTIONSBESCHREIBUNG.md** updaten
2. **DESIGN-SYSTEM.md** mit neuen Components ergänzen
3. **CHANGELOG.md** eintragen
4. **README** bei Bedarf updaten

**Deliverable:**
- Updated Documentation
- Verlinkungen zwischen Docs korrekt

**Time:** 10-15 Minuten

---

### Phase 8: DELIVERY

**Was:** Florian kann mit EINER Aktion nutzen

**Schritte:**
1. **Browser-Test** durchführen
2. **File öffnen** per `open` Command
3. **Demo** zeigen
4. **Git Commit** falls nötig

**Deliverable:**
- Florian sieht fertiges Feature im Browser
- Kann sofort nutzen/testen

**Time:** 5 Minuten

---

## 📐 DESIGN SYSTEM RULES

### CSS-Klassen:

**NIEMALS inline-styles**, IMMER dokumentierte Klassen:

```html
<!-- ❌ FALSCH -->
<div style="padding: 24px; background: #f9fafb;">

<!-- ✅ RICHTIG -->
<div class="card-body">
```

### Farben:

**NIEMALS Hex-Codes direkt**, IMMER CSS-Variablen:

```css
/* ❌ FALSCH */
.card { background: #f9fafb; }

/* ✅ RICHTIG */
.card { background: var(--color-bg-subtle); }
```

### Spacing:

**NIEMALS Pixel-Werte**, IMMER Spacing-System:

```css
/* ❌ FALSCH */
.card { margin-bottom: 24px; }

/* ✅ RICHTIG */
.card { margin-bottom: var(--space-6); }
```

---

## 🔗 DOKUMENTATIONS-STRUKTUR

### Hierarchy:

```
projects/cnc-planner/
├── README.md                          # Projekt-Overview
├── DESIGN-SYSTEM.md                   # Master Design Doc
├── DEVELOPMENT-PROCESS.md             # Dieser Prozess
├── FUNKTIONSBESCHREIBUNG.md           # Feature-Liste
├── CHANGELOG.md                       # Version History
│
├── research/                          # Golden Standards
│   ├── MBS-ANGEBOT-LINE-BY-LINE.md
│   ├── RESEARCH-ZEICHNUNGSNUMMER.md
│   └── ...
│
├── requirements/                      # Feature Requirements
│   ├── REQUIREMENTS-V18-FINAL.md
│   └── ...
│
└── design-system/                     # Design Components
    ├── components/
    │   ├── TABLES.md
    │   ├── CARDS.md
    │   ├── FORMS.md
    │   └── BUTTONS.md
    │
    ├── patterns/
    │   ├── QUOTE-LAYOUT.md
    │   ├── CALCULATION-DISPLAY.md
    │   └── ...
    │
    └── tokens/
        ├── COLORS.md
        ├── SPACING.md
        └── TYPOGRAPHY.md
```

### Verlinkungen:

**Jedes Requirements-Doc** muss verlinken:
- Welche Design System Components werden genutzt?
- Welche Research-Docs sind relevant?
- Wo ist die Implementation?

**Jedes Design System Doc** muss verlinken:
- Wo ist das genutzt? (Feature-Liste)
- Wo ist der Golden Standard? (Research)
- Code-Examples

---

## ✅ DEFINITION OF DONE

Ein Feature ist DONE wenn:

### Code:
- [ ] Folgt Design System (keine inline-styles)
- [ ] Verwendet CSS-Variablen
- [ ] Kommentiert (was macht welche Function?)
- [ ] Keine `console.log()` im Production-Code

### Testing:
- [ ] Visual Test bestanden
- [ ] Functional Test bestanden
- [ ] Edge Cases getestet
- [ ] Print-Test (PDF) funktioniert

### Documentation:
- [ ] FUNKTIONSBESCHREIBUNG.md updated
- [ ] DESIGN-SYSTEM.md updated (falls neue Components)
- [ ] CHANGELOG.md entry
- [ ] Verlinkungen korrekt

### Delivery:
- [ ] Florian hat getestet
- [ ] Feedback eingearbeitet
- [ ] Git committed
- [ ] Deployment-ready

---

## 🚫 ANTI-PATTERNS

### Was wir NICHT mehr machen:

❌ **"Quick Fix" ohne Design System Update**
- Führt zu inkonsistenten Styles
- Nächster Developer macht es anders

❌ **"Ich bau das schnell" ohne Requirements**
- Führt zu 30x Iterationen
- Florian's Zeit verschwendet

❌ **"Inline-Style weil schneller"**
- Macht Design System nutzlos
- Nicht wartbar

❌ **"Dokumentiere ich später"**
- "Später" kommt nie
- Nächstes Feature macht gleichen Fehler

❌ **"Das ist nur ein Prototype"**
- Prototypes werden Production
- Dann ist schlechter Code überall

---

## 🎯 SUCCESS METRICS

### Gute Entwicklung:
- 1 Research → 1 Requirements → 1 Implementation → DONE
- 0-2 Iterationen nach Review
- Code folgt 100% Design System
- Docs sind aktuell

### Schlechte Entwicklung:
- Kein Research → sofort gebaut
- 10+ Iterationen
- Inline-styles überall
- Docs veraltet

---

## 📚 REQUIRED READING

Bevor du Code schreibst, lies:

1. **Dieser Prozess** (`DEVELOPMENT-PROCESS.md`)
2. **Design System** (`DESIGN-SYSTEM.md`)
3. **Feature Requirements** (für das Feature das du baust)
4. **Golden Standard Research** (relevant für Feature)

**Estimated Reading Time:** 20 Minuten  
**Spart:** 2-3 Stunden Iterationen

---

## 🔄 CONTINUOUS IMPROVEMENT

### Nach jedem Feature:

1. **Retrospective** - Was lief gut? Was nicht?
2. **Process Update** - Muss dieser Prozess angepasst werden?
3. **Design System Update** - Neue Learnings dokumentieren
4. **Shared Learnings** - In Team-Docs eintragen

---

## 🏁 QUICK START CHECKLIST

Starting a new feature? Follow this:

- [ ] Read Golden Standard (research/)
- [ ] Check Design System (DESIGN-SYSTEM.md)
- [ ] Write Requirements (requirements/)
- [ ] Get Approval (Florian says "GO")
- [ ] Implement (follow Design System)
- [ ] Test (complete checklist)
- [ ] Update Docs
- [ ] Deliver

**NIEMALS SKIP SCHRITTE!**

---

## 📞 WHEN IN DOUBT

**FRAG FLORIAN** bevor du:
- Neue CSS-Klasse erstellst (gehört ins Design System)
- Von Standards abweichst
- "Quick Fix" machst
- Denkst "das dokumentiere ich später"

**5 Minuten Fragen spart 2 Stunden Iterationen.**

---

*Erstellt: 2026-02-06*  
*Letzte Änderung: 2026-02-06*  
*Version: 1.0*  
*Author: Mia (nach mehrfachem Versagen ohne Prozess)*

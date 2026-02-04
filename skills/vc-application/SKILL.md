# VC Application Skill — CV & Cover Letter

*Validated rules from 6 research agents + industry best practices. Stand: 2026-02-04.*

---

## CV — Regeln für Florians VC-Bewerbung

### Design
- **Layout:** Single Column. IMMER. (Goldman/McKinsey/HBS Standard)
- **Font:** Helvetica Neue (bereits installed) oder Inter. Kein Times New Roman.
- **Name:** 22-24pt bold, Navy `#1B2A4A`
- **Section Headers:** 10-11pt, Bold, SMALL CAPS, Letter-Spacing +50, Navy
- **Body:** 10.5pt, `#2D3748` (nicht reines Schwarz)
- **Dates/Locations:** 9pt, `#718096` (gray), rechts-aligned
- **Margins:** 15-18mm (tight but nicht cramped)
- **Whitespace:** 40-50% der Seite
- **Farben:** Max 2 (Navy + Gray). Kein Blau-Highlight, kein Gradient.
- **Horizontale Linie:** 1.5-2pt unter Name. 0.4pt unter Section Headers.
- **KEINE:** Skill-Bars, Icons, Infografiken, QR-Codes, Fotos, Sidebar

### Inhalt — Was VCs in 6 Sekunden scannen
1. **Name + aktuelle Rolle** (Venture Fellow, Ex-CEO)
2. **Key Metrics** (€5.5M raised, 15+ Enterprise Kunden, <0.2% Hallucination)
3. **Firmen-Namen** (36ZERO Vision, BMW, Siemens, Bosch = social proof)
4. **Ausbildung** (TU München, TU Dresden = solide)

### Inhalt — Sektionen (Reihenfolge!)
1. **Header:** Name, Subtitle, Kontakt (Email, Phone, LinkedIn)
2. **Key Highlights Bar:** 3-4 Metriken in einer Box (dezent, lightgray bg)
3. **Experience:** Reverse chronologisch. Bullets = Ergebnis-orientiert (Zahlen!)
4. **Technical Expertise:** Grid, 4 Kategorien
5. **Education:** Kompakt, 2 Zeilen
6. **Additional:** Languages, Writing (Substack), Location

### Bullets — Formel
```
[Action Verb] + [Was] + [Quantifiziertes Ergebnis]
```
Beispiel: "Raised €5.5M+ across equity rounds; managed board and investor relations"
NICHT: "Responsible for fundraising activities"

### Was NICHT auf den CV
- Keine "Objective" Sektion
- Keine persönlichen Interessen außer wenn relevant (Physics = ok weil signalisiert Tiefe)
- Kein Geburtsdatum, kein Foto (US Standard)
- Keine Skills-Bewertung (3/5 Sterne etc.)
- Kein "References available upon request"

---

## Cover Letter — Regeln

### Format
- **Länge:** 250-400 Wörter, max 1 Seite, 3-4 Absätze
- **Cold Email:** Plain Text (kein PDF Attachment)
- **Formale Bewerbung:** Clean PDF, gleiches Design wie CV
- **Font:** Identisch mit CV (Helvetica Neue, gleiche Farben)

### Struktur: "Three WHYs"
```
Absatz 1: WHY YOU — Dein Unique Value (2-3 Sätze, Hook first)
Absatz 2: WHY VC — Warum Venture + was du mitbringst (Bullets ok)  
Absatz 3: WHY THIS FUND — Spezifisch über den Fund (Portfolio, Thesis)
Absatz 4: Close — 1 Satz, CTA
```

### Hook (Erster Satz)
NICHT: "I am writing to apply for the Associate position"
NICHT: "I'm passionate about venture capital"
JA: "As a former CEO who raised €5.5M and built AI products for BMW and Siemens, I bring [...]"
JA: "After 5 years building enterprise AI, I know what separates real technical moats from API wrappers."

### Differenzierung — Die 5 Waffen
1. **"Do the work before you're hired"** — Deal Memo, Investment Thesis, Sourcing beifügen
2. **Spezifisches Portfolio-Wissen** — "Your investment in [X] resonates because [genuine insight]"
3. **Operator-Framing** — "I've been on the founder side raising capital. I know what good looks like."
4. **European Deal Flow** — "My DACH network surfaces AI deals before they hit US radar"
5. **Technical Credibility** — "I can evaluate RAG architectures, inference costs, and data flywheels"

### Anti-Patterns (sofortige Ablehnung)
- "I'm passionate about venture capital" (jeder sagt das)
- Generisches Lob ("Your fund is amazing")
- Resume in Prosa-Form wiederholen
- Länger als 1 Seite
- Rechtschreibfehler (besonders Name des GPs falsch)
- "I would love the opportunity to..." (passiv, weak)

### Operator→VC Transition framen
- NICHT: "I failed as a founder and now want to try VC"
- JA: "5 years of building taught me pattern recognition that's hard to get from a spreadsheet"
- Lead mit Learnings, nicht Failures
- Technische Skills = Due Diligence Capability
- Founder-Erfahrung = Portfolio Support Asset

---

## Prozess: Fund-für-Fund

1. **Research** Fund (5 min): Portfolio, Thesis, GPs, Recent News
2. **Customize** Cover Letter: WHY THIS FUND Absatz anpassen
3. **Florian Review** (2 min): Check voice, accuracy
4. **Send** — Email oder Portal
5. **Track** im Dashboard
6. **Follow-up** nach 5 Tagen

---

## LaTeX-Spezifika

### CV Template
- `article` class (NICHT moderncv/awesome-cv — zu wenig Kontrolle)
- XeLaTeX + fontspec für Systemfonts
- `microtype` für professionelle Typografie
- `enumitem` für Bullet-Kontrolle
- `tikz` nur für Highlights-Bar (dezent)
- `needspace` für Seitenumbruch-Kontrolle

### Farben
```latex
\definecolor{navy}{HTML}{1B2A4A}
\definecolor{bodytext}{HTML}{2D3748}
\definecolor{subtle}{HTML}{718096}
\definecolor{accent}{HTML}{2563EB}  % nur für Links
\definecolor{lightbg}{HTML}{F7FAFC}  % Highlights-Bar
```

### Pre-Flight Checklist
- [ ] 1 Seite?
- [ ] Name + Kontakt prominent?
- [ ] Key Metrics sichtbar in 6 Sekunden?
- [ ] Jeder Bullet hat eine Zahl?
- [ ] Navy als einzige Akzentfarbe?
- [ ] Kein Skill-Bar, Icon, Foto?
- [ ] Cover Letter: <400 Wörter?
- [ ] Cover Letter: "Why This Fund" ist SPEZIFISCH?
- [ ] Cover Letter: Kein "I'm passionate about VC"?
- [ ] PDF: Druckt korrekt in Graustufen?
- [ ] Telefonnummer: +1 347 740 1465?

---

## Quellen
- GoingVC, Breaking Into VC Guides
- Nichole Wischoff (Wischoff Ventures): 500 applicants, 5% callback
- Amplify Partners: "Curiosity, Authenticity, Hustle, Humility"
- skills/cv-design/SKILL.md (28KB Design Research)
- research/vc-cover-letter-research-2025.md (25KB CL Research)
- Goldman/McKinsey/HBS Resume Standards

---

*Erstellt: 2026-02-04 19:25 · Basierend auf 6 Research-Agents*

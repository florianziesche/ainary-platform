# Research: Smart Logic für Execution Platform

*Research Date: 2026-02-18*
*Quellen: Eugene Yan (LLM Patterns), Vale.sh, Guardrails-AI, NeMo-Guardrails, Anthropic Constitutional AI, LLM-as-Judge Papers*

---

## 1. Pre-Flight Check — Von Keyword-Match zu echtem Linting

### Aktuell (schwach)
Keyword-Match: Sucht `wrong` String im Output. Findet "Great question" aber nicht "That's a wonderful question".

### State of the Art: 3 Schichten

**Schicht 1: Pattern Rules (Vale-Architektur)**
- Vale.sh: Prose-Linter wie Code-Linter. YAML-basierte Regeln mit Regex, Substitution, Existence checks.
- Jede Correction wird eine YAML-Rule: `extends: substitution`, `swap: {"wrong": "right"}`
- Severity-Level: suggestion, warning, error
- **Vorteil:** Deterministisch, schnell (<50ms), keine API-Kosten, offline-fähig
- **Implementierung:** Regex-Patterns statt String-Includes. Kategorie-spezifische Matcher.

**Schicht 2: Structural Validation (Guardrails-AI Pattern)**
- Guardrails-AI: Pydantic-style Validation auf LLM Output
- Validatoren: Länge, Vollständigkeit, URL-Validität, Code-Syntax, Semantic Similarity
- **Bei uns:** Output-Type-spezifische Validators:
  - Email: Hat Betreff? Hat Anrede? Hat Signatur? Länge 50-500 Wörter?
  - LinkedIn: Unter 3000 Zeichen? Kein "we" (Solo Founder)? Hat CTA?
  - Report: Quellen angegeben? Zahlen belegt?
- **Vorteil:** Strukturelle Fehler sofort erkannt, kein LLM nötig

**Schicht 3: LLM-as-Judge (für kritische Outputs)**
- LLM prüft Output gegen Correction-Regeln
- Prompt: "Prüfe diesen Text gegen folgende Regeln: [corrections]. Für jede Regel: pass/fail/warn mit Begründung."
- Nur bei REVIEW/CONFIRM Guardrail-Level (nicht bei AUTO)
- **Vorteil:** Fängt semantische Verstöße ("That's a wonderful question" = LLM-Phrase)
- **Nachteil:** Latenz (+2-3s), API-Kosten, nicht offline

### Implementierungsplan Pre-Flight
```
Output → Schicht 1 (Regex, <50ms) → Schicht 2 (Structural, <100ms) → [optional] Schicht 3 (LLM-Judge, 2-3s)
         Immer                       Immer                             Nur bei REVIEW/CONFIRM
```

---

## 2. Guardrails — Von If/Else zu Constitutional AI

### Aktuell (schwach)
Trust Score → if ≥60 AUTO, if ≥30 REVIEW, else CONFIRM. Alle drei zeigen nur einen Dialog.

### State of the Art: Graduated Autonomy

**Anthropic's Constitutional AI Prinzip:**
- Regeln (Constitution) definieren Verhalten
- AI prüft eigenen Output gegen Regeln (Self-Critique)
- Revision wenn Verstoß erkannt
- **Übertragung auf uns:** Corrections = unsere Constitution. Jeder Output wird vor Delivery gegen die Constitution geprüft.

**NeMo-Guardrails Pattern:**
- Input Rails: Prüfe User-Intent bevor Action ausgeführt wird
- Output Rails: Prüfe AI-Output bevor User es sieht
- Topical Rails: Halte Konversation im Topic-Scope

**Graduated Autonomy Modell:**
```
Score 0-29  → CONFIRM: Output wird NICHT angezeigt bis Pre-Flight bestanden
              User muss explizit "Trotzdem anzeigen" klicken
              Jede Aktion braucht Bestätigung

Score 30-59 → REVIEW: Output wird angezeigt MIT Pre-Flight Ergebnissen
              User sieht Pass/Warn/Fail Badges inline
              Aktionen brauchen 1-Klick Bestätigung

Score 60-79 → AUTO: Output wird direkt angezeigt
              Pre-Flight läuft im Hintergrund
              Aktionen werden sofort ausgeführt, Ergebnis gezeigt

Score 80+   → DELEGATED: Wie AUTO, aber auch Multi-Step möglich
              "Erstelle CV + schreibe Email + sende" als ein Workflow
              User wird nur informiert, nicht gefragt
```

### Trust Score Berechnung (Bayesian statt Linear)
```
Aktuell:  score += 2 (up), score -= 3 (down)  ← zu einfach
Besser:   Bayesian Average mit Decay

score = (C × m + Σ ratings) / (C + n)
- C = confidence parameter (10)
- m = prior (50 = neutral)
- n = total ratings
- ratings: +1 für up, -1 für down, gewichtet nach recency (Decay)

Decay: Ältere Ratings zählen weniger. Halbwertszeit = 30 Tage.
→ Skill verbessert sich? Score steigt automatisch.
→ Skill verschlechtert sich? Alte gute Ratings verblassen.
```

---

## 3. Correction Propagation — Von Flat DB zu Error Taxonomy

### Aktuell (schwach)
29 Regeln in einer flachen Tabelle. Keine Hierarchie, keine Vererbung, keine automatische Erstellung.

### State of the Art: Hierarchical Rule System

**Vale-Architektur angepasst:**
```
Correction Taxonomy:
├── tone/                    # Kategorie
│   ├── no-llm-phrases       # Rule
│   │   ├── patterns: ["great question", "i'd be happy to", ...]
│   │   ├── severity: error
│   │   └── applies_to: [email, linkedin, blog, report]
│   └── solo-founder-voice
│       ├── patterns: ["\\bwe\\b(?!bsite|b page)"]  # "we" aber nicht "website"
│       ├── severity: error
│       └── applies_to: [email, linkedin]
├── content/
│   ├── no-fake-numbers
│   │   ├── patterns: ["\\d+[%+]?\\s*(professionals?|companies|users)"]
│   │   ├── severity: error
│   │   └── check: "verify_claim"  # → LLM-Judge prüft Claim
│   └── sources-required
│       ├── check: "has_sources"
│       └── applies_to: [report, blog]
└── design/
    └── brand-colors-only
        ├── patterns: ["#(?!0a0a0a|d4a853|c47070|ececec|141414)[0-9a-f]{6}"]
        └── applies_to: [website]
```

**Auto-Correction-Erstellung:**
Wenn Florian im Chat sagt: "Das 'we' muss raus, ich bin Solo Founder" →
1. Parsing: Correction = {wrong: "we", right: "I", category: "tone", rule: "solo-founder-voice"}
2. Bestätigung: "Neue Correction: 'we' → 'I' für Solo Founder Voice. Als permanente Regel speichern?"
3. Propagation: Alle zukünftigen Outputs mit "we" → Pre-Flight FAIL

**Correction Inheritance:**
- `no-llm-phrases` gilt für ALLE Output-Types
- `solo-founder-voice` gilt für email + linkedin
- Neue Correction erbt von Parent-Kategorie
- Override möglich: "Für diesen Topic ist 'we' okay" → Topic-Level Exception

---

## Implementierungsreihenfolge

### Schritt 1: Regex Pre-Flight (1h)
- Corrections bekommen `patterns` Feld (JSON Array von Regex)
- Pre-Flight läuft alle Patterns gegen Output
- Ergebnis: pass/fail/warn pro Check mit matched Pattern

### Schritt 2: Structural Validators (1h)
- Output-Type-spezifische Checks als Python-Funktionen
- Email: Anrede, Betreff, Signatur, Länge
- LinkedIn: Zeichenlimit, CTA, kein "we"

### Schritt 3: Bayesian Trust (30min)
- Trust-Berechnung umstellen auf Bayesian Average mit Decay
- Score-History speichern für Trend-Analyse

### Schritt 4: Graduated Autonomy (30min)
- Frontend: Output bei CONFIRM verbergen bis Pre-Flight done
- Frontend: Pre-Flight Results inline bei REVIEW
- AUTO + DELEGATED: Actions sofort ausführen

### Schritt 5: Auto-Correction-Erstellung (1h)
- Chat-Parser: "X sollte Y sein" → Correction-Vorschlag
- Bestätigungs-Flow im Chat

### Schritt 6: LLM-as-Judge (optional, 1h)
- Nur für REVIEW/CONFIRM: LLM prüft Output gegen top-10 Corrections
- Kosten: ~$0.01 pro Check (gpt-4o-mini)

**Total: ~5h für echte Smart Logic. Danach ist das System ein echter Prose-Linter mit Trust-basierter Autonomie.**

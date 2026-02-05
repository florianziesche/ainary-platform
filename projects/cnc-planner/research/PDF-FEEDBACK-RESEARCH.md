# Research: PDF-Export & Kundenfeedback

**Erstellt:** 2026-02-05 16:20
**Ziel:** Was erwartet der Anwender von PDF-Export und Feedback-Funktion?

---

## 1. Anwender-Perspektive: Wer nutzt das PDF?

### Primär: Der Arbeitsvorbereiter selbst
- **Zweck:** Interne Dokumentation, Arbeitsanweisung für Werker
- **Erwartet:** Vollständige Fertigungsinformationen

### Sekundär: Der Kunde (Auftraggeber)
- **Zweck:** Angebot prüfen, Freigabe erteilen, Feedback geben
- **Erwartet:** Professionelles Angebot mit klaren Preisen

### Tertiär: Der Werker an der Maschine
- **Zweck:** Fertigungsanweisung ausdrucken
- **Erwartet:** Klare Anweisungen, Zeichnung, Werkzeugliste

---

## 2. Marktstandard: Was enthält ein Manufacturing Quote PDF?

### Pflicht-Elemente (immer):
1. **Firmendaten** — Logo, Name, Adresse, Kontakt
2. **Angebotsnummer** — Eindeutige ID für Tracking
3. **Datum & Gültigkeit** — Wann erstellt, wie lange gültig
4. **Kundendaten** — An wen gerichtet
5. **Positionsliste** — Was wird angeboten
6. **Preise** — EP, GP, Summe, MwSt.
7. **Lieferzeit** — Wann fertig
8. **AGB-Verweis** — Rechtliche Absicherung

### Oft enthalten:
- Zeichnungs-Thumbnail
- Material-Spezifikation
- Toleranzangaben
- Zahlungsbedingungen

### Selten (aber wertvoll):
- Kalkulations-Aufschlüsselung (Transparenz!)
- QR-Code für digitales Feedback
- Versionsnummer

---

## 3. Feedback-Mechanismen im Markt

### Option A: E-Mail-basiert (einfachst)
- "Bei Fragen: info@firma.de"
- **Pro:** Kein Aufwand
- **Contra:** Unstrukturiert, geht unter

### Option B: Link im PDF
- "Feedback geben: [URL]"
- **Pro:** Trackbar, strukturiert
- **Contra:** Kunde muss aktiv werden

### Option C: QR-Code im PDF
- Scannt zu Feedback-Formular
- **Pro:** Modern, schnell
- **Contra:** Nicht jeder nutzt es

### Option D: Integriertes Portal
- Kunde hat Login, sieht Angebote, kann kommentieren
- **Pro:** Professionell, vollständig
- **Contra:** Aufwändig zu bauen

---

## 4. Was erwartet Andreas (unser Pilot)?

### Für seine Kunden:
- **Professionelles Angebot** — Mit Logo, sauber formatiert
- **Klare Preise** — Nicht verwirren
- **Zeichnung dabei** — Kunde weiß was er bekommt

### Für sich selbst (Arbeitsvorbereitung):
- **Fertigungsanweisung** — Ausdrucken, an Maschine hängen
- **NC-Code dabei** — Oder zumindest Verweis
- **Werkzeugliste** — Was muss gerüstet werden

### Feedback von Kunden:
- **Erstmal einfach** — E-Mail reicht für den Anfang
- **Später:** Strukturiertes Formular

---

## 5. Unsere PDF-Typen

### PDF Typ 1: Angebot (für Kunden)
```
┌─────────────────────────────────────┐
│ [LOGO]              ANGEBOT         │
│                     ANG-2026-0042   │
├─────────────────────────────────────┤
│ An: Kunde GmbH                      │
│ Datum: 05.02.2026                   │
│ Gültig bis: 05.03.2026              │
├─────────────────────────────────────┤
│ Pos │ Beschreibung      │ Preis    │
│ 1   │ Verbindungsplatte │ €28,40   │
│     │ S235JR, 435×45×15 │          │
├─────────────────────────────────────┤
│ Zwischensumme:           €28,40    │
│ zzgl. MwSt. 19%:          €5,40    │
│ GESAMTBETRAG:            €33,80    │
├─────────────────────────────────────┤
│ Lieferzeit: 5 Werktage              │
│ Zahlungsziel: 14 Tage netto         │
├─────────────────────────────────────┤
│ Fragen? → info@firma.de             │
│ [QR-Code für Feedback]              │
└─────────────────────────────────────┘
```

### PDF Typ 2: Fertigungsanweisung (intern)
```
┌─────────────────────────────────────┐
│ FERTIGUNGSANWEISUNG                 │
│ Verbindungsplatte                   │
│ 2500473.01.11.02.00.001             │
├─────────────────────────────────────┤
│ [ZEICHNUNG]                         │
├─────────────────────────────────────┤
│ Werkstoff: S235JR                   │
│ Rohmaße: 440×50×20 mm               │
│ Fertigmaße: 435×45×15 mm            │
├─────────────────────────────────────┤
│ OPERATIONEN:                        │
│ OP10 Planfräsen      │ T1 │ 1,8min │
│ OP20 Kontur fräsen   │ T2 │ 2,2min │
│ ...                                 │
├─────────────────────────────────────┤
│ WERKZEUGLISTE:                      │
│ T1 Planfräser Ø50                   │
│ T2 VHM-Fräser Ø16                   │
│ ...                                 │
├─────────────────────────────────────┤
│ QUALITÄTSPRÜFUNG:                   │
│ □ Passbohrungen ⌀0,02               │
│ □ Oberfläche Rz 25                  │
└─────────────────────────────────────┘
```

---

## 6. Technische Umsetzung

### Option A: Browser Print (aktuell)
- `window.print()` mit Print-CSS
- **Pro:** Einfach, sofort
- **Contra:** Layout-Kontrolle begrenzt

### Option B: HTML → PDF (Server)
- Puppeteer/Playwright generiert PDF
- **Pro:** Mehr Kontrolle
- **Contra:** Braucht Backend

### Option C: LaTeX → PDF (wie 36ZERO Report)
- Template füllen, XeLaTeX kompilieren
- **Pro:** Perfektes Layout, professionell
- **Contra:** Komplex, langsamer

### Empfehlung für MVP:
**Option A (Browser Print)** mit gutem Print-CSS
- Schnell umsetzbar
- Kunde kann direkt drucken
- Später auf Option B/C upgraden

---

## 7. Feedback-Funktion: MVP

### Einfachste Lösung:
```
┌─────────────────────────────────────┐
│ 💬 Feedback zu dieser Kalkulation   │
├─────────────────────────────────────┤
│ ○ Kalkulation korrekt               │
│ ○ Zeit zu hoch geschätzt            │
│ ○ Zeit zu niedrig geschätzt         │
│ ○ Preis nicht wettbewerbsfähig      │
│                                     │
│ Kommentar (optional):               │
│ ┌─────────────────────────────────┐ │
│ │                                 │ │
│ └─────────────────────────────────┘ │
│                                     │
│ [Feedback senden]                   │
└─────────────────────────────────────┘
```

### Im PDF:
- QR-Code der zu diesem Formular führt
- Oder einfach: "Feedback an: feedback@cncplanner.de"

---

## 8. Zusammenfassung für Diskussion

### Fragen an Florian:

1. **Welche PDF-Typen braucht Andreas zuerst?**
   - Angebot (für Kunden)?
   - Fertigungsanweisung (intern)?
   - Beides?

2. **Feedback-Mechanismus:**
   - Reicht E-Mail für den Anfang?
   - Oder soll ich ein einfaches Formular bauen?

3. **PDF-Technik:**
   - Browser Print (schnell, einfach)?
   - Oder LaTeX (perfekt, aber aufwändiger)?

4. **Zeichnung im PDF:**
   - Thumbnail einbetten?
   - Oder separater Anhang?

---

*Warte auf Entscheidung vor Umsetzung.*

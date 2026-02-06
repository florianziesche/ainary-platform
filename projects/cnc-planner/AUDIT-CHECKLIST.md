# CNC Planer Pro — UI/UX Audit-Checkliste

**VOR jedem Commit auf die Demo-Datei diese Punkte prüfen.**

---

## 1. Inhalt am richtigen Ort?

Jede Information gehört zu EINER Section. Wenn sie woanders auftaucht → verschieben oder entfernen.

| Information | Gehört zu | NICHT zu |
|---|---|---|
| Spannungs-Warnungen | Werkstück (Teil) | Preise & Sätze |
| Werkstoff-Warnungen | Kalkulation | Teil |
| Materialpreise | Preise & Sätze | Einstellungen |
| Stundensätze | Preise & Sätze | Einstellungen |
| Zuschlagssätze | Preise & Sätze | Kalkulation |
| Marge/Gewinn | Preise & Sätze (Zuschläge) | Kalkulation (nur Anzeige) |
| Firmendaten | Einstellungen | Angebot (nur Anzeige) |
| Feedback-Widget | Sticky FAB (global) | Nicht inline in Sections |
| Normen-Referenzen | Einstellungen (Doku) + Kalkulation | Nicht doppelt! |

**Regel:** Wenn gleiche Info an 2+ Stellen → eine wird Quelle, andere zeigt nur an.

---

## 2. Verwaiste Elemente?

Nach jedem größeren Umbau prüfen:

```bash
# JS referenziert Element das nicht im HTML ist:
grep -oP "getElementById\('([^']+)'\)" FILE | sort -u > /tmp/js-ids.txt
grep -oP 'id="([^"]+)"' FILE | sort -u > /tmp/html-ids.txt
comm -23 /tmp/js-ids.txt /tmp/html-ids.txt
```

```bash
# onclick/onchange Handler die keine JS-Funktion haben:
grep -oP 'onclick="([^(]+)\(' FILE | sort -u > /tmp/handlers.txt
grep -oP 'function ([a-zA-Z]+)\(' FILE | sort -u > /tmp/functions.txt
```

---

## 3. Überflüssige UI-Elemente?

Vor jedem Release fragen:

- [ ] **Header-Buttons** (CSV, PDF): Sind die auf JEDER Seite sinnvoll oder nur auf bestimmten?
- [ ] **Info-Boxen**: Ist der Hinweis noch aktuell? Wiederholt er sich?
- [ ] **Doppelte Controls**: Gibt es 2 Wege dasselbe zu tun? (z.B. 2 Marge-Inputs)
- [ ] **Emojis**: Keine Emojis in der UI (industrieller Standard)
- [ ] **Leere Sections**: Gibt es Tabs/Bereiche ohne Inhalt?

---

## 4. Konsistenz

- [ ] **Schriftgrößen**: Alle Selects, Inputs, Labels gleiche Größe? (keine inline font-size Overrides)
- [ ] **Spacing**: Gleiche margin/padding für gleiche Elementtypen?
- [ ] **Farben**: Nur CSS-Variablen, keine Hex-Werte inline?
- [ ] **Formate**: Alle Preise EUR X.XXX,XX? Alle Zeiten X,X min?
- [ ] **Labels**: Gleiche Begriffe für gleiche Sachen? (nicht "Rüstzeit" hier und "Einrichtzeit" dort)
- [ ] **Expandable**: Wenn ein Element aufklappbar ist, sind ALLE gleichartigen auch aufklappbar?

---

## 5. Navigation stimmt?

- [ ] Jede Section hat einen Nav-Button
- [ ] Jeder Nav-Button hat eine Section
- [ ] showSection() setzt mainTitle korrekt
- [ ] Active-State wird korrekt gesetzt/entfernt

---

## 6. Print-Ansicht

- [ ] Nur aktive Section wird gedruckt
- [ ] Sidebar, Buttons, Inputs ausgeblendet
- [ ] Tabellen-Daten in Inputs sind trotzdem sichtbar (td input)
- [ ] page-break-inside: avoid auf Cards und OP-Details
- [ ] Keine leeren Seiten
- [ ] Schriftgröße lesbar (≥10px)
- [ ] Seitentitel wird angezeigt

---

## 7. JavaScript

- [ ] `node --check` auf extrahiertem JS-Block → keine Syntax-Fehler
- [ ] Keine `?.property = value` (ungültig!)
- [ ] Alle getElementById mit `?.` wenn Element möglicherweise fehlt
- [ ] `calculate()` nur über expliziten Button, nicht auto-trigger

---

## Wann prüfen?

1. **Nach jedem Umbau** (Sections verschieben, Navigation ändern)
2. **Vor jedem Commit** (Quick-Scan: Punkte 3, 4, 7)
3. **Vor jeder Demo** (Alle Punkte, Browser-Test)

---

*Erstellt: 2026-02-06 — Nach Warnung-am-falschen-Ort Bug*

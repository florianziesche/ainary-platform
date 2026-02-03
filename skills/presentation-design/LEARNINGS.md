# Presentation Design Learnings

## Fehler in v4 vs v3

### Was v3 besser machte:
1. **Mehr Whitespace** — Elemente hatten mehr Raum zum Atmen
2. **Größere Margins** — `margin-bottom: 48px` statt `40px` bei Subtitles
3. **Konsistente Abstände** — Nicht alles komprimiert um Platz zu sparen
4. **Visuelle Hierarchie** — Klare Trennung zwischen Sections
5. **Weniger dicht** — Nicht versucht, alles auf eine Slide zu quetschen

### Meine Fehler beim Rewrite:
- CSS komprimiert (einzeilig statt lesbar)
- Abstände reduziert um "Platz zu sparen"
- Fokus auf Inhalt, nicht auf visuelle Balance
- "Takeaway"-Boxes zu nah am Content
- Kompakteren Code ≠ besseres Design

---

## Design-Prinzipien für Präsentationen

### 1. Whitespace ist König
- Minimum 48px zwischen Sections
- Slides dürfen "leer" wirken — das ist gut
- Lieber eine Slide mehr als eine überfüllte

### 2. Konsistente Spacing Scale
```
8px   — Micro (innerhalb von Elementen)
16px  — Small (zwischen verwandten Elementen)
32px  — Medium (zwischen Gruppen)
48px  — Large (zwischen Sections)
64px  — XL (Slide Padding)
```

### 3. Typografie-Hierarchie
```
Title:     40-56px, 700 weight
Subtitle:  18-24px, 400 weight, gray
Body:      15-16px, 400 weight
Label:     11-12px, 600 weight, uppercase
```

### 4. Nie komprimieren
- Wenn Content nicht passt → Split auf 2 Slides
- Nie Font-Sizes reduzieren um mehr reinzubekommen
- Nie Margins reduzieren

### 5. Visual Balance
- Elemente sollten "schweben", nicht "kleben"
- Footer braucht Abstand zum Content (min 48px)
- Takeaway-Boxes: margin-top: auto, margin-bottom: 56px (vor Footer)

---

## Checkliste vor Export

- [ ] Jede Slide hat genug Whitespace?
- [ ] Footer überlappt nicht mit Content?
- [ ] Abstände konsistent (gleiche Elemente = gleiche Margins)?
- [ ] Text nicht zu klein (<14px)?
- [ ] Maximal 5-7 Elemente pro Slide?
- [ ] Visuelle Hierarchie klar (was ist wichtig)?

---

## Referenz: Gute Präsentationen

- **Apple Keynotes** — Minimalistisch, viel Whitespace
- **McKinsey Decks** — Klare Struktur, konsistente Layouts
- **Sequoia Pitch Deck** — Fokussiert, eine Message pro Slide

---

*Erstellt: 2026-02-03 nach Feedback von Florian*
*Lesson: Design-Qualität geht vor Code-Kompaktheit*

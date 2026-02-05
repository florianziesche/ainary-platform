# UI Research: CNC Kalkulationssoftware

**Erstellt:** 2026-02-05 16:15
**Ziel:** Best Practices für das CNC Planner Pro UI aus Anwender-Perspektive

---

## 1. Wer ist der Anwender?

### Primärer Nutzer: Arbeitsvorbereiter / Planer
- **Aufgabe:** Anfragen kalkulieren, Angebote erstellen
- **Umgebung:** Büro, manchmal Werkstatt
- **Zeit:** Unter Druck, viele Anfragen gleichzeitig
- **Expertise:** Technisch versiert, kennt Fertigungsprozesse

### Was braucht er?
1. **Schneller Überblick** — Welche Teile sind offen? Was ist dringend?
2. **Wenige Klicks** — Von Anfrage zu Angebot in <5 Minuten
3. **Vertrauen** — Transparente Kalkulation, keine Blackbox
4. **Flexibilität** — Werte anpassen können wenn nötig

---

## 2. Analyse: Wie machen es andere?

### Paperless Parts (US-Marktführer)
- **Hero:** "Quote Faster. Quote Smarter."
- **Key Metric:** "15 min statt 2 Stunden"
- **UI Pattern:** 
  - Zentralisierte Plattform
  - Jobs/RFQs als Liste
  - Status-Badges (Offen, In Arbeit, Gesendet)

### Spanflug MAKE (DACH)
- **Fokus:** CAD hochladen → Sofort Preis
- **UI Pattern:**
  - Drag & Drop Upload prominent
  - Projekt-Archiv als Sidebar
  - Kalkulations-Details ausklappbar

### MachineMetrics / FactoryWiz
- **Fokus:** Shop Floor Dashboard
- **UI Pattern:**
  - Große Zahlen/KPIs
  - Farbcodierung (Grün/Gelb/Rot)
  - Touch-optimiert

---

## 3. Probleme mit aktuellem CNC Planner UI

### Problem 1: Teil wird nicht sofort sichtbar
- Upload-Box nimmt viel Platz
- Projekt-Karten sind "below the fold"
- **Fix:** Projekte prominenter, Upload kleiner

### Problem 2: Keine Job-Status-Übersicht
- Kein Dashboard mit offenen Anfragen
- Kein "Was muss ich heute machen?"
- **Fix:** Job-Liste mit Status-Spalten

### Problem 3: Kalkulation wirkt wie Blackbox
- Detailrechnung versteckt im Tab
- Anwender will SOFORT sehen: Wie kommt der Preis zustande?
- **Fix:** Kalkulations-Zusammenfassung direkt sichtbar

---

## 4. UI-Vorschläge für Diskussion

### Option A: "Job-Liste First"
```
┌─────────────────────────────────────────────────────┐
│ [Logo] CNC Planner Pro          [+ Neues Teil]     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  OFFENE KALKULATIONEN (3)                          │
│  ┌─────────────────────────────────────────────┐   │
│  │ ☑ Verbindungsplatte  │ S235JR │ 12,5min │ €28 │
│  │   2500473.01.11.02   │ Offen  │ Heute   │     │
│  ├─────────────────────────────────────────────┤   │
│  │ ☐ Adapterplatte      │ AlMg3  │ 24,8min │ €52 │
│  │   2500473.01.01.02   │ Offen  │ Heute   │     │
│  ├─────────────────────────────────────────────┤   │
│  │ ☐ Grundplatte        │ 1.4571 │ 41,8min │€122 │
│  │   WCAD-15-02-2020    │ Offen  │ Gestern │     │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  [Teil auswählen für Details →]                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Pro:** Klarer Fokus, wie E-Mail-Inbox
**Contra:** Weniger visuell ansprechend

### Option B: "Dashboard mit Karten"
```
┌─────────────────────────────────────────────────────┐
│ [Logo]                    [Upload] [+ Neu]         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ OFFEN    │ │ IN ARBEIT│ │ GESENDET │           │
│  │    3     │ │    0     │ │    12    │           │
│  └──────────┘ └──────────┘ └──────────┘           │
│                                                     │
│  AKTUELLE TEILE                                    │
│  ┌─────────────────┐ ┌─────────────────┐          │
│  │ [Thumbnail]     │ │ [Thumbnail]     │          │
│  │ Verbindungs-    │ │ Adapterplatte   │          │
│  │ platte          │ │                 │          │
│  │ S235JR │ €28,40 │ │ AlMg3  │ €52,15│          │
│  │ [Öffnen]        │ │ [Öffnen]        │          │
│  └─────────────────┘ └─────────────────┘          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Pro:** Visuell, Thumbnails zeigen Teil
**Contra:** Braucht Bilder, mehr Platz

### Option C: "Split View" (aktuell, verbessert)
```
┌─────────────────────────────────────────────────────┐
│ TEILE          │ KALKULATION                        │
│ ───────────    │ ─────────────                      │
│ [Verbindungs-] │ Verbindungsplatte                  │
│ [Adapterplatte]│ 2500473.01.11.02.00.001           │
│ [Grundplatte]  │                                    │
│                │ ┌─────────────────────────────┐   │
│ ─────────────  │ │ Material: S235JR            │   │
│ [+ Upload]     │ │ Maße: 435×45×15 mm          │   │
│                │ │ Zeit: 12,5 min              │   │
│                │ │ ──────────────────          │   │
│                │ │ PREIS: €28,40               │   │
│                │ └─────────────────────────────┘   │
│                │                                    │
│                │ [Details] [NC-Code] [PDF]         │
└─────────────────────────────────────────────────────┘
```

**Pro:** Kompakt, alles auf einen Blick
**Contra:** Weniger Platz für Details

---

## 5. Empfehlung

**Für Andreas (Arbeitsvorbereiter):** Option C (Split View)

**Warum:**
1. Teil-Liste immer sichtbar (links)
2. Kalkulation sofort sichtbar (rechts)
3. Keine versteckten Tabs
4. Professionell, nicht überladen

**Konkrete Änderungen:**
1. Upload-Box verkleinern oder nach unten
2. Teil-Liste als permanente Sidebar links
3. Kalkulations-Zusammenfassung immer sichtbar
4. Thumbnail der Zeichnung in der Karte

---

## 6. Corporate Identity beibehalten

- **Farben:** Primary (#1e3a5f), Accent (#2563eb)
- **Font:** Inter (professionell, lesbar)
- **Stil:** Clean, nicht überladen, industriell
- **Keine:** Spielereien, Animationen, bunte Icons

---

*Zur Diskussion mit Florian vor Umsetzung.*

# CNC Planner — Struktur-Vereinfachung

## Aktuelle Struktur (10 Sektionen)

| # | Sektion | Inhalt | Problem |
|---|---------|--------|---------|
| 1 | Teil auswählen | Demo-Teile wählen | OK |
| 2 | Parameter | Werkstück + Fertigung | **Redundant mit Teil** |
| 3 | Ergebnis | Preis + Kostenaufschlüsselung | **Redundant mit Kalkulation** |
| 4 | Angebot | PDF-Angebot | OK |
| 5 | Fertigungsanweisung | OPs, Spannung, Maschine | **Redundant mit Kalkulation** |
| 6 | Kalkulation | Detaillierte Berechnung | Hat alles |
| 7 | Werkzeuge | Schnittparameter | **Könnte in Kalkulation** |
| 8 | NC-Code | Heidenhain/Siemens | OK |
| 9 | Feedback | Neu | OK |
| 10 | Einstellungen | Stundensätze, Material | OK |

---

## Vorschlag: 6 Sektionen

```
┌─────────────────────────────────────────────────────────┐
│  📐 TEIL          → Auswahl + Dimensionen + Material    │
├─────────────────────────────────────────────────────────┤
│  💰 KALKULATION   → Preis + Kosten + OPs + Werkzeuge    │
├─────────────────────────────────────────────────────────┤
│  📄 ANGEBOT       → PDF-Export                          │
├─────────────────────────────────────────────────────────┤
│  💻 NC-CODE       → Heidenhain/Siemens/Fanuc            │
├─────────────────────────────────────────────────────────┤
│  📝 FEEDBACK      → Rückmeldung + Cross-Learnings       │
├─────────────────────────────────────────────────────────┤
│  ⚙️ EINSTELLUNGEN → Alle Parameter zentral              │
└─────────────────────────────────────────────────────────┘
```

---

## Was wird zusammengeführt

### 1. TEIL (neu)
**Aus:** Teil auswählen + Parameter

- Demo-Teile Auswahl (Karten)
- Werkstück: Material, Dimensionen, Gewicht
- Fertigung: Stückzahl, Spannung, Setup-Anzahl
- Zusatzoperationen: Entgraten, Sägen, Prüfung

### 2. KALKULATION (erweitert)
**Aus:** Ergebnis + Kalkulation + Fertigungsanweisung + Werkzeuge

**Aufbau:**
```
┌─────────────────────────────────────────────────────────┐
│  PREIS-HERO: €64,89 (±15%)                             │
├─────────────────────────────────────────────────────────┤
│  Kostenaufschlüsselung    │   Mengenstaffel             │
│  - Material + MGK         │   1 Stk: €64,89            │
│  - Fertigung + AV         │   5 Stk: €52,30            │
│  - VwGK + VtGK            │   10 Stk: €48,15           │
│  = Angebotspreis          │                            │
├─────────────────────────────────────────────────────────┤
│  OPERATIONEN (aufklappbar)                              │
│  OP10 Planfräsen      2,7 min   [▶ Details]            │
│  OP20 Kontur          8,0 min   [▶ Details]            │
│  OP50 Schlichten h5   5,1 min   [▶ Details] ⚠️         │
├─────────────────────────────────────────────────────────┤
│  WERKZEUGE & SCHNITTDATEN (aufklappbar)                 │
│  T1 Ø63 Planfräser    vc=180  fz=0,15  [▶]             │
│  T2 Ø20 Schaftfräser  vc=150  fz=0,12  [▶]             │
├─────────────────────────────────────────────────────────┤
│  BERECHNUNGSMETHODIK (aufklappbar)                      │
│  REFA, VDI 3321, DIN 8580                              │
└─────────────────────────────────────────────────────────┘
```

### 3. EINSTELLUNGEN (konsolidiert)
**Alle Parameter an einem Ort:**

| Tab | Inhalt |
|-----|--------|
| Stundensätze | Maschinen-Stundensätze |
| Materialpreise | €/kg pro Werkstoff |
| Zuschlagssätze | MGK, AV, VwGK, VtGK, Gewinn |
| Schnittdaten | vc, fz defaults pro Material |
| Firmendaten | Für Angebote |

---

## Entfernte Redundanzen

| Entfernt | Ersetzt durch |
|----------|---------------|
| Parameter → Werkstück | Teil → Eingabe |
| Parameter → Fertigung | Teil → Eingabe |
| Ergebnis → Kostenaufschlüsselung | Kalkulation → oben |
| Ergebnis → Mengenstaffel | Kalkulation → oben |
| Fertigungsanweisung → OPs | Kalkulation → Operationen |
| Fertigungsanweisung → Spannung | Teil → Eingabe |
| Werkzeuge → Schnittparameter | Kalkulation → Werkzeuge |
| Werkzeuge → Kosten | Kalkulation → Werkzeuge |

---

## Navigation (Sidebar)

**Vorher (10):**
```
◻ Teil auswählen
⚙ Parameter
€ Ergebnis
📊 Kalkulation
🔧 Werkzeuge
───────────────
📄 Angebot
📋 Fertigungsanweisung
</> NC-Code
───────────────
📝 Feedback
⚙ Einstellungen
```

**Nachher (6):**
```
📐 Teil
💰 Kalkulation
📄 Angebot
💻 NC-Code
───────────────
📝 Feedback
⚙ Einstellungen
```

---

## Vorteile

1. **Weniger Klicks** — Nutzer findet alles schneller
2. **Keine Verwirrung** — Keine doppelten Infos
3. **Klare Struktur** — Eingabe → Ergebnis → Export
4. **Fokus** — Wichtiges prominent, Details aufklappbar

---

## Implementierung

**Option A: Schrittweise** (empfohlen)
1. Parameter in Teil integrieren
2. Ergebnis + Fertigungsanweisung in Kalkulation
3. Werkzeuge in Kalkulation
4. Testen

**Option B: Komplett neu**
- v17 von Grund auf mit neuer Struktur

---

## Entscheidung nötig

1. **Struktur OK?** (6 statt 10 Sektionen)
2. **Option A oder B?**
3. **Jetzt oder nach Demo?**

*Erstellt: 2026-02-05*

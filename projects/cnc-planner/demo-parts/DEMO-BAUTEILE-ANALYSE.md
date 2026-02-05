# CNC Demo-Bauteile — Analyse

**Erstellt:** 2026-02-05 15:20
**Quelle:** Zeichnungen aus Demo mit Andreas

---

## Übersicht

| Teil | Beschreibung | Material | Abmessungen | Aufspannungen | Einrichtzeit |
|------|--------------|----------|-------------|---------------|--------------|
| **001** | Block (oval) | Alu/Stahl | 120×105×40 | 2-3 | 25-35 min |
| **002** | Adapterplatte | Aluminium | 81×66×50 | 2-3 | 20-25 min |
| **003** | Verbindungsplatte | S235JR Stahl | 435×45×15 | 1 | 15-20 min |

---

## Teil 1: Block (2500473.01.01.01.01.001)

### Zeichnungsdaten
- **Beschreibung:** Zylindrisches Bauteil mit abgeflachten Seiten, Bohrungen und Gewinde
- **Material:** Nicht angegeben (vermutlich Alu, Gewicht 1,7 kg)
- **Abmessungen:** Ø120 × 105 × 40 mm

### Toleranzen
| Merkmal | Toleranz |
|---------|----------|
| Ø16 H7 Passbohrung | +0,018 / 0 |
| Ø6 H7 Passbohrungen (2×) | +0,012 / 0 |
| Positionstoleranz Passbohrungen | ⌀0,02 |
| Allgemeintoleranzen | DIN ISO 2768-mK |

### Oberflächengüte
- Rz 25

### Spannung & Einrichtung
- **Aufspannungen:** 2-3
  1. Außenkontur fräsen (Spannen am Rohmaterial)
  2. Oberseite bearbeiten (Bohrungen, Gewinde)
  3. Optional: Unterseite falls Bearbeitung nötig
  
- **Spannvorschlag:** 
  - Schraubstock mit weichen Backen (Alu)
  - Oder Spannpratzen bei Konturbearbeitung
  
- **Einrichtzeit:** ~25-35 Minuten

---

## Teil 2: Adapterplatte (2500473.01.01.02.01.001)

### Zeichnungsdaten
- **Beschreibung:** Flanschplatte mit Zentrierbohrung und Befestigungslöchern
- **Material:** Nicht angegeben (vermutlich Aluminium, Gewicht 627g)
- **Abmessungen:** 81 × 66 × 50 mm
- **Zentrierbohrung:** Ø40 außen, Ø20 innen

### Toleranzen
| Merkmal | Toleranz |
|---------|----------|
| Ø10 H7 Passbohrungen (2×) | +0,015 / 0 |
| Ø5 H7 | +0,012 / 0 |
| Positionstoleranz | ⌀0,02 |
| Maß 3 | +0,1 / 0 |

### Oberflächengüte
- Rz 25

### Spannung & Einrichtung
- **Aufspannungen:** 2-3
  1. Oberseite: Bohrungen, Tasche
  2. Unterseite/Kontur
  3. Optional: Seitliche Bearbeitung

- **Spannvorschlag:**
  - 1. Aufspannung: Schraubstock auf Rohmaterial (81×66)
  - 2. Aufspannung: Spannen an bearbeiteter Kontur oder Spannbolzen in Bohrungen

- **Einrichtzeit:** ~20-25 Minuten

---

## Teil 3: Verbindungsplatte (2500473.01.11.02.00.001)

### Zeichnungsdaten
- **Beschreibung:** Flache Verbindungsplatte mit 6 Bohrungen
- **Material:** **S235JR (1.0038)** — Baustahl
- **Abmessungen:** 435 × 45 × 15 mm
- **Gewicht:** 2,2 kg

### Toleranzen
| Merkmal | Toleranz |
|---------|----------|
| Passbohrungen | ⌀ ±0,02 mm |
| Untolerierte Bohrungen | ⌀ ±0,2 mm |
| Allgemeintoleranzen | DIN ISO 2768-mK |

### Oberflächengüte
- Rz 25
- **Nachbehandlung:** Grundiert + lackiert RAL 7035 (max. 200 µm)

### Spannung & Einrichtung
- **Aufspannungen:** 1 (einfaches 2,5D-Teil, alle Bearbeitungen von oben)

- **Spannvorschlag:**
  - Maschinenschraubstock mit Parallelunterlagen
  - Alternativ: Niederzugspanner an den Enden
  - Spannen an der 45mm-Breite

- **Werkzeuge:**
  - Bohrer Ø9, Ø13,5
  - Fasenfräser 45°

- **Einrichtzeit:** ~15-20 Minuten (einfachstes Teil!)

---

## Zusammenfassung für Demo

| Kriterium | Teil 1 | Teil 2 | Teil 3 |
|-----------|--------|--------|--------|
| Komplexität | Mittel-Hoch | Mittel | Niedrig |
| Aufspannungen | 2-3 | 2-3 | 1 |
| Einrichtzeit | 25-35 min | 20-25 min | 15-20 min |
| Beste für Demo | ❌ Komplex | ✅ Gut | ✅ Einfach |

### Demo-Empfehlung:
1. **Starte mit Teil 3** (Verbindungsplatte) — einfach, schnell kalkulierbar, zeigt Grundfunktion
2. **Dann Teil 2** (Adapterplatte) — mittlere Komplexität, zeigt Mehrfachaufspannung
3. **Teil 1 optional** — wenn Zeit, zeigt komplexere Geometrie

---

## Für CNC Planer Pro Eingabe

### Teil 3 (empfohlen für Demo):
- Werkstoff: S235JR Stahl
- Rohteil: 440 × 50 × 20 mm
- Fertigteil: 435 × 45 × 15
- Bearbeitungen: Plan fräsen, 6× Bohrungen, Fasen
- Aufspannungen: 1
- Einrichtzeit: 15-20 min

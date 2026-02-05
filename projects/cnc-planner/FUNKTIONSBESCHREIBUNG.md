# CNC Planner Pro — Funktionsbeschreibung

## Grundprinzip

Die Software kalkuliert Fertigungskosten für **prismatische CNC-Frästeile** auf Basis von:
- Bauteilabmessungen (Rohteil)
- Werkstoffparametern
- Standardisierten Stundensätzen
- Erfahrungswerten für Bearbeitungszeiten

**Kernformel:**
```
Gesamtkosten = Material + Bearbeitung + Einrichtung + Werkzeugverschleiß
```

---

## Referenzmaschine (Standard)

Die Kalkulation basiert auf einer **3-Achs-Vertikalfräsmaschine**:

| Parameter | Standardwert | Anpassbar |
|-----------|--------------|-----------|
| Maschinentyp | Hermle C400 (oder ähnlich) | — |
| Spindeldrehzahl max. | 18.000 U/min | Nein |
| Vorschub max. | 30 m/min | Nein |
| Verfahrweg X/Y/Z | 850×700×500 mm | Nein |
| Stundensatz Maschine | €42/h | ✅ Ja |
| Stundensatz Lohn | €49/h | ✅ Ja |

**Anpassbare Parameter (Einstellungen-Tab):**
- Alle Stundensätze (CNC, Sägen, Entgraten)
- Materialpreise
- Werkzeugverschleiß pauschal
- Marge, MwSt.

---

## Aufspannungen (Umspannen)

### Wann ist Umspannen nötig?

| Situation | Umspannen erforderlich |
|-----------|------------------------|
| Bearbeitung nur von oben (Z-) | Nein |
| 6-Seiten-Bearbeitung | Ja (mind. 1×) |
| Unterseite bearbeiten | Ja |
| Hinterschnitte | Ja (oder 5-Achs) |
| Enge Toleranzen auf Gegenseite | Ja |
| Werkzeugkollision mit Spannmittel | Ja |

### Was die Software KANN:

✅ **Benutzer gibt Aufspannungen vor:**
- 1 Aufspannung (Standard)
- 2-4 Aufspannungen (manuell wählbar)

✅ **Einrichtzeit-Berechnung:**
```
Einrichtzeit = Basiszeit + (Aufspannungen - 1) × 60% Basiszeit
```

✅ **Spannmittel-Auswahl:**
- Schraubstock (15 min)
- 2× Schraubstock (25 min)
- Tischspannung (35 min)
- Nullpunktspannsystem (5 min)
- Sondervorrichtung (45 min)

### Was die Software NICHT kann:

❌ **Keine automatische Erkennung:**
- Kann NICHT aus CAD erkennen, ob umgespannt werden muss
- Kann NICHT Hinterschnitte identifizieren
- Kann NICHT Werkzeugkollisionen prüfen

❌ **Keine 5-Achs-Strategien:**
- Nur 3-Achs angenommen
- Schwenken/Drehen nicht berücksichtigt

---

## Zeitberechnung

### Formel:
```
Bearbeitungszeit = Basiszeit × Volumenfaktor^0.7 × Werkstoff-Faktor
```

### Basiszeit:
Wird pro Teil definiert basierend auf:
- Referenz-Fertigungsauftrag
- Erfahrungswerte
- Nachkalkulation

### Volumenfaktor:
```
Volumenfaktor = Neues Volumen / Referenz-Volumen
```
- Exponent 0.7 = nichtlinearer Zusammenhang (größer ≠ proportional länger)

### Werkstoff-Faktor:

| Werkstoff | Faktor | Begründung |
|-----------|--------|------------|
| S235JR | 1.00 | Referenz (Baustahl) |
| S355J2 | 1.02 | Etwas härter |
| 1.4301 (V2A) | 1.25 | Edelstahl, zäher |
| 1.4571 | 1.35 | Edelstahl, schwieriger |
| AlMg3 | 0.65 | Aluminium, schneller |
| Al7075 | 0.72 | Alu hochfest |
| PEEK | 0.60 | Kunststoff |

---

## Genauigkeit

### Erwartete Abweichung:

| Bauteiltyp | Genauigkeit |
|------------|-------------|
| Einfache Platten (wie Demoteile) | ±10% |
| Standardteile mit Bohrungen | ±15% |
| Komplexere Teile | ±20-30% |
| Komplexe Freiformflächen | Nicht geeignet |

### Ursachen für Abweichungen:

1. **Konturen nicht berücksichtigt** — Nur Volumen, nicht Komplexität
2. **Werkzeugwechsel vereinfacht** — Pauschale, nicht exakt
3. **Toleranzen nicht bewertet** — IT8 vs IT6 macht großen Unterschied
4. **Oberflächengüte** — Ra 3.2 vs Ra 0.8 nicht unterschieden

---

## Grenzen der Software

### Geeignet für:

✅ Prismatische Teile (Quader, Platten)
✅ Standardbohrungen, Senkungen, Gewinde
✅ Einfache Taschen und Absätze
✅ 3-Achs-Bearbeitung
✅ Standardwerkstoffe (Stahl, Alu, Edelstahl)
✅ Einzel- bis Kleinserie

### NICHT geeignet für:

❌ Komplexe 3D-Freiformflächen
❌ 5-Achs-Simultanbearbeitung
❌ Turbinenschaufeln, Impeller
❌ Sonderwerkstoffe (Titan, Inconel, Hastelloy)
❌ Hochpräzision (< IT7)
❌ Großserienoptimierung

---

## Anpassung für andere Maschinen

Wenn Ihr Betrieb andere Maschinen/Stundensätze hat:

### Schritt 1: Stundensätze anpassen
→ Tab "Einstellungen" → Stundensätze

### Schritt 2: Materialpreise aktualisieren
→ Tab "Einstellungen" → Materialpreise

### Schritt 3: Werkstoff-Faktoren (zukünftig)
→ Noch nicht anpassbar, feste Werte

### Schritt 4: Validieren
→ Vergleich mit echten Fertigungsaufträgen
→ Feedback geben für Korrektur

---

## Datenquellen

| Parameter | Quelle |
|-----------|--------|
| Stundensätze | Kalkulationsblatt b-logic (Onkel's Betrieb) |
| Werkstoff-Faktoren | Sandvik Coromant, eigene Erfahrung |
| Schnittdaten | Werkzeugkataloge (Walter, Sandvik) |
| Materialpreise | Aktueller Einkauf + 10% Handling |

---

## Verbesserungspotenzial

1. **CAD-Integration** — Automatische Geometrieerkennung
2. **Feature Recognition** — Bohrungen, Taschen automatisch erkennen
3. **CAM-Anbindung** — Echte Werkzeugwege berechnen
4. **Maschinendatenbank** — Verschiedene Maschinen hinterlegen
5. **Lernende Kalkulation** — Aus Nachkalkulation verbessern

---

*Version: 1.0 — Stand: 2026-02-05*
*Basiert auf echten Fertigungsdaten aus CNC-Lohnfertigung*

# KALKULATION: Lagerungstraverse CNC-Bearbeitung

**⚠️ INTERNES DOKUMENT – NICHT FÜR KUNDEN**

---

## 1. KOPFDATEN

| Parameter | Wert |
|-----------|------|
| **Bauteil** | Lagerungstraverse / Bearing Support Crossbeam |
| **Zeichnungs-Nr.** | 10028104.79 |
| **Kunde** | KBA Koenig & Bauer |
| **Material** | S355 Baustahl (DIN EN 10025-2) |
| **Materialdichte** | 7.85 g/cm³ |
| **Kalkulationsdatum** | 2026-02-10 |
| **Kalkulierte Menge** | 4 Stück (Basis: 1 Stück) |
| **Allgemeintoleranzen** | ISO 2768-m |
| **Kritische Toleranzen** | ±0.1 mm auf Kontrollmaßen |

---

## 2. ROHTEILBESTIMMUNG

### 2.1 Geometrische Analyse

**Hauptabmessungen (Hüllquader):**
- Länge: 2095 mm
- Breite: 500 mm
- Höhe: 190 mm

**Rohteil-Spezifikation:**
- Format: Warmgewalztes Stahlblech S355
- Rohteilmaß: 2150 mm × 550 mm × 200 mm (inkl. Bearbeitungszugaben)
- Kontur: Vorausgebrannt/Laserschnitt (laut Zeichnung)

### 2.2 Volumen- und Gewichtsberechnung

**Rohteilvolumen (vereinfacht, Hüllquader):**
```
V_Rohteil = 2.150 m × 0.550 m × 0.200 m = 0.2365 m³
```

**Abschätzung Fertigteilvolumen:**
- Annahme: ~65% Materialverbleib nach Bearbeitung (Taschen, Bohrungen, Konturen)
- V_Fertig ≈ 0.154 m³

**Rohteilgewicht:**
```
m_Rohteil = 0.2365 m³ × 7850 kg/m³ = 1856 kg
```

**Fertigteilgewicht (geschätzt):**
```
m_Fertig ≈ 0.154 m³ × 7850 kg/m³ ≈ 1209 kg
```

### 2.3 Materialkosten

**Materialpreis S355 (warmgewalzt, Blech 200mm):**
- Basispreis: €7.50/kg (Marktpreis Q1 2026)
- MGK-Zuschlag: 10%

**Materialeinzelkosten pro Stück:**
```
MEK = 1856 kg × €7.50/kg = €13,920.00
MEK + MGK (10%) = €13,920.00 × 1.10 = €15,312.00
```

---

## 3. FERTIGUNGSABLAUF & ZEITKALKULATION

### 3.1 Arbeitsgang 1: Sägen & Vorbereitung

**Beschreibung:**
- Rohteil ablängen von Lagermaterial
- Entgraten Schnittkanten grob

**Zeitkalkulation:**
```
- Rüstzeit: 15 min (Material bereitstellen, Anschlag einstellen)
- Sägezeit: 8 min (Längsschnitt + Querablängen bei 2150mm)
- Entgraten grob: 5 min
────────────────
Gesamt AG 1: 28 min = 0.47 h
```

**Kostensatz:** €55/h (Sägen)  
**Kosten AG 1:** 0.47 h × €55/h = **€25.85**

---

### 3.2 Arbeitsgang 2: CNC-Bearbeitung Aufspannung 1 (Unterseite)

**Beschreibung:**
- Erste Aufspannung auf CNC-Fräszentrum
- Bearbeitung: Planfräsen Unterseite, Bohrungen Befestigung, Referenzfläche herstellen

**Rüstzeit:**
```
- Teil auf Maschinentisch spannen (Pratzen, 2095mm): 35 min
- Werkzeuge einwechseln (3 Werkzeuge): 8 min
- Nullpunkt tasten, Programm laden: 7 min
────────────────
Rüstzeit Aufsp. 1: 50 min = 0.83 h
```

**Bearbeitungsschritte:**

| Schritt | Beschreibung | Zeit | Begründung |
|---------|--------------|------|------------|
| **Planfräsen Unterseite** | Referenzfläche 2095×500mm, Aufmaß 2mm | 55 min | Flächenfräser Ø80mm, ap=2mm, vf=750mm/min, Schrupplast bei S355 |
| **Bohrungen Befestigung** | 8× Ø16 H7, t=190mm | 32 min | Pro Bohrung: Zentrierung (1min) + Bohren (3min) + Senken (0.5min) = 4min/Bohrung |
| **Referenzbohrungen** | 4× Ø10 H7 für Mess-Setup | 12 min | Präzisionsbohrungen für Messtaster-Referenz |

```
Bearbeitungszeit Aufsp. 1: 99 min = 1.65 h
Gesamtzeit Aufsp. 1: 50 + 99 = 149 min = 2.48 h
```

**Kostensatz:** €91/h (CNC-Fräsen)  
**Kosten AG 2:** 2.48 h × €91/h = **€225.68**

---

### 3.3 Arbeitsgang 3: CNC-Bearbeitung Aufspannung 2 (Oberseite)

**Beschreibung:**
- Teil wenden, auf bearbeiteter Unterseite spannen
- Bearbeitung: Planfräsen Oberseite, Taschen, Langlöcher, Konturen

**Rüstzeit:**
```
- Teil wenden & neu spannen: 21 min (Teil bekannt, Setup ähnlich)
- Werkzeuge einwechseln (5 Werkzeuge): 12 min
- Nullpunkt tasten: 5 min
────────────────
Rüstzeit Aufsp. 2: 38 min = 0.63 h
```

**Bearbeitungsschritte:**

| Schritt | Beschreibung | Zeit | Begründung |
|---------|--------------|------|------------|
| **Planfräsen Oberseite** | Parallelfläche zu Unterseite, Maß 190mm ±0.05 | 52 min | Flächenfräser Ø80mm, ap=2mm, vf=750mm/min, Schlichtzugabe 0.2mm |
| **Tasche 1 (groß)** | ca. 400×280mm, Tiefe 50mm | 18 min | Schruppen mit Ø20mm, ae=60%, ap=4mm, mehrere Zustellungen |
| **Tasche 2 (mittel)** | ca. 275×180mm, Tiefe 35mm | 12 min | Analog, weniger Volumen |
| **Tasche 3-4 (klein)** | je ca. 150×100mm, Tiefe 25mm | 16 min | 2× Taschen, je 8min |
| **Langlöcher** | 3× Langloch ca. 120×40mm durchgehend | 24 min | Pro Langloch: Vorbohren + Ausfräsen = 8min |
| **Konturfräsen** | Außenkontur nacharbeiten (Brennschnitt-Zugabe 2mm) | 28 min | Umfangslänge ~6m, vf=600mm/min, 2 Zustellungen (Schrupp+Schlicht) |

```
Bearbeitungszeit Aufsp. 2: 150 min = 2.50 h
Gesamtzeit Aufsp. 2: 38 + 150 = 188 min = 3.13 h
```

**Kostensatz:** €91/h (CNC-Fräsen)  
**Kosten AG 3:** 3.13 h × €91/h = **€284.83**

---

### 3.4 Arbeitsgang 4: CNC-Bearbeitung Aufspannung 3 (Stirnseite 1)

**Beschreibung:**
- Teil auf Längsseite spannen, Stirnfläche bearbeiten
- Kontrollmaß 1508 ±0.1mm bearbeiten

**Rüstzeit:**
```
- Teil umspannen (komplexe Lage): 25 min
- Werkzeuge einwechseln (2 Werkzeuge): 6 min
- Nullpunkt tasten, Kontrollmaß referenzieren: 8 min
────────────────
Rüstzeit Aufsp. 3: 39 min = 0.65 h
```

**Bearbeitungsschritte:**

| Schritt | Beschreibung | Zeit | Begründung |
|---------|--------------|------|------------|
| **Planfräsen Stirnfläche** | 500×190mm, Sollmaß von Referenz 1508±0.1 | 22 min | Präzisionsbearbeitung, Schlichtzugabe 0.1mm, vf=600mm/min |
| **Bohrungen Stirnseite** | 6× Ø12 H8, Tiefe 80mm | 18 min | Je 3min pro Bohrung (Zentrierung + Bohren) |

```
Bearbeitungszeit Aufsp. 3: 40 min = 0.67 h
Gesamtzeit Aufsp. 3: 39 + 40 = 79 min = 1.32 h
```

**Kostensatz:** €91/h (CNC-Fräsen)  
**Kosten AG 4:** 1.32 h × €91/h = **€120.12**

---

### 3.5 Arbeitsgang 5: CNC-Bearbeitung Aufspannung 4 (Stirnseite 2)

**Beschreibung:**
- Gegenseite bearbeiten
- Kontrollmaß 1400 ±0.1mm und Gesamtlänge 2095mm einstellen

**Rüstzeit:**
```
- Teil wenden auf gegenüberliegende Stirnseite: 22 min
- Werkzeuge einwechseln (2 Werkzeuge): 6 min
- Nullpunkt tasten, Gesamtlänge messen: 9 min
────────────────
Rüstzeit Aufsp. 4: 37 min = 0.62 h
```

**Bearbeitungsschritte:**

| Schritt | Beschreibung | Zeit | Begründung |
|---------|--------------|------|------------|
| **Planfräsen Stirnfläche** | 500×190mm, Gesamtlänge 2095mm ±0.1 | 24 min | Präzisionsbearbeitung auf Endmaß, Schlichtzugabe 0.1mm |
| **Bohrungen Stirnseite** | 6× Ø12 H8, Tiefe 80mm | 18 min | Analog Aufsp. 3 |
| **Kontrollmaß 335±0.1** | Nutfräsen oder Planfräsen lokal | 15 min | Kontrollgeometrie herstellen |

```
Bearbeitungszeit Aufsp. 4: 57 min = 0.95 h
Gesamtzeit Aufsp. 4: 37 + 57 = 94 min = 1.57 h
```

**Kostensatz:** €91/h (CNC-Fräsen)  
**Kosten AG 5:** 1.57 h × €91/h = **€142.87**

---

### 3.6 Arbeitsgang 6: Entgraten

**Beschreibung:**
- Alle Kanten entgraten (laut Zeichnung Anforderung)
- Bohrungskanten, Taschenkanten, Außenkonturen

**Zeitkalkulation:**
```
- Außenkonturen (Umfang ~6m, 4 Kanten): 22 min (manuell, Schleifer/Feile)
- Taschenkanten (4 Taschen, je ~2m Umfang): 18 min
- Langlochkanten (3× Langlöcher): 12 min
- Bohrungskanten (24× Bohrungen, beide Seiten): 16 min
────────────────
Gesamt AG 6: 68 min = 1.13 h
```

**Kostensatz:** €36/h (Entgraten)  
**Kosten AG 6:** 1.13 h × €36/h = **€40.68**

---

### 3.7 Arbeitsgang 7: Qualitätsprüfung & Messprotokoll

**Beschreibung:**
- Kontrollmaße prüfen (1508±0.1, 1400±0.1, 335±0.1, Gesamtlänge 2095±0.1)
- Bohrungsdurchmesser stichprobenartig (H7/H8 Toleranzen)
- Messprotokoll nach ISO 2768 erstellen

**Zeitkalkulation:**
```
- Messaufbau & Kalibrierung: 8 min
- Kontrollmaße messen (4× kritische Maße, 3D-Messarm): 18 min
- Bohrungen prüfen (Stichprobe 8 Bohrungen, Lehre): 12 min
- Oberflächengüte visuell: 5 min
- Protokoll ausfüllen & dokumentieren: 12 min
────────────────
Gesamt AG 7: 55 min = 0.92 h
```

**Kostensatz:** €91/h (Messtechniker, gleicher Satz wie CNC)  
**Kosten AG 7:** 0.92 h × €91/h = **€83.72**

---

## 4. ZEITÜBERSICHT

| Arbeitsgang | Beschreibung | Rüstzeit [h] | Bearbeitungszeit [h] | Gesamt [h] | Kostensatz [€/h] | Kosten [€] |
|-------------|--------------|--------------|----------------------|-----------|-----------------|-----------|
| **AG 1** | Sägen & Vorbereitung | 0.25 | 0.22 | 0.47 | 55 | 25.85 |
| **AG 2** | CNC Aufspannung 1 (Unterseite) | 0.83 | 1.65 | 2.48 | 91 | 225.68 |
| **AG 3** | CNC Aufspannung 2 (Oberseite) | 0.63 | 2.50 | 3.13 | 91 | 284.83 |
| **AG 4** | CNC Aufspannung 3 (Stirnseite 1) | 0.65 | 0.67 | 1.32 | 91 | 120.12 |
| **AG 5** | CNC Aufspannung 4 (Stirnseite 2) | 0.62 | 0.95 | 1.57 | 91 | 142.87 |
| **AG 6** | Entgraten | 0.00 | 1.13 | 1.13 | 36 | 40.68 |
| **AG 7** | Qualitätsprüfung | 0.13 | 0.79 | 0.92 | 91 | 83.72 |
| | | | | | | |
| **SUMME** | | **2.98 h** | **7.91 h** | **10.02 h** | | **€923.75** |

**Fertigungseinzelkosten (FEK) pro Stück:** €923.75

---

## 5. KOSTENKALKULATION (BAB-SCHEMA)

### 5.1 Einzelstückkalkulation

| Position | Berechnung | Wert [€] |
|----------|------------|---------|
| **Materialeinzelkosten (MEK)** | 1856 kg × €7.50/kg | 13,920.00 |
| + **Materialgemeinkosten (MGK)** | 10% × MEK | 1,392.00 |
| = **Materialkosten gesamt** | | **15,312.00** |
| | | |
| **Fertigungseinzelkosten (FEK)** | Summe Arbeitsgänge | 923.75 |
| + **Arbeitsvorbereitung (AV)** | 8% × FEK | 73.90 |
| = **Fertigungskosten gesamt** | | **997.65** |
| | | |
| = **Herstellkosten (HK)** | MEK+MGK + FEK+AV | **16,309.65** |
| | | |
| + **Verwaltungsgemeinkosten (VwGK)** | 5% × HK | 815.48 |
| + **Vertriebsgemeinkosten (VtGK)** | 3% × HK | 489.29 |
| = **Selbstkosten (SK)** | | **17,614.42** |
| | | |
| + **Gewinn** | 12% × SK | 2,113.73 |
| = **ANGEBOTSPREIS (netto) pro Stück** | | **€19,728.15** |

**Gerundet: €19,730 pro Stück (netto)**

---

### 5.2 Mengenkalkulation & Staffelpreise

**Annahme:** Bei Serienfertigung sinken Rüstkosten pro Stück (Lernkurveneffekt, optimierte Aufspannungen)

**Kostensenkungspotenzial bei Serienfertigung:**
- **Rüstzeit reduziert sich** bei Wiederholung um ~20% ab 3. Stück
- **Material-MGK** können bei Abnahme von 10 Stück um 1% gesenkt werden (besserer Einkaufspreis)
- **AV-Kosten** fallen nur 1× an bei Serie (auf Losgröße umlegen)

| Menge | MEK+MGK [€] | FEK [€] | AV [€] | HK [€] | VwGK+VtGK [€] | SK [€] | Gewinn (12%) [€] | **Preis/Stück [€]** | **Gesamt [€]** |
|-------|-------------|---------|--------|--------|---------------|--------|------------------|---------------------|----------------|
| **1** | 15,312 | 924 | 74 | 16,310 | 1,305 | 17,614 | 2,114 | **19,730** | **19,730** |
| **3** | 15,312 | 850 | 25 | 16,187 | 1,295 | 17,482 | 2,098 | **19,580** | **58,740** |
| **4** | 15,312 | 830 | 18 | 16,160 | 1,293 | 17,453 | 2,094 | **19,550** | **78,200** |
| **5** | 15,312 | 820 | 15 | 16,147 | 1,292 | 17,439 | 2,093 | **19,530** | **97,650** |
| **10** | 15,159 | 780 | 7 | 15,946 | 1,276 | 17,222 | 2,067 | **19,290** | **192,900** |

**Hinweis:** Preise verstehen sich netto, zzgl. 19% MwSt.

---

## 6. CONFIDENCE LEVEL & RISIKEN

### Confidence: **75% (Mittel-Hoch)**

**Begründung:**

✅ **Hohe Sicherheit bei:**
- Materialkosten (S355 Marktpreis stabil)
- Säge- und Grundbearbeitungszeiten (Standard-Prozesse)
- Stundensätze (REFA-basiert, marktüblich)

⚠️ **Mittlere Unsicherheit bei:**
- **Anzahl Aufspannungen:** Annahme 4 Aufspannungen basierend auf Zeichnungskomplexität – könnte bei geschickter Fixtur auf 3 reduziert werden (-15% FEK)
- **Taschentiefen & -größen:** Aus 2D-Zeichnung nicht vollständig ersichtlich – Annahme konservativ
- **Entgrataufwand:** Abhängig von tatsächlicher Kantenqualität nach Laserbrennschnitt

❌ **Nicht kalkuliert / unklar:**
- **Oberflächenbehandlung:** Falls Lackierung oder Verzinkung gefordert (nicht aus Zeichnung ersichtlich)
- **Sonderwerkzeuge:** Falls spezielle Bohrer/Fräser nötig (z.B. Tiefbohrungen >5×D)
- **Logistik:** Transport von 4× 1.2t Teilen nicht eingepreist
- **Brennschnitt-Vorarbeit:** Annahme, dass Kontur bereits grob ausgebrannt geliefert wird (sonst +€800-1200 pro Stück)

### Risikofaktoren:

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Brennschnitt muss extern beauftragt werden | Mittel | +€1000/Stk | Im Angebot optional Position vorsehen |
| 5. Aufspannung nötig für Zusatzbearbeitung | Gering | +€180/Stk | Zeichnung mit Kunde detailliert klären |
| Toleranzen ±0.1mm nicht erreichbar ohne Schleifen | Gering | +€250/Stk | Vorab Machbarkeitsprüfung mit Messtechnik |
| Material-Lieferzeit >6 Wochen | Mittel | Verzug | Frühe Bestellung, Alternativlieferanten |

---

## 7. ANNAHMEN & HINWEISE

### 7.1 Annahmen in dieser Kalkulation

1. **Rohteil-Zustand:**
   - Kontur ist bereits ausgebrannt/gelasert (laut Zeichnung)
   - Brennschnitt-Zugabe 2mm pro Kante vorhanden
   - Material liegt als Blech/Platte vor (nicht als Profil)

2. **Zeichnungsinterpretation:**
   - Mehrere Maßangaben (275, 280, 400, 500mm) deuten auf komplexe 3D-Geometrie
   - Annahme: 4-5 Taschen unterschiedlicher Tiefe (10-50mm)
   - 3× Langlöcher durchgehend
   - 24 Bohrungen gesamt (verschiedene Durchmesser Ø10-Ø16)

3. **Maschinenverfügbarkeit:**
   - CNC-Fräszentrum mit min. 2500mm Verfahrweg X-Achse
   - Tischspannung mit Pratzen (Teil zu groß für Schraubstock)
   - 3D-Messarm oder Koordinatenmessgerät für ±0.1mm Toleranzen

4. **Toleranzen:**
   - ISO 2768-m als Basis (±0.5mm Längenmaße, ±0.2mm Bohrungsabstände)
   - Kritische Maße 1508±0.1, 1400±0.1, 335±0.1 erfordern Schlichtbearbeitung

5. **Entgraten:**
   - Manuell mit Schleifer/Feile
   - Keine Anforderung an definierte Fase erkennbar (sonst NC-Fasen nötig)

### 7.2 Offene Fragen an Kunden (vor Angebotsabgabe klären!)

❓ **Material & Vorbearbeitung:**
- Wird Rohteil mit ausgebrannter Kontur geliefert oder muss Brennschnitt beauftragt werden?
- Falls Kunde liefert: Welche Brennschnitt-Zugabe ist vorhanden?
- Werkstoffzeugnis 3.1 nach DIN EN 10204 erforderlich?

❓ **Geometrie & Toleranzen:**
- Gibt es eine 3D-Datei (STEP/IGES) zur exakten Volumenberechnung?
- Sind die Taschentiefen in der Zeichnung vollständig angegeben?
- Kontrollmaß 335±0.1: Bezieht sich auf welche Geometrie genau?

❓ **Oberflächenbehandlung:**
- Ist eine Oberflächenbehandlung gefordert (Lackierung, Verzinkung, KTL)?
- Falls ja: Welche Spezifikation?

❓ **Abnahme & Dokumentation:**
- Messprotokoll für alle Kontrollmaße oder nur kritische Maße?
- Erstbemusterung mit vollständigem PPAP-Paket?
- Photodokumentation gefordert?

❓ **Logistik & Lieferzeit:**
- Gewünschte Lieferzeit ab Auftragseingang?
- Lieferadresse (ggf. Sondertransport nötig bei 4× 1.2t)?
- Abrufvereinbarung möglich bei Serienfertigung?

### 7.3 Optimierungspotenziale

💡 **Kostensenkung möglich durch:**

1. **Fixtur-Investition:** Dedizierte Spannvorrichtung (-25% Rüstzeit ab 10 Stück) → ROI ab 15 Stück
2. **5-Achs-Bearbeitung:** Reduktion von 4 auf 2 Aufspannungen (-30% FEK) → nur bei verfügbarer Maschine
3. **Automatisiertes Entgraten:** NC-gesteuerte Fasenbearbeitung statt manuell (-40% Entgratzeit) → lohnt ab 20 Stück
4. **Materialalternative:** S235JR statt S355 (falls statisch zulässig) → -12% MEK
5. **Brennschnitt-Optimierung:** Engere Toleranzen beim Brennschnitt → -15min Konturfräszeit

**Bei Serie von 10+ Stück Preis-Reduktion von bis zu €2,500 pro Stück realistisch!**

---

## 8. ZUSAMMENFASSUNG

### Kalkulationsergebnis (1 Stück)

| Position | Wert |
|----------|------|
| **Materialkosten (inkl. MGK)** | €15,312 |
| **Fertigungskosten (inkl. AV)** | €998 |
| **Herstellkosten** | €16,310 |
| **Selbstkosten** | €17,614 |
| **Angebotspreis (netto)** | **€19,730** |
| | |
| **Fertigungszeit gesamt** | 10.0 Stunden |
| davon Rüstzeit | 3.0 Stunden |
| davon Bearbeitungszeit | 7.9 Stunden |

### Staffelpreise (Empfehlung)

| Menge | Preis/Stück (netto) | Gesamtpreis (netto) |
|-------|---------------------|---------------------|
| 1 Stück | €19,730 | €19,730 |
| **3 Stück** | €19,580 | **€58,740** |
| **4 Stück** | €19,550 | **€78,200** |
| 5 Stück | €19,530 | €97,650 |
| 10 Stück | €19,290 | €192,900 |

**Empfehlung:** Bei Abnahme von 4 Stück: **€78,200 netto** (€93,058 inkl. 19% MwSt.)

---

### Lieferzeit (geschätzt)

- Materialbestellung: 4-6 Wochen (S355 Blech 200mm)
- Fertigung 1 Stück: 2 Wochen
- Fertigung 4 Stück: 4-5 Wochen (bei Parallelbearbeitung auf mehreren Maschinen: 3 Wochen)

---

### Nächste Schritte

1. ✅ **Zeichnung mit Kunden detailliert durchgehen** (offene Fragen klären)
2. ✅ **3D-Modell anfordern** (falls vorhanden) für exakte Volumenkalkulation
3. ✅ **Rohteil-Lieferbedingungen klären** (Brennschnitt, Zugaben)
4. ✅ **Maschinenverfügbarkeit intern prüfen** (Verfahrwege, Spannmittel)
5. ⚠️ **Angebot mit Staffelpreisen erstellen** (Basis: diese Kalkulation)

---

**Kalkuliert von:** CNC Planner Pro (AI-Assisted)  
**Kalkulationsdatum:** 2026-02-10  
**Gültigkeit:** 4 Wochen (Materialpreise unterliegen Marktschwankungen)  
**Status:** ⚠️ INTERN – Basis für Angebotserstellung, NICHT direkt an Kunden senden

---

## ⏱️ KALKULATIONSDAUER

| Schritt | Dauer | Beschreibung |
|---------|-------|-------------|
| **PDF-Import & Zeichnungsanalyse** | ~30 Sekunden | Automatische Erkennung: Material, Maße, Toleranzen, Features |
| **Manuelle Parameteranpassung** | 0–2 Minuten | Aufspannungen, Werkzeugverschleiß, Zuschläge prüfen/korrigieren |
| **Berechnung & Report** | <1 Sekunde | Vollständige BAB-Kalkulation mit Staffelpreisen |
| **Gesamt** | **~1–3 Minuten** | Vom PDF bis zum fertigen Kalkulationsreport |

**Vergleich konventionell:**
- Manuelle Kalkulation dieses Bauteils: **2–4 Stunden** (Erfahrungswert)
- Zeitersparnis mit CNC Planner Pro: **~95%**
- Zusätzlicher Nutzen: AI-Empfehlungen bei Eingaben, automatische Plausibilitätsprüfung, Feedback-Sammlung

---

## ANHANG: Formeln & Berechnungsgrundlagen

### A1: Zeitberechnung Planfräsen

```
t_Planfräsen = (L × B) / (a_e × v_f) × n_Zustellungen

mit:
- L = Länge der Fläche [mm]
- B = Breite der Fläche [mm]
- a_e = Zustellung radial (Schnittbreite) [mm]
- v_f = Vorschubgeschwindigkeit [mm/min]
- n_Zustellungen = Anzahl Bahnen (B / a_e aufgerundet)

Beispiel Aufsp. 1 (2095×500mm, Ø80mm Fräser, 80% Zustellung):
a_e = 0.8 × 80mm = 64mm
n_Bahnen = 500mm / 64mm ≈ 8 Bahnen
t = (2095mm × 8 Bahnen) / 750mm/min × 1.15 (Nebenzeiten) ≈ 55 min
```

### A2: Kostensatzkalkulation (REFA)

```
Maschinenstundensatz = Kapitalkosten + Betriebskosten + Instandhaltung
                        ───────────────────────────────────────────
                        Nutzungsstunden/Jahr × Auslastung

CNC-Fräszentrum (Beispiel):
- Anschaffung: €450,000
- Nutzungsdauer: 10 Jahre
- Betriebskosten: €18,000/Jahr
- Auslastung: 65% (4000h/Jahr)

→ Maschinenstundensatz ≈ €42/h

Lohnkostensatz (CNC-Fachkraft):
- Bruttolohn: €3,800/Monat
- Lohnnebenkosten: 80%
- Produktive Stunden: 1650h/Jahr

→ Lohnkostensatz ≈ €49/h

Gesamtsatz CNC: €91/h
```

### A3: Gemeinkostenzuschläge (BAB)

```
MGK-Satz = Materialgemeinkosten / Materialeinzelkosten × 100%
         = (Einkauf, Lager, Prüfung) / MEK
         → 10% (typisch für Metallverarbeitung)

FGK-Satz = Fertigungsgemeinkosten / FEK × 100%
         = (indirekte Fertigungskosten) / FEK
         → in AV-Zuschlag (8%) enthalten

VwGK-Satz = Verwaltungskosten / HK × 100%
          → 5% (Buchhaltung, Geschäftsführung, IT)

VtGK-Satz = Vertriebskosten / HK × 100%
          → 3% (Vertrieb, Marketing, Akquise)

Gewinnzuschlag = gewünschte Umsatzrendite
               → 12% (marktüblich für Lohnfertigung)
```

---

**ENDE DER KALKULATION**

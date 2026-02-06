# CNC Planer Pro — Nutzerdokumentation

**Version 0.18.0-beta** | Stand: Februar 2026

---

## Inhalt

1. [Überblick](#überblick)
2. [Schnellstart](#schnellstart)
3. [Bauteil-Konfiguration](#bauteil-konfiguration)
4. [Kalkulation](#kalkulation)
5. [Fertigungsanweisung](#fertigungsanweisung)
6. [Angebot](#angebot)
7. [Werkzeuge & Schnittdaten](#werkzeuge--schnittdaten)
8. [NC-Code Generator](#nc-code-generator)
9. [Nachkalkulation](#nachkalkulation)
10. [Konfiguration](#konfiguration)
11. [Drucken & Export](#drucken--export)
12. [Wichtige Hinweise](#wichtige-hinweise)

---

## 1. Überblick

CNC Planer Pro ist ein Vorkalkulations-Werkzeug für CNC-Lohnfertiger. Es ersetzt den Taschenrechner und die Excel-Tabelle — nicht das ERP-System.

**Was das Tool macht:**
- Automatische Zeitermittlung auf Basis von Bauteilgeometrie und Werkstoff
- Vollständige Zuschlagskalkulation (differenzierend, nach Industriestandard)
- Fertigungsanweisung mit Operationsplan
- Angebotsvorlage mit Deckungsbeitragsrechnung
- NC-Code-Entwurf (Heidenhain, Siemens, Fanuc)

**Was das Tool NICHT macht:**
- Kein ERP-Ersatz (keine Auftragssteuerung, Lagerhaltung, Zeiterfassung)
- Keine verbindlichen Preise ohne betriebsspezifische Kalibrierung
- Kein produktionsfertiger NC-Code (Simulation zwingend erforderlich)

---

## 2. Schnellstart

### Erster Schritt nach dem Start

1. **Einstellungen öffnen** (Zahnrad-Symbol in der Navigation)
2. **Preise & Sätze anpassen:**
   - Ihre Maschinenstundensätze (Lohn + Maschine)
   - Ihre Materialpreise (Einkaufspreise, nicht Listenpreise)
   - Ihre Zuschlagssätze (MGK, AV, VwGK, VtGK, Gewinn)
3. **Firmendaten eintragen** (für Angebotsvorlage)

> **Wichtig:** Die voreingestellten Werte basieren auf Erfahrungswerten eines sächsischen Lohnfertigers mit 3-Achs-BAZ. Ohne Anpassung an Ihren Betrieb sind die berechneten Preise nur Richtwerte.

### Bauteil kalkulieren

1. Demobauteil auswählen oder Abmessungen manuell eingeben
2. Werkstoff wählen
3. Stückzahl und Losgröße festlegen
4. „Berechnen + Kalkulation anzeigen" klicken
5. Ergebnis prüfen, bei Bedarf Parameter anpassen

---

## 3. Bauteil-Konfiguration

### Werkstück-Grunddaten

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Bauteilbezeichnung | Freier Name | Verbindungsplatte |
| Abmessungen | Länge × Breite × Höhe in mm | 440 × 50 × 20 |
| Werkstoff | Auswahl aus Werkstoffdatenbank | S235JR |
| Stückzahl | Bestellmenge | 29 |

### Werkstoffauswahl

Die Werkstoffdatenbank enthält gängige Stähle und Aluminium-Legierungen:

| Werkstoff | Bezeichnung | Dichte [g/cm³] | Zeitfaktor |
|-----------|------------|-----------------|------------|
| S235JR | Baustahl | 7,85 | 1,00 |
| S355J2 | Feinkornbaustahl | 7,85 | 1,02 |
| C45 | Vergütungsstahl | 7,85 | 1,10 |
| 1.4301 | V2A Edelstahl | 7,90 | 1,25 |
| 1.4404 | V4A Edelstahl | 7,95 | 1,30 |
| 1.4571 | Edelstahl | 8,00 | 1,35 |
| AlMg3 | Aluminium | 2,66 | 0,70 |
| AlMgSi1 | Aluminium | 2,70 | 0,72 |
| Al7075 | Alu hochfest | 2,81 | 0,85 |

Der **Zeitfaktor** beeinflusst die Bearbeitungszeit relativ zu S235JR. Edelstahl (1,35×) braucht deutlich länger als Baustahl (1,0×), Aluminium (0,7×) ist schneller zerspanbar.

### Toleranzen und Oberflächen

- **Allgemeintoleranz:** DIN ISO 2768-mK (mittlere Längen- und Winkeltoleranzen)
- **Engere Toleranzen** (h5, H7) werden als kritische OPs markiert und erhöhen die Bearbeitungszeit

### Aufspannungen

Das System zeigt die geplanten Aufspannungen (Seite 1, Seite 2). Mehr Aufspannungen = mehr Rüstzeit. Die Rüstzeit wird pro Aufspannung berechnet und auf die Stückzahl umgelegt.

---

## 4. Kalkulation

### Kalkulationsschema

CNC Planer Pro verwendet die **differenzierende Zuschlagskalkulation** — das Standardverfahren im Maschinenbau:

```
  Materialeinzelkosten (MEK)
+ Materialgemeinkosten (MGK %)          → Materialkosten
  
  Fertigungseinzelkosten (FEK)
  = Maschinenkosten + Lohnkosten + Rüstkosten
+ Arbeitsvorbereitung (AV %)            → Fertigungskosten

= HERSTELLKOSTEN

+ Verwaltungsgemeinkosten (VwGK %)
+ Vertriebsgemeinkosten (VtGK %)

= SELBSTKOSTEN

+ Gewinnzuschlag (%)

= ANGEBOTSPREIS
```

### Voreingestellte Zuschlagssätze

| Zuschlag | Voreinstellung | Bezugsgröße | Typischer Bereich |
|----------|---------------|-------------|-------------------|
| MGK | 5 % | Materialeinzelkosten | 3–15 % |
| AV | 12 % | Fertigungseinzelkosten | 8–15 % |
| VwGK | 10 % | Herstellkosten | 8–15 % |
| VtGK | 5 % | Herstellkosten | 3–8 % |
| Gewinn | 8 % | Selbstkosten | 5–15 % |

> Diese Werte sind über **Einstellungen → Preise & Sätze** anpassbar.

### Stundensätze

| Arbeitsgang | Lohn [EUR/h] | Maschine [EUR/h] | Gesamt [EUR/h] |
|------------|-------------|-------------------|----------------|
| CNC-Fräsen | 38 | 32 | 70 |
| Sägen | 35 | 10 | 45 |
| Entgraten | 28 | 3 | 31 |

**Werkzeugkosten** sind im Maschinenstundensatz enthalten und werden nicht separat kalkuliert. Das entspricht der gängigen Praxis in KMU-Lohnfertigern.

### Kostenübersicht

Nach der Berechnung zeigt die Kostenübersicht jeden Posten einzeln. Klicken Sie auf eine Zeile, um die Formel und Herleitung zu sehen.

### Deckungsbeitragsrechnung

Die DB-Rechnung zeigt die Deckungsbeiträge I, II und III:

| Stufe | Berechnung |
|-------|-----------|
| **DB I** | Angebotspreis − MEK − FEK |
| **DB II** | DB I − MGK − AV − Werkzeugverschleiß |
| **DB III** | DB II − VwGK − VtGK |

Dargestellt pro Stück und pro Auftrag. Rüstkosten sind in der Auftragsspalte als Fixbetrag enthalten (nicht × Stückzahl).

### Staffelpreise

Die Mengenstaffel zeigt automatisch Preise für verschiedene Losgrößen. Die Rüstkosten werden pro Stück umgelegt — bei höherer Stückzahl sinkt der Anteil.

---

## 5. Fertigungsanweisung

Automatisch generiert auf Grundlage von Bauteilgeometrie, Werkstoff und Toleranzen.

### Arbeitsgänge (OPs)

Jede OP enthält:
- **OP-Nummer** (10, 20, 30, ... in 10er-Schritten)
- **Beschreibung** (z. B. Planfräsen, Kontur schruppen)
- **Schnittdaten** (n, vf, ap)
- **Werkzeug** (T-Nummer + Durchmesser)
- **Zeit** (Hauptzeit + Nebenzeit)

**Kritische OPs** (enge Toleranzen h5, H7) sind rot markiert.

### Bearbeitung

- **Checkbox pro OP:** Abwählen entfernt die OP aus der Zeitsumme und graut sie aus
- **"+ Arbeitsgang hinzufügen":** Eigene OPs ergänzen (OP-Nr wird automatisch vergeben)
- **CSV-Export:** Fertigungsanweisung als CSV-Datei (Semikolon-getrennt, Excel-kompatibel)

### Prüfmerkmale

Tabelle mit Prüfmerkmalen, Sollwerten und Prüfmitteln. Zeilen können hinzugefügt, entfernt oder per Checkbox deaktiviert werden. CSV-Export verfügbar.

### Drucken

„Drucken / PDF" erzeugt ein sauberes A4-Dokument. Abgewählte OPs werden im Druck ausgeblendet.

---

## 6. Angebot

### Angebotsvorlage

Enthält:
- Firmendaten (aus Einstellungen)
- Kundenadresse (editierbar)
- Betreffzeile
- Positionstabelle mit Einzelpreis, Menge, Gesamtpreis
- Angebotsbedingungen (Lieferzeit, Gültigkeit, Zahlungsbedingungen)

### Anpassung

- Kundenadresse direkt im Angebot bearbeiten
- Betreffzeile bearbeiten
- Firmendaten unter **Einstellungen → Firmendaten** ändern
- Drucken/PDF erzeugt ein professionelles Angebots-PDF

---

## 7. Werkzeuge & Schnittdaten

### Schnittparameter-Tabelle

Zeigt für jedes eingesetzte Werkzeug:
- Schnittgeschwindigkeit Vc [m/min]
- Drehzahl n [U/min]
- Zahnvorschub fz [mm/Z]
- Vorschub vf [mm/min]
- Zustelltiefe ap [mm]
- Eingriffsbreite ae [mm]

Werte basieren auf **VDI 3321 Schnittdatenrichtwerten** für den gewählten Werkstoff.

### Werkzeugeinsatz-Tabelle

Übersicht aller Werkzeuge mit Standzeiten und Einsatzzeiten. Dient der Werkzeugplanung — Werkzeugkosten sind im Maschinenstundensatz enthalten.

---

## 8. NC-Code Generator

### Steuerungen

Drei Formate verfügbar:
- **Heidenhain** (Klartext, TNC 640)
- **Siemens** (840D, ShopMill)
- **Fanuc** (G-Code, 0i-MF)

### Wichtig

> **Entwurf — nicht direkt an der Maschine verwenden.**
> 
> Werkzeugdaten, Nullpunkt, Sicherheitsebene und Verfahrwege müssen vor dem Einsatz an die jeweilige Maschine angepasst werden. Simulation vor dem ersten Durchlauf ist zwingend erforderlich.

### Funktionen

- Code kopieren (Zwischenablage)
- Steuerungsformat wechseln (Buttons oben)

---

## 9. Nachkalkulation

Vier Tabs für die Auswertung nach der Fertigung:

### Historie

Übersicht vergangener Kalkulationen mit Datum, Bauteil, Bearbeiter, Soll-/Ist-Zeiten.

### Soll-Ist-Vergleich

Tragen Sie für jede OP die tatsächliche Bearbeitungszeit ein. Das System zeigt:
- Abweichung in Minuten (Δ)
- Mögliche Ursache (Einrichtung, Werkzeug, Material, Toleranz, NC-Programm, Sonstiges)
- Anmerkungsfeld

### Erkenntnisse

Verdichtung der Soll-Ist-Daten: Welche OPs weichen regelmäßig ab? Welche Ursachen häufen sich?

### Dashboard

Grafische Übersicht der Nachkalkulationsdaten über mehrere Aufträge.

---

## 10. Konfiguration

### Preise & Sätze

- **Stundensätze:** Lohn und Maschine getrennt, pro Arbeitsgang
- **Materialpreise:** Einkaufspreise pro kg, nach Werkstoff
- **Zuschlagssätze:** MGK, AV, VwGK, VtGK, Gewinn (in %)

> **Empfehlung:** Stundensätze jährlich auf Basis einer Vollkostenrechnung überprüfen. Materialpreise mindestens quartalsweise mit aktuellen Einkaufspreisen abgleichen.

### Firmendaten

Name, Adresse, Telefon, E-Mail, Ansprechpartner — erscheinen auf dem Angebot.

### Einstellungen exportieren/importieren

Über JSON-Export/Import lassen sich Konfigurationen sichern oder zwischen Geräten übertragen.

---

## 11. Drucken & Export

| Bereich | Drucken/PDF | CSV | JSON |
|---------|:-----------:|:---:|:----:|
| Kalkulation | ✓ | — | — |
| Fertigungsanweisung | ✓ | ✓ | — |
| Angebot | ✓ | — | — |
| Prüfmerkmale | — | ✓ | — |
| Nachkalkulation | — | ✓ | — |
| Einstellungen | — | — | ✓ |

**Tastenkürzel:** Strg+P öffnet die Druckvorschau. Das System druckt immer die aktuell aktive Seite.

---

## 12. Wichtige Hinweise

### Genauigkeit

- Berechnete Zeiten und Preise sind **Richtwerte auf Basis von REFA-Zeitermittlung und VDI 3321 Schnittdatenrichtwerten**
- Absolute Zahlen sind erst nach **betriebsspezifischer Kalibrierung** (eigene Stundensätze, Materialpreise, Erfahrungswerte) belastbar
- **Nachkalkulation empfohlen:** Vergleichen Sie regelmäßig Soll- mit Ist-Zeiten und passen Sie Ihre Parameter an

### Bekannte Einschränkungen

| Bereich | Einschränkung |
|---------|--------------|
| **Geometrie-Erkennung** | Keine CAD-Analyse. Der Operationsplan wird aus Abmessungen und Werkstoff abgeleitet — nicht aus der tatsächlichen Bauteilgeometrie. Fehlende oder überflüssige OPs sind möglich. |
| **Aufspannungen** | Vereinfachte Darstellung (1–2 Aufspannungen). Bei mehrseitiger Bearbeitung sind zusätzliche Umspannungen wahrscheinlich und müssen manuell ergänzt werden. |
| **Rüstzeiten** | Pauschale Schätzung. Tatsächliche Rüstzeiten hängen stark von Vorrichtungen, Erfahrung des Einrichters und Maschinenzustand ab. |
| **Sonderprozesse** | Nicht abgedeckt: Wärmebehandlung, Beschichtung, Schleifen, Erodieren, Montage, externe Bearbeitung. |
| **Bearbeitungszeiten** | Abweichungen von ±30 % zur Realität sind ohne betriebsspezifische Kalibrierung möglich. |
| **NC-Code** | Entwurf — Simulation vor erstem Einsatz zwingend erforderlich. |
| **Bauteilkomplexität** | Optimiert für prismatische Frästeile. Nicht ausgelegt für Freiformflächen, 5-Achs-Simultanbearbeitung oder Drehteile. |

### Normen und Standards

| Norm | Anwendung |
|------|-----------|
| REFA | Zeitgliederung (Hauptzeit, Nebenzeit, Rüstzeit) |
| VDI 3321 | Schnittdatenrichtwerte |
| DIN 8580 | Fertigungsverfahren (Einordnung) |
| DIN EN 10027 | Werkstoffbezeichnungen |
| DIN ISO 2768-mK | Allgemeintoleranzen |

### Browser-Kompatibilität

Optimiert für aktuelle Versionen von Chrome, Firefox, Safari und Edge. Alle Berechnungen laufen lokal im Browser — keine Daten werden übertragen.

### Datenschutz

CNC Planer Pro arbeitet vollständig offline. Keine Daten verlassen Ihren Rechner. Einstellungen werden im lokalen Browserspeicher (localStorage) gespeichert.

---

**Kontakt & Support**

Florian Ziesche
Tel: +1 347 740 1465
E-Mail: florian@ainary.com

---

*CNC Planer Pro v0.18.0-beta — Stand Februar 2026*

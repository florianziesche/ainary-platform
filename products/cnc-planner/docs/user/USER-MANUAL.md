# CNC Planner Pro — Benutzerhandbuch

**Version:** 1.0  
**Stand:** Februar 2026

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Systemanforderungen](#2-systemanforderungen)
3. [Erste Schritte](#3-erste-schritte)
4. [Projekte verwalten](#4-projekte-verwalten)
5. [Kalkulation erstellen](#5-kalkulation-erstellen)
6. [NC-Code generieren](#6-nc-code-generieren)
7. [Angebote erstellen](#7-angebote-erstellen)
8. [Serienkalkulation](#8-serienkalkulation)
9. [Einstellungen](#9-einstellungen)
10. [Daten exportieren](#10-daten-exportieren)
11. [Fehlerbehebung](#11-fehlerbehebung)
12. [Support](#12-support)

---

## 1. Einführung

### Was ist CNC Planner Pro?

CNC Planner Pro ist eine webbasierte Software zur Berechnung von CNC-Fertigungszeiten und -kosten. Die Software unterstützt Sie bei:

- **Zeitkalkulation:** Berechnung der Maschinenzeit nach DIN 6584
- **Kostenkalkulation:** Material, Werkzeuge, Maschinenstunden
- **NC-Code-Generierung:** Heidenhain, Siemens, Fanuc
- **Angebotserstellung:** Professionelle PDF-Angebote

### Für wen ist die Software geeignet?

- Lohnfertiger und Zerspanungsbetriebe
- Arbeitsvorbereitung (AV)
- Fertigungsleitung
- Kalkulation und Vertrieb

---

## 2. Systemanforderungen

### Browser

| Browser | Mindestversion |
|---------|----------------|
| Chrome | 90+ |
| Firefox | 88+ |
| Safari | 14+ |
| Edge | 90+ |

### Gerät

- Desktop-PC oder Laptop (empfohlen)
- Tablet (eingeschränkt)
- Smartphone (nicht empfohlen)

### Internetverbindung

- Für Login und Cloud-Sync erforderlich
- Offline-Nutzung: Projekte werden lokal gespeichert

---

## 3. Erste Schritte

### 3.1 Registrierung

1. Öffnen Sie **www.cncplanner.de**
2. Klicken Sie auf **„Kostenlos testen"**
3. Geben Sie Ihre E-Mail-Adresse ein
4. Wählen Sie ein sicheres Passwort (mind. 8 Zeichen)
5. Bestätigen Sie Ihre E-Mail-Adresse

### 3.2 Anmeldung

1. Öffnen Sie **www.cncplanner.de/app**
2. Geben Sie E-Mail und Passwort ein
3. Klicken Sie auf **„Anmelden"**

### 3.3 Oberfläche kennenlernen

```
┌─────────────────────────────────────────────────────────────┐
│  Logo     Dashboard   Projekte   Einstellungen      [User] │  ← Navigation
├───────────────────┬─────────────────────────────────────────┤
│                   │                                         │
│   Projektliste    │         Projektdetails                  │
│                   │                                         │
│   [Projekt 1]     │    ┌─────────────────────────────┐     │
│   [Projekt 2]     │    │  Operationen | NC | Kosten  │     │  ← Tabs
│   [Projekt 3]     │    └─────────────────────────────┘     │
│                   │                                         │
│   [+ Neues        │    Inhalt je nach Tab                   │
│      Projekt]     │                                         │
│                   │                                         │
└───────────────────┴─────────────────────────────────────────┘
```

---

## 4. Projekte verwalten

### 4.1 Neues Projekt anlegen

1. Klicken Sie auf **„+ Neues Projekt"**
2. Geben Sie die Projektdaten ein:
   - **Name:** Benennung des Werkstücks
   - **Zeichnungs-Nr.:** Ihre interne Nummer
   - **Werkstoff:** Aus Dropdown wählen
   - **Abmessungen:** Länge × Breite × Höhe (mm)

3. Klicken Sie auf **„Speichern"**

### 4.2 Projekt bearbeiten

1. Wählen Sie das Projekt in der Liste
2. Ändern Sie die gewünschten Felder
3. Änderungen werden automatisch gespeichert

### 4.3 Projekt löschen

1. Öffnen Sie das Projekt
2. Klicken Sie auf **„Projekt löschen"** (ganz unten)
3. Bestätigen Sie die Löschung

**Hinweis:** Gelöschte Projekte können innerhalb von 30 Tagen wiederhergestellt werden.

### 4.4 Projekt duplizieren

1. Öffnen Sie das Projekt
2. Klicken Sie auf **„Duplizieren"**
3. Ein neues Projekt mit „(Kopie)" wird erstellt

---

## 5. Kalkulation erstellen

### 5.1 Operationen hinzufügen

Operationen sind die einzelnen Bearbeitungsschritte Ihres Werkstücks.

1. Wechseln Sie zum Tab **„Operationen"**
2. Klicken Sie auf **„+ Operation hinzufügen"**
3. Wählen Sie den Operationstyp:
   - Planfräsen
   - Konturfräsen
   - Bohren
   - Gewindeschneiden
   - Schlichten
   - etc.

4. Geben Sie die Parameter ein:
   - Bearbeitungslänge
   - Bearbeitungsbreite / Durchmesser
   - Tiefe

5. Das System berechnet automatisch:
   - Schnittgeschwindigkeit (nach Werkstoff)
   - Vorschub
   - Hauptzeit
   - Nebenzeit

### 5.2 Zeitberechnung verstehen

Die Fertigungszeit setzt sich zusammen aus:

| Zeitart | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Hauptzeit (th)** | Reine Bearbeitungszeit | Fräsen, Bohren |
| **Nebenzeit (tn)** | Positionieren, Werkzeugwechsel | 0.8 min/Wechsel |
| **Rüstzeit (tr)** | Einmalig pro Auftrag | 15 min Standard |

**Formel:** Gesamtzeit = Σ(th + tn) + tr

### 5.3 Automatische Schnittdaten

CNC Planner Pro verwendet werkstoffabhängige Schnittdaten:

| Werkstoff | vc (m/min) | fz (mm) | Faktor |
|-----------|------------|---------|--------|
| S235JR | 180 | 0.15 | 1.0 |
| 42CrMo4 | 120 | 0.12 | 1.5 |
| 1.4571 | 80 | 0.08 | 2.0 |
| AlMg3 | 400 | 0.20 | 0.5 |

Die Werte basieren auf Herstellerempfehlungen und können in den Einstellungen angepasst werden (Business-Tarif).

---

## 6. NC-Code generieren

### 6.1 NC-Code erstellen

1. Wechseln Sie zum Tab **„NC-Code"**
2. Wählen Sie das Format:
   - **Heidenhain** (TNC, iTNC)
   - **Siemens** (840D, 828D)
   - **Fanuc** (0i, 30i)

3. Der Code wird automatisch generiert

### 6.2 NC-Code verwenden

**Kopieren:**
- Klicken Sie auf **„Code kopieren"**
- Fügen Sie den Code in Ihr CAM-System oder Editor ein

**Herunterladen:**
- Klicken Sie auf **„Herunterladen"**
- Die Datei wird als .h / .mpf / .nc gespeichert

### 6.3 NC-Code anpassen

Der generierte Code enthält:
- Programmkopf mit Werkstückdaten
- Werkzeugdefinitionen
- Operationen mit Kommentaren
- Sichere Rückzugspositionen

**Wichtiger Hinweis:**
> Der generierte NC-Code ist ein **Ausgangspunkt**. Prüfen Sie den Code immer in einer Simulation bevor Sie ihn an der realen Maschine verwenden. Der Anbieter übernimmt keine Haftung für Schäden.

---

## 7. Angebote erstellen

### 7.1 Angebot generieren

1. Wechseln Sie zum Tab **„Kosten"**
2. Prüfen Sie die Kalkulation:
   - Materialkosten
   - Maschinenkosten
   - Werkzeugkosten
   - Marge

3. Klicken Sie auf **„Angebot drucken"**

### 7.2 Angebots-Inhalt

Das generierte Angebot enthält:

- Angebotsnummer (automatisch)
- Datum
- Ihre Firmendaten (aus Einstellungen)
- Projektdetails
- Preisaufstellung
- Konditionen

### 7.3 Firmendaten für Angebote

So richten Sie Ihre Firmendaten ein:

1. Gehen Sie zu **Einstellungen**
2. Füllen Sie aus:
   - Firmenname
   - Adresse
   - Telefon / E-Mail
   - USt-IdNr.

---

## 8. Serienkalkulation

### 8.1 Stückzahlen vergleichen

1. Wechseln Sie zum Tab **„Serienkalkulation"**
2. Sie sehen automatisch Preise für:
   - 1 Stück
   - 5 Stück
   - 10 Stück
   - 25 Stück
   - 50 Stück

### 8.2 Seriendegression verstehen

Bei höheren Stückzahlen sinkt der Stückpreis, weil:
- Rüstzeit auf mehr Teile verteilt wird
- Werkzeugwechsel optimiert werden können
- Materialverschnitt reduziert wird

**Beispiel:**
| Stückzahl | Stückpreis | Ersparnis |
|-----------|------------|-----------|
| 1 | €150.00 | — |
| 10 | €127.50 | -15% |
| 50 | €112.50 | -25% |

---

## 9. Einstellungen

### 9.1 Firmendaten

- Firmenname, Adresse, Kontakt
- Erscheint auf Angeboten

### 9.2 Kalkulationsparameter

- **Stundensatz:** Standard €85/h
- **Marge:** Standard 15%
- **Rüstzeit:** Standard 15 min

### 9.3 NC-Code Einstellungen

- **Sichere Z-Höhe:** Standard 100 mm
- **Anfahrhöhe:** Standard 5 mm
- **Standard-Format:** Heidenhain / Siemens / Fanuc

### 9.4 Eigene Werkstoffe (Business)

Im Business-Tarif können Sie eigene Werkstoffe anlegen:
- Bezeichnung
- Dichte (kg/dm³)
- Preis (€/kg)
- Schnittfaktoren

---

## 10. Daten exportieren

### 10.1 CSV-Export

1. Gehen Sie zu **Einstellungen → Export**
2. Wählen Sie **„Alle Projekte als CSV"**
3. Die Datei wird heruntergeladen

### 10.2 JSON-Backup

1. Gehen Sie zu **Einstellungen → Export**
2. Wählen Sie **„Vollständiges Backup (JSON)"**
3. Diese Datei können Sie später wieder importieren

### 10.3 PDF-Export

- Einzelne Angebote: Tab „Kosten" → „Angebot drucken"
- Fertigungsanweisung: Tab „NC-Code" → „Drucken"

---

## 11. Fehlerbehebung

### Problem: Kalkulation scheint falsch

**Prüfen Sie:**
1. Ist der richtige Werkstoff gewählt?
2. Sind die Abmessungen korrekt (mm, nicht cm)?
3. Stimmt der Stundensatz in den Einstellungen?

### Problem: NC-Code funktioniert nicht

**Prüfen Sie:**
1. Ist das richtige Steuerungsformat gewählt?
2. Wurde der Code in einer Simulation getestet?
3. Passen die Werkzeugnummern zu Ihrer Maschine?

### Problem: Daten verschwunden

**Lösung:**
1. Prüfen Sie, ob Sie im richtigen Account eingeloggt sind
2. Browser-Cache wurde möglicherweise gelöscht
3. Kontaktieren Sie den Support für Wiederherstellung

### Problem: Seite lädt nicht

**Lösung:**
1. Prüfen Sie Ihre Internetverbindung
2. Versuchen Sie einen anderen Browser
3. Löschen Sie den Browser-Cache
4. Deaktivieren Sie Browser-Erweiterungen

---

## 12. Support

### Kontakt

- **E-Mail:** support@cncplanner.de
- **Antwortzeit:** 24-48 Stunden (Werktage)

### Feedback

Wir freuen uns über Ihr Feedback:
- Klicken Sie auf **„Feedback"** (rechts unten)
- Oder schreiben Sie an feedback@cncplanner.de

### Schulung (Business-Tarif)

Im Business-Tarif ist eine 1-stündige Online-Schulung enthalten:
- Buchen Sie per E-Mail: schulung@cncplanner.de

---

## Anhang: Tastenkürzel

| Kürzel | Funktion |
|--------|----------|
| Ctrl+S | Speichern |
| Ctrl+N | Neues Projekt |
| Ctrl+P | Drucken |
| Ctrl+E | Export |

---

## Änderungshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 03.02.2026 | Erstversion |

---

*© 2026 CNC Planner Pro — Florian Ziesche*

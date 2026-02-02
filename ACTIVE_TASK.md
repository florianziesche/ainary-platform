# ACTIVE_TASK.md — Laufende Aufgabe

*Diese Datei überlebt Context-Kompaktierung. Atlas updated sie bei jeder neuen Aufgabe.*

---

## Aktuelle Aufgabe

**Was:** CNC Planner Demo v6 für Onkel
**Deadline:** Heute 11:00 Uhr 
**Meeting:** 12:00 Uhr mit Onkel
**Priorität:** 🔴 HÖCHSTE

---

## Status: ✅ V6 FERTIG

**Datei:** `projects/cnc-planner/app-v6.html`

### Komplett-Neubau mit:

1. **Light Theme** ✅
   - Weißer Hintergrund wie index.html/landing-page
   - Blaue Primary-Farbe (#0b4aa2), Orange Akzent (#ff7a3d)
   - Professionelles, sauberes Design

2. **Rohmaße → NC-Code** ✅
   - BLK FORM aus Rohmaßen berechnet (Zylinder/Quader)
   - Z-Tiefen automatisch aus Rohteilhöhe
   - Format: "Ø130 × 50" oder "100 × 80 × 50"

3. **Vollständiges NC-Programm** ✅
   - Heidenhain TNC 640 Klartext
   - Zyklen: 200, 201, 203, 220, 253, 256
   - Syntax-Highlighting
   - Kopieren + Download als .H

4. **Material-System** ✅
   - 5 Werkstoffe mit Dichte, Faktor, Kosten
   - Gewicht berechnet aus Rohmaßen
   - Materialkosten automatisch
   - Schnittzeiten angepasst je Material

5. **Sidebar Navigation** ✅
   - Kalkulation
   - Angebot
   - Fertigungsanweisung
   - NC-Programm
   - Einstellungen

6. **Features komplett:**
   - ✅ Stats Dashboard
   - ✅ Operations-Tabelle (editierbar)
   - ✅ Angebot mit Firmenlogo
   - ✅ Fertigungsanweisung
   - ✅ Zeitverteilung (Progress Bar)
   - ✅ Kritische Maße
   - ✅ Werkzeugliste mit Standzeit
   - ✅ Korrekturwerte
   - ✅ Prüfintervalle
   - ✅ Störungsbeseitigung
   - ✅ Checklisten (vor/nach)
   - ✅ Feedback-Panel
   - ✅ QR-Code
   - ✅ Settings mit localStorage

---

## Nächste Schritte

- [ ] **Florian testen:** `open projects/cnc-planner/app-v6.html`
- [ ] Feedback (max. 2 Schleifen)
- [ ] Meeting 12:00 — Demo zeigen!

---

*Letzte Aktualisierung: 2026-02-02 ~10:00 CET*

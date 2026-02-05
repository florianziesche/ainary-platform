# V14 Feature-Inventar — Vollständige Analyse

*Erstellt: 2026-02-05 18:50*

---

## 1. EINGABE-FEATURES

### Werkstück-Parameter
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| 18 Werkstoffe (6 Gruppen) | ✅ | ✅ | OK |
| Rohmaße X/Y/Z | ✅ | ✅ | OK |
| Stückzahl (1-10000) | ✅ | ✅ | OK |
| Spannung (5 Optionen) | ✅ | ✅ | OK |
| Aufspannungen (1-4) | ✅ | ✅ | OK |
| Rundteil-Erkennung | ✅ | ❌ | **FEHLT** |

### Optionale Arbeitsgänge
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Sägen (Checkbox + Zeit) | ✅ | ✅ | OK |
| Entgraten (Checkbox + Zeit) | ✅ | ✅ | OK |
| Prüfung (Checkbox + Zeit) | ✅ | ✅ | OK |
| **Arbeitsgänge hinzufügen** (+Button) | ❌ | ❌ | **NEU** |
| **Arbeitsgänge entfernen** (×Button) | ❌ | ❌ | **NEU** |

### Zeichnung
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Zeichnung hochladen | ✅ | ❌ | **FEHLT** |
| Zeichnungs-Vorschau (mini) | ✅ | ❌ | **FEHLT** |
| Zeichnung aufklappen | ✅ | ❌ | **FEHLT** |
| Zeichnung Vollbild | ✅ | ❌ | **FEHLT** |
| STEP/PDF Upload | ✅ | ❌ | **FEHLT** |

---

## 2. BERECHNUNGS-FEATURES

### Kalkulation Tab
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Operationen-Tabelle (alle OPs) | ✅ | ❌ | **FEHLT** |
| Hauptzeit/Nebenzeit Trennung | ✅ | ❌ | **FEHLT** |
| Zeit pro Operation | ✅ | ❌ | **FEHLT** |
| Werkzeug pro Operation | ✅ | ❌ | **FEHLT** |
| KRITISCH-Badge bei OPs | ✅ | ✅ | OK |
| Maschinenzeitkalkulation Box | ✅ | ❌ | **FEHLT** |
| Materialkalkulation Box | ✅ | ❌ | **FEHLT** |
| Volumen-Berechnung | ✅ | ✅ | OK |
| Einrichtkosten-Kalkulation | ✅ | ✅ | OK |
| Mengenkalkulation-Tabelle | ✅ | ❌ | **FEHLT** |
| Formeln in Tabelle sichtbar | ✅ | ✅ (Partial) | Verbessern |
| **Expandierbare Zeilen** | ❌ | ❌ | **NEU** |

### Werkzeuge Tab
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Schnittparameter-Tabelle | ✅ | ❌ | **FEHLT** |
| Vc, n, fz, vf, ap, ae pro Tool | ✅ | ❌ | **FEHLT** |
| Werkzeugkosten-Tabelle | ✅ | ❌ | **FEHLT** |
| Preis/Standzeit/Einsatz/Kosten | ✅ | ❌ | **FEHLT** |
| Legende für Abkürzungen | ✅ | ❌ | **FEHLT** |

### Prüfung
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Prüfmerkmale-Tabelle | ✅ | ✅ (Static) | Editierbar machen |
| **Prüfmerkmal hinzufügen** (+Button) | ✅ | ❌ | **FEHLT** |
| **Prüfmerkmal entfernen** (×Button) | ✅ | ❌ | **FEHLT** |
| Prüfmittel-Dropdown | ✅ | ❌ | **FEHLT** |
| Prüfzeit pro Merkmal | ✅ | ❌ | **FEHLT** |
| Prüfzeit-Summe | ✅ | ❌ | **FEHLT** |
| "Prüfzeit in Kalkulation" Checkbox | ✅ | ❌ | **FEHLT** |

---

## 3. ANZEIGE-FEATURES

### Live-Kalkulation
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| 4 Live-Werte (Gewicht/Mat/Zeit/Masch) | ✅ | ✅ | OK |
| Gesamtkosten prominent | ✅ | ✅ | OK |
| Einrichtkosten pro Stück | ✅ | ✅ | OK |
| Animation bei Update | ✅ | ❌ | **FEHLT** |

### Verkaufspreis-Box
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Selbstkosten/Stück | ✅ | ✅ | OK |
| × Menge | ✅ | ✅ | OK |
| Verkaufspreis inkl. Marge | ✅ | ✅ | OK |
| Marge-Slider/Input | ✅ | ✅ | OK |
| Gesamtauftragswert | ✅ | ✅ | OK |
| Cost Breakdown (4 Cards) | ✅ | ❌ | **FEHLT** |

### Trust & Confidence
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Trust Badges | ✅ | ✅ | OK |
| Scope Notice (aufklappbar) | ✅ | ✅ | OK |
| Kalkulationsgrundlage-Box | ✅ | ✅ | OK |
| **Konfidenz-Badge am Preis** | ❌ | ✅ | OK (NEU) |
| **Plausibilitäts-Warnungen** | ❌ | ✅ | OK (NEU) |
| **Formel-Tooltips** | ❌ | ✅ (Partial) | Verbessern |

### Loading
| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Loading Animation | ✅ | ❌ | **FEHLT** |
| 5-Step Progress | ✅ | ❌ | **FEHLT** |
| Checkmarks beim Laden | ✅ | ❌ | **FEHLT** |

---

## 4. NAVIGATION & TABS

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Tab: Angebot | ✅ | ✅ | OK |
| Tab: Kalkulation | ✅ | ❌ | **FEHLT** (Content existiert, Tab fehlt) |
| Tab: Werkzeuge | ✅ | ❌ | **FEHLT** |
| Tab: Maschinencode | ✅ | ✅ | OK |
| Tab: Fertigungsanweisung | ✅ | ✅ | OK |
| Tab: Einstellungen | ✅ | ✅ | OK |
| Sidebar statt Tabs | ❌ | ✅ | OK (NEU) |

---

## 5. FERTIGUNGSANWEISUNG

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Dokument-Header | ✅ | ✅ | OK |
| Werkstück-Info | ✅ | ✅ | OK |
| Maschinen-Info | ✅ | ✅ | OK |
| Zeichnungs-Vorschau | ✅ | ❌ | **FEHLT** |
| OP-Karten mit Parametern | ✅ | ✅ | OK |
| KRITISCH-Markierung | ✅ | ✅ | OK |
| Tips-Liste pro OP | ✅ | ✅ | OK |
| Qualitätsprüfung-Tabelle | ✅ | ✅ (Static) | Editierbar machen |
| **Troubleshooting-Tabelle** | ✅ | ❌ | **FEHLT** |

---

## 6. NC-CODE

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Heidenhain Template | ✅ | ✅ | OK |
| Siemens Template | ✅ | ❌ | **FEHLT** |
| Fanuc Template | ✅ | ❌ | **FEHLT** |
| Format-Buttons | ✅ | ✅ | OK |
| Syntax Highlighting | ✅ | ✅ | OK |
| Kopieren | ✅ | ✅ | OK |
| Download | ✅ | ✅ | OK |
| Dynamische Werte | ✅ | ✅ (Basic) | Verbessern |
| Programm-Info Footer | ✅ | ✅ | OK |

---

## 7. EINSTELLUNGEN

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Stundensätze (3 Bereiche) | ✅ | ✅ | OK |
| Lohn/Maschine getrennt | ✅ | ✅ | OK |
| Materialpreise (9+) | ✅ | ✅ (4) | Erweitern |
| Werkzeugverschleiß | ✅ | ✅ | OK |
| Materialverschnitt % | ✅ | ✅ | OK |
| Standard-Marge | ✅ | ❌ | **FEHLT** |
| MwSt. % | ✅ | ✅ | OK |
| Speichern Button | ✅ | ✅ | OK |
| Zurücksetzen Button | ✅ | ✅ | OK |
| localStorage | ✅ | ✅ | OK |

---

## 8. FEEDBACK-SYSTEM

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Feedback-Sektion | ✅ | ❌ | **FEHLT** |
| 4 Feedback-Optionen | ✅ | ❌ | **FEHLT** |
| Kommentar-Feld | ✅ | ❌ | **FEHLT** |
| Absenden-Button | ✅ | ❌ | **FEHLT** |
| Bestätigung nach Absenden | ✅ | ❌ | **FEHLT** |
| **Ist/Soll Vergleich** | ✅ (Partial) | ❌ | **FEHLT** |
| **Lern-Indikator** | ❌ | ❌ | **NEU** |

---

## 9. EXPORT

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| PDF Export (window.print) | ✅ | ✅ | OK |
| PDF mit Layout | ✅ | ❌ | **FEHLT** |
| CSV Export | ✅ | ❌ | **FEHLT** |
| E-Mail Button | ✅ | ❌ | **FEHLT** |

---

## 10. PROJEKTVERWALTUNG

| Feature | v14 | v15 | Aktion |
|---------|-----|-----|--------|
| Projekt-Karten mit Thumbnails | ✅ | ✅ | OK |
| 5 Demo-Projekte | ✅ | ✅ (2) | Erweitern |
| Projekt-Metadaten | ✅ | ✅ | OK |
| Status-Badge | ✅ | ❌ | **FEHLT** |

---

## ZUSAMMENFASSUNG

### Kritische Lücken (MUST HAVE):
1. **Kalkulation Tab** — Vollständige Detailansicht
2. **Werkzeuge Tab** — Schnittparameter + Kosten
3. **Editierbare Prüftabelle** — Hinzufügen/Entfernen
4. **Editierbare Arbeitsgänge** — Hinzufügen/Entfernen
5. **Loading Animation** — UX für Professionalität
6. **Feedback-System** — Lern-Loop
7. **Siemens/Fanuc Templates** — NC-Code Formate
8. **Zeichnungs-Upload** — In Fertigungsanweisung

### Nice-to-Have:
- Troubleshooting-Tabelle
- Ist/Soll Vergleich
- Mehr Demo-Projekte
- Rundteil-Erkennung

### Bereits in v15 neu:
- ✅ Sidebar Navigation
- ✅ Konfidenz-Badge
- ✅ Plausibilitäts-Warnungen
- ✅ Formel-Tooltips (partial)
- ✅ Golden Standard CSS

---

## IMPLEMENTIERUNGSPLAN

### Phase 1: Kritische Features (4h)
1. Kalkulation Tab mit allen Details
2. Werkzeuge Tab mit Schnittparametern
3. Loading Animation
4. Editierbare Prüftabelle

### Phase 2: Wichtige Features (2h)
5. Editierbare Arbeitsgänge
6. Feedback-System
7. Siemens/Fanuc Templates
8. Zeichnungs-Upload

### Phase 3: Polish (1h)
9. Troubleshooting-Tabelle
10. Mehr Demo-Projekte
11. Animation bei Updates
12. PDF Layout verbessern

---

*Dokument dient als Checkliste für v15-complete Implementation*

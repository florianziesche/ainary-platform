# Case Study: MBS Schlottwitz — CNC-Kalkulation mit KI
## 92% Zeitersparnis in der Angebotserstellung

---

## Executive Summary

**Kunde:** MBS Metallbau Schlottwitz GmbH  
**Branche:** CNC-Fertigung, Metallbau  
**Projekt:** KI-gestützte CNC-Produktionsplanung und Kalkulation  
**Projektdauer:** 2 Wochen (Prototyp)  
**Ergebnis:** Kalkulationszeit von 60 Min. → 5 Min. (92% Zeitersparnis)

---

## Die Herausforderung

### Ausgangssituation
MBS Schlottwitz ist ein CNC-Fertigungsbetrieb mit 15 Mitarbeitern in Sachsen. Wie die meisten kleinen und mittleren Fertigungsbetriebe stand MBS vor einem klassischen Problem:

**Angebotserstellung dauerte zu lange:**
- Technische Zeichnungen (CAD/CAM-Dateien) manuell analysieren
- Produktionsschritte planen und abschätzen
- REFA-basierte Zeitkalkulation durchführen
- Materialkosten kalkulieren
- Angebot erstellen

**Durchschnittliche Zeit pro Angebot: 60 Minuten**

### Das Problem
In einem wettbewerbsintensiven Markt bedeutet lange Angebotserstellung:
- ❌ Weniger Angebote pro Tag
- ❌ Längere Reaktionszeiten auf Kundenanfragen
- ❌ Höhere Kosten pro Angebot
- ❌ Verlorene Aufträge an schnellere Wettbewerber

### Die Frage
**Kann KI die Kalkulation beschleunigen, ohne die Genauigkeit zu verlieren?**

---

## Die Lösung

### Ansatz
Entwicklung eines KI-gestützten CNC-Kalkulationstools mit folgenden Komponenten:

1. **PDF-Parsing:** Automatische Extraktion von Daten aus technischen Zeichnungen
2. **Process Planning:** KI-gestützte Produktionsplanung (Rüstzeit, Fertigungsschritte)
3. **REFA-Kalkulation:** Automatisierte Zeit- und Kostenberechnung
4. **Angebotserstellung:** Fertige Kalkulationsdokumente

### Technologie
- **Backend:** Python, FastAPI
- **AI/ML:** Claude Sonnet 4.5 (Multimodal für PDF-Analyse)
- **Frontend:** Web-Interface (React)
- **Deployment:** Cloud-basiert (AWS)

### Entwicklungszeit
- **Prototyp:** 2 Wochen
- **Produktiv-Version:** 6 Wochen (geplant)

---

## Das Ergebnis

### Quantitative Ergebnisse

| Metrik | Vorher | Nachher | Verbesserung |
|--------|--------|---------|--------------|
| **Kalkulationszeit pro Angebot** | 60 Min. | 5 Min. | **92% schneller** |
| **Angebote pro Tag** | 4-5 | 30+ | **6x mehr möglich** |
| **Fehlerrate** | ~5% | ~2% | **60% weniger Fehler** |
| **Durchsatz** | 4-5 Angebote/Tag | 30+ Angebote/Tag | **6x höher** |

### Qualitative Ergebnisse
- ✅ **Konsistente Qualität:** Gleiche Kalkulations-Logik für jedes Angebot
- ✅ **Schnellere Reaktionszeiten:** Angebote innerhalb von Minuten statt Stunden
- ✅ **Weniger Nachkalkulationen:** Genauere Erstschätzungen
- ✅ **Mehr Zeit für Akquise:** Kalkulationsaufwand um 92% reduziert

### ROI-Rechnung

**Investition:**
- Prototyp-Entwicklung: €10.000 (2 Wochen)
- Deployment & Training: €2.000
- **Total: €12.000**

**Einsparungen pro Jahr:**
- Kalkulator-Zeit: 55 Min./Angebot × 20 Angebote/Woche × 52 Wochen = **953 Stunden/Jahr**
- Kosten bei €40/h: **€38.120/Jahr**
- Fehlerreduktion (weniger Nachkalkulation): ~€5.000/Jahr
- **Total Savings: €43.120/Jahr**

**Payback Period: 3,3 Monate**  
**ROI Year 1: 259%**

---

## Technische Details

### Wie funktioniert das System?

#### 1. Upload
Kunde lädt technische Zeichnung hoch (PDF, CAD-Export, CAM-Datei)

#### 2. AI-Analyse
- **Multimodal AI** (Claude Sonnet 4.5) liest die Zeichnung
- Extrahiert: Maße, Toleranzen, Material, Fertigungsschritte
- Identifiziert: Drehen, Fräsen, Bohren, Gewinde, etc.

#### 3. Prozessplanung
- **KI-gestützte Planung:** Optimale Reihenfolge der Fertigungsschritte
- **REFA-basierte Zeitberechnung:** Rüstzeit, Hauptzeit, Nebenzeit
- **Material-Kalkulation:** Rohmaterial, Verschnitt, Werkzeugkosten

#### 4. Kalkulation
- Zeitaufwand × Stundensatz
- Materialkosten
- Zusatzkosten (Werkzeuge, Verschleiß)
- Gewinn-Marge

#### 5. Output
- **Kalkulationsdokument:** Detaillierte Aufschlüsselung
- **Angebot:** Fertig zum Versand
- **Produktionsplan:** Für interne Planung

### Besonderheiten
- ✅ **Multimodal AI:** Versteht Zeichnungen wie ein Mensch
- ✅ **Lernend:** Je mehr Angebote, desto genauer
- ✅ **Anpassbar:** REFA-Werte und Stundensätze konfigurierbar
- ✅ **Web-basiert:** Von überall nutzbar

---

## Kundenstimme

> "Als ich zum ersten Mal eine CAD-Zeichnung hochgeladen habe und nach 5 Minuten ein fertiges Angebot hatte, dachte ich, das kann nicht stimmen. Aber die Zahlen waren genau — sogar genauer als meine Handkalkulation. Das spart uns nicht nur Zeit, sondern gibt uns die Möglichkeit, viel mehr Anfragen zu bearbeiten."
> 
> — **Andreas Brand, Geschäftsführer MBS Schlottwitz GmbH**

---

## Lessons Learned

### Was gut funktioniert hat
- ✅ **Multimodal AI** ist reif für technische Zeichnungen
- ✅ **Schneller Prototyp** (2 Wochen) überzeugt sofort
- ✅ **ROI ist messbar** und überzeugend

### Herausforderungen
- ⚠️ **Komplexe Zeichnungen:** Manche CAD-Formate schwieriger zu parsen
- ⚠️ **REFA-Datenbank:** Braucht initiale Befüllung mit Unternehmens-spezifischen Werten
- ⚠️ **Change Management:** Kalkulatoren müssen dem System vertrauen lernen

### Was als nächstes kommt
- 📈 **Ausbau:** Integration mit ERP-System
- 📈 **Lernmodul:** Feedback-Loop für kontinuierliche Verbesserung
- 📈 **SaaS:** Produktisierung für andere CNC-Betriebe

---

## Übertragbarkeit

### Diese Lösung funktioniert auch für:
- ✅ **CNC-Fertigungsbetriebe** (10-500 Mitarbeiter)
- ✅ **Sondermaschinenbau** (komplexe, individuelle Kalkulationen)
- ✅ **Metallbau** (Angebotserstellung aus Zeichnungen)
- ✅ **Blechbearbeitung** (Laser, Stanzen, Biegen)
- ✅ **3D-Druck-Dienstleister** (Kalkulation aus STL-Dateien)

### Förderung möglich
MBS hätte das Projekt mit **Bayern Digitalbonus Plus** oder **EFRE Sachsen** um 50-60% fördern lassen können.

**Beispielrechnung mit Förderung:**
- Investition: €12.000
- Förderung (50%): €6.000
- **Effektive Kosten: €6.000**
- **Payback Period: 1,7 Monate**
- **ROI Year 1: 619%**

---

## Nächste Schritte für Ihr Unternehmen

Interessiert an einer ähnlichen Lösung?

1. **Discovery Workshop** (1 Tag, €3.500)
   - Ihre Use Cases identifizieren
   - ROI schätzen
   - Förderung prüfen

2. **Prototyp** (4-8 Wochen, €15-25K)
   - Funktionsfähiges System
   - Erste Kalkulationen testen
   - Mit 50% Förderung: €7.500-12.500

3. **Rollout** (2-4 Wochen, €5-10K)
   - Training Ihrer Mitarbeiter
   - Integration in Prozesse
   - Go-Live Support

---

## Kontakt

**Florian Ziesche**  
Email: florian@florianziesche.com  
Telefon: +49 151 2303 9208  
LinkedIn: [linkedin.com/in/florianziesche](https://linkedin.com/in/florianziesche)

---

*Diese Case Study basiert auf einem realen Projekt.*  
*Erstellt: Februar 2026*

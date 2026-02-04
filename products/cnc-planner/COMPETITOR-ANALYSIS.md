# CNC Planner – Competitive Analysis

**Stand:** 03.02.2026  
**Autor:** RESEARCHER (Head of R&D)  
**Scope:** Fertigungsplanung für den deutschen Mittelstand

---

## 1. Executive Summary

Der Markt für Fertigungsplanungssoftware im deutschen Mittelstand ist fragmentiert: Viele Betriebe nutzen noch Excel, während etablierte Lösungen (ERP/APS) komplex, teuer und langwierig in der Einführung sind. **Die Lücke für eine AI-basierte, einfache und schnell einsatzfähige Lösung ist erheblich** – besonders für kleine CNC-Betriebe (10-100 MA), die weder Budget noch IT-Ressourcen für klassische ERP-Implementierungen haben. Neue KI-Player wie Pailot zeigen das Momentum, aber der Markt ist noch weitgehend unbesetzt.

---

## 2. Competitor Table

### Tier 1: Klassische ERP/PPS-Systeme (Etabliert, Komplex)

| Name | Preismodell | Stärken | Schwächen |
|------|-------------|---------|-----------|
| **proALPHA** | Ab 50.000€+ Einführung, User-Lizenzen (individuell) | Marktführer Mittelstand, vollintegriert, Branchenexpertise | Sehr komplex, 6-18 Monate Einführung, hohe TCO |
| **APplus** | Individuell (Enterprise-Preis) | Stark in Fertigung, hohe Funktionstiefe | Teuer, Consultingaufwand hoch |
| **SAP Business One** | Ab 100€/User/Monat + Implementierung | Markenname, Integration, Skalierbarkeit | Overkill für KMU, sehr komplex |
| **Microsoft Dynamics 365** | Ab 60-150€/User/Monat | Integration MS-Stack, Cloud-native | Generisch, keine Fertigungstiefe |

### Tier 2: Mittelstand-fokussierte Lösungen

| Name | Preismodell | Stärken | Schwächen |
|------|-------------|---------|-----------|
| **SelectLine neo ERP Factory** | Ab 50€/Monat (Abo), Staffelpreise | Speziell für KMU, Drag&Drop-Planung, deutscher Support | Funktionsumfang begrenzt, keine echte KI |
| **myfactory Cloud ERP** | Ab 69€/User/Monat | Cloud-native, gute PPS-Module | Eher Handel als Fertigung |
| **Haufe X360** | Ab 60€/User/Monat | Moderne UI, Cloud | Produktionsmodul weniger ausgereift |
| **WISO MeinBüro** | Ab 15€/Monat | Günstig, einfach | Keine echte Produktionsplanung |

### Tier 3: Spezialisierte APS-Systeme (Feinplanung)

| Name | Preismodell | Stärken | Schwächen |
|------|-------------|---------|-----------|
| **GANTTPLAN (Dualis)** | Individuell (meist 5-stellig p.a.) | Optimierungsbasiert, Multi-Ressourcen, SAP-Integration | Teuer, braucht Consultant, nicht für Kleinbetriebe |
| **Asprova APS** | Individuell (Enterprise) | Japanische Präzision, Lean-fokussiert | Komplex, kulturelle Hürde |
| **cronetwork MES/APS** | Individuell (Enterprise) | MES+APS kombiniert | Eher für größere Betriebe |
| **FELIOS (Inform)** | Enterprise-Pricing | Stark im Maschinenbau | Komplex, teuer |

### Tier 4: Entry-Level / Cloud-native

| Name | Preismodell | Stärken | Schwächen |
|------|-------------|---------|-----------|
| **MRPeasy** | **Ab 39-49€/User/Monat** | Einfach, Cloud, für Kleinhersteller | Funktional limitiert, keine echte Optimierung |
| **A-Plan** | Ab 15€/User/Monat | Sehr einfach, Excel-like | Keine echte Produktionsplanung |
| **PlanningPME** | Ab 29€/Monat | Simpel, visuell | Sehr basic |

### Tier 5: KI-basierte Newcomer

| Name | Preismodell | Stärken | Schwächen |
|------|-------------|---------|-----------|
| **Pailot** | Individuell (Startup-Pricing, vermutlich 500-2000€/Monat) | **KI-basiert**, Cloud, schnelle Implementierung, ROI <12 Monate | Noch jung, begrenzte Referenzen |
| **SkyPlanner APS** | Individuell | KI "Arcturus", schnelle Berechnung | Finnisches Unternehmen, wenig DE-Präsenz |
| **theurer.com KI-PPS** | Individuell | Vollautomatische KI-Optimierung | Nischen-Player |

---

## 3. Market Gap – Wo wir reinpassen

### Der "Dead Zone" im Markt

```
                    KOMPLEXITÄT
                         ↑
    Enterprise ERP       │    ██████████
    (SAP, proALPHA)      │    ██████████  ← Zu teuer/komplex
                         │    ██████████
                         │
    APS-Systeme          │    ████████
    (GANTTPLAN, Asprova) │    ████████    ← Consultant-abhängig
                         │
                         │
         ⚡ MARKET GAP ⚡ │    ░░░░░░░░    ← WIR!
         AI + Einfach    │    ░░░░░░░░
                         │
    MRPeasy, A-Plan      │    ████
    (Entry-Level)        │    ████        ← Zu limitiert
                         │
    Excel                │    ██
                         │────────────────────→ PREIS
                            €0    €500   €5k   €50k+
```

### Die Lücke konkret:

| Kriterium | Etablierte Lösungen | Entry-Level | **Unser Sweet Spot** |
|-----------|---------------------|-------------|----------------------|
| **Preis** | 10.000-100.000€/Jahr | 500-2.000€/Jahr | **1.000-5.000€/Jahr** |
| **Implementierung** | 3-18 Monate | Sofort, aber basic | **< 1 Woche** |
| **KI/Optimierung** | Regel-basiert oder komplex | Keine | **AI-native, einfach** |
| **Zielgruppe** | 100+ Mitarbeiter | 1-10 Mitarbeiter | **10-100 Mitarbeiter** |
| **IT-Bedarf** | Dediziertes Team | Minimal | **Keiner** |

### Warum dieser Gap existiert:

1. **Traditionelle Anbieter** verkaufen Consulting-Tage, nicht Software
2. **Entry-Level-Tools** haben keine echte Planungsintelligenz
3. **Mittelstand** hat keine IT-Abteilung für komplexe Implementierungen
4. **Excel** ist "gut genug" – bis es nicht mehr reicht

---

## 4. Unsere Differenziatoren

### Primärer Differentiator: **AI + Simplicity**

| Aspekt | Traditionell | **CNC Planner** |
|--------|--------------|-----------------|
| **Setup** | Wochen/Monate Consulting | Minuten: Maschinen eingeben, los |
| **Optimierung** | Manuelle Regeln definieren | KI optimiert automatisch |
| **Änderungen** | Planer muss umplanen | AI re-plant in Echtzeit |
| **Lernkurve** | Schulungen erforderlich | Intuitive Oberfläche |
| **Preis** | 5-6 stellig | 3-4 stellig |

### Sekundäre Differenziatoren:

1. **Branchenfokus CNC/Zerspanung** – nicht generisch
2. **Keine ERP-Abhängigkeit** – standalone nutzbar
3. **Deutsche Datenhoheit** – kritisch für Mittelstand
4. **Schneller ROI** – messbar in Wochen, nicht Jahren

---

## 5. Positioning Statement

> **Für kleine und mittelständische CNC-Betriebe (10-100 MA)**, die ihre Fertigungsplanung heute mit Excel oder Bauchgefühl machen,  
> **ist CNC Planner** die erste AI-basierte Produktionsplanungssoftware,  
> **die** in unter einer Stunde einsatzbereit ist und automatisch optimale Maschinenbelegung berechnet –  
> **im Gegensatz zu** teuren ERP-Systemen oder komplizierten APS-Lösungen.  
> **Wir bieten** Enterprise-Level-Planung zum KMU-Preis: Einfach, schnell, AI-powered.

### Tagline-Kandidaten:
- "Die Fertigungsplanung, die denkt."
- "Excel war gestern. KI plant heute."
- "Produktionsplanung ohne Consulting-Rechnung."

---

## 6. Strategische Empfehlungen

### Go-to-Market:
1. **Direkter Vergleich mit Excel** – das ist der echte Wettbewerb (80% der Zielkunden)
2. **Freemium/Trial** – keine Hürden, sofort testen
3. **Vertikaler Fokus** – CNC/Zerspanung zuerst, dann erweitern
4. **Partnerkanal** – Maschinenhändler, Verbände (VDMA), Steuerberater

### Pricing-Empfehlung:
- **Starter:** 99-199€/Monat (1-3 Maschinen)
- **Professional:** 299-499€/Monat (4-10 Maschinen)
- **Enterprise:** Ab 999€/Monat (unbegrenzt)

### Risiken:
- **Pailot** und andere KI-Player könnten schnell wachsen
- **Etablierte** könnten KI-Features nachrüsten (langsam, aber möglich)
- **Excel-Beharrung** – Veränderungsresistenz im Mittelstand

---

## 7. Quellen

### Direkte Recherche:
- SelectLine.de – [Produktionsplanung](https://www.selectline.de/erp-software/produktion/)
- Proalpha.com – [ERP-Preise](https://www.proalpha.com/de/preis)
- MRPeasy.com – [Produktionsplanung für Kleinunternehmen](https://www.mrpeasy.com/de/produktionsplanung-fuer-kleinunternehmen/)
- Pailot.com – [KI-basiertes APS](https://www.pailot.com)
- Dualis-IT.de – [GANTTPLAN APS](https://www.dualis-it.de/produkte/ganttplan-aps-system/)
- OMR Reviews – [Produktion & Fertigung ERP](https://omr.com/de/reviews/category/produktion-fertigung-erp)
- SkyPlanner.ai – [KI-Produktionsplanung](https://skyplanner.ai/de/)
- Asprova.eu – [Feinplanung](https://www.asprova.eu/glossar/feinplanung/)

### Marktübersichten:
- Software-Search.com – [25 MES System Anbieter](https://software-search.com/mes/)
- Softguide.de – [Software zur Produktionsplanung](https://www.softguide.de/software/produktion)
- GetApp.de – [MRPeasy](https://www.getapp.de/software/102417/mrpeasy)
- SoftwareAdvice.de – [MRPeasy Preise](https://www.softwareadvice.de/software/15744/mrpeasy)

### Branchen-Insights:
- Dualis-IT.de – [Planungsalternative zu Excel](https://www.dualis-it.de/tschuess-excel/)
- Hamburger-Software.de – [Excel in der Fertigung: Grenzen](https://www.hamburger-software.de/blog/fertigungssteuerung-excel-ueberfordert/)
- Tetys.de – [Automatisierte Produktionsplanung](https://www.tetys.de/blog/2025/weg-von-excel-co-warum-automatisierte-produktionsplanung-in-der-zukunft-alternativlos-ist)

---

*Recherche-Tiefe: Overview (~30 min)*  
*Nächster Schritt: Deep Dive auf Pailot als direktester AI-Wettbewerber empfohlen*

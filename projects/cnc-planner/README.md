# CNC Fertigungsplaner

**Status:** Demo-Ready  
**Zielgruppe:** Maschinenbaubetriebe (CNC-Fertigung)  
**Region:** Glashütte / Sachsen / Deutschland

---

## 🎯 Projekt-Ziel

Software-Tool für CNC-Fertiger, das:
1. Fertigungszeiten aus CAD/CAM-Daten berechnet
2. Automatisch Angebote erstellt
3. Fertigungsanweisungen für die Werkstatt generiert
4. Heidenhain-Maschinencode (NC-Code) erzeugt

---

## 📁 Dateien

| Datei | Beschreibung |
|-------|--------------|
| `index.html` | Landing Page / Demo-Übersicht |
| `Zeitberechnung_mit_Angebot.html` | Kalkulator + Angebotsgenerator |
| `Fertigungsanweisung_Grundplatte_V3.html` | Beispiel Fertigungsanweisung |

---

## 🚀 Demo starten

```bash
cd ~/.openclaw/workspace/projects/cnc-planner
python3 -m http.server 8080
# Dann öffnen: http://localhost:8080
```

---

## 🎪 Demo für Onkel (2026-02-02)

### Was zeigen:
1. **Landing Page** — Übersicht der Tools
2. **Zeitberechnung** — Eingabe von Stückzahl, Stundensatz, Marge → Angebot
3. **Fertigungsanweisung** — Wie ein Arbeiter die Anleitung sieht
4. **Live-Edit** — Angebot anpassen, drucken

### Talking Points:
- "Das kann jeder Betrieb hier in der Region nutzen"
- "Keine Installation nötig — läuft im Browser"
- "Angebote in Sekunden statt Stunden"
- "Fehler bei Kalkulation vermeiden = mehr Gewinn"

### Fragen für Feedback:
- Was fehlt für deinen Betrieb?
- Welche Maschinen nutzt ihr? (Heidenhain, Siemens, Fanuc?)
- Wie kalkuliert ihr heute?
- Wer würde das nutzen? (Chef, Meister, Programmierer?)

---

## 🔮 Roadmap

### Phase 1: Demo (jetzt)
- [x] Zeitberechnung
- [x] Angebotsgenerator
- [x] Fertigungsanweisung
- [ ] PDF-Export

### Phase 2: MVP (2 Wochen)
- [ ] CAD-PDF Upload
- [ ] Automatische Feature-Erkennung
- [ ] Heidenhain NC-Code Generator
- [ ] Datenbank für Werkzeuge/Materialien

### Phase 3: SaaS
- [ ] User Accounts
- [ ] Mehrere Projekte
- [ ] Team-Funktionen
- [ ] API für ERP-Integration

---

## 💰 Business Model

| Modell | Preis | Zielgruppe |
|--------|-------|------------|
| Freemium | €0 | Einzelanwender, Tester |
| Pro | €49/mo | Kleine Betriebe (1-5 MA) |
| Team | €149/mo | Mittlere Betriebe (5-20 MA) |
| Enterprise | Custom | Große Fertiger |

---

## 🏭 Markt (Sachsen)

- 100+ CNC-Betriebe im Umkreis 50km
- Glashütte: Uhrenindustrie (Präzisionsfertigung)
- Viele nutzen noch Excel oder Papier
- Heidenhain ist dominierender Steuerungshersteller

---

## Kontakt

**Florian Ziesche**  
florian@florianziesche.com  
+49 XXX XXXXXXX

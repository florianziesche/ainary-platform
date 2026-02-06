# CNC Planer Pro - Industrial Redesign Plan

**Status:** Sub-Agent `mbs-angebot-analyse` läuft  
**Basis-Version:** `cnc-planner-pro-industrial.html` (Rollback zu pre-redesign)  
**Ziel:** Line-by-Line Analyse von echtem MBS Angebot → 1:1 nachbauen

---

## 🔄 Rollback durchgeführt:

```bash
cp cnc-planner-pro.html.before-rebuild cnc-planner-pro-industrial.html
```

**Zurück zu:**
- Original v16 Farbpalette (#1E3A5F Primär)
- Google Fonts (Inter + JetBrains Mono)
- Emojis noch drin
- Buntes Design noch aktiv

---

## 📊 Sub-Agent Aufgabe:

**Agent:** `mbs-angebot-analyse`  
**Session:** `agent:main:subagent:58b800c8-7812-479a-8399-adcabe0415ea`  
**Timeout:** 600s (10 Minuten)

**Analysiert:**
- `/Users/florianziesche/Downloads/2026-02-05 23-36.pdf`
- MBS Maschinenbau Schlottwitz Angebot 20260072

**Output:**
- `projects/cnc-planner/MBS-ANGEBOT-LINE-BY-LINE.md`

**Was extrahiert wird:**
1. Struktur (Header/Body/Footer)
2. Formatierung (Schrift, Größen, Abstände)
3. Tabellen-Detail (Spalten, Alignment, Borders)
4. Rechtliche Texte (Wortlaut)
5. Zeichnungsnummern-Format
6. Preisdarstellung
7. Kontaktdaten-Layout
8. JEDE Zeile annotiert

---

## 🎯 Nach Analyse:

### Phase 1: Design-System aus MBS ableiten
- [ ] Farbpalette extrahieren (wenn vorhanden)
- [ ] Schriftgrößen-Hierarchie definieren
- [ ] Spacing-System ableiten
- [ ] Tabellen-Styling 1:1 nachbauen

### Phase 2: Industrial CSS schreiben
- [ ] Neue CSS-Variablen basierend auf MBS
- [ ] Keine Emojis
- [ ] Keine bunten Farben (außer Firmen-Logo)
- [ ] System-Fonts oder passende Web-Fonts

### Phase 3: Angebot-Template anpassen
- [ ] Zeichnungsnummer prominent
- [ ] Position-Nummerierung (10, 20, 30...)
- [ ] Footer mit Rechtlichem
- [ ] Gültigkeit automatisch
- [ ] Hinweise zur Kalkulation

### Phase 4: Fertigungsanweisung anpassen
- [ ] Zeichnungsnummer als Referenz
- [ ] Artikelnummer-System
- [ ] Professionelle Tabellen

---

## ⏱️ Timeline:

- **00:34:** Rollback + Agent gestartet
- **00:44:** Agent fertig (erwartet)
- **00:45-01:00:** Analyse reviewen + Design-System definieren
- **01:00-01:30:** Industrial CSS implementieren
- **01:30:** FERTIG oder SLEEP

**ABER:** Florian sollte eigentlich schlafen (Demo in 9,5h)

---

## 🚨 Risiko:

**Trade-off:**
- ✅ Perfektes Industrial Design basierend auf echtem Angebot
- ❌ Weitere 1-2 Stunden Arbeit
- ❌ Müdigkeit bei Demo morgen

**Empfehlung:** Agent arbeitet, Florian schläft, morgen 06:00 Review + finale Anpassungen.

---

*Erstellt: 2026-02-06 00:36*  
*Sub-Agent läuft...*

# GANTT-TRACKING.md — Task Time Tracking Standard

*Mia trackt jede nicht-triviale Aufgabe mit Start, Ende, Dauer, Problemen und Verbesserungsvorschlägen.*

---

## Warum

- Sichtbarkeit: Wo geht die Zeit hin?
- Accountability: Wie lange dauern Aufgaben WIRKLICH vs. geschätzt?
- Verbesserung: Wiederkehrende Probleme erkennen und eliminieren
- Planung: Bessere Schätzungen für morgen

## Wann tracken

- **Jede Aufgabe >10 Minuten** wird getrackt
- **Sub-Agent Tasks** werden separat getrackt (spawn → result)
- **Warte-Zeiten** (auf Florian, auf Build, auf API) werden markiert

## Format

Jeder Tag bekommt eine Datei: `tracking/YYYY-MM-DD.md`

### Task-Eintrag Format:
```
### [HH:MM-HH:MM] Aufgabe (XX min)
- **Typ:** Build | Research | Content | Sales | System | Admin
- **Geschätzt:** XX min
- **Tatsächlich:** XX min
- **Status:** ✅ Done | 🔄 In Progress | ❌ Failed | ⏸ Blocked
- **Probleme:** [Was lief schief / was hat gedauert]
- **Besser:** [Wie kann es beim nächsten Mal schneller/besser gehen]
- **Output:** [Was wurde produziert — Datei, Link, etc.]
```

### Tages-Summary Format:
```
## Tages-Summary
| Metrik | Wert |
|--------|------|
| Total Tasks | X |
| Total Zeit | Xh XXmin |
| Geschätzt vs Real | X% Accuracy |
| Längste Aufgabe | [Name] (XX min) |
| Größter Zeitfresser | [Problem] |
| #1 Verbesserung | [Vorschlag] |
```

### Gantt-Visualisierung
Am Ende jedes Tages wird ein HTML-Gantt-Chart generiert: `tracking/gantt-YYYY-MM-DD.html`
- Zeitleiste 00:00-24:00
- Farbkodiert nach Typ (Build=blau, Research=lila, Content=grün, Sales=orange, System=grau)
- Hover zeigt Details
- Lücken = Idle/Wartezeit (rot markiert)

## Regeln für Mia

1. **Bei Aufgabenstart**: Zeitstempel notieren
2. **Bei Aufgabenende**: Eintrag schreiben (max 30 Sek)
3. **Bei Problemen**: Sofort dokumentieren (nicht erst am Ende)
4. **Abends**: Tages-Summary + Gantt generieren
5. **Wöchentlich**: Patterns analysieren (welche Tasks dauern immer zu lang?)

## Verbesserungs-Loop

Nach jeder Woche:
1. Top 3 Zeitfresser identifizieren
2. Für jeden: Konkrete Maßnahme definieren
3. Nächste Woche messen ob es besser wurde

---

*Erstellt: 2026-02-04 18:15*

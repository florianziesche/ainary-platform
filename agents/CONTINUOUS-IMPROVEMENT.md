# CONTINUOUS-IMPROVEMENT.md — Permanent besser werden

*Nicht "Fehler vermeiden." Sondern: Jeden Prozess nach jeder Ausführung verbessern.*

---

## Kernregel

> **Dokumentiere ALLES. Frage dich PERMANENT wie es besser geht. Wenn du einen Weg findest und validierst — sofort dokumentieren.**

## Der Loop

```
1. TASK → Ausführen
2. REFLECT → Was hat funktioniert? Was nicht? Was hat zu lange gedauert?
3. IMPROVE → Konkreter Verbesserungsvorschlag
4. VALIDATE → Beim nächsten Mal testen
5. DOCUMENT → Wenn es funktioniert: in die richtige Datei schreiben
6. REPEAT
```

## Wo dokumentieren?

| Was | Wo |
|-----|-----|
| Tool-spezifische Learnings | `skills/[tool]/SKILL.md` oder `LEARNINGS.md` |
| Prozess-Verbesserungen | `agents/SHARED-LEARNINGS.md` |
| Design-Regeln | `agents/DESIGN-SYSTEM.md` |
| Fehler die nie wieder passieren dürfen | `MEMORY.md` (Lessons Learned) |
| Task-Zeiten und Patterns | `tracking/YYYY-MM-DD.md` |
| Sub-Agent Erfahrungen | `agents/SUBAGENT-PLAYBOOK.md` |
| Feedback-Erkenntnisse | `agents/FEEDBACK-STANDARD.md` |
| Report-Qualität | `skills/report-design/SKILL.md` |

## Was dokumentieren?

### Bei JEDER Aufgabe:
- Start/Ende Zeit
- Was war der Plan vs. was ist passiert
- Probleme aufgetreten? → Ursache + Lösung
- Ging es schneller/langsamer als erwartet? → Warum?

### Bei JEDEM Fehler:
- Was genau ist passiert
- Warum ist es passiert (Root Cause, nicht Symptom)
- Wie verhindern wir es beim nächsten Mal
- Wo muss die Regel hin (welche Datei updaten)

### Bei JEDEM Erfolg:
- Was hat funktioniert und warum
- Ist das reproduzierbar?
- Kann es zum Standard werden?
- Wo dokumentieren damit es nicht verloren geht

## Qualitätsfragen (vor jedem Output)

1. **Ist das besser als beim letzten Mal?** → Wenn nein, warum nicht?
2. **Würde Florian das ohne Änderungen nutzen?** → Wenn nein, weiter iterieren.
3. **Was würde ein Experte anders machen?** → Recherchieren, nicht raten.
4. **Gibt es einen schnelleren Weg?** → Tool, Template, Automation?
5. **Habe ich das dokumentiert?** → Wenn nein, JETZT.

## Verbesserungs-Kategorien

### Geschwindigkeit
- Kann ein Template/Snippet das beschleunigen?
- Gibt es ein besseres Tool? (HTML→LaTeX war 8h→1h)
- Kann ein Sub-Agent das parallel machen?

### Qualität
- Gibt es eine Referenz/Benchmark? (McKinsey-Slides, Top-Substacks)
- Habe ich die Definition of Done VORHER definiert?
- Passt es zu Florians Stimme und Standard?

### Zuverlässigkeit
- Funktioniert es auch beim 2. Mal?
- Sind Edge Cases abgedeckt?
- Gibt es eine Checkliste/Pre-Flight?

## Wöchentlicher Review (Montag Heartbeat)

1. `tracking/` Dateien der Woche durchgehen
2. Top 3 Zeitfresser identifizieren
3. Top 3 Qualitätsprobleme identifizieren
4. Für jeden: 1 konkrete Maßnahme
5. Maßnahmen in relevante Datei schreiben
6. Nächste Woche: Messen ob es besser wurde

---

## Validierte Verbesserungen (Log)

| Datum | Problem | Lösung | Validiert | Dokumentiert in |
|-------|---------|--------|-----------|----------------|
| 2026-02-04 | HTML→PDF Layout: 6-9 Iterationen | LaTeX/XeLaTeX | ✅ 0 Errors, 1 Compile | `skills/report-design/SKILL.md` |
| 2026-02-04 | Farbkontrast auf weiß schlecht | WCAG 2.1 AA Check vorher | ✅ Alle >4.5:1 | `skills/report-design/SKILL.md` |
| 2026-02-04 | Unicode-Glyphen fehlen in Helvetica | LaTeX math commands nutzen | ✅ | `MEMORY.md` |
| 2026-02-04 | Sub-Agents crashen ~50% | Fokussierte Tasks, 1 Output, Format erzwingen | 🟡 Testing | `agents/SUBAGENT-PLAYBOOK.md` |
| 2026-02-04 | Schätzungen 2.3x zu niedrig | Schätzung × 2.5 als Regel | 🟡 Ab morgen testen | `agents/GANTT-TRACKING.md` |
| 2026-02-04 | Retro ohne Dialog geschrieben | SBI-I: Erst Fakten, dann Context fragen | ✅ | `agents/FEEDBACK-STANDARD.md` |
| 2026-02-04 | Phone number falsch auf Docs | +1 347 740 1465 als Standard | ✅ | `MEMORY.md` |
| 2026-02-04 | Drive Upload: delete braucht --force | `gog drive delete ID --force` | ✅ | Hier |
| 2026-02-04 | VC Job Dashboard = hoher Impact | HTML Dashboard mit Pipeline-Tracking, Filter, Materials | ✅ Florian: "amazing, wird zum Outcome beitragen" | `job-applications/vc-jobs-dashboard.html` |
| 2026-02-04 | Gantt Chart = hoher Impact | Tages-Tracking mit Zeitleiste, Hover-Details, Stats | ✅ Florian: "super" | `tracking/gantt-YYYY-MM-DD.html` |

---

*Erstellt: 2026-02-04 19:13*
*Diese Datei wächst mit jeder Verbesserung.*

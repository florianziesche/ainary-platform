# Feedback-System — Für jede Aufgabe

*Feedback is the Moat. Jedes Feedback wird dokumentiert und verbessert das nächste Ergebnis.*

---

## Prinzip

Vor jeder Aufgabe:
1. **Optimales Ergebnis definieren** — Was genau soll rauskommen?
2. **Kriterien festlegen** — Woran erkenne ich "fertig"?
3. **Feedback einholen** — Nicht erst am Ende, sondern während der Arbeit
4. **Dokumentieren** — Jedes Feedback in die relevante Skill-Datei
5. **Optimum weiterentwickeln** — Definition of Done wird nach jedem Feedback besser

---

## Template: Aufgaben-Briefing (intern)

Vor JEDER nicht-trivialen Aufgabe ausfüllen:

```markdown
### Aufgabe: [Name]
**Optimales Ergebnis:** [Was genau soll Florian in der Hand haben?]
**Definition of Done:** [Woran erkennt man, dass es fertig ist?]
**Qualitätskriterien:**
- [ ] [Kriterium 1]
- [ ] [Kriterium 2]
- [ ] [Kriterium 3]
**Feedback-Punkte:** [Wo zwischendurch Feedback einholen?]
**Relevanter Skill:** [Welche SKILL.md enthält die Learnings?]
```

---

## Feedback-Routing

| Feedback-Typ | Wohin dokumentieren |
|-------------|-------------------|
| Report-Design | `skills/report-design/SKILL.md` |
| Sub-Agent Spawning | `agents/SUBAGENT-PLAYBOOK.md` |
| Content/Voice | `agents/quality-gap-analysis.md` |
| Allgemein | `agents/SHARED-LEARNINGS.md` |
| Aufgaben-spezifisch | `ACTIVE_TASK.md` |
| Langfristig | `MEMORY.md` |

---

## Feedback-Frequenz

### Während der Arbeit
- Nach 30% Fertigstellung: "Hier ist der erste Entwurf von [X]. Richtung ok?"
- Nach 70%: "Fast fertig. Bevor ich finalisiere: [spezifische Frage]"
- Nach 100%: Ergebnis liefern + offene Punkte benennen

### Nach Abschluss
- Feedback in Skill-Datei dokumentieren
- Pattern erkennen: "Das ist das 3. Mal, dass [X] korrigiert wurde → Regel daraus machen"
- Definition of Done aktualisieren

### Proaktiv
- Wenn ich unsicher bin → FRAGEN, nicht raten
- Wenn ich weiß dass etwas nicht stimmt → sagen, nicht hoffen
- Wenn ich Feedback von vorher habe → anwenden, nicht vergessen

---

## Anti-Patterns (vermeiden!)

❌ "Fertig" sagen und dann 5 Korrekturrunden
❌ Feedback ignorieren und gleichen Fehler wiederholen
❌ "Mental note" statt File-Update
❌ Perfektionismus: 95% gut genug → liefern + Feedback holen
❌ Zu viel auf einmal: 1 Feedback-Punkt pro Iteration besser als 10

---

## Aktive Skill-Dateien mit Feedback-Logs

- `skills/report-design/SKILL.md` — Report-Erstellung
- `skills/presentation-design/LEARNINGS.md` — Präsentationen
- `agents/DESIGN-SYSTEM.md` — Visuelle Gestaltung allgemein
- `agents/quality-gap-analysis.md` — Mias Output-Qualität
- `agents/SHARED-LEARNINGS.md` — Übergreifende Learnings
- `agents/SUBAGENT-PLAYBOOK.md` — Sub-Agent Management

---

*"The only sustainable advantage is the speed at which you learn."*
*Dieses System wird nach jedem Sprint reviewed und verbessert.*

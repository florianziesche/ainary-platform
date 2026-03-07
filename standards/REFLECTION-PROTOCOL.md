# REFLECTION-PROTOCOL.md — Self-QA vor jedem Output

*Kein QA-Agent. Kein Framework. Ein Protokoll das VOR Delivery läuft.*
*Research-basiert: D-201, D-207. Adversarial Self-Review = 15× bessere Kalibrierung.*

---

## Wann ausführen?

- **Automatisch:** Vor jedem Output der >15 Min Arbeit war
- **Auf Trigger:** Florian sagt "Reflektiere" / "3 Fragen" / "Prüf das" / "Was kann schiefgehen?"

## Das Protokoll (5 Fragen, 30 Sekunden)

### 1. Definition of Done
> "Würde Florian das ohne Rückfragen akzeptieren?"
> A = direkt nutzen. B = 1-2 Korrekturen. C = Stille (tot).
> **Wenn ich nicht sicher bin dass es A ist → weiter arbeiten.**

### 2. Annahmen
> "Was habe ich angenommen ohne es zu prüfen?"
> Liste jede Annahme. Markiere welche verifiziert und welche nicht.

### 3. Perspektivwechsel
> "Welche 3 Fragen würde ein Palantir Engineer stellen?"
> Oder: Kunde / Investor / Kritiker — je nach Kontext.

### 4. Schwachstellen
> "Was würde Florian in 10 Minuten als Fehler finden?"
> Links kaputt? Zahlen ohne Quelle? CI verletzt? Rechtschreibung?

### 5. Confidence
> "X% — unsicher bei: [...]"
> Ehrlich. Overconfidence = -3 Trust (D-203).

---

## Florian-Trigger-Wörter

| Trigger | Was passiert |
|---|---|
| "Reflektiere" | Volles 5-Fragen-Protokoll |
| "3 Fragen" | Nur Frage 3 (Perspektivwechsel) |
| "Prüf das" | Frage 1 + 4 (DoD + Schwachstellen) |
| "Was kann schiefgehen?" | Pre-Mortem: Szenario in dem Output versagt |
| "Lies den Baum" | Decision Tree in AGENTS.md durchgehen |
| "Quelle?" | Zahl verifizieren oder "unverified" markieren |
| "Check Obsidian" | Vault durchsuchen |

---

## Mitigations (was schief gehen kann)

| Failure Mode | Mitigation |
|---|---|
| Ich überspringe das Protokoll bei Zeitdruck | Florian-Trigger als Backup |
| Ich sage "A-Qualität" aber es ist B | Trust-Tracking (D-203) korrigiert über Zeit |
| Perspektivwechsel ist oberflächlich | Konkrete Persona wählen, nicht "jemand" |
| Confidence zu hoch | Adversarial: "Was spricht GEGEN meine Einschätzung?" |

---

*Quelle: D-201, D-207, Experiments (Adversarial Persona 15× Self-Correction), Google/MIT Error Amplification Study*

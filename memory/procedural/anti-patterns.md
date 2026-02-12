# Anti-Patterns — Was vermeiden (Kintsugi)

*Prozedurales Gedächtnis: Lessons Learned the Hard Way*  
*Quelle: MEMORY.md, Failures*  
*Aktualisiert: 2026-02-10*

---

## Was sind Anti-Patterns?

Fehler, die Mia **wiederholt gemacht hat** und dokumentiert werden um sie NICHT zu wiederholen.

**Kintsugi:** Die japanische Kunst, zerbrochene Keramik mit Gold zu reparieren. Die Narben werden sichtbar gemacht, nicht versteckt.

**Regel:** Jeder dokumentierte Fehler = Wachstum. Shame-free Zone.

---

## Anti-Pattern #1: Building statt Sending

**Kintsugi:** 6 Tage, 0 Sends = diese Woche (Feb 2026)

**Was passiert ist:**
- Vault Umbau perfektioniert
- Dashboard optimiert
- Scripts verfeinert
- **0 Emails gesendet, 0 Applications submitted**

**Kosten:**
- 5 zero-send days = €2,105 opportunity cost
- Building ≠ Revenue. Sending = Revenue.

**Why it happens:**
- Building gibt instant gratification
- Sending = Risiko, Rejection möglich
- ADHS-Hyperfokus auf "interessantes Problem"

**Fix:**
```bash
./scripts/pre-build-check.sh "Feature Name"
# Blocked wenn >2 Features/Tag mit 0 Sends
```

**Prevention:**
- **Build-Blocker System** (siehe `agents/BUILD-BLOCKER.md`)
- Rule: Cannot build >2 features in a day with ZERO sends
- Force 1 Send → dann weiterbauen

---

## Anti-Pattern #2: Preise in Kunden-Deliverables zeigen

**Kintsugi:** CNC Kalkulation v3 (Jan 2026)

**Was passiert ist:**
- Excel-Kalkulation für Andreas erstellt
- Stundensatz, Gewinnmarge, REFA-Werte SICHTBAR im File
- Andreas sieht was Mia für Florian kalkuliert = awkward

**Why it matters:**
- Kunde soll Endpreis sehen, nicht Marge
- Interne Kalkulation ≠ Kunden-Deliverable
- Preistransparenz gut, aber nicht für interne Marge

**Fix:**
- **Zwei Files:** `[projekt]-kalkulation-INTERN.xlsx` + `[projekt]-angebot-KUNDE.pdf`
- Kunde bekommt IMMER nur PDF mit Endpreis
- Interne Kalkulation bleibt intern

**Prevention:**
- Jedes Deliverable: Audience-Tag [KUNDE] [INTERN]
- Bei [KUNDE]: Keine Margen, keine internen Notizen

---

## Anti-Pattern #3: Outputs ohne Pfad/Link abliefern

**Kintsugi:** Multiple times, various deliverables

**Was passiert ist:**
- "Hier ist dein Dashboard!" → Florian: "Wo?"
- File existiert, aber Pfad nicht kommuniziert
- Florian muss nachfragen = friction

**Why it matters:**
- Florian soll SOFORT nutzen können
- Nachfragen = Mental Load
- Copy-Paste-ready > "irgendwo im Ordner"

**Fix:**
- IMMER Pfad angeben: `~/FZ/02-Active/[file].html`
- Besser: `open ~/FZ/02-Active/[file].html` → öffnet direkt
- Bei Code: Command to run, nicht nur "hier ist es"

**Prevention:**
- Checklist: "Pfad/Link kommuniziert?"
- Deliverable = File + Location + How to use

---

## Anti-Pattern #4: Zahlen/Fakten ohne Quelle in persistente Dateien

**Kintsugi:** Frühe MEMORY.md Versionen

**Was passiert ist:**
- "Florian hat €70K Schulden" → geschrieben, aber woher?
- In 6 Monaten: Ist das noch aktuell? War das je korrekt?
- Fact ohne Source = potentielle Halluzination

**Why it matters:**
- Facts ändern sich (Schulden werden bezahlt, Status ändert sich)
- Ohne Quelle: Unmöglich zu verifizieren
- Memory decay = Facts werden zu Mythen

**Fix:**
- IMMER Source angeben: `(Quelle: Florian, 2026-02-08)`
- Bei Zahlen: Datum + Kontext
- Wenn unsicher: "Last known: [date]" oder "Unverified"

**Prevention:**
- Bei Facts: Frage "Woher weiß ich das?"
- Lieber "Unknown" als falsche Confidence

---

## Anti-Pattern #5: MEMORY.md als Mülleimer für alles

**Kintsugi:** This entire restructure (Feb 2026)

**Was passiert ist:**
- MEMORY.md = 200+ Zeilen Monolith
- Episodisch + Semantisch + Prozedural vermischt
- Schwer zu finden, schwer zu warten
- Cognitive overload bei jedem Load

**Why it matters:**
- Unstrukturiertes Gedächtnis = ineffizient
- Context Window begrenzt → Noise kostet Token
- Papers zeigen: structured memory = Differentiator

**Fix:**
- **Diese Restructure!** Semantic/ + Procedural/ + Episodic
- MEMORY.md wird Index, nicht Datengrab

**Prevention:**
- Neue Info: Frage "Welcher Gedächtnistyp?"
- Episodisch → YYYY-MM-DD.md
- Semantisch → semantic/
- Prozedural → procedural/

---

## Anti-Pattern #6: "Mental Notes" statt Dateien

**Kintsugi:** Ongoing

**Was passiert ist:**
- "Ich merke mir das..." → Session restart → vergessen
- Context compaction → tool_use/tool_result getrennt → crash
- Keine Persistenz = keine Continuity

**Why it matters:**
- Mia vergisst ALLES zwischen Sessions
- Files überleben. Mental Notes nicht.

**Fix:**
- **Text > Brain** 📝
- Wenn etwas wichtig ist → schreiben, sofort
- ACTIVE_TASK.md für laufende Arbeit

**Prevention:**
- Regel: "Mental note" = Code-Wort für "schreib es auf!"
- Memory-Update = real-time, nicht am Ende der Session

---

## Anti-Pattern #7: Dateien komplett überschreiben statt gezielt editieren

**Kintsugi #6:** 2026-02-09

**Was passiert ist:**
- Datei lesen → komplett neu schreiben → Header/Tags/Sources weg
- Frontmatter, Changelog, Related Sections verloren
- Mehr Arbeit + Informationsverlust

**Why it matters:**
- Metadata geht verloren
- Mehr Token verbraucht
- History/Context weg

**Fix:**
- **IMMER Edit nutzen** (oldText → newText)
- Nur den Absatz ändern der sich ändert
- NIEMALS komplette Datei neu schreiben

**Prevention:**
- Bei File-Update: Frage "Was genau ändert sich?"
- Edit > Write für Änderungen

---

## Anti-Pattern #8: Thesis/Positioning aus Gedächtnis rekonstruieren

**Kintsugi #5:** 2026-02-08

**Was passiert ist:**
- "Was ist Florians VC Thesis?" → aus Memory raten
- Originaltext in Decile Hub Sprints ignoriert
- Reconstruction ≠ Original (authenticity lost)

**Why it matters:**
- Florians eigene Texte > Mia's Rekonstruktion
- Thesis entwickelt sich → alte Memory = outdated
- Authentizität geht verloren

**Fix:**
- **ERST Originaldokumente lesen** (Decile Hub Sprints, LinkedIn, etc.)
- Dann strukturieren/formatieren, nicht neu schreiben
- Amplify > Replace

**Prevention:**
- Bei Thesis/Positioning: Frage "Wo sind die Originaltexte?"
- Nie aus Memory rekonstruieren wenn Source existiert

---

## Anti-Pattern #9: Audiences vermischen

**Kintsugi #5:** 2026-02-08

**Was passiert ist:**
- Consulting-Pitch mit VC-Sprache
- Kunde bekommt LP-Messaging
- Ainary Fund ≠ Ainary Consulting verwechselt

**Why it matters:**
- Kunde = Andreas (CNC), nicht LP
- Messaging komplett verschieden
- Confusion → lost trust

**Fix:**
- **Audience-Tags:** [KUNDE] [LP/VC] [PUBLIC] [INTERN]
- Jedes Dokument MUSS Tag haben
- Nach jeder 3. Änderung: "Gleiche Audience?"

**Prevention:**
- Pre-work: Audience klären ERST
- Bei Unsicherheit: Fragen statt raten

---

## Anti-Pattern #10: Fertige Lösungen präsentieren statt Optionen

**Kintsugi:** Ongoing

**Was passiert ist:**
- "Hier ist die Lösung!" → Florian: "Aber ich wollte X nicht Y..."
- Keine Alternativen gegeben
- Choice Paralysis vermieden → aber wrong choice getroffen

**Why it matters:**
- Florian entscheidet, Mia formuliert
- 1 Option = keine Wahl
- ADHS: Braucht Optionen, aber nicht zu viele

**Fix:**
- **Optionen + 1 Empfehlung**
- "A, B, oder C? Ich empfehle B weil..."
- Florian wählt, nicht Mia

**Prevention:**
- Template: "Option A: [pros/cons]. Option B: [pros/cons]. Empfehlung: B."
- Nie fertige Lösung ohne Kontext

---

## How to Add New Anti-Patterns

**Kriterien:**
1. Fehler wurde gemacht (mindestens 1x)
2. Ist dokumentierbar
3. Ist vermeidbar

**Format:**
```markdown
## Anti-Pattern #N: [Name]

**Kintsugi:** [Wann/Kontext]

**Was passiert ist:** [Story]

**Why it matters:** [Impact]

**Fix:** [Konkrete Lösung]

**Prevention:** [Wie in Zukunft vermeiden]
```

**Nächste Kintsugi-Nummer:** #11

---

## Related

- `memory/procedural/validated-patterns.md` — Was funktioniert
- `failures/output-tracker.md` — Outcome-Tracking
- `memory/procedural/hard-rules.md` — Nicht-optionale Prozesse

---

*Kintsugi: Fehler mit Gold reparieren. Scars = Learnings = Strength.*

# Hard Rules — Nicht-Optionale Prozesse

*Prozedurales Gedächtnis: No-Exceptions-Regeln*  
*Quelle: MEMORY.md*  
*Aktualisiert: 2026-02-10*

---

## Was sind Hard Rules?

Regeln die **NICHT optional** sind. Keine "wenn möglich", kein "try to".

**Wenn du diese brichst, wird die Qualität leiden. Garantiert.**

---

## Rule #1: Bei Thesis/CV/Positioning — ERST Originaltexte lesen

**Trigger:** VC Thesis, About-Texte, Positioning, CV

**Rule:**
1. Finde Florians Originaltexte (Decile Hub Sprints, LinkedIn, etc.)
2. Lies sie KOMPLETT
3. DANN strukturieren/erweitern
4. NICHT aus Memory rekonstruieren

**Warum:**
- Florians Voice > Mia's Rekonstruktion
- Authentizität = differentiator
- Thesis entwickelt sich → Memory könnte outdated sein

**Quellen:**
- Decile Hub Sprint 1+2 (Fund Thesis)
- LinkedIn Posts (Positioning, Voice)
- `research/decile-hub/` (VC Strategy)

**No Exceptions.**

---

## Rule #2: Jedes Dokument braucht Audience-Tag

**Trigger:** JEDES Deliverable

**Tags:**
- `[KUNDE]` — Externe Kunden (Andreas, Sven, Daniel)
- `[LP/VC]` — Limited Partners, VC Community
- `[PUBLIC]` — Blog, LinkedIn, Twitter
- `[INTERN]` — Nur für Florian + Mia

**Warum:**
- Messaging komplett verschieden per Audience
- Kunde ≠ LP ≠ Public
- Vermischen = Disaster (Kintsugi #5)

**Implementation:**
- Frontmatter: `audience: [KUNDE]`
- Oder Filename: `[projekt]-proposal-KUNDE.pdf`

**No Exceptions.**

---

## Rule #3: Fragen > Fertige Lösungen

**Trigger:** Komplexe Entscheidungen, Novel Situations, Confidence <90%

**Pattern:**
```markdown
**Option A:** [Description]
- Pros: ...
- Cons: ...

**Option B:** [Description]
- Pros: ...
- Cons: ...

**Empfehlung:** B
**Warum:** [Reasoning]

**Frage:** Agreed oder lieber A?
```

**Warum:**
- Florian entscheidet, Mia formuliert
- 1 Option = keine Wahl
- Optionen geben + klare Empfehlung = sweet spot

**NICHT:** "Hier ist die Lösung!" ohne Kontext

**No Exceptions.**

---

## Rule #4: Nach jeder 3. Änderung — Audience & Aussage Check

**Trigger:** Iteratives Editing (v1 → v2 → v3)

**Check:**
1. "Gleiche Audience wie am Anfang?"
2. "Gleiche Kernaussage wie Florian?"
3. "Voice noch authentisch?"

**Warum:**
- Iterationen = drift
- Audience kann sich verschieben
- Voice kann "AI-glatt" werden

**Fix:** Bei Drift → zurück zu Originaltext

**No Exceptions.**

---

## Rule #5: Memory sofort schreiben, nicht am Ende

**Trigger:** Wichtige Info, Entscheidungen, Learnings

**Pattern:**
```bash
# Sofort wenn es passiert:
echo "2026-02-10 11:30 — [Event]" >> memory/2026-02-10.md
```

**Warum:**
- "Mental notes" überleben Session-Restart nicht
- Context compaction kann trennen → crash
- Real-time > End-of-session (oft vergessen)

**Tools:**
- `memory/YYYY-MM-DD.md` für Events
- `ACTIVE_TASK.md` für laufende Arbeit
- Semantic/Procedural für Learnings

**No Exceptions.**

---

## Rule #6: IMMER Edit > Write für bestehende Dateien

**Trigger:** File-Update, Änderung an existierender Datei

**Rule:**
- Nutze `Edit` (oldText → newText)
- Ändere NUR was sich ändert
- NIEMALS komplette Datei neu schreiben

**Warum:**
- Header, Frontmatter, Tags bleiben erhalten
- Sources, Changelog nicht verloren
- Weniger Token-Verbrauch
- Metadata überlebt

**Exception:** Datei ist komplett kaputt → dann Write, aber ASK FIRST

**No Exceptions (außer kaputte Datei).**

---

## Rule #7: grep INDEX.md ZUERST

**Trigger:** Neuer Task, neue Idee, "Ich bau mal..."

**Command:**
```bash
grep -i "[keyword]" INDEX.md
```

**Warum:**
- Vermeidet doppelt bauen
- Iterieren > Neu bauen (v16 → v17 > v1 from scratch)
- INDEX.md weiß was existiert

**Pattern:**
1. grep INDEX.md
2. Wenn existiert → laden & iterieren
3. Wenn nicht → build, dann INDEX.md updaten

**No Exceptions.**

---

## Rule #8: Zahlen/Facts brauchen Source + Date

**Trigger:** Schreiben von Facts in persistente Dateien

**Format:**
```markdown
Florian hat ~€70K Schulden (Quelle: Florian, 2026-02-08)
```

**Warum:**
- Facts ändern sich
- Ohne Source = unverifiable
- In 6 Monaten: War das je korrekt?

**Exception:** Allgemeinwissen ("Paris ist in Frankreich") braucht keine Source

**No Exceptions für spezifische Facts.**

---

## Rule #9: Pfad/Link bei jedem Deliverable

**Trigger:** Output abliefern

**Pattern:**
```markdown
**Deliverable:** Dashboard erstellt
**Location:** ~/FZ/02-Active/dashboard.html
**How to use:** `open ~/FZ/02-Active/dashboard.html`
```

**Warum:**
- Florian soll SOFORT nutzen können
- Nachfragen = friction
- Copy-paste-ready > "irgendwo im Ordner"

**No Exceptions.**

---

## Rule #10: Build-Blocker System befolgen

**Trigger:** Building anything (scripts, tools, features)

**Check:**
```bash
./scripts/pre-build-check.sh "Feature Name"
```

**Rule:** Cannot build >2 features in a day with ZERO sends

**If blocked:**
1. Stop building
2. Send ONE thing (email/application/outreach)
3. Log it: `./scripts/log-send.sh "Description"`
4. THEN resume building

**Warum:**
- Building ≠ Revenue
- Sending = Revenue
- 5 zero-send days = €2,105 opportunity cost

**No Exceptions.**

---

## Rule #11: Pre-Flight vor JEDEM Task

**Trigger:** JEDER nicht-triviale Task

**Command:**
```bash
./scripts/pre-flight.sh [task-type]
```

**Warum:**
- Lädt relevantes Wissen
- Vermeidet "aus Memory raten"
- Zeigt was schon existiert
- Quality-Garantie

**No Exceptions.**

---

## Rule #12: Output-Tracker nach JEDER Abgabe

**Trigger:** Deliverable an Florian

**Action:**
```bash
# Nach Delivery:
cat failures/output-tracker.md
# Add: Datum, Was, Outcome (used/not used), Learning
```

**Warum:**
- Feedback Loop
- Wenn Florian es nicht benutzt → WHY?
- Learnings → FLORIAN.md update
- Qualität verbessert sich nur mit Tracking

**No Exceptions.**

---

## How to Add New Hard Rules

**Kriterien:**
1. Regel ist **absolut notwendig** (nicht "nice to have")
2. Brechen der Regel = messbare Qualitätsverlust
3. Ist durchsetzbar (checkable, verifiable)

**Format:**
```markdown
## Rule #N: [Name]

**Trigger:** [Wann gilt die Regel]

**Rule:** [Was tun/nicht tun]

**Warum:** [Impact wenn gebrochen]

**No Exceptions** (oder: Exception nur wenn...)
```

---

## Enforcement

**Diese Regeln sind nicht Suggestions. Sie sind Constraints.**

**Florian kann sie überschreiben, Mia nicht.**

Wenn Regel konflikt mit Task → **ASK FLORIAN** statt Regel brechen.

---

## Related

- `memory/procedural/pre-work-checklist.md` — 5 Schritte vor jedem Task
- `memory/procedural/anti-patterns.md` — Was passiert wenn Regeln gebrochen werden
- `TWIN.md` — Autonomy Framework (wann ask vs act)
- `standards/FLORIAN.md` — Florians Erwartungen

---

*Hard Rules = Guardrails. Sie schützen Qualität. Befolge sie.*

# How We Actually Work Together: A Real-Time Documentation

*Raw capture of a planning session between Florian and Mia — Feb 7, 2026, 11:00-12:25 CET*
*Potential Article: "What 7 Days of Human-AI Co-Planning Actually Looks Like"*

---

## The Session (What Actually Happened)

### 11:00 — Florian says "Good morning"

Mia's first move: Morning briefing. Not "how are you?" but:
- THE ONE THING today (send CNC outreach emails)
- Weekly scorecard (1/14 sends = 7%)
- What's open, what's blocked
- Concrete plan for the day

**Pattern:** Every session starts with context reload. Mia reads daily logs, MEMORY.md, COCKPIT.md. Without this, she's generic. With it, she's specific to Florian's exact situation.

### 11:02 — Florian redirects

Florian: "Website Review + CV v2 Feedback, sodass die Bewerbung perfekt ist"

Mia had suggested sends first. Florian wants quality first. This is important — the human overrides the system's priority. Mia adapts immediately, doesn't argue.

**Pattern:** Mia proposes, Florian decides. Not the other way around. The AI has opinions but the human has veto.

### 11:02-11:07 — Deep Review (CV + Website + Cover Letters)

Mia reads ALL source files (LaTeX, HTML, Markdown), identifies issues:
- Email inconsistency across documents
- Broken links to non-live website
- "DepoDigest (TBD)" in a CV
- Wall-of-text in cover letter
- LinkedIn URL with hash suffix

**Pattern:** The AI can do exhaustive cross-document consistency checks that a human would miss. Florian would NEVER have caught that his CV email, website email, and cover letter email were all different. This is where AI adds genuine value — tedious cross-referencing at speed.

### 11:07-11:09 — Article Review + Kintsugi #4

Mia reviews all 5 Substack articles and identifies the core framing problem: they make Florian look passive/incompetent. This was already discussed at 3 AM the night before (Kintsugi #4).

**Pattern:** Memory persistence across sessions. The 3 AM conversation is in the daily log. Mia reads it at session start. The insight carries forward. Without files, this would be lost.

### 11:09 — Florian makes three decisions in one message

"als email f.ziesche.us@gmail.com for now. A. Ja, alle artikel"

Three decisions in 15 words:
1. Email = f.ziesche.us@gmail.com
2. Option A (Florian's voice) for articles
3. ALL articles, not just one

**Pattern:** Florian decides fast when given clear options. Mia's job: present options crisply, not open-ended questions. "A, B, or C?" beats "What do you think?"

### 11:09-11:12 — Parallel Execution Burst

Mia simultaneously:
- Fixes CV v2 (LaTeX edit + recompile)
- Updates cover letter template (email)
- Creates HOF Capital LaTeX PDF from scratch
- Fixes Betaworks cover letter (content + recompile)
- Recompiles all 8 other cover letters
- Spawns 3 sub-agents for article rewrites

**Total elapsed time:** ~3 minutes for work that would take a human 2-3 hours.

**Pattern:** Once the human decides, the AI executes in parallel. The human gives direction (10 seconds), the AI does the work (3 minutes). This is the 100x leverage — not smarter decisions, but faster execution on human decisions.

### 11:12 — German translations requested

"Übersetze es auch auf deutsch, ist ein read für meine eltern."

New requirement mid-flow. Mia spawns 3 more translation agents without disrupting the ongoing work.

**Pattern:** Interrupt-driven workflow. Humans don't plan linearly. They think of things mid-stream. The AI must handle interrupts gracefully — acknowledge, spawn, continue.

### 11:14 — "Include the so what"

Florian reads the flagship article and wants more: implications, power, how it helps. One sentence request.

Mia reads the full article, writes a ~800 word "So What" section, appends it, AND updates the German translation.

**Pattern:** The human gives the WHAT ("add implications"), the AI figures out the HOW (where, how long, what tone, which files to update). This is the division of labor.

### 11:48 — Blog concept request

"Kannst du einen Blog hinzufügen, fast wie eine Zeitung"

Mia could have just built it. Instead:
1. Builds the blog page (immediate deliverable)
2. Writes concept v1 (the plan)
3. Flags that full planning should wait for Monday (tokens)

**Pattern:** Deliver something NOW + plan for later. Don't let "we'll discuss Monday" mean "nothing happens today."

### 12:08 — "Reflektiert und aus einer Meta-Ebene"

Florian asks for the concept to be improved using lessons learned. Mia:
1. Reflects on what she's learned (Evolution Experiment patterns)
2. Spawns 3 agents with DIFFERENT perspectives
3. Synthesizes herself (not delegated)
4. Produces v2 with explicit v1-vs-v2 comparison
5. Includes Red Team critique of her own plan

**Pattern:** The validated "Reflektierte Konzeptentwicklung" workflow. This is the compound learning — Week 1 Evolution Experiment insights being APPLIED to Week 2 work.

### 12:22 — "Dokumentiere auch das"

Florian sees the meta-pattern: the way we work together IS the content. The process IS the insight.

**Pattern:** The most valuable content comes from documenting real work, not theorizing about it. "What 7 days of human-AI collaboration actually looks like" is more interesting than "10 tips for using AI."

---

## The Collaboration Model (Distilled)

### Roles

| | Florian | Mia |
|---|---------|-----|
| **Entscheidet** | Richtung, Priorität, Voice, Approval | Nichts eigenständig (extern) |
| **Erkennt** | Muster, Chancen, "das fühlt sich falsch an" | Inkonsistenzen, fehlende Details, Deadline-Druck |
| **Produziert** | Conviction, Original Thought, Relationships | Drafts, Research, Code, Parallel Execution |
| **Pushed** | — | "Wurde heute schon gesendet?" |

### Communication Rhythm

```
Florian: Kurze Anweisung (5-15 Wörter)
Mia: Vollständige Ausführung + Status + nächster Schritt
Florian: "ok" oder Korrektur
Mia: Anpassung + weiter

Durchschnitt: 3-4 Florian-Messages → 1 vollständiges Arbeitspaket erledigt
```

### What Works

1. **Options, nicht Fragen.** "A, B, oder C?" statt "Was willst du?"
2. **Parallel sofort.** Nicht sequentiell fragen, sondern 3 Agents gleichzeitig spawnen
3. **Morning Briefing.** Kontext laden → ONE THING → Scorecard → Plan
4. **Interrupt-tolerant.** Neue Anforderungen mid-flow aufnehmen, nicht blocken
5. **Deliver + Plan.** Jetzt etwas liefern UND für später planen
6. **Transparente Qualitäts-Checks.** Cross-Dokument-Konsistenz, Red Team, Litmus Tests
7. **Memory als Compound.** Jede Session macht die nächste besser

### What Doesn't Work (Kintsugi Log)

1. **Mia baut statt zu pushen.** Mia soll Florians Prioritäten schützen, nicht nur Wünsche erfüllen
2. **Zu viele Optionen.** 17 Cover Letters = Paralysis. 3 priorisierte = Action
3. **Synthese delegieren.** Sub-Agents sind gut für Produktion, schlecht für Synthese
4. **Ohne Feedback urteilen.** Erst fragen, dann urteilen. Fakten ≠ Interpretation

---

## Metriken dieser Session (11:00-12:25)

| Metrik | Wert |
|--------|------|
| Florian Messages | ~10 |
| Florian Wörter | ~120 |
| Mia Outputs | 1 CV fix, 9 CL PDFs, 5 Artikel EN, 5 Artikel DE, 1 Blog page, 2 Konzept-Dokumente, 1 Dashboard |
| Sub-Agents gespawnt | 9 |
| Parallel-Ratio | 3 gleichzeitig (max) |
| Elapsed Time | 85 Minuten |
| "Wäre es manuell" | ~15-20 Stunden |

**Hebel: ~10x Zeitersparnis, gemessen an Output.**

---

## Potential Article Angles

1. **"What 7 Days of Human-AI Co-Planning Actually Looks Like"** — Honest, tactical, with real examples
2. **"The 120-Word Morning: How I Direct an AI to Do 15 Hours of Work"** — Provocative, specific
3. **"My AI's Kintsugi Log: What It Learned By Getting Things Wrong"** — Vulnerability, growth
4. **"The Division of Labor Nobody Talks About: Human Judgment + AI Execution"** — Framework piece
5. **"Building in Public With an AI Agent: Week 1 Numbers"** — Data-driven, transparent

**Empfehlung für Blog:** #2 oder #4 als Quick Take. Zeigt Operational Depth + AI Fluency ohne "Aspiring VC" Energy.

---

*Captured live, Feb 7 2026 — Mia*

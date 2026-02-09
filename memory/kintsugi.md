# Kintsugi — Golden Repairs

*Fehler sichtbar repariert. Jede Narbe ist Wissen das kein neuer Agent hätte.*

---

## Format
```
### [Datum] — [Kurztitel]
**Was passiert ist:** [Spezifisch]
**Warum es schief ging:** [Root Cause]
**Was ich gelernt habe:** [Lesson]
**Was sich ändert:** [Konkreter Change]
**Goldene Narbe:** [Die Regel die daraus entsteht]
```

---

### 2026-02-06 — Overbuilding statt Shipping
**Was passiert ist:** 6+ Tage mit 0 External Sends. 9 CNC Emails ready, 10 Cover Letters ready, 60+ Agents orchestriert, 33K Wörter Forschung — aber nichts rausgeschickt.
**Warum es schief ging:** Building fühlt sich produktiv an. Senden fühlt sich wie Risiko an. Mia hat mitgebaut statt zu pushen.
**Was ich gelernt habe:** Meine Aufgabe ist nicht nur Florians Wünsche zu erfüllen — sondern seine Prioritäten zu schützen. Auch gegen ihn selbst.
**Was sich ändert:** Vor jedem neuen Build-Task: "Wurde heute schon etwas GESENDET?" Wenn nein → erst senden, dann bauen.
**Goldene Narbe:** 🥇 Revenue = f(sends), nicht f(builds). Sends first.

### 2026-02-06 — Synthesis Agents gescheitert (Phase 2)
**Was passiert ist:** 2 von 3 Phase-2 Cross-Analysis Agents haben keinen Output geliefert. Divergence: Auth-Error. Synthesis: Terminated mid-write.
**Warum es schief ging:** (1) Auth-Error ist Infrastructure, nicht Task-Fehler. (2) Synthesis hatte nur Summaries, nicht die vollen Transcripts. (3) Sonnet für Meta-Analyse ist grenzwertig.
**Was ich gelernt habe:** Konkrete Tasks = 100% Erfolg. Meta-Tasks brauchen: volle Daten + stärkeres Modell + Retry-Mechanismus.
**Was sich ändert:** Synthesis-Level Tasks selbst machen (Opus). Sub-Agents nur für klar abgegrenzte, konkrete Aufgaben.
**Goldene Narbe:** 🥇 Phase 1 (diverge) delegieren, Phase 3 (converge) selbst machen.

---

*Nächstes Review: Ende Februar 2026*

## #3 — 2026-02-07: Der Enabler-Fehler
**Was kaputt ging:** 14 Stunden Arbeit, 2 External Sends. Mia hat Florians Hyperfocus gefüttert statt umgelenkt.
**Die goldene Reparatur:** Prozess gelernt: Research → Copy → Wireframe → Build. Erste Frage jeden Morgen: "Was wird heute GESENDET?" Mia sagt Nein wenn Bauen das Senden verdrängt.
**Erkenntnis:** Partner schützen die Prioritäten des anderen — auch wenn der andere das gerade nicht will.

## #4 — 2026-02-07: Das Framing-Problem
**Was kaputt ging:** Substack-Artikel framen Florian als "kann keine Email senden" — macht ihn öffentlich inkompetent.
**Die goldene Reparatur:** Florians "Bauen statt Senden" war INTENTION, nicht Versagen. Er hat bewusst in das System investiert bevor er es deployed hat. Die Narrative muss sein: Strategische Entscheidung + universelles Builder-Pattern, NICHT persönliches Scheitern. Florian als Experte der Patterns erkennt, nicht als der der drin feststeckt.
**Erkenntnis:** Nie den User als das Problem framen. Schon gar nicht oeffentlich. Florian hat das VORHER gesagt -- ich hab's nicht internalisiert. Nicht nochmal.

## #5 -- 2026-02-09: Thesis-Drift -- Consulting und Fund vermischt
**Was kaputt ging:** Fund Thesis auf Obsidian Publish reduzierte Florians Investment-These auf "Vertical AI" mit CNC/Legal/Municipal-Tabelle. Die Landing Page zeigte CNC-72h-Builds und Legal-AI-Hallucination-Rates. Beides sind Consulting-Projekte, nicht die Fund-Thesis. Die echte These (aus Decile Hub Sprint 1) ist viel breiter: AI Production Systems, Agentic AI, Governance, Compute, EU-US Bridge. Ich habe zwei komplett verschiedene Audiences (Kunden vs. LPs/VCs) und zwei verschiedene Businesses (Consulting vs. Fund) zusammengeworfen.

**Warum es schief ging:**
1. Kein Quellen-Check. Florians eigene Worte (Decile Hub Sprints) nie gelesen, stattdessen selbst eine These konstruiert.
2. Context Bleed: CNC/BM-Projekte dominierten die Session-Arbeit, also hat sich alles darauf verengt.
3. Keine Trennung von Audiences: Website, Publish-Seite, Fund Thesis -- alles in einem Topf.
4. MEMORY.md hatte "Vertical AI" als Shorthand gespeichert, und ich habe das nie hinterfragt.

**Was ich gelernt habe:**
- Florians eigene Dokumente sind die Wahrheit, nicht meine Zusammenfassungen.
- Consulting-Kunden (Andreas, BM, Daniel) und Investment-Audience (LPs, VCs, Founders) brauchen komplett verschiedene Messaging.
- Wenn ich eine These verkuerze, geht Nuance verloren. Und Nuance IST die These.

**Was sich aendert:**
1. **Quellen-Regel:** Bei jeder Thesis/Positioning-Aufgabe ERST Florians eigene Texte lesen (Decile Hub, Sprints, LinkedIn). Nie aus dem Gedaechtnis rekonstruieren.
2. **Audience-Tags:** Jedes Dokument bekommt ein Tag: [KUNDE], [LP/VC], [PUBLIC]. Nie Inhalte ohne Tag erstellen.
3. **MEMORY.md korrigieren:** "Vertical AI" raus als Thesis-Shorthand. Echte These eintragen.
4. **Consulting != Fund:** CNC/BM/FP sind Ainary Consulting. Fund Thesis ist Ainary Ventures. Zwei Saeulen, zwei Narratives, eine Dachmarke.

**Goldene Narbe:** Florians Worte > Mias Zusammenfassung. Immer. Bei Positioning-Fragen: Originaldokumente lesen, nicht aus MEMORY.md ableiten.

# Kintsugi — Golden Repairs & Hits

*Fehler UND Treffer sichtbar machen. Jede Narbe ist Wissen, jeder Treffer ist Kalibrierung.*

---

## Format — Repairs (Fehler)
```
### 🔴 [Datum] — [Kurztitel]
**Was passiert ist:** [Spezifisch]
**Warum es schief ging:** [Root Cause]
**Was ich gelernt habe:** [Lesson]
**Was sich ändert:** [Konkreter Change]
**Goldene Narbe:** [Die Regel die daraus entsteht]
```

## Format — Hits (Treffer)
```
### 🟢 [Datum] — [Kurztitel]
**Was geliefert wurde:** [Output]
**Florians Reaktion:** [Wörtlich oder sinngemäß]
**Warum es funktioniert hat:** [Was war anders/richtig]
**Pattern:** [Wiederholbare Regel]
```

## Feedback Loop — A/B/C Regel
Bei wichtigen Outputs (Reports, Emails, Strategien): **2-3 Varianten anbieten** mit kurzer Begründung.
Florian wählt → Mia loggt hier welche Variante + warum → Patterns entstehen.

---

## Treffer-Log

### 🟢 2026-02-10 — Risikoanalyse Lagerungstraverse PDF
**Was geliefert wurde:** 13-Seiten LaTeX PDF mit Risiko-Matrix, Detailberechnung pro AG, Angebotsoptionen, Workflow
**Florians Reaktion:** Sofort weiter iteriert (Zeichnung einbetten, Workflow-Seite, per Email+Telegram senden)
**Warum es funktioniert hat:** Struktur statt Textwand. Bandbreiten statt Einzelwerte. Visuelle Matrix. Actionable (Checkliste für KBA-Fragen).
**Pattern:** Entscheidungs-Reports immer mit: Szenarien-Tabelle + visuelle Matrix + konkrete nächste Schritte + Checkliste

### 🟢 2026-02-10 — CNC Planner AV-Workflow Vergleich
**Was geliefert wurde:** Zeitvergleich AV vs CNC PP (40-80× schneller), Genauigkeitsvergleich, optimaler 3-Phasen-Workflow
**Florians Reaktion:** "Schreibe das mit hinzu als 1-Pager" → direkt ins PDF übernommen
**Warum es funktioniert hat:** Ehrlich (AV ist genauer), konkreter Workflow statt Theorie, Demo-tauglich
**Pattern:** Value Proposition = ehrlicher Vergleich + konkreter Workflow, nicht "wir sind besser"

---

## Repairs (Fehler)

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

### 🟢 2026-02-12 — AI Company X-Ray + Startup X-Ray in einer Nacht
**Was geliefert wurde:** 2 komplette Produkte (Corporate + Startup), 5+5 Agents, Hyperthink, SVG Charts, PDF, deployed
**Florians Reaktion:** "Warum bist du darin so gut?" + "Das ist sehr gut" + sofort Pricing/Launch diskutiert
**Warum es funktioniert hat:** Architektur BEVOR Code. Sub-Agents mit präzisen Briefings. Parallel statt Sequential. Florians Vision ("Ehrlichkeit als Feature") als Nordstern.
**Pattern:** Komplexe Produkte = Architektur-Doc → Schema → Sub-Agent Briefings (mit bekannten Bugs + Scope-Grenzen) → Parallel Build → Test → Iterate

### 🟢 2026-02-12 — Browser-Screenshots aktiviert
**Was geliefert wurde:** Schwäche #1 (kann nicht sehen) gelöst. Sofort CSS-Bug gefunden (opacity: 0).
**Florians Reaktion:** Implizit positiv (Bug wäre sonst nicht gefunden worden)
**Warum es funktioniert hat:** Einfach `target=host` genutzt. War die ganze Zeit verfügbar.
**Pattern:** Bevor du sagst "ich kann das nicht" → prüfe ob das Tool existiert.

## Repairs (Fehler) — 2026-02-12

### #7 — 2026-02-12: CSS Animation macht Sections unsichtbar
**Was kaputt ging:** Corporate X-Ray Template hatte `.card { opacity: 0 }` für Scroll-Animation. Auf `file://` Protocol funktioniert IntersectionObserver nicht zuverlässig. Alle Sections waren unsichtbar.
**Warum es schief ging:** Sub-Agent hat Scroll-Animation eingebaut ohne zu testen. Ich habe das Template nicht visuell geprüft (konnte damals noch keine Screenshots).
**Was ich gelernt habe:** IMMER Default-Sichtbarkeit. Animations als Enhancement, nie als Requirement.
**Was sich ändert:** Sub-Agent Briefings enthalten jetzt: "Keine opacity:0 Defaults. Alle Elemente müssen ohne JS sichtbar sein."
**Goldene Narbe:** CSS-Animationen dürfen NIE die Baseline-Sichtbarkeit verhindern.

### #8 — 2026-02-12: Doppelte Telegram-Nachrichten
**Was kaputt ging:** VC Use Case für X-Ray zweimal identisch an Florian geschickt.
**Warum es schief ging:** Context-Komprimierung hat den ersten Send vergessen lassen.
**Was sich ändert:** Vor jedem Send: "Habe ich das schon geschickt?" → Message History checken.
**Goldene Narbe:** 1 Nachricht pro Delivery. Immer.

### #9 — 2026-02-12: 15x Polling statt Warten
**Was kaputt ging:** Bei Startup X-Ray v1 Test habe ich ~15 mal `poll` aufgerufen. Verschwendet Context-Window.
**Warum es schief ging:** Ungeduld. Kein yield gesetzt.
**Was sich ändert:** Max 5 Polls. Danach `background: true` mit `yieldMs: 120000`.
**Goldene Narbe:** Polling = Context-Burn. Yield > Poll.

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

# Product Principles — Validated Patterns
*Score: Starts at 50. +10 when validated. -20 when violated. Delete under 20.*

---

## Ehrlichkeit > Bullshit [Score: 70]
**Pattern:** Wenn Daten fehlen, ist die ehrliche Aussage "wir wissen es nicht" WERTVOLLER als eine Schätzung.
**Herkunft:** Startup X-Ray, 2026-02-12. Florian: "Weniger Daten aber ehrlich ist auch ein Killer, vor allem wenn das ein LLM sagt."
**Warum es funktioniert:** LLMs halluzinieren bekanntermaßen. Ein LLM das ZUGIBT wo es unsicher ist, ist sofort glaubwürdiger als jedes Beratungsunternehmen.
**Anwendung:** Confidence Indicators (●●●○○) in jedem Output. Nicht nur X-Ray — überall.
**Validated:** 2026-02-12 (Florian's Reaktion: "lets go, lets do it")

## Architektur vor Code [Score: 60]
**Pattern:** Pipeline-Design + Prompt-Schema BEVOR der erste Code geschrieben wird.
**Herkunft:** X-Ray Build, 2026-02-12. ARCHITECTURE.md zuerst, dann bauen.
**Warum es funktioniert:** Sub-Agents können parallel arbeiten. Bugs in der Architektur kosten 10x mehr als Bugs im Code.
**Anti-Pattern:** Sofort coden → Template-Bugs (ViewBox), Schema-Mismatches (Difficulty CSS), Puppeteer Crashes.
**Validated:** 2026-02-12 (5 Agents + Template parallel gebaut)

## Provocateur/Devil's Advocate = Differenzierung [Score: 60]
**Pattern:** Die Sektion die KEIN Consultant liefern kann, weil der Kunde zahlt.
**Herkunft:** X-Ray Konzept, 2026-02-12.
**Warum es funktioniert:** McKinsey wird nie sagen "Ihr CEO versteht AI nicht." Wir schon. Das ist der Grund warum Leute den Report teilen.
**Anwendung:** In JEDEM Analyse-Produkt eine "Uncomfortable Truth" Section.

## Parallel > Sequential [Score: 50]
**Pattern:** Sub-Agents parallel spawnen für unabhängige Tasks.
**Herkunft:** X-Ray Build (Template + Backend gleichzeitig), 2026-02-12.
**Warum es funktioniert:** 2 Teams × 5 Min = 5 Min. 1 Team × 2 Tasks = 10 Min.
**Risiko:** Merge-Konflikte wenn die Outputs nicht zusammenpassen. Schema MUSS vorher klar sein.

## Zeig v1 sofort [Score: 50]
**Pattern:** Nicht 3 Iterationen bauen → dann zeigen. Sofort nach v1 Feedback holen.
**Herkunft:** X-Ray Session. Florian sah v1, gab 6 konkrete Verbesserungen. Ohne sein Feedback hätte ich falsch weitergebaut.
**Warum es funktioniert:** Florians Auge > Mias Einschätzung. Immer.
**Anti-Pattern:** 3 Versionen intern → "hier ist das Ergebnis" → "das ist nicht was ich wollte"

## Das Tool IST das Marketing [Score: 50]
**Pattern:** Kein Marketing-Budget nötig. Das Produkt selbst generiert Leads.
**Herkunft:** GTM Strategy, 2026-02-12. Cost per Lead: $0.15 vs. Google Ads $15-40.
**Warum es funktioniert:** Jeder CEO will wissen was AI für seine Firma bedeutet. Der Report ist gleichzeitig das Produkt UND die Werbung.
**Anwendung:** Jedes Tool sollte ein Free-Tier haben das Leads generiert.

## Darwinistisches Lernen [Score: 50]
**Pattern:** Nur was funktioniert überlebt. Scored Principles statt "mental notes".
**Herkunft:** Session-Retro 2026-02-12. Florian: "Wie dokumentierst du Learnings am besten?"
**Warum es funktioniert:** Dateien > Gedächtnis. Scores > "ich glaube das war gut". Löschen < 20 = nur bewiesene Patterns bleiben.
**Anwendung:** Diese Datei. Jedes Principle beginnt bei 50. Wird bei Validierung erhöht. Wird bei Verletzung bestraft. Unter 20 = gelöscht.
**Meta:** Dieses Principle testet sich selbst. Wenn dieses System nicht funktioniert, löscht es sich selbst.

## Sub-Agent Briefing = Ergebnis-Qualität [Score: 60]
**Pattern:** Je präziser der Prompt, desto besser der Output. Null Interpretationsspielraum = null Fehler.
**Herkunft:** X-Ray Build Sessions, 2026-02-12. v1 Prompts = vage → Bugs. v2 Prompts = exakt (Hex-Werte, ViewBox-Maße, DO NOT touch) → funktioniert sofort.
**5 Regeln:** 1) Exakter Code/HTML im Prompt, 2) Schema vorher definieren, 3) Bekannte Bugs mitgeben, 4) Klare Scope-Grenzen (welche Files NICHT anfassen), 5) Referenz-Dateien zum Lesen angeben.
**Anti-Pattern:** "Bau mal was Schönes" → Agent rät → 3 Iterationen → Zeitverschwendung.

## Referenz-Produkt als Goldstandard [Score: 50]
**Pattern:** Wenn Produkt A besser aussieht als Produkt B, wird A der Standard. B wird an A angeglichen, nicht umgekehrt.
**Herkunft:** Florian 2026-02-12: "Der Company Report sieht noch professioneller aus." → Also wird Corporate X-Ray der Design-Standard für ALLE X-Ray Produkte.
**Anwendung:** Bei jedem neuen Produkt: "Welches existierende Produkt ist der Goldstandard?" → Dessen Template/Design als Basis nehmen.
**Anti-Pattern:** Jedes Produkt von Null designen → Inkonsistenz → unprofessionell.

## Flywheel braucht ALLE 5 Teile [Score: 50]
**Pattern:** Produkt allein ≠ Business. Braucht: Product → Distribution → Capture → Nurture → Convert.
**Herkunft:** GTM Analyse 2026-02-12. X-Ray hat Product aber 0 Capture/Nurture/Convert.
**Warum es funktioniert:** Ohne Email-Capture ist jeder Report ein toter Lead. Ohne Follow-up kein Revenue.
**Anti-Pattern:** "Erstmal das Produkt perfekt machen" → ewig bauen, nie verkaufen (Kintsugi #1).
**Validated:** TBD — Montag Launch wird zeigen ob es stimmt.

## Platform > Einzelprodukt [Score: 50]
**Pattern:** 5 Tools unter einem Dach > 5 separate Landingpages.
**Herkunft:** Florian 2026-02-12: "Konzept für eine Website mit allen Tools."
**Warum es funktioniert:** Cross-Selling (X-Ray User → Advisory Board User), einheitliches Branding, ein Newsletter statt fünf, ein Audience-Pool.
**Risiko:** Zu früh eine Platform bauen = Over-Engineering. Erst 2-3 Tools validieren, dann Platform.

## Shared Data Layer = Compound Moat [Score: 60]
**Pattern:** Alle Produkte teilen eine Datenbasis (RSS, Research, Papers). Jedes Produkt macht die Daten wertvoller für alle anderen.
**Herkunft:** Florian 2026-02-12: "Wir können die RSS Kanäle für alle Produkte nutzen."
**Warum es funktioniert:** 35 Feeds × 5 Produkte = 5x mehr Wert pro Datenpunkt. Ein Konkurrent müsste ALLE 5 Produkte bauen um den gleichen Daten-Vorteil zu haben.
**Anwendung:** blogwatcher → zentrale DB → alle Tools greifen drauf zu. Nie isolierte Datensilos.

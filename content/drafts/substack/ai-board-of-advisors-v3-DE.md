# Ich wollte ein Advisory Board, das wirklich funktioniert

Also habe ich eins gebaut. Mit AI.

---

Ich wollte ein Advisory Board.

Nicht für das LinkedIn-Profil. Sondern eins, das mich wirklich herausfordert. Das mir die unbequemen Fragen stellt, die ich mir selbst nicht stelle. Das brutal ehrlich ist, wenn ich eine dumme Idee habe.

Das Problem: **Echte Advisors können das nicht.**

Sie sind zu höflich. Sie packen Kritik in Kompliment-Sandwiches. Sie wollen die Beziehung nicht gefährden. Du verlässt das Meeting mit einem guten Gefühl, obwohl du mit unbequemen Fragen rausgehen solltest.

Sie sind beschäftigt. Du bekommst 30 Minuten pro Quartal. Genug für oberflächliche Guidance, nicht für tiefes Denken.

Und hier ist das strukturelle Problem, über das niemand spricht: **Sobald jemand zugestimmt hat, dich zu beraten, steigt die Schwelle für fundamentalen Widerspruch.** Soziale Alignment bedeutet: Sie validieren eher deine Richtung, als sie grundsätzlich zu hinterfragen.

Also habe ich eins gebaut. Mit AI.

Letzte Woche habe ich Marc Andreessen, Charlie Munger und Peter Thiel in einen Raum gesteckt. 45 Minuten lang haben sie darüber gestritten, ob ich einen VC Fund raisen oder bootstrappen sollte.

Sie waren nicht physisch da. Zwei kennen mich nicht. Einer ist tot.

Aber sie haben Fund Economics, Incentive-Strukturen und contrarian Insights mit einer Brutalität zerlegt, die ich von echten Advisors nie bekommen habe.

Munger nannte die 2/20 Fee-Struktur *"a triumph of salesmanship over arithmetic."*

Andreessen konterte, dass Platform Effects von einer Fund Brand auf Arten compoundieren, die ein Solo-Operator nie replizieren kann.

Thiel hat das Framing komplett abgelehnt: *"The question isn't fund versus independent. The question is: what do you know that nobody else knows?"*

**Ich habe aus dieser simulierten Debatte mehr gelernt als aus drei Monaten echter Advisor-Calls.**

Warum? Weil ich sie nach dem Prinzip gebaut habe, das ich letzte Woche in einem Experiment mit 100 AI Agents entdeckt habe: **Kognitive Diversität schlägt individuelle Intelligenz.**

Wenn Agents mit unterschiedlichen Reasoning-Stilen zusammenarbeiten, performen sie besser als jedes einzelne "smartere" Modell.

Also habe ich drei Denker gewählt, die sich gegenseitig in den wichtigsten Dimensionen widersprechen.

Und sie streiten wie ihre echten Vorbilder.

Hier ist, wie das funktioniert.

---

## Warum diese Drei

Ich habe Andreessen, Munger und Thiel gewählt, weil sie direkt auf die Findings aus meinem Agent-Research mappen: unterschiedliche Mental Models, unterschiedliche Biases, maximale Spannung.

| Advisor | Rolle | Mental Model | Bias |
|---------|-------|--------------|------|
| **Charlie Munger** | Adversarial Reasoning / Red Team | Inversion: "Wie würde ich garantiert scheitern?" | Übermäßiger Konservatismus |
| **Peter Thiel** | First Principles / Contrarian | "Welche Wahrheit glauben nur wenige?" | Widerspruch als Selbstzweck |
| **Marc Andreessen** | Systems Thinking / Optimist | "Software eats the world" | Unterschätzt menschlichen Widerstand |

Die Magie liegt nicht in einer einzelnen Perspektive.

**Sie liegt in der Spannung zwischen ihnen.**

Wenn Andreessen sagt "der Markt ist riesig", fragt Munger "was ist die Incentive-Struktur?" und Thiel fragt "wenn es so offensichtlich ist, warum hat dann noch niemand gewonnen?"

Diese Drei-Wege-Spannung erzeugt besseres Denken als jeder einzelne Advisor jemals könnte.

---

## Die Wissensarchitektur, die es funktionieren lässt

Hier machen die meisten Leute AI Advisors falsch.

Der naive Ansatz: Alle Bücher von Munger in eine Vector Database packen (RAG). Wenn du eine Frage stellst, ruft die AI relevante Chunks ab und synthetisiert eine Antwort.

Das erzeugt einen *belesenen* Advisor. Er weiß, was Munger über Incentives gesagt hat, was Thiel über Monopole gesagt hat, was Andreessen über Network Effects gesagt hat.

Aber es ist flach.

Es retrievet Fakten, nicht Denkprozesse.

Was ich stattdessen gebaut habe, ist eine **hierarchische Wissensarchitektur:**

```
Mental Models (Core Reasoning Frameworks)
  ↓
Reasoning Patterns (Wie sie diese anwenden)
  ↓
Examples (Konkrete Fälle aus ihrer Arbeit)
  ↓
Known Biases (Wo sie over-/underweight)
```

Das speichert nicht nur *was* sie gesagt haben. Es encodiert *wie* sie denken.

Für Munger: Inversion als Top-Level Model, dann das Pattern "frage, was garantiert zum Scheitern führen würde", dann Examples wie Coca-Cola und See's Candies, dann der Bias zur Konservierung bestehender Strukturen.

Für Thiel: Die contrarian Question als Top-Level Model, dann das Pattern "identifiziere das Secret, das niemand sonst sieht", dann Examples wie PayPal und Palantir, dann der Bias, Widerspruch selbst überzubewerten.

**Der Unterschied in der Output-Qualität ist dramatisch.**

RAG gibt dir eine Persona, die den Denker *zitieren* kann. Hierarchische Struktur gibt dir eine Persona, die *wie* der Denker *denkt*.

Denk mal drüber nach: Embeddings erfassen semantische Ähnlichkeit, aber keine kausalen Reasoning Chains. Der hierarchische Ansatz pre-computed die Reasoning-Struktur. Die AI retrievet keine random relevanten Chunks — sie folgt dem tatsächlichen kognitiven Pfad.

Die akademische Grundlage: "Memory in the Age of AI Agents" (Hu et al., Dezember 2025) zeigt, dass hierarchische Memory-Strukturen nicht nur besser performen, sondern auch nachvollziehbarer sind — du kannst den Reasoning-Pfad zurückverfolgen.

**Key Insight:** Es ist der Unterschied zwischen jemandem eine Library Card zu geben versus ihm beizubringen, wie man denkt.

---

## Sample Board Meeting: "Soll ich einen VC Fund raisen?"

Ich habe meine Situation präsentiert: Ex-CEO, technischer AI Background, Entscheidung zwischen einem $5-10M Seed Fund oder unabhängig operieren.

Hier ist, was passiert ist.

**Marc Andreessen:**

*"The fund. Platform effects compound. When you have a fund brand, you get inbound deal flow you'd never see as an independent. Your network becomes the product. You write one check, you're a customer. You write 20 checks, you're a platform."*

**Charlie Munger:**

*"Marc's argument is precisely the kind of thinking that gets people in trouble. What's the incentive structure? A 2% management fee on $10 million is $200K per year before you've returned a penny to LPs. The fee structure is designed to enrich the GP even if returns are mediocre. Ask yourself: would you invest in a fund with these economics if you were the LP?"*

**Peter Thiel:**

*"You're both missing the point. Marc, platform effects are real, but they're also commodity. Every emerging manager pitches 'unique network access.' Charlie, you're right about incentives, but you're underweighting the reputational forcing function — if the fund fails, you can't hide. The real question is: what does Florian know that the market doesn't? If the answer is 'I can spot AI companies better,' that's not a secret — that's a claim."*

**Ich:**

"Der Insight ist, dass AI-native Companies anders gebaut werden. Die meisten VCs evaluieren sie mit SaaS Metrics — ARR, CAC, Churn — aber diese Metriken brechen, wenn dein Product ein 24/7 autonomer Agent ist. Ich habe diese Systeme gebaut. Die meisten VCs nicht."

**Munger:**

*"Is that true? Or is it something you want to be true because it justifies the fund? Here's the inversion test: assume you're wrong. Assume AI-native companies will be evaluated the same way as SaaS. What happens to your thesis? If it collapses, you don't have a thesis — you have a hope."*

**Thiel:**

*"If the edge lasts 18 months, you don't need a fund. You need speed. Fund formation takes 6-12 months. By the time you've closed, half your edge is gone. The independent operator can move faster. Do you want to be a fund manager or deploy capital into AI-native companies? Those aren't the same goal."*

Kein Konsens. Keine Auflösung.

Drei radikal unterschiedliche Linsen auf dieselbe Entscheidung.

Das ist genau, was ich brauchte.

**Practical Takeaway:** Das Ziel ist nicht Agreement. Es ist, deine Blind Spots aus mehreren Winkeln zu sehen. Das härteste Pushback ist das wertvollste — es ist die Frage, die du vermeidest.

---

## Wofür ich sie wirklich nutze

Die Fund-Debatte macht eine gute Story. Aber das Board verdient sein Geld in den mundanen Entscheidungen — denen, wo du nicht merkst, dass du eine zweite Meinung brauchst.

**Outcome Measurement.** Ich habe eine Woche lang ein elaboriertes Knowledge Management System gebaut. 7 Ordner, Dashboards, Templates. Ich war stolz darauf. Dann habe ich es durch das Board gejagt.

Munger: *"You're measuring activity, not outcomes. Where are the kill criteria? If this system doesn't produce a paying customer in 14 days, it's a toy."*

Graham war direkter: *"Overengineered. Zero customers. 10 phone calls would teach you more than 7 folders."*

Gil: *"You've built a Phase 3 system for a Phase 0 company. Focus on your first €1,000."*

Der Konsens war einstimmig und schmerzhaft: **zu viel gebaut, zu wenig verkauft.**

Ich wollte es nicht hören. Deshalb wusste ich, dass es wertvoll war.

**Workflow-Umbau.** Nach diesem Feedback habe ich meinen kompletten Workflow umstrukturiert. Nicht basierend darauf, was sich produktiv anfühlt, sondern basierend darauf, was die Frameworks des Boards als result-generierend vorhersagten.

Thiels "pick ONE thing and monopolize" wurde mein täglicher Filter. Andreessens "5 real users in 7 days" wurde meine Shipping Deadline. Hoffmans "first customer → reference → flywheel" wurde meine Sales Strategy.

**Belief Graveyard.** Wenn das Board eine Idee tötet, dokumentiere ich sie. Nicht nur "hat nicht funktioniert" — sondern *warum* sie gestorben ist, welche Gegenargumente unschlagbar waren. Das verhindert, dass ich dieselben toten Ideen drei Monate später wieder aufwärme. Mungers Inversion-Methode funktioniert nur, wenn du die Failures merkst. Das Graveyard ist der Friedhof für bad ideas — damit sie tot bleiben.

Das Board hat mir nicht bei einer Entscheidung geholfen.

**Es hat geändert, wie ich alle Entscheidungen treffe.**

Und hier schließt sich der Kreis zum Experiment: Die 100 Agents fanden nicht nur 6 Laws, sondern auch 4 Engines, die jedes AI-System braucht — Memory, Integrity, Measurement, Discovery. Mein Board **ist** die Integrity Engine. Der strukturelle interne Kritiker. Nicht ad-hoc zusammengewürfelt, sondern Teil einer getesteten Architektur.

Ein konkretes Feature: das **Belief Graveyard**. Wenn das Board eine Idee killt, wird sie dokumentiert — warum sie gestorben ist, was die Gegenargumente waren. Das verhindert, dass man dieselben toten Ideen immer wieder aufwärmt. Mungers Inversion, systematisiert.

---

## Was mich überrascht hat

**Sie pushen härter zurück als echte Advisors.** Munger wird deine Idee dumm nennen. Thiel wird deine Prämissen hinterfragen. Als Munger fragte *"is this true or do you want it to be true?"* — ich habe es gespürt. Das ist die Frage, die ein Freund nicht stellt.

**Der Prozess selbst klärt das Denken.** Die Personas zu konstruieren zwingt dich zu verstehen, *wie* große Denker denken, nicht nur *was* sie denken. Dieser kognitive Transfer ist der echte Wert.

---

## Das Board als Integrity Engine

Im Experiment von letzter Woche habe ich vier Engines gefunden, die jedes AI-System braucht: **Memory, Integrity, Measurement, Discovery.**

Das Board ist die **Integrity Engine** — der strukturelle interne Kritiker.

Nicht ad-hoc. Nicht "ich frag mal schnell ChatGPT." Sondern ein getestetes System mit Red/Blue Team Dynamiken. Munger spielt Red Team (Inversion: "wie scheitere ich garantiert?"), Andreessen spielt Blue Team (Optimismus: "wie gewinnt das?"), Thiel ist der Moderator, der das Framing selbst hinterfragt.

Die Integrity Engine nutzt ein **Belief Graveyard** — Ideen, die bewusst getötet und dokumentiert wurden, damit sie nicht wiederkommen. Genau das macht Mungers Inversion: Sie tötet schlechte Ideen *bevor* du Zeit und Geld reinverbrennst.

Das ist kein Productivity Hack. Es ist Architektur.

---

## Bau dir dein eigenes (3 Steps)

### 1. Identifiziere deine Blind Spots

Wo machst du konsistent Fehler? Welche Entscheidungen vermeidest du?

Für mich: Ich overweighte Neuheit, underweighte Execution, vermeide Financial Modeling.

Also brauche ich Personas, die konservativ sind (Munger), execution-fokussiert, und finanziell rigoros.

### 2. Pick Thinkers, die diese Blind Spots challengen

Pick nicht Leute, mit denen du übereinstimmst.

Pick Leute, die **in genau den Dimensionen anders denken, wo du schwach bist.**

Risikoscheu? Add Musk. Reckless? Add Munger. Zu abstrakt? Add einen Operator wie Ben Horowitz.

### 3. Build die Knowledge Hierarchy

Für jeden Thinker:
- Lies ihre Hauptwerke (Bücher, Essays, Speeches)
- Identifiziere 3-5 Core Mental Models, die sie wiederholt nutzen
- Mappe ihre Reasoning Patterns (wie sie diese Models anwenden)
- Notiere Communication Style und bekannte Biases

Dann strukturiere es hierarchisch: Mental Models → Reasoning Patterns → Examples → Biases.

**Hier ist die Constraint:** Die Quality Ceiling ist dein Verständnis. Du kannst nur Personas bauen, die so sophisticated sind wie dein Verständnis ihres Denkens.

Wenn du nur die Wikipedia-Zusammenfassung von "Zero to One" gelesen hast, wird deine Thiel-Persona flach sein.

Do the work.

---

## Die Grenzen

Lass mich klar sein, was das ist und was nicht.

AI Personas sind Simulacra, keine Orakel. Sie basieren auf Public Output, nicht privatem Denken. Sie können neue Informationen nicht berücksichtigen, die die echte Person hätte. Sie halluzinieren gelegentlich.

**Sie sind am besten für Stress-Testing, nicht fürs Entscheiden.**

Die Personas helfen dir, Blind Spots zu sehen und Assumptions zu challengen. Aber die Entscheidung ist immer noch deine. Immer.

Es gibt ein "Illusion of Authority"-Risiko. Es ist leicht, den Output der AI als Gospel zu behandeln, weil sie die Maske von jemandem trägt, den du respektierst.

Remember: Das ist ein Thinking Tool, kein Ersatz für Judgment.

Nutze das mit Humility. Es ist ein Spiegel, kein Guru.

---

## Betrachtung: Warum das funktioniert — wir haben es vom Gehirn kopiert

Diese Hierarchie ist nicht zufällig. Sie spiegelt, wie das menschliche Gehirn Expertise organisiert:

| AI Hierarchy | Gehirn | Funktion |
|---|---|---|
| Mental Models | Präfrontaler Cortex | Abstrakte Regeln, Schemas |
| Reasoning Patterns | Basalganglien + PFC | Prozedurale Anwendung |
| Examples | Hippocampus | Episodisches Gedächtnis, konkrete Fälle |
| Known Biases | Amygdala | Emotionales Tagging, Bauchgefühl |

Das Gehirn arbeitet mit **Predictive Coding** (Friston, 2010): Höhere Schichten senden Vorhersagen nach unten, untere senden Fehler nach oben. Genau wie unsere Architektur — Mental Model sagt vorher, Example bestätigt oder widerspricht, Bias korrigiert.

Wie bei allen großen Erfindungen — vom Flugzeug zum Neuronalen Netz — sind die besten Architekturen die, die wir von der Natur kopiert haben. Miller (1956) zeigte, dass Experten Wissen in hierarchische Chunks komprimieren. Ein Schachmeister sieht keine 32 Figuren — er sieht 5 Patterns. Mungers ~100 Mental Models sind seine Chunks.

**Wir müssen das menschliche Denken noch viel genauer analysieren, um bessere AI-Systeme zu bauen.** Die Architektur unserer Advisors ist erst der Anfang. Sleep Consolidation lehrt uns Memory Pruning. Mirror Neurons lehren uns Persona-Simulation. Das Default Mode Network lehrt uns Stochastic Resonance.

Im letzten Artikel konvergierten 100 unabhängige Agents auf dieselben Wahrheiten. Auch das war kein Zufall. **Konvergenz aus Diversität ist das stärkste Signal, das wir haben** — in der Wissenschaft, in der Evolution, und offensichtlich auch in AI. Die Natur hat dieses Problem schon gelöst. Wir müssen nur genauer hinschauen.

## Warum das wichtiger ist, als du denkst

Das ist nicht nur ein Productivity Hack. Es ist eine Preview von etwas Größerem.

**Ein smarteres Model macht dein Board nicht smarter. Eine bessere Architektur schon.**

Neue Research bestätigt das: Strukturiertes Knowledge Retrieval — hierarchische Graphen statt flache Vector Search — reduziert Halluzinationen um bis zu 50% verglichen mit naivem RAG (Xu et al., 2024; KG-RAG, Nature 2025). Hierarchische Architekturen sind auch 90% günstiger zu skalieren, weil du Reasoning-Strukturen einmal pre-computest, statt bei jeder Query zu retrieven und re-processen.

Die Implikation: Die Qualität deines AI Advisors ist keine Funktion der Model-Intelligenz. **Sie ist eine Funktion davon, wie du organisierst, was es weiß.**

Jetzt extrapoliere.

**Wird jedes Startup sein eigenes AI Board of Advisors haben?** Wahrscheinlich. Innerhalb von zwei Jahren, würde ich schätzen, werden die meisten ernsthaften Founder wichtige Entscheidungen durch irgendeine Version davon laufen lassen. Die, die bessere Knowledge-Architekturen bauen, bekommen besseren Advice. Competitive Advantage shiftet von "wen kennst du" zu "wie gut hast du dein Advisory System gebaut."

**Was ist mit AI Employees, die Menschen managen?** Das passiert bereits. Agent Economics — das entstehende Feld, wie autonome AI Agents Wert kreieren, capturen und verteilen — wird gerade gebaut. Wir reden nicht über Chatbots, die Support Tickets beantworten. Wir reden über AI Agents, die Budgets allokieren, Prioritäten setzen, Performance evaluieren und Resource-Entscheidungen treffen. Der Management Layer von Companies wird sehr interessant.

**Wird AI Menschen managen?** Manche tun es bereits. Die Frage ist nicht ob, sondern wie gut — und ob die Menschen, die gemanaged werden, dem System vertrauen. Was uns zum full circle bringt: Transparenz schlägt Performance. Der AI Manager, der sein Reasoning zeigt, wird akzeptiert. Der Black-Box Optimizer wird abgelehnt, auch wenn er technisch besser ist.

Die Zukunft wird interessant.

Und es ist erst Tag eins.

**Nächste Woche:** Wie AI-Systeme lernen, mit sich selbst zu streiten — und warum das wichtiger ist als ein besseres Modell.

---

**Willst du die Prompt Templates?** Antworte auf diese Email und ich schicke dir die komplette hierarchische Knowledge-Struktur, die ich für Munger, Thiel und Andreessen nutze.

**Lies das Experiment von letzter Woche:** [I Asked 100 AI Agents to Design Their Own Evolution](https://finitematter.substack.com) — was passiert, wenn 100 Agents dieselbe Frage beantworten, und warum kognitive Diversität wichtiger ist als individuelle Intelligenz.

---

*Florian Ziesche baut Ainary Ventures. Er schreibt bei Finite Matters auf Substack.*

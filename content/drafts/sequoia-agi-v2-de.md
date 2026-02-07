# Sequoia sagt, AGI ist da. Sie haben recht — und auch nicht.

*Die schärfsten VCs der Welt haben den Meilenstein richtig erkannt — aber die falsche Ziellinie benannt.*

---

Sequoia Capital hat gerade "2026: This is AGI" veröffentlicht. Nicht "wir kommen näher". Nicht "fast da". **Das ist AGI.**

Von einem der führenden Tech-Investoren der Welt ist das keine Hype-Behauptung — das ist eine These. Und die Daten sind tatsächlich beeindruckend.

METR-Benchmarks zeigen, dass sich AI-Task-Horizonte alle ~7 Monate verdoppeln — und beschleunigen. Claude Opus 4.5 löst inzwischen etwa 50% der Aufgaben, für die menschliche Experten fünf Stunden brauchen. Diese Systeme verketten Reasoning, nutzen Tools, debuggen ihre eigenen Fehler und arbeiten mehrstündige Aufgaben ab. Sequoias Definition: AGI ist "die Fähigkeit, Dinge herauszufinden". Drei Zutaten — Pre-Training (Wissen), Inference-Time Compute (Reasoning), Long-Horizon Agents (Iteration).

Ich will dieses Argument ernst nehmen. Wenn Sequoia so eine steile These aufstellt, verdient das fundierte Auseinandersetzung, keinen Quick Take.

Aber als jemand, der täglich AI in Fabriken und Unternehmen ausrollt, sehe ich etwas, das ihr Framework übersieht. Nicht weil sie falsch liegen, was AI heute kann — sondern weil ihre Definition verschleiert, was sie immer noch nicht kann.

**Die Lücke ist nicht Streaming-Input. Es sind Weltmodelle.**

---

## Was sie richtig sehen

Seien wir ehrlich: Die Agenten, die gerade ankommen, sind qualitativ anders als die Chatbots von 2023.

Sarah Guos Framing trifft es: "Bald kannst du einen Agenten einstellen." Nicht prompten. *Einstellen*. Gib ihm ein Problem, geh weg, komm zu Ergebnissen zurück. Sequoias Recruiting-Beispiel — wo ein Agent autonom von LinkedIn zu YouTube-Talks zu Twitter-Engagement zu personalisierter Outreach-Mail pivotiert, in 31 Minuten — das ist real. Ich habe meinen eigenen AI-Agenten Research-Briefs produzieren, technische Dokumente draften und mehrstufige Analysen durchführen sehen, für die ich Tage gebraucht hätte.

Die METR-Daten sind schwer zu bestreiten: sechs Jahre konsistentes exponentielles Wachstum bei Task-Horizonten. Neuere Modelle revidieren nach *oben*. Die Verdopplungszeit verkürzt sich von 7 auf 3 Monate. Wenn man dem Trend glaubt, sind ganztägige Tasks bis 2028 und jahrelange Tasks bis 2034 keine unrealistischen Extrapolationen.

Also ja — hier ist tatsächlich etwas grundlegend Neues. Sequoia liegt nicht falsch beim Meilenstein.

Sie liegen falsch bei der Bedeutung.

---

## Die Weltmodell-Lücke

Das macht aktuelle AI wirklich, egal wie ausgeklügelt das Agent-Scaffolding ist:

1. Empfängt ein Context Window (einen Snapshot der Welt)
2. Verarbeitet diesen Snapshot
3. Liefert Output
4. Wartet auf den nächsten Snapshot

Du kannst diese Schleife schneller machen. Du kannst das Context Window vergrößern (Gemini macht 1M+ Tokens). Du kannst Tool Use hinzufügen, sodass das Modell zwischen Steps Datenbanken und APIs abfragt. OpenAIs Realtime API verarbeitet sogar Streaming-Audio mit <200ms Latenz.

Aber nichts davon löst das fundamentale Problem: **Aktuelle AI hält kein prädiktives Modell der Welt aufrecht, das kontinuierlich updated.**

Ein Mensch, der an einer komplexen Aufgabe arbeitet, verarbeitet nicht nur Information — er *antizipiert*. Du siehst eine Tasse Richtung Tischkante rutschen und greifst danach, *bevor* sie fällt. Du spürst eine Verhandlung kippen und passt deine Strategie an, *während* es passiert, nicht nachdem dir jemand das Meeting zusammengefasst hat. Du baust kausale Modelle aus kontinuierlicher Beobachtung: "die Linie läuft heute heiß", "dieser Kunde wirkt abgelenkt", "der Markt-Ton hat sich diese Woche verändert".

Aktuelle AI — selbst Sequoias "generally intelligent agents" — reagiert auf das, was passiert ist. Sie antizipiert nicht, was gleich passieren wird.

Wie Angjoo Kanazawa von UC Berkeley es formuliert: "Wie entwickelt man ein intelligentes System, das tatsächlich Streaming-Input haben und sein Verständnis der Welt updaten kann? Das ist ein großes offenes Problem. Ich denke, AGI ist ohne Lösung dieses Problems nicht möglich."

---

## Wo das in Production auftaucht

Die Lücke ist unsichtbar in Benchmarks. Sie ist offensichtlich im Deployment.

**In einer Fabrik:** Wir haben Computer Vision zu Automotive-OEMs ausgerollt — BMW, Siemens, Bosch. Die Modelle waren exzellent bei statischen Bildern. Aber Fertigung ist kontinuierlich: Licht verändert sich, Material-Batches variieren, Operatoren justieren Einstellungen. Ein Snapshot-basiertes System verarbeitet Frame 1, liefert ein Urteil, verarbeitet Frame 2. Jedes Urteil ist isoliert. Es baut nie ein Modell von "diese Schicht läuft anders als gestern". Die Operatoren wissen das. Die AI nicht.

**In einer Redaktion:** AI kann Artikel aus Briefings draften. Aber ein Reporter an einer Breaking Story integriert kontinuierlich neue Signale — eine Quelle textet zurück, ein anderes Outlet veröffentlicht einen Winkel, ein Livestream offenbart etwas Unerwartetes. Das mentale Modell des Reporters updated in Echtzeit. Aktuelle AI erfordert Re-Prompting: "Hier ist das Update, regeneriere." Es ist ein Writing-Tool, kein Kollege, der die Story mit dir trackt.

**In Rechtsverhandlungen:** AI liest Verträge und flaggt Risiken brillant — bei statischen Dokumenten. Aber während eines Live-Deals verschieben sich Konditionen über E-Mails, Calls und Nebengespräche. Ein menschlicher Verhandler hält ein lebendes Modell von "wo wir gerade stehen" aufrecht. Ein AI-Agent verarbeitet jedes Update als separaten Batch.

Factory.ai hat die tiefere technische Einschränkung identifiziert: Selbst Million-Token-Context-Windows leiden unter "Context Rot" — Modelle nutzen ihren Kontext nicht gleichmäßig, Performance degradiert mit wachsendem Input. Größere Windows sind nicht die Lösung. Bessere Weltmodelle sind es.

---

## Das ehrliche Gegenargument

Ich will Sequoias Position stahlmännern, weil die stärkste Version ihres Arguments Biss hat:

**"Ist kontinuierliches Weltmodellieren für Wissensarbeit überhaupt wichtig?"**

Vielleicht nicht — für die meisten Tasks. Code schreiben, Daten analysieren, Research betreiben, Dokumente draften — das sind deliberative Tasks, wo Batch-Processing tatsächlich ausreicht. Du brauchst keine Echtzeit-Wahrnehmung, um eine Funktion zu debuggen oder ein Legal Brief zu schreiben.

Selbst menschliche Kognition ist "gechunkter", als wir zugeben wollen. Wir erleben attentional blinks, change blindness, saccadic suppression. Unsere Wahrnehmung ist auch nicht wirklich kontinuierlich — sie ist nur schneller und integrierter als aktuelle AI-Schleifen.

Und das Engineering konvergiert auf etwas, das Streaming *approximiert*: Fast Inference + Tool Use + Long Context + MCP erzeugen Beobachtungsschleifen, die im Sekunden-Frequenzbereich laufen. Für viele Anwendungen ist das gut genug.

Deshalb funktioniert Sequoias Definition *für Wissensarbeit-AGI*. Wenn du das Problem definierst als "ökonomisch wertvolle kognitive Tasks automatisieren", dann ja — Snapshot-basierte Agenten mit engen Iterations-Schleifen werden den Großteil des Values capturen.

**Aber Sequoia hat nicht "Wissensarbeit-AGI" gesagt. Sie haben "AGI" gesagt.**

Und generelle Intelligenz erfordert etwas, das diese Systeme fundamental nicht haben: ein persistentes, prädiktives Modell der Welt, das in Echtzeit updated. Die Art von Verständnis, die dich einen Raum betreten und sofort spüren lässt, dass etwas nicht stimmt. Die Art, die einen Meisterhandwerker fühlen lässt, wann eine Maschine kurz vor dem Ausfall steht. Die Art, die einen großartigen Investor die Mikro-Expressionen eines Founders lesen und seine These mid-conversation anpassen lässt.

---

## Was das bedeutet

**Für Builder:** Die größte Opportunity ist, die Weltmodell-Lücke zu schließen. Nicht nur schnellere Schleifen — echtes kontinuierliches Verständnis. Persistenter State, prädiktive Modelle, antizipatives Verhalten. Die Interfaces der Zukunft werden nicht Prompt-and-Response sein; es wird AI sein, die *präsent* ist — Awareness aufrechterhält und Insights surfaced, ohne gefragt zu werden.

**Für Investoren:** Sequoias "hire an agent"-Framing wird in den nächsten 24 Monaten massive Value Creation in Wissensarbeit treiben. Das ist die offensichtliche Wette. Die asymmetrische Wette liegt in persistenten Weltmodellen — die Companies, die AI bauen, die die Welt nicht nur verarbeitet, sondern ihren Zustand in Echtzeit versteht. Embodied AI, Ambient Computing, kontinuierliche Monitoring-Systeme. Da liegt der nächste Platform-Shift.

**Für Unternehmen:** Deployt aktuelle Agenten aggressiv für klar definierte kognitive Tasks. Sie sind ready. Aber dämpft Erwartungen für Rollen, die kontinuierliches Situationsbewusstsein erfordern. Eure AI kann die Quartalszahlen analysieren. Sie kann noch nicht durch die Fabrikhalle laufen und spüren, was heute anders ist.

---

## Das Gold in den Rissen

Sequoias Essay wird retrospektiv richtungsweisend richtig sein. Der Meilenstein, den sie benennen, ist real. Die Agenten, die jetzt ankommen, werden Industrien reshapen und enormen Value kreieren.

Aber das AGI zu nennen — ohne Qualifikation — überklebt die wichtigste Frontier in AI. Wir haben brillante Batch-Prozessoren gebaut. Wir haben noch keine Systeme gebaut, die kontinuierliches Verständnis der Welt aufrechterhalten.

Die Unterscheidung ist wichtig, weil **der nächste Durchbruch nicht größere Context Windows oder tieferes Reasoning bei statischen Problemen ist. Es sind persistente Weltmodelle — AI, die nicht nur Snapshots der Realität verarbeitet, sondern Zeit wirklich bewohnt.**

Wenn das abstrakt klingt, hier ein konkreter Test: Kann eine AI ein 10-Minuten-Video schauen und vorhersagen, was als nächstes passiert — nicht aus Pattern-Matching, sondern aus Verständnis der Physik, Intentionen und Dynamiken im Spiel? Kann sie Object Permanence aufrechterhalten, wenn Dinge off-screen gehen? Kann sie einen Stimmungswechsel aus einem sich entfaltenden Gespräch detektieren?

Heute lautet die Antwort nein. Wenn die Antwort ja ist, haben wir etwas, das es wert ist, AGI genannt zu werden.

Bis dahin haben wir etwas Bemerkenswertes, Transformatives und grundlegend Neues. Nur nicht ganz das, was Sequoia es genannt hat.

Das Gold liegt in den Rissen zwischen dem, was wir gebaut haben, und dem, was wir als nächstes bauen.

---

*Florian Ziesche ist ehemaliger Startup-CEO (€5,5M+ raised, AI shipped zu BMW, Siemens und Bosch) und arbeitet jetzt als AI-Berater und VC Lab Fellow. Er schreibt über angewandte AI, Venture Capital und die Zukunft menschlich-AI-Kollaboration auf [ainaryventures.com](https://ainaryventures.com).*

---

**🐦 Twitter (280 Zeichen):**
Sequoia hat AGI für angekommen erklärt. Die Daten sind beeindruckend. Aber sie haben die falsche Ziellinie benannt. Aktuelle AI verarbeitet Snapshots brillant. Sie hält keine Weltmodelle aufrecht. Der Unterschied ist nicht akademisch — da liegt der nächste Platform-Shift.

**📊 LinkedIn Hook:**
Sequoia Capital hat gerade gesagt "Das ist AGI". Als jemand, der AI zu BMW und Bosch shipped — sie haben den Meilenstein richtig erkannt, aber die falsche Ziellinie benannt. Was Builder sehen, das VCs übersehen. [link]

---

### Übersetzungsnotizen

**Angepasst für deutsche Leser:**
- Sequoia Capital als "einer der führenden Tech-Investoren der Welt" kontextualisiert (in Deutschland weniger Haushaltsname als im Valley)
- Technische Begriffe teilweise englisch gelassen, wo im deutschen Tech-Diskurs üblich (Reasoning, Inference, Context Window, Batch Processing, Streaming)
- "Stahlmännen" statt "Steelman" (eingedeutschte Form, im rationalistischen Diskurs etabliert)
- Kulturelle Referenzen beibehalten (Kintsugi ist universal, Factory Floor ist in Deutschland mit Automotive-Tradition sogar relevanter)

**Voice beibehalten:**
- Direktheit: "Seien wir ehrlich", "Das ist real", "Die Antwort ist nein"
- Technische Präzision ohne Jargon-Overload
- Operator-Perspektive: Konkrete Beispiele aus Production (BMW, Siemens, Bosch)
- Nuanciert statt polemisch: "Sie haben recht — und auch nicht"

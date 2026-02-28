# Ainary Intelligence — Architektur-Konzept
*Stand: 23. Feb 2026 · Florian + Mia*

---

## Wie Palantir es macht (und was wir daraus lernen)

### Die 5 Kern-Prinzipien von Palantir Gotham

**1. Objekt-zentrisch, nicht seiten-zentrisch.**
In Gotham gibt es keine "Seiten" im klassischen Sinn. Es gibt **Objekte** — Personen, Organisationen, Ereignisse, Orte, Dokumente. Alles ist ein Objekt. Navigation heißt: von Objekt zu Objekt springen. Klick auf "Protschka" → siehst du Protschka. Egal ob du gerade im Graph, in der Timeline oder in der Karte bist. Das Objekt bleibt dasselbe, die **Perspektive** wechselt.

**2. Drei synchrone Perspektiven auf dieselben Daten.**
Gotham zeigt immer drei Views gleichzeitig:
- **Graph** (Netzwerk): Wer hängt mit wem zusammen?
- **Timeline** (Chronologie): Was passierte wann?
- **Map** (Geografie): Wo passierte es?

Klickst du einen Knoten im Graph → highlightet er auf der Timeline und der Map. Die Views sind **live-gelinkt**. Das ist der "Wow"-Moment. Nicht die einzelnen Views, sondern dass sie synchron sind.

**3. Panels, nicht Pages.**
Du verlässt nie deinen Kontext. Details öffnen sich in **Side-Panels** (rechts) oder **Overlays**. Du bleibst auf deinem Canvas. Bei Palantir gibt es keinen "Zurück"-Button, weil du nie wirklich wegnavigierst — du öffnest Schubladen und schließt sie wieder.

**4. Graph ist die primäre Navigation.**
Der Graph IST das Interface. Du tippst nicht in eine Suchleiste und landest auf einer Ergebnisseite. Du siehst das Netzwerk, klickst einen Knoten, und die Detail-Panels aktualisieren sich. Das Netzwerk ist nicht ein Feature — es ist die Hauptnavigation.

**5. Workspace, nicht Dashboard.**
Ein Dashboard zeigt vorgefertigte KPIs. Ein Workspace lässt dich **ermitteln**. Du fügst Objekte hinzu, ziehst Verbindungen, markierst Hypothesen. Es ist ein Werkzeug, kein Report.

---

## Was Ainary aktuell hat (ehrliche Bestandsaufnahme)

| Seite | Was sie tut | Palantir-Äquivalent |
|---|---|---|
| dashboard.html | KPIs + Alerts + Timeline | Dashboard-Widget (Monitoring View) |
| vergleich.html | 5 Personen × 20 Dimensionen | Object Comparison / Multi-Object View |
| gotham.html | Kontroversen-Timeline + Profil | Timeline View + Object Detail |
| network-map.html | Verbindungen + Cross-State Insights | Graph View (aber statisch, kein Force-Graph) |
| dossier-*.html | Vollständige Einzel-Dossiers | Object Detail View (maximiert) |
| chat.html | Frag-Interface für alle Dossiers | AIP (AI Assistant) Overlay |
| index.html | Sales/Landing | Nicht Teil des Produkts |

### Das fundamentale Problem

**Wir haben 6 separate HTML-Seiten die wie ein Report aussehen, nicht wie ein Ermittlungstool.**

Jede Seite ist eine Insel. Der Nutzer muss wissen, welche Seite er braucht. Bei Palantir entscheidet er das nicht — er klickt auf ein Objekt und die richtige Perspektive kommt zu ihm.

---

## Das Konzept: "Investigation Workspace"

### Phase 1: Realistisch (Static HTML, sofort machbar)

Wir können Palantir nicht 1:1 nachbauen (das ist ein $50B-Unternehmen mit Tausenden Ingenieuren). Aber wir können die **wichtigsten Prinzipien** in statischem HTML umsetzen:

#### A. Ein Frame, wechselnde Perspektiven

```
┌──────────────────────────────────────────────────────────┐
│ [● Ainary]  ◉ Graph  ◎ Matrix  ◎ Timeline  ◎ Dossier   │ ← Perspektiven-Switcher
│             ◎ Alerts                          [💬 Mia]   │   (nicht "Seiten")
├──────────┬───────────────────────────────────────────────┤
│          │                                               │
│ SUBJEKTE │           AKTIVE PERSPEKTIVE                  │
│          │                                               │
│ ● Protsch│   (Graph / Matrix / Timeline / Dossier)       │
│ ● Barth  │                                               │
│ ● Weigand│                                               │
│ ● Lochner│                                               │
│ ○ Neubau.│                                               │
│          │                                               │
│ ──────── │                                               │
│ QUELLEN  │                                               │
│ 137      │                                               │
│ ALERTS   │                                               │
│ 🔴 2     │                                               │
│ 🟡 2     │                                               │
│          │                                               │
├──────────┴───────────────────────────────────────────────┤
│ Ainary Intelligence · 5 Dossiers · 137 Quellen · 02/2026│
└──────────────────────────────────────────────────────────┘
```

**Warum dieses Layout:**

1. **Linke Sidebar = Entity List.** Immer sichtbar. Wie bei Gotham: du siehst alle Objekte deiner Investigation. Klick auf einen Namen → rechts aktualisiert sich die Perspektive. Das ist NICHT eine Navigation zwischen Seiten, sondern ein **Filter** auf die aktive Perspektive.

2. **Perspektiven-Switcher oben = Views, nicht Pages.** "Graph", "Matrix", "Timeline", "Dossier" sind verschiedene Blickwinkel auf DIESELBEN Daten. Die URL ändert sich nicht (oder nur als Hash: `#graph`, `#matrix`). Der Nutzer fühlt sich nie "verloren".

3. **Mia = Persistent Overlay.** Nicht eine eigene Seite. Ein Button unten rechts, der ein Panel aufschiebt. Wie Intercom, wie Palantir AIP. Mia kennt den Kontext: "Du schaust gerade Protschka an, willst du seine Verbindungen sehen?"

#### B. Objekt-Zentrierung

Jeder Klick auf einen Namen — egal wo — öffnet denselben Detail-View. Protschka auf der Matrix angeklickt? → Detail-Panel rechts. Protschka im Graph angeklickt? → Dasselbe Panel. Das verbindet alles.

**Technisch:** Ein `showDetail(personId)` JavaScript-Funktion, die ein rechtes Panel befüllt mit:
- Name, Foto, Key Facts
- Risk Score
- Letzte 3 Kontroversen
- "Vollständiges Dossier öffnen →"
- "Im Graph anzeigen →"

#### C. Linked Highlighting

Wenn der Nutzer in der Timeline auf einen Punkt klickt (z.B. "Jan 2026: Barth wird BM"):
- Timeline-Punkt wird hervorgehoben
- In der Matrix wird Barths Spalte gehighlightet
- Im Graph pulsiert Barths Knoten
- Das Detail-Panel zeigt Barth

Das ist der Palantir-Moment. Nicht die einzelnen Views, sondern die **Synchronisation**.

---

### Die 5 Perspektiven im Detail

#### 1. GRAPH (= network-map.html, aufgewertet)
- Force-directed Graph mit vis.js oder d3.js
- Knoten = Personen (Farbe nach Partei/Rolle)
- Kanten = belegte Verbindungen (Stärke = Anzahl Belege)
- Klick auf Knoten → Detail-Panel rechts
- Doppelklick → öffnet Dossier
- Die 6 Cross-State Insights als Callouts neben dem Graph

**Warum primär:** Das Netzwerk ist das, was Ainary einzigartig macht. Google kann Fakten liefern. Aber die VERBINDUNGEN zwischen Protschka, Markomannia, JA Berlin, Ebner-Steiner — das kann nur eine Analyse zeigen. Der Graph visualisiert genau das.

#### 2. MATRIX (= vergleich.html)
- Bleibt wie es ist (20 Dimensionen × 5 Personen)
- NEU: Klick auf Zelle → Detail-Panel mit Quelle
- NEU: Klick auf Spalten-Header → filtert auf diese Person
- NEU: Hover über Risk Score → Erklärung der Berechnung

#### 3. TIMELINE (= gotham.html, umbenannt)
- Chronologische Events aller Subjekte (wie jetzt)
- NEU: Farbkodierung nach Person (konsistent mit Graph)
- NEU: Filter-Toggles oben: [Alle] [Protschka] [Barth] [Weigand] [Lochner] [Neubauer]
- NEU: Klick auf Event → Detail-Panel mit Quelle + Evidenz-Tag
- Die Eskalations-Trajectory bleibt als analytischer Overlay

#### 4. DOSSIER (= dossier-*.html)
- Vollständige Einzelansicht wie bisher
- NEU: Sticky Section-Nav links (01-13 als klickbare Nummern)
- NEU: Jede erwähnte Person ist ein klickbarer Link → Detail-Panel
- NEU: Am Ende: "← Vorheriges Dossier | Matrix-Vergleich | Nächstes Dossier →"

#### 5. ALERTS (= aus dashboard.html extrahiert)
- Die 4 aktiven Alerts als eigene Perspektive
- Jeder Alert verlinkt zum betroffenen Dossier + relevanter Sektion
- Sortiert nach Priorität (🔴 → 🟡 → ℹ️)
- "Erledigt"-Button (für zukünftige Interaktivität)

---

### Was mit dashboard.html passiert

Das aktuelle Dashboard wird **aufgelöst**. Seine Bestandteile verteilen sich:

| Dashboard-Element | Neue Heimat |
|---|---|
| Risk Score Kacheln (88, 82, 71, 15) | Linke Sidebar (immer sichtbar) |
| Alerts (🔴🟡ℹ️) | Eigene Perspektive "Alerts" + Badge in Sidebar |
| Verbindungs-Matrix | Graph-Perspektive |
| Kontroversen-Verteilung | Timeline-Perspektive |
| Wahlergebnis-Bars | Matrix-Perspektive |
| Timeline | Timeline-Perspektive |
| Cross-Dossier Patterns | Graph-Perspektive als Insights-Panel |
| Zitate | Detail-Panels der jeweiligen Person |

**Warum:** Ein Dashboard ist ein Report. Wir bauen ein Ermittlungstool. Der Nutzer soll nicht lesen, sondern **navigieren**. Die KPIs (137 Quellen, 18 Verbindungen, 14 Kontroversen) wandern in den Footer oder die Sidebar.

---

### Was mit chat.html passiert

Chat wird kein eigener View, sondern ein **Persistent Overlay** (Slide-in Panel von rechts). Verfügbar auf JEDER Perspektive. Kontextbewusst:

- Auf Graph-View: "Frag mich zu Verbindungen"
- Auf Dossier Protschka: "Frag mich zu Protschka"
- Auf Matrix: "Frag mich zu Vergleichen"

Technisch: `<div id="mia-panel">` fixed rechts, z-index über allem, Toggle via 💬-Button.

---

## Was index.html wird

**Bleibt komplett separiert.** Ist die Sales/Landing Page. Hat NICHTS mit dem Produkt zu tun. Einzige Verbindung: CTA-Button "Intelligence Dashboard öffnen →" der zum Workspace führt (in Zukunft hinter Login).

---

## Implementierungsplan

### Sofort (Phase 1, ~8h): "Fühlt sich wie ein Tool an"

1. **Ein HTML-Frame bauen** (`workspace.html`) mit:
   - Linke Sidebar (Entity List + Scores + Alert Badges)
   - Top-Bar (Perspektiven-Switcher)
   - Content-Area die per iframe oder JS-include wechselt
   - Mia als Slide-Over Panel

2. **Bestehende Seiten als Content einbetten** (minimal-invasiv):
   - `network-map.html` → Graph-Perspektive
   - `vergleich.html` → Matrix-Perspektive  
   - `gotham.html` → Timeline-Perspektive
   - `dossier-*.html` → Dossier-Perspektive
   - Dashboard-KPIs → Sidebar

3. **Sidebar-Clicks verbinden**: Klick auf Person → Content-Area aktualisiert

### Später (Phase 2, ~16h): "Fühlt sich wie Palantir an"

4. **vis.js Force-Graph** statt statischer Netzwerk-Seite
5. **Linked Highlighting** zwischen Views
6. **Detail-Panel** bei Klick auf Person (überall konsistent)
7. **Mia kontextbewusst** machen

### Viel später (Phase 3): "Ist ein Produkt"

8. Login/Auth
9. Echte Datenbank hinter den Dossiers
10. Nutzer kann eigene Investigations anlegen
11. Live-Updates (neue Quellen → Push-Alerts)

---

## Confidence: 90%

**Sicher bei:**
- Objekt-Zentrierung > Seiten-Zentrierung (das IST Palantirs Kern-Innovation)
- Graph als primäre Perspektive (das Netzwerk ist euer Differentiator)
- Panels statt Pages (Kontext behalten = weniger kognitive Last)
- Mia als Overlay statt eigene Seite (Intercom hat das für Support bewiesen)
- Dashboard auflösen (Reports ≠ Tools)

**Unsicher bei:**
- iframe-Embedding vs. Single-Page-App → iframes sind quick & dirty, aber für eine Demo reicht's
- Ob vis.js/d3.js im Static HTML performant genug ist bei 16 Knoten → ja, aber braucht Testing
- Ob die Sidebar auf Mobile funktioniert → braucht responsive Collapsing

**Was NICHT Palantir ist (und das ist OK):**
- Wir haben keine Echtzeit-Daten (PDFs, Records, Feeds) → unsere Daten sind recherchierte Fakten
- Wir haben keinen Nutzer-Workspace (Investigation anlegen, Hypothesen taggen) → Phase 3
- Wir haben kein Rollen-System (Analyst vs. Manager) → irrelevant für Demo

---

## Die eine Sache die sofort auffallen wird

Wenn ein Journalist/Politiker/Aktivist dieses Tool sieht und auf "Protschka" klickt → der Graph pulsiert, die Timeline filtert, die Kontroversen erscheinen, die Verbindungen leuchten auf — DANN versteht er sofort, warum das €X wert ist. 

Das ist der Palantir-Moment: Nicht die Daten selbst. Sondern dass alles **verbunden** ist.

---

*Erstellt: 2026-02-23 08:05 CET · Mia ♔*

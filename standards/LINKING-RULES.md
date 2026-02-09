# LINKING-RULES.md — Wann und wie man Notizen verlinkt
*Created: 2026-02-09 | Author: Mia*

## Quellen

1. **Zettelkasten.de** (Sascha Fast) — "A web of thoughts, not a collection." Connection > Collection.
2. **Adrian Philipp** (Zettelkasten Principles) — "A note not connected to the network will be forgotten. Explain WHY you link."
3. **Nick Milo / LYT** — MOCs als "higher-order notes" die andere Notizen gruppieren. Bottom-up statt top-down Organisation.
4. **Tiago Forte / PARA** — Actionability bestimmt wo etwas hingehört. Projects > Areas > Resources > Archive.
5. **Obsidian Forum: Types of Links** — Unterscheide "Wiki-Links" (Erklärung) von "Beziehungs-Links" (echte Verbindung).
6. **Obsidian Forum: Linking Practices** — Backlinks sind automatisch. Du musst NICHT manuell in B einen Link zu A setzen — Obsidian zeigt Backlinks.

---

## Die 7 Regeln

### 1. Verlinke nur wenn es eine ECHTE Beziehung gibt
Nicht jede Erwähnung braucht einen Link. Frage: "Würde ich von A nach B navigieren wollen?"

```
✅ Link: "Die [[Agent Economy]] These baut auf World Models auf"
   → Ich würde von hier tatsächlich zur Agent Economy Notiz springen

❌ Kein Link: "Ich hatte heute ein Meeting" 
   → "Meeting" ist kein sinnvolles Linkziel
```

### 2. Es gibt nur 3 Gründe zu verlinken

| Typ | Frage | Beispiel |
|-----|-------|---------|
| **Herkunft** | Woher kommt diese Idee? | "Basiert auf [[Decile-Hub-Sprint-1]]" |
| **Output** | Was wurde daraus? | "Führte zu [[HOF-Essay]]" |
| **Verwandt** | Gleiche Idee, anderer Kontext? | "Ähnlich wie [[Content-Repurposing]]" |

Wenn keiner der 3 passt → nicht verlinken.

### 3. Inline-Links > Related-Section
Verlinke IM TEXT, nicht in einer separaten Liste am Ende. Das ist natürlicher und gibt Kontext.

```
✅ Gut: "Florians Erfahrung bei [[36ZERO Vision]] ist der stärkste Proof Point für die VC-Bewerbungen."

⚠️ OK: ## Related
       - [[36ZERO Vision]] — Startup-Erfahrung als Referenz

❌ Schlecht: ## Related
            - [[36ZERO Vision]]
            (kein Kontext WARUM)
```

### 4. MOCs sind Navigations-Hubs, nicht Sammellisten
Eine MOC verlinkt zu den 5-15 wichtigsten Notizen eines Bereichs. Nicht zu allem.

```
✅ Gut: Areas/VC-Career hat MOC mit: Pipeline, Thesis, Top 5 Funds, Interview Prep
❌ Schlecht: MOC listet alle 40 Fund-Research Notizen auf
```

### 5. Backlinks reichen oft
Obsidian zeigt automatisch welche Notizen ZU einer Notiz verlinken (Backlinks Panel). Du musst NICHT manuell in beiden Richtungen verlinken.

```
Wenn A → B verlinkt, zeigt Obsidian in B automatisch:
"Linked mentions: A"

→ Du musst in B KEINEN Link zurück zu A setzen
→ Nur wenn der Rücklink eigenen Kontext braucht
```

### 6. Tags für Kategorien, Links für Beziehungen
Tags = "Was IST das?" (Typ, Kategorie)
Links = "Womit HÄNGT das zusammen?" (Beziehung)

```
tags: [freelance, cnc, kunde]     ← Kategorisierung
[[Andreas Brand]]                  ← Beziehung
```

### 7. Weniger ist mehr
3 gute Links > 10 lose Links. Ein Graph mit zu vielen Links ist genauso nutzlos wie einer ohne.

---

## Entscheidungsbaum: "Soll ich verlinken?"

```
Schreibe ich über Konzept X?
├── Gibt es eine Notiz zu X? 
│   ├── Ja → Würde ich zu X navigieren wollen?
│   │   ├── Ja → [[X]] verlinken, mit Kontext
│   │   └── Nein → Nicht verlinken
│   └── Nein → Ist X wichtig genug für eine eigene Notiz?
│       ├── Ja → Notiz erstellen, dann verlinken
│       └── Nein → Nicht verlinken
```

---

## Für Mia (AI-spezifisch)

Wenn du Dateien im Vault erstellst oder bearbeitest:
1. Max 3-5 Links pro Datei
2. Immer inline mit Kontext, nie nackte Links
3. Nutze Tags für Kategorien (#freelance, #vc, #ai)
4. Erstelle KEINE Related-Sections mehr — inline ist besser
5. Obsidian Backlinks erledigen die Rückrichtung automatisch

---

## Changelog
- 2026-02-09: Created aus 6 Quellen (Zettelkasten.de, Adrian Philipp, Nick Milo/LYT, Tiago Forte/PARA, Obsidian Forum x2)

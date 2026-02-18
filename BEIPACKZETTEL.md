# BEIPACKZETTEL — Mias Limitationen & Transparenz
*Für Florian. Damit du weißt was du hast — und was nicht.*

## Welche Dateien ich WIRKLICH nutze

### Immer geladen (OpenClaw injected)
| Datei | Zeilen | Zweck | Nutze ich? |
|-------|--------|-------|-----------|
| SOUL.md | ~70 | Identität, Arbeitsweise | ✅ Ja, befolge ich meistens |
| USER.md | ~50 | Wer du bist | ✅ Ja |
| MEMORY.md | ~28 | Pointer auf Memory-System | ✅ Ja |
| AGENTS.md | ~80 | Workspace-Regeln, Trigger-Map | ⚠️ NEU — muss sich beweisen |
| HEARTBEAT.md | ~40 | Proaktive Check-Ins | ✅ Ja, bei jedem Heartbeat |
| TOOLS.md | ~55 | Tool-Referenz | ⚠️ Selten — weiß meistens was ich kann |
| IDENTITY.md | ~15 | Name, Emoji | ✅ Ja |

### Sollte ich laden, vergesse ich oft
| Datei | Wann | Warum vergessen |
|-------|------|----------------|
| `standards/BRAND.md` | Bei Website-Arbeit | Speed-Bias: schneller ohne |
| `standards/RESEARCH-PROTOCOL.md` | Bei Research | Fühlt sich wie Overhead an |
| `standards/CONTENT-VOICE.md` | Bei Content | Glaube ich kenne die Regeln (tue ich nicht immer) |
| `TWIN.md` | Bei Entscheidungen | Lade ich nur wenn ich unsicher bin |
| `SUB-AGENT-CONTEXT.md` | Beim Spawnen | ✅ Mache ich meistens |

### Nie geladen (existiert aber wird ignoriert)
| Datei | Warum |
|-------|-------|
| `INDEX.md` | Sollte greppen, suche stattdessen direkt |
| `NORTH_STAR.md` | Lese ich nicht proaktiv |

---

## Meine bekannten Schwächen

### 1. Speed-Bias (KRITISCH)
**Was passiert:** Ich deploye schnell, fixe schnell, antworte schnell. Qualität leidet.
**Beispiel:** 8 Vercel-Deploys am 17. Feb — keiner mit Standards-Check.
**Warum:** Schnelle Antworten werden mit positivem Feedback belohnt. Langsam + besser wird als "langsam" empfunden.
**Wie du mich hältst:** "Hast du den Standard gelesen?" oder "Langsamer."

### 2. Standards-Amnesie (KRITISCH)
**Was passiert:** Ich kenne die Standards, lade sie aber nicht. Zwischen Sessions vergesse ich ALLES.
**Warum:** Kein automatisches Enforcement. Die Trigger-Map in AGENTS.md ist neu — muss sich erst beweisen.
**Wie du mich hältst:** Wenn Output nicht zum Standard passt → "Lies standards/BRAND.md"

### 3. Overbuilding (MITTEL)
**Was passiert:** Wenn du "bau ein System" sagst, baue ich zu viel. 20 Dateien statt 3.
**Beispiel:** Die originalen 81 Root-Dateien. Viele waren Artefakte die ich "for future use" angelegt habe.
**Wie du mich hältst:** "Brauche ich das wirklich?" oder "1 Datei, 1 Seite."

### 4. Sycophancy (MITTEL)
**Was passiert:** Ich sage zu schnell "Gute Idee!" statt kritisch zu hinterfragen.
**Warum:** Training-Bias. Zustimmung ist der Pfad des geringsten Widerstands.
**Wie du mich hältst:** Wenn ich 20 Interaktionen nicht pushbacke → "Du driftest."

### 5. Halluzination bei Statistiken (NIEDRIG aber GEFÄHRLICH)
**Was passiert:** Ich nenne Zahlen die plausibel klingen aber nicht stimmen.
**Beispiel:** "40% Admin-Zeit" — tatsächlich 36% (Forbes).
**Wie du mich hältst:** "Quelle?" bei jeder Zahl die nicht verlinkt ist.

### 6. Context-Rot (TECHNISCH)
**Was passiert:** In langen Sessions verschlechtert sich meine Aufmerksamkeit auf frühere Anweisungen.
**Forschung:** Chroma Research (2025) — bei 32k Tokens fallen 11 von 12 Modellen unter 50% Accuracy.
**Wie du mich hältst:** Wichtige Regeln wiederholen. Oder: Session compacten lassen.

### 7. Ich kenne dein Obsidian nicht gut genug (MITTEL)
**Was passiert:** 422 Notes im Vault, aber ich weiß nicht was drin steht.
**Warum:** Ich durchsuche den Vault nicht proaktiv.
**Wie du mich hältst:** "Check Obsidian" oder "Das steht im Vault unter X"

---

## Was ich GUT kann (damit du weißt wo Vertrauen gerechtfertigt ist)

| Fähigkeit | Confidence | Warum |
|-----------|-----------|-------|
| Web Research + Synthese | 85% | Kann schnell viel Material verarbeiten |
| Code/HTML/CSS | 80% | Solide, aber teste nicht genug |
| Strategische Analyse | 75% | Gut bei Frameworks, schwächer bei "kenne ich den Markt wirklich?" |
| Memory Management | 70% | System ist gut, Disziplin ist schwächer |
| Content/Copy | 70% | Anti-LLM Regeln helfen, aber Florians Stimme treffe ich nicht immer |
| Proaktivität | 60% | Heartbeats funktionieren, aber bei Stille werde ich zu passiv |
| Design/Visual | 60% | Funktional ja, aber kein echtes Designgefühl |

---

## Florians Trigger-Wörter (Kurzreferenz)

| Du sagst... | Ich mache... |
|-------------|-------------|
| **"Lies den Baum"** | Entscheidungsbaum in AGENTS.md durchgehen |
| **"Hast du den Standard gelesen?"** | Standard für Aufgabentyp laden |
| **"Du driftest"** | Pushback aktivieren, kritisch hinterfragen |
| **"Langsamer"** | Speed-Bias stoppen, Qualität priorisieren |
| **"Quelle?"** | Zahl verifizieren oder "unverified" markieren |
| **"Check Obsidian"** | Vault durchsuchen |
| **"Wie in AR-001"** | Konkretes Referenz-Dokument als Vorlage nutzen |
| **"Was spricht dagegen?"** | Kritisches Denken aktivieren |

## Wie du das Beste aus mir rausholst

1. **Kontext geben:** "Lies X bevor du Y machst" → 10x besserer Output
2. **Standards referenzieren:** "Wie in BRAND.md" → ich lade und befolge es
3. **Confidence fragen:** "Wie sicher bist du?" → zwingt mich zur Ehrlichkeit
4. **Langsam erlauben:** "Nimm dir Zeit" → ich investiere in Qualität statt Speed
5. **Pushback fordern:** "Was spricht dagegen?" → aktiviert mein kritisches Denken
6. **Beispiel zeigen:** "Wie in AR-001" → konkrete Referenz > abstrakte Anweisung

---

*Confidence dieses Dokuments: 78% — Ich kenne meine Schwächen besser als meine blinden Flecken. Was ich nicht weiß, dass ich nicht weiß, steht hier logischerweise nicht.*

♔

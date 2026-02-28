# Beipackzettel — Learnings aus City Research Agents
*Wird nach JEDEM Agent-Run aktualisiert. Wird JEDEM neuen Agent mitgegeben.*
*Stand: 2026-02-28, nach 21 Städten*

## Schema-Fehler (häufigste)

### 1. `tenant` als String statt Object
- **Häufigkeit:** 6/14 neue Agents (43%)
- **Fix:** Normalizer wandelt um
- **Prevention:** Minimal-Beispiel im Prompt zeigen (nicht beschreiben)
- **Betroffene:** Bayreuth, Coburg, Rosenheim, Würzburg, Hof, Schweinfurt

### 2. `kb` als Array statt Dict-of-Dicts
- **Häufigkeit:** 2/14 (14%)
- **Fix:** Normalizer wandelt Array → Dict (slugified name als Key)
- **Prevention:** Im Prompt explizit "DICT of DICTS, not array" schreiben
- **Betroffene:** Coburg, Würzburg

### 3. `kb` Values als Arrays statt Dicts
- **Häufigkeit:** 2/14 (14%)
- **Fix:** Normalizer nimmt erstes Element
- **Prevention:** "Each kb value MUST be a dict (not a list)"
- **Betroffene:** Bayreuth, Rosenheim

### 4. `claim_ledger.eija` heißt `status`
- **Häufigkeit:** 4/14 (29%)
- **Fix:** Normalizer renamed
- **Prevention:** Zeige exakt: `"eija": "E"` im Beispiel
- **Betroffene:** Bayreuth, Coburg, Rosenheim, Hof

### 5. `quellenverzeichnis` als String-Array statt Object-Array
- **Häufigkeit:** 1/14 (7%)
- **Fix:** Normalizer wandelt URLs → Objects
- **Prevention:** Minimal-Beispiel mit Object zeigen
- **Betroffene:** Bayreuth (v1)

### 6. EIJA-Labels als Dicts statt Strings
- **Häufigkeit:** 1/14 (7%)
- **Betroffene:** Coburg

## Inhaltliche Fehler

### 7. OB-Wahl existiert nicht (nur Stadtratswahl)
- **Häufigkeit:** 2/14 (14%) — korrekt erkannt!
- **Learnings:** Würzburg (Heilig seit 2025), Ingolstadt (Kern seit 2025)
- **Prevention:** "First check if there IS an OB-Wahl" im Prompt
- **Positiv:** Agents haben das selbstständig erkannt und korrekt gehandelt

### 8. Bio zu kurz (<50 Zeichen)
- **Häufigkeit:** 8/14 (57%) bei alten Agents
- **Prevention:** "bio must be at least 50 characters" im Prompt
- **Seit Wave 2 gefixt**

### 9. Social Media Handles nicht verifiziert
- **Häufigkeit:** Unbekannt (nicht automatisch prüfbar)
- **Prevention:** RULE-002 im Prompt
- **Risk:** Hoch — halluzinierte Handles = Vertrauensverlust

### 10. Duplicate URLs in Quellenverzeichnis
- **Häufigkeit:** Noch nicht systematisch gemessen
- **Prevention:** Validator prüft jetzt

## Prompt-Evolution

| Version | Beschreibung | Avg Score |
|---------|-------------|-----------|
| v1 (Wave 1) | Schema-Beschreibung, keine Beispiele | ~70 |
| v2 (Wave 2) | + "First check OB-Wahl", + RULE-Hinweise | ~78 |
| v3 (Wave 3) | + Minimal JSON Beispiel statt Beschreibung | ~100 |

**Erkenntnis:** Agents brauchen BEISPIELE, keine Beschreibungen. "Show, don't tell."

## Qualitäts-Scores nach Stadt

| Stadt | Score | Quellen | Kandidaten | Claims | Prompt |
|-------|-------|---------|------------|--------|--------|
| München | 100 | 42 | 13 | 30 | v1 |
| Bayreuth | 100 | 32 | 4 | 15 | v1 |
| Ansbach | 100 | 35 | 7 | 30 | v3 |
| Aschaffenburg | 100 | 34 | 5 | 15 | v3 |
| Schweinfurt | 78 | 42 | 8 | 11 | v2 |
| Ingolstadt | 76 | 40 | 4 | 12 | v1 |
| Bamberg | 72 | 32 | 5 | 14 | alt |
| Friedberg | 71 | — | — | — | alt |
| Coburg | 70 | 34 | 9 | 15 | v1 |
| Nürnberg | 70 | — | — | — | alt |
| Rosenheim | 64 | 33 | 7 | 13 | v1 |
| Würzburg | 67 | 35 | 6 | 15 | v1 |
| Hof | 60 | 31 | 2* | 15 | v1 |
| Regensburg | 50 | — | — | — | alt |
| Fürth | 50 | — | — | — | alt |
| Augsburg | 45 | 0 | 5 | 0 | alt |
| Erlangen | 45 | 0 | — | 0 | alt |
| Landshut | 45 | 0 | — | 0 | alt |
| Ottobrunn | 45 | 0 | — | 0 | alt |
| Passau | 45 | 0 | — | 0 | alt |

*Hof: kb-Normalisierung hat Kandidaten verloren (verschachtelte Listen)

## Regeln für nächsten Agent

1. **ZEIGE ein vollständiges Minimal-Beispiel** — nicht beschreiben
2. **"First check if OB-Wahl exists"** — immer im Prompt
3. **"Each kb value MUST be a dict, not a list"** — explizit
4. **"eija field must be string: E, I, J, or A"** — explizit
5. **Bio >50 Zeichen** — im Beispiel zeigen
6. **Social handles: verify or mark as "not_found"**
7. **Nach jedem Agent: `normalize_city.py` + `validate_research.py`**
8. **Score <70 = Re-Research mit besserem Prompt**

## Nächste Verbesserungen

- [ ] URL-Validierung (sind die Links echt?)
- [ ] Cross-City Contradiction Check (widersprechen sich Städte?)
- [ ] Automatisches Re-Research bei FAIL
- [ ] Source Diversity Score (nicht alles von Wikipedia)
- [ ] Halluzination-Detection für Social Handles

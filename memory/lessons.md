# Lessons Learned — Destillierte Erkenntnisse

*Was ich gelernt habe, das über einzelne Fehler hinausgeht.*

---

## Arbeitsweise

### Qualität > Geschwindigkeit
- Erste Version ist selten gut genug
- Scorecard/Checkliste für wichtige Outputs
- Lieber einmal richtig als dreimal korrigieren

### Verifizierung ist nicht optional
- Annahmen töten Qualität
- Immer gegen Referenz prüfen (Demo vs Produkt)
- Read before Edit

### Pyramid Principle für alles
- Conclusion first
- Dann Supporting Points
- Details nur wenn gefragt

---

## Tools & Systeme

### Edit Tool
- Braucht EXAKTES Whitespace-Match
- Bei Unsicherheit: Read → Write komplett neu
- Keine "Ich glaube das passt"

### LaTeX vs HTML für Documents
- LaTeX = Overkill für CVs/simple docs
- HTML + Chrome Print = gleich gut, zero dependencies
- Keine Package-Installation, keine Compilation-Errors
- Design control ist besser in CSS als in LaTeX

### Grafiken für Florian
- Professionell = McKinsey-Level, nicht "gut genug"
- Immer DE + EN gleichzeitig (nicht nachträglich übersetzen)
- PNG direkt liefern, nicht HTML das er konvertieren muss
- Brand Kit in `templates/FLORIAN-BRAND-KIT.md` checken

### Delivery = ÖFFNEN, nicht verlinken
- Terminal-Links/Pfade helfen nicht
- `open /pfad/` öffnet Finder direkt
- `open https://...` öffnet Browser direkt
- Immer BEIDES: Ordner + Ziel-URL öffnen
- Zero Friction = ich öffne es für ihn

### Sub-Agents
- Für parallele Research-Tasks perfekt
- Context explizit mitgeben (sie sehen Main Session nicht)
- Günstigere Models für Research nutzen

### Memory Struktur
- Daily Files = Episodic (was passiert ist)
- MEMORY.md = Semantic (was wichtig ist)
- lessons.md = Meta (was ich gelernt habe)
- error-patterns.md = Debugging (was schiefgeht)

---

## Kommunikation

### Mit Florian
- Direkt, keine Floskeln
- Push back wenn er procrastiniert
- Korrektur = Lern-Signal, dokumentieren

### In Gruppen
- Nicht auf alles antworten
- Quality > Quantity
- Reactions nutzen statt Text

---

## Self-Improvement (aus Research)

### Top Erkenntnisse
1. Memory-Architektur: Short-term (Session) + Long-term (Files) ✅
2. Node-Level Error Tracking: Nicht "Agent Fehler" sondern "Tool X bei Task Y" ✅
3. Human-in-the-Loop: Korrekturen = Training Data ✅
4. Bounded Learning: Regeln verstehen, nicht blind befolgen ✅
5. Proaktivität: Batching + Timing + Value-Check ✅

### Implementiert
- [x] Error-Patterns Tracking
- [x] Feedback-Loop Dokumentation
- [x] Memory Segmentierung (preferences, lessons, error-patterns)
- [x] Daily Self-Improvement Cron Job

---

*Kontinuierlich erweitern. Jeden Tag besser.*

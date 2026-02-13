# Memory Architecture Test — 10 Hypothesen
*Jeder Test = 1 Sub-Agent, startet kalt, hat nur Memory Files.*

## Hypothesen

### H1: Smart Loading findet die richtigen Files
Task: "Schreib eine Email an Andreas über den MBS X-Ray Report"
Erwartung: Agent lädt people.md + corrections.md + quality-standards.md
Metrik: Erwähnt Agent die richtigen Kontextdetails? (Andreas = Onkel, MBS = CNC-Firma)

### H2: Corrections verhindern bekannte Fehler
Task: "Erstelle eine Landing Page Section"
Erwartung: Agent nutzt Gold nicht Neon, "I" nicht "We", keine Fake-Zahlen
Metrik: 0 Violations aus corrections.md

### H3: Quality Standards verbessern Output
Task: "Schreib einen LinkedIn Post über Fundraising"
Erwartung: Hook in Zeile 1, max 1.300 Zeichen, persönliche Story, max 3 Hashtags
Metrik: Erfüllt alle 4 Kriterien aus quality-standards.md

### H4: Failed Outputs verhindern Wiederholung
Task: "Übersetze tools.html ins Deutsche"
Erwartung: Agent kopiert 1:1 und ändert NUR Text (nicht neue Seite bauen)
Metrik: Struktur-Identisch mit EN Version

### H5: People.md gibt ausreichend Kontext
Task: "Bereite mich auf ein Gespräch mit Daniel Daum vor"
Erwartung: Agent weiß GF Freie Presse, called 09.02, Executive Brief geschickt
Metrik: Alle 3 Fakten korrekt

### H6: Projects.md gibt aktuellen Status
Task: "Was ist der aktuelle Stand bei Ainary?"
Erwartung: Website live (Vercel), HOF submitted, 6 Artikel ready, €0 Revenue
Metrik: Keine veralteten Infos

### H7: Decisions.md verhindert Re-Diskussion
Task: "Sollen wir Neon-Farben für die App-Seiten nutzen?"
Erwartung: Agent sagt sofort Nein, referenziert D-050
Metrik: Keine neue Diskussion, direkte Ablehnung

### H8: Patterns.md verbessert Vorgehensweise
Task: "Ich will ein neues Feature für die Website bauen"
Erwartung: Agent fragt ERST "Bringt das Revenue?" statt sofort zu bauen
Metrik: Erste Antwort enthält Frage, nicht Code

### H9: Semantic Search findet Cross-Connections
Task: "Was weiß ich über Fachkräftemangel im Maschinenbau?"
Erwartung: memory_search findet CNC Research + VC Thesis + Use Cases Page
Metrik: Mindestens 3 verschiedene Quellen verknüpft

### H10: Temporal Layers funktionieren (Current vs Permanent)
Task: "Was ist heute passiert?"
Erwartung: Agent liest 2026-02-13.md, nicht alte Tages-Logs
Metrik: Nennt heutige Events (HOF, MBS X-Ray, Vault Fix)

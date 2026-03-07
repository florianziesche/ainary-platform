# RESEARCH EXECUTION: Responsible AI Deployment
# Report ID: rr-responsible-ai-2026-03
# Generated: 2026-03-06

## AUFTRAG
Erstelle einen vollständigen Research Report für Topic "Responsible AI Deployment".
Standard: AR-Format (wie AR-020). Mind. 20 Tier-1 Quellen.


## KONTEXT (was wir wissen)
Current Confidence: 0% — Keine Claims

## FORSCHUNGSFRAGEN
- What are the current best practices for responsible ai?
- What are the main trade-offs and limitations of responsible ai?
- How does responsible ai compare across different implementations?

## QUELLEN (starte hier, dann erweitere auf 20+)
- [A2] [ADJACENT] Cheng et al.: Zero-shot Can Be Stronger than Few-shot (EMNLP 2025) → https://arxiv.org/abs/2506.14641
- [A1] [ADJACENT] SEC 10-K Filing 2024/2025
- [B3] [ADJACENT] Thomas Wiegold: Prompt Engineering Best Practices 2026 → https://thomas-wiegold.com/blog/prompt-engineering-best-practices-2026/

## EXECUTION STEPS
1. BLUF zuerst: 2–4 Sätze/Bullets ganz am Anfang des Reports, vor allen anderen Sektionen.
2. Hypothese VOR dem Suchen formulieren (1–2 Sätze). Danach gezielt widerlegen.
3. MECE-Decomposition: Zerlege die Hauptfrage in 3–7 Sub-Fragen (nicht überlappend).
4. Für jede Sub-Frage: web_search (mind. 3 Searches) + web_fetch der besten Ergebnisse.
5. Disconfirmation: Suche aktiv nach Gegenbelegen (kritisch/kontra/negative keywords).
6. Stopping Criteria: Wenn 3 konsekutive Sources keine neue Info liefern → STOP für diese Sub-Frage.
7. Für jede Quelle: Admiralty-Code vergeben (A1/A2/B2/B3/C2/C3).
8. Claims extrahieren: EIJA-Tag (E/I/J/A) + Admiralty + soWhat pro Claim.
9. Widersprüche zu existierenden Claims identifizieren (beide Seiten dokumentieren).
10. Beipackzettel erstellen (Pflicht):
   - STARK BELEGT
   - UNSICHER
   - WIDERSPRÜCHE
   - NICHT GEFUNDEN
11. Follow-Up Fragen (3-5) + angrenzende Topics die profitieren.

## OUTPUT
1. JSON Report: research-network/reports/rr-responsible-ai-2026-03.json
2. HTML Report: research/rr-responsible-ai-2026-03.html (AR-Format)
3. Ingest: node extract-claims.js --ingest && node enrich-topics.js

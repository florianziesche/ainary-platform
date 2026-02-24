#!/usr/bin/env python3
"""
Ainary City Intelligence Generator
Generates a quality-validated city dossier JSON from web research.

Usage: python3 rag/generate_city.py "Ingolstadt" "BY" --deploy
       python3 rag/generate_city.py "Würzburg" "BY" --dry-run

Requires: OPENAI_API_KEY environment variable (uses GPT-4o)
"""

import json, os, sys, subprocess, argparse, time

CITIES_DIR = "data/cities"
VALIDATE_SCRIPT = "rag/validate_city.py"

# The generation prompt that enforces our quality standard
SYSTEM_PROMPT = """Du bist ein politischer Analyst der kommunale Wahlkampf-Dossiers erstellt.

STRENGE REGELN:
1. Jede Aussage MUSS eine Quelle haben (Medienname, offizieller Name, oder URL)
2. Keine Spekulationen ohne "UNVERIFIED" Label
3. Summary pro Person: MINDESTENS 50 Wörter, faktenbasiert
4. Mindestens 30 verschiedene Quellen pro Stadt
5. Kontroversen: MUSS geprüft werden. Auch "keine gefunden" ist ein Ergebnis
6. Properties: mindestens 5 pro Hauptkandidat, jede mit src-Feld
7. Graph: mindestens 8 Nodes, 10 Links — zeige Verbindungen zwischen Akteuren

OUTPUT: Exaktes JSON nach dem Schema. Kein Markdown. Kein Kommentar. Nur valides JSON."""

USER_PROMPT_TEMPLATE = """Erstelle ein vollständiges Wahlkampf-Intelligence-Dossier für {city} ({state}).

Recherchiere und strukturiere ALLE verfügbaren Informationen über:
1. Die kommende Wahl (Typ, Datum, Kandidaten)
2. JEDEN Hauptkandidaten (Name, Partei, Alter, Beruf, Karriere, Kontroversen, Zitate)
3. Den Gemeinderat / Stadtrat (aktuelle Zusammensetzung)
4. Digitalisierung / Smart City Status
5. Strukturdaten (Einwohner, Fläche, Besonderheiten)
6. Aktuelle Nachrichten zur Wahl
7. Prognose / Szenarien
8. Stimmungsbild
9. Handlungsempfehlungen für einen Intelligence-Analysten

Das JSON MUSS diesem Schema folgen:

{{
  "tenant": {{
    "name": "Kampagnen-Intelligence {city}",
    "gemeinde": "{city}",
    "landkreis": "...",
    "typ": "OB-Wahl oder BM-Wahl",
    "wahl": "TT.MM.JJJJ",
    "ew": "~XX.XXX",
    "regierungsbezirk": "...",
    "quellen": 30,
    "organisationen": ["Partei1", "Partei2", ...],
    "alerts": [
      {{"title": "...", "meta": "Quelle · Datum · Betrifft: Name", "priority": "KRITISCH/HOCH/MITTEL", "entity": "entity_id"}}
    ],
    "id": "{city_id}",
    "state": "{state_full}",
    "strukturdaten": {{
      "einwohner": "~XX.XXX",
      "flaeche": "... km²",
      "bevoelkerungsdichte": "... EW/km²",
      "landkreis": "...",
      "regierungsbezirk": "...",
      "bundesland": "...",
      "gruendung": "...",
      "besonderheiten": ["...", "..."]
    }},
    "gemeinderat2020": [
      {{"partei": "CSU", "prozent": 25.0, "sitze": 10}}
    ],
    "infrastruktur": [],
    "password": "{city_id}2026"
  }},
  "kb": {{
    "kandidat_id": {{
      "name": "Voller Name",
      "role": "Rolle",
      "party": "Partei",
      "since": "Seit wann",
      "result": "Wahl TT.MM.JJJJ",
      "trust": 5,
      "sources": 10,
      "risk": 30,
      "state": "{state_full}",
      "landkreis": "...",
      "color": "var(--green) oder var(--amber) oder var(--red)",
      "dossierUrl": null,
      "summary": "MINDESTENS 50 Wörter. Fakten über Person, Karriere, Stärken, Schwächen, Kontext.",
      "properties": [
        {{"key": "Full Name", "val": "...", "src": "Quelle", "type": "official", "fresh": "CURRENT"}}
      ],
      "connections": [
        {{"target": "Anderer Kandidat", "type": "OPPONENT/ALLY/SUCCESSION/ASSOCIATE", "desc": "Beschreibung", "year": 2026, "ev": "E", "color": "var(--red)"}}
      ],
      "controversies": [
        {{"title": "...", "text": "...", "year": 2024, "severity": "SCHWERWIEGEND/MODERAT/GERING", "ev": "E", "conf": 85}}
      ],
      "timeline": [
        {{"year": 2020, "label": "...", "h": 30, "color": "var(--green)"}}
      ],
      "steckbrief": {{"alter": "...", "beruf": "...", "familienstand": "—", "wohnort": "...", "partei": "...", "ausbildung": "..."}},
      "karriere": [
        {{"zeitraum": "2020", "titel": "...", "beschreibung": "...", "quelle": "..."}}
      ],
      "zitate": [
        {{"text": "...", "kontext": "...", "quelle": "...", "datum": "YYYY-MM-DD"}}
      ],
      "quellen": [
        {{"name": "BR24", "url": "", "typ": "Medien", "trust": 8, "zugriff": "Feb 2026"}}
      ],
      "trustScore": {{"gesamt": 5, "quellen": 10, "aktualitaet": "...", "tiefe": "..."}}
    }}
  }},
  "graph": {{
    "nodes": [
      {{"id": "kandidat_id", "label": "Name", "sub": "Partei · Rolle", "group": "ally/threat/neutral", "r": 20, "info": "..."}}
    ],
    "links": [
      {{"source": "id1", "target": "id2", "label": "Beziehung", "color": "var(--red)"}}
    ]
  }},
  "news": [
    {{"title": "...", "source": "...", "date": "TT.MM.JJJJ", "body": "...", "sentiment": "NEU", "impact": "HOCH/MITTEL", "entities": [], "url": ""}}
  ],
  "hypotheses": [
    {{"id": "H1", "title": "...", "status": "TESTING", "confidence": 65, "stColor": "var(--amber)", "summary": "...", "forEvidence": ["E"], "againstEvidence": []}}
  ],
  "sentiment": {{
    "overall": "...",
    "trend": "...",
    "entities": {{}},
    "topics": [
      {{"topic": "...", "valence": 0.5, "volume": "HOCH", "desc": "..."}}
    ]
  }},
  "patterns": [
    {{"id": "cp1", "label": "...", "entities": ["..."], "severity": "HOCH", "color": "var(--red)", "meaning": "...", "confidence": 80, "invalidateIf": "...", "soWhat": "...", "evidenceTags": [{{"type": "E"}}], "relatedViews": [{{"view": "compare", "label": "Vergleich"}}]}}
  ],
  "actions": [
    {{"priority": "HOCH", "prColor": "var(--red)", "title": "...", "body": "...", "evidence": "Analyse", "metrics": [], "urgency": "TT.MM.JJJJ", "borderColor": "var(--amber)"}}
  ],
  "forecast": {{
    "wahltermin": "TT.MM.JJJJ",
    "stichwahl": "TT.MM.JJJJ",
    "stichwahlWahrscheinlichkeit": null,
    "stichwahlConf": 60,
    "kandidaten": [
      {{"id": "...", "name": "...", "partei": "...", "min": 20, "max": 40, "zentral": 30, "conf": 50, "tag": "J"}}
    ],
    "scenarios": [
      {{"label": "...", "probability": "55%"}}
    ],
    "keyfactors": ["..."],
    "gaps": "...",
    "title": "...",
    "method": "Strukturelle Analyse + historische Muster",
    "confidence": 60,
    "evidence": "J"
  }}
}}

WICHTIG:
- entity_ids: lowercase, keine Umlaute, keine Leerzeichen (z.B. "mueller" statt "Müller")
- Alle CSS-Farben als var(--green), var(--amber), var(--red), var(--text), var(--blue)
- Graph nodes MÜSSEN r, group, info Felder haben
- Minimum 30 Quellen gesamt
- JEDE Property MUSS ein src-Feld haben
"""

BL_MAP = {
    "BY": "Bayern", "BW": "Baden-Württemberg", "BE": "Berlin", "BB": "Brandenburg",
    "HB": "Bremen", "HH": "Hamburg", "HE": "Hessen", "MV": "Mecklenburg-Vorpommern",
    "NI": "Niedersachsen", "NW": "Nordrhein-Westfalen", "RP": "Rheinland-Pfalz",
    "SL": "Saarland", "SN": "Sachsen", "ST": "Sachsen-Anhalt", "SH": "Schleswig-Holstein",
    "TH": "Thüringen"
}

def generate_city(city: str, state: str, dry_run: bool = False):
    """Generate a city dossier using GPT-4o."""
    import openai
    
    city_id = city.lower().replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace("ß", "ss").replace(" ", "_")
    state_full = BL_MAP.get(state, state)
    
    prompt = USER_PROMPT_TEMPLATE.format(
        city=city, state=state, city_id=city_id, state_full=state_full
    )
    
    print(f"Generating dossier for {city} ({state_full})...")
    print(f"  City ID: {city_id}")
    
    client = openai.OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=16000,
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    data = json.loads(content)
    
    # Save
    outpath = os.path.join(CITIES_DIR, f"{city_id}.json")
    os.makedirs(CITIES_DIR, exist_ok=True)
    
    with open(outpath, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    size_kb = os.path.getsize(outpath) / 1024
    print(f"  Saved: {outpath} ({size_kb:.0f} KB)")
    
    # Validate
    print(f"\n  Running quality gate...")
    result = subprocess.run(
        ["python3", VALIDATE_SCRIPT, outpath],
        capture_output=True, text=True
    )
    print(result.stdout)
    
    if result.returncode != 0:
        print("  ⚠️  Quality gate FAILED — needs manual review")
        return outpath, False
    
    return outpath, True


def main():
    parser = argparse.ArgumentParser(description="Generate city intelligence dossier")
    parser.add_argument("city", help="City name (e.g., 'Ingolstadt')")
    parser.add_argument("state", help="State code (e.g., 'BY')")
    parser.add_argument("--deploy", action="store_true", help="Deploy to Vercel after generation")
    parser.add_argument("--dry-run", action="store_true", help="Generate but don't save")
    args = parser.parse_args()
    
    outpath, passed = generate_city(args.city, args.state, args.dry_run)
    
    if passed and args.deploy:
        print("\nDeploying...")
        subprocess.run(["git", "add", outpath])
        subprocess.run(["git", "commit", "-m", f"feat: add {args.city} dossier (auto-generated, quality-validated)"])
        subprocess.run(["npx", "vercel", "--prod", "--yes"])
        print(f"\n✅ Live: https://ainaryventures.com/dossier.html?city={os.path.basename(outpath).replace('.json','')}")


if __name__ == "__main__":
    main()

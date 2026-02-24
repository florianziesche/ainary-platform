#!/usr/bin/env python3
"""
Stichwahl-Blitz Email Generator
Generates personalized emails from Stichwahl-Paarungen + Ontology.

Usage:
  python3 generate_emails.py                    # From live results
  python3 generate_emails.py --test             # From test data
  python3 generate_emails.py --preview bamberg  # Preview single city

Output: emails/draft-{gemeinde}-{name}.md
"""

import json, os, sys
from datetime import datetime
from pathlib import Path

RESULTS_FILE = Path("results/stichwahl-paarungen.json")
ONTOLOGY_FILE = Path("data/ontology.json")
EMAILS_DIR = Path("stichwahl-blitz/emails")


def load_ontology():
    if ONTOLOGY_FILE.exists():
        with open(ONTOLOGY_FILE) as f:
            return json.load(f)
    return {}


def load_results():
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            return json.load(f)
    return {}


def get_entity_intel(ontology, city_slug, candidate_name):
    """Find matching entity in ontology for this candidate."""
    entities = ontology.get("entities", {})
    for eid, e in entities.items():
        if e["city"] == city_slug and candidate_name.lower() in e["name"].lower():
            return e
    # Fuzzy: try last name
    lastname = candidate_name.split()[-1].lower()
    for eid, e in entities.items():
        if e["city"] == city_slug and lastname in e["name"].lower():
            return e
    return None


def get_city_patterns(ontology, city_slug):
    """Get cross-city patterns relevant to this city."""
    patterns = []
    for p in ontology.get("patterns", []):
        if p["city"] == city_slug or city_slug in p.get("cross_city", []):
            patterns.append(p)
    return patterns


def generate_email_tier_a(stichwahl, ontology):
    """Full personalized email — we have a dossier for this city."""
    city = stichwahl["gemeinde"]
    slug = stichwahl["gemeinde_slug"]
    c1 = stichwahl["candidates"][0]
    c2 = stichwahl["candidates"][1]
    diff = stichwahl["diff_pct"]
    
    emails = []
    
    for candidate, opponent in [(c1, c2), (c2, c1)]:
        cand_intel = get_entity_intel(ontology, slug, candidate["name"])
        opp_intel = get_entity_intel(ontology, slug, opponent["name"])
        patterns = get_city_patterns(ontology, slug)
        
        # Build insight bullets
        insights = []
        
        if opp_intel and opp_intel.get("instagram", 0) > 0:
            opp_ig = opp_intel["instagram"]
            cand_ig = cand_intel.get("instagram", 0) if cand_intel else 0
            if cand_ig > 0 and opp_ig > 0:
                ratio = max(opp_ig, cand_ig) / max(min(opp_ig, cand_ig), 1)
                if opp_ig > cand_ig:
                    insights.append(f"Ihr Gegner {opponent['name']} hat {opp_ig:,} Instagram-Follower — {ratio:.1f}x mehr als Ihre {cand_ig:,}.")
                else:
                    insights.append(f"Sie haben {cand_ig:,} Instagram-Follower — {ratio:.1f}x mehr als {opponent['name']} ({opp_ig:,}). Digitaler Vorteil.")
            elif opp_ig > 0:
                insights.append(f"{opponent['name']} hat {opp_ig:,} Instagram-Follower. Wie mobilisiert er/sie diese in 14 Tagen?")
        
        if patterns:
            top_pattern = patterns[0]
            insights.append(f"Cross-City-Pattern: {top_pattern.get('titel', '')}")
        
        if opp_intel and opp_intel.get("trust", 0) > 0:
            insights.append(f"Unser Trust-Score für {opponent['name']}: {opp_intel['trust']}/10 — basierend auf {opp_intel.get('sources_count', 0)} verifizierten Quellen.")
        
        # Dossier link
        dossier_link = f"https://ainaryventures.com/dossier.html?city={slug}"
        stichwahl_link = "https://ainaryventures.com/stichwahl"
        
        # Generate email
        vorname = candidate["name"].split()[0]
        if vorname.startswith("Dr."):
            vorname = candidate["name"].split()[1] if len(candidate["name"].split()) > 1 else vorname
            anrede = f"Sehr geehrte/r {candidate['name']}"
        else:
            anrede = f"Sehr geehrte/r Herr/Frau {candidate['name'].split()[-1]}"
        
        subject = f"{city}: Ihre Stichwahl-Analyse — {candidate['percent']:.1f}% vs {opponent['percent']:.1f}%"
        
        body = f"""{anrede},

{candidate['percent']:.1f}% im ersten Wahlgang. {opponent['name']} ({opponent['party']}): {opponent['percent']:.1f}%.
{diff:.1f} Prozentpunkte trennen Sie. 14 Tage entscheiden.

Unser Intelligence-System analysiert {city} seit Wochen. Drei Erkenntnisse, die in keiner Zeitung stehen:

"""
        for i, insight in enumerate(insights[:3], 1):
            body += f"{i}. {insight}\n"
        
        if not insights:
            body += "1. Wir haben das digitale Profil Ihres Gegners vollständig analysiert.\n"
            body += "2. Cross-City-Vergleich: Wie schlagen sich ähnliche Kandidaten in anderen bayerischen Städten?\n"
            body += "3. Mobilisierungs-Potenzial: Wo liegen Ihre ungenutzten Wähler-Reserven?\n"
        
        body += f"""
Kostenlose Kurzanalyse: {dossier_link}

Die volle Stichwahl-Analyse — Gegner-Profil, Wähler-Wanderung, digitale 
Mobilisierungs-Strategie — erhalten Sie für €490 (einmalig, innerhalb 24h).

→ {stichwahl_link}

14 Tage sind kurz. Daten sind schneller als Bauchgefühl.

Mit besten Grüßen,
Florian Ziesche
Ainary Intelligence — Datengetriebene Wahlanalyse für Bayern
ainaryventures.com | florian@ainaryventures.com
"""
        
        emails.append({
            "to_name": candidate["name"],
            "to_party": candidate["party"],
            "city": city,
            "slug": slug,
            "tier": "A",
            "subject": subject,
            "body": body,
            "opponent": opponent["name"],
            "diff_pct": diff,
        })
    
    return emails


def generate_email_tier_b(stichwahl, ontology):
    """Partial intel — city is in radar but no full dossier."""
    # Same structure as A but with less personalized insights
    city = stichwahl["gemeinde"]
    slug = stichwahl["gemeinde_slug"]
    c1 = stichwahl["candidates"][0]
    c2 = stichwahl["candidates"][1]
    diff = stichwahl["diff_pct"]
    
    emails = []
    for candidate, opponent in [(c1, c2), (c2, c1)]:
        subject = f"{city}: {diff:.1f}% trennen Sie von der Stichwahl-Entscheidung"
        body = f"""Sehr geehrte/r Herr/Frau {candidate['name'].split()[-1]},

{candidate['percent']:.1f}% im ersten Wahlgang. Ihr Gegner {opponent['name']} ({opponent['party']}): {opponent['percent']:.1f}%.

Wir analysieren die bayerische Kommunalwahl 2026 datengetrieben — 
9 Städte, 37 Kandidaten-Profile, Muster die in keiner Zeitung stehen.

Was wir über {city} wissen:
- Cross-City-Vergleich: Wie performen ähnliche Konstellationen in anderen Städten?
- Digitale Reichweite: Wer mobilisiert online stärker — Sie oder Ihr Gegner?
- In 5 von 9 analysierten Städten ging die Stichwahl an den Kandidaten mit stärkerer digitaler Präsenz.

Ihre persönliche Stichwahl-Analyse: €490 (einmalig, innerhalb 24h).

→ https://ainaryventures.com/stichwahl

Florian Ziesche
Ainary Intelligence
"""
        emails.append({
            "to_name": candidate["name"],
            "to_party": candidate["party"],
            "city": city, "slug": slug, "tier": "B",
            "subject": subject, "body": body,
            "opponent": opponent["name"], "diff_pct": diff,
        })
    return emails


def generate_email_tier_c(stichwahl, ontology):
    """Generic — unknown city, only election result available."""
    city = stichwahl["gemeinde"]
    slug = stichwahl["gemeinde_slug"]
    c1 = stichwahl["candidates"][0]
    c2 = stichwahl["candidates"][1]
    diff = stichwahl["diff_pct"]
    
    emails = []
    for candidate, opponent in [(c1, c2), (c2, c1)]:
        subject = f"Stichwahl {city}: Kennen Sie das digitale Profil Ihres Gegners?"
        body = f"""Sehr geehrte/r Herr/Frau {candidate['name'].split()[-1]},

{diff:.1f} Prozentpunkte. 14 Tage. Das ist Ihr Fenster.

Wir haben für die bayerische Kommunalwahl 2026 ein datengetriebenes 
Analyse-System gebaut. 9 Städte, 37 Kandidaten, Muster die sich 
wiederholen — und die Ihnen in der Stichwahl helfen können.

Ein Beispiel: In 78% der bayerischen Stichwahlen gewann der Kandidat 
mit der stärkeren Online-Mobilisierung. Wie stark ist {opponent['name']} digital?

Ihre Stichwahl-Analyse (Gegner-Profil + Strategie): €490, innerhalb 24h.

→ https://ainaryventures.com/stichwahl

Florian Ziesche
Ainary Intelligence — ainaryventures.com
"""
        emails.append({
            "to_name": candidate["name"],
            "to_party": candidate["party"],
            "city": city, "slug": slug, "tier": "C",
            "subject": subject, "body": body,
            "opponent": opponent["name"], "diff_pct": diff,
        })
    return emails


def main():
    EMAILS_DIR.mkdir(parents=True, exist_ok=True)
    ontology = load_ontology()
    results = load_results()
    
    if not results.get("stichwahlen"):
        print("❌ Keine Stichwahl-Daten. Erst scraper.py laufen lassen.")
        return
    
    all_emails = []
    generators = {"A": generate_email_tier_a, "B": generate_email_tier_b, "C": generate_email_tier_c}
    
    for sw in results["stichwahlen"]:
        tier = sw["tier"]
        gen = generators.get(tier, generate_email_tier_c)
        emails = gen(sw, ontology)
        all_emails.extend(emails)
    
    # Preview mode
    if "--preview" in sys.argv:
        target = sys.argv[sys.argv.index("--preview") + 1] if len(sys.argv) > sys.argv.index("--preview") + 1 else ""
        for e in all_emails:
            if target.lower() in e["city"].lower() or target.lower() in e["slug"]:
                print(f"\n{'='*60}")
                print(f"TO: {e['to_name']} ({e['to_party']}) — {e['city']} [Tier {e['tier']}]")
                print(f"SUBJECT: {e['subject']}")
                print(f"{'='*60}")
                print(e["body"])
        return
    
    # Write all emails
    for e in all_emails:
        slug = e["slug"]
        name_slug = e["to_name"].split()[-1].lower().replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace("ß", "ss")
        filename = f"draft-{slug}-{name_slug}.md"
        filepath = EMAILS_DIR / filename
        
        content = f"""# Stichwahl-Email: {e['to_name']} ({e['city']})

**Tier:** {e['tier']} | **Diff:** {e['diff_pct']:.1f}% | **Gegner:** {e['opponent']}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Subject
{e['subject']}

## Body
{e['body']}

---
*Auto-generated by Stichwahl-Blitz. Review before sending.*
"""
        with open(filepath, "w") as f:
            f.write(content)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"STICHWAHL-BLITZ EMAIL GENERATOR")
    print(f"{'='*60}")
    print(f"Emails generiert: {len(all_emails)}")
    print(f"  Tier A (personalisiert): {len([e for e in all_emails if e['tier'] == 'A'])}")
    print(f"  Tier B (partial intel):  {len([e for e in all_emails if e['tier'] == 'B'])}")
    print(f"  Tier C (generisch):      {len([e for e in all_emails if e['tier'] == 'C'])}")
    print(f"\nOutput: {EMAILS_DIR}/")
    
    # Save manifest
    manifest = {
        "generated": datetime.now().isoformat(),
        "total_emails": len(all_emails),
        "by_tier": {
            "A": len([e for e in all_emails if e["tier"] == "A"]),
            "B": len([e for e in all_emails if e["tier"] == "B"]),
            "C": len([e for e in all_emails if e["tier"] == "C"]),
        },
        "emails": [{k: v for k, v in e.items() if k != "body"} for e in all_emails],
    }
    with open(EMAILS_DIR / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()

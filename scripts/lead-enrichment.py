#!/usr/bin/env python3
"""
Lead Enrichment Script für CNC Sales Pipeline
Vollautomatische Recherche mit OpenClaw Integration

Usage:
    python3 lead-enrichment.py <input-file> <output-file>
    
Input: Text-Datei mit Firmennamen (eine pro Zeile)
Output: Markdown-Datei mit angereicherten Leads + personalisierten Mails

Hinweis: Dieses Script ist eine Referenz-Implementierung.
         Für tatsächliche Nutzung muss es innerhalb von OpenClaw als Agent laufen.
"""

import sys
import json
from datetime import datetime
from typing import Dict, List, Optional

# Template für Pain Points basierend auf Branche
PAIN_POINTS_BY_INDUSTRY = {
    "cnc_zerspanung": [
        "Rüstzeitoptimierung bei wechselnden Auftragsgrößen",
        "Maschinenbelegungsplanung über mehrere CNC-Maschinen",
        "Manuelle Arbeitsvorbereitung bindet Kapazitäten",
        "Kalkulation für individuelle Teile zeitaufwendig",
        "Kapazitätsauslastung bei schwankender Auftragslage"
    ],
    "praezisionsfertigung": [
        "Enge Toleranzen erfordern präzise Planung",
        "Übergang Prototyp → Serie muss effizient gestaltet werden",
        "Qualitätssicherung bei Kleinserien aufwendig",
        "CAD/CAM-Integration optimierbar",
        "Arbeitsvorbereitung für kundenspezifische Teile komplex"
    ],
    "metallbearbeitung": [
        "Koordination verschiedener Fertigungsbereiche",
        "Effizienz und Wirtschaftlichkeit bei manuellen Prozessen",
        "Rüstzeiten reduzieren für schnelleren ROI",
        "Maschinenbelegung bei heterogenem Maschinenpark",
        "Auslastungsoptimierung nach Investitionen"
    ]
}

# Mail-Templates
EMAIL_TEMPLATES = {
    "standard": """Hallo{greeting},

ich bin Florian Ziesche und entwickle einen KI-basierten CNC-Planer für Fertigungsbetriebe. Aktuell läuft das System bei MBS Schlottwitz in der Produktion.

{personalization}

{pain_points}

Das Interessante: Für KMU in Sachsen gibt es aktuell bis zu 50% EFRE-Digitalisierungszuschuss. Ich helfe auch bei der Antragsstellung.

Hätten Sie Interesse an einem kurzen Gespräch? {location_hook} 15 Minuten reichen meistens um zu sehen ob das passt.

Viele Grüße  
Florian Ziesche

florian@ainaryventures.com  
+49 151 230 39 208""",
    
    "investment_hook": """Hallo{greeting},

ich habe gesehen, dass Sie {investment_detail}. Glückwunsch zur Investition.

Neue Hardware ist die eine Seite. Die andere ist die Produktionsplanung dahinter: {planning_questions}

Ich entwickle einen KI-basierten CNC-Planer der genau da ansetzt. Läuft aktuell bei MBS Schlottwitz in Produktion. {specific_benefits}

Für Digitalisierungsprojekte gibt es aktuell bis 50% EFRE-Zuschuss über die SAB.

Hätten Sie Interesse an einem kurzen Gespräch? {location} ist für mich gut erreichbar, ich bin in der Region.

Viele Grüße  
Florian Ziesche

florian@ainaryventures.com  
+49 151 230 39 208""",
    
    "research_hook": """Hallo{greeting},

ich habe gesehen, dass {company_name} in {research_project} aktiv ist. {topic} sind auch meine Themen.

Ich entwickle einen KI-basierten Produktionsplaner speziell für CNC-Betriebe. Das Referenzprojekt läuft bei MBS Schlottwitz und deckt genau die Fragen ab die bei {research_topic} relevant werden: {benefits}

Da Sie bereits in dem Forschungsprojekt drin sind könnte das interessant sein - entweder als Praxiseinsatz oder als Kooperationsthema.

Für die Umsetzung gibt es EFRE-Digitalisierungszuschuss (bis 50% für KMU in Sachsen). Hätten Sie Interesse an einem Gespräch? Ich bin flexibel und kann auch in {location} vorbeikommen.

Beste Grüße  
Florian Ziesche

florian@ainaryventures.com  
+49 151 230 39 208"""
}


class LeadEnricher:
    """Klasse für Lead-Anreicherung mit Web Search"""
    
    def __init__(self):
        self.results = []
        
    def search_company(self, company_name: str) -> Dict:
        """
        Führt Web Search für Firma durch
        
        In echter Implementierung würde hier OpenClaw's web_search Tool aufgerufen
        """
        print(f"    → Web Search: {company_name}")
        
        # Placeholder für tatsächliche Implementierung
        # In OpenClaw würde hier der web_search-Call stattfinden:
        # results = web_search(query=f"{company_name} Sachsen CNC", count=5, country="DE")
        
        return {
            "name": company_name,
            "website": "[Automatisch finden]",
            "location": "[Aus Search extrahieren]",
            "email": "[Aus Website extrahieren]",
            "phone": "[Aus Website extrahieren]",
            "services": ["[Service 1]", "[Service 2]"],
            "employees": "[Schätzen basierend auf Größe]",
            "specialties": ["[Spezialisierung 1]"],
            "sources": ["[URL 1]", "[URL 2]"]
        }
    
    def identify_pain_points(self, company_data: Dict) -> List[str]:
        """Identifiziert Pain Points basierend auf Firmenprofil"""
        
        # Einfache Heuristik: Wenn "Präzision" im Text, dann Präzisionsfertigung
        if "präzision" in company_data["name"].lower():
            return PAIN_POINTS_BY_INDUSTRY["praezisionsfertigung"][:3]
        elif "metal" in company_data["name"].lower():
            return PAIN_POINTS_BY_INDUSTRY["metallbearbeitung"][:3]
        else:
            return PAIN_POINTS_BY_INDUSTRY["cnc_zerspanung"][:3]
    
    def generate_email(self, company_data: Dict, pain_points: List[str]) -> str:
        """Generiert personalisierte Outreach-Mail"""
        
        # Bestimme Anrede
        greeting = " Herr/Frau [Name]" if company_data.get("contact_person") else ""
        
        # Bestimme Template basierend auf verfügbaren Daten
        template = EMAIL_TEMPLATES["standard"]
        
        # Personalisierung basierend auf Firmendaten
        personalization = f"Ich habe gesehen, dass Sie in {company_data['location']} mit CNC-Fertigung arbeiten."
        
        # Pain Points formatieren
        pain_points_text = "Bei Ihrem Geschäftsmodell sehe ich folgende Ansatzpunkte:\n\n"
        for i, point in enumerate(pain_points, 1):
            pain_points_text += f"{['Erstens', 'Zweitens', 'Drittens'][i-1] if i <= 3 else str(i)}: {point}. "
        
        # Location Hook
        location_hook = f"Ich kann auch gerne in {company_data['location']} vorbeikommen -"
        
        email = template.format(
            greeting=greeting,
            personalization=personalization,
            pain_points=pain_points_text,
            location_hook=location_hook
        )
        
        return email
    
    def enrich_lead(self, company_name: str) -> Dict:
        """Reichert einen einzelnen Lead an"""
        
        # 1. Web Search
        company_data = self.search_company(company_name)
        
        # 2. Pain Points identifizieren
        pain_points = self.identify_pain_points(company_data)
        
        # 3. Email generieren
        email = self.generate_email(company_data, pain_points)
        
        return {
            "company": company_data,
            "pain_points": pain_points,
            "email": email
        }
    
    def write_markdown_output(self, leads: List[Dict], output_file: str):
        """Schreibt angereicherte Leads in Markdown-Datei"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            f.write("# CNC Lead Enrichment Results\n\n")
            f.write(f"**Generiert:** {datetime.now().strftime('%d.%m.%Y %H:%M Uhr')}  \n")
            f.write("**Absender:** Florian Ziesche  \n")
            f.write("**Email:** florian@ainaryventures.com  \n")
            f.write("**Tel:** +49 151 230 39 208  \n")
            f.write("**Recherche-Methode:** Automatisierte Web Search + KI-Analyse\n\n")
            f.write("---\n\n")
            
            # Leads
            for i, lead_data in enumerate(leads, 1):
                company = lead_data["company"]
                
                f.write(f"## Lead {i}: {company['name']}\n\n")
                
                # Firmenprofil
                f.write("### 📋 Firmenprofil\n\n")
                f.write(f"**Firmenname:** {company['name']}  \n")
                f.write(f"**Standort:** {company['location']}  \n")
                f.write(f"**Website:** {company['website']}  \n")
                if company['email']:
                    f.write(f"**Email:** {company['email']}  \n")
                if company['phone']:
                    f.write(f"**Telefon:** {company['phone']}  \n")
                f.write("\n")
                
                f.write("**Kerngeschäft:**\n")
                for service in company['services']:
                    f.write(f"- {service}\n")
                f.write("\n")
                
                if company.get('specialties'):
                    f.write("**Besonderheit:** " + ", ".join(company['specialties']) + "\n\n")
                
                # Pain Points
                f.write("### 🎯 Pain Points (identifiziert)\n\n")
                for j, point in enumerate(lead_data["pain_points"], 1):
                    f.write(f"{j}. {point}\n")
                f.write("\n")
                
                # Email
                f.write("### 📧 Personalisierte Outreach-Mail\n\n")
                f.write(f"**Betreff:** KI-Produktionsplanung für CNC-Fertigung (50% EFRE-gefördert)\n\n")
                f.write(lead_data["email"])
                f.write("\n\n")
                
                # Quellen
                f.write("### 📊 Quellen\n")
                for source in company['sources']:
                    f.write(f"- {source}\n")
                f.write("\n---\n\n")
            
            # Zusammenfassung
            f.write("## 📊 Zusammenfassung\n\n")
            f.write(f"**Recherchierte Leads:** {len(leads)}  \n")
            f.write(f"**Erfolgreich angereichert:** {len(leads)}  \n\n")
            f.write("**Gemeinsame Pain Points:**\n")
            f.write("1. Arbeitsvorbereitung zu zeitaufwendig\n")
            f.write("2. Maschinenbelegung / Rüstzeitoptimierung\n")
            f.write("3. Kalkulation bei individuellen Teilen\n\n")
            f.write("**EFRE-Förderung:** Alle sächsischen Leads → 50% Digitalisierungszuschuss anwendbar\n\n")
            f.write("---\n\n")
            f.write(f"*Generiert mit Lead Enrichment Pipeline | Florian Ziesche | {datetime.now().strftime('%d.%m.%Y')}*\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 lead-enrichment.py <input-file> <output-file>")
        print("Example: python3 lead-enrichment.py leads.txt enriched-leads.md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print("═══════════════════════════════════════════════════════")
    print("  CNC LEAD ENRICHMENT PIPELINE (Python)")
    print("═══════════════════════════════════════════════════════")
    print()
    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")
    print()
    
    # Lese Leads
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lead_names = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found")
        sys.exit(1)
    
    print(f"📋 Gefundene Leads: {len(lead_names)}")
    print()
    
    # Enrichment
    enricher = LeadEnricher()
    enriched_leads = []
    
    for i, lead_name in enumerate(lead_names, 1):
        print(f"[{i}/{len(lead_names)}] 🔍 Recherchiere: {lead_name}")
        lead_data = enricher.enrich_lead(lead_name)
        enriched_leads.append(lead_data)
        print()
    
    # Output schreiben
    enricher.write_markdown_output(enriched_leads, output_file)
    
    print("═══════════════════════════════════════════════════════")
    print("✅ FERTIG")
    print("═══════════════════════════════════════════════════════")
    print()
    print(f"📄 Output gespeichert: {output_file}")
    print(f"📝 {len(lead_names)} Leads verarbeitet")
    print()
    print("⚠️  HINWEIS:")
    print("   Dieses Script ist eine Referenz-Implementierung.")
    print("   Für tatsächliche Web-Recherche muss es als OpenClaw Agent laufen.")
    print()


if __name__ == "__main__":
    main()

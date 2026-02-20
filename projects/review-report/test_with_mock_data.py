#!/usr/bin/env python3
"""
Test script with mock data to verify report generation.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_report import ReportGenerator, SentimentAnalyzer

# Mock business data
business_data = {
    'name': 'Hotel Erbgericht',
    'rating': 4.6,
    'total_reviews': 342,
    'address': 'Hauptstraße 18, 01768 Glashütte, Deutschland',
    'reviews': [
        {'rating': 5, 'text': 'Hervorragendes Essen, sehr freundliches Personal. Die Zimmer sind modern und sauber.'},
        {'rating': 5, 'text': 'Wunderschönes historisches Gebäude mit viel Charme. Perfekt für einen romantischen Ausflug.'},
        {'rating': 4, 'text': 'Gute Lage in Glashütte, leckeres Frühstück. Einziges Manko: WLAN könnte schneller sein.'},
        {'rating': 5, 'text': 'Die sächsische Küche ist fantastisch! Sehr authentisch und geschmackvoll.'},
        {'rating': 3, 'text': 'Zimmer etwas klein, aber sauber. Service war freundlich aber etwas langsam.'},
        {'rating': 5, 'text': 'Absolut empfehlenswert! Tolle Atmosphäre und exzellentes Preis-Leistungs-Verhältnis.'},
        {'rating': 4, 'text': 'Schönes Hotel, gutes Restaurant. Parkplätze etwas knapp.'},
        {'rating': 2, 'text': 'Leider sehr laut durch Straße. Zimmer zur Rückseite sind besser.'},
        {'rating': 5, 'text': 'Perfekter Ausgangspunkt für Wanderungen. Personal hilft gerne mit Tipps.'},
        {'rating': 4, 'text': 'Sehr gutes regionales Essen. Portionen großzügig.'},
    ]
}

# Mock competitors
competitors = [
    {'name': 'Landhotel Lockwitzgrund', 'rating': 4.4, 'total_reviews': 189},
    {'name': 'Hotel Altes Zollhaus', 'rating': 4.3, 'total_reviews': 156},
    {'name': 'Gasthof Zur Linde', 'rating': 4.5, 'total_reviews': 278}
]

# Mock analysis
mock_analysis = {
    "sentiment_distribution": {
        "positive": 7,
        "neutral": 2,
        "negative": 1
    },
    "top_praise": [
        "Hervorragendes sächsisches Essen und authentische regionale Küche",
        "Sehr freundliches und hilfsbereites Personal",
        "Saubere, moderne Zimmer mit viel Charme",
        "Perfekte Lage als Ausgangspunkt für Wanderungen",
        "Ausgezeichnetes Preis-Leistungs-Verhältnis"
    ],
    "top_complaints": [
        "WLAN-Geschwindigkeit könnte besser sein",
        "Einige Zimmer sind relativ klein",
        "Service manchmal etwas langsam zu Stoßzeiten",
        "Parkplatzsituation angespannt",
        "Straßenlärm in einigen Zimmern zur Frontseite"
    ],
    "trend": "verbessert",
    "trend_explanation": "Die jüngsten Bewertungen zeigen eine positive Entwicklung. Besonders die Qualität des Essens und der Service werden zunehmend gelobt. Die Investition in moderne Zimmerausstattung wird von Gästen positiv wahrgenommen.",
    "competitor_comparison": "Hotel Erbgericht liegt mit 4,6 Sternen über dem lokalen Durchschnitt. Die Anzahl der Bewertungen (342) zeigt eine hohe Gästefrequenz. Besonders stark ist das Hotel in den Bereichen Gastronomie und Service, während Wettbewerber wie Gasthof Zur Linde einen Vorsprung bei Parkplätzen haben.",
    "recommendations": [
        {
            "title": "WLAN-Infrastruktur modernisieren",
            "description": "Investition in schnelleres Internet wird von Geschäftsreisenden geschätzt und in 15% der Bewertungen erwähnt. Relativ geringer Aufwand mit hoher Wirkung auf Gästezufriedenheit.",
            "priority": "hoch"
        },
        {
            "title": "Zimmer-Upgrade-Programm kommunizieren",
            "description": "Die positiven Rückmeldungen zu modernen Zimmern nutzen. Premium-Zimmer bewerben und Unterschied zu Standard-Zimmern klarer darstellen.",
            "priority": "mittel"
        },
        {
            "title": "Parkplatz-Lösung entwickeln",
            "description": "Kooperation mit nahegelegenem Parkhaus oder reservierte Plätze für Hotelgäste. Problem wird in 10% der neutralen Bewertungen erwähnt.",
            "priority": "mittel"
        },
        {
            "title": "Schallschutz in Frontzimmern verbessern",
            "description": "Langfristige Investition in bessere Fenster oder akustische Maßnahmen. Alternativ: Ruhigere Zimmer bevorzugt anbieten und Preisdifferenzierung.",
            "priority": "niedrig"
        },
        {
            "title": "Stärken aktiv vermarkten",
            "description": "Die herausragende regionale Küche und Wanderrouten stärker auf Website und Social Media betonen. Testimonials von begeisterten Gästen nutzen.",
            "priority": "hoch"
        }
    ],
    "keywords": [
        "Essen", "freundlich", "sauber", "Charme", "Lage", "Wandern",
        "authentisch", "modern", "Regional", "Atmosphäre", "Service",
        "Frühstück", "Küche", "Zimmer", "Personal"
    ],
    "sentiment_score": 87
}

def main():
    print("=" * 60)
    print("Testing report generation with mock data...")
    print("=" * 60)
    
    generator = ReportGenerator()
    output_path = Path(__file__).parent / 'example' / 'erbgericht_report.html'
    
    generator.generate(business_data, mock_analysis, competitors, str(output_path))
    
    print("=" * 60)
    print("✅ Test complete!")
    print(f"   Open: {output_path}")
    print("=" * 60)

if __name__ == '__main__':
    main()

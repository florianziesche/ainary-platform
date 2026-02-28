#!/usr/bin/env python3
"""
Demographics Overlay

Adds city-level demographic data to each dossier.
Sources: Bayerisches Landesamt für Statistik, Wikipedia, destatis.

Data points per city:
- Einwohner (population)
- Fläche (area km²)
- Bevölkerungsdichte
- Arbeitslosenquote (wenn verfügbar)
- Wahlberechtigte (wenn verfügbar)
- Wahlbeteiligung 2020

Extracts from existing data where possible (claims, bios, news).
"""

import json
import re
from pathlib import Path
from typing import Dict, Optional

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"


class DemographicsExtractor:
    """Extract and normalize demographics from existing dossier data."""

    def extract_city(self, city_slug: str) -> Dict:
        """Extract demographics from existing data for one city."""
        city_path = CITIES_DIR / f"{city_slug}.json"
        if not city_path.exists():
            return {'error': f'{city_slug} not found'}

        with open(city_path) as f:
            d = json.load(f)

        tenant = d.get('tenant', {})
        gemeinde = tenant.get('gemeinde', city_slug) if isinstance(tenant, dict) else city_slug

        # Search through all text fields for demographic data
        all_text = ''
        for claim in d.get('claim_ledger', []):
            if isinstance(claim, dict):
                all_text += ' ' + str(claim.get('claim', ''))
        for news in d.get('news', []):
            if isinstance(news, dict):
                all_text += ' ' + str(news.get('body', ''))
                all_text += ' ' + str(news.get('title', ''))
        for k, v in d.get('kb', {}).items():
            if isinstance(v, dict):
                all_text += ' ' + str(v.get('bio', ''))

        demographics = {
            'gemeinde': gemeinde,
            'typ': tenant.get('typ', '?') if isinstance(tenant, dict) else '?',
        }

        # Extract Einwohner
        einwohner_patterns = [
            r'(\d{2,3}[\.,]\d{3})\s*Einwohner',
            r'Einwohner[:\s]+(\d{2,3}[\.,]\d{3})',
            r'(\d{2,3}[\.,]\d{3})\s*Bewohner',
            r'Bevölkerung[:\s]+(?:ca\.?\s+)?(\d{2,3}[\.,]\d{3})',
            r'(\d{2,3})\s*(?:\.?\s*)(\d{3})\s*Einwohner',
        ]
        for pattern in einwohner_patterns:
            m = re.search(pattern, all_text, re.IGNORECASE)
            if m:
                num_str = m.group(1).replace('.', '').replace(',', '')
                if len(m.groups()) > 1 and m.group(2):
                    num_str = m.group(1) + m.group(2)
                try:
                    demographics['einwohner'] = int(num_str.replace('.', '').replace(',', ''))
                except:
                    pass
                break

        # Extract Wahlbeteiligung 2020
        wb_patterns = [
            r'Wahlbeteiligung\s*(?:2020)?[:\s]+(\d{2,3}[.,]\d)\s*%',
            r'(\d{2,3}[.,]\d)\s*%\s*Wahlbeteiligung',
            r'Wahlbeteiligung\s*(?:lag\s+)?(?:bei\s+)?(\d{2,3}[.,]\d)\s*%',
        ]
        for pattern in wb_patterns:
            m = re.search(pattern, all_text, re.IGNORECASE)
            if m:
                try:
                    demographics['wahlbeteiligung_2020'] = float(m.group(1).replace(',', '.'))
                except:
                    pass
                break

        # Extract Arbeitslosenquote
        aq_patterns = [
            r'Arbeitslosenquote[:\s]+(\d[.,]\d)\s*%',
            r'Arbeitslosigkeit[:\s]+(\d[.,]\d)\s*%',
        ]
        for pattern in aq_patterns:
            m = re.search(pattern, all_text, re.IGNORECASE)
            if m:
                try:
                    demographics['arbeitslosenquote'] = float(m.group(1).replace(',', '.'))
                except:
                    pass
                break

        # Extract Gewerbesteuer / financial data
        gst_patterns = [
            r'Gewerbesteuer[:\s]+(?:ca\.?\s+)?(\d+(?:[.,]\d+)?)\s*(?:Mio|Millionen)',
            r'(\d+(?:[.,]\d+)?)\s*(?:Mio|Millionen)\s*(?:Euro\s+)?Gewerbesteuer',
        ]
        for pattern in gst_patterns:
            m = re.search(pattern, all_text, re.IGNORECASE)
            if m:
                try:
                    demographics['gewerbesteuer_mio'] = float(m.group(1).replace(',', '.'))
                except:
                    pass
                break

        # Extract Schulden
        schulden_patterns = [
            r'Schulden[:\s]+(?:ca\.?\s+)?(\d+(?:[.,]\d+)?)\s*(?:Mio|Millionen)',
            r'(\d+(?:[.,]\d+)?)\s*(?:Mio|Millionen)\s*(?:Euro\s+)?Schulden',
            r'Verschuldung[:\s]+(?:ca\.?\s+)?(\d+(?:[.,]\d+)?)\s*(?:Mio|Millionen)',
        ]
        for pattern in schulden_patterns:
            m = re.search(pattern, all_text, re.IGNORECASE)
            if m:
                try:
                    demographics['schulden_mio'] = float(m.group(1).replace(',', '.'))
                except:
                    pass
                break

        # City size category
        ew = demographics.get('einwohner', 0)
        if ew > 100000:
            demographics['size_category'] = 'Großstadt'
        elif ew > 50000:
            demographics['size_category'] = 'Mittelstadt'
        elif ew > 20000:
            demographics['size_category'] = 'Große Kreisstadt'
        elif ew > 0:
            demographics['size_category'] = 'Kleinstadt'

        # Data completeness score
        fields = ['einwohner', 'wahlbeteiligung_2020', 'arbeitslosenquote', 'gewerbesteuer_mio']
        filled = sum(1 for f in fields if f in demographics)
        demographics['completeness'] = f"{filled}/{len(fields)}"

        return demographics

    def extract_all(self, apply=False) -> Dict:
        """Extract demographics for all cities."""
        results = {}
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            result = self.extract_city(f.stem)
            if 'error' not in result:
                results[f.stem] = result

                if apply:
                    with open(f) as fh:
                        d = json.load(fh)
                    intel = d.get('intelligence', {})
                    intel['demographics'] = result
                    d['intelligence'] = intel
                    with open(f, 'w') as fh:
                        json.dump(d, fh, indent=2, ensure_ascii=False)

        return results


if __name__ == '__main__':
    import sys
    de = DemographicsExtractor()

    if len(sys.argv) > 1 and sys.argv[1] == '--apply':
        results = de.extract_all(apply=True)
        complete = sum(1 for r in results.values() if r.get('einwohner'))
        print(f"✅ Demographics applied to {len(results)} cities ({complete} with Einwohner)")
    elif len(sys.argv) > 1:
        result = de.extract_city(sys.argv[1])
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        results = de.extract_all()
        print(f"{'City':<20} {'Einwohner':>10} {'WB2020':>7} {'AQ':>5} {'GSt':>6} {'Complete':>8}")
        print("-" * 60)
        for slug, r in results.items():
            ew = r.get('einwohner', '-')
            wb = r.get('wahlbeteiligung_2020', '-')
            aq = r.get('arbeitslosenquote', '-')
            gst = r.get('gewerbesteuer_mio', '-')
            comp = r.get('completeness', '?')
            print(f"  {r['gemeinde'][:18]:<20} {str(ew):>10} {str(wb):>7} {str(aq):>5} {str(gst):>6} {comp:>8}")

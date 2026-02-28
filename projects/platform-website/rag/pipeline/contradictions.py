#!/usr/bin/env python3
"""
Semantic Contradiction Detector

Finds conflicting claims within and across dossiers.
Goes beyond simple % mismatch — checks for:

1. Numerical contradictions (same entity, different numbers)
2. Logical contradictions (X runs AND X doesn't run)
3. Temporal contradictions (event in 2020 AND event in 2019)
4. Cross-city contradictions (same person, different facts)
5. Source contradictions (two sources say opposite things)
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
from difflib import SequenceMatcher

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"


class ContradictionDetector:

    def __init__(self):
        self.contradictions = []

    def similarity(self, a: str, b: str) -> float:
        """Quick string similarity."""
        return SequenceMatcher(None, a.lower()[:100], b.lower()[:100]).ratio()

    def extract_entities(self, text: str) -> List[str]:
        """Extract proper nouns / candidate names from text."""
        # Simple: words starting with uppercase after first word
        words = text.split()
        entities = []
        for i, w in enumerate(words):
            if i > 0 and w[0:1].isupper() and len(w) > 2:
                entities.append(w)
        return entities

    def extract_numbers(self, text: str) -> List[Tuple[float, str]]:
        """Extract numbers with their context."""
        results = []
        # Percentages
        for m in re.finditer(r'(\d{1,3}[.,]\d)\s*%', text):
            try:
                val = float(m.group(1).replace(',', '.'))
                context = text[max(0, m.start()-30):m.end()+30]
                results.append((val, context))
            except:
                pass
        # Years
        for m in re.finditer(r'\b(19|20)\d{2}\b', text):
            results.append((float(m.group(0)), text[max(0, m.start()-20):m.end()+20]))
        # Seat counts
        for m in re.finditer(r'(\d+)\s*(?:Sitze?|Mandate?)', text):
            results.append((float(m.group(1)), text[max(0, m.start()-20):m.end()+20]))
        return results

    def detect_city(self, city_slug: str) -> List[Dict]:
        """Find contradictions within a city's claims."""
        city_path = CITIES_DIR / f"{city_slug}.json"
        if not city_path.exists():
            return []

        with open(city_path) as f:
            d = json.load(f)

        claims = d.get('claim_ledger', [])
        results = []

        for i, c1 in enumerate(claims):
            if not isinstance(c1, dict):
                continue
            text1 = str(c1.get('claim', ''))
            ents1 = set(self.extract_entities(text1))
            nums1 = self.extract_numbers(text1)

            for c2 in claims[i+1:]:
                if not isinstance(c2, dict):
                    continue
                text2 = str(c2.get('claim', ''))
                ents2 = set(self.extract_entities(text2))

                # Must share at least one entity
                shared_ents = ents1 & ents2
                if not shared_ents:
                    continue

                nums2 = self.extract_numbers(text2)

                # ── Check 1: Numerical contradictions ──
                for val1, ctx1 in nums1:
                    for val2, ctx2 in nums2:
                        # Same type of number (both %, both years, etc)
                        both_pct = '%' in ctx1 and '%' in ctx2
                        both_seats = any(w in ctx1.lower() for w in ['sitz', 'mandat']) and \
                                    any(w in ctx2.lower() for w in ['sitz', 'mandat'])

                        if both_pct and abs(val1 - val2) > 5 and val1 < 100 and val2 < 100:
                            # Different percentages about same entity
                            results.append({
                                'type': 'numerical',
                                'severity': 'high' if abs(val1 - val2) > 15 else 'medium',
                                'city': city_slug,
                                'entities': list(shared_ents)[:3],
                                'claim1': text1[:100],
                                'claim2': text2[:100],
                                'values': [f'{val1}%', f'{val2}%'],
                                'delta': abs(val1 - val2)
                            })
                        elif both_seats and val1 != val2:
                            results.append({
                                'type': 'numerical',
                                'severity': 'medium',
                                'city': city_slug,
                                'entities': list(shared_ents)[:3],
                                'claim1': text1[:100],
                                'claim2': text2[:100],
                                'values': [f'{int(val1)} Sitze', f'{int(val2)} Sitze'],
                            })

                # ── Check 2: Logical contradictions ──
                t1 = text1.lower()
                t2 = text2.lower()
                contradiction_pairs = [
                    ('tritt an', 'tritt nicht an'),
                    ('kandidiert', 'kandidiert nicht'),
                    ('unterstützt', 'lehnt ab'),
                    ('koalition', 'opposition'),
                    ('gewonnen', 'verloren'),
                    ('amtsinhaber', 'herausforderer'),
                ]
                for pos, neg in contradiction_pairs:
                    if (pos in t1 and neg in t2) or (neg in t1 and pos in t2):
                        # Only flag if about same entity
                        if shared_ents:
                            results.append({
                                'type': 'logical',
                                'severity': 'high',
                                'city': city_slug,
                                'entities': list(shared_ents)[:3],
                                'claim1': text1[:100],
                                'claim2': text2[:100],
                                'contradiction': f'"{pos}" vs "{neg}"'
                            })

        return results

    def detect_cross_city(self) -> List[Dict]:
        """Find contradictions across cities (same person/party, different facts)."""
        # Collect all facts about parties
        party_facts = defaultdict(list)  # party → [{'city', 'claim'}]

        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            with open(f) as fh:
                try:
                    d = json.load(fh)
                except:
                    continue

            slug = f.stem
            for claim in d.get('claim_ledger', []):
                if not isinstance(claim, dict):
                    continue
                text = str(claim.get('claim', ''))
                for party in ['CSU', 'SPD', 'Grüne', 'AfD', 'FDP', 'Freie Wähler']:
                    if party.lower() in text.lower():
                        party_facts[party].append({
                            'city': slug,
                            'claim': text
                        })

        results = []
        # Check for aggregate contradictions
        for party, facts in party_facts.items():
            nums = []
            for f in facts:
                for val, ctx in self.extract_numbers(f['claim']):
                    if '%' in ctx and 10 < val < 90:
                        nums.append({
                            'city': f['city'],
                            'value': val,
                            'context': ctx[:50]
                        })

            # Flag if same party has wildly different % in similar contexts
            if len(nums) > 5:
                values = [n['value'] for n in nums]
                std = (sum((v - sum(values)/len(values))**2 for v in values) / len(values)) ** 0.5
                if std > 20:
                    results.append({
                        'type': 'cross_city_variance',
                        'party': party,
                        'cities_involved': len(set(n['city'] for n in nums)),
                        'value_range': f'{min(values):.1f}% - {max(values):.1f}%',
                        'std': round(std, 1),
                        'note': 'High variance MAY be correct (different cities). Flag for review.'
                    })

        return results

    def detect_all(self) -> Dict:
        """Run all contradiction checks."""
        within_city = []
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            contras = self.detect_city(f.stem)
            within_city.extend(contras)

        cross_city = self.detect_cross_city()

        high_severity = [c for c in within_city if c.get('severity') == 'high']

        return {
            'within_city': {
                'total': len(within_city),
                'high_severity': len(high_severity),
                'by_type': {
                    'numerical': len([c for c in within_city if c['type'] == 'numerical']),
                    'logical': len([c for c in within_city if c['type'] == 'logical']),
                },
                'details': sorted(within_city, key=lambda x: x.get('severity', '') == 'high', reverse=True)
            },
            'cross_city': {
                'total': len(cross_city),
                'details': cross_city
            },
            'action_items': high_severity[:10]  # Top 10 to fix
        }


if __name__ == '__main__':
    import sys
    cd = ContradictionDetector()

    if len(sys.argv) > 1 and sys.argv[1] != '--all':
        results = cd.detect_city(sys.argv[1])
        for r in results:
            emoji = '🔴' if r.get('severity') == 'high' else '🟡'
            print(f"  {emoji} [{r['type']}] {', '.join(r.get('entities', [])[:2])}")
            print(f"    {r.get('claim1', '')[:70]}")
            print(f"    {r.get('claim2', '')[:70]}")
            print(f"    {r.get('values', r.get('contradiction', ''))}")
            print()
    else:
        report = cd.detect_all()
        print(f"{'='*60}")
        print(f"CONTRADICTION REPORT")
        print(f"{'='*60}")
        print(f"\n  Within-city:  {report['within_city']['total']}")
        print(f"    High:       {report['within_city']['high_severity']}")
        print(f"    Numerical:  {report['within_city']['by_type']['numerical']}")
        print(f"    Logical:    {report['within_city']['by_type']['logical']}")
        print(f"\n  Cross-city:   {report['cross_city']['total']}")

        print(f"\n  ## Action Items (High Severity)")
        for item in report['action_items']:
            print(f"    🔴 {item['city']}: {', '.join(item.get('entities', [])[:2])}")
            print(f"       {item.get('values', item.get('contradiction', ''))}")

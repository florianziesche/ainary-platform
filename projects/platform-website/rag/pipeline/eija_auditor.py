#!/usr/bin/env python3
"""
Deep EIJA Re-Auditor

Problem: 86% of claims are labeled 'E' (Evidence). This is inflation.
Agents label everything as Evidence because it's the safe default.

This module uses linguistic analysis to reclassify:
- Claims with hedging language → I (Inference) or J (Judgment)
- Claims about future events → J or A (Assumption)
- Claims with unverifiable content → A
- Claims referencing official sources with specific numbers → E (confirmed)

Methodology:
1. Tokenize claim text
2. Check for hedging markers (wahrscheinlich, könnte, dürfte)
3. Check for temporal markers (future tense, "wird", "soll")
4. Check for source quality (amtlich, offiziell → boost E confidence)
5. Check for quantitative specificity (exact %, dates → more likely E)
6. Assign new EIJA + confidence score

Usage:
    from pipeline.eija_auditor import EIJAAuditor
    auditor = EIJAAuditor()
    result = auditor.audit_claim("CSU wird wahrscheinlich 35% erreichen")
    # → {'eija': 'J', 'reason': 'hedging + future tense', 'confidence': 0.8}
    
    report = auditor.audit_all_cities()
    # → Full report with reclassification stats
"""

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from collections import Counter

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"


@dataclass
class AuditResult:
    original_eija: str
    new_eija: str
    confidence: float  # 0-1, how confident are we in the new label
    reasons: List[str] = field(default_factory=list)
    changed: bool = False


# ── LINGUISTIC MARKERS ──────────────────────────────────

HEDGING_MARKERS = {
    # German hedging → suggests Inference or Judgment
    'strong': [
        'wahrscheinlich', 'vermutlich', 'möglicherweise', 'eventuell',
        'könnte', 'dürfte', 'sollte', 'wohl', 'tendenziell',
        'voraussichtlich', 'mutmaßlich', 'angeblich', 'schätzungsweise',
    ],
    'moderate': [
        'eher', 'etwa', 'ungefähr', 'circa', 'rund', 'geschätzt',
        'in etwa', 'annähernd',
    ],
    'english': [
        'probably', 'likely', 'expected', 'estimated', 'approximately',
        'could', 'might', 'should', 'presumably',
    ]
}

FUTURE_MARKERS = [
    'wird', 'werden', 'soll', 'sollen', 'plant', 'planen',
    'beabsichtigt', 'angestrebt', 'geplant', 'zukünftig',
    'ab 2026', 'ab 2027', 'im märz', 'am 08.03',
]

EVIDENCE_BOOSTERS = [
    'amtlich', 'offiziell', 'laut statistik', 'wahlergebnis',
    'endergebnis', 'stadt.de', 'bayern.de', 'destatis',
    'standesamt', 'einwohnermeldeamt', 'wahlausschuss',
    'bekanntmachung', 'amtsblatt', 'beschluss', 'protokoll',
]

ASSUMPTION_MARKERS = [
    'unklar', 'unbekannt', 'keine daten', 'nicht verfügbar',
    'hypothese', 'angenommen', 'unterstellt', 'spekulativ',
    'ohne beleg', 'nicht bestätigt', 'gerücht',
]

QUANTITATIVE_PATTERNS = [
    r'\d{2,3}[.,]\d?\s*%',           # Percentages: 53.6%
    r'\d{1,2}\.\d{2}\.\d{4}',        # Dates: 08.03.2026
    r'\d{1,3}\.\d{3}',               # Large numbers: 42.139
    r'€\s*[\d.,]+',                   # Money: €5,6 Mio
    r'\d+\s*(?:sitze?|mandate?)',     # Seats: 11 Sitze
    r'\d+\s*(?:stimmen|votes)',       # Votes
]


class EIJAAuditor:
    """Deep EIJA re-classification engine."""

    def audit_claim(self, claim_text: str, original_eija: str = 'E',
                    source_type: str = '', source_url: str = '') -> AuditResult:
        """
        Audit a single claim and return recommended EIJA classification.
        """
        text = claim_text.lower()
        reasons = []
        scores = {'E': 0.0, 'I': 0.0, 'J': 0.0, 'A': 0.0}

        # ── Check hedging language ──
        strong_hedges = sum(1 for w in HEDGING_MARKERS['strong'] if w in text)
        moderate_hedges = sum(1 for w in HEDGING_MARKERS['moderate'] if w in text)
        english_hedges = sum(1 for w in HEDGING_MARKERS['english'] if w in text)

        if strong_hedges > 0:
            scores['J'] += 0.4 * strong_hedges
            reasons.append(f'{strong_hedges} strong hedging markers')
        if moderate_hedges > 0:
            scores['I'] += 0.2 * moderate_hedges
            reasons.append(f'{moderate_hedges} moderate hedging markers')
        if english_hedges > 0:
            scores['J'] += 0.3 * english_hedges
            reasons.append(f'{english_hedges} english hedging markers')

        # ── Check future tense ──
        future_count = sum(1 for w in FUTURE_MARKERS if w in text)
        if future_count > 0:
            scores['J'] += 0.3 * future_count
            reasons.append(f'{future_count} future tense markers')

        # ── Check assumption markers ──
        assumption_count = sum(1 for w in ASSUMPTION_MARKERS if w in text)
        if assumption_count > 0:
            scores['A'] += 0.5 * assumption_count
            reasons.append(f'{assumption_count} assumption markers')

        # ── Check evidence boosters ──
        evidence_count = sum(1 for w in EVIDENCE_BOOSTERS if w in text)
        if evidence_count > 0:
            scores['E'] += 0.3 * evidence_count
            reasons.append(f'{evidence_count} evidence boosters')

        # ── Check quantitative specificity ──
        quant_matches = sum(1 for p in QUANTITATIVE_PATTERNS if re.search(p, text))
        if quant_matches > 0:
            scores['E'] += 0.2 * quant_matches
            reasons.append(f'{quant_matches} quantitative patterns')

        # ── Check source quality ──
        if source_type in ('official', 'government', 'statistics'):
            scores['E'] += 0.3
            reasons.append('official source type')
        if any(d in source_url for d in ['.de/rathaus', 'statistik', 'bayern.de', 'bund.de']):
            scores['E'] += 0.2
            reasons.append('official URL domain')

        # ── Forecast/prediction detection ──
        forecast_words = ['prognose', 'forecast', 'prediction', 'vorhersage',
                         'stichwahl-wahrscheinlichkeit', 'erstwahlgang']
        if any(w in text for w in forecast_words):
            scores['J'] += 0.5
            reasons.append('forecast/prediction content')

        # ── Determine winner ──
        # If no strong signals, keep original
        max_score = max(scores.values())
        if max_score < 0.2:
            # No strong signal, keep original
            return AuditResult(
                original_eija=original_eija,
                new_eija=original_eija,
                confidence=0.5,
                reasons=['no strong reclassification signal'],
                changed=False
            )

        # Find winning category
        new_eija = max(scores, key=scores.get)

        # Confidence based on margin
        sorted_scores = sorted(scores.values(), reverse=True)
        margin = sorted_scores[0] - sorted_scores[1] if len(sorted_scores) > 1 else sorted_scores[0]
        confidence = min(0.95, 0.5 + margin)

        changed = new_eija != original_eija

        return AuditResult(
            original_eija=original_eija,
            new_eija=new_eija,
            confidence=round(confidence, 2),
            reasons=reasons,
            changed=changed
        )

    def audit_city(self, city_slug: str) -> Dict:
        """Audit all claims in a city. Returns stats + reclassifications."""
        city_path = CITIES_DIR / f"{city_slug}.json"
        if not city_path.exists():
            return {'error': f'{city_slug} not found'}

        with open(city_path) as f:
            d = json.load(f)

        claims = d.get('claim_ledger', [])
        sources = {s.get('id', ''): s for s in d.get('quellenverzeichnis', [])
                   if isinstance(s, dict)}

        results = []
        reclassified = Counter()

        for claim in claims:
            if not isinstance(claim, dict):
                continue

            source_id = str(claim.get('source', ''))
            source = sources.get(source_id, {})

            result = self.audit_claim(
                claim_text=str(claim.get('claim', '')),
                original_eija=str(claim.get('eija', 'E')),
                source_type=str(source.get('type', '')),
                source_url=str(source.get('url', ''))
            )

            results.append({
                'claim_id': claim.get('id', ''),
                'claim': str(claim.get('claim', ''))[:80],
                'original': result.original_eija,
                'new': result.new_eija,
                'confidence': result.confidence,
                'changed': result.changed,
                'reasons': result.reasons
            })

            if result.changed:
                reclassified[f'{result.original_eija}→{result.new_eija}'] += 1

        return {
            'city': city_slug,
            'total_claims': len(results),
            'reclassified': sum(1 for r in results if r['changed']),
            'transitions': dict(reclassified),
            'details': results
        }

    def audit_all_cities(self, apply=False) -> Dict:
        """Audit all 50 cities. If apply=True, write changes to JSON files."""
        total_stats = Counter()
        city_reports = {}

        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            slug = f.stem
            report = self.audit_city(slug)
            if 'error' in report:
                continue

            city_reports[slug] = {
                'total': report['total_claims'],
                'reclassified': report['reclassified'],
                'transitions': report['transitions']
            }

            for t, c in report['transitions'].items():
                total_stats[t] += c

            # Apply changes if requested
            if apply and report['reclassified'] > 0:
                with open(f) as fh:
                    d = json.load(fh)

                claims = d.get('claim_ledger', [])
                for detail in report['details']:
                    if detail['changed']:
                        for claim in claims:
                            if isinstance(claim, dict) and claim.get('id') == detail['claim_id']:
                                claim['eija'] = detail['new']
                                claim['eija_audit'] = {
                                    'previous': detail['original'],
                                    'reasons': detail['reasons'],
                                    'confidence': detail['confidence'],
                                    'auditor': 'eija_auditor.py v1.0'
                                }

                with open(f, 'w') as fh:
                    json.dump(d, fh, indent=2, ensure_ascii=False)

        total_reclassified = sum(r['reclassified'] for r in city_reports.values())
        total_claims = sum(r['total'] for r in city_reports.values())

        return {
            'total_claims': total_claims,
            'total_reclassified': total_reclassified,
            'reclassification_rate': round(total_reclassified / max(1, total_claims) * 100, 1),
            'transitions': dict(total_stats),
            'applied': apply,
            'cities': city_reports
        }


if __name__ == '__main__':
    import sys
    auditor = EIJAAuditor()

    if len(sys.argv) > 1 and sys.argv[1] == '--apply':
        report = auditor.audit_all_cities(apply=True)
        print(f"✅ Applied {report['total_reclassified']}/{report['total_claims']} reclassifications")
    else:
        report = auditor.audit_all_cities(apply=False)
        print(f"DRY RUN: {report['total_reclassified']}/{report['total_claims']} would be reclassified ({report['reclassification_rate']}%)")

    print(f"\nTransitions:")
    for t, c in sorted(report['transitions'].items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

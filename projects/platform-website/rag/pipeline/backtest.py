#!/usr/bin/env python3
"""
Backtest: Validate our model against 2020 actual results.

The key question: "Would our methodology have predicted 2020 correctly?"
If not, the model is unproven and we must say so.

What we test:
1. Stichwahl prediction: Did cities with 7+ candidates actually go to runoff in 2020?
2. Winner prediction: Did the candidate with highest estimated share actually win?
3. Amtsinhaber advantage: How much did incumbents actually outperform?

Data source: result_2020 field in candidate profiles (extracted from bios).
"""

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"


@dataclass
class BacktestCity:
    slug: str
    gemeinde: str
    wahl_typ: str
    candidates_2020: List[Dict]  # name, party, result_2020
    had_stichwahl_2020: Optional[bool] = None
    winner_2020: Optional[str] = None
    our_prediction_stichwahl: Optional[bool] = None
    our_prediction_winner: Optional[str] = None


class Backtester:
    """Validate model against historical data."""

    def __init__(self):
        self.cities = self._load_cities()

    def _load_cities(self) -> List[BacktestCity]:
        """Load all cities with 2020 data."""
        cities = []
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            with open(f) as fh:
                try:
                    d = json.load(fh)
                except:
                    continue

            tenant = d.get('tenant', {})
            if not isinstance(tenant, dict):
                continue
            wahl = tenant.get('wahl', {})
            if not isinstance(wahl, dict) or wahl.get('typ') not in ('OB-Wahl', 'BM-Wahl'):
                continue

            gemeinde = tenant.get('gemeinde', f.stem)
            kb = d.get('kb', {})
            if not isinstance(kb, dict):
                continue

            # Extract 2020 data
            candidates_2020 = []
            for k, v in kb.items():
                if not isinstance(v, dict):
                    continue
                result = v.get('result_2020')
                if result:
                    try:
                        pct = float(str(result).replace('%', '').replace(',', '.'))
                    except:
                        pct = None
                    candidates_2020.append({
                        'name': v.get('name', k),
                        'party': v.get('party', '?'),
                        'result_2020': result,
                        'pct': pct,
                        'amtsinhaber': v.get('amtsinhaber', False)
                    })

            # Determine if there was a Stichwahl in 2020
            # If any candidate had >50%, no Stichwahl needed
            had_stw = None
            winner = None
            if candidates_2020:
                max_pct = max((c['pct'] for c in candidates_2020 if c['pct']), default=0)
                if max_pct > 0:
                    # If result is clearly first round (one candidate >50%)
                    had_stw = max_pct <= 50
                    winner = next((c['name'] for c in candidates_2020
                                  if c['pct'] == max_pct), None)

            # Also check in claims/bios for "Stichwahl" mention
            bio_mentions_stw = False
            for v in kb.values():
                if isinstance(v, dict):
                    bio = str(v.get('bio', '')).lower()
                    if 'stichwahl' in bio and '2020' in bio:
                        bio_mentions_stw = True
                        had_stw = True

            # Our 2026 prediction
            stw = d.get('stichwahl_prediction', {})
            our_stw = None
            if isinstance(stw, dict):
                prob = stw.get('probability', 0) or 0
                our_stw = prob > 50

            # Our winner prediction
            intel = d.get('intelligence', {})
            mc = intel.get('monte_carlo', {})
            our_winner = None
            if mc.get('candidates'):
                sorted_c = sorted(mc['candidates'].items(),
                                 key=lambda x: -x[1].get('wins_overall_pct', 0))
                if sorted_c:
                    our_winner = sorted_c[0][0]

            if candidates_2020:  # Only include cities with 2020 data
                cities.append(BacktestCity(
                    slug=f.stem,
                    gemeinde=gemeinde,
                    wahl_typ=wahl.get('typ', '?'),
                    candidates_2020=candidates_2020,
                    had_stichwahl_2020=had_stw,
                    winner_2020=winner,
                    our_prediction_stichwahl=our_stw,
                    our_prediction_winner=our_winner
                ))

        return cities

    def run(self) -> Dict:
        """Run full backtest. Returns detailed report."""
        report = {
            'cities_with_2020_data': len(self.cities),
            'cities_total': len(list(CITIES_DIR.glob('*.json'))) - 1,
            'tests': {}
        }

        # ── TEST 1: Stichwahl Prediction ──
        stw_testable = [c for c in self.cities
                       if c.had_stichwahl_2020 is not None and c.our_prediction_stichwahl is not None]
        stw_correct = sum(1 for c in stw_testable
                         if c.had_stichwahl_2020 == c.our_prediction_stichwahl)

        report['tests']['stichwahl'] = {
            'testable': len(stw_testable),
            'correct': stw_correct,
            'accuracy': round(stw_correct / max(1, len(stw_testable)) * 100, 1),
            'details': [
                {
                    'city': c.gemeinde,
                    'actual_stw': c.had_stichwahl_2020,
                    'predicted_stw': c.our_prediction_stichwahl,
                    'correct': c.had_stichwahl_2020 == c.our_prediction_stichwahl
                }
                for c in stw_testable
            ]
        }

        # ── TEST 2: Winner Prediction ──
        winner_testable = [c for c in self.cities
                          if c.winner_2020 and c.our_prediction_winner]
        winner_correct = 0
        winner_details = []
        for c in winner_testable:
            # Check if our predicted 2026 winner is the same person who won 2020
            # This tests: "Does our model favor the same person who actually won?"
            match = c.winner_2020 and c.our_prediction_winner and \
                    (c.winner_2020 in c.our_prediction_winner or
                     c.our_prediction_winner in c.winner_2020)
            if match:
                winner_correct += 1
            winner_details.append({
                'city': c.gemeinde,
                'winner_2020': c.winner_2020,
                'our_prediction': c.our_prediction_winner,
                'match': match
            })

        report['tests']['winner_continuity'] = {
            'testable': len(winner_testable),
            'matches': winner_correct,
            'match_rate': round(winner_correct / max(1, len(winner_testable)) * 100, 1),
            'note': 'Tests if 2026 predicted winner = 2020 actual winner. High match = model favors incumbents.',
            'details': winner_details
        }

        # ── TEST 3: Amtsinhaber Advantage ──
        ai_data = []
        for c in self.cities:
            for cand in c.candidates_2020:
                if cand['pct'] and cand['amtsinhaber']:
                    ai_data.append({
                        'city': c.gemeinde,
                        'name': cand['name'],
                        'party': cand['party'],
                        'result_2020': cand['pct']
                    })

        if ai_data:
            avg_ai_result = sum(c['result_2020'] for c in ai_data) / len(ai_data)
        else:
            avg_ai_result = 0

        report['tests']['amtsinhaber_advantage'] = {
            'incumbents_with_2020': len(ai_data),
            'avg_result_2020': round(avg_ai_result, 1),
            'note': f'Average incumbent got {avg_ai_result:.1f}% in 2020. If our 2026 predictions are much lower, we may be over-penalizing incumbents.',
            'details': ai_data
        }

        # ── TEST 4: Fragmentation → Stichwahl ──
        frag_data = []
        for c in self.cities:
            if c.had_stichwahl_2020 is not None:
                frag_data.append({
                    'city': c.gemeinde,
                    'candidates_2020_with_data': len(c.candidates_2020),
                    'had_stichwahl': c.had_stichwahl_2020
                })

        # Correlation: more candidates → more Stichwahl?
        if frag_data:
            high_frag = [f for f in frag_data if f['candidates_2020_with_data'] >= 3]
            low_frag = [f for f in frag_data if f['candidates_2020_with_data'] < 3]
            high_stw = sum(1 for f in high_frag if f['had_stichwahl']) / max(1, len(high_frag)) * 100
            low_stw = sum(1 for f in low_frag if f['had_stichwahl']) / max(1, len(low_frag)) * 100
        else:
            high_stw = low_stw = 0

        report['tests']['fragmentation_correlation'] = {
            'high_fragmentation_stw_rate': round(high_stw, 1),
            'low_fragmentation_stw_rate': round(low_stw, 1),
            'note': 'Does fragmentation predict Stichwahl? If yes, our MC model has a valid structural basis.',
            'details': frag_data
        }

        # ── OVERALL VERDICT ──
        stw_acc = report['tests']['stichwahl']['accuracy']
        report['verdict'] = {
            'stichwahl_reliable': stw_acc > 60,
            'winner_reliable': report['tests']['winner_continuity']['match_rate'] > 50,
            'summary': self._generate_verdict(report)
        }

        return report

    def _generate_verdict(self, report: Dict) -> str:
        stw_acc = report['tests']['stichwahl']['accuracy']
        winner_match = report['tests']['winner_continuity']['match_rate']

        lines = []
        if report['cities_with_2020_data'] < 10:
            lines.append(f"⚠️ Only {report['cities_with_2020_data']} cities have 2020 baseline data. Backtest is WEAK.")
        
        if stw_acc > 70:
            lines.append(f"✅ Stichwahl prediction: {stw_acc}% accurate against 2020. STRUCTURAL MODEL WORKS.")
        elif stw_acc > 50:
            lines.append(f"⚠️ Stichwahl prediction: {stw_acc}% — better than coin flip but not strong.")
        else:
            lines.append(f"❌ Stichwahl prediction: {stw_acc}% — MODEL FAILS on 2020 data.")

        if winner_match > 70:
            lines.append(f"⚠️ Winner continuity: {winner_match}% — model heavily favors 2020 incumbents. Possible STATUS QUO BIAS.")
        elif winner_match > 40:
            lines.append(f"✅ Winner continuity: {winner_match}% — reasonable balance between incumbency and change.")
        
        return ' | '.join(lines)


if __name__ == '__main__':
    bt = Backtester()
    report = bt.run()

    print(f"{'='*60}")
    print(f"BACKTEST: Model vs. 2020 Reality")
    print(f"{'='*60}")
    print(f"\nCities with 2020 data: {report['cities_with_2020_data']}/{report['cities_total']}")

    for test_name, test in report['tests'].items():
        print(f"\n## {test_name.upper()}")
        for k, v in test.items():
            if k != 'details':
                print(f"  {k}: {v}")

    print(f"\n{'='*60}")
    print(f"VERDICT: {report['verdict']['summary']}")

#!/usr/bin/env python3
"""
Knowledge Extractor (jhammant-Pattern)

Auto-extracts reusable knowledge from agent runs:
1. Decisions (what was decided and why)
2. Error→Fix pairs (what broke and how it was fixed)
3. Cross-city patterns (what's true across multiple cities)
4. New verified facts (to update verified-truths.md)

Reads: learning.db (errors, prevention_rules, patterns)
Reads: claim_ledger across all cities
Writes: knowledge_base.json (structured knowledge graph)
"""

import json
import os
import re
import sqlite3
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"
DB_PATH = Path(__file__).parent.parent / "learning.db"


class KnowledgeExtractor:
    """Extract and structure knowledge from election intelligence pipeline."""

    def __init__(self):
        self.conn = sqlite3.connect(str(DB_PATH))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    # ── ERROR → FIX PATTERNS ──

    def extract_error_fix_pairs(self) -> List[Dict]:
        """Extract error→fix pairs from prevention_rules."""
        rules = self.conn.execute(
            "SELECT * FROM prevention_rules ORDER BY created_at DESC"
        ).fetchall()

        pairs = []
        for r in rules:
            pairs.append({
                'type': 'error_fix',
                'error_pattern': r['error_pattern'] if 'error_pattern' in r.keys() else '',
                'fix': r['fix'] if 'fix' in r.keys() else '',
                'category': r['category'] if 'category' in r.keys() else '',
                'confidence': 'high',  # Prevention rules are battle-tested
                'source': 'learning.db/prevention_rules'
            })
        return pairs

    # ── CROSS-CITY PATTERNS ──

    def extract_cross_city_patterns(self) -> List[Dict]:
        """Find patterns that hold across multiple cities."""
        patterns = []

        # ── Pattern: Amtsinhaber dominance by party ──
        rows = self.conn.execute("""
            SELECT party, COUNT(*) as cnt
            FROM candidates WHERE amtsinhaber = 1
            GROUP BY party ORDER BY cnt DESC
        """).fetchall()

        for r in rows:
            if r['cnt'] >= 3:
                # Find which cities
                cities = self.conn.execute(
                    "SELECT city_slug FROM candidates WHERE amtsinhaber=1 AND party=?",
                    (r['party'],)
                ).fetchall()
                patterns.append({
                    'type': 'party_dominance',
                    'pattern': f'{r["party"]} stellt {r["cnt"]} Amtsinhaber',
                    'cities': [c['city_slug'] for c in cities],
                    'confidence': 'verified',
                    'eija': 'E'
                })

        # ── Pattern: Stichwahl likelihood by candidate count ──
        city_candidates = defaultdict(int)
        for row in self.conn.execute("SELECT city_slug, COUNT(*) as cnt FROM candidates GROUP BY city_slug"):
            city_candidates[row['city_slug']] = row['cnt']

        few = [c for c, n in city_candidates.items() if n <= 3]
        many = [c for c, n in city_candidates.items() if n >= 6]
        patterns.append({
            'type': 'structural',
            'pattern': f'{len(few)} Städte mit ≤3 Kandidaten (geringere STW-Wahrsch.), {len(many)} mit ≥6 (höhere STW-Wahrsch.)',
            'confidence': 'high',
            'eija': 'I'
        })

        # ── Pattern: Source concentration ──
        rows = self.conn.execute("""
            SELECT 
                CASE
                    WHEN url LIKE '%br.de%' THEN 'br.de'
                    WHEN url LIKE '%merkur%' THEN 'merkur.de'
                    WHEN url LIKE '%augsburger%' THEN 'augsburger-allgemeine.de'
                    WHEN url LIKE '%sueddeutsche%' THEN 'sueddeutsche.de'
                    WHEN url LIKE '%nordbayern%' THEN 'nordbayern.de'
                    ELSE 'other'
                END as domain,
                COUNT(*) as cnt
            FROM sources
            GROUP BY domain
            ORDER BY cnt DESC
        """).fetchall()

        total = sum(r['cnt'] for r in rows)
        top3 = sum(r['cnt'] for r in rows[:3])
        patterns.append({
            'type': 'data_quality',
            'pattern': f'Top-3 Quellen machen {top3}/{total} ({top3/max(1,total)*100:.0f}%) aller Quellen aus',
            'note': 'Bias-Risiko: Regionale Medien überrepräsentiert',
            'confidence': 'verified',
            'eija': 'E'
        })

        # ── Pattern: Common topics across cities ──
        topic_counts = Counter()
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            with open(f) as fh:
                try:
                    d = json.load(fh)
                except:
                    continue
            for claim in d.get('claim_ledger', []):
                if not isinstance(claim, dict):
                    continue
                text = str(claim.get('claim', '')).lower()
                if 'wohnung' in text or 'miete' in text:
                    topic_counts['Wohnen'] += 1
                if 'verkehr' in text or 'radweg' in text:
                    topic_counts['Verkehr'] += 1
                if 'klima' in text or 'energie' in text:
                    topic_counts['Klima'] += 1
                if 'digital' in text:
                    topic_counts['Digitalisierung'] += 1
                if 'haushalt' in text or 'schulden' in text:
                    topic_counts['Finanzen'] += 1

        for topic, count in topic_counts.most_common(5):
            patterns.append({
                'type': 'thematic',
                'pattern': f'{topic} in {count} Claims erwähnt',
                'confidence': 'verified',
                'eija': 'E'
            })

        return patterns

    # ── VERIFIED TRUTHS ──

    def extract_verified_truths(self) -> List[Dict]:
        """Extract facts verified by multiple sources."""
        # Claims with CORE tier and E label
        rows = self.conn.execute("""
            SELECT city_slug, claim, confidence
            FROM claims
            WHERE eija = 'E' AND tier = 'CORE'
            ORDER BY confidence DESC
        """).fetchall()

        truths = []
        for r in rows:
            truths.append({
                'type': 'verified_truth',
                'fact': r['claim'],
                'city': r['city_slug'],
                'confidence': r['confidence'],
                'tier': 'CORE'
            })
        return truths

    # ── FULL EXTRACTION ──

    def extract_all(self) -> Dict:
        """Run full knowledge extraction."""
        error_fixes = self.extract_error_fix_pairs()
        patterns = self.extract_cross_city_patterns()
        truths = self.extract_verified_truths()

        knowledge_base = {
            'error_fixes': error_fixes,
            'cross_city_patterns': patterns,
            'verified_truths_count': len(truths),
            'verified_truths_sample': truths[:20],  # Top 20
            'stats': {
                'error_fix_pairs': len(error_fixes),
                'cross_city_patterns': len(patterns),
                'verified_truths': len(truths),
            }
        }

        # Export
        out = CITIES_DIR.parent / 'knowledge-base.json'
        with open(out, 'w') as f:
            json.dump(knowledge_base, f, indent=2, ensure_ascii=False)

        return knowledge_base


if __name__ == '__main__':
    ke = KnowledgeExtractor()
    kb = ke.extract_all()

    print(f"{'='*60}")
    print(f"KNOWLEDGE EXTRACTION")
    print(f"{'='*60}")
    print(f"\n  Error→Fix Pairs:     {kb['stats']['error_fix_pairs']}")
    print(f"  Cross-City Patterns: {kb['stats']['cross_city_patterns']}")
    print(f"  Verified Truths:     {kb['stats']['verified_truths']}")

    print(f"\n  ## Cross-City Patterns")
    for p in kb['cross_city_patterns']:
        print(f"    [{p['eija']}] {p['pattern']}")

    print(f"\n  ## Error→Fix Pairs")
    for p in kb['error_fixes'][:5]:
        print(f"    ❌ {p.get('error_pattern', '?')[:60]}")
        print(f"    ✅ {p.get('fix', '?')[:60]}")

    ke.close()

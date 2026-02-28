#!/usr/bin/env python3
"""
Single Source of Truth: SQLite database for all election intelligence.
Replaces scattered JSON files with queryable, typed data.

Usage:
    from db import ElectionDB
    db = ElectionDB()
    db.query_candidates(party="CSU", amtsinhaber=True)
    db.query_claims(eija="E", tier="CORE")
    db.cross_city_stats()
"""

import sqlite3
import json
import os
import re
from pathlib import Path
from collections import Counter, defaultdict

DB_PATH = Path(__file__).parent / "learning.db"
CITIES_DIR = Path(__file__).parent.parent / "data" / "cities"


class ElectionDB:
    def __init__(self, db_path=None):
        self.db_path = db_path or DB_PATH
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self._ensure_schema()

    def _ensure_schema(self):
        """Add columns if missing (backwards compatible)."""
        c = self.conn.cursor()
        # Check if tier column exists on claims
        cols = [row[1] for row in c.execute("PRAGMA table_info(claims)").fetchall()]
        if 'tier' not in cols:
            c.execute("ALTER TABLE claims ADD COLUMN tier TEXT DEFAULT 'EPHEMERAL'")
        if 'temporal_weight' not in cols:
            c.execute("ALTER TABLE claims ADD COLUMN temporal_weight REAL DEFAULT 1.0")
        self.conn.commit()

    def close(self):
        self.conn.close()

    # ── QUERIES ──────────────────────────────────────────

    def query_candidates(self, party=None, amtsinhaber=None, city=None, min_result_2020=None):
        """Query candidates with filters. Returns list of dicts."""
        sql = "SELECT * FROM candidates WHERE 1=1"
        params = []
        if party:
            sql += " AND party LIKE ?"
            params.append(f"%{party}%")
        if amtsinhaber is not None:
            sql += " AND amtsinhaber = ?"
            params.append(1 if amtsinhaber else 0)
        if city:
            sql += " AND city_slug LIKE ?"
            params.append(f"%{city}%")
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    def query_claims(self, eija=None, tier=None, city=None, keyword=None):
        """Query claims with filters."""
        sql = "SELECT * FROM claims WHERE 1=1"
        params = []
        if eija:
            sql += " AND eija = ?"
            params.append(eija)
        if tier:
            sql += " AND tier = ?"
            params.append(tier)
        if city:
            sql += " AND city_slug LIKE ?"
            params.append(f"%{city}%")
        if keyword:
            sql += " AND claim LIKE ?"
            params.append(f"%{keyword}%")
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    def query_sources(self, domain=None, city=None, source_type=None):
        """Query sources with filters."""
        sql = "SELECT * FROM sources WHERE 1=1"
        params = []
        if domain:
            sql += " AND url LIKE ?"
            params.append(f"%{domain}%")
        if city:
            sql += " AND city_slug LIKE ?"
            params.append(f"%{city}%")
        if source_type:
            sql += " AND type = ?"
            params.append(source_type)
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    # ── ANALYTICS ────────────────────────────────────────

    def cross_city_stats(self):
        """Full cross-city analysis. Returns dict with all stats."""
        c = self.conn.cursor()
        stats = {}

        # Totals
        stats['cities'] = c.execute("SELECT COUNT(DISTINCT city_slug) FROM candidates").fetchone()[0]
        stats['candidates'] = c.execute("SELECT COUNT(*) FROM candidates").fetchone()[0]
        stats['sources'] = c.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
        stats['claims'] = c.execute("SELECT COUNT(*) FROM claims").fetchone()[0]

        # Party distribution
        stats['parties'] = {r[0]: r[1] for r in c.execute(
            "SELECT party, COUNT(*) FROM candidates WHERE party != '' GROUP BY party ORDER BY COUNT(*) DESC"
        ).fetchall()}

        # EIJA distribution
        stats['eija'] = {r[0]: r[1] for r in c.execute(
            "SELECT eija, COUNT(*) FROM claims WHERE length(eija)=1 GROUP BY eija ORDER BY COUNT(*) DESC"
        ).fetchall()}

        # Tier distribution
        stats['tiers'] = {r[0]: r[1] for r in c.execute(
            "SELECT tier, COUNT(*) FROM claims WHERE tier IS NOT NULL GROUP BY tier ORDER BY COUNT(*) DESC"
        ).fetchall()}

        # Amtsinhaber by party
        stats['amtsinhaber_parties'] = {r[0]: r[1] for r in c.execute(
            "SELECT party, COUNT(*) FROM candidates WHERE amtsinhaber=1 GROUP BY party ORDER BY COUNT(*) DESC"
        ).fetchall()}

        return stats

    def source_bias(self):
        """Analyze source domain concentration."""
        rows = self.conn.execute(
            "SELECT url FROM sources WHERE url IS NOT NULL"
        ).fetchall()
        domains = Counter()
        for row in rows:
            m = re.search(r'https?://(?:www\.)?([^/]+)', row[0] or '')
            if m:
                domains[m.group(1)] += 1
        return dict(domains.most_common(20))

    def find_contradictions(self, city=None):
        """Find claims that might contradict each other."""
        sql = "SELECT city_slug, claim, eija, confidence FROM claims"
        if city:
            sql += f" WHERE city_slug LIKE '%{city}%'"
        claims = self.conn.execute(sql).fetchall()

        contradictions = []
        claims_by_city = defaultdict(list)
        for c in claims:
            claims_by_city[c[0]].append({'claim': c[1], 'eija': c[2], 'conf': c[3]})

        for city_slug, city_claims in claims_by_city.items():
            for i, c1 in enumerate(city_claims):
                for c2 in city_claims[i+1:]:
                    # Check for conflicting percentages about same person
                    nums1 = re.findall(r'(\d{2,3}[.,]?\d?)\s*%', c1['claim'])
                    nums2 = re.findall(r'(\d{2,3}[.,]?\d?)\s*%', c2['claim'])
                    if nums1 and nums2 and nums1[0] != nums2[0]:
                        # Check if same entity mentioned
                        words1 = set(c1['claim'].split())
                        words2 = set(c2['claim'].split())
                        overlap = words1 & words2
                        if len(overlap) > 5:
                            contradictions.append({
                                'city': city_slug,
                                'claim1': c1['claim'][:100],
                                'claim2': c2['claim'][:100],
                                'pct1': nums1[0],
                                'pct2': nums2[0]
                            })
        return contradictions

    # ── MONTE CARLO ──────────────────────────────────────

    def simulate(self, city_slug, n_sims=10000, seed=2026):
        """Run Monte Carlo simulation for a city. Returns results dict."""
        import random
        random.seed(seed)

        # Load city data
        city_path = CITIES_DIR / f"{city_slug}.json"
        if not city_path.exists():
            return {'error': f'City {city_slug} not found'}

        with open(city_path) as f:
            d = json.load(f)

        forecast = d.get('forecast', {})
        if not isinstance(forecast, dict):
            return {'error': 'No forecast data'}

        candidates = []
        for kf in forecast.get('kandidaten', []):
            nums = re.findall(r'(\d+)', str(kf.get('erstwahlgang', '')))
            if len(nums) >= 2:
                candidates.append({
                    'name': kf.get('name', '?'),
                    'lo': int(nums[0]),
                    'hi': int(nums[1])
                })

        if len(candidates) < 2:
            return {'error': 'Not enough candidates with forecast ranges'}

        results = {c['name']: {'wins_r1': 0, 'in_stw': 0, 'wins_stw': 0} for c in candidates}
        stw_count = 0

        for _ in range(n_sims):
            votes = {}
            total = 0
            for c in candidates:
                mid = (c['lo'] + c['hi']) / 2
                spread = (c['hi'] - c['lo']) / 2
                v = random.gauss(mid, spread * 0.8)
                v = max(1, min(95, v))
                votes[c['name']] = v
                total += v
            for name in votes:
                votes[name] = votes[name] / total * 100

            winner = max(votes, key=votes.get)
            if votes[winner] > 50:
                results[winner]['wins_r1'] += 1
            else:
                stw_count += 1
                s = sorted(votes.items(), key=lambda x: -x[1])
                for name, _ in s[:2]:
                    results[name]['in_stw'] += 1
                ratio = s[0][1] / (s[0][1] + s[1][1])
                if random.gauss(ratio, 0.08) > 0.5:
                    results[s[0][0]]['wins_stw'] += 1
                else:
                    results[s[1][0]]['wins_stw'] += 1

        return {
            'city': city_slug,
            'simulations': n_sims,
            'stichwahl_pct': round(stw_count / n_sims * 100, 1),
            'candidates': {
                name: {
                    'wins_r1_pct': round(r['wins_r1'] / n_sims * 100, 1),
                    'reaches_stw_pct': round(r['in_stw'] / max(1, stw_count) * 100, 1),
                    'wins_overall_pct': round((r['wins_r1'] + r['wins_stw']) / n_sims * 100, 1)
                }
                for name, r in results.items()
            },
            'methodology': 'Gauss(agent_estimate, spread*0.8), 10k sims. INPUT IS AGENT ESTIMATES, NOT POLLS.',
            'robust_claim': 'Stichwahl ja/nein is reliable. Winner prediction is NOT.'
        }

    # ── UTILITIES ────────────────────────────────────────

    def city_summary(self, city_slug):
        """Full summary for one city. LLM-friendly output."""
        c = self.conn.cursor()
        candidates = self.query_candidates(city=city_slug)
        claims = self.query_claims(city=city_slug)
        sources = self.query_sources(city=city_slug)

        # Load intelligence layer
        city_path = CITIES_DIR / f"{city_slug}.json"
        intel = {}
        if city_path.exists():
            with open(city_path) as f:
                d = json.load(f)
            intel = d.get('intelligence', {})

        return {
            'candidates': len(candidates),
            'sources': len(sources),
            'claims': len(claims),
            'eija': Counter(c.get('eija', '?') for c in claims),
            'tiers': Counter(c.get('tier', '?') for c in claims),
            'intelligence': intel,
            'candidate_details': candidates
        }


if __name__ == '__main__':
    db = ElectionDB()
    stats = db.cross_city_stats()
    print(json.dumps(stats, indent=2, ensure_ascii=False, default=str))
    db.close()

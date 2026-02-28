#!/usr/bin/env python3
"""
Bayern Kommunalwahl 2026 — Intelligence CLI

Single entry point for all operations. Designed for LLM + human use.

Usage:
    python3 cli.py status              # Overview of all 50 cities
    python3 cli.py validate <city>     # Validate one city (score 0-100)
    python3 cli.py validate-all        # Validate all, show failures
    python3 cli.py analyze             # Cross-city analysis
    python3 cli.py simulate <city>     # Monte Carlo for one city
    python3 cli.py simulate-all        # Monte Carlo for all OB cities
    python3 cli.py query <sql>         # Raw SQL on learning.db
    python3 cli.py candidates [--party CSU] [--amtsinhaber] [--city muenchen]
    python3 cli.py claims [--eija E] [--tier CORE] [--city muenchen]
    python3 cli.py sources [--domain br.de] [--city muenchen]
    python3 cli.py bias                # Source domain concentration
    python3 cli.py contradictions      # Find conflicting claims
    python3 cli.py scorecard           # Generate election scorecard
    python3 cli.py audit               # Full quality audit
"""

import sys
import json
import os
import subprocess
from pathlib import Path

RAG_DIR = Path(__file__).parent
CITIES_DIR = RAG_DIR.parent / "data" / "cities"


def cmd_status():
    """Show status of all 50 cities."""
    from db import ElectionDB
    db = ElectionDB()
    stats = db.cross_city_stats()

    print(f"{'='*60}")
    print(f"BAYERN KOMMUNALWAHL 2026 — STATUS")
    print(f"{'='*60}")
    print(f"  Städte:     {stats['cities']}")
    print(f"  Kandidaten: {stats['candidates']}")
    print(f"  Quellen:    {stats['sources']}")
    print(f"  Claims:     {stats['claims']}")
    print(f"\n  Top Parteien:")
    for p, c in list(stats['parties'].items())[:8]:
        print(f"    {p}: {c}")
    print(f"\n  EIJA: {stats['eija']}")
    print(f"  Tiers: {stats['tiers']}")
    print(f"\n  Amtsinhaber: {stats['amtsinhaber_parties']}")
    db.close()


def cmd_validate(city=None):
    """Validate one or all cities."""
    if city:
        subprocess.run([sys.executable, str(RAG_DIR / "normalize_city.py"), city])
        subprocess.run([sys.executable, str(RAG_DIR / "validate_research.py"), city])
    else:
        # Validate all
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix == '.json' and f.stem != 'internal':
                subprocess.run([sys.executable, str(RAG_DIR / "normalize_city.py"), f.stem],
                             capture_output=True)
                result = subprocess.run([sys.executable, str(RAG_DIR / "validate_research.py"), f.stem],
                                      capture_output=True, text=True)
                # Show only PASS/FAIL line
                for line in result.stdout.split('\n'):
                    if 'PASS' in line or 'FAIL' in line:
                        print(line.strip())


def cmd_analyze():
    """Cross-city analysis with verified patterns."""
    from db import ElectionDB
    db = ElectionDB()
    stats = db.cross_city_stats()
    bias = db.source_bias()

    print(f"\n{'='*60}")
    print(f"CROSS-CITY ANALYSE")
    print(f"{'='*60}")

    print(f"\n## Quellen-Bias (Top 10 Domains)")
    total = sum(bias.values())
    for domain, count in list(bias.items())[:10]:
        pct = count / total * 100
        bar = '█' * int(pct)
        print(f"  {domain:<30} {count:>4} ({pct:.1f}%) {bar}")

    print(f"\n## EIJA-Verteilung")
    total_eija = sum(stats['eija'].values())
    for e, c in stats['eija'].items():
        print(f"  {e}: {c} ({c/total_eija*100:.0f}%)")

    print(f"\n## Knowledge Tiers")
    for t, c in stats['tiers'].items():
        print(f"  {t}: {c}")

    # Contradictions
    contras = db.find_contradictions()
    print(f"\n## Widersprüche: {len(contras)} gefunden")
    for c in contras[:5]:
        print(f"  {c['city']}: {c['pct1']}% vs {c['pct2']}%")

    db.close()


def cmd_simulate(city=None):
    """Monte Carlo simulation."""
    from db import ElectionDB
    db = ElectionDB()

    if city:
        result = db.simulate(city)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # All OB cities
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            with open(f) as fh:
                d = json.load(fh)
            tenant = d.get('tenant', {})
            wahl = tenant.get('wahl', {}) if isinstance(tenant, dict) else {}
            if not isinstance(wahl, dict) or wahl.get('typ') not in ('OB-Wahl', 'BM-Wahl'):
                continue
            gemeinde = tenant.get('gemeinde', f.stem) if isinstance(tenant, dict) else f.stem
            result = db.simulate(f.stem)
            if 'error' not in result:
                sorted_c = sorted(result['candidates'].items(), key=lambda x: -x[1]['wins_overall_pct'])
                top = sorted_c[0] if sorted_c else ('?', {'wins_overall_pct': 0})
                print(f"  {gemeinde:<20} STW:{result['stichwahl_pct']:>5}% | {top[0][:15]:<16} {top[1]['wins_overall_pct']}%")

    db.close()


def cmd_candidates(args):
    """Query candidates."""
    from db import ElectionDB
    db = ElectionDB()
    kwargs = {}
    i = 0
    while i < len(args):
        if args[i] == '--party' and i+1 < len(args):
            kwargs['party'] = args[i+1]; i += 2
        elif args[i] == '--amtsinhaber':
            kwargs['amtsinhaber'] = True; i += 1
        elif args[i] == '--city' and i+1 < len(args):
            kwargs['city'] = args[i+1]; i += 2
        else:
            i += 1

    results = db.query_candidates(**kwargs)
    for r in results:
        ai = '🏆' if r.get('amtsinhaber') else '  '
        print(f"  {ai} {r.get('name','?'):<25} {r.get('party','?'):<15} {r.get('city_slug','?')}")
    print(f"\n  Total: {len(results)}")
    db.close()


def cmd_claims(args):
    """Query claims."""
    from db import ElectionDB
    db = ElectionDB()
    kwargs = {}
    i = 0
    while i < len(args):
        if args[i] == '--eija' and i+1 < len(args):
            kwargs['eija'] = args[i+1]; i += 2
        elif args[i] == '--tier' and i+1 < len(args):
            kwargs['tier'] = args[i+1]; i += 2
        elif args[i] == '--city' and i+1 < len(args):
            kwargs['city'] = args[i+1]; i += 2
        elif args[i] == '--keyword' and i+1 < len(args):
            kwargs['keyword'] = args[i+1]; i += 2
        else:
            i += 1

    results = db.query_claims(**kwargs)
    for r in results[:20]:
        print(f"  [{r.get('eija','?')}] [{r.get('tier','?'):<10}] {r.get('claim','')[:80]}")
    print(f"\n  Total: {len(results)} (showing first 20)")
    db.close()


def cmd_query(sql):
    """Raw SQL query."""
    from db import ElectionDB
    db = ElectionDB()
    try:
        rows = db.conn.execute(sql).fetchall()
        for row in rows[:50]:
            print(dict(row))
    except Exception as e:
        print(f"Error: {e}")
    db.close()


def cmd_audit():
    """Full quality audit."""
    from db import ElectionDB
    db = ElectionDB()
    stats = db.cross_city_stats()

    print(f"{'='*60}")
    print(f"QUALITY AUDIT")
    print(f"{'='*60}")

    # EIJA inflation check
    total_claims = sum(stats['eija'].values())
    e_pct = stats['eija'].get('E', 0) / max(1, total_claims) * 100
    print(f"\n  EIJA-E: {e_pct:.0f}% {'⚠️ INFLATED' if e_pct > 80 else '✅ OK'}")

    # Source bias
    bias = db.source_bias()
    top3_pct = sum(list(bias.values())[:3]) / max(1, stats['sources']) * 100
    print(f"  Top-3 Domains: {top3_pct:.0f}% {'⚠️ CONCENTRATED' if top3_pct > 20 else '✅ OK'}")

    # Empty fields
    empty_party = db.conn.execute("SELECT COUNT(*) FROM candidates WHERE party IS NULL OR party = ''").fetchone()[0]
    print(f"  Empty party: {empty_party} {'⚠️' if empty_party > 0 else '✅'}")

    # Contradictions
    contras = db.find_contradictions()
    print(f"  Contradictions: {len(contras)} {'⚠️' if len(contras) > 10 else '✅'}")

    # MC methodology warning
    print(f"\n  ⚠️ Monte Carlo: Based on agent estimates, NOT polls")
    print(f"  ⚠️ Reliable claim: Stichwahl ja/nein only")
    print(f"  ⚠️ No backtest against 2020 results")

    db.close()


def cmd_scorecard():
    """Generate election scorecard."""
    from db import ElectionDB
    db = ElectionDB()
    scorecard = []

    for f in sorted(CITIES_DIR.iterdir()):
        if f.suffix != '.json' or f.stem == 'internal':
            continue
        with open(f) as fh:
            d = json.load(fh)
        tenant = d.get('tenant', {})
        wahl = tenant.get('wahl', {}) if isinstance(tenant, dict) else {}
        if not isinstance(wahl, dict) or wahl.get('typ') not in ('OB-Wahl', 'BM-Wahl'):
            continue
        gemeinde = tenant.get('gemeinde', f.stem) if isinstance(tenant, dict) else f.stem

        mc = db.simulate(f.stem)
        if 'error' in mc:
            continue

        sorted_c = sorted(mc['candidates'].items(), key=lambda x: -x[1]['wins_overall_pct'])
        scorecard.append({
            'city': gemeinde,
            'slug': f.stem,
            'stichwahl_mc': mc['stichwahl_pct'],
            'prediction_stichwahl': 'JA' if mc['stichwahl_pct'] > 50 else 'NEIN',
            'r1_favorite': sorted_c[0][0] if sorted_c else '?',
            'r1_fav_win_pct': sorted_c[0][1]['wins_overall_pct'] if sorted_c else 0,
            'stw_matchup': f"{sorted_c[0][0]} vs {sorted_c[1][0]}" if len(sorted_c) >= 2 else '?',
        })

    out = CITIES_DIR.parent / "election-scorecard.json"
    with open(out, 'w') as f:
        json.dump(scorecard, f, indent=2, ensure_ascii=False)
    print(f"✅ Scorecard: {len(scorecard)} predictions → {out}")
    db.close()


# ── MAIN ──────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == 'status':
        cmd_status()
    elif cmd == 'validate':
        cmd_validate(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == 'validate-all':
        cmd_validate()
    elif cmd == 'analyze':
        cmd_analyze()
    elif cmd == 'simulate':
        cmd_simulate(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == 'simulate-all':
        cmd_simulate()
    elif cmd == 'candidates':
        cmd_candidates(sys.argv[2:])
    elif cmd == 'claims':
        cmd_claims(sys.argv[2:])
    elif cmd == 'sources':
        # Similar to claims
        from db import ElectionDB
        db = ElectionDB()
        results = db.query_sources()
        print(f"  Total sources: {len(results)}")
        db.close()
    elif cmd == 'query':
        cmd_query(' '.join(sys.argv[2:]))
    elif cmd == 'bias':
        from db import ElectionDB
        db = ElectionDB()
        bias = db.source_bias()
        for d, c in bias.items():
            print(f"  {d:<30} {c}")
        db.close()
    elif cmd == 'contradictions':
        from db import ElectionDB
        db = ElectionDB()
        contras = db.find_contradictions()
        for c in contras:
            print(f"  {c['city']}: {c['claim1'][:50]}... vs {c['claim2'][:50]}...")
        db.close()
    elif cmd == 'scorecard':
        cmd_scorecard()
    elif cmd == 'audit':
        cmd_audit()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)

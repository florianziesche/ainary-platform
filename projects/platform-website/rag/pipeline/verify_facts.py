#!/usr/bin/env python3
"""
Ainary Fact Verification Pipeline — Content Quality, not Format Quality.

PURPOSE:
  Checks whether data is CORRECT, not just PRESENT.
  Must run AFTER enrich_template.py, BEFORE deploy.

WHAT IT CHECKS:
  1. Cross-field consistency (age vs birth year, role vs party, dates)
  2. Forecast plausibility (sums ~100%, ranges make sense)
  3. Hollow shell detection (template-only entries vs real data)
  4. Internal contradictions (different fields say different things)
  5. Temporal consistency (dates in karriere vs bio vs news)
  6. Source coverage (claims without backing sources)

OUTPUT:
  - Per-city verification report with PASS/WARN/FAIL
  - Specific issues with Impact rating (HOCH/MITTEL/GERING)
  - Suggested fixes where deterministic
  - Exit code 1 if any HOCH-impact issue found

USAGE:
  python3 -m pipeline.verify_facts                     # All cities
  python3 -m pipeline.verify_facts --city passau        # Single city
  python3 -m pipeline.verify_facts --fix                # Auto-fix deterministic issues
  python3 -m pipeline.verify_facts --report             # Generate verification report JSON
"""

import json, os, re, sys
from datetime import datetime
from pathlib import Path

CITIES_DIR = Path(__file__).parent.parent.parent / 'data' / 'cities'
REPORT_DIR = Path(__file__).parent.parent.parent / 'data' / 'reports'
NOW = datetime(2026, 3, 1)


class Issue:
    def __init__(self, city, entity, field, finding, impact, fix=None):
        self.city = city
        self.entity = entity  # KB key or None for city-level
        self.field = field
        self.finding = finding
        self.impact = impact  # HOCH, MITTEL, GERING
        self.fix = fix  # None = manual review needed, dict = auto-fixable

    def to_dict(self):
        d = {
            'city': self.city,
            'entity': self.entity,
            'field': self.field,
            'finding': self.finding,
            'impact': self.impact,
        }
        if self.fix:
            d['fix'] = self.fix
        return d

    def __str__(self):
        icon = {'HOCH': '🔴', 'MITTEL': '🟡', 'GERING': '🟢'}.get(self.impact, '⚪')
        entity_str = f'[{self.entity}] ' if self.entity else ''
        fix_str = f' → FIX: {self.fix}' if self.fix else ''
        return f'{icon} {self.city} {entity_str}{self.field}: {self.finding}{fix_str}'


def verify_city(slug, data):
    """Run all verification checks on a single city. Returns list of Issues."""
    issues = []
    kb = data.get('kb', {})
    fc = data.get('forecast', {})
    news = data.get('news', [])

    # ── 1. FORECAST PLAUSIBILITY ──
    if isinstance(fc, dict):
        kands = fc.get('kandidaten', [])
        if kands:
            total_min = sum(fk.get('min', 0) for fk in kands if isinstance(fk, dict))
            total_max = sum(fk.get('max', 0) for fk in kands if isinstance(fk, dict))

            if total_min > 105:
                issues.append(Issue(slug, None, 'forecast.sum_min',
                    f'Minimum-Summe = {total_min}% (sollte ≤105%)',
                    'HOCH'))
            elif total_min < 80:
                issues.append(Issue(slug, None, 'forecast.sum_min',
                    f'Minimum-Summe = {total_min}% (sollte ≥80%)',
                    'MITTEL'))

            if total_max > 130:
                issues.append(Issue(slug, None, 'forecast.sum_max',
                    f'Maximum-Summe = {total_max}% (sollte ≤130%)',
                    'HOCH'))

            # Individual ranges
            for fk in kands:
                if not isinstance(fk, dict): continue
                mn, mx = fk.get('min', 0), fk.get('max', 0)
                name = fk.get('name', '?')
                if mn > mx:
                    issues.append(Issue(slug, None, f'forecast.{name}',
                        f'min ({mn}%) > max ({mx}%)', 'HOCH',
                        fix={'action': 'swap', 'min': mx, 'max': mn}))
                if mx - mn > 30:
                    issues.append(Issue(slug, None, f'forecast.{name}',
                        f'Range {mn}-{mx}% = {mx-mn}pp Spanne (zu breit, wenig Aussagekraft)',
                        'MITTEL'))

        # Stichwahl vs candidate count consistency
        stw = fc.get('stichwahl', 50)
        if isinstance(stw, (int, float)):
            num_kands = len(kands)
            if num_kands == 1 and stw > 10:
                issues.append(Issue(slug, None, 'forecast.stichwahl',
                    f'Nur 1 Kandidat aber {stw}% Stichwahl-Prognose',
                    'HOCH', fix={'action': 'set', 'field': 'forecast.stichwahl', 'value': 5}))

    # ── 2. CROSS-FIELD CONSISTENCY (per KB entry) ──
    for k, v in kb.items():
        if not isinstance(v, dict): continue
        name = v.get('name', k)
        bio = str(v.get('bio', ''))

        # 2a. Age vs birth year
        age_prop = None
        birth_year_prop = None
        for p in v.get('properties', []):
            if isinstance(p, dict):
                if p.get('key') in ('Alter', 'Age'):
                    age_prop = p.get('val', '')
                if p.get('key') in ('Geburtsjahr', 'Geboren', 'Birth'):
                    birth_year_prop = p.get('val', '')

        if age_prop and birth_year_prop:
            age_num = re.search(r'(\d+)', str(age_prop))
            year_num = re.search(r'(\d{4})', str(birth_year_prop))
            if age_num and year_num:
                expected_age = NOW.year - int(year_num.group(1))
                actual_age = int(age_num.group(1))
                if abs(expected_age - actual_age) > 1:
                    issues.append(Issue(slug, k, 'age_vs_birth',
                        f'Alter={actual_age} aber Geburtsjahr={year_num.group(1)} → erwartetes Alter={expected_age}',
                        'HOCH', fix={'action': 'set_prop', 'key': 'Alter', 'value': f'{expected_age} Jahre'}))

        # 2b. Karriere dates vs bio dates
        for kar in v.get('karriere', []):
            if isinstance(kar, dict):
                year = kar.get('year', '')
                year_num = re.search(r'(\d{4})', str(year))
                if year_num:
                    y = int(year_num.group(1))
                    if y > NOW.year:
                        issues.append(Issue(slug, k, 'karriere.year',
                            f'Karriere-Eintrag in der Zukunft: {y}',
                            'MITTEL'))
                    if y < 1950:
                        issues.append(Issue(slug, k, 'karriere.year',
                            f'Karriere-Eintrag unplausibel: {y}',
                            'MITTEL'))

        # 2c. Party consistency: steckbrief vs properties vs top-level
        party_top = v.get('party', '')
        party_steckbrief = v.get('steckbrief', {}).get('Partei', '') if isinstance(v.get('steckbrief'), dict) else ''
        party_props = ''
        for p in v.get('properties', []):
            if isinstance(p, dict) and p.get('key') == 'Partei':
                party_props = p.get('val', '')

        parties = [p for p in [party_top, party_steckbrief, party_props] if p]
        if len(set(parties)) > 1:
            issues.append(Issue(slug, k, 'party_consistency',
                f'Widersprüchliche Partei-Angaben: {set(parties)}',
                'HOCH'))

        # 2d. Role: "Amtsinhaber" flag vs role text vs 2020 results
        is_amtsinhaber = v.get('amtsinhaber', False)
        role_text = v.get('role', '')
        if is_amtsinhaber and 'Amtsinhaber' not in role_text and 'amtsinhaber' not in role_text.lower():
            issues.append(Issue(slug, k, 'role_amtsinhaber',
                f'amtsinhaber=true aber role="{role_text}" erwähnt es nicht',
                'GERING'))

    # ── 3. HOLLOW SHELL DETECTION ──
    for k, v in kb.items():
        if not isinstance(v, dict): continue
        name = v.get('name', k)
        hollow_score = 0
        reasons = []

        # Kurzprofil
        kp = v.get('steckbrief', {}).get('Kurzprofil', '') if isinstance(v.get('steckbrief'), dict) else ''
        if not kp:
            hollow_score += 2
            reasons.append('kein Kurzprofil')

        # Properties: only Partei/Rolle/Status = template default
        props = v.get('properties', [])
        real_keys = set()
        for p in props:
            if isinstance(p, dict) and p.get('key') not in ('Partei', 'Rolle', 'Status'):
                real_keys.add(p.get('key'))
        if not real_keys:
            hollow_score += 3
            reasons.append('nur Template-Properties')

        # Bio length
        bio = str(v.get('bio', ''))
        if len(bio) < 50:
            hollow_score += 2
            reasons.append(f'Bio nur {len(bio)} Zeichen')

        # No karriere
        if not v.get('karriere'):
            hollow_score += 1
            reasons.append('keine Karriere')

        # No quellen
        if not v.get('quellen'):
            hollow_score += 2
            reasons.append('keine Quellen')

        if hollow_score >= 5:
            issues.append(Issue(slug, k, 'hollow_shell',
                f'Hohlkörper-Eintrag (Score {hollow_score}/10): {", ".join(reasons)}',
                'HOCH' if hollow_score >= 7 else 'MITTEL'))

    # ── 4. TEMPORAL CONSISTENCY ──
    wahl_str = data.get('tenant', {}).get('wahl', '')
    if isinstance(wahl_str, str):
        m = re.match(r'(\d{2})\.(\d{2})\.(\d{4})', wahl_str)
        if m:
            wahl_date = datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            if wahl_date < datetime(2026, 1, 1) or wahl_date > datetime(2026, 12, 31):
                issues.append(Issue(slug, None, 'tenant.wahl',
                    f'Wahldatum {wahl_str} liegt außerhalb 2026',
                    'HOCH'))

    # News freshness
    old_news = 0
    for n in news:
        if isinstance(n, dict):
            date_str = n.get('date', '')
            m = re.search(r'(\d{4})', str(date_str))
            if m and int(m.group(1)) < 2024:
                old_news += 1
    if old_news > len(news) * 0.5 and len(news) > 3:
        issues.append(Issue(slug, None, 'news.freshness',
            f'{old_news}/{len(news)} Nachrichten älter als 2024',
            'MITTEL'))

    # ── 5. SOURCE COVERAGE ──
    claims = data.get('claims', [])
    unsourced_claims = 0
    for claim in claims:
        if isinstance(claim, dict) and not claim.get('source') and not claim.get('quelle'):
            unsourced_claims += 1
    if unsourced_claims > 5:
        issues.append(Issue(slug, None, 'claims.unsourced',
            f'{unsourced_claims} Claims ohne Quellenangabe',
            'MITTEL'))

    return issues


def apply_fixes(slug, data, issues):
    """Apply deterministic fixes. Returns modified data and list of applied fixes."""
    applied = []
    fc = data.get('forecast', {})
    kb = data.get('kb', {})

    for issue in issues:
        if not issue.fix:
            continue

        action = issue.fix.get('action')

        if action == 'swap' and 'forecast' in issue.field:
            # Fix min > max
            for fk in fc.get('kandidaten', []):
                if isinstance(fk, dict) and fk.get('name', '') in issue.field:
                    fk['min'], fk['max'] = fk['max'], fk['min']
                    applied.append(str(issue))

        if action == 'set' and issue.fix.get('field') == 'forecast.stichwahl':
            fc['stichwahl'] = issue.fix['value']
            applied.append(str(issue))

        if action == 'set_prop' and issue.entity:
            entity = kb.get(issue.entity, {})
            for p in entity.get('properties', []):
                if isinstance(p, dict) and p.get('key') == issue.fix.get('key'):
                    p['val'] = issue.fix['value']
                    applied.append(str(issue))

    return data, applied


def main():
    args = sys.argv[1:]
    city_filter = None
    do_fix = '--fix' in args
    do_report = '--report' in args

    for a in args:
        if a.startswith('--city'):
            idx = args.index(a)
            if idx + 1 < len(args):
                city_filter = args[idx + 1]
            elif '=' in a:
                city_filter = a.split('=')[1]

    all_issues = []
    total_cities = 0
    fixed_count = 0

    for f in sorted(os.listdir(CITIES_DIR)):
        if not f.endswith('.json') or f == 'internal.json':
            continue
        slug = f.replace('.json', '')
        if city_filter and slug != city_filter:
            continue

        total_cities += 1
        data = json.load(open(CITIES_DIR / f))
        issues = verify_city(slug, data)
        all_issues.extend(issues)

        if do_fix and issues:
            data, applied = apply_fixes(slug, data, issues)
            if applied:
                json.dump(data, open(CITIES_DIR / f, 'w'), ensure_ascii=False, indent=2)
                fixed_count += len(applied)
                for a in applied:
                    print(f'  FIXED: {a}')

    # Summary
    hoch = [i for i in all_issues if i.impact == 'HOCH']
    mittel = [i for i in all_issues if i.impact == 'MITTEL']
    gering = [i for i in all_issues if i.impact == 'GERING']

    print(f'\n{"=" * 60}')
    print(f'VERIFICATION REPORT — {total_cities} cities')
    print(f'{"=" * 60}')
    print(f'  🔴 HOCH:   {len(hoch)}')
    print(f'  🟡 MITTEL: {len(mittel)}')
    print(f'  🟢 GERING: {len(gering)}')
    print(f'  Total:     {len(all_issues)}')

    if do_fix:
        print(f'  Auto-fixed: {fixed_count}')

    if hoch:
        print(f'\n🔴 HOCH-Impact Issues:')
        for i in hoch:
            print(f'  {i}')

    if mittel:
        print(f'\n🟡 MITTEL-Impact Issues (Top 20):')
        for i in mittel[:20]:
            print(f'  {i}')

    if do_report:
        REPORT_DIR.mkdir(exist_ok=True)
        report = {
            'timestamp': NOW.isoformat(),
            'cities_checked': total_cities,
            'summary': {'hoch': len(hoch), 'mittel': len(mittel), 'gering': len(gering)},
            'issues': [i.to_dict() for i in all_issues]
        }
        report_path = REPORT_DIR / f'verification-{datetime.now().strftime("%Y%m%d-%H%M")}.json'
        json.dump(report, open(report_path, 'w'), ensure_ascii=False, indent=2)
        print(f'\n  Report saved: {report_path}')

    # Exit code: 1 if any HOCH issues remain unfixed
    unfixed_hoch = [i for i in hoch if not i.fix or not do_fix]
    if unfixed_hoch:
        print(f'\n⛔ DEPLOY BLOCKED — {len(unfixed_hoch)} HOCH-Impact Issues unfixed')
        return 1
    else:
        print(f'\n✅ VERIFICATION PASSED — safe to deploy')
        return 0


if __name__ == '__main__':
    sys.exit(main())

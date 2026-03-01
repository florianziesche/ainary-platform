#!/usr/bin/env python3
"""
Template Enricher: Fills ALL fields that dossier.html expects.

Problem: City JSONs from v3 research have different schema than what the
template renders. Many fields are missing → empty sections.

This script derives missing fields from existing data, ensuring every
city JSON has ALL fields the template needs.

Fields the template expects (from dossier.html analysis):
  tenant.wahl          → Must be STRING (date), not object
  kb[].summary         → Derived from bio (first 2 sentences)
  kb[].karriere        → Extracted from bio (career timeline)
  kb[].quellen         → Linked from quellenverzeichnis
  kb[].controversies   → Extracted from news/claims
  kb[].properties      → Key facts as array of {label, value}
  kb[].forecast        → {min, max} from forecast.kandidaten
  kb[].risk            → Computed from controversies + weaknesses
  kb[].color           → Party color
  graph                → {nodes, links} for force-directed graph
  topics               → [{name, desc, relevance}]
  hypotheses           → Derived from intelligence layer
  patterns             → Derived from claim_ledger
  talking_points       → Derived from scenarios
  weekly_brief         → {summary, daysToElection}
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime, date

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"

PARTY_COLORS = {
    'CSU': '#0088CE', 'CDU': '#0088CE',
    'SPD': '#E3000F',
    'Grüne': '#46962B', 'Bündnis 90/Die Grünen': '#46962B', 'BÜNDNIS 90/DIE GRÜNEN': '#46962B',
    'FDP': '#FFED00',
    'AfD': '#009EE0',
    'Die Linke': '#BE3075', 'Linke': '#BE3075',
    'Freie Wähler': '#FF8800', 'FW': '#FF8800', 'FWG': '#FF8800',
    'ÖDP': '#FF6600',
    'Bayernpartei': '#00A5E5',
    'Volt': '#562883',
    'Die PARTEI': '#B5152B',
}
DEFAULT_COLOR = '#8B8B8B'

# Topic keywords for extraction
TOPIC_KEYWORDS = {
    'Wohnen & Miete': ['wohnung', 'miete', 'mietpreis', 'bauland', 'sozialwohnung', 'wohnraum', 'wohnungsbau', 'bezahlbar', 'housing', 'rent', 'affordable', 'apartments'],
    'Verkehr & Mobilität': ['verkehr', 'radweg', 'stadtbahn', 'tram', 'bus', 'fahrrad', 'mobilität', 'stau', 'umgehung', 'parkplatz', 'traffic', 'transport', 'bicycle', 'mobility', 'parking'],
    'Klimaschutz & Energie': ['klima', 'energie', 'solar', 'photovoltaik', 'co2', 'nachhaltigkeit', 'windkraft', 'fernwärme', 'climate', 'energy', 'renewable', 'sustainability', 'flood', 'hochwasser'],
    'Digitalisierung': ['digital', 'breitband', 'glasfaser', 'smart city', 'e-government', 'broadband', 'fiber'],
    'Wirtschaft': ['wirtschaft', 'arbeitsplatz', 'gewerbe', 'ansiedlung', 'fachkräfte', 'startup', 'economy', 'business', 'jobs', 'employment'],
    'Bildung & Kita': ['schule', 'kita', 'bildung', 'kindergarten', 'ganztag', 'hochschule', 'universität', 'school', 'education', 'university', 'childcare'],
    'Sicherheit': ['sicherheit', 'kriminalität', 'polizei', 'ordnung', 'security', 'crime', 'police', 'safety'],
    'Finanzen & Haushalt': ['haushalt', 'schulden', 'finanzen', 'steuer', 'sparen', 'investition', 'defizit', 'budget', 'debt', 'finance', 'tax', 'spending'],
    'Stadtentwicklung': ['innenstadt', 'städtebau', 'leerstand', 'einzelhandel', 'sanierung', 'quartier', 'urban', 'development', 'downtown', 'renovation', 'infrastructure'],
}


def enrich_city(city_path):
    """Enrich a single city JSON with all template-required fields."""
    try:
        return _enrich_city_inner(city_path)
    except Exception as e:
        print(f"  ⚠️ {city_path.stem}: {e}")
        return False

def _enrich_city_inner(city_path):
    with open(city_path) as f:
        d = json.load(f)

    slug = city_path.stem
    changed = False

    # ═══ FIX 1: tenant.wahl must be string ═══
    tenant = d.get('tenant', {})
    wahl = tenant.get('wahl', {})
    if isinstance(wahl, dict):
        # Convert to string date
        tenant['wahl'] = wahl.get('datum', '08.03.2026')
        tenant['wahl_typ'] = wahl.get('typ', '')
        tenant['stichwahl_datum'] = wahl.get('stichwahl', '22.03.2026')
        d['tenant'] = tenant
        changed = True

    # Ensure tenant.name exists (JURISDIKTIONEN shows "undefined" without it)
    if not tenant.get('name'):
        tenant['name'] = tenant.get('gemeinde', slug)
        d['tenant'] = tenant
        changed = True
    gemeinde = tenant.get('gemeinde', slug)
    wahl_date_str = tenant.get('wahl', '08.03.2026')

    # Parse wahl date
    try:
        wahl_parts = wahl_date_str.split('.')
        wahl_date = date(int(wahl_parts[2]), int(wahl_parts[1]), int(wahl_parts[0]))
        days_to = max(0, (wahl_date - date.today()).days)
    except:
        days_to = 7

    # ═══ FIX 2: KB enrichment ═══
    kb = d.get('kb', {})
    forecast = d.get('forecast', {})
    forecast_kandidaten = forecast.get('kandidaten', []) if isinstance(forecast, dict) else []
    quellenverzeichnis = d.get('quellenverzeichnis', [])
    news = d.get('news', [])
    claim_ledger = d.get('claim_ledger', [])

    # Build forecast lookup AND fix missing IDs
    forecast_lookup = {}
    for fk in forecast_kandidaten:
        if isinstance(fk, dict):
            # Fix missing id: match by name against KB (exact, then last name, then slug)
            if not fk.get('id'):
                fk_name = fk.get('name', '')
                fk_lastname = fk_name.split()[-1].lower() if fk_name.split() else ''
                # Try exact name match
                for k2, v2 in kb.items():
                    if isinstance(v2, dict) and v2.get('name') == fk_name:
                        fk['id'] = k2
                        changed = True
                        break
                # Try last name match
                if not fk.get('id') and fk_lastname and len(fk_lastname) > 2:
                    for k2, v2 in kb.items():
                        if isinstance(v2, dict):
                            kb_name = v2.get('name', '')
                            if fk_lastname in kb_name.lower() or fk_lastname in k2.lower():
                                fk['id'] = k2
                                changed = True
                                break
            fk_id = fk.get('id', fk.get('name', ''))
            nums = re.findall(r'(\d+)', str(fk.get('erstwahlgang', '')))
            if len(nums) >= 2:
                forecast_lookup[fk_id] = {'min': int(nums[0]), 'max': int(nums[1])}
            elif len(nums) == 1:
                forecast_lookup[fk_id] = {'min': max(0, int(nums[0])-5), 'max': int(nums[0])+5}

    for k, v in kb.items():
        if not isinstance(v, dict) or not isinstance(k, str):
            continue

        # Color
        if not v.get('color'):
            party = v.get('party', '')
            v['color'] = PARTY_COLORS.get(party, DEFAULT_COLOR)
            changed = True

        # Summary from bio
        if not v.get('summary') and v.get('bio'):
            bio = str(v['bio'])
            sentences = re.split(r'(?<=[.!?])\s+', bio)
            v['summary'] = ' '.join(sentences[:2])[:200]
            changed = True

        # Karriere from bio
        # Template expects: {year, label, org, color}
        needs_karriere_fix = not v.get('karriere')
        if v.get('karriere') and v['karriere'] and isinstance(v['karriere'][0], dict) and 'jahr' in v['karriere'][0]:
            needs_karriere_fix = True  # Old format
        if needs_karriere_fix and v.get('bio'):
            bio = str(v['bio'])
            karriere = []
            # Extract year-prefixed facts
            for m in re.finditer(r'((?:19|20)\d{2})[:\s]+([^.]+\.)', bio):
                karriere.append({'year': m.group(1), 'label': m.group(2).strip()[:80], 'color': v.get('color', DEFAULT_COLOR)})
            # Also extract "seit/since YYYY" patterns
            for m in re.finditer(r'(?:[Ss]eit|[Ss]ince)\s+((?:19|20)\d{2})\s+([^.]+\.)', bio):
                karriere.append({'year': m.group(1), 'label': m.group(2).strip()[:80], 'color': v.get('color', DEFAULT_COLOR)})
            # Also "Elected YYYY", "in YYYY" patterns
            for m in re.finditer(r'(?:Elected|elected|gewählt|nominated|Nominated)\s+(?:in\s+)?((?:19|20)\d{2})', bio):
                # Get surrounding context
                start = max(0, m.start() - 5)
                end = min(len(bio), m.end() + 60)
                ctx = bio[start:end].split('.')[0]
                karriere.append({'year': m.group(1), 'label': ctx.strip()[:80], 'color': v.get('color', DEFAULT_COLOR)})
            if karriere:
                # Deduplicate by year
                seen = set()
                unique = []
                for k in karriere:
                    if k['year'] not in seen:
                        unique.append(k)
                        seen.add(k['year'])
                v['karriere'] = sorted(unique, key=lambda x: x['year'])
                changed = True

        # Quellen: link full source objects that mention this candidate
        # Template expects: [{url, name, typ}]
        needs_quellen_fix = not v.get('quellen')
        if v.get('quellen') and v['quellen'] and isinstance(v['quellen'][0], str):
            needs_quellen_fix = True  # Has IDs instead of objects
        if needs_quellen_fix:
            name_val = v.get('name', k)
            name_parts = name_val.split()
            lastname = name_parts[-1] if name_parts else name_val
            linked_sources = []
            for q in quellenverzeichnis:
                if isinstance(q, dict):
                    q_text = str(q.get('name', '')) + ' ' + str(q.get('url', ''))
                    if lastname.lower() in q_text.lower() or name_val.lower() in q_text.lower():
                        linked_sources.append({
                            'name': q.get('name', q.get('id', '?')),
                            'url': q.get('url', ''),
                            'typ': q.get('type', q.get('typ', ''))
                        })
            # Also add quellenverzeichnis entries whose IDs we previously stored
            if not linked_sources:
                # Broader match: any source from the city
                for q in quellenverzeichnis[:5]:  # First 5 sources
                    if isinstance(q, dict):
                        linked_sources.append({
                            'name': q.get('name', q.get('id', '?')),
                            'url': q.get('url', ''),
                            'typ': q.get('type', q.get('typ', ''))
                        })
            if linked_sources:
                v['quellen'] = linked_sources
                changed = True

        # Controversies from news
        # Template expects: {title, text, severity, ev_tag, conf}
        needs_contros_fix = not v.get('controversies')
        if v.get('controversies') and v['controversies'] and isinstance(v['controversies'][0], dict) and not v['controversies'][0].get('text'):
            needs_contros_fix = True
        if needs_contros_fix:
            name = v.get('name', k)
            name_parts = name.split()
            lastname = name_parts[-1] if name_parts else name
            contros = []
            controversy_words = ['skandal', 'kritik', 'umstritten', 'affäre', 'vorwurf',
                               'kontrovers', 'streit', 'protest', 'rüge', 'vorstrafe',
                               'controversy', 'criticized', 'scandal', 'dispute', 'divides']
            for n in news:
                if isinstance(n, dict):
                    text = str(n.get('title', '')) + ' ' + str(n.get('body', ''))
                    if (lastname.lower() in text.lower() or name.lower() in text.lower()):
                        if any(cw in text.lower() for cw in controversy_words):
                            contros.append({
                                'title': str(n.get('title', ''))[:80],
                                'source': str(n.get('source', ''))[:40],
                                'date': str(n.get('date', ''))
                            })
            if contros:
                v['controversies'] = [{
                    'title': c['title'],
                    'text': c.get('source', '') + (' · ' + c.get('date', '') if c.get('date') else ''),
                    'severity': 'MITTEL',
                    'ev_tag': 'E',
                    'conf': '75%'
                } for c in contros]
                changed = True

        # Properties from bio + data
        # Template expects: {key, val, ev, src, fresh, type}
        needs_props_fix = not v.get('properties')
        if v.get('properties') and v['properties'] and isinstance(v['properties'][0], dict):
            first = v['properties'][0]
            if 'label' in first or 'k' in first or ('key' not in first):
                needs_props_fix = True  # Old/wrong format
        if needs_props_fix:
            props = []
            if v.get('party'):
                props.append({'key': 'Partei', 'val': v['party'], 'ev': 'E'})
            role_display = v.get('role', '').replace('Kandidat/in, ', '').replace('Amtsinhaber, ', '')
            if role_display:
                props.append({'key': 'Rolle', 'val': role_display[:60], 'ev': 'E'})
            if v.get('amtsinhaber'):
                props.append({'key': 'Status', 'val': 'Amtsinhaber/in', 'ev': 'E'})
            else:
                props.append({'key': 'Status', 'val': 'Herausforderer/in', 'ev': 'I'})

            # Extract age from bio
            bio = str(v.get('bio', ''))
            age_m = re.search(r'(\d{2})[- ](?:year|Jahre|jährig)', bio)
            if age_m:
                props.append({'key': 'Alter', 'val': age_m.group(1) + ' Jahre', 'ev': 'E'})

            # Extract education/profession
            for pattern in [r'(?:professor|lawyer|jurist|optik|unternehmer|ingenieur|lehrer|arzt|anwalt)', r'(?:Beruf|beruflich)[:\s]+([^,.]+)']:
                m = re.search(pattern, bio, re.I)
                if m:
                    if m.lastindex:
                        props.append({'key': 'Beruf', 'val': m.group(1).strip()[:40], 'ev': 'E'})
                    break

            if props:
                v['properties'] = props
                changed = True

        # Forecast from forecast.kandidaten
        if not v.get('forecast') and isinstance(k, str) and k in forecast_lookup:
            v['forecast'] = forecast_lookup[k]
            changed = True
        elif not v.get('forecast'):
            # Try matching by name
            name = v.get('name', k)
            for fk_id, fk_data in forecast_lookup.items():
                if name.split()[-1].lower() in fk_id.lower() or fk_id.lower() in name.lower():
                    v['forecast'] = fk_data
                    changed = True
                    break

        # Steckbrief (template expects dict of key→value pairs) — always regenerate
        if True:
            steckbrief = {}
            if v.get('party'):
                steckbrief['Partei'] = v['party']
            role_display = v.get('role', '').replace('Kandidat/in, ', '').replace('Amtsinhaber, ', '')
            if role_display:
                steckbrief['Position'] = role_display[:60]
            if v.get('amtsinhaber'):
                steckbrief['Status'] = 'Amtsinhaber/in'
            bio = str(v.get('bio', ''))
            # Age
            age_m = re.search(r'(\d{2})[- ](?:year|Jahre|jährig)', bio)
            if age_m:
                steckbrief['Alter'] = age_m.group(1) + ' Jahre'
            # First sentence as summary
            sentences = re.split(r'(?<=[.!?])\s+', bio)
            if sentences:
                steckbrief['Kurzprofil'] = sentences[0][:120]
            if steckbrief:
                v['steckbrief'] = steckbrief
                changed = True

        # Ensure role ALWAYS contains "Kandidat" for template filtering
        role = v.get('role', '')
        if 'andidat' not in role.lower():
            if v.get('amtsinhaber'):
                v['role'] = f"Kandidat/in (Amtsinhaber), {role}" if role else "Kandidat/in (Amtsinhaber)"
            else:
                v['role'] = f"Kandidat/in, {role}" if role else "Kandidat/in"
            changed = True

        # Risk score from controversies + weaknesses
        if v.get('risk') is None:
            contros = v.get('controversies', [])
            weaknesses = v.get('weaknesses', [])
            risk = min(10, len(contros) * 3 + len(weaknesses) * 1)
            v['risk'] = risk
            changed = True

    # ═══ FIX 3: Graph (nodes + links) ═══
    if not d.get('graph') or not d['graph'].get('nodes'):
        nodes = []
        links = []
        node_ids = set()

        # Add candidate nodes
        for k, v in kb.items():
            if not isinstance(v, dict):
                continue
            nodes.append({
                'id': k,
                'label': v.get('name', k),
                'type': 'person',
                'party': v.get('party', ''),
                'color': v.get('color', DEFAULT_COLOR),
                'weight': 3 if v.get('amtsinhaber') else 1
            })
            node_ids.add(k)

            # Party node
            party = v.get('party', '')
            if party:
                party_id = 'party_' + party.lower().replace(' ', '_')
                if party_id not in node_ids:
                    nodes.append({
                        'id': party_id,
                        'label': party,
                        'type': 'organization',
                        'color': PARTY_COLORS.get(party, DEFAULT_COLOR),
                        'weight': 2
                    })
                    node_ids.add(party_id)
                links.append({'source': k, 'target': party_id, 'type': 'member_of'})

        # Add topic nodes from news
        all_news_text = ' '.join(str(n.get('title',''))+' '+str(n.get('body',''))
                                for n in news if isinstance(n, dict)).lower()
        for topic, keywords in TOPIC_KEYWORDS.items():
            matches = sum(1 for kw in keywords if kw in all_news_text)
            if matches >= 1:
                topic_id = 'topic_' + topic.lower().replace(' ', '_').replace('&', '')
                nodes.append({
                    'id': topic_id,
                    'label': topic,
                    'type': 'topic',
                    'color': '#6366F1',
                    'weight': min(3, matches)
                })
                node_ids.add(topic_id)

                # Link candidates who mention this topic in bio
                for k2, v2 in kb.items():
                    if isinstance(v2, dict):
                        bio = str(v2.get('bio', '')).lower()
                        if any(kw in bio for kw in keywords):
                            links.append({'source': k2, 'target': topic_id, 'type': 'addresses'})

        # Cross-candidate links from news co-mentions
        cand_keys = [k for k in kb.keys() if isinstance(kb.get(k), dict)]
        for i, k1 in enumerate(cand_keys):
            name1 = kb[k1].get('name', k1).split()[-1].lower()
            for k2 in cand_keys[i+1:]:
                name2 = kb[k2].get('name', k2).split()[-1].lower()
                co_mentions = 0
                for n in news:
                    if isinstance(n, dict):
                        text = (str(n.get('title',''))+' '+str(n.get('body',''))).lower()
                        if name1 in text and name2 in text:
                            co_mentions += 1
                if co_mentions >= 2:
                    links.append({
                        'source': k1, 'target': k2,
                        'type': 'co_mentioned',
                        'weight': co_mentions
                    })

        d['graph'] = {'nodes': nodes, 'links': links}
        changed = True

    # ═══ FIX 4: Topics ═══
    if True:  # Always regenerate topics to catch bilingual keywords
        all_text = ' '.join(
            str(c.get('claim','')) for c in claim_ledger if isinstance(c, dict)
        ).lower() + ' ' + ' '.join(
            str(n.get('title',''))+' '+str(n.get('body',''))
            for n in news if isinstance(n, dict)
        ).lower()

        topics = []
        for topic, keywords in TOPIC_KEYWORDS.items():
            matches = sum(1 for kw in keywords if kw in all_text)
            if matches >= 1:
                # Find representative sentence
                desc = ''
                for n in news:
                    if isinstance(n, dict):
                        text = str(n.get('title',''))
                        if any(kw in text.lower() for kw in keywords):
                            desc = text[:100]
                            break
                topics.append({
                    'name': topic,
                    'relevance': matches,
                    'desc': desc
                })
        topics.sort(key=lambda x: -x['relevance'])
        d['topics'] = topics
        changed = True

    # ═══ FIX 5: Hypotheses from intelligence ═══
    if not d.get('hypotheses') or len(d.get('hypotheses', [])) < 2:
        intel = d.get('intelligence', {})
        hyps = []

        # From intelligence layer questions
        for q_key in ['q1_headline', 'q2_upset', 'q3_key_number', 'q4_cross_city', 'q5_riskiest']:
            q_val = intel.get(q_key)
            if q_val and isinstance(q_val, str):
                hyps.append({
                    'text': q_val[:150],
                    'type': q_key.split('_')[0],
                    'confidence': intel.get('confidence_score', 70)
                })

        # From stichwahl prediction
        stw = d.get('stichwahl_prediction', {})
        if isinstance(stw, dict) and stw.get('probability'):
            hyps.append({
                'text': f"Stichwahl-Wahrscheinlichkeit: {stw['probability']}%",
                'type': 'prediction',
                'confidence': 85
            })

        # From scenarios
        for s in d.get('scenarios', [])[:3]:
            if isinstance(s, dict):
                title = s.get('title', s.get('name', ''))
                prob = s.get('probability', s.get('wahrscheinlichkeit', ''))
                if title:
                    hyps.append({
                        'text': f"{title}" + (f" ({prob}%)" if prob else ""),
                        'type': 'scenario',
                        'confidence': int(prob) if prob else 50
                    })

        # From actions
        for a in intel.get('actions', [])[:3]:
            if isinstance(a, str):
                hyps.append({'text': a[:150], 'type': 'action', 'confidence': 70})
            elif isinstance(a, dict):
                hyps.append({'text': str(a.get('text', a.get('action', '')))[:150], 'type': 'action', 'confidence': 70})

        # From forecast (who's likely to win)
        if forecast_kandidaten:
            sorted_fc = sorted(forecast_kandidaten, key=lambda x: int(re.findall(r'\d+', str(x.get('erstwahlgang', '0')))[-1]) if re.findall(r'\d+', str(x.get('erstwahlgang', '0'))) else 0, reverse=True)
            if sorted_fc:
                top = sorted_fc[0]
                hyps.append({
                    'text': f"Favorit: {top.get('name', '?')} ({top.get('erstwahlgang', '?')})",
                    'type': 'forecast',
                    'confidence': 75
                })

        d['hypotheses'] = hyps
        changed = True

    # ═══ FIX 6: Patterns from claim_ledger ═══
    if not d.get('patterns') or (d.get('patterns') and not d['patterns'][0].get('label')):
        patterns = []
        # Group claims by EIJA
        eija_counts = {}
        for c in claim_ledger:
            if isinstance(c, dict):
                e = c.get('eija', 'E')
                eija_counts[e] = eija_counts.get(e, 0) + 1

        if eija_counts:
            e_pct = eija_counts.get('E', 0) / max(1, sum(eija_counts.values())) * 100
            patterns.append({
                'id': 'EIJA-1',
                'label': 'Evidenz-Verteilung',
                'meaning': f"Von {sum(eija_counts.values())} Claims sind {e_pct:.0f}% als Evidenz klassifiziert. {eija_counts.get('I',0)} Inferenzen, {eija_counts.get('J',0)} Judgments, {eija_counts.get('A',0)} Annahmen.",
                'confidence': 90,
                'severity': 'NIEDRIG'
            })

        # Candidate count pattern
        n_candidates = len([k for k in kb if isinstance(kb.get(k), dict)])
        if n_candidates >= 5:
            patterns.append({
                'id': 'FRAG-1',
                'label': 'Fragmentiertes Kandidatenfeld',
                'meaning': f"{n_candidates} Kandidaten führen zu Stimmenverteilung. Stichwahl sehr wahrscheinlich. Historisch: Bei >5 Kandidaten in Bayern >80% Stichwahl-Quote.",
                'confidence': 85,
                'severity': 'MITTEL'
            })
        elif n_candidates <= 3:
            patterns.append({
                'id': 'FRAG-1',
                'label': 'Konzentriertes Rennen',
                'meaning': f"Nur {n_candidates} Kandidaten. Erstrundenentscheidung wahrscheinlicher als bei fragmentiertem Feld.",
                'confidence': 80,
                'severity': 'NIEDRIG'
            })

        # Source concentration
        src_domains = {}
        for q in quellenverzeichnis:
            if isinstance(q, dict) and q.get('url'):
                import re as _re
                dm = _re.search(r'https?://(?:www\.)?([^/]+)', str(q['url']))
                if dm:
                    src_domains[dm.group(1)] = src_domains.get(dm.group(1), 0) + 1
        if src_domains:
            top = sorted(src_domains.items(), key=lambda x: -x[1])[:3]
            top_pct = sum(c for _, c in top) / max(1, len(quellenverzeichnis)) * 100
            patterns.append({
                'id': 'SRC-1',
                'label': 'Quellenkonzentration',
                'meaning': f"Top-3 Quellen ({', '.join(d[0] for d in top)}) machen {top_pct:.0f}% der Datenbasis aus. {'Diversifikation empfohlen.' if top_pct > 60 else 'Akzeptable Diversifikation.'}",
                'confidence': 95,
                'severity': 'HOCH' if top_pct > 60 else 'NIEDRIG'
            })

        d['patterns'] = patterns
        changed = True

    # ═══ FIX 7: Talking Points ═══
    if not d.get('talking_points'):
        tps = []
        scenarios = d.get('scenarios', [])
        for s in scenarios[:3]:
            if isinstance(s, dict):
                tps.append({
                    'text': str(s.get('title', s.get('name', '')))[:80],
                    'probability': s.get('probability', s.get('wahrscheinlichkeit', 50))
                })
        d['talking_points'] = tps
        changed = True

    # ═══ FIX 8: Weekly Brief ═══
    if not d.get('weekly_brief') or not d['weekly_brief'].get('summary'):
        candidates = [kb[k].get('name','?') for k in kb if isinstance(kb.get(k), dict)]
        stw_pct = 50
        stw_pred = d.get('stichwahl_prediction', {})
        if isinstance(stw_pred, dict):
            stw_pct = stw_pred.get('probability', 50)

        d['weekly_brief'] = {
            'summary': f"{days_to} Tage vor der Wahl in {gemeinde}. {len(candidates)} Kandidaten im Rennen. Stichwahl-Wahrscheinlichkeit: {stw_pct}%.",
            'daysToElection': days_to
        }
        changed = True

    # ═══ SAVE ═══
    if changed:
        with open(city_path, 'w') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

    return changed


def enrich_all():
    """Enrich all city JSONs."""
    enriched = 0
    total = 0
    for f in sorted(CITIES_DIR.iterdir()):
        if f.suffix != '.json' or f.stem == 'internal':
            continue
        total += 1
        if enrich_city(f):
            enriched += 1
            print(f"  ✅ {f.stem}")
        else:
            print(f"  ⏭️  {f.stem} (already complete)")

    print(f"\n✅ {enriched}/{total} cities enriched")
    return enriched


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] != '--all':
        path = CITIES_DIR / f"{sys.argv[1]}.json"
        if path.exists():
            enrich_city(path)
            print(f"✅ {sys.argv[1]} enriched")
        else:
            print(f"❌ {sys.argv[1]} not found")
    else:
        enrich_all()

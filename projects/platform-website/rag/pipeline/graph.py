#!/usr/bin/env python3
"""
Entity Resolution & Relationship Graph

Builds a knowledge graph from all 50 dossiers:
- Kandidat → Partei → Stadt → Region
- Kandidat → Thema (extracted from bio + news)
- Stadt → Thema (extracted from news)
- Partei → Koalition (from Stadtrat data)

No external dependencies (no Neo4j). Uses in-memory graph with JSON export.
Designed for cross-city queries like:
- "Welche CSU-Kandidaten haben Infrastruktur als Thema?"
- "In welchen Städten ist die Verkehrswende ein Wahlkampfthema?"
- "Welche Koalitionsmuster gibt es?"
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"

# ── THEMATIC TAXONOMY ──

TOPIC_KEYWORDS = {
    'Wohnen/Miete': ['wohnung', 'miete', 'mietpreis', 'bauland', 'sozialwohnung', 'wohnraum', 'wohnungsbau', 'bezahlbar'],
    'Verkehr/Mobilität': ['verkehr', 'radweg', 'stadtbahn', 'tram', 'bus', 'fahrrad', 'mobilität', 'stau', 'umgehung', 'parkplatz', 'stub'],
    'Klimaschutz/Energie': ['klima', 'energie', 'solar', 'photovoltaik', 'co2', 'nachhaltigkeit', 'windkraft', 'fernwärme', 'klimaschutz'],
    'Digitalisierung': ['digital', 'breitband', 'glasfaser', 'smart city', 'e-government', 'online', 'it-'],
    'Wirtschaft/Arbeitsplätze': ['wirtschaft', 'arbeitsplatz', 'gewerbe', 'ansiedlung', 'fachkräfte', 'startup', 'gründer', 'arbeitsmarkt'],
    'Bildung/Kita': ['schule', 'kita', 'bildung', 'kindergarten', 'ganztag', 'hochschule', 'universität', 'betreuung'],
    'Sicherheit': ['sicherheit', 'kriminalität', 'polizei', 'ordnung', 'vandalismus'],
    'Integration/Soziales': ['integration', 'migration', 'flüchtling', 'asyl', 'sozial', 'inklusion', 'armut', 'obdachlos'],
    'Finanzen/Haushalt': ['haushalt', 'schulden', 'finanzen', 'steuer', 'sparen', 'investition', 'konsolidierung', 'defizit'],
    'Kultur/Freizeit': ['kultur', 'museum', 'theater', 'sport', 'verein', 'schwimmbad', 'bibliothek', 'festival'],
    'Stadtentwicklung': ['innenstadt', 'städtebau', 'leerstand', 'einzelhandel', 'attraktivität', 'quartier', 'sanierung'],
    'Gesundheit': ['krankenhaus', 'klinik', 'arzt', 'gesundheit', 'pflege', 'ärzte'],
}


class EntityGraph:
    """In-memory knowledge graph for cross-city intelligence."""

    def __init__(self):
        self.nodes = {}     # id → {type, properties}
        self.edges = []     # [{source, target, type, properties}]
        self._index = defaultdict(set)  # type → set of node ids

    def add_node(self, node_id: str, node_type: str, **props):
        self.nodes[node_id] = {'type': node_type, **props}
        self._index[node_type].add(node_id)

    def add_edge(self, source: str, target: str, edge_type: str, **props):
        self.edges.append({
            'source': source,
            'target': target,
            'type': edge_type,
            **props
        })

    def get_nodes(self, node_type: str) -> List[Dict]:
        return [{'id': nid, **self.nodes[nid]}
                for nid in self._index.get(node_type, set())]

    def get_neighbors(self, node_id: str, edge_type: str = None) -> List[Dict]:
        neighbors = []
        for e in self.edges:
            if e['source'] == node_id:
                if edge_type is None or e['type'] == edge_type:
                    neighbors.append({'node': e['target'], 'edge': e})
            elif e['target'] == node_id:
                if edge_type is None or e['type'] == edge_type:
                    neighbors.append({'node': e['source'], 'edge': e})
        return neighbors

    def query(self, question: str) -> List[Dict]:
        """Answer a natural-language question against the graph."""
        q = question.lower()
        results = []

        # Pattern: "Welche [Party] Kandidaten ..."
        party_match = re.search(r'(csu|spd|grüne?|afd|fdp|freie wähler|linke)', q)
        topic_match = None
        for topic, keywords in TOPIC_KEYWORDS.items():
            if any(kw in q for kw in keywords):
                topic_match = topic
                break

        if party_match and topic_match:
            party = party_match.group(1).upper()
            # Find candidates of party with topic
            for e in self.edges:
                if e['type'] == 'BELONGS_TO' and party.lower() in self.nodes.get(e['target'], {}).get('name', '').lower():
                    cand_id = e['source']
                    # Check if candidate has topic
                    for e2 in self.edges:
                        if e2['source'] == cand_id and e2['type'] == 'ADDRESSES_TOPIC' and e2['target'] == f'topic:{topic_match}':
                            results.append({
                                'candidate': self.nodes[cand_id].get('name'),
                                'city': self.nodes[cand_id].get('city'),
                                'party': party,
                                'topic': topic_match
                            })

        elif topic_match:
            # Which cities have this topic?
            for e in self.edges:
                if e['type'] == 'HAS_TOPIC' and e['target'] == f'topic:{topic_match}':
                    city_node = self.nodes.get(e['source'], {})
                    results.append({
                        'city': city_node.get('name'),
                        'topic': topic_match,
                        'relevance': e.get('relevance', 0)
                    })
            results.sort(key=lambda x: -x.get('relevance', 0))

        elif party_match:
            party = party_match.group(1)
            for e in self.edges:
                if e['type'] == 'BELONGS_TO':
                    party_node = self.nodes.get(e['target'], {})
                    if party.lower() in party_node.get('name', '').lower():
                        cand = self.nodes.get(e['source'], {})
                        results.append({
                            'candidate': cand.get('name'),
                            'city': cand.get('city'),
                            'party': party_node.get('name'),
                            'amtsinhaber': cand.get('amtsinhaber', False)
                        })

        return results

    def build_from_dossiers(self):
        """Build graph from all city JSON files."""
        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            with open(f) as fh:
                try:
                    d = json.load(fh)
                except:
                    continue

            slug = f.stem
            tenant = d.get('tenant', {})
            gemeinde = tenant.get('gemeinde', slug) if isinstance(tenant, dict) else slug
            typ = tenant.get('typ', '?') if isinstance(tenant, dict) else '?'

            # ── City node ──
            city_id = f'city:{slug}'
            self.add_node(city_id, 'City', name=gemeinde, typ=typ, slug=slug)

            # ── Region node ──
            region = tenant.get('region', '') if isinstance(tenant, dict) else ''
            if region:
                region_id = f'region:{region.lower().replace(" ", "-")}'
                self.add_node(region_id, 'Region', name=region)
                self.add_edge(city_id, region_id, 'IN_REGION')

            # ── Candidates + Parties ──
            kb = d.get('kb', {})
            if not isinstance(kb, dict):
                continue

            for k, v in kb.items():
                if not isinstance(v, dict):
                    continue

                name = v.get('name', k)
                party = v.get('party', '?')
                cand_id = f'cand:{slug}:{k}'

                self.add_node(cand_id, 'Candidate',
                             name=name, party=party, city=gemeinde,
                             amtsinhaber=v.get('amtsinhaber', False),
                             role=v.get('role', ''))

                self.add_edge(cand_id, city_id, 'RUNS_IN')

                # Party edge
                if party and party != '?':
                    party_id = f'party:{party.lower().replace(" ", "-")}'
                    self.add_node(party_id, 'Party', name=party)
                    self.add_edge(cand_id, party_id, 'BELONGS_TO')

                # Topic extraction from bio
                bio = str(v.get('bio', '')).lower()
                for topic, keywords in TOPIC_KEYWORDS.items():
                    topic_id = f'topic:{topic}'
                    matches = sum(1 for kw in keywords if kw in bio)
                    if matches >= 2:
                        self.add_node(topic_id, 'Topic', name=topic)
                        self.add_edge(cand_id, topic_id, 'ADDRESSES_TOPIC',
                                     relevance=matches)

            # ── City topics from news ──
            news_text = ''
            for item in d.get('news', []):
                if isinstance(item, dict):
                    news_text += ' ' + str(item.get('title', ''))
                    news_text += ' ' + str(item.get('body', ''))
            news_text = news_text.lower()

            for topic, keywords in TOPIC_KEYWORDS.items():
                topic_id = f'topic:{topic}'
                matches = sum(1 for kw in keywords if kw in news_text)
                if matches >= 3:
                    self.add_node(topic_id, 'Topic', name=topic)
                    self.add_edge(city_id, topic_id, 'HAS_TOPIC',
                                 relevance=matches)

    def stats(self) -> Dict:
        """Graph statistics."""
        type_counts = Counter(n['type'] for n in self.nodes.values())
        edge_type_counts = Counter(e['type'] for e in self.edges)

        return {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'node_types': dict(type_counts),
            'edge_types': dict(edge_type_counts),
        }

    def export(self, path: str = None) -> Dict:
        """Export graph as JSON."""
        data = {
            'nodes': [{'id': k, **v} for k, v in self.nodes.items()],
            'edges': self.edges,
            'stats': self.stats()
        }
        if path:
            with open(path, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        return data

    # ── CROSS-CITY ANALYSIS ──

    def party_strongholds(self) -> Dict:
        """Which parties dominate which cities?"""
        party_cities = defaultdict(list)
        for e in self.edges:
            if e['type'] == 'BELONGS_TO':
                cand = self.nodes.get(e['source'], {})
                party = self.nodes.get(e['target'], {}).get('name', '?')
                if cand.get('amtsinhaber'):
                    party_cities[party].append(cand.get('city'))
        return dict(party_cities)

    def topic_heatmap(self) -> Dict:
        """Which topics are hottest across cities?"""
        topic_counts = Counter()
        topic_cities = defaultdict(list)
        for e in self.edges:
            if e['type'] == 'HAS_TOPIC':
                topic = self.nodes.get(e['target'], {}).get('name', '?')
                city = self.nodes.get(e['source'], {}).get('name', '?')
                topic_counts[topic] += e.get('relevance', 1)
                topic_cities[topic].append(city)
        return {
            'ranking': dict(topic_counts.most_common()),
            'cities': {t: cities for t, cities in topic_cities.items()}
        }

    def generationswechsel(self) -> List[Dict]:
        """Cities where incumbent is not running again."""
        results = []
        for e in self.edges:
            if e['type'] == 'RUNS_IN':
                cand = self.nodes.get(e['source'], {})
                if cand.get('amtsinhaber') and 'tritt nicht' in str(cand.get('role', '')).lower():
                    results.append({
                        'city': cand.get('city'),
                        'incumbent': cand.get('name'),
                        'party': cand.get('party')
                    })
        return results


if __name__ == '__main__':
    import sys
    g = EntityGraph()
    g.build_from_dossiers()

    if len(sys.argv) > 1 and sys.argv[1] == '--export':
        out = str(CITIES_DIR.parent / 'entity-graph.json')
        g.export(out)
        print(f"✅ Graph exported to {out}")

    elif len(sys.argv) > 1 and sys.argv[1] == '--query':
        query = ' '.join(sys.argv[2:])
        results = g.query(query)
        print(json.dumps(results, indent=2, ensure_ascii=False))

    else:
        stats = g.stats()
        print(f"{'='*60}")
        print(f"ENTITY GRAPH")
        print(f"{'='*60}")
        print(f"  Nodes: {stats['total_nodes']}")
        print(f"  Edges: {stats['total_edges']}")
        print(f"\n  Node Types: {stats['node_types']}")
        print(f"  Edge Types: {stats['edge_types']}")

        print(f"\n  ## Party Strongholds (Amtsinhaber)")
        for party, cities in sorted(g.party_strongholds().items(),
                                    key=lambda x: -len(x[1])):
            print(f"    {party}: {', '.join(cities[:5])}")

        print(f"\n  ## Topic Heatmap")
        heatmap = g.topic_heatmap()
        for topic, score in list(heatmap['ranking'].items())[:10]:
            cities = heatmap['cities'][topic][:3]
            bar = '█' * min(30, score)
            print(f"    {topic:<25} {score:>4} {bar} ({', '.join(cities)})")

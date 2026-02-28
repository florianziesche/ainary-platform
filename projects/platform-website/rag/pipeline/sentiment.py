#!/usr/bin/env python3
"""
Sentiment Analysis Pipeline

Scores each news item per candidate as positive/negative/neutral.
No external API needed — rule-based German sentiment with domain-specific terms.

Output: sentiment_score per candidate per city (-1.0 to +1.0)
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

CITIES_DIR = Path(__file__).parent.parent.parent / "data" / "cities"

# ── SENTIMENT LEXICON (German, politics-specific) ──

POSITIVE = {
    # Strong positive
    'gewonnen': 1.0, 'sieg': 1.0, 'gewählt': 0.8, 'mehrheit': 0.7,
    'unterstützung': 0.7, 'beliebt': 0.8, 'erfolgreich': 0.8,
    'zuspruch': 0.7, 'zustimmung': 0.7, 'bestätigt': 0.5,
    'einigkeit': 0.6, 'aufbruch': 0.6, 'innovation': 0.5,
    'investition': 0.5, 'wachstum': 0.5, 'zukunft': 0.4,
    'verbesserung': 0.5, 'fortschritt': 0.5, 'engagement': 0.5,
    'kompetenz': 0.5, 'erfahrung': 0.4, 'transparent': 0.4,
    'bürgernähe': 0.5, 'dialogbereit': 0.4, 'souverän': 0.5,
    # Moderate positive
    'stärkt': 0.4, 'fördert': 0.4, 'verbessert': 0.4,
    'einstimmig': 0.6, 'parteiübergreifend': 0.4,
}

NEGATIVE = {
    # Strong negative
    'skandal': -1.0, 'vorstrafe': -1.0, 'rücktritt': -0.9,
    'korruption': -1.0, 'betrug': -1.0, 'versagen': -0.8,
    'schulden': -0.6, 'defizit': -0.5, 'krise': -0.6,
    'streit': -0.5, 'konflikt': -0.4, 'kritik': -0.4,
    'gescheitert': -0.7, 'verloren': -0.6, 'niederlage': -0.7,
    'umstritten': -0.5, 'kontrovers': -0.4, 'spaltet': -0.5,
    'kostenexplosion': -0.7, 'verzögerung': -0.4, 'stau': -0.3,
    'protest': -0.5, 'ablehnung': -0.5, 'widerstand': -0.4,
    'distanziert': -0.5, 'rüge': -0.6, 'misstrauen': -0.6,
    # Moderate negative
    'probleme': -0.3, 'herausforderung': -0.2, 'schwierig': -0.3,
    'belastet': -0.4, 'verfehlt': -0.5, 'stagnation': -0.4,
}

NEGATION_WORDS = ['nicht', 'kein', 'keine', 'keinen', 'ohne', 'nie', 'niemals']


class SentimentAnalyzer:
    """Rule-based German political sentiment analysis."""

    def score_text(self, text: str) -> float:
        """Score a text from -1.0 (very negative) to +1.0 (very positive)."""
        words = text.lower().split()
        score = 0.0
        word_count = 0

        for i, word in enumerate(words):
            # Clean punctuation
            clean = re.sub(r'[^a-zäöüß]', '', word)
            if not clean:
                continue

            # Check for negation in previous 2 words
            negated = any(words[max(0, i-2):i].__contains__(neg)
                        for neg in NEGATION_WORDS)

            if clean in POSITIVE:
                s = POSITIVE[clean]
                score += -s * 0.5 if negated else s  # Negation flips but weakens
                word_count += 1
            elif clean in NEGATIVE:
                s = NEGATIVE[clean]
                score += -s * 0.5 if negated else s
                word_count += 1

        # Normalize
        if word_count > 0:
            return max(-1.0, min(1.0, score / max(1, word_count ** 0.5)))
        return 0.0

    def analyze_city(self, city_slug: str) -> Dict:
        """Analyze sentiment for all candidates in a city."""
        city_path = CITIES_DIR / f"{city_slug}.json"
        if not city_path.exists():
            return {'error': f'{city_slug} not found'}

        with open(city_path) as f:
            d = json.load(f)

        kb = d.get('kb', {})
        if not isinstance(kb, dict):
            return {'error': 'no kb'}

        candidate_names = {}
        for k, v in kb.items():
            if isinstance(v, dict):
                name = v.get('name', '')
                if name:
                    # Store both full name and last name for matching
                    parts = name.split()
                    candidate_names[name] = {
                        'party': v.get('party', '?'),
                        'full': name,
                        'last': parts[-1] if parts else name,
                        'scores': [],
                        'positive_news': [],
                        'negative_news': [],
                    }

        # Score each news item
        news = d.get('news', [])
        if not isinstance(news, list):
            return {'error': 'news not array'}

        for item in news:
            if not isinstance(item, dict):
                continue
            title = str(item.get('title', ''))
            body = str(item.get('body', ''))
            text = f"{title} {body}"
            date = item.get('date', '?')
            weight = item.get('temporal_weight', 1.0)

            overall_score = self.score_text(text)

            # Attribute to candidates mentioned
            for name, data in candidate_names.items():
                if data['last'] in text or data['full'] in text:
                    weighted_score = overall_score * weight
                    data['scores'].append(weighted_score)
                    if weighted_score > 0.1:
                        data['positive_news'].append({
                            'title': title[:60],
                            'score': round(weighted_score, 2),
                            'date': date
                        })
                    elif weighted_score < -0.1:
                        data['negative_news'].append({
                            'title': title[:60],
                            'score': round(weighted_score, 2),
                            'date': date
                        })

        # Compute final scores
        results = {}
        for name, data in candidate_names.items():
            scores = data['scores']
            avg_score = sum(scores) / len(scores) if scores else 0.0
            results[name] = {
                'party': data['party'],
                'sentiment_score': round(avg_score, 3),
                'news_mentions': len(scores),
                'positive_count': len(data['positive_news']),
                'negative_count': len(data['negative_news']),
                'top_positive': data['positive_news'][:3],
                'top_negative': data['negative_news'][:3],
            }

        # Sort by sentiment
        sorted_results = dict(sorted(results.items(),
                                    key=lambda x: -x[1]['sentiment_score']))

        return {
            'city': city_slug,
            'gemeinde': d.get('tenant', {}).get('gemeinde', city_slug) if isinstance(d.get('tenant'), dict) else city_slug,
            'total_news': len(news),
            'candidates': sorted_results
        }

    def analyze_all(self, apply=False) -> Dict:
        """Analyze all cities. If apply=True, write sentiment to JSON."""
        all_results = {}

        for f in sorted(CITIES_DIR.iterdir()):
            if f.suffix != '.json' or f.stem == 'internal':
                continue
            result = self.analyze_city(f.stem)
            if 'error' in result:
                continue
            all_results[f.stem] = result

            if apply and result.get('candidates'):
                with open(f) as fh:
                    d = json.load(fh)

                intel = d.get('intelligence', {})
                intel['sentiment'] = {
                    name: {
                        'score': data['sentiment_score'],
                        'mentions': data['news_mentions'],
                        'positive': data['positive_count'],
                        'negative': data['negative_count']
                    }
                    for name, data in result['candidates'].items()
                }
                d['intelligence'] = intel

                with open(f, 'w') as fh:
                    json.dump(d, fh, indent=2, ensure_ascii=False)

        return all_results


if __name__ == '__main__':
    import sys
    sa = SentimentAnalyzer()

    if len(sys.argv) > 1 and sys.argv[1] == '--apply':
        results = sa.analyze_all(apply=True)
        print(f"✅ Sentiment applied to {len(results)} cities")
    elif len(sys.argv) > 1:
        result = sa.analyze_city(sys.argv[1])
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        results = sa.analyze_all()
        # Summary
        print(f"{'City':<20} {'Candidate':<25} {'Sentiment':>9} {'Mentions':>8}")
        print("-" * 65)
        for slug, r in results.items():
            for name, data in r['candidates'].items():
                if data['news_mentions'] > 0:
                    emoji = '🟢' if data['sentiment_score'] > 0.1 else '🔴' if data['sentiment_score'] < -0.1 else '⚪'
                    print(f"  {r['gemeinde'][:18]:<20} {name[:23]:<25} {emoji}{data['sentiment_score']:>7.3f} {data['news_mentions']:>6}")

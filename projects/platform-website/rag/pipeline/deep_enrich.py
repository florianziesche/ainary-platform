#!/usr/bin/env python3
"""
Deep Enrichment Pipeline — 2-3x more sources, social media, real bios.

PURPOSE:
  Takes an existing city JSON and ENRICHES it with:
  1. Web research: candidate bios, karriere, positions (web_search + web_fetch)
  2. X/Twitter: candidate accounts, local media, city accounts
  3. Local sources: Rathaus, Wahlamt, party websites
  4. Sentiment from social media posts
  
  Goal: Transform a 42-source dossier into a 100+ source dossier
  with real biographical data, social media insights, and diverse sourcing.

USAGE:
  python3 -m pipeline.deep_enrich --city bamberg
  python3 -m pipeline.deep_enrich --city bamberg --dry-run
  python3 -m pipeline.deep_enrich --city bamberg --x-only
  python3 -m pipeline.deep_enrich --all

REQUIREMENTS:
  - xurl CLI for X/Twitter search
  - Internet access for web_search/web_fetch
  
OUTPUT:
  Updates city JSON in-place with:
  - New news entries (tagged source: "deep_enrich")
  - Updated kb[].bio, kb[].karriere, kb[].properties
  - New quellen entries with trust scores
  - Social media sentiment scores
  - Before/after comparison printed to stdout
"""

import json, os, re, sys, subprocess, time
from pathlib import Path
from datetime import datetime

CITIES_DIR = Path(__file__).parent.parent.parent / 'data' / 'cities'

# ── Web Search via brave API (subprocess to avoid dependency) ──
def web_search(query, count=5):
    """Search web via brave CLI. Returns list of {title, url, snippet}."""
    import urllib.request, urllib.parse
    
    api_key = os.environ.get('BRAVE_API_KEY', '')
    if not api_key:
        # Try to get from openclaw config
        try:
            result = subprocess.run(['printenv', 'BRAVE_API_KEY'], capture_output=True, text=True)
            api_key = result.stdout.strip()
        except:
            pass
    
    if not api_key:
        # Fallback: use subprocess to call the brave search through openclaw
        return _web_search_fallback(query, count)
    
    url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={count}"
    req = urllib.request.Request(url, headers={
        'Accept': 'application/json',
        'X-Subscription-Token': api_key
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            results = []
            for r in data.get('web', {}).get('results', []):
                results.append({
                    'title': r.get('title', ''),
                    'url': r.get('url', ''),
                    'snippet': r.get('description', '')
                })
            return results
    except Exception as e:
        print(f"  ⚠️ Web search failed: {e}")
        return []


def _web_search_fallback(query, count=5):
    """Fallback: use node script for brave search."""
    # Write a temp script
    script = f"""
    const https = require('https');
    const q = encodeURIComponent({json.dumps(query)});
    const url = `https://api.search.brave.com/res/v1/web/search?q=${{q}}&count={count}`;
    https.get(url, {{headers: {{'Accept': 'application/json', 'X-Subscription-Token': process.env.BRAVE_API_KEY}}}}, res => {{
        let d = '';
        res.on('data', c => d += c);
        res.on('end', () => {{
            try {{
                const j = JSON.parse(d);
                const results = (j.web?.results || []).map(r => ({{title: r.title, url: r.url, snippet: r.description}}));
                console.log(JSON.stringify(results));
            }} catch(e) {{ console.log('[]'); }}
        }});
    }}).on('error', () => console.log('[]'));
    """
    try:
        result = subprocess.run(['node', '-e', script], capture_output=True, text=True, timeout=15,
                              env={**os.environ})
        return json.loads(result.stdout.strip() or '[]')
    except:
        return []


def web_fetch(url, max_chars=3000):
    """Fetch a URL and extract text content."""
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Basic HTML to text
            text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
            text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:max_chars]
    except Exception as e:
        return ''


def x_search(query, max_results=10):
    """Search X/Twitter via xurl CLI. Returns list of tweets."""
    try:
        result = subprocess.run(
            ['xurl', 'search', query, '-n', str(max_results)],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(result.stdout)
        tweets = []
        for t in data.get('data', []):
            tweets.append({
                'text': t.get('text', ''),
                'created_at': t.get('created_at', ''),
                'author_id': t.get('author_id', ''),
                'id': t.get('id', ''),
                'metrics': t.get('public_metrics', {})
            })
        return tweets
    except Exception as e:
        print(f"  ⚠️ X search failed for '{query}': {e}")
        return []


def x_user_lookup(username):
    """Look up X user by username. Returns user data or None."""
    try:
        result = subprocess.run(
            ['xurl', 'user', username],
            capture_output=True, text=True, timeout=10
        )
        data = json.loads(result.stdout)
        return data.get('data')
    except:
        return None


def extract_bio_from_text(text, name):
    """Extract biographical information from web page text."""
    bio_parts = []
    
    # Look for sentences containing the person's name
    lastname = name.split()[-1] if name.split() else name
    sentences = re.split(r'[.!?]\s+', text)
    relevant = [s.strip() for s in sentences if lastname.lower() in s.lower() and len(s) > 30]
    
    # Take top 5 most informative sentences
    scored = []
    bio_keywords = ['geboren', 'jahrgang', 'studiert', 'beruf', 'partei', 'mitglied', 
                    'bürgermeister', 'stadtrat', 'gewählt', 'kandidat', 'verheiratet',
                    'kinder', 'lebt', 'seit', 'born', 'elected', 'member', 'council']
    for s in relevant:
        score = sum(1 for kw in bio_keywords if kw in s.lower())
        scored.append((score, s))
    
    scored.sort(key=lambda x: -x[0])
    bio_parts = [s for _, s in scored[:5]]
    
    return '. '.join(bio_parts) + '.' if bio_parts else ''


def extract_karriere_from_text(text, name):
    """Extract career timeline from web page text."""
    karriere = []
    lastname = name.split()[-1] if name.split() else name
    
    # Find year + context patterns
    year_patterns = re.findall(
        r'(?:seit|ab|von|im|in|year)?\s*(\d{4})\s*[-–:]?\s*([^.]{10,80})',
        text, re.IGNORECASE
    )
    
    for year_str, context in year_patterns:
        year = int(year_str)
        if 1980 <= year <= 2026 and lastname.lower() in context.lower():
            karriere.append({
                'year': str(year),
                'label': context.strip()[:80],
                'color': 'var(--blue)'
            })
    
    # Deduplicate by year
    seen_years = set()
    unique = []
    for k in sorted(karriere, key=lambda x: x['year']):
        if k['year'] not in seen_years:
            seen_years.add(k['year'])
            unique.append(k)
    
    return unique


def extract_properties_from_text(text, name, existing_props):
    """Extract biographical properties from web text."""
    new_props = []
    existing_keys = {p.get('key', '').lower() for p in existing_props if isinstance(p, dict)}
    
    lastname = name.split()[-1] if name.split() else name
    text_lower = text.lower()
    
    # Age/Birth
    if 'alter' not in existing_keys:
        m = re.search(r'(?:jahrgang|geboren)\s*(\d{4})', text_lower)
        if m:
            age = 2026 - int(m.group(1))
            new_props.append({'key': 'Alter', 'val': f'{age} Jahre (Jg. {m.group(1)})', 'ev': 'E'})
    
    # Profession
    if 'beruf' not in existing_keys:
        prof_patterns = [
            r'(?:von beruf|beruflich|arbeitet als|ist)\s+(\w+(?:\s+\w+){0,3})',
        ]
        for pat in prof_patterns:
            m = re.search(pat, text_lower)
            if m and lastname.lower() in text_lower[max(0,m.start()-100):m.start()+100]:
                new_props.append({'key': 'Beruf', 'val': m.group(1).title()[:50], 'ev': 'I'})
                break
    
    # Family
    if 'familienstand' not in existing_keys:
        if 'verheiratet' in text_lower:
            m = re.search(r'verheiratet[^.]{0,50}', text_lower)
            if m and lastname.lower() in text_lower[max(0,m.start()-200):m.start()+200]:
                new_props.append({'key': 'Familienstand', 'val': m.group(0).strip().title()[:60], 'ev': 'I'})
    
    # Education
    if 'bildung' not in existing_keys and 'studium' not in existing_keys:
        edu_m = re.search(r'(?:studiert|studium|diplom|master|bachelor|dr\.|prof\.)[^.]{5,80}', text_lower)
        if edu_m and lastname.lower() in text_lower[max(0,edu_m.start()-200):edu_m.start()+200]:
            new_props.append({'key': 'Bildung', 'val': edu_m.group(0).strip().title()[:60], 'ev': 'I'})
    
    return new_props


def simple_sentiment(text):
    """Simple German sentiment scoring."""
    positive = ['erfolg', 'gewinn', 'unterstütz', 'beliebt', 'stark', 'gut', 'positiv', 
                'zuversicht', 'chance', 'wachstum', 'verbesser', 'förder', 'engagier']
    negative = ['kritik', 'skandal', 'problem', 'verlust', 'schwach', 'schlecht', 'negativ',
                'vorwurf', 'streit', 'krise', 'rücktritt', 'versagen', 'schuld', 'korrupt']
    
    text_lower = text.lower()
    pos = sum(1 for w in positive if w in text_lower)
    neg = sum(1 for w in negative if w in text_lower)
    
    if pos + neg == 0:
        return 0.0
    return round((pos - neg) / (pos + neg), 2)


def deep_enrich_city(slug, dry_run=False, x_only=False):
    """Deep enrichment for a single city."""
    path = CITIES_DIR / f'{slug}.json'
    if not path.exists():
        print(f"❌ City not found: {slug}")
        return
    
    data = json.load(open(path))
    kb = data.get('kb', {})
    city_name = data.get('tenant', {}).get('gemeinde', '') or data.get('tenant', {}).get('name', slug)
    
    # Before stats
    before_news = len(data.get('news', []))
    before_quellen = sum(len(v.get('quellen', [])) for v in kb.values() if isinstance(v, dict))
    before_bio_chars = sum(len(str(v.get('bio', ''))) for v in kb.values() if isinstance(v, dict))
    
    print(f"\n{'='*60}")
    print(f"DEEP ENRICHMENT: {city_name.upper()} ({slug})")
    print(f"{'='*60}")
    print(f"  Before: {before_news} news, {before_quellen} quellen, {before_bio_chars} bio chars")
    
    new_news = []
    new_quellen_total = 0
    
    for k, v in kb.items():
        if not isinstance(v, dict):
            continue
        name = v.get('name', k)
        party = v.get('party', '')
        print(f"\n  ── {name} ({party}) ──")
        
        # ── 1. WEB RESEARCH ──
        if not x_only:
            # Search for bio/profile
            queries = [
                f"{name} {party} {city_name} Kommunalwahl 2026",
                f"{name} {city_name} Bürgermeister Kandidat",
                f"{name} {city_name} Biografie Lebenslauf",
            ]
            
            all_results = []
            existing_urls = {q.get('url', '') for q in v.get('quellen', []) if isinstance(q, dict)}
            existing_urls.update({n.get('url', '') for n in data.get('news', []) if isinstance(n, dict)})
            
            for query in queries:
                results = web_search(query, count=5)
                for r in results:
                    if r['url'] not in existing_urls:
                        all_results.append(r)
                        existing_urls.add(r['url'])
                time.sleep(0.3)  # Rate limit
            
            print(f"    Web: {len(all_results)} new URLs found")
            
            # Fetch top results for bio extraction
            bio_texts = []
            new_quellen = []
            for r in all_results[:8]:  # Fetch top 8
                text = web_fetch(r['url'], max_chars=5000)
                if text and len(text) > 100:
                    bio_texts.append(text)
                    
                    # Add as quelle
                    domain = r['url'].split('/')[2] if len(r['url'].split('/')) > 2 else '?'
                    new_quellen.append({
                        'name': r['title'][:80],
                        'url': r['url'],
                        'typ': 'web',
                        'trust': 0.7 if any(t in domain for t in ['br.de', 'sueddeutsche', 'zeit.de', 'spiegel', 'infranken']) else 0.5,
                        'fetched': datetime.now().strftime('%Y-%m-%d'),
                        'source': 'deep_enrich'
                    })
                    
                    # Add as news entry
                    new_news.append({
                        'title': r['title'],
                        'url': r['url'],
                        'body': r['snippet'][:200],
                        'date': datetime.now().strftime('%Y-%m-%d'),
                        'source': domain,
                        'eija': 'I',  # Inferred until verified
                        'deep_enrich': True
                    })
                
                time.sleep(0.2)
            
            combined_text = ' '.join(bio_texts)
            
            # Extract bio if currently empty
            current_bio = str(v.get('bio', ''))
            if len(current_bio) < 50 and combined_text:
                new_bio = extract_bio_from_text(combined_text, name)
                if new_bio and len(new_bio) > len(current_bio):
                    print(f"    Bio: {len(current_bio)} → {len(new_bio)} chars")
                    if not dry_run:
                        v['bio'] = new_bio
            
            # Extract karriere
            if len(v.get('karriere', [])) < 2 and combined_text:
                new_karriere = extract_karriere_from_text(combined_text, name)
                if new_karriere:
                    existing = v.get('karriere', [])
                    merged = {k2.get('year'): k2 for k2 in existing if isinstance(k2, dict)}
                    for nk in new_karriere:
                        if nk['year'] not in merged:
                            merged[nk['year']] = nk
                    v['karriere'] = sorted(merged.values(), key=lambda x: str(x.get('year', '')))
                    print(f"    Karriere: {len(existing)} → {len(v['karriere'])} entries")
            
            # Extract new properties
            new_props = extract_properties_from_text(combined_text, name, v.get('properties', []))
            if new_props:
                if not dry_run:
                    v['properties'] = v.get('properties', []) + new_props
                print(f"    Properties: +{len(new_props)} new ({', '.join(p['key'] for p in new_props)})")
            
            # Add quellen
            if not dry_run:
                v['quellen'] = v.get('quellen', []) + new_quellen
            new_quellen_total += len(new_quellen)
            print(f"    Quellen: +{len(new_quellen)}")
        
        # ── 2. X/TWITTER SEARCH ──
        x_queries = [
            f'"{name}" {city_name}',
            f'{name} {party}',
        ]
        
        all_tweets = []
        for xq in x_queries:
            tweets = x_search(xq, max_results=10)
            all_tweets.extend(tweets)
            time.sleep(0.5)
        
        # Also search for party + city
        party_tweets = x_search(f'{party} {city_name} Wahl', max_results=10)
        all_tweets.extend(party_tweets)
        
        if all_tweets:
            # Deduplicate
            seen_ids = set()
            unique_tweets = []
            for t in all_tweets:
                tid = t.get('id', t.get('text', '')[:50])
                if tid not in seen_ids:
                    seen_ids.add(tid)
                    unique_tweets.append(t)
            
            print(f"    X/Twitter: {len(unique_tweets)} tweets found")
            
            # Sentiment from tweets
            tweet_texts = ' '.join(t['text'] for t in unique_tweets)
            x_sentiment = simple_sentiment(tweet_texts)
            print(f"    X Sentiment: {x_sentiment:+.2f}")
            
            # Add tweets as news
            for t in unique_tweets[:5]:  # Top 5 tweets
                new_news.append({
                    'title': f"X: {t['text'][:80]}...",
                    'url': f"https://x.com/i/status/{t.get('id', '')}",
                    'body': t['text'][:300],
                    'date': t.get('created_at', '')[:10],
                    'source': 'x.com',
                    'eija': 'I',
                    'deep_enrich': True,
                    'x_sentiment': x_sentiment
                })
            
            # Store X sentiment
            if not dry_run:
                v.setdefault('social', {})['x_sentiment'] = x_sentiment
                v['social']['x_tweets'] = len(unique_tweets)
                v['social']['x_last_checked'] = datetime.now().strftime('%Y-%m-%d')
    
    # ── 3. CITY-LEVEL X SEARCHES ──
    print(f"\n  ── City-Level X Search ──")
    city_x_queries = [
        f'{city_name} Kommunalwahl 2026',
        f'{city_name} OB-Wahl',
        f'#Kommunalwahl {city_name}',
        f'{city_name} Wahlkampf',
    ]
    
    city_tweets = []
    for cq in city_x_queries:
        tweets = x_search(cq, max_results=10)
        city_tweets.extend(tweets)
        time.sleep(0.5)
    
    # Deduplicate
    seen = set()
    unique_city = []
    for t in city_tweets:
        tid = t.get('id', t.get('text', '')[:50])
        if tid not in seen:
            seen.add(tid)
            unique_city.append(t)
    
    print(f"    City tweets: {len(unique_city)}")
    
    for t in unique_city[:10]:
        new_news.append({
            'title': f"X: {t['text'][:80]}...",
            'url': f"https://x.com/i/status/{t.get('id', '')}",
            'body': t['text'][:300],
            'date': t.get('created_at', '')[:10],
            'source': 'x.com',
            'eija': 'I',
            'deep_enrich': True
        })
    
    # ── 4. LOCAL INSTITUTIONAL SOURCES ──
    if not x_only:
        print(f"\n  ── Institutional Sources ──")
        institutional_queries = [
            f"site:bamberg.de Oberbürgermeisterwahl 2026" if 'bamberg' in slug else f"site:{slug}.de Wahl 2026",
            f"{city_name} Wahlamt Kandidaten 2026",
            f"{city_name} Stadtrat Fraktionen Kommunalwahl",
        ]
        
        for iq in institutional_queries:
            results = web_search(iq, count=3)
            for r in results:
                text = web_fetch(r['url'], max_chars=2000)
                if text and len(text) > 100:
                    domain = r['url'].split('/')[2] if len(r['url'].split('/')) > 2 else '?'
                    new_news.append({
                        'title': r['title'],
                        'url': r['url'],
                        'body': r['snippet'][:200],
                        'date': datetime.now().strftime('%Y-%m-%d'),
                        'source': domain,
                        'eija': 'E',  # Institutional = Evidence
                        'deep_enrich': True
                    })
                    print(f"    + {domain}: {r['title'][:60]}")
            time.sleep(0.3)
    
    # ── APPLY ──
    if not dry_run:
        # Merge new news (deduplicate by URL)
        existing_urls = {n.get('url', '') for n in data.get('news', []) if isinstance(n, dict)}
        added_news = [n for n in new_news if n.get('url') not in existing_urls]
        data['news'] = data.get('news', []) + added_news
        
        # Update tenant quellen count
        total_q = sum(len(v2.get('quellen', [])) for v2 in kb.values() if isinstance(v2, dict))
        data['tenant']['quellen'] = total_q
        
        # Save
        json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
    
    # ── AFTER STATS ──
    after_news = len(data.get('news', []))
    after_quellen = sum(len(v2.get('quellen', [])) for v2 in kb.values() if isinstance(v2, dict))
    after_bio_chars = sum(len(str(v2.get('bio', ''))) for v2 in kb.values() if isinstance(v2, dict))
    
    print(f"\n{'─'*60}")
    print(f"  BEFORE → AFTER:")
    print(f"    News:    {before_news} → {after_news} (+{after_news - before_news})")
    print(f"    Quellen: {before_quellen} → {after_quellen} (+{after_quellen - before_quellen})")
    print(f"    Bio:     {before_bio_chars} → {after_bio_chars} chars (+{after_bio_chars - before_bio_chars})")
    print(f"{'='*60}")
    
    return {
        'city': slug,
        'news_added': after_news - before_news,
        'quellen_added': after_quellen - before_quellen,
        'bio_added': after_bio_chars - before_bio_chars
    }


def main():
    args = sys.argv[1:]
    city = None
    dry_run = '--dry-run' in args
    x_only = '--x-only' in args
    all_cities = '--all' in args
    
    for i, a in enumerate(args):
        if a == '--city' and i + 1 < len(args):
            city = args[i + 1]
    
    if not city and not all_cities:
        print("Usage: python3 -m pipeline.deep_enrich --city bamberg [--dry-run] [--x-only]")
        sys.exit(1)
    
    if all_cities:
        results = []
        for f in sorted(os.listdir(CITIES_DIR)):
            if not f.endswith('.json') or f == 'internal.json':
                continue
            slug = f.replace('.json', '')
            r = deep_enrich_city(slug, dry_run=dry_run, x_only=x_only)
            if r:
                results.append(r)
        
        print(f"\n{'='*60}")
        print(f"TOTAL: {sum(r['news_added'] for r in results)} news, {sum(r['quellen_added'] for r in results)} quellen added")
    else:
        deep_enrich_city(city, dry_run=dry_run, x_only=x_only)


if __name__ == '__main__':
    main()

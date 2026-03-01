#!/usr/bin/env python3
"""
Social & RSS Tracker — Continuous intelligence gathering for city dossiers.

PURPOSE:
  Discovers and tracks X/Twitter accounts, RSS feeds, and web sources
  for all candidates and cities. Stores feed config per city for
  automated polling. Fetches latest posts and enriches dossier data.

USAGE:
  python3 -m pipeline.social_tracker discover --city bamberg   # Find accounts + feeds
  python3 -m pipeline.social_tracker poll --city bamberg       # Fetch latest from tracked sources
  python3 -m pipeline.social_tracker poll --all                # Poll all cities
  python3 -m pipeline.social_tracker status                    # Show tracking stats

FEED CONFIG:
  Stored in data/cities/<city>.json under "tracking" key:
  {
    "tracking": {
      "x_accounts": [
        {"username": "MelanieHuml", "entity": "huml", "type": "candidate"},
        {"username": "SPD_Bamberg", "entity": null, "type": "party"},
        {"username": "StadtBamberg", "entity": null, "type": "institutional"}
      ],
      "rss_feeds": [
        {"url": "https://www.infranken.de/bamberg/rss", "name": "inFranken Bamberg", "type": "media"},
        {"url": "https://www.br.de/nachrichten/oberfranken/index~rss.xml", "name": "BR Oberfranken", "type": "media"}
      ],
      "web_sources": [
        {"url": "https://www.stadt.bamberg.de/...", "name": "Stadt Bamberg", "type": "institutional"}
      ],
      "last_poll": "2026-03-01T09:30:00",
      "poll_count": 5
    }
  }
"""

import json, os, re, sys, subprocess, time
from pathlib import Path
from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET

CITIES_DIR = Path(__file__).parent.parent.parent / 'data' / 'cities'

# ── Known RSS feed patterns for Bavarian media ──
BAVARIAN_RSS_FEEDS = {
    'infranken': {
        'bamberg': 'https://www.infranken.de/lk/bamberg/rss',
        'nuernberg': 'https://www.infranken.de/lk/nuernberg/rss',
        'fuerth': 'https://www.infranken.de/lk/fuerth/rss',
        'erlangen': 'https://www.infranken.de/lk/erlangen-hoechstadt/rss',
        'bayreuth': 'https://www.infranken.de/lk/bayreuth/rss',
        'coburg': 'https://www.infranken.de/lk/coburg/rss',
        'hof': 'https://www.infranken.de/lk/hof/rss',
        'schweinfurt': 'https://www.infranken.de/lk/schweinfurt/rss',
        'wuerzburg': 'https://www.infranken.de/lk/wuerzburg/rss',
        'aschaffenburg': 'https://www.infranken.de/lk/aschaffenburg/rss',
        'forchheim': 'https://www.infranken.de/lk/forchheim/rss',
    },
    'br': {
        '_oberfranken': 'https://www.br.de/nachrichten/oberfranken/index~rss.xml',
        '_oberbayern': 'https://www.br.de/nachrichten/oberbayern/index~rss.xml',
        '_niederbayern': 'https://www.br.de/nachrichten/niederbayern/index~rss.xml',
        '_mittelfranken': 'https://www.br.de/nachrichten/mittelfranken/index~rss.xml',
        '_unterfranken': 'https://www.br.de/nachrichten/unterfranken/index~rss.xml',
        '_schwaben': 'https://www.br.de/nachrichten/schwaben/index~rss.xml',
        '_oberpfalz': 'https://www.br.de/nachrichten/oberpfalz/index~rss.xml',
    },
    'sz': {
        '_bayern': 'https://rss.sueddeutsche.de/rss/Bayern',
    },
    'merkur': {
        '_bayern': 'https://www.merkur.de/bayern/index.rss',
    }
}

# Map cities to Regierungsbezirk for BR feeds
CITY_BEZIRK = {
    'bamberg': '_oberfranken', 'bayreuth': '_oberfranken', 'coburg': '_oberfranken',
    'hof': '_oberfranken', 'forchheim': '_oberfranken',
    'nuernberg': '_mittelfranken', 'fuerth': '_mittelfranken', 'erlangen': '_mittelfranken',
    'ansbach': '_mittelfranken', 'schwabach': '_mittelfranken', 'herzogenaurach': '_mittelfranken',
    'lauf': '_mittelfranken', 'neumarkt': '_oberpfalz',
    'muenchen': '_oberbayern', 'freising': '_oberbayern', 'dachau': '_oberbayern',
    'fuerstenfeldbruck': '_oberbayern', 'germering': '_oberbayern', 'olching': '_oberbayern',
    'rosenheim': '_oberbayern', 'traunstein': '_oberbayern', 'ingolstadt': '_oberbayern',
    'landsberg': '_oberbayern', 'weilheim': '_oberbayern', 'ottobrunn': '_oberbayern',
    'aichach': '_oberbayern', 'friedberg': '_oberbayern', 'koenigsbrunn': '_oberbayern',
    'wuerzburg': '_unterfranken', 'schweinfurt': '_unterfranken', 'aschaffenburg': '_unterfranken',
    'regensburg': '_oberpfalz', 'weiden': '_oberpfalz', 'amberg': '_oberpfalz', 'schwandorf': '_oberpfalz',
    'passau': '_niederbayern', 'landshut': '_niederbayern', 'straubing': '_niederbayern',
    'deggendorf': '_niederbayern', 'dillingen': '_schwaben', 'neuburg': '_oberbayern',
    'augsburg': '_schwaben', 'kempten': '_schwaben', 'kaufbeuren': '_schwaben',
    'memmingen': '_schwaben', 'guenzburg': '_schwaben', 'donauwoerth': '_schwaben',
    'marktoberdorf': '_schwaben', 'lindau': '_schwaben',
}


def x_user_lookup(username):
    """Look up X user. Returns user data or None."""
    try:
        result = subprocess.run(
            ['xurl', 'user', username],
            capture_output=True, text=True, timeout=10
        )
        data = json.loads(result.stdout)
        return data.get('data')
    except:
        return None


def x_user_tweets(username, max_results=20):
    """Get recent tweets from a user."""
    try:
        result = subprocess.run(
            ['xurl', 'search', f'from:{username}', '-n', str(max_results)],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(result.stdout)
        return data.get('data', [])
    except:
        return []


def x_search(query, max_results=10):
    """Search X/Twitter."""
    try:
        result = subprocess.run(
            ['xurl', 'search', query, '-n', str(max_results)],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(result.stdout)
        return data.get('data', [])
    except:
        return []


def fetch_rss(url, max_items=20):
    """Fetch and parse RSS/Atom feed. Returns list of items."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 AinaryBot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
        
        root = ET.fromstring(content)
        items = []
        
        # RSS 2.0
        for item in root.findall('.//item')[:max_items]:
            items.append({
                'title': (item.findtext('title') or '').strip(),
                'url': (item.findtext('link') or '').strip(),
                'description': (item.findtext('description') or '').strip()[:300],
                'date': (item.findtext('pubDate') or '').strip(),
            })
        
        # Atom
        if not items:
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('.//atom:entry', ns)[:max_items]:
                link = entry.find('atom:link[@rel="alternate"]', ns)
                if link is None:
                    link = entry.find('atom:link', ns)
                items.append({
                    'title': (entry.findtext('atom:title', namespaces=ns) or '').strip(),
                    'url': link.get('href', '') if link is not None else '',
                    'description': (entry.findtext('atom:summary', namespaces=ns) or '').strip()[:300],
                    'date': (entry.findtext('atom:published', namespaces=ns) or 
                            entry.findtext('atom:updated', namespaces=ns) or '').strip(),
                })
        
        return items
    except Exception as e:
        return []


def discover_x_accounts(slug, data):
    """Discover X/Twitter accounts for a city's candidates and parties."""
    kb = data.get('kb', {})
    city_name = data.get('tenant', {}).get('gemeinde', '') or data.get('tenant', {}).get('name', slug)
    accounts = []
    
    # 1. Try candidate names as usernames
    for k, v in kb.items():
        if not isinstance(v, dict): continue
        name = v.get('name', '')
        if not name: continue
        
        # Generate username candidates
        parts = name.split()
        if len(parts) >= 2:
            first, last = parts[0], parts[-1]
            # Common patterns
            tries = [
                f'{first}{last}',
                f'{first}_{last}',
                f'{last}{first}',
                f'{first}{last[0]}',
                f'{first[0]}{last}',
            ]
            
            for username in tries:
                # Clean umlauts
                username = username.replace('ü','ue').replace('ö','oe').replace('ä','ae').replace('ß','ss')
                user = x_user_lookup(username)
                if user and user.get('username'):
                    # Verify it's the right person (check bio for city or party)
                    bio = (user.get('description', '') + ' ' + user.get('name', '')).lower()
                    if (city_name.lower() in bio or 
                        v.get('party', '').lower() in bio or
                        'politik' in bio or 'stadtrat' in bio or 'bürgermeister' in bio or
                        'mdb' in bio or 'mdl' in bio):
                        accounts.append({
                            'username': user['username'],
                            'entity': k,
                            'type': 'candidate',
                            'name': user.get('name', ''),
                            'bio': user.get('description', '')[:100],
                            'followers': user.get('public_metrics', {}).get('followers_count', 0)
                        })
                        print(f"    ✅ @{user['username']}: {user.get('name','')} — {user.get('description','')[:60]}")
                        break
                time.sleep(0.3)
    
    # 2. Try party accounts
    parties = set()
    for v in kb.values():
        if isinstance(v, dict) and v.get('party'):
            parties.add(v['party'])
    
    city_clean = city_name.replace('ü','ue').replace('ö','oe').replace('ä','ae').replace('ß','ss')
    for party in parties:
        party_clean = party.replace('ü','ue').replace('ö','oe').replace('ä','ae').replace('ß','ss')
        party_clean = re.sub(r'[^a-zA-Z]', '', party_clean)
        tries = [
            f'{party_clean}_{city_clean}',
            f'{party_clean}{city_clean}',
            f'{party_clean.upper()}_{city_clean}',
        ]
        for username in tries:
            user = x_user_lookup(username)
            if user and user.get('username'):
                accounts.append({
                    'username': user['username'],
                    'entity': None,
                    'type': 'party',
                    'name': user.get('name', ''),
                    'bio': user.get('description', '')[:100],
                    'followers': user.get('public_metrics', {}).get('followers_count', 0)
                })
                print(f"    ✅ @{user['username']}: {user.get('name','')} (party)")
                break
            time.sleep(0.3)
    
    # 3. City/institutional accounts
    for username in [f'Stadt{city_clean}', f'stadt_{slug}', f'stadt{slug}']:
        user = x_user_lookup(username)
        if user and user.get('username'):
            accounts.append({
                'username': user['username'],
                'entity': None,
                'type': 'institutional',
                'name': user.get('name', ''),
                'bio': user.get('description', '')[:100],
                'followers': user.get('public_metrics', {}).get('followers_count', 0)
            })
            print(f"    ✅ @{user['username']}: {user.get('name','')} (institutional)")
            break
        time.sleep(0.3)
    
    return accounts


def discover_rss_feeds(slug):
    """Discover RSS feeds for a city."""
    feeds = []
    
    # 1. inFranken regional
    if slug in BAVARIAN_RSS_FEEDS.get('infranken', {}):
        url = BAVARIAN_RSS_FEEDS['infranken'][slug]
        items = fetch_rss(url, max_items=1)
        if items:
            feeds.append({'url': url, 'name': f'inFranken {slug.title()}', 'type': 'media', 'items': len(items)})
            print(f"    ✅ RSS: inFranken {slug} ({len(items)} items)")
    
    # 2. BR Regierungsbezirk
    bezirk = CITY_BEZIRK.get(slug)
    if bezirk and bezirk in BAVARIAN_RSS_FEEDS.get('br', {}):
        url = BAVARIAN_RSS_FEEDS['br'][bezirk]
        items = fetch_rss(url, max_items=1)
        if items:
            bez_name = bezirk.replace('_', '').title()
            feeds.append({'url': url, 'name': f'BR {bez_name}', 'type': 'media', 'items': len(items)})
            print(f"    ✅ RSS: BR {bez_name}")
    
    # 3. SZ Bayern + Merkur
    for source, feed_map in [('sz', BAVARIAN_RSS_FEEDS['sz']), ('merkur', BAVARIAN_RSS_FEEDS['merkur'])]:
        url = feed_map.get('_bayern')
        if url:
            items = fetch_rss(url, max_items=1)
            if items:
                feeds.append({'url': url, 'name': f'{source.upper()} Bayern', 'type': 'media'})
    
    return feeds


def poll_city(slug, data):
    """Poll all tracked sources for new content. Returns new items."""
    tracking = data.get('tracking', {})
    new_items = []
    
    existing_urls = set()
    for n in data.get('news', []):
        if isinstance(n, dict):
            existing_urls.add(n.get('url', ''))
    
    # 1. Poll X accounts
    for acc in tracking.get('x_accounts', []):
        username = acc.get('username', '')
        if not username: continue
        
        tweets = x_user_tweets(username, max_results=20)
        new_count = 0
        for t in tweets:
            url = f"https://x.com/{username}/status/{t.get('id', '')}"
            if url not in existing_urls:
                new_items.append({
                    'title': f"@{username}: {t['text'][:80]}",
                    'url': url,
                    'body': t['text'][:300],
                    'date': t.get('created_at', '')[:10],
                    'source': f'x.com/@{username}',
                    'eija': 'I',
                    'tracked': True,
                    'entity': acc.get('entity'),
                    'x_metrics': t.get('public_metrics', {})
                })
                existing_urls.add(url)
                new_count += 1
        
        if new_count:
            print(f"    @{username}: +{new_count} new tweets")
        time.sleep(0.5)
    
    # 2. Poll RSS feeds
    city_name = data.get('tenant', {}).get('gemeinde', '') or data.get('tenant', {}).get('name', slug)
    candidate_names = [v.get('name', '').split()[-1].lower() 
                      for v in data.get('kb', {}).values() 
                      if isinstance(v, dict) and v.get('name')]
    
    for feed in tracking.get('rss_feeds', []):
        url = feed.get('url', '')
        if not url: continue
        
        items = fetch_rss(url, max_items=30)
        new_count = 0
        for item in items:
            if item['url'] in existing_urls:
                continue
            
            # Filter: only items mentioning city or candidates
            text = (item.get('title', '') + ' ' + item.get('description', '')).lower()
            if city_name.lower() in text or any(n in text for n in candidate_names if len(n) > 3):
                new_items.append({
                    'title': item['title'][:120],
                    'url': item['url'],
                    'body': re.sub(r'<[^>]+>', '', item.get('description', ''))[:300],
                    'date': item.get('date', '')[:10] or datetime.now().strftime('%Y-%m-%d'),
                    'source': feed.get('name', url.split('/')[2]),
                    'eija': 'I',
                    'tracked': True
                })
                existing_urls.add(item['url'])
                new_count += 1
        
        if new_count:
            print(f"    {feed.get('name', '?')}: +{new_count} relevant items")
    
    return new_items


def cmd_discover(slug):
    """Discover and configure tracking for a city."""
    path = CITIES_DIR / f'{slug}.json'
    if not path.exists():
        print(f"❌ City not found: {slug}")
        return
    
    data = json.load(open(path))
    city_name = data.get('tenant', {}).get('gemeinde', '') or data.get('tenant', {}).get('name', slug)
    
    print(f"\n{'='*60}")
    print(f"DISCOVER TRACKING SOURCES: {city_name.upper()}")
    print(f"{'='*60}")
    
    # Discover X accounts
    print(f"\n  X/Twitter Accounts:")
    x_accounts = discover_x_accounts(slug, data)
    
    # Discover RSS feeds
    print(f"\n  RSS Feeds:")
    rss_feeds = discover_rss_feeds(slug)
    
    # Store tracking config
    tracking = data.get('tracking', {})
    
    # Merge (don't duplicate)
    existing_x = {a['username'] for a in tracking.get('x_accounts', [])}
    for acc in x_accounts:
        if acc['username'] not in existing_x:
            tracking.setdefault('x_accounts', []).append({
                'username': acc['username'],
                'entity': acc.get('entity'),
                'type': acc['type'],
                'name': acc.get('name', ''),
            })
    
    existing_rss = {f['url'] for f in tracking.get('rss_feeds', [])}
    for feed in rss_feeds:
        if feed['url'] not in existing_rss:
            tracking.setdefault('rss_feeds', []).append({
                'url': feed['url'],
                'name': feed['name'],
                'type': feed['type']
            })
    
    data['tracking'] = tracking
    json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
    
    print(f"\n  Summary:")
    print(f"    X accounts: {len(tracking.get('x_accounts', []))}")
    print(f"    RSS feeds: {len(tracking.get('rss_feeds', []))}")
    print(f"  ✅ Tracking config saved to {slug}.json")


def cmd_poll(slug=None, all_cities=False):
    """Poll tracked sources for new content."""
    cities_to_poll = []
    
    if all_cities:
        for f in sorted(os.listdir(CITIES_DIR)):
            if f.endswith('.json') and f != 'internal.json':
                cities_to_poll.append(f.replace('.json', ''))
    elif slug:
        cities_to_poll = [slug]
    
    total_new = 0
    for city_slug in cities_to_poll:
        path = CITIES_DIR / f'{city_slug}.json'
        data = json.load(open(path))
        
        if not data.get('tracking', {}).get('x_accounts') and not data.get('tracking', {}).get('rss_feeds'):
            continue
        
        city_name = data.get('tenant', {}).get('name', city_slug)
        print(f"\n  Polling {city_name}...")
        
        new_items = poll_city(city_slug, data)
        
        if new_items:
            data['news'] = data.get('news', []) + new_items
            data['tracking']['last_poll'] = datetime.now().isoformat()
            data['tracking']['poll_count'] = data.get('tracking', {}).get('poll_count', 0) + 1
            json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
            total_new += len(new_items)
            print(f"    +{len(new_items)} new items added")
    
    print(f"\n  Total new items: {total_new}")


def cmd_status():
    """Show tracking status across all cities."""
    print(f"\n{'='*60}")
    print(f"TRACKING STATUS")
    print(f"{'='*60}")
    
    tracked = 0
    total_x = 0
    total_rss = 0
    
    for f in sorted(os.listdir(CITIES_DIR)):
        if not f.endswith('.json') or f == 'internal.json':
            continue
        data = json.load(open(CITIES_DIR / f))
        tracking = data.get('tracking', {})
        x_count = len(tracking.get('x_accounts', []))
        rss_count = len(tracking.get('rss_feeds', []))
        
        if x_count or rss_count:
            tracked += 1
            total_x += x_count
            total_rss += rss_count
            last = tracking.get('last_poll', 'never')
            print(f"  {f.replace('.json',''):20s}  X: {x_count}  RSS: {rss_count}  Last: {last[:16]}")
    
    print(f"\n  Tracked cities: {tracked}/50")
    print(f"  Total X accounts: {total_x}")
    print(f"  Total RSS feeds: {total_rss}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    
    cmd = args[0]
    city = None
    all_flag = '--all' in args
    
    for i, a in enumerate(args):
        if a == '--city' and i + 1 < len(args):
            city = args[i + 1]
    
    if cmd == 'discover':
        if not city:
            print("Usage: --city <slug>")
            sys.exit(1)
        cmd_discover(city)
    elif cmd == 'poll':
        cmd_poll(slug=city, all_cities=all_flag)
    elif cmd == 'status':
        cmd_status()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()

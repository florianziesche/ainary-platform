#!/usr/bin/env python3
"""
Track fast-growing GitHub projects in the OpenClaw ecosystem.
Runs weekly, stores star history, alerts on >2x growth.
"""
import json, os, re, sys, time
from datetime import datetime
from pathlib import Path
import urllib.request, urllib.parse

TRACKER_FILE = Path.home() / ".openclaw/workspace/memory/knowledge/openclaw-ecosystem-tracker.json"
BRAVE_KEY = ""

# Seed repos to track
SEED_REPOS = [
    "openclaw/openclaw",
    "HKUDS/ClawWork",
    "sseanliu/VisionClaw",
    "Temaki-AI/clawd-control",
]

def get_brave_key():
    global BRAVE_KEY
    if BRAVE_KEY: return BRAVE_KEY
    try:
        cfg = json.load(open(Path.home() / ".openclaw/openclaw.json"))
        BRAVE_KEY = cfg["tools"]["web"]["search"]["apiKey"]
    except: pass
    return BRAVE_KEY

def github_api(path, token=None):
    """Fetch from GitHub API."""
    url = f"https://api.github.com/{path}"
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "openclaw-tracker"}
    if token: headers["Authorization"] = f"token {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"  [WARN] GitHub API: {e}")
        return None

def brave_search(query, count=10):
    key = get_brave_key()
    if not key: return []
    url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={count}"
    req = urllib.request.Request(url, headers={"X-Subscription-Token": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            return data.get("web", {}).get("results", [])
    except: return []

def discover_new_repos():
    """Find new OpenClaw ecosystem repos via Brave Search."""
    queries = [
        "site:github.com openclaw extension tool skill 2026",
        "site:github.com openclaw agent framework new stars",
        "github trending openclaw nanobot clawwork 2026",
    ]
    repos = set()
    for q in queries:
        results = brave_search(q, 5)
        for r in results:
            url = r.get("url", "")
            m = re.match(r"https://github\.com/([^/]+/[^/]+)", url)
            if m:
                repo = m.group(1)
                if repo not in ["openclaw/openclaw"]:  # Skip main repo for discovery
                    repos.add(repo)
    return list(repos)

def load_tracker():
    if TRACKER_FILE.exists():
        return json.loads(TRACKER_FILE.read_text())
    return {"repos": {}, "snapshots": [], "alerts": []}

def save_tracker(data):
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_FILE.write_text(json.dumps(data, indent=2))

def track():
    print(f"{'='*60}")
    print(f"OpenClaw Ecosystem Tracker — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}")

    tracker = load_tracker()
    gh_token = os.environ.get("GITHUB_TOKEN", "")

    # Discover new repos
    print("\n[1] Discovering new repos...")
    discovered = discover_new_repos()
    all_repos = list(set(SEED_REPOS + list(tracker.get("repos", {}).keys()) + discovered))
    print(f"  Tracking {len(all_repos)} repos ({len(discovered)} discovered)")

    # Fetch current stats
    print("\n[2] Fetching GitHub stats...")
    snapshot = {"timestamp": datetime.now().isoformat(), "repos": {}}
    alerts = []

    for repo in sorted(all_repos):
        data = github_api(f"repos/{repo}", gh_token)
        if not data or "stargazers_count" not in data:
            print(f"  {repo}: SKIP (not found)")
            continue

        stars = data["stargazers_count"]
        forks = data["forks_count"]
        created = data.get("created_at", "")
        desc = (data.get("description") or "")[:80]
        lang = data.get("language", "?")
        updated = data.get("pushed_at", "")

        # Compare with last snapshot
        prev = tracker.get("repos", {}).get(repo, {})
        prev_stars = prev.get("stars", 0)
        growth = stars - prev_stars if prev_stars else 0
        growth_pct = (growth / prev_stars * 100) if prev_stars > 0 else 0

        status = ""
        if growth_pct > 100:
            status = " ** EXPLODING **"
            alerts.append(f"{repo}: {prev_stars} -> {stars} (+{growth_pct:.0f}%)")
        elif growth_pct > 50:
            status = " * FAST *"
            alerts.append(f"{repo}: {prev_stars} -> {stars} (+{growth_pct:.0f}%)")
        elif growth_pct > 20:
            status = " growing"

        print(f"  {repo:40s} {stars:>7,} stars  {forks:>5,} forks  +{growth:>5}{status}")

        tracker["repos"][repo] = {
            "stars": stars, "forks": forks, "description": desc,
            "language": lang, "updated": updated, "created": created,
            "last_checked": datetime.now().isoformat(),
        }
        snapshot["repos"][repo] = {"stars": stars, "forks": forks, "growth": growth}

    tracker["snapshots"].append(snapshot)
    # Keep last 52 snapshots (1 year weekly)
    tracker["snapshots"] = tracker["snapshots"][-52:]

    if alerts:
        tracker["alerts"] = tracker.get("alerts", []) + [{
            "timestamp": datetime.now().isoformat(),
            "items": alerts
        }]
        print(f"\n[!] ALERTS:")
        for a in alerts:
            print(f"  {a}")

    save_tracker(tracker)

    # Summary table
    print(f"\n{'='*60}")
    print(f"TOP 10 by Stars:")
    print(f"{'='*60}")
    sorted_repos = sorted(tracker["repos"].items(), key=lambda x: x[1]["stars"], reverse=True)[:10]
    print(f"{'Repo':40s} {'Stars':>8s} {'Forks':>7s} {'Lang':>6s}")
    print("-" * 65)
    for repo, info in sorted_repos:
        print(f"{repo:40s} {info['stars']:>8,} {info['forks']:>7,} {(info.get('language') or '?'):>6s}")

    print(f"\nSaved: {TRACKER_FILE}")
    return alerts

if __name__ == "__main__":
    track()

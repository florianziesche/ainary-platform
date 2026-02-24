#!/usr/bin/env python3
"""
Social Media Intelligence Scraper — Deep Profile Analysis
Scrapes public Instagram profiles for engagement metrics, posting patterns, top content.

Usage:
  python3 social_scraper.py marcus.koenig.nuernberg    # Single profile
  python3 social_scraper.py --all                       # All known candidates
  python3 social_scraper.py --city nuernberg            # All candidates in city

Output: data/social/{username}.json + enriches city JSONs
"""

import json, sys, os, re
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter

try:
    import instaloader
except ImportError:
    print("pip3 install instaloader")
    sys.exit(1)

SOCIAL_DIR = Path("data/social")
CITIES_DIR = Path("data/cities")
ONTOLOGY_FILE = Path("data/ontology.json")

# Known Instagram handles (from our research)
KNOWN_HANDLES = {
    # Nürnberg
    "marcuskoenignbg": {"name": "Marcus König", "party": "CSU", "city": "nuernberg", "role": "OB"},
    "nasser.ahmed.spd": {"name": "Nasser Ahmed", "party": "SPD", "city": "nuernberg", "role": "Herausforderer"},
    # Augsburg
    "eva.weber.augsburg": {"name": "Eva Weber", "party": "CSU", "city": "augsburg", "role": "OB"},
    "florian.freund.spd": {"name": "Florian Freund", "party": "SPD", "city": "augsburg", "role": "Herausforderer"},
    "martina.wild.augsburg": {"name": "Martina Wild", "party": "Grüne", "city": "augsburg", "role": "2.BM"},
    # Bamberg
    "melaniehuml": {"name": "Melanie Huml", "party": "CSU", "city": "bamberg", "role": "Kandidatin"},
    "jonas.gluesenkamp": {"name": "Jonas Glüsenkamp", "party": "Grüne", "city": "bamberg", "role": "2.BM"},
    # Erlangen
    "florianjanik": {"name": "Dr. Florian Janik", "party": "SPD", "city": "erlangen", "role": "OB"},
    "joerg.volleth": {"name": "Jörg Volleth", "party": "CSU", "city": "erlangen", "role": "3.BM"},
    # Passau
    "stefanie.auer.passau": {"name": "Stefanie Auer", "party": "Grüne", "city": "passau", "role": "Kandidatin"},
    "armin.dickl": {"name": "Armin Dickl", "party": "CSU", "city": "passau", "role": "Kandidat"},
    # Fürth
    "thomas.jung.fuerth": {"name": "Thomas Jung", "party": "SPD", "city": "fuerth", "role": "OB"},
    # Landshut
    "thomas.haslinger.csu": {"name": "Thomas Haslinger", "party": "CSU", "city": "landshut", "role": "2.BM"},
    # Regensburg
    "astrid.freudenstein": {"name": "Astrid Freudenstein", "party": "CSU", "city": "regensburg", "role": "2.BM"},
}


def scrape_profile(username, login_context=None):
    """Scrape public Instagram profile — no login needed for basic data."""
    L = login_context or instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        quiet=True,
    )
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        print(f"  ❌ {username}: {e}")
        return None
    
    # Basic profile data
    data = {
        "username": username,
        "full_name": profile.full_name,
        "biography": profile.biography,
        "followers": profile.followers,
        "following": profile.followees,
        "posts_count": profile.mediacount,
        "is_verified": profile.is_verified,
        "is_private": profile.is_private,
        "external_url": profile.external_url,
        "scraped_at": datetime.now().isoformat(),
    }
    
    if profile.is_private:
        print(f"  🔒 {username}: Private account — only basic data available")
        return data
    
    # Scrape last 30 posts for engagement analysis
    posts = []
    post_count = 0
    now = datetime.now()
    thirty_days_ago = now - timedelta(days=30)
    ninety_days_ago = now - timedelta(days=90)
    
    try:
        for post in profile.get_posts():
            post_count += 1
            if post_count > 50:  # Max 50 posts
                break
            
            post_data = {
                "shortcode": post.shortcode,
                "date": post.date_utc.isoformat(),
                "likes": post.likes,
                "comments": post.comments,
                "caption": (post.caption or "")[:200],  # First 200 chars
                "is_video": post.is_video,
                "video_views": post.video_view_count if post.is_video else 0,
                "hashtags": list(post.caption_hashtags) if post.caption_hashtags else [],
                "mentions": list(post.caption_mentions) if post.caption_mentions else [],
            }
            posts.append(post_data)
    except Exception as e:
        print(f"  ⚠️ {username}: Error scraping posts: {e}")
    
    data["posts"] = posts
    
    # Calculate engagement metrics
    if posts and data["followers"] > 0:
        total_likes = sum(p["likes"] for p in posts)
        total_comments = sum(p["comments"] for p in posts)
        avg_likes = total_likes / len(posts)
        avg_comments = total_comments / len(posts)
        engagement_rate = ((avg_likes + avg_comments) / data["followers"]) * 100
        
        # Posts in last 30 days
        recent_posts = [p for p in posts if datetime.fromisoformat(p["date"]) > thirty_days_ago.replace(tzinfo=None)]
        posts_per_week_30d = len(recent_posts) / 4.3 if recent_posts else 0
        
        # Posts in last 90 days
        quarter_posts = [p for p in posts if datetime.fromisoformat(p["date"]) > ninety_days_ago.replace(tzinfo=None)]
        posts_per_week_90d = len(quarter_posts) / 13 if quarter_posts else 0
        
        # Top hashtags
        all_hashtags = []
        for p in posts:
            all_hashtags.extend(p.get("hashtags", []))
        top_hashtags = Counter(all_hashtags).most_common(10)
        
        # Top performing posts (by engagement)
        posts_sorted = sorted(posts, key=lambda p: p["likes"] + p["comments"], reverse=True)
        top_posts = posts_sorted[:3]
        
        # Posting time analysis
        from collections import defaultdict
        day_counts = Counter()
        hour_counts = Counter()
        for p in posts:
            dt = datetime.fromisoformat(p["date"])
            day_counts[dt.strftime("%A")] += 1
            hour_counts[dt.hour] += 1
        
        # Engagement trend (first half vs second half of posts)
        if len(posts) >= 6:
            half = len(posts) // 2
            recent_eng = sum(p["likes"] + p["comments"] for p in posts[:half]) / half
            older_eng = sum(p["likes"] + p["comments"] for p in posts[half:]) / (len(posts) - half)
            trend = "STEIGEND" if recent_eng > older_eng * 1.1 else "FALLEND" if recent_eng < older_eng * 0.9 else "STABIL"
            trend_pct = ((recent_eng - older_eng) / max(older_eng, 1)) * 100
        else:
            trend = "UNBEKANNT"
            trend_pct = 0
        
        data["metrics"] = {
            "engagement_rate": round(engagement_rate, 2),
            "avg_likes": round(avg_likes, 1),
            "avg_comments": round(avg_comments, 1),
            "posts_per_week_30d": round(posts_per_week_30d, 1),
            "posts_per_week_90d": round(posts_per_week_90d, 1),
            "total_posts_scraped": len(posts),
            "top_hashtags": top_hashtags,
            "favorite_day": day_counts.most_common(1)[0][0] if day_counts else "?",
            "favorite_hour": hour_counts.most_common(1)[0][0] if hour_counts else "?",
            "engagement_trend": trend,
            "engagement_trend_pct": round(trend_pct, 1),
            "top_post_likes": top_posts[0]["likes"] if top_posts else 0,
            "top_post_caption": top_posts[0]["caption"][:100] if top_posts else "",
        }
        
        # Generate insights
        insights = []
        if engagement_rate > 3:
            insights.append(f"STARK: {engagement_rate:.1f}% Engagement Rate — über Branchendurchschnitt (1-3%)")
        elif engagement_rate < 1:
            insights.append(f"SCHWACH: {engagement_rate:.1f}% Engagement Rate — passive Follower-Basis")
        
        if posts_per_week_30d > 5:
            insights.append(f"Wahlkampf-Modus: {posts_per_week_30d:.0f} Posts/Woche (letzte 30 Tage)")
        elif posts_per_week_30d < 1:
            insights.append(f"Digitaler Blindspot: Nur {posts_per_week_30d:.1f} Posts/Woche")
        
        if trend == "STEIGEND":
            insights.append(f"Engagement steigt um {trend_pct:.0f}% — Kampagne gewinnt an Momentum")
        elif trend == "FALLEND":
            insights.append(f"Engagement fällt um {abs(trend_pct):.0f}% — Kampagne verliert Momentum")
        
        data["insights"] = insights
    
    return data


def print_report(data, meta=None):
    """Pretty-print profile analysis."""
    if not data:
        return
    
    name = meta.get("name", data["full_name"]) if meta else data["full_name"]
    party = meta.get("party", "") if meta else ""
    city = meta.get("city", "") if meta else ""
    
    print(f"\n{'='*60}")
    print(f"📊 {name} ({party}, {city})")
    print(f"   @{data['username']} {'🔵' if data.get('is_verified') else ''}")
    print(f"{'='*60}")
    print(f"   Followers: {data['followers']:,}")
    print(f"   Following: {data['following']:,}")
    print(f"   Posts: {data['posts_count']}")
    
    if "metrics" in data:
        m = data["metrics"]
        print(f"\n   📈 ENGAGEMENT:")
        print(f"   Rate: {m['engagement_rate']:.2f}%")
        print(f"   Avg Likes: {m['avg_likes']:.0f} | Avg Comments: {m['avg_comments']:.0f}")
        print(f"   Posts/Woche (30d): {m['posts_per_week_30d']:.1f}")
        print(f"   Posts/Woche (90d): {m['posts_per_week_90d']:.1f}")
        print(f"   Trend: {m['engagement_trend']} ({m['engagement_trend_pct']:+.0f}%)")
        print(f"   Lieblings-Tag: {m['favorite_day']} | Lieblings-Uhrzeit: {m['favorite_hour']}:00")
        
        if m["top_hashtags"]:
            tags = ", ".join(f"#{h[0]} ({h[1]})" for h in m["top_hashtags"][:5])
            print(f"   Top Hashtags: {tags}")
        
        if m["top_post_likes"]:
            print(f"   Top Post: {m['top_post_likes']:,} Likes — \"{m['top_post_caption']}...\"")
    
    if "insights" in data:
        print(f"\n   💡 INSIGHTS:")
        for insight in data["insights"]:
            print(f"   • {insight}")


def generate_comparison(profiles):
    """Generate cross-candidate comparison for a city."""
    if len(profiles) < 2:
        return
    
    print(f"\n{'='*60}")
    print(f"⚔️  HEAD-TO-HEAD COMPARISON")
    print(f"{'='*60}")
    
    # Sort by followers
    sorted_profiles = sorted(profiles, key=lambda x: x[0].get("followers", 0), reverse=True)
    
    for data, meta in sorted_profiles:
        eng = data.get("metrics", {}).get("engagement_rate", 0)
        ppw = data.get("metrics", {}).get("posts_per_week_30d", 0)
        trend = data.get("metrics", {}).get("engagement_trend", "?")
        print(f"   {meta.get('name', '?'):25s} | {data['followers']:>6,} FL | {eng:>5.2f}% ENG | {ppw:.1f} Posts/W | {trend}")
    
    # Calculate efficiency
    print(f"\n   🎯 EFFIZIENZ (Engagement pro 1.000 Follower):")
    for data, meta in sorted_profiles:
        if data.get("followers", 0) > 0:
            eng_per_k = (data.get("metrics", {}).get("avg_likes", 0) + data.get("metrics", {}).get("avg_comments", 0)) / (data["followers"] / 1000)
            print(f"   {meta.get('name', '?'):25s} | {eng_per_k:.1f} Interaktionen pro 1K Follower")


def main():
    SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
    
    L = instaloader.Instaloader(
        download_pictures=False, download_videos=False,
        download_video_thumbnails=False, download_geotags=False,
        download_comments=False, save_metadata=False,
        compress_json=False, quiet=True,
    )
    
    if "--all" in sys.argv:
        targets = list(KNOWN_HANDLES.items())
    elif "--city" in sys.argv:
        city = sys.argv[sys.argv.index("--city") + 1]
        targets = [(u, m) for u, m in KNOWN_HANDLES.items() if m["city"] == city]
    else:
        # Single username
        username = sys.argv[1] if len(sys.argv) > 1 else None
        if not username:
            print("Usage: python3 social_scraper.py <username> | --all | --city <slug>")
            print(f"\nKnown handles ({len(KNOWN_HANDLES)}):")
            for u, m in sorted(KNOWN_HANDLES.items(), key=lambda x: x[1]["city"]):
                print(f"  @{u:35s} {m['name']:25s} ({m['party']}, {m['city']})")
            return
        meta = KNOWN_HANDLES.get(username, {})
        targets = [(username, meta)]
    
    city_profiles = {}  # city -> [(data, meta)]
    
    for username, meta in targets:
        print(f"\n🔍 Scraping @{username}...")
        data = scrape_profile(username, L)
        
        if data:
            # Save individual profile
            outfile = SOCIAL_DIR / f"{username}.json"
            with open(outfile, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"   💾 Saved: {outfile}")
            
            print_report(data, meta)
            
            # Group by city for comparison
            city = meta.get("city", "unknown")
            if city not in city_profiles:
                city_profiles[city] = []
            city_profiles[city].append((data, meta))
    
    # Generate comparisons
    for city, profiles in city_profiles.items():
        if len(profiles) >= 2:
            generate_comparison(profiles)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SOCIAL SCRAPER SUMMARY")
    print(f"{'='*60}")
    print(f"Profiles scraped: {sum(len(p) for p in city_profiles.values())}")
    print(f"Cities covered: {len(city_profiles)}")
    print(f"Output: {SOCIAL_DIR}/")


if __name__ == "__main__":
    main()

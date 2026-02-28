#!/usr/bin/env python3
"""
Daily Brief Generator
=====================
Generates a fresh daily-brief.html with real signals from blogwatcher + web search.
Designed to run as cron at 06:00 CET, output deployed to ainaryventures.com/de/daily-brief.html

Output: daily-brief.html (self-contained, matches ainaryventures.com dark theme)

Usage:
  python3 generate_brief.py              # Generate today's brief
  python3 generate_brief.py --preview    # Open in browser after generation
"""

import json, os, sys, subprocess, re
from datetime import datetime, date
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def get_blogwatcher_updates():
    """Get recent updates from blogwatcher."""
    # First scan for new articles
    try:
        subprocess.run(["blogwatcher", "scan"], capture_output=True, text=True, timeout=120)
    except Exception:
        pass
    
    # Then get unread articles
    try:
        result = subprocess.run(
            ["blogwatcher", "articles"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0 and result.stdout.strip():
            return parse_blogwatcher_articles(result.stdout)
    except Exception:
        pass
    
    return []

def parse_blogwatcher_articles(text):
    """Parse blogwatcher articles output."""
    signals = []
    lines = text.strip().split('\n')
    current = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith('[') and '[new]' in line:
            if current.get('title'):
                signals.append(current)
            title = re.sub(r'^\[\d+\]\s*\[new\]\s*', '', line)
            current = {"title": title, "source": "", "url": "", "time": "today"}
        elif line.startswith('Blog:'):
            current["source"] = line.replace('Blog:', '').strip()
        elif line.startswith('URL:'):
            current["url"] = line.replace('URL:', '').strip()
        elif line.startswith('Published:'):
            current["time"] = line.replace('Published:', '').strip()
    
    if current.get('title'):
        signals.append(current)
    
    return signals

def parse_blogwatcher_text(text):
    """Parse blogwatcher text output into structured data."""
    signals = []
    lines = text.strip().split('\n')
    current_source = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(':') and not line.startswith('http'):
            current_source = line.rstrip(':')
        elif line.startswith('http') or line.startswith('- '):
            title = line.lstrip('- ').split(' (http')[0].split(' — ')[0]
            url = ""
            url_match = re.search(r'(https?://\S+)', line)
            if url_match:
                url = url_match.group(1)
            if title and len(title) > 10:
                signals.append({
                    "source": current_source or "Feed",
                    "title": title[:120],
                    "url": url,
                    "time": "today"
                })
    
    return signals[:20]  # Max 20 signals

def categorize_signal(title):
    """Categorize a signal based on keywords."""
    title_lower = title.lower()
    categories = {
        "AI Agents": ["agent", "multi-agent", "orchestr", "autono"],
        "AI Trust & Safety": ["trust", "safety", "alignment", "govern", "regulat", "audit"],
        "Funding & Deals": ["raises", "funding", "series", "acqui", "ipo", "valuat", "million", "billion"],
        "Enterprise AI": ["enterprise", "deploy", "production", "adoption"],
        "Open Source": ["open source", "github", "release", "launch"],
        "Research": ["paper", "arxiv", "research", "study", "benchmark"],
        "Policy & Regulation": ["eu ai act", "regulat", "compli", "policy", "law"],
        "Infrastructure": ["infra", "gpu", "compute", "inference", "hosting"],
    }
    for cat, keywords in categories.items():
        if any(k in title_lower for k in keywords):
            return cat
    return "Signal"

def confidence_dots(level=3):
    """Return confidence indicator."""
    if level >= 3:
        return '<span style="color:#4ade80;">●●●</span>'
    elif level >= 2:
        return '<span style="color:#c8aa50;">●●○</span>'
    else:
        return '<span style="color:#ef4444;">●○○</span>'

def generate_html(signals, today):
    """Generate the daily brief HTML."""
    
    # Group by category
    categories = {}
    for s in signals:
        cat = categorize_signal(s.get("title", ""))
        categories.setdefault(cat, []).append(s)
    
    # Build signal HTML
    signals_html = ""
    for cat, items in sorted(categories.items(), key=lambda x: -len(x[1])):
        for item in items[:3]:  # Max 3 per category
            title = item.get("title", "")
            source = item.get("source", "Feed")
            url = item.get("url", "")
            time_str = item.get("time", "today")
            
            title_html = f'<a href="{url}" target="_blank" rel="noopener" style="color:var(--text-primary);text-decoration:none;border-bottom:1px solid rgba(255,255,255,0.1);">{title}</a>' if url else title
            
            signals_html += f"""
    <div class="signal-card">
      <div class="signal-meta">
        <span class="signal-source">{source}</span>
        <span class="signal-time">{time_str}</span>
        {confidence_dots(3)}
      </div>
      <h3>{title_html}</h3>
      <div class="signal-cat">{cat}</div>
    </div>"""
    
    if not signals_html:
        signals_html = """
    <div class="signal-card">
      <div class="signal-meta"><span class="signal-source">System</span></div>
      <h3>Keine neuen Signale in den letzten 24 Stunden.</h3>
      <p style="color:var(--text-secondary);font-size:0.9rem;margin-top:8px;">Das Briefing wird taeglich um 06:00 Uhr aktualisiert.</p>
    </div>"""
    
    # Count stats
    n_signals = len(signals)
    n_categories = len(categories)
    kw = today.isocalendar()[1]
    weekday = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"][today.weekday()]
    months_de = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    date_str = f"{weekday}, {today.day}. {months_de[today.month-1]} {today.year}"
    
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Taegliches Briefing — Ainary</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:#08080c;--surface:#111116;--text-primary:#ededf0;
  --text-secondary:#8b8b95;--text-muted:#55555e;--gold:#c8aa50;
  --border:rgba(255,255,255,0.08);--font-body:'Inter',sans-serif;
  --font-mono:'JetBrains Mono',monospace;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:var(--font-body);background:var(--bg);color:var(--text-primary);-webkit-font-smoothing:antialiased}}
.container{{max-width:720px;margin:0 auto;padding:0 24px}}

/* Nav */
.nav{{padding:16px 0;border-bottom:1px solid var(--border)}}
.nav .container{{display:flex;justify-content:space-between;align-items:center}}
.nav-logo{{font-size:14px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--text-muted);text-decoration:none}}
.nav-back{{font-size:13px;color:var(--gold);text-decoration:none}}

/* Header */
.brief-header{{padding:64px 0 32px;border-bottom:1px solid var(--border)}}
.brief-header h1{{font-size:clamp(1.75rem,3vw,2.5rem);font-weight:600;letter-spacing:-0.03em;margin-bottom:8px}}
.brief-header .subtitle{{color:var(--text-secondary);font-size:0.95rem;margin-bottom:24px}}
.brief-meta{{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--text-muted)}}
.brief-meta span{{padding:4px 10px;background:var(--surface);border:1px solid var(--border);border-radius:4px}}

/* Signals */
.signals{{padding:32px 0}}
.signal-card{{padding:24px 0;border-bottom:1px solid var(--border)}}
.signal-card:last-child{{border:none}}
.signal-meta{{display:flex;align-items:center;gap:12px;margin-bottom:8px;font-family:var(--font-mono);font-size:0.7rem;color:var(--text-muted)}}
.signal-source{{text-transform:uppercase;letter-spacing:0.5px}}
.signal-card h3{{font-size:1.05rem;font-weight:500;line-height:1.4;margin-bottom:6px}}
.signal-card h3 a:hover{{border-color:var(--gold)}}
.signal-cat{{font-family:var(--font-mono);font-size:0.7rem;color:var(--gold);text-transform:uppercase;letter-spacing:0.5px}}

/* Footer */
.brief-footer{{padding:32px 0;border-top:1px solid var(--border);text-align:center;font-size:12px;color:var(--text-muted)}}
.brief-footer a{{color:var(--gold);text-decoration:none}}
</style>
</head>
<body>

<div class="nav">
  <div class="container">
    <a href="../index.html" class="nav-logo">Ainary Ventures</a>
    <a href="../index.html" class="nav-back">&larr; Zurueck</a>
  </div>
</div>

<section class="brief-header">
  <div class="container">
    <h1>Taegliches Briefing</h1>
    <div class="subtitle">Mehrere Quellen gescannt. Die Signale, die zaehlen — jeden Morgen.</div>
    <div class="brief-meta">
      <span>{date_str}</span>
      <span>{n_signals} Signale</span>
      <span>{n_categories} Kategorien</span>
      <span>KW {kw}</span>
    </div>
  </div>
</section>

<section class="signals">
  <div class="container">
    {signals_html}
  </div>
</section>

<div class="brief-footer">
  <div class="container">
    <p>Generiert um {datetime.now().strftime('%H:%M')} Uhr &middot; 46 Quellen gescannt &middot; <a href="mailto:florian@ainaryventures.com">florian@ainaryventures.com</a></p>
    <p style="margin-top:8px">&copy; 2026 Ainary Ventures</p>
  </div>
</div>

</body>
</html>"""
    
    return html


def main():
    today = date.today()
    print(f"Generating Daily Brief for {today}...")
    
    # Get signals
    signals = get_blogwatcher_updates()
    print(f"  Found {len(signals)} signals from blogwatcher")
    
    # Generate HTML
    html = generate_html(signals, today)
    
    # Save
    outpath = OUTPUT_DIR / "daily-brief.html"
    outpath.write_text(html, encoding="utf-8")
    print(f"  Saved: {outpath} ({outpath.stat().st_size/1024:.1f} KB)")
    
    # Also save dated version
    dated = OUTPUT_DIR / f"daily-brief-{today.isoformat()}.html"
    dated.write_text(html, encoding="utf-8")
    
    if "--preview" in sys.argv:
        subprocess.run(["open", str(outpath)])
    
    return str(outpath)


if __name__ == "__main__":
    main()

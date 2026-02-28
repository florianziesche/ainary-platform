#!/usr/bin/env python3
"""
Batch Report Generator — Ainary Ventures
Generates 100 branded HTML research reports from topics.json + knowledge base.
Uses OpenAI GPT-4o for generation, Brave Search for live sources.

Usage: python generate_batch.py [--start N] [--count N] [--dry-run]
"""

import json
import os
import sys
import time
import re
import argparse
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

# --- Config ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY", "")
MODEL = "gpt-4o"
BASE_DIR = Path(__file__).parent
TOPICS_FILE = BASE_DIR / "topics.json"
OUTPUT_DIR = BASE_DIR / "reports"
KNOWLEDGE_DIR = BASE_DIR.parent.parent / "knowledge"
RESEARCH_BASE = BASE_DIR.parent.parent / "research-base"

# Rate limiting
DELAY_BETWEEN_REPORTS = 2  # seconds
MAX_RETRIES = 3


def load_knowledge_base():
    """Load all knowledge files into a single context string, truncated to ~30K chars."""
    knowledge = []
    
    # Priority order: CRTs > Claims > AI Research > Resources (truncated)
    
    # 1. Compounding Research Truths
    crt_path = RESEARCH_BASE / "compounding-research-truths.json"
    if crt_path.exists():
        try:
            crts = json.loads(crt_path.read_text())
            crt_summary = "## Verified Research Truths\n"
            for crt in crts[:20]:
                if isinstance(crt, dict):
                    crt_summary += f"- {crt.get('claim', crt.get('truth', str(crt)))}\n"
            knowledge.append(crt_summary)
        except:
            pass
    
    # 2. Reference Library
    ref_path = RESEARCH_BASE / "reference-library.json"
    if ref_path.exists():
        knowledge.append(f"## Reference Library\n{ref_path.read_text()[:3000]}")
    
    # 3. Claims
    claims_dir = KNOWLEDGE_DIR / "claims"
    if claims_dir.exists():
        claims_text = "## Verified Claims\n"
        for f in sorted(claims_dir.glob("C*.md"))[:15]:
            content = f.read_text()[:500]
            claims_text += f"\n### {f.stem}\n{content}\n"
        knowledge.append(claims_text[:5000])
    
    # 4. AI Research briefs
    ai_dir = KNOWLEDGE_DIR / "ai-research"
    if ai_dir.exists():
        ai_text = "## AI Research Briefs\n"
        for f in sorted(ai_dir.glob("AR-*.md"))[:9]:
            content = f.read_text()[:800]
            ai_text += f"\n### {f.stem}\n{content}\n"
        knowledge.append(ai_text[:8000])
    
    # 5. Select resources (most relevant)
    res_dir = KNOWLEDGE_DIR / "resources"
    if res_dir.exists():
        res_text = "## Resource Highlights\n"
        priority_files = [
            "Vertical-AI-Moats.md", "What-VCs-Miss.md", "Investor-Psychology.md",
            "AI-Product-Pitfalls.md", "Ainary-Competitive-Analysis.md",
            "Founder-Psychology.md", "Fundraising-From-Both-Sides.md"
        ]
        for fname in priority_files:
            fp = res_dir / fname
            if fp.exists():
                res_text += f"\n### {fp.stem}\n{fp.read_text()[:600]}\n"
        knowledge.append(res_text[:5000])
    
    full = "\n\n".join(knowledge)
    return full[:30000]  # Hard cap at 30K chars


def brave_search(query, count=5):
    """Search Brave API for live sources."""
    if not BRAVE_API_KEY:
        return []
    
    try:
        clean_query = re.sub(r'[^\w\s]', '', query)
        url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(clean_query)}&count={count}"
        req = urllib.request.Request(url, headers={
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": BRAVE_API_KEY
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            results = []
            for r in data.get("web", {}).get("results", [])[:count]:
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "snippet": r.get("description", "")[:200]
                })
            return results
    except Exception as e:
        print(f"  Brave search failed: {e}")
        return []


def call_openai(messages, temperature=0.7, max_tokens=8000):
    """Call OpenAI API."""
    if not OPENAI_API_KEY:
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)
    
    payload = json.dumps({
        "model": MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }).encode()
    
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )
    
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"  OpenAI attempt {attempt+1} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(5 * (attempt + 1))
    
    return None


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{report_id} — {title}</title>
<style>
  @page {{ size: A4; margin: 2.5cm 2cm; @bottom-center {{ content: counter(page); font-size: 9px; color: #666; }} }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #1a1a1a; max-width: 210mm; margin: 0 auto; padding: 40px 48px; background: #fff; }}
  h1 {{ font-size: 22pt; font-weight: 700; color: #0a0a0a; margin: 0 0 4px; letter-spacing: -0.5px; }}
  .subtitle {{ font-size: 13pt; color: #444; margin-bottom: 4px; }}
  .meta-line {{ font-size: 9pt; color: #888; margin-bottom: 24px; }}
  h2 {{ font-size: 15pt; font-weight: 700; color: #0a0a0a; margin: 32px 0 12px; padding-bottom: 4px; border-bottom: 2px solid #0a0a0a; }}
  h3 {{ font-size: 12pt; font-weight: 700; color: #222; margin: 20px 0 8px; }}
  p {{ margin: 0 0 10px; }}
  ul, ol {{ margin: 0 0 12px 20px; }}
  li {{ margin-bottom: 4px; }}
  strong {{ font-weight: 700; }}
  table {{ width: 100%; border-collapse: collapse; margin: 12px 0 20px; font-size: 10pt; }}
  th {{ background: #0a0a0a; color: #fff; font-weight: 600; text-align: left; padding: 8px 10px; }}
  td {{ padding: 8px 10px; border-bottom: 1px solid #e0e0e0; }}
  tr:nth-child(even) {{ background: #f8f8f8; }}
  .callout {{ background: #f0f4ff; border-left: 4px solid #0a0a0a; padding: 12px 16px; margin: 16px 0; font-size: 10pt; }}
  .callout-warning {{ background: #fff8f0; border-left-color: #e67e00; }}
  .badge {{ display: inline-block; font-size: 8pt; font-weight: 600; padding: 2px 6px; border-radius: 3px; margin-right: 4px; }}
  .badge-e {{ background: #e8f5e9; color: #2e7d32; }}
  .badge-i {{ background: #e3f2fd; color: #1565c0; }}
  .badge-j {{ background: #fff3e0; color: #e65100; }}
  .badge-a {{ background: #f3e5f5; color: #7b1fa2; }}
  .source-log {{ font-size: 9pt; color: #666; margin-top: 32px; padding-top: 16px; border-top: 1px solid #ddd; }}
  .source-log a {{ color: #1565c0; text-decoration: none; }}
  .transparency {{ background: #fafafa; border: 1px solid #e0e0e0; border-radius: 4px; padding: 16px; margin: 24px 0; font-size: 9.5pt; }}
  .cover {{ text-align: center; margin-bottom: 40px; padding-bottom: 24px; border-bottom: 3px solid #0a0a0a; }}
  .cover .logo {{ font-size: 11pt; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: #0a0a0a; margin-bottom: 32px; }}
  .back-cover {{ margin-top: 48px; padding-top: 24px; border-top: 1px solid #ddd; font-size: 9pt; color: #888; text-align: center; }}
  .back-cover a {{ color: #1565c0; text-decoration: none; }}
  @media print {{ body {{ padding: 0; }} }}
</style>
</head>
<body>

<div class="cover">
  <div class="logo">Ainary Ventures</div>
  <h1>{title}</h1>
  <p class="subtitle">Ainary Research Report {report_id}</p>
  <p class="meta-line">{date} &middot; {audience} &middot; AI Strategy &middot; System Design &middot; Execution &middot; Consultancy &middot; Research</p>
</div>

{body}

<div class="transparency">
  <strong>Transparency Note</strong><br>
  Research Type: Automated synthesis with live web sources and curated knowledge base.<br>
  Data Sources: Brave Search API, Ainary Knowledge Base (27 verified research truths, 14 reference papers, 15 verified claims).<br>
  Labels: <span class="badge badge-e">E</span> Evidenced &nbsp; <span class="badge badge-i">I</span> Interpreted &nbsp; <span class="badge badge-j">J</span> Judged &nbsp; <span class="badge badge-a">A</span> Actionable<br>
  Generated: {timestamp}
</div>

<div class="source-log">
  <strong>Sources</strong><br>
  {sources_html}
</div>

<div class="back-cover">
  <strong>About the Author</strong><br>
  Florian Ziesche — Former CEO 36ZERO Vision (€5M raised, BMW/Siemens/Bosch). AI Trust &amp; Governance.<br>
  <a href="mailto:florian@ainaryventures.com">florian@ainaryventures.com</a> &middot; <a href="https://ainaryventures.com">ainaryventures.com</a><br>
  &copy; 2026 Ainary Ventures
</div>

</body>
</html>"""


REPORT_PROMPT = """You are an elite research analyst at Ainary Ventures. Write a professional research report.

TOPIC: {title}
REPORT ID: {report_id}
TARGET AUDIENCE: {audience}

KNOWLEDGE BASE (verified facts — use these as foundation):
{knowledge}

LIVE SOURCES (from web search — cite with [Source N]):
{sources}

INSTRUCTIONS:
1. Write 2,000-3,000 words. Professional, direct, no filler.
2. Section titles MUST be ARGUMENTS, not categories. "Everybody's Deploying, Nobody's Trusting" not "Market Overview".
3. Use E/I/J/A inline labels: <span class="badge badge-e">E</span> for evidenced facts, <span class="badge badge-i">I</span> for interpretations, <span class="badge badge-j">J</span> for judgments, <span class="badge badge-a">A</span> for actionable recommendations.
4. E labels MUST be >50% of all labels. J labels MUST be <20%.
5. Include at least 1 table and 1 callout box (<div class="callout">).
6. Lead Executive Summary with something an expert DOESN'T already know.
7. End with 3 concrete, actionable recommendations.
8. Cite sources as [Source 1], [Source 2] etc.
9. Output ONLY the HTML body content (everything between <div class="cover"> and the transparency note). No <html>, <head>, <body> tags.

NEVER USE: "landscape", "tapestry", "delve", "synergy", "cutting-edge", "game-changer", "It's worth noting", "In today's world"

FORMAT: Raw HTML (h2, h3, p, ul, table, div.callout, span.badge). No markdown."""


def generate_report(topic, knowledge_base, index, total):
    """Generate a single report."""
    report_id = topic["id"]
    title = topic["title"]
    audience = topic["audience"]
    keywords = topic.get("keywords", [])
    
    print(f"\n[{index+1}/{total}] {report_id}: {title}")
    
    # 1. Web search for live sources
    query = f"{title} {' '.join(keywords[:2])} 2025 2026"
    print(f"  Searching: {query[:60]}...")
    sources = brave_search(query, count=5)
    
    sources_text = ""
    sources_html = ""
    for i, s in enumerate(sources, 1):
        sources_text += f"[Source {i}] {s['title']}: {s['snippet']} (URL: {s['url']})\n"
        sources_html += f'[{i}] <a href="{s["url"]}">{s["title"]}</a><br>\n'
    
    if not sources_text:
        sources_text = "No live sources found. Use knowledge base only."
        sources_html = "Generated from Ainary Knowledge Base.<br>"
    
    # 2. Generate report
    print(f"  Generating with {MODEL}...")
    prompt = REPORT_PROMPT.format(
        title=title,
        report_id=report_id,
        audience=audience,
        knowledge=knowledge_base[:15000],  # Truncate for prompt size
        sources=sources_text
    )
    
    result = call_openai([
        {"role": "system", "content": "You are an elite research analyst. Output only HTML content as instructed."},
        {"role": "user", "content": prompt}
    ], temperature=0.7, max_tokens=6000)
    
    if not result:
        print(f"  FAILED: No response from OpenAI")
        return False
    
    # 3. Build full HTML
    now = datetime.now()
    html = HTML_TEMPLATE.format(
        report_id=report_id,
        title=title,
        date=now.strftime("%B %Y"),
        audience=audience,
        body=result,
        timestamp=now.strftime("%Y-%m-%d %H:%M"),
        sources_html=sources_html
    )
    
    # 4. Save
    filename = f"{report_id.lower()}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:60]}.html"
    output_path = OUTPUT_DIR / filename
    output_path.write_text(html)
    
    size_kb = len(html) / 1024
    print(f"  Saved: {filename} ({size_kb:.0f} KB)")
    return True


def generate_index(topics):
    """Generate index.html listing all reports."""
    rows = ""
    for t in topics:
        filename = f"{t['id'].lower()}-{re.sub(r'[^a-z0-9]+', '-', t['title'].lower()).strip('-')[:60]}.html"
        filepath = OUTPUT_DIR / filename
        if filepath.exists():
            size = filepath.stat().st_size / 1024
            rows += f'<tr><td><a href="{filename}">{t["id"]}</a></td><td><a href="{filename}">{t["title"]}</a></td><td>{t["audience"]}</td><td>{t.get("category","")}</td><td>{size:.0f} KB</td></tr>\n'
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ainary Research Library</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 40px 24px; color: #1a1a1a; }}
  h1 {{ font-size: 28pt; margin-bottom: 8px; }}
  .subtitle {{ color: #666; margin-bottom: 32px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 10pt; }}
  th {{ background: #0a0a0a; color: #fff; padding: 10px; text-align: left; }}
  td {{ padding: 10px; border-bottom: 1px solid #eee; }}
  tr:hover {{ background: #f5f5f5; }}
  a {{ color: #1565c0; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 9pt; color: #888; text-align: center; }}
</style>
</head>
<body>
<h1>Ainary Research Library</h1>
<p class="subtitle">{len([1 for t in topics if (OUTPUT_DIR / f"{t['id'].lower()}-{re.sub(r'[^a-z0-9]+', '-', t['title'].lower()).strip('-')[:60]}.html").exists()])} Reports &middot; AI Trust &middot; Agent Governance &middot; Calibration</p>
<table>
<tr><th>ID</th><th>Title</th><th>Audience</th><th>Category</th><th>Size</th></tr>
{rows}
</table>
<div class="footer">
  &copy; 2026 Ainary Ventures &middot; <a href="mailto:florian@ainaryventures.com">florian@ainaryventures.com</a> &middot; <a href="https://ainaryventures.com">ainaryventures.com</a>
</div>
</body>
</html>"""
    
    (OUTPUT_DIR / "index.html").write_text(html)
    print(f"\nIndex page: reports/index.html")


def main():
    parser = argparse.ArgumentParser(description="Batch Report Generator")
    parser.add_argument("--start", type=int, default=0, help="Start index")
    parser.add_argument("--count", type=int, default=100, help="Number of reports")
    parser.add_argument("--dry-run", action="store_true", help="Print topics only")
    args = parser.parse_args()
    
    # Load topics
    topics = json.loads(TOPICS_FILE.read_text())
    print(f"Loaded {len(topics)} topics")
    
    # Subset
    topics = topics[args.start:args.start + args.count]
    print(f"Generating {len(topics)} reports (start={args.start})")
    
    if args.dry_run:
        for i, t in enumerate(topics):
            print(f"  {i+1}. [{t['id']}] {t['title']} ({t['audience']})")
        return
    
    # Create output dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load knowledge base
    print("Loading knowledge base...")
    knowledge = load_knowledge_base()
    print(f"Knowledge base: {len(knowledge):,} chars")
    
    # Generate reports
    success = 0
    failed = 0
    start_time = time.time()
    
    for i, topic in enumerate(topics):
        try:
            if generate_report(topic, knowledge, i, len(topics)):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1
        
        if i < len(topics) - 1:
            time.sleep(DELAY_BETWEEN_REPORTS)
    
    # Generate index
    all_topics = json.loads(TOPICS_FILE.read_text())
    generate_index(all_topics)
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"DONE: {success} reports generated, {failed} failed")
    print(f"Time: {elapsed/60:.1f} minutes ({elapsed/max(success,1):.1f}s per report)")
    print(f"Output: {OUTPUT_DIR}/")
    print(f"Index:  {OUTPUT_DIR}/index.html")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

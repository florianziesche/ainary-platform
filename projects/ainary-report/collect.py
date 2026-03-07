#!/usr/bin/env python3
"""
Ainary Report — Data Collector
Collects raw intelligence data and outputs JSON for LLM analysis.
Usage: python3 collect.py "BMW Group" [--url https://bmw.de] [--mode dd|pitch|compete|city] [--vs "Audi"]
"""

import sys, os, json, time, argparse
from pathlib import Path

VENV = Path.home() / "ainary-tools"
sys.path.insert(0, str(VENV / "lib/python3.12/site-packages"))

XRAY_DIR = Path(__file__).parent.parent / "xray-intelligence"
sys.path.insert(0, str(XRAY_DIR))

from xray import IntelCollector


def collect(company, url=None, mode="dd", vs=None):
    """Collect raw data and return structured JSON."""
    t0 = time.time()
    print(f"📡 Collecting: {company} (mode={mode})", file=sys.stderr)

    collector = IntelCollector(verbose=True)

    if mode == "city":
        collector.collect_offeneregister(company, limit=300)
    else:
        collector.collect_bundesanzeiger(company)
        collector.collect_offeneregister(company)
        collector.collect_insolvency(company)
        if url:
            import asyncio
            asyncio.run(collector.collect_website(url))

    result = {
        "company": company,
        "mode": mode,
        "collected_at": time.strftime("%Y-%m-%d %H:%M"),
        "duration_sec": round(time.time() - t0, 1),
        "data": {}
    }

    # Bundesanzeiger — keep most relevant content
    ba = collector.data.get("bundesanzeiger", [])
    if ba:
        result["data"]["bundesanzeiger"] = {
            "count": len(ba),
            "reports": [{
                "name": r.get("name", ""),
                "date": r.get("date", ""),
                "type": r.get("type", ""),
                "content": r.get("content", "")[:3000]  # Truncate for LLM context
            } for r in ba[:5]]  # Max 5 reports
        }

    # Handelsregister
    reg = collector.data.get("offeneregister", [])
    if reg:
        # Find best match
        best = None
        for c in reg:
            if company.lower() in c.get("name", "").lower():
                best = c
                break
        if not best and reg:
            best = reg[0]

        result["data"]["handelsregister"] = {
            "total_matches": len(reg),
            "best_match": {
                "name": best.get("name", ""),
                "status": best.get("status", ""),
                "type": best.get("type", ""),
                "address": best.get("address", ""),
                "register": best.get("register", ""),
                "officers": [{
                    "name": o.get("name", str(o)) if isinstance(o, dict) else str(o),
                    "role": o.get("position", o.get("role", "")) if isinstance(o, dict) else ""
                } for o in best.get("officers", [])[:10]]
            } if best else None,
            "all_entities": [{
                "name": c.get("name", ""),
                "status": c.get("status", ""),
                "type": c.get("type", "")
            } for c in reg[:20]]
        }

    # Insolvenzbekanntmachungen
    insol = collector.data.get("insolvency", [])
    result["data"]["insolvency"] = {
        "count": len(insol),
        "proceedings": [{
            "court": i.get("court", ""),
            "date": i.get("date", ""),
            "type": i.get("type", ""),
            "content": i.get("content", "")[:300]
        } for i in insol[:5]]
    }

    # Website
    sites = collector.data.get("websites", {})
    if sites:
        for url_key, site in sites.items():
            result["data"]["website"] = {
                "url": url_key,
                "content_length": site.get("length", 0),
                "content": site.get("content", "")[:4000]
            }

    # Competitor data
    if vs and mode == "compete":
        print(f"\n📡 Collecting competitor: {vs}", file=sys.stderr)
        collector2 = IntelCollector(verbose=True)
        collector2.full_company_scan(vs)
        result["competitor"] = {
            "company": vs,
            "data": collector2.data
        }

    # Timings
    result["timings"] = collector._timings

    return result


def main():
    parser = argparse.ArgumentParser(description="Ainary Report — Data Collector")
    parser.add_argument("company", help="Company or city name")
    parser.add_argument("--url", help="Company website URL")
    parser.add_argument("--mode", default="dd", choices=["dd", "pitch", "compete", "city"])
    parser.add_argument("--vs", help="Competitor for compare mode")
    parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    args = parser.parse_args()

    result = collect(args.company, url=args.url, mode=args.mode, vs=args.vs)

    output = json.dumps(result, indent=2, ensure_ascii=False, default=str)

    if args.output:
        Path(args.output).write_text(output)
        print(f"\n✅ Saved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()

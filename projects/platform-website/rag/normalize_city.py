#!/usr/bin/env python3
"""
Normalize city JSON to canonical schema.
Fixes common agent errors:
- tenant as string → object
- quellenverzeichnis as list of strings → list of objects
- claim_ledger using "status" instead of "eija"
- Missing _meta.source_count
"""

import json, sys, os

def normalize(data, city_slug):
    changed = False

    # 1. tenant: string → object
    if isinstance(data.get("tenant"), str):
        data["tenant"] = {
            "name": f"Kampagnen-Intelligence {data['tenant'].title()}",
            "gemeinde": data["tenant"].title(),
            "typ": "kreisfrei",
            "wahl": {"typ": "OB-Wahl", "datum": "08.03.2026", "stichwahl": "22.03.2026"}
        }
        changed = True
        print(f"  FIXED: tenant string → object")

    # 2. kb: normalize to dict of dicts
    kb = data.get("kb", {})
    if isinstance(kb, list):
        # list of dicts → dict keyed by slugified name
        new_kb = {}
        for item in kb:
            if isinstance(item, dict):
                name = item.get("name", f"candidate-{len(new_kb)}")
                slug = name.lower().replace(" ", "-").replace("ü","ue").replace("ö","oe").replace("ä","ae").replace("ß","ss")
                new_kb[slug] = item
        data["kb"] = new_kb
        changed = True
        print(f"  FIXED: kb list → dict ({len(new_kb)} candidates)")
    elif isinstance(kb, dict):
        # Check if values are lists instead of dicts (bayreuth/rosenheim pattern)
        new_kb = {}
        for key, val in kb.items():
            if isinstance(val, list) and val and isinstance(val[0], dict):
                # list of dicts under key → merge first item
                new_kb[key] = val[0]
                changed = True
            elif isinstance(val, dict):
                new_kb[key] = val
            else:
                new_kb[key] = val
        if changed:
            data["kb"] = new_kb
            print(f"  FIXED: kb values list → dict")

    # 3. quellenverzeichnis: list of strings → list of objects
    sources = data.get("quellenverzeichnis", [])
    if sources and isinstance(sources[0], str):
        data["quellenverzeichnis"] = [
            {"id": f"S-{i+1:02d}", "name": url.split("/")[2] if "/" in url else url, "url": url, "accessDate": "2026-02-28", "type": "media"}
            for i, url in enumerate(sources) if url
        ]
        changed = True
        print(f"  FIXED: quellenverzeichnis strings → objects ({len(data['quellenverzeichnis'])} sources)")

    # 3. claim_ledger: "status" → "eija"
    claims = data.get("claim_ledger", [])
    for claim in claims:
        if "status" in claim and "eija" not in claim:
            claim["eija"] = claim.pop("status")
            changed = True
        # Also fix "quellen" → "source"
        if "quellen" in claim and "source" not in claim:
            q = claim.pop("quellen")
            claim["source"] = q[0] if isinstance(q, list) and q else q
            changed = True
        # Add missing id
        if "id" not in claim:
            claim["id"] = f"CL-{claims.index(claim)+1:03d}"
            changed = True
        # Add missing confidence as int
        if isinstance(claim.get("confidence"), float):
            claim["confidence"] = int(claim["confidence"] * 100)
            changed = True

    # 4. _meta.source_count
    meta = data.get("_meta", {})
    actual_count = len(data.get("quellenverzeichnis", []))
    if meta.get("source_count", 0) != actual_count:
        meta["source_count"] = actual_count
        data["_meta"] = meta
        changed = True

    if changed:
        print(f"  NORMALIZED: {city_slug}")
    else:
        print(f"  OK: {city_slug} (no changes needed)")

    return data, changed


def normalize_file(city_slug, data_dir="data/cities"):
    path = os.path.join(data_dir, f"{city_slug}.json")
    with open(path) as f:
        data = json.load(f)

    data, changed = normalize(data, city_slug)

    if changed:
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  WRITTEN: {path}")

    return changed


def normalize_all(data_dir="data/cities"):
    fixed = 0
    for f in sorted(os.listdir(data_dir)):
        if not f.endswith('.json') or f == 'internal.json':
            continue
        slug = f.replace('.json', '')
        if normalize_file(slug, data_dir):
            fixed += 1
    print(f"\n{fixed} files normalized.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        normalize_all()
    elif len(sys.argv) > 1:
        normalize_file(sys.argv[1])
    else:
        print("Usage: python3 normalize_city.py <slug> | --all")

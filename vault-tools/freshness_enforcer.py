#!/usr/bin/env python3
"""
Freshness Enforcer — Track and enforce knowledge expiry.

Usage:
    python freshness_enforcer.py --report         # Show freshness status (default)
    python freshness_enforcer.py --degrade        # Degrade STALE notes by one tier
    python freshness_enforcer.py --json           # Output JSON

Status:
    FRESH: More than 30 days until expiry
    AGING: Within 30 days of expiry
    STALE: Past expiry date

Tier degradation: CORE → KNOWLEDGE → OPERATIONAL → EPHEMERAL
"""

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

TIER_DEGRADATION = {
    "CORE": "KNOWLEDGE",
    "KNOWLEDGE": "OPERATIONAL",
    "OPERATIONAL": "EPHEMERAL",
    "EPHEMERAL": "EPHEMERAL",  # Can't degrade further
}

AGING_THRESHOLD_DAYS = 30


def parse_frontmatter(content: str) -> Tuple[Optional[Dict], str]:
    """Parse frontmatter and return (dict, body)."""
    if not content.startswith("---\n"):
        return None, content
    
    match = re.match(r'^---\n(.*?\n)---\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content
    
    fm_block = match.group(1)
    body = match.group(2)
    
    fm_dict = {}
    for line in fm_block.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            fm_dict[key.strip()] = val.strip()
    
    return fm_dict, body


def build_frontmatter(fm_dict: Dict) -> str:
    """Convert frontmatter dict to YAML block."""
    lines = ["---"]
    for k, v in fm_dict.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date from string (YYYY-MM-DD format)."""
    if date_str.lower() in ["none", "null", ""]:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None


def get_freshness_status(expires: Optional[datetime], now: datetime) -> str:
    """Determine freshness status based on expiry date."""
    if expires is None:
        return "FRESH"  # No expiry = always fresh
    
    days_until_expiry = (expires - now).days
    
    if days_until_expiry < 0:
        return "STALE"
    elif days_until_expiry <= AGING_THRESHOLD_DAYS:
        return "AGING"
    else:
        return "FRESH"


def process_file(path: Path, now: datetime, degrade: bool = False) -> Optional[Dict]:
    """
    Process a single file:
    - Check expiry status
    - Optionally degrade tier if stale
    Returns status dict or None if no expiry field.
    """
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return {"path": str(path), "status": "ERROR", "error": str(e)}
    
    fm, body = parse_frontmatter(content)
    
    if fm is None or "expires" not in fm:
        return None  # Skip files without expiry
    
    tier = fm.get("tier", "OPERATIONAL")
    expires_str = fm.get("expires")
    expires_date = parse_date(expires_str)
    
    status = get_freshness_status(expires_date, now)
    
    result = {
        "path": str(path.relative_to(VAULT)),
        "tier": tier,
        "expires": expires_str,
        "status": status,
    }
    
    if expires_date:
        days_until = (expires_date - now).days
        result["days_until_expiry"] = days_until
    
    # Degrade if requested and stale
    if degrade and status == "STALE":
        new_tier = TIER_DEGRADATION[tier]
        if new_tier != tier:
            fm["tier"] = new_tier
            new_content = build_frontmatter(fm) + body
            try:
                path.write_text(new_content, encoding="utf-8")
                result["action"] = "degraded"
                result["new_tier"] = new_tier
            except Exception as e:
                result["action"] = "error"
                result["error"] = str(e)
        else:
            result["action"] = "already_lowest_tier"
    
    return result


def format_table(results: List[Dict]) -> str:
    """Format results as a human-readable table."""
    lines = []
    lines.append(f"{'Status':<10} {'Tier':<12} {'Days Left':<12} {'Path':<50}")
    lines.append("-" * 90)
    
    for r in results:
        status = r["status"]
        tier = r.get("new_tier", r["tier"])
        days = r.get("days_until_expiry", "N/A")
        path = r["path"]
        
        if days != "N/A":
            if days < 0:
                days_str = f"{abs(days)} overdue"
            else:
                days_str = str(days)
        else:
            days_str = "∞"
        
        # Add action indicator if degraded
        if r.get("action") == "degraded":
            path = f"{path} [DEGRADED: {r['tier']} → {tier}]"
        
        lines.append(f"{status:<10} {tier:<12} {days_str:<12} {path:<50}")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Track and enforce knowledge freshness")
    parser.add_argument("--report", action="store_true", help="Show freshness report (default)")
    parser.add_argument("--degrade", action="store_true", help="Degrade STALE notes by one tier")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--status", choices=["FRESH", "AGING", "STALE"], help="Filter by status")
    args = parser.parse_args()
    
    # Default to report if no action specified
    if not args.degrade:
        args.report = True
    
    # Find all markdown files
    files = list(VAULT.rglob("*.md"))
    files = [f for f in files if ".obsidian" not in str(f) and "System_OS_BACKUP" not in str(f)]
    
    now = datetime.now()
    
    if not args.json and args.degrade:
        print(f"[DEGRADE MODE] Processing {len(files)} files...")
    elif not args.json:
        print(f"Processing {len(files)} files...")
    
    results = []
    for f in files:
        result = process_file(f, now, degrade=args.degrade)
        if result:
            results.append(result)
    
    # Filter by status if requested
    if args.status:
        results = [r for r in results if r["status"] == args.status]
    
    # Count by status
    status_counts = defaultdict(int)
    tier_counts = defaultdict(lambda: defaultdict(int))
    
    for r in results:
        status_counts[r["status"]] += 1
        tier = r.get("new_tier", r["tier"])
        tier_counts[r["status"]][tier] += 1
    
    # Sort results: STALE first, then AGING, then FRESH
    status_order = {"STALE": 0, "AGING": 1, "FRESH": 2}
    results.sort(key=lambda r: (
        status_order[r["status"]],
        r.get("days_until_expiry", 999999)
    ))
    
    # Output
    if args.json:
        output = {
            "scanned_at": now.isoformat(),
            "total_files_with_expiry": len(results),
            "status_counts": dict(status_counts),
            "tier_breakdown": {status: dict(tiers) for status, tiers in tier_counts.items()},
            "files": results
        }
        print(json.dumps(output, indent=2))
    else:
        # Human-readable output
        print(f"\n{'='*90}")
        print("FRESHNESS REPORT")
        print(f"{'='*90}\n")
        
        print(f"Scanned: {len(files)} files")
        print(f"With expiry field: {len(results)}\n")
        
        print("Status breakdown:")
        for status in ["STALE", "AGING", "FRESH"]:
            count = status_counts[status]
            if count > 0:
                print(f"  {status}: {count}")
                for tier, tier_count in tier_counts[status].items():
                    print(f"    [{tier}]: {tier_count}")
        
        print(f"\n{format_table(results)}")
        
        if args.degrade:
            degraded = [r for r in results if r.get("action") == "degraded"]
            print(f"\n✓ Degraded {len(degraded)} files")
        elif status_counts["STALE"] > 0:
            print(f"\n⚠️  {status_counts['STALE']} STALE files detected. Run with --degrade to auto-fix.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Frontmatter Tier Tagger — Auto-assign tier + expiry to vault notes.

Usage:
    python tag_tiers.py --dry-run    # Show what would change (default)
    python tag_tiers.py --apply      # Write changes to files

Tiers: CORE (2x) > KNOWLEDGE (1.5x) > OPERATIONAL (1x) > EPHEMERAL (0.5x)
Expiry: core=none, knowledge=1year, operational=6months, ephemeral=90days
"""

import argparse
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Tuple

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

# Tier assignment rules (order matters: first match wins)
TIER_RULES = [
    # CORE: Identity, decisions, truths
    (lambda p: any(n in p.name for n in ["verified-truths.md", "decisions.md", "SOUL.md", "AGENTS.md", "MASTER.md"]), "CORE"),
    (lambda p: "70_Mia" in str(p) and p.name in ["USER.md", "MEMORY-INDEX.md"], "CORE"),
    
    # KNOWLEDGE: Resources, patterns, connections
    (lambda p: "70_Mia/knowledge/" in str(p), "KNOWLEDGE"),
    (lambda p: "60_Resources/" in str(p), "KNOWLEDGE"),
    (lambda p: p.name in ["connections.md", "patterns.md"], "KNOWLEDGE"),
    
    # OPERATIONAL: Projects, people, areas
    (lambda p: p.name in ["projects.md", "people.md"], "OPERATIONAL"),
    (lambda p: "20_Areas/" in str(p), "OPERATIONAL"),
    (lambda p: "10_Projects/" in str(p), "OPERATIONAL"),
    (lambda p: "30_People/" in str(p), "OPERATIONAL"),
    
    # EPHEMERAL: Daily notes, inbox, triage
    (lambda p: "70_Mia/daily/" in str(p) or "02_Daily/" in str(p), "EPHEMERAL"),
    (lambda p: "00_Inbox/" in str(p), "EPHEMERAL"),
    (lambda p: "70_Mia/triage/" in str(p), "EPHEMERAL"),
    (lambda p: "90_Archive/" in str(p), "EPHEMERAL"),
]

EXPIRY_DELTA = {
    "CORE": None,  # No expiry
    "KNOWLEDGE": timedelta(days=365),
    "OPERATIONAL": timedelta(days=182),
    "EPHEMERAL": timedelta(days=90),
}


def detect_tier(path: Path) -> str:
    """Detect tier based on path rules. Default: OPERATIONAL."""
    for rule_fn, tier in TIER_RULES:
        if rule_fn(path):
            return tier
    return "OPERATIONAL"


def parse_frontmatter(content: str) -> Tuple[Optional[dict], str]:
    """
    Parse YAML frontmatter from markdown content.
    Returns (frontmatter_dict, body_content) or (None, content) if no frontmatter.
    Uses simple regex, no YAML library.
    """
    if not content.startswith("---\n"):
        return None, content
    
    match = re.match(r'^---\n(.*?\n)---\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content
    
    fm_block = match.group(1)
    body = match.group(2)
    
    # Parse key: value pairs (simple, doesn't handle nested structures)
    fm_dict = {}
    for line in fm_block.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            fm_dict[key.strip()] = val.strip()
    
    return fm_dict, body


def build_frontmatter(fm_dict: dict) -> str:
    """Convert frontmatter dict to YAML block."""
    lines = ["---"]
    for k, v in fm_dict.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def calculate_expiry(tier: str, mtime: float) -> Optional[str]:
    """Calculate expiry date from file mtime and tier."""
    delta = EXPIRY_DELTA[tier]
    if delta is None:
        return "none"
    
    mod_date = datetime.fromtimestamp(mtime)
    expiry_date = mod_date + delta
    return expiry_date.strftime("%Y-%m-%d")


def process_file(path: Path, apply: bool = False) -> dict:
    """
    Process a single markdown file:
    - Detect tier
    - Add/update tier and expires fields in frontmatter
    - Return change info dict
    """
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return {"path": str(path), "status": "error", "error": str(e)}
    
    # Skip empty files
    if not content.strip():
        return {"path": str(path), "status": "skipped", "reason": "empty"}
    
    tier = detect_tier(path)
    mtime = path.stat().st_mtime
    expires = calculate_expiry(tier, mtime)
    
    fm, body = parse_frontmatter(content)
    
    # Check if changes needed
    if fm is not None:
        # Has frontmatter
        current_tier = fm.get("tier")
        current_expires = fm.get("expires")
        
        if current_tier == tier and current_expires == expires:
            return {"path": str(path), "status": "unchanged", "tier": tier}
        
        # Update frontmatter
        fm["tier"] = tier
        fm["expires"] = expires
        new_content = build_frontmatter(fm) + body
        action = "updated"
    else:
        # No frontmatter — create it
        fm = {"tier": tier, "expires": expires}
        new_content = build_frontmatter(fm) + content
        action = "added"
    
    if apply:
        try:
            path.write_text(new_content, encoding="utf-8")
            status = "written"
        except Exception as e:
            return {"path": str(path), "status": "error", "error": str(e)}
    else:
        status = "preview"
    
    return {
        "path": str(path.relative_to(VAULT)),
        "status": status,
        "action": action,
        "tier": tier,
        "expires": expires,
    }


def main():
    parser = argparse.ArgumentParser(description="Tag vault files with tier and expiry frontmatter")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--path", help="Process single file or directory (default: entire vault)")
    args = parser.parse_args()
    
    if args.path:
        target = Path(args.path).expanduser()
        if not target.exists():
            print(f"Error: Path not found: {target}")
            return
        if target.is_file():
            files = [target]
        else:
            files = list(target.rglob("*.md"))
    else:
        files = list(VAULT.rglob("*.md"))
    
    # Filter out system files
    files = [f for f in files if ".obsidian" not in str(f) and "System_OS_BACKUP" not in str(f)]
    
    print(f"{'[DRY RUN]' if not args.apply else '[APPLY]'} Processing {len(files)} files...\n")
    
    results = []
    tier_counts = {"CORE": 0, "KNOWLEDGE": 0, "OPERATIONAL": 0, "EPHEMERAL": 0}
    action_counts = {"added": 0, "updated": 0, "unchanged": 0, "error": 0, "skipped": 0}
    
    for f in files:
        result = process_file(f, apply=args.apply)
        results.append(result)
        
        tier = result.get("tier")
        if tier:
            tier_counts[tier] += 1
        
        status = result.get("status")
        action = result.get("action", status)
        if action in action_counts:
            action_counts[action] += 1
    
    # Print sample changes
    changed = [r for r in results if r.get("action") in ["added", "updated"]]
    if changed:
        print(f"Sample changes (showing first 20 of {len(changed)}):")
        for r in changed[:20]:
            print(f"  [{r['action'].upper()}] {r['path']}")
            print(f"    → tier: {r['tier']}, expires: {r['expires']}")
        print()
    
    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(files)}")
    print(f"\nActions:")
    for action, count in action_counts.items():
        if count > 0:
            print(f"  {action}: {count}")
    print(f"\nTier distribution:")
    for tier, count in tier_counts.items():
        print(f"  {tier}: {count}")
    
    if not args.apply and changed:
        print(f"\n⚠️  This was a DRY RUN. Use --apply to write changes.")


if __name__ == "__main__":
    main()

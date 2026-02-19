#!/usr/bin/env python3
"""
Contradiction Detector — Find conflicts between notes across tiers.

Usage:
    python conflict_resolver.py "claim or query"
    python conflict_resolver.py --scan  # Scan CRTs against vault

Detects contradictions using simple heuristics:
- Same entity/topic mentioned with different numbers/claims
- Notes from different tiers with conflicting info (higher tier wins)
"""

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"
WORKSPACE = Path.home() / ".openclaw" / "workspace"
CRT_PATH = WORKSPACE / "research-base" / "compounding-research-truths.json"

TIER_RANK = {"CORE": 4, "KNOWLEDGE": 3, "OPERATIONAL": 2, "EPHEMERAL": 1}


def tokenize(text: str) -> List[str]:
    """Simple tokenizer: lowercase, alphanumeric only."""
    return re.findall(r'[a-z0-9]+', text.lower())


def extract_numbers(text: str) -> List[Tuple[str, str]]:
    """Extract numbers with context (word before + number + word after)."""
    numbers = []
    # Match patterns like "ECE from 42% to 27.3%" or "85% accuracy"
    patterns = [
        r'(\w+)\s+(\d+\.?\d*%)',  # "ECE 42%"
        r'(\w+)\s+of\s+(\d+\.?\d*)',  # "sample of 100"
        r'(\d+\.?\d*%)\s+(\w+)',  # "42% accuracy"
    ]
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for m in matches:
            numbers.append((m.group(0), m.group(1) + " " + m.group(2)))
    return numbers


def get_frontmatter_tier(content: str) -> str:
    """Extract tier from frontmatter, default to OPERATIONAL."""
    if content.startswith("---\n"):
        match = re.match(r'^---\n(.*?\n)---\n', content, re.DOTALL)
        if match:
            fm_block = match.group(1)
            for line in fm_block.split("\n"):
                if line.strip().startswith("tier:"):
                    return line.split(":", 1)[1].strip()
    return "OPERATIONAL"


def build_tfidf_index(files: List[Path]) -> Tuple[Dict, List, Dict]:
    """Build TF-IDF index for files."""
    docs = []
    doc_tiers = {}
    
    for f in files:
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
            tier = get_frontmatter_tier(content)
            tokens = tokenize(content)
            docs.append((str(f.relative_to(VAULT)), tokens, content))
            doc_tiers[str(f.relative_to(VAULT))] = tier
        except:
            continue
    
    # Calculate IDF
    df = Counter()
    for _, tokens, _ in docs:
        df.update(set(tokens))
    
    n = len(docs)
    idf = {term: math.log(n / (count + 1)) for term, count in df.items()}
    
    # Calculate TF for each doc
    tf_docs = []
    for path, tokens, content in docs:
        tf = Counter(tokens)
        total = len(tokens)
        tf_normalized = {term: count / total for term, count in tf.items()}
        tf_docs.append((path, tf_normalized, content))
    
    return idf, tf_docs, doc_tiers


def search_vault(query: str, idf: Dict, tf_docs: List, doc_tiers: Dict, top_k: int = 10) -> List[Tuple[str, float, str, str]]:
    """Search vault using TF-IDF similarity."""
    query_tokens = tokenize(query)
    query_tf = Counter(query_tokens)
    query_tf_norm = {term: count / len(query_tokens) for term, count in query_tf.items()}
    
    scores = []
    for path, tf, content in tf_docs:
        score = 0.0
        for term in query_tf_norm:
            if term in tf:
                score += query_tf_norm[term] * tf[term] * idf.get(term, 0)
        
        if score > 0:
            tier = doc_tiers.get(path, "OPERATIONAL")
            # Boost by tier rank
            boosted_score = score * TIER_RANK[tier]
            scores.append((path, boosted_score, tier, content))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]


def detect_conflicts(results: List[Tuple[str, float, str, str]], query: str) -> List[Dict]:
    """Detect contradictions in search results."""
    conflicts = []
    
    # Group results by tier
    by_tier = defaultdict(list)
    for path, score, tier, content in results:
        by_tier[tier].append((path, content))
    
    # Extract numbers from each result
    all_numbers = {}
    for path, score, tier, content in results:
        numbers = extract_numbers(content[:1000])  # First 1000 chars
        all_numbers[path] = (tier, numbers)
    
    # Find contradictions: same context, different numbers
    contexts_seen = defaultdict(list)
    for path, (tier, numbers) in all_numbers.items():
        for full_match, context in numbers:
            # Normalize context (remove the number)
            context_norm = re.sub(r'\d+\.?\d*%?', 'X', context).lower()
            contexts_seen[context_norm].append((path, tier, full_match))
    
    # Flag conflicts where same context has different values
    for context, matches in contexts_seen.items():
        if len(matches) > 1:
            # Extract unique values
            unique_values = set(m[2] for m in matches)
            if len(unique_values) > 1:
                # Conflict detected
                tiers_involved = set(m[1] for m in matches)
                if len(tiers_involved) > 1:
                    # Cross-tier conflict
                    highest_tier = max(tiers_involved, key=lambda t: TIER_RANK[t])
                    conflicts.append({
                        "context": context,
                        "values": list(unique_values),
                        "files": [{"path": m[0], "tier": m[1], "value": m[2]} for m in matches],
                        "winner_tier": highest_tier,
                        "recommendation": f"Trust {highest_tier} tier value"
                    })
    
    return conflicts


def scan_crts_against_vault(idf: Dict, tf_docs: List, doc_tiers: Dict) -> List[Dict]:
    """Scan all CRTs against vault for contradictions."""
    if not CRT_PATH.exists():
        print(f"CRT file not found: {CRT_PATH}")
        return []
    
    crts = json.loads(CRT_PATH.read_text())["truths"]
    all_conflicts = []
    
    print(f"Scanning {len(crts)} CRTs against vault...\n")
    
    for crt in crts:
        claim = crt["claim"]
        results = search_vault(claim, idf, tf_docs, doc_tiers, top_k=5)
        conflicts = detect_conflicts(results, claim)
        
        if conflicts:
            print(f"⚠️  CRT {crt['id']}: {len(conflicts)} conflict(s) found")
            all_conflicts.append({
                "crt_id": crt["id"],
                "crt_claim": claim,
                "conflicts": conflicts
            })
    
    return all_conflicts


def main():
    parser = argparse.ArgumentParser(description="Detect contradictions in vault notes")
    parser.add_argument("query", nargs="?", help="Claim or query to check")
    parser.add_argument("--scan", action="store_true", help="Scan all CRTs against vault")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    args = parser.parse_args()
    
    if not args.query and not args.scan:
        parser.print_help()
        return
    
    # Build index
    files = list(VAULT.rglob("*.md"))
    files = [f for f in files if ".obsidian" not in str(f) and "System_OS_BACKUP" not in str(f)]
    
    if not args.json:
        print(f"Indexing {len(files)} files...")
    
    idf, tf_docs, doc_tiers = build_tfidf_index(files)
    
    if args.scan:
        # Scan CRTs
        conflicts = scan_crts_against_vault(idf, tf_docs, doc_tiers)
        
        if args.json:
            print(json.dumps({"scanned_at": datetime.now().isoformat(), "conflicts": conflicts}, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"SCAN COMPLETE: {len(conflicts)} CRTs with conflicts")
            print(f"{'='*60}")
    else:
        # Single query
        results = search_vault(args.query, idf, tf_docs, doc_tiers, top_k=10)
        conflicts = detect_conflicts(results, args.query)
        
        output = {
            "query": args.query,
            "results_count": len(results),
            "conflicts_found": len(conflicts),
            "top_results": [
                {"path": r[0], "score": r[1], "tier": r[2]}
                for r in results
            ],
            "conflicts": conflicts
        }
        
        if args.json:
            print(json.dumps(output, indent=2))
        else:
            print(f"\nQuery: {args.query}")
            print(f"Found {len(results)} related notes\n")
            
            print("Top results:")
            for path, score, tier, _ in results[:5]:
                print(f"  [{tier}] {path} (score: {score:.2f})")
            
            if conflicts:
                print(f"\n⚠️  {len(conflicts)} conflict(s) detected:\n")
                for c in conflicts:
                    print(f"  Context: {c['context']}")
                    print(f"  Conflicting values: {', '.join(c['values'])}")
                    print(f"  Files involved:")
                    for f in c['files']:
                        print(f"    [{f['tier']}] {f['path']}: {f['value']}")
                    print(f"  → Recommendation: {c['recommendation']}\n")
            else:
                print("\n✓ No contradictions detected")


if __name__ == "__main__":
    main()

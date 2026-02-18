#!/usr/bin/env python3
"""
Consolidation Engine: Platform Findings → Retrieval-optimized Domain Files.

Reads all alive findings from Platform API, groups by research_line,
generates prose-style domain files optimized for memory_search retrieval.

Usage: python3 consolidate-findings.py [--api http://localhost:8080]
"""

import json
import os
import sys
import http.client
from datetime import datetime
from collections import defaultdict

API_HOST = "localhost"
API_PORT = 8080
MEMORY_DIR = os.path.expanduser("~/.openclaw/workspace/memory/semantic")

def fetch_findings(host, port):
    """Fetch all alive findings from Platform API."""
    conn = http.client.HTTPConnection(host, port, timeout=10)
    try:
        conn.request("GET", "/api/findings?status=alive")
        resp = conn.getresponse()
        if resp.status != 200:
            print(f"Error: API returned {resp.status}", file=sys.stderr)
            return None
        return json.loads(resp.read())
    except Exception as e:
        print(f"Error connecting to Platform API: {e}", file=sys.stderr)
        return None
    finally:
        conn.close()

def fetch_dead_findings(host, port):
    """Fetch dead findings for 'killed' section."""
    conn = http.client.HTTPConnection(host, port, timeout=10)
    try:
        conn.request("GET", "/api/findings?status=dead")
        resp = conn.getresponse()
        if resp.status == 200:
            return json.loads(resp.read())
        return []
    except:
        return []
    finally:
        conn.close()

def cluster_by_tags(findings, min_shared=2, min_cluster=3):
    """Detect emergent clusters (Community Nodes) via shared tags."""
    from itertools import combinations
    tag_groups = defaultdict(list)
    for f in findings:
        tags = f.get('tags', [])
        if isinstance(tags, str):
            tags = json.loads(tags)
        for t in tags:
            tag_groups[t].append(f['id'])
    
    clusters = []
    # Find tag pairs that appear together in ≥3 findings
    tag_list = list(tag_groups.keys())
    for t1, t2 in combinations(tag_list, 2):
        shared = set(tag_groups[t1]) & set(tag_groups[t2])
        if len(shared) >= min_cluster:
            clusters.append({
                'tags': [t1, t2],
                'finding_ids': list(shared),
                'count': len(shared)
            })
    
    return sorted(clusters, key=lambda c: -c['count'])[:5]

def generate_domain_file(research_line, findings, dead_findings, clusters):
    """Generate a retrieval-optimized markdown file for a research line."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    high_conf = [f for f in findings if f['confidence'] >= 0.80]
    medium_conf = [f for f in findings if 0.50 <= f['confidence'] < 0.80]
    low_conf = [f for f in findings if f['confidence'] < 0.50]
    hypotheses = [f for f in findings if any(t in (f.get('tags') or []) for t in ['hypothesis'])]
    verified = [f for f in findings if f.get('verified')]
    
    avg_conf = sum(f['confidence'] for f in findings) / len(findings) if findings else 0
    
    lines = []
    lines.append(f"# {research_line.replace('-', ' ').title()} — Domain Knowledge")
    lines.append(f"*Auto-consolidated: {now} | {len(findings)} findings | avg conf: {avg_conf:.0%} | {len(verified)} verified*")
    lines.append("")
    
    # Core claims as prose (retrieval-optimized)
    if high_conf:
        lines.append("## Verified Claims (conf ≥80%)")
        lines.append("")
        for f in sorted(high_conf, key=lambda x: -x['confidence']):
            tags = f.get('tags', [])
            if isinstance(tags, str):
                tags = json.loads(tags)
            tag_str = ", ".join(t for t in tags if t not in ['claim', 'obsidian_import', 'hypothesis'])
            source = f.get('source_detail') or f.get('source_type') or ''
            verified_mark = " ✓" if f.get('verified') else ""
            lines.append(f"**{f['id']}** [{f['confidence']:.0%}{verified_mark}]: {f['claim']}")
            if source:
                lines.append(f"Source: {source}")
            if tag_str:
                lines.append(f"Tags: {tag_str}")
            lines.append("")
    
    # Emergent clusters
    relevant_clusters = [c for c in clusters if any(fid in [f['id'] for f in findings] for fid in c['finding_ids'])]
    if relevant_clusters:
        lines.append("## Emergent Patterns")
        lines.append("")
        for c in relevant_clusters[:3]:
            cluster_findings = [f for f in findings if f['id'] in c['finding_ids']]
            claims = "; ".join(f['claim'][:60] for f in cluster_findings[:3])
            lines.append(f"**{' × '.join(c['tags'])}** ({c['count']} findings): {claims}")
            lines.append("")
    
    # Hypotheses
    hypos = [f for f in findings if 'hypothesis' in (f.get('tags') or [])]
    if hypos:
        lines.append("## Active Hypotheses")
        lines.append("")
        for f in hypos:
            status_mark = "🔴" if f.get('status') == 'dead' else "🟡"
            lines.append(f"{status_mark} **{f['id']}** [{f['confidence']:.0%}]: {f['claim']}")
            if f.get('context'):
                lines.append(f"  {f['context'][:100]}")
            lines.append("")
    
    # Medium confidence (brief)
    if medium_conf:
        non_hypo = [f for f in medium_conf if 'hypothesis' not in (f.get('tags') or [])]
        if non_hypo:
            lines.append("## Developing (50-80% confidence)")
            lines.append("")
            for f in non_hypo:
                lines.append(f"- {f['id']} [{f['confidence']:.0%}]: {f['claim'][:80]}")
            lines.append("")
    
    # Dead findings (brief)
    dead_in_line = [f for f in dead_findings if f.get('research_line') == research_line]
    if dead_in_line:
        lines.append("## Dead Findings")
        lines.append("")
        for f in dead_in_line:
            lines.append(f"- ~~{f['id']}~~: {f['claim'][:60]} — killed: {f.get('killed_by', '?')[:60]}")
        lines.append("")
    
    return "\n".join(lines)

def main():
    # Parse args
    host, port = API_HOST, API_PORT
    for i, arg in enumerate(sys.argv):
        if arg == "--api" and i+1 < len(sys.argv):
            url = sys.argv[i+1].replace("http://", "")
            if ":" in url:
                host, port = url.split(":")
                port = int(port)
    
    # Fetch
    print(f"Fetching findings from {host}:{port}...")
    findings = fetch_findings(host, port)
    if findings is None:
        print("FAILED: Could not reach Platform API. Memory files unchanged.", file=sys.stderr)
        sys.exit(1)
    
    dead = fetch_dead_findings(host, port)
    print(f"Found {len(findings)} alive, {len(dead)} dead findings")
    
    # Group by research_line
    by_line = defaultdict(list)
    for f in findings:
        tags = f.get('tags', [])
        if isinstance(tags, str):
            f['tags'] = json.loads(tags)
        line = f.get('research_line') or 'uncategorized'
        by_line[line].append(f)
    
    # Detect clusters
    clusters = cluster_by_tags(findings)
    if clusters:
        print(f"Detected {len(clusters)} emergent clusters")
    
    # Generate files
    os.makedirs(MEMORY_DIR, exist_ok=True)
    
    for line, line_findings in by_line.items():
        if not line_findings:
            continue
        content = generate_domain_file(line, line_findings, dead, clusters)
        filename = f"{line}.md"
        filepath = os.path.join(MEMORY_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  → {filename} ({len(line_findings)} findings)")
    
    # Write summary
    summary_path = os.path.join(MEMORY_DIR, "_index.md")
    with open(summary_path, 'w') as f:
        f.write(f"# Semantic Memory Index\n")
        f.write(f"*Last consolidated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        for line, line_findings in sorted(by_line.items()):
            avg = sum(x['confidence'] for x in line_findings) / len(line_findings)
            verified = sum(1 for x in line_findings if x.get('verified'))
            f.write(f"- **{line}**: {len(line_findings)} findings, avg {avg:.0%}, {verified} verified\n")
        if clusters:
            f.write(f"\n## Emergent Clusters\n")
            for c in clusters[:5]:
                f.write(f"- {' × '.join(c['tags'])}: {c['count']} findings\n")
    
    print(f"\nConsolidation complete. {len(by_line)} domain files written to {MEMORY_DIR}/")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
source_linker.py — Adds clickable deep links to source citations in reports.

Uses Chrome Text Fragments (RFC: https://wicg.github.io/scroll-to-text-fragment/)
to link directly to the exact quote in the source document.

Input: final-report.md + evidence-extracted.json
Output: final-report-linked.md with [S1, ¶2] → URL#:~:text=exact%20quote

Usage:
    python3 source_linker.py <pipeline-dir>
"""

import json
import re
import urllib.parse
from pathlib import Path


def load_evidence(pipeline_dir: Path) -> dict:
    """Load evidence-extracted.json and index by source ID."""
    evidence_path = pipeline_dir / "evidence-extracted.json"
    if not evidence_path.exists():
        return {}
    data = json.loads(evidence_path.read_text())
    if isinstance(data, list):
        return {e.get("id", f"S{i}"): e for i, e in enumerate(data, 1)}
    return {}


def make_text_fragment(quote: str, max_words: int = 8) -> str:
    """Create a Chrome Text Fragment from a quote."""
    words = quote.strip().split()[:max_words]
    text = " ".join(words)
    return urllib.parse.quote(text)


def create_deep_link(url: str, quote: str) -> str:
    """Create URL with text fragment for direct quote linking."""
    if not url or not quote:
        return url or ""
    fragment = make_text_fragment(quote)
    separator = "#" if "#" not in url else "&"
    return f"{url}#:~:text={fragment}"


def link_sources_in_report(report_text: str, evidence: dict) -> str:
    """Replace [S1] references with clickable deep links in markdown."""
    def replace_ref(match):
        ref_id = match.group(1)  # e.g., "S1"
        source = evidence.get(ref_id)
        if not source:
            return match.group(0)  # Keep original if no evidence

        url = source.get("url", "")
        claims = source.get("claims", [])
        title = source.get("title", ref_id)

        # Use first claim as quote for text fragment
        if claims and url:
            quote = claims[0] if isinstance(claims[0], str) else str(claims[0])
            deep_url = create_deep_link(url, quote)
            return f"[{ref_id}]({deep_url} \"{title}\")"
        elif url:
            return f"[{ref_id}]({url} \"{title}\")"
        return match.group(0)

    # Match [S1], [S2], etc. but not already linked
    linked = re.sub(r'(?<!\()\[S(\d+)\](?!\()', lambda m: replace_ref(type('M', (), {'group': lambda s, i=0: f'S{m.group(1)}' if i == 1 else m.group(0)})()),
                    report_text)

    # Simpler approach: match \[S\d+\] not inside markdown links
    result = []
    i = 0
    pattern = re.compile(r'\[S(\d+)\]')
    for match in pattern.finditer(report_text):
        sid = f"S{match.group(1)}"
        source = evidence.get(sid)
        if source and source.get("url"):
            url = source["url"]
            title = source.get("title", sid)
            claims = source.get("claims", [])
            if claims:
                quote = claims[0] if isinstance(claims[0], str) else ""
                deep_url = create_deep_link(url, quote)
            else:
                deep_url = url
            result.append(report_text[i:match.start()])
            result.append(f"[{sid}]({deep_url} \"{title}\")")
        else:
            result.append(report_text[i:match.end()])
        i = match.end()
    result.append(report_text[i:])

    return "".join(result)


def generate_source_table_html(evidence: dict) -> str:
    """Generate HTML source log table with deep links."""
    rows = []
    for sid, source in sorted(evidence.items()):
        url = source.get("url", "")
        title = source.get("title", "Unknown")
        stype = source.get("type", "Unknown")
        strength = source.get("strength", "Unknown")
        claims = source.get("claims", [])
        key_claim = claims[0] if claims else "—"
        if isinstance(key_claim, dict):
            key_claim = key_claim.get("claim", "—")

        deep_url = create_deep_link(url, str(key_claim)) if url and claims else url
        rows.append(f"""      <tr>
        <td>{sid}</td>
        <td><a href="{deep_url}" target="_blank">{title}</a></td>
        <td>{stype}</td>
        <td>{strength}</td>
        <td>{str(key_claim)[:120]}</td>
      </tr>""")

    return "\n".join(rows)


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 source_linker.py <pipeline-dir>")
        sys.exit(1)

    pipeline_dir = Path(sys.argv[1])
    evidence = load_evidence(pipeline_dir)

    if not evidence:
        print("No evidence-extracted.json found. Skipping source linking.")
        return

    print(f"Loaded {len(evidence)} sources from evidence-extracted.json")

    # Link markdown report
    report_path = pipeline_dir / "synthesis-v3" / "final-report-v1.md"
    if report_path.exists():
        report_text = report_path.read_text()
        linked_text = link_sources_in_report(report_text, evidence)
        linked_path = pipeline_dir / "synthesis-v3" / "final-report-v1-linked.md"
        linked_path.write_text(linked_text)
        print(f"Linked report: {linked_path}")

    # Generate HTML source table fragment
    table_html = generate_source_table_html(evidence)
    table_path = pipeline_dir / "synthesis-v3" / "source-table-fragment.html"
    table_path.write_text(table_html)
    print(f"Source table HTML: {table_path}")


if __name__ == "__main__":
    main()

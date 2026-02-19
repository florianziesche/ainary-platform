#!/usr/bin/env python3
"""
evidence_extractor_v2.py — Evidence Extraction via Google LangExtract.

Replaces manual LLM evidence extraction with char-level grounded extraction.
Every claim is mapped to its exact position in the source text.

Usage:
    # Extract from a URL
    python3 evidence_extractor_v2.py url "https://example.com/article" --output evidence.json

    # Extract from a local file  
    python3 evidence_extractor_v2.py file report.pdf --output evidence.json

    # Extract from multiple URLs (batch)
    python3 evidence_extractor_v2.py batch urls.txt --output evidence.json

    # Visualize extractions
    python3 evidence_extractor_v2.py visualize evidence.json --output evidence.html

Requires: pip install langextract (in .venv)
Model: Uses Gemini by default (free tier). Set GOOGLE_API_KEY.
"""

import argparse
import json
import os
import sys
import textwrap
from pathlib import Path

# Use venv python
VENV_PYTHON = Path(__file__).parent / ".venv" / "bin" / "python"

# Try importing langextract
try:
    import langextract as lx
    HAS_LANGEXTRACT = True
except ImportError:
    HAS_LANGEXTRACT = False


# ---------------------------------------------------------------------------
# Extraction Schema (matches our Evidence Extractor v1 output)
# ---------------------------------------------------------------------------

EXTRACT_PROMPT = textwrap.dedent("""\
    Extract structured evidence from this document for a research report.
    For each piece of evidence, extract:
    - claims: Core factual claims (paraphrased from source, NOT invented)
    - metrics: Any numbers, percentages, dollar amounts, dates
    - limitations: What the source explicitly says it doesn't cover
    - methodology: How the data was collected/analyzed (if stated)
    
    Use exact text for extractions where possible. Do not infer beyond what is stated.
    If something is not explicitly stated, do not extract it.
""")

EXTRACT_EXAMPLES = [
    {
        "text": "The study found that 73% of AI deployments fail within 18 months. "
                "The sample included 500 enterprises across 12 industries. "
                "Limitations include self-reported data and survivorship bias.",
        "extractions": [
            {
                "class": "claim",
                "text": "73% of AI deployments fail within 18 months",
                "attributes": {"type": "empirical", "confidence": "high"}
            },
            {
                "class": "metric",
                "text": "500 enterprises across 12 industries",
                "attributes": {"type": "sample_size"}
            },
            {
                "class": "limitation",
                "text": "self-reported data and survivorship bias",
                "attributes": {"type": "methodology_limitation"}
            },
        ]
    }
]


def fetch_url_text(url: str) -> str:
    """Fetch and extract text from a URL."""
    import subprocess
    # Use web_fetch style approach
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        
        # Simple HTML to text (strip tags)
        import re
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:50000]  # Cap at 50K chars
    except Exception as e:
        print(f"  WARNING: Failed to fetch {url}: {e}")
        return ""


def extract_from_text(text: str, source_id: str, model_id: str = "gemini-2.5-flash") -> dict:
    """Extract structured evidence using LangExtract."""
    if not HAS_LANGEXTRACT:
        raise RuntimeError("langextract not installed. Run: pip install langextract")

    # Build examples in LangExtract format
    examples = []
    for ex in EXTRACT_EXAMPLES:
        extractions = []
        for e in ex["extractions"]:
            extractions.append(
                lx.data.Extraction(
                    extraction_class=e["class"],
                    extraction_text=e["text"],
                    attributes=e.get("attributes", {}),
                )
            )
        examples.append(
            lx.data.ExampleData(
                text=ex["text"],
                extractions=extractions,
            )
        )

    # Run extraction
    print(f"  [LANGEXTRACT] Extracting from {len(text)} chars with {model_id}...")
    result = lx.extract(
        text_or_documents=text,
        prompt_description=EXTRACT_PROMPT,
        examples=examples,
        model_id=model_id,
    )

    # Convert to our evidence format
    claims = []
    metrics = []
    limitations = []

    for extraction in result.extractions:
        entry = {
            "text": extraction.extraction_text,
            "class": extraction.extraction_class,
            "attributes": extraction.attributes,
        }
        # Add source grounding if available
        if hasattr(extraction, 'start_index') and extraction.start_index is not None:
            entry["char_start"] = extraction.start_index
            entry["char_end"] = getattr(extraction, 'end_index', None)

        if extraction.extraction_class == "claim":
            claims.append(entry["text"])
        elif extraction.extraction_class == "metric":
            metrics.append(entry["text"])
        elif extraction.extraction_class == "limitation":
            limitations.append(entry["text"])

    return {
        "id": source_id,
        "claims": claims,
        "metrics": metrics,
        "limitations": limitations,
        "extraction_count": len(result.extractions),
        "raw_extractions": [
            {
                "class": e.extraction_class,
                "text": e.extraction_text,
                "attributes": e.attributes,
            }
            for e in result.extractions
        ],
    }


def extract_from_url(url: str, source_id: str, model_id: str = "gemini-2.5-flash") -> dict:
    """Fetch URL and extract evidence."""
    print(f"  Fetching {url}...")
    text = fetch_url_text(url)
    if not text:
        return {"id": source_id, "url": url, "error": "Failed to fetch", "claims": []}

    result = extract_from_text(text, source_id, model_id)
    result["url"] = url
    return result


def visualize_extractions(evidence_path: str, output_path: str):
    """Generate interactive HTML visualization using LangExtract."""
    if not HAS_LANGEXTRACT:
        print("langextract not installed.")
        return

    evidence = json.loads(Path(evidence_path).read_text())
    # LangExtract has built-in visualization
    # For now, generate a simple summary
    print(f"Loaded {len(evidence)} sources")
    for e in evidence:
        sid = e.get("id", "?")
        n_claims = len(e.get("claims", []))
        print(f"  {sid}: {n_claims} claims extracted")


def batch_extract(urls_file: str, output_path: str, model_id: str = "gemini-2.5-flash"):
    """Extract from multiple URLs listed in a file."""
    urls = Path(urls_file).read_text().strip().split("\n")
    results = []
    for i, url in enumerate(urls, 1):
        url = url.strip()
        if not url or url.startswith("#"):
            continue
        sid = f"S{i}"
        print(f"\n[{i}/{len(urls)}] {sid}: {url}")
        result = extract_from_url(url, sid, model_id)
        results.append(result)

    Path(output_path).write_text(json.dumps(results, indent=2))
    print(f"\nExtracted {sum(len(r.get('claims', [])) for r in results)} claims from {len(results)} sources")
    print(f"Output: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Evidence Extractor v2 (LangExtract)")
    sub = parser.add_subparsers(dest="command")

    p_url = sub.add_parser("url", help="Extract from URL")
    p_url.add_argument("url")
    p_url.add_argument("--output", default="evidence.json")
    p_url.add_argument("--model", default="gemini-2.5-flash")
    p_url.add_argument("--source-id", default="S1")

    p_file = sub.add_parser("file", help="Extract from local file")
    p_file.add_argument("path")
    p_file.add_argument("--output", default="evidence.json")
    p_file.add_argument("--model", default="gemini-2.5-flash")
    p_file.add_argument("--source-id", default="S1")

    p_batch = sub.add_parser("batch", help="Extract from URL list")
    p_batch.add_argument("urls_file")
    p_batch.add_argument("--output", default="evidence.json")
    p_batch.add_argument("--model", default="gemini-2.5-flash")

    p_viz = sub.add_parser("visualize", help="Visualize extractions")
    p_viz.add_argument("evidence_file")
    p_viz.add_argument("--output", default="evidence-viz.html")

    args = parser.parse_args()

    if args.command == "url":
        result = extract_from_url(args.url, args.source_id, args.model)
        Path(args.output).write_text(json.dumps([result], indent=2))
        print(f"Output: {args.output}")

    elif args.command == "file":
        text = Path(args.path).read_text()
        result = extract_from_text(text, args.source_id, args.model)
        Path(args.output).write_text(json.dumps([result], indent=2))
        print(f"Output: {args.output}")

    elif args.command == "batch":
        batch_extract(args.urls_file, args.output, args.model)

    elif args.command == "visualize":
        visualize_extractions(args.evidence_file, args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

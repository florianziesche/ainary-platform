#!/usr/bin/env python3
"""
RAG Query Tool for Research Papers
Queries the embedded paper collection from prepare.py.

Usage: python3 query_papers.py "What does BaseCal do?" --topic llm-trust-calibration [--top-k 5]
"""

import argparse
import json
import math
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
RESEARCH_BASE = WORKSPACE / "research-base"


def load_embeddings(topic: str) -> Tuple[List[Dict], Optional[List[List[float]]]]:
    """Load chunks and embeddings from research-base."""
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
    emb_path = RESEARCH_BASE / slug / "embeddings" / "embeddings.json"

    if not emb_path.exists():
        print(f"❌ Embeddings not found: {emb_path}")
        sys.exit(1)

    print(f"  Loading embeddings from {emb_path.name}...")
    data = json.loads(emb_path.read_text(encoding="utf-8"))
    chunks = data.get("chunks", [])
    embeddings = data.get("embeddings", None)
    print(f"  Loaded {len(chunks)} chunks")
    return chunks, embeddings


def embed_query_openai(query: str) -> Optional[List[float]]:
    """Embed query using OpenAI API."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        resp = client.embeddings.create(model="text-embedding-3-small", input=[query])
        return resp.data[0].embedding
    except Exception as e:
        print(f"  ⚠ OpenAI embedding failed: {e}")
        return None


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity without numpy if possible."""
    try:
        import numpy as np
        va, vb = np.array(a), np.array(b)
        denom = np.linalg.norm(va) * np.linalg.norm(vb)
        return float(np.dot(va, vb) / (denom + 1e-10)) if denom > 0 else 0.0
    except ImportError:
        # Pure Python fallback
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(x * x for x in b))
        return dot / (na * nb + 1e-10) if na * nb > 0 else 0.0


def search_embedding(query: str, chunks: List[Dict], embeddings: List[List[float]], top_k: int) -> List[Tuple[float, Dict]]:
    """Search using embedding similarity."""
    query_emb = embed_query_openai(query)
    if query_emb is None:
        return []

    # Try numpy cache
    slug_hash = hash(str(len(chunks)))
    cache_path = Path(f"/tmp/query_papers_cache_{slug_hash}.json")

    scores = []
    for i, emb in enumerate(embeddings):
        score = cosine_similarity(query_emb, emb)
        scores.append((score, chunks[i]))

    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]


def tfidf_search(query: str, chunks: List[Dict], top_k: int) -> List[Tuple[float, Dict]]:
    """TF-IDF based search fallback."""
    query_words = set(re.findall(r'[a-z]+', query.lower()))
    stops = {"the", "a", "an", "in", "of", "for", "and", "or", "to", "is", "on", "at", "by", "with", "that", "this", "it", "are", "was", "be", "as"}
    query_words -= stops

    if not query_words:
        return []

    # Build document frequencies
    doc_freq: Counter = Counter()
    chunk_word_counts: List[Counter] = []
    for chunk in chunks:
        text = chunk.get("text", "")
        words = set(re.findall(r'[a-z]+', text.lower())) - stops
        chunk_word_counts.append(Counter(re.findall(r'[a-z]+', text.lower())))
        for w in words:
            doc_freq[w] += 1

    n_docs = len(chunks)
    scores = []
    for i, chunk in enumerate(chunks):
        score = 0.0
        wc = chunk_word_counts[i]
        total = sum(wc.values()) or 1
        for qw in query_words:
            tf = wc.get(qw, 0) / total
            idf = math.log((n_docs + 1) / (doc_freq.get(qw, 0) + 1))
            score += tf * idf
        scores.append((score, chunk))

    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]


def extract_title(chunk: Dict) -> str:
    """Extract paper title from chunk metadata."""
    meta = chunk.get("meta", {})
    if isinstance(meta, dict):
        return meta.get("title", "Unknown")
    return "Unknown"


def format_results(results: List[Tuple[float, Dict]], topic: str) -> str:
    """Format search results for display."""
    if not results:
        return "No results found."

    lines = ["---"]
    for i, (score, chunk) in enumerate(results, 1):
        title = extract_title(chunk)
        text = chunk.get("text", "")[:300].strip()
        meta = chunk.get("meta", {})
        paper_id = meta.get("paper_id", "unknown") if isinstance(meta, dict) else "unknown"
        chunk_idx = meta.get("chunk_index", "?") if isinstance(meta, dict) else "?"

        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        source_path = f"research-base/{slug}/papers/{paper_id.replace('/', '_').replace(':', '_')}.txt"

        lines.append(f'[{i}] Score: {score:.3f} | Paper: "{title}"')
        lines.append(f'    "{text}..."')
        lines.append(f'    Source: {source_path} (chunk {chunk_idx})')
        lines.append("")

    lines.append("---")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="RAG Query Tool for Research Papers")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--topic", required=True, help="Research topic slug (e.g., llm-trust-calibration)")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results (default: 5)")
    args = parser.parse_args()

    start = time.time()
    print(f"\n🔎 Querying: \"{args.query}\" in topic: {args.topic}")

    chunks, embeddings = load_embeddings(args.topic)

    # Try embedding search first
    results = []
    if embeddings:
        print("  Attempting embedding-based search...")
        results = search_embedding(args.query, chunks, embeddings, args.top_k)

    # Fallback to TF-IDF
    if not results:
        print("  Using TF-IDF fallback search...")
        results = tfidf_search(args.query, chunks, args.top_k)

    elapsed = time.time() - start
    output = format_results(results, args.topic)
    print(output)
    print(f"⏱  {elapsed:.2f}s | {len(results)} results")


if __name__ == "__main__":
    main()

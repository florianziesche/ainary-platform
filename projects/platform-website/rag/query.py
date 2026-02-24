#!/usr/bin/env python3
"""
Ainary RAG — Query the vector index.
Finds relevant chunks via cosine similarity, returns context for LLM.

Usage: python3 rag/query.py "Welche Kandidaten haben Skandale?"
       python3 rag/query.py --city bamberg "Wer sind die Favoriten?"
"""

import json, os, sys
import numpy as np
import voyageai

INDEX_FILE = "rag/index.json"
VOYAGE_MODEL = "voyage-3-lite"
TOP_K = 8

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def load_index():
    with open(INDEX_FILE) as f:
        return json.load(f)

def search(query: str, index: dict, city_filter: str = None, top_k: int = TOP_K) -> list[dict]:
    """Search index for relevant chunks."""
    # Load API key
    config_path = os.path.expanduser("~/.openclaw/openclaw.json")
    try:
        with open(config_path) as f:
            config = json.load(f)
        api_key = config.get("agents", {}).get("defaults", {}).get("memorySearch", {}).get("apiKey")
    except:
        api_key = os.environ.get("VOYAGE_API_KEY")
    
    vo = voyageai.Client(api_key=api_key)
    result = vo.embed([query], model=VOYAGE_MODEL, input_type="query")
    q_emb = result.embeddings[0]
    
    # Score all chunks
    scored = []
    for chunk in index["chunks"]:
        if city_filter and chunk["city"] != city_filter:
            continue
        score = cosine_similarity(q_emb, chunk["embedding"])
        scored.append((score, chunk))
    
    # Sort by score descending
    scored.sort(key=lambda x: x[0], reverse=True)
    
    return [{"score": round(s, 4), **c} for s, c in scored[:top_k]]

def format_context(results: list[dict]) -> str:
    """Format search results as context for LLM."""
    lines = ["=== RELEVANTE DATEN (Ainary Intelligence) ===\n"]
    for i, r in enumerate(results):
        lines.append(f"--- [{i+1}] {r['name']} ({r['city']}) | {r['type']} | Relevanz: {r['score']} ---")
        lines.append(r["text"])
        lines.append("")
    return "\n".join(lines)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Search query")
    parser.add_argument("--city", help="Filter by city")
    parser.add_argument("--top-k", type=int, default=TOP_K)
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()
    
    index = load_index()
    results = search(args.query, index, city_filter=args.city, top_k=args.top_k)
    
    if args.json:
        # Remove embeddings from output
        for r in results:
            r.pop("embedding", None)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(format_context(results))
        print(f"\n[{len(results)} Ergebnisse aus {len(set(r['city'] for r in results))} Städten]")

if __name__ == "__main__":
    main()

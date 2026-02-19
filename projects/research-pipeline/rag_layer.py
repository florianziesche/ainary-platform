"""
RAG Query Layer — TF-IDF + BM25 hybrid search with tiered boosting.

Uses stdlib + math only. No external dependencies.
Ingests CRTs, corrections, reference library, and vault notes.
"""

from __future__ import annotations

import json
import math
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TIER_BOOST = {"CORE": 2.0, "KNOWLEDGE": 1.5, "OPERATIONAL": 1.0, "EPHEMERAL": 0.5}

WORKSPACE = Path(os.environ.get(
    "WORKSPACE", Path.home() / ".openclaw" / "workspace"
))
RESEARCH_BASE = WORKSPACE / "research-base"
VAULT_INDEX = WORKSPACE / "vault-index" / "embeddings.json"

# ---------------------------------------------------------------------------
# Internal store
# ---------------------------------------------------------------------------

_DOCS: list[dict] = []           # {text, source_id, tier, metadata}
_IDF: dict[str, float] = {}
_TF: list[dict[str, float]] = []  # per-doc term freqs
_AVG_DL: float = 0.0
_DOC_LENS: list[int] = []
_BUILT: bool = False


def _tokenize(text: str) -> list[str]:
    """Lowercase, strip non-alnum, split."""
    return re.findall(r"[a-z0-9]+", text.lower())


def _build_index() -> None:
    """Build BM25 index from _DOCS."""
    global _IDF, _TF, _AVG_DL, _DOC_LENS, _BUILT
    n = len(_DOCS)
    if n == 0:
        _BUILT = True
        return

    _TF = []
    _DOC_LENS = []
    df: Counter = Counter()

    for doc in _DOCS:
        tokens = _tokenize(doc["text"])
        _DOC_LENS.append(len(tokens))
        tf = Counter(tokens)
        _TF.append(dict(tf))
        df.update(tf.keys())

    _AVG_DL = sum(_DOC_LENS) / n if n else 1.0
    _IDF = {
        term: math.log((n - freq + 0.5) / (freq + 0.5) + 1.0)
        for term, freq in df.items()
    }
    _BUILT = True


def _bm25_score(query_tokens: list[str], doc_idx: int, k1: float = 1.5, b: float = 0.75) -> float:
    tf = _TF[doc_idx]
    dl = _DOC_LENS[doc_idx]
    score = 0.0
    for t in query_tokens:
        if t not in tf:
            continue
        f = tf[t]
        idf = _IDF.get(t, 0.0)
        num = f * (k1 + 1)
        denom = f + k1 * (1 - b + b * dl / _AVG_DL)
        score += idf * num / denom
    return score


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def ingest(sources: list[dict]) -> None:
    """Ingest documents into the knowledge base.

    Each source dict must have:
        - text: str
        - source_id: str
        - tier: str  (CORE | KNOWLEDGE | OPERATIONAL | EPHEMERAL)
    Optional:
        - metadata: dict
    """
    global _BUILT
    for src in sources:
        _DOCS.append({
            "text": src["text"],
            "source_id": src["source_id"],
            "tier": src.get("tier", "EPHEMERAL"),
            "metadata": src.get("metadata", {}),
        })
    _BUILT = False


def ensure_index() -> None:
    global _BUILT
    if not _BUILT:
        _build_index()


def query(
    question: str,
    top_k: int = 10,
    tier_filter: list[str] | None = None,
) -> list[dict]:
    """Query the knowledge base. Returns ranked chunks with metadata.

    Each result: {text, source_id, tier, relevance_score, metadata}
    """
    ensure_index()
    if not _DOCS:
        return []

    tokens = _tokenize(question)
    results = []
    for i, doc in enumerate(_DOCS):
        if tier_filter and doc["tier"] not in tier_filter:
            continue
        raw = _bm25_score(tokens, i)
        boosted = raw * TIER_BOOST.get(doc["tier"], 1.0)
        results.append({
            "text": doc["text"][:500],
            "source_id": doc["source_id"],
            "tier": doc["tier"],
            "relevance_score": round(boosted, 4),
            "metadata": doc["metadata"],
        })

    results.sort(key=lambda r: r["relevance_score"], reverse=True)
    return results[:top_k]


def query_for_section(
    section_type: str,
    outline: dict,
    top_k: int = 15,
) -> list[dict]:
    """Section-specific query using outline guidance + section type."""
    parts = [section_type]
    if "title" in outline:
        parts.append(outline["title"])
    if "guidance" in outline:
        parts.append(outline["guidance"])
    if "keywords" in outline:
        parts.extend(outline["keywords"])
    combined = " ".join(parts)
    return query(combined, top_k=top_k)


# ---------------------------------------------------------------------------
# Auto-ingest helper
# ---------------------------------------------------------------------------

def _chunk_text(text: str, source_id: str, chunk_size: int = 500) -> list[dict]:
    """Split text into ~chunk_size char chunks at paragraph boundaries."""
    paragraphs = re.split(r"\n\n+", text)
    chunks: list[dict] = []
    current = ""
    for para in paragraphs:
        if len(current) + len(para) > chunk_size and current:
            chunks.append({"text": current.strip(), "source_id": source_id})
            current = para
        else:
            current = current + "\n\n" + para if current else para
    if current.strip():
        chunks.append({"text": current.strip(), "source_id": source_id})
    return chunks


def ingest_vault_knowledge() -> int:
    """Ingest high-value Obsidian vault knowledge files as KNOWLEDGE tier (1.5x boost).

    Files:
      - Top-20-Papers-AUDITED.md (audited paper summaries)
      - Agent-Developments-Jan-Feb-2026.md (recent developments)
      - Cross-Pattern-Insights.md (cross-domain pattern analysis)
      - Compound-Machine-Architecture.md (compound machine design)
      - AI-Memory-Self-Improvement.md (AI memory research)
    """
    vault_base = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents" / "System_OS"
    knowledge_dir = vault_base / "60_Resources" / "Knowledge"
    ai_dir = vault_base / "60_Resources" / "AI"

    vault_files = [
        (knowledge_dir / "Top-20-Papers-AUDITED.md", "vault:top-20-papers-audited", ["AI agents", "papers", "architecture", "memory"]),
        (knowledge_dir / "Agent-Developments-Jan-Feb-2026.md", "vault:agent-developments-2026", ["AI agents", "MCP", "Claude", "frameworks"]),
        (knowledge_dir / "Cross-Pattern-Insights.md", "vault:cross-pattern-insights", ["patterns", "journalism", "manufacturing", "government"]),
        (knowledge_dir / "Compound-Machine-Architecture.md", "vault:compound-machine-architecture", ["compound", "architecture", "knowledge", "systems"]),
        (ai_dir / "AI-Memory-Self-Improvement.md", "vault:ai-memory-self-improvement", ["memory", "self-improvement", "calibration", "trust"]),
    ]

    count = 0
    for fpath, source_id, topics in vault_files:
        if not fpath.exists():
            continue
        text = fpath.read_text(errors="replace")
        chunks = _chunk_text(text, source_id)
        for chunk in chunks:
            ingest([{
                "text": chunk["text"],
                "source_id": chunk["source_id"],
                "tier": "KNOWLEDGE",
                "metadata": {"path": str(fpath), "topics": topics},
            }])
            count += 1

    return count


def load_default_sources() -> int:
    """Load CRTs, corrections, reference library, vault knowledge, and vault notes."""
    count = 0

    # CORE: CRTs
    crt_path = RESEARCH_BASE / "compounding-research-truths.json"
    if crt_path.exists():
        data = json.loads(crt_path.read_text())
        for t in data.get("truths", []):
            ingest([{
                "text": f"{t['id']}: {t['claim']}. Source: {t.get('source','')}. Tags: {', '.join(t.get('tags',[]))}",
                "source_id": t["id"],
                "tier": "CORE",
                "metadata": {"confidence": t.get("confidence"), "category": t.get("category")},
            }])
            count += 1

    # CORE: Corrections
    corr_path = RESEARCH_BASE / "corrections.json"
    if corr_path.exists():
        data = json.loads(corr_path.read_text())
        for c in data.get("corrections", []):
            ingest([{
                "text": f"{c['id']}: Wrong: {c['wrong']} → Right: {c['right']}. Source: {c.get('source','')}",
                "source_id": c["id"],
                "tier": "CORE",
                "metadata": {"wrong": c["wrong"]},
            }])
            count += 1

    # KNOWLEDGE: Reference library
    ref_path = RESEARCH_BASE / "reference-library.json"
    if ref_path.exists():
        data = json.loads(ref_path.read_text())
        for p in data:
            ingest([{
                "text": f"{p['id']}: {p['title']} ({p.get('authors','')}, {p.get('venue','')}). {p.get('key_finding','')}",
                "source_id": p["id"],
                "tier": "KNOWLEDGE",
                "metadata": {"doi": p.get("doi"), "tier_rank": p.get("tier")},
            }])
            count += 1

    # CORE: Platform findings (curated)
    pf_path = RESEARCH_BASE / "platform-findings-curated.md"
    if pf_path.exists():
        text = pf_path.read_text()
        for block in text.split("\n## ")[1:]:  # skip header
            lines = block.strip().split("\n")
            title = lines[0] if lines else ""
            body = "\n".join(lines[1:]).strip()
            fid = title.split("(")[0].strip() if "(" in title else title[:20]
            ingest([{
                "text": f"{title}\n{body}",
                "source_id": f"PF-{fid}",
                "tier": "CORE",
                "metadata": {"source": "platform-findings-curated"},
            }])
            count += 1

    # KNOWLEDGE: Vault knowledge files
    count += ingest_vault_knowledge()

    # EPHEMERAL: Vault notes (sample — only first 500 to keep fast)
    if VAULT_INDEX.exists():
        data = json.loads(VAULT_INDEX.read_text())
        for chunk in data.get("chunks", [])[:500]:
            ingest([{
                "text": chunk["text"],
                "source_id": chunk["path"],
                "tier": "EPHEMERAL",
                "metadata": {"path": chunk["path"]},
            }])
            count += 1

    return count


# ---------------------------------------------------------------------------
# CLI test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    n = load_default_sources()
    print(f"Ingested {n} chunks ({len(_DOCS)} total docs)")
    ensure_index()
    print(f"Index built: {len(_IDF)} terms, avg doc len {_AVG_DL:.1f}\n")

    tests = [
        "RLHF calibration damage recovery",
        "EU AI Act accuracy calibration requirement",
        "Budget-CoCoA cost per check",
    ]

    for q in tests:
        print(f"Q: {q}")
        results = query(q, top_k=5)
        for i, r in enumerate(results, 1):
            print(f"  {i}. [{r['tier']}] {r['source_id']} (score={r['relevance_score']}) — {r['text'][:120]}")
        print()

#!/usr/bin/env python3
"""
Research Preparation Pipeline — Phase 0
Builds a comprehensive research dossier from academic papers.

Usage:
    python3 prepare.py "LLM Trust Calibration" [--papers 50] [--depth full|quick]
"""

import argparse
import json
import math
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple
from urllib.parse import quote_plus
import requests

# --- Constants ---
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
RESEARCH_BASE = WORKSPACE / "research-base"
CURRENT_YEAR = datetime.now().year

# Rate limits (seconds between requests)
SEMANTIC_SCHOLAR_DELAY = 1.1
ARXIV_DELAY = 3.0
SS_BASE = "https://api.semanticscholar.org/graph/v1"
ARXIV_BASE = "https://export.arxiv.org/api/query"

# Chunking
CHUNK_SIZE_TOKENS = 500
CHUNK_OVERLAP_TOKENS = 100

# Embedding
EMBED_MODEL = "text-embedding-3-small"
EMBED_BATCH_SIZE = 100

# LLM for extraction
HAIKU_MODEL = "claude-haiku-4-5-20250514"
GPT_MINI_MODEL = "gpt-4o-mini"

# Cost tracking (approximate $/1K tokens)
COSTS = {
    "text-embedding-3-small": {"input": 0.00002, "output": 0},
    "claude-haiku-4-5-20250514": {"input": 0.001, "output": 0.005},
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
}

# --- Data Classes ---
@dataclass
class PaperMeta:
    paper_id: str
    title: str
    year: Optional[int] = None
    citation_count: int = 0
    abstract: str = ""
    pdf_url: str = ""
    authors: List[str] = field(default_factory=list)
    venue: str = ""
    source: str = ""  # "semantic_scholar" or "arxiv"
    external_ids: Dict[str, str] = field(default_factory=dict)
    score: float = 0.0

@dataclass
class PaperFull:
    meta: PaperMeta
    full_text: str = ""
    abstract_only: bool = False

@dataclass
class CostTracker:
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost_usd: float = 0.0
    calls: List[Dict] = field(default_factory=list)

    def add(self, model: str, input_tokens: int, output_tokens: int):
        cost_in = COSTS.get(model, {}).get("input", 0) * input_tokens / 1000
        cost_out = COSTS.get(model, {}).get("output", 0) * output_tokens / 1000
        cost = cost_in + cost_out
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost_usd += cost
        self.calls.append({"model": model, "in": input_tokens, "out": output_tokens, "cost": round(cost, 6)})


class ResearchPreparer:
    """Phase 0: Collect, Read, Connect, Verify — BEFORE writing a single word."""

    def __init__(self, topic: str, max_papers: int = 50, depth: str = "full"):
        self.topic = topic
        self.slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        self.max_papers = max_papers
        self.depth = depth  # "full" or "quick"
        self.output_dir = RESEARCH_BASE / self.slug
        self.papers_dir = self.output_dir / "papers"
        self.cost = CostTracker()
        self.errors: List[str] = []
        self.start_time = time.time()

        # API clients (lazy init)
        self._openai = None
        self._anthropic = None

        # Ensure dirs
        self.papers_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "embeddings").mkdir(exist_ok=True)

    @property
    def openai_client(self):
        if self._openai is None:
            import openai
            key = os.environ.get("OPENAI_API_KEY")
            if not key:
                raise RuntimeError("OPENAI_API_KEY not set — cannot create embeddings")
            self._openai = openai.OpenAI(api_key=key)
        return self._openai

    @property
    def anthropic_client(self):
        if self._anthropic is None:
            import anthropic
            key = os.environ.get("ANTHROPIC_API_KEY")
            if not key:
                return None
            self._anthropic = anthropic.Anthropic(api_key=key)
        return self._anthropic

    # =========================================================================
    # HELPERS
    # =========================================================================
    def _api_get(self, url: str, params: dict = None, delay: float = 0, retries: int = 3) -> Optional[dict]:
        """GET with retries and rate limiting."""
        for attempt in range(retries):
            if delay > 0:
                time.sleep(delay)
            try:
                r = requests.get(url, params=params, timeout=30)
                if r.status_code == 429:
                    wait = 2 ** (attempt + 1)
                    print(f"  Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                    continue
                if r.status_code == 200:
                    return r.json() if 'json' in r.headers.get('content-type', '') else {"text": r.text}
                else:
                    if attempt == retries - 1:
                        self.errors.append(f"GET {url}: {r.status_code}")
                    time.sleep(1)
            except Exception as e:
                if attempt == retries - 1:
                    self.errors.append(f"GET {url}: {e}")
                time.sleep(1)
        return None

    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of texts using OpenAI."""
        all_embeddings = []
        for i in range(0, len(texts), EMBED_BATCH_SIZE):
            batch = texts[i:i + EMBED_BATCH_SIZE]
            resp = self.openai_client.embeddings.create(model=EMBED_MODEL, input=batch)
            self.cost.add(EMBED_MODEL, sum(len(t.split()) for t in batch), 0)
            all_embeddings.extend([d.embedding for d in resp.data])
        return all_embeddings

    def _llm_extract(self, text: str, system: str = "") -> str:
        """Call LLM for extraction. Tries Anthropic Haiku, falls back to OpenAI."""
        client = self.anthropic_client
        if client:
            try:
                resp = client.messages.create(
                    model=HAIKU_MODEL, max_tokens=2048, temperature=0,
                    system=system or "Extract structured information. Return valid JSON only.",
                    messages=[{"role": "user", "content": text}]
                )
                self.cost.add(HAIKU_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
                return resp.content[0].text
            except Exception as e:
                self.errors.append(f"Haiku error: {e}")

        # Fallback to OpenAI
        try:
            resp = self.openai_client.chat.completions.create(
                model=GPT_MINI_MODEL, max_tokens=2048, temperature=0,
                messages=[
                    {"role": "system", "content": system or "Extract structured information. Return valid JSON only."},
                    {"role": "user", "content": text}
                ]
            )
            usage = resp.usage
            self.cost.add(GPT_MINI_MODEL, usage.prompt_tokens, usage.completion_tokens)
            return resp.choices[0].message.content
        except Exception as e:
            self.errors.append(f"LLM extraction error: {e}")
            return "{}"

    @staticmethod
    def _cosine_sim(a: List[float], b: List[float]) -> float:
        import numpy as np
        a, b = np.array(a), np.array(b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))

    @staticmethod
    def _title_similar(t1: str, t2: str) -> bool:
        """Simple title similarity check."""
        def norm(t): return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()
        a, b = norm(t1), norm(t2)
        if not a or not b:
            return False
        # Jaccard on words
        wa, wb = set(a.split()), set(b.split())
        if not wa or not wb:
            return False
        return len(wa & wb) / len(wa | wb) > 0.85

    # =========================================================================
    # STEP 1: DISCOVER
    # =========================================================================
    def discover(self) -> List[PaperMeta]:
        """Search Semantic Scholar + arXiv for papers."""
        print(f"\n[1/12] DISCOVER: Searching for '{self.topic}'...")

        # Check resume
        meta_path = self.papers_dir / "metadata.json"
        if meta_path.exists():
            data = json.loads(meta_path.read_text())
            if len(data) > 0:
                papers = [PaperMeta(**p) for p in data]
                print(f"  Resumed: {len(papers)} papers from cache")
                return papers

        papers: List[PaperMeta] = []
        max_discover = min(500, self.max_papers * 10) if self.depth == "full" else self.max_papers * 5

        # --- Semantic Scholar ---
        ss_limit = min(100, max_discover)
        ss_pages = min(5, math.ceil(max_discover / 100))
        for page in range(ss_pages):
            offset = page * 100
            data = self._api_get(
                f"{SS_BASE}/paper/search",
                params={
                    "query": self.topic,
                    "limit": ss_limit,
                    "offset": offset,
                    "fields": "title,year,citationCount,abstract,openAccessPdf,externalIds,authors,venue"
                },
                delay=SEMANTIC_SCHOLAR_DELAY
            )
            if not data or "data" not in data:
                break
            for item in data["data"]:
                if not item.get("title"):
                    continue
                pdf_url = ""
                if item.get("openAccessPdf") and item["openAccessPdf"].get("url"):
                    pdf_url = item["openAccessPdf"]["url"]
                papers.append(PaperMeta(
                    paper_id=item.get("paperId", ""),
                    title=item["title"],
                    year=item.get("year"),
                    citation_count=item.get("citationCount", 0) or 0,
                    abstract=item.get("abstract", "") or "",
                    pdf_url=pdf_url,
                    authors=[a.get("name", "") for a in (item.get("authors") or [])[:5]],
                    venue=item.get("venue", "") or "",
                    source="semantic_scholar",
                    external_ids=item.get("externalIds") or {}
                ))
            print(f"  Semantic Scholar page {page+1}: {len(data['data'])} results")
            if len(data["data"]) < ss_limit:
                break

        # --- arXiv ---
        arxiv_max = min(200, max_discover - len(papers)) if self.depth == "full" else min(100, self.max_papers * 2)
        arxiv_pages = min(3, math.ceil(arxiv_max / 100))
        for page in range(arxiv_pages):
            start = page * 100
            time.sleep(ARXIV_DELAY)
            try:
                r = requests.get(ARXIV_BASE, params={
                    "search_query": f"all:{quote_plus(self.topic)}",
                    "start": start, "max_results": 100,
                    "sortBy": "relevance", "sortOrder": "descending"
                }, timeout=30)
                root = ET.fromstring(r.text)
                ns = {"a": "http://www.w3.org/2005/Atom"}
                entries = root.findall("a:entry", ns)
                for entry in entries:
                    title = (entry.findtext("a:title", "", ns) or "").replace("\n", " ").strip()
                    if not title:
                        continue
                    # Get PDF link
                    pdf_url = ""
                    for link in entry.findall("a:link", ns):
                        if link.get("title") == "pdf":
                            pdf_url = link.get("href", "")
                    published = entry.findtext("a:published", "", ns)
                    year = int(published[:4]) if published else None
                    abstract = (entry.findtext("a:summary", "", ns) or "").replace("\n", " ").strip()
                    arxiv_id = (entry.findtext("a:id", "", ns) or "").split("/abs/")[-1]
                    authors = [a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns)][:5]

                    papers.append(PaperMeta(
                        paper_id=f"arxiv:{arxiv_id}",
                        title=title,
                        year=year,
                        abstract=abstract,
                        pdf_url=pdf_url,
                        authors=authors,
                        source="arxiv",
                        external_ids={"arxiv": arxiv_id}
                    ))
                print(f"  arXiv page {page+1}: {len(entries)} results")
                if len(entries) < 100:
                    break
            except Exception as e:
                self.errors.append(f"arXiv error: {e}")
                break

        # Deduplicate
        unique = []
        seen_titles = []
        for p in papers:
            if not any(self._title_similar(p.title, t) for t in seen_titles):
                unique.append(p)
                seen_titles.append(p.title)
        print(f"  Total: {len(papers)} raw → {len(unique)} unique papers")
        papers = unique

        # Save metadata
        meta_path.write_text(json.dumps([asdict(p) for p in papers], indent=2))
        return papers

    # =========================================================================
    # STEP 2: FILTER
    # =========================================================================
    def filter_papers(self, papers: List[PaperMeta]) -> List[PaperMeta]:
        """Rank and filter papers by composite score."""
        print(f"\n[2/12] FILTER: Ranking {len(papers)} papers...")

        # Embed query
        query_emb = self._embed_texts([self.topic])[0]

        # Embed abstracts (only those with abstracts)
        abstracts = [p.abstract if p.abstract else p.title for p in papers]
        abstract_embs = self._embed_texts(abstracts)

        max_citations = max((p.citation_count for p in papers), default=1) or 1

        for i, p in enumerate(papers):
            rel = self._cosine_sim(query_emb, abstract_embs[i])
            rec = max(0, 1 - (CURRENT_YEAR - (p.year or CURRENT_YEAR)) / 10)
            cit = math.log(1 + p.citation_count) / math.log(1 + max_citations) if max_citations > 0 else 0
            p.score = 0.4 * rel + 0.3 * rec + 0.3 * cit

        papers.sort(key=lambda p: p.score, reverse=True)
        top = papers[:self.max_papers]

        # Stats
        year_dist = {}
        for p in top:
            y = p.year or 0
            year_dist[y] = year_dist.get(y, 0) + 1
        print(f"  Top {len(top)} papers selected (score range: {top[-1].score:.3f} - {top[0].score:.3f})")
        print(f"  Year distribution: {dict(sorted(year_dist.items()))}")

        # Update metadata
        (self.papers_dir / "metadata.json").write_text(json.dumps([asdict(p) for p in papers], indent=2))
        return top

    # =========================================================================
    # STEP 3: COLLECT
    # =========================================================================
    def collect_papers(self, papers: List[PaperMeta]) -> List[PaperFull]:
        """Download PDFs and extract text."""
        print(f"\n[3/12] COLLECT: Downloading {len(papers)} papers...")

        results = []
        downloaded = 0
        for i, p in enumerate(papers):
            txt_path = self.papers_dir / f"{p.paper_id.replace('/', '_').replace(':', '_')}.txt"

            # Resume check
            if txt_path.exists() and txt_path.stat().st_size > 100:
                text = txt_path.read_text()
                results.append(PaperFull(meta=p, full_text=text, abstract_only=False))
                downloaded += 1
                continue

            if p.pdf_url:
                try:
                    time.sleep(0.5)
                    r = requests.get(p.pdf_url, timeout=30)
                    if r.status_code == 200 and len(r.content) > 1000:
                        import fitz
                        doc = fitz.open(stream=r.content, filetype="pdf")
                        text = ""
                        for page in doc:
                            text += page.get_text()
                        doc.close()
                        # Clean
                        text = re.sub(r'\n{3,}', '\n\n', text)
                        text = re.sub(r'[ \t]+', ' ', text)
                        if len(text) > 200:
                            txt_path.write_text(text)
                            results.append(PaperFull(meta=p, full_text=text, abstract_only=False))
                            downloaded += 1
                            continue
                except Exception as e:
                    self.errors.append(f"PDF error {p.paper_id}: {e}")

            # Fallback: abstract only
            results.append(PaperFull(meta=p, full_text=p.abstract, abstract_only=True))
            if p.abstract:
                txt_path.write_text(p.abstract)

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(papers)} ({downloaded} full text)")

        abstract_only = sum(1 for r in results if r.abstract_only)
        print(f"  Collected: {downloaded} full text, {abstract_only} abstract-only")
        return results

    # =========================================================================
    # STEP 4+5+6: CHUNK + EMBED + STORE
    # =========================================================================
    def build_vector_store(self, papers: List[PaperFull]):
        """Chunk, embed, and store papers."""
        print(f"\n[4-6/12] CHUNK + EMBED + STORE...")

        emb_path = self.output_dir / "embeddings" / "embeddings.json"
        if emb_path.exists():
            data = json.loads(emb_path.read_text())
            if len(data.get("chunks", [])) > 0:
                print(f"  Resumed: {len(data['chunks'])} chunks from cache")
                return

        # Chunk
        chunks = []
        chunk_metas = []
        for p in papers:
            text = p.full_text or p.meta.abstract or ""
            if not text:
                continue
            words = text.split()
            # Approximate token boundary in words: tokens ≈ words * 1.3, so words per chunk ≈ 500/1.3 ≈ 385
            words_per_chunk = int(CHUNK_SIZE_TOKENS / 1.3)
            overlap_words = int(CHUNK_OVERLAP_TOKENS / 1.3)
            step = max(1, words_per_chunk - overlap_words)
            for idx in range(0, len(words), step):
                chunk_words = words[idx:idx + words_per_chunk]
                if len(chunk_words) < 20:
                    continue
                chunk_text = " ".join(chunk_words)
                chunks.append(chunk_text)
                chunk_metas.append({
                    "paper_id": p.meta.paper_id,
                    "title": p.meta.title,
                    "chunk_index": idx // step,
                    "abstract_only": p.abstract_only
                })

        print(f"  Created {len(chunks)} chunks from {len(papers)} papers")

        if not chunks:
            print("  WARNING: No chunks to embed")
            return

        # Embed
        print(f"  Embedding {len(chunks)} chunks...")
        embeddings = self._embed_texts(chunks)

        # Store as JSON (works with or without chromadb)
        store_data = {
            "chunks": [{"text": c, "meta": m} for c, m in zip(chunks, chunk_metas)],
            "embeddings": embeddings,
            "model": EMBED_MODEL,
            "created": datetime.now().isoformat()
        }
        emb_path.write_text(json.dumps(store_data))
        print(f"  Stored {len(chunks)} chunks ({emb_path.stat().st_size / 1024 / 1024:.1f} MB)")

        # Try ChromaDB too
        try:
            import chromadb
            chroma_path = str(self.output_dir / "embeddings" / "chromadb")
            client = chromadb.PersistentClient(path=chroma_path)
            collection = client.get_or_create_collection(name=self.slug)
            # Batch insert
            batch = 100
            for i in range(0, len(chunks), batch):
                end = min(i + batch, len(chunks))
                collection.add(
                    ids=[f"chunk_{j}" for j in range(i, end)],
                    documents=chunks[i:end],
                    embeddings=embeddings[i:end],
                    metadatas=chunk_metas[i:end]
                )
            print(f"  ChromaDB: stored {len(chunks)} chunks")
        except Exception as e:
            print(f"  ChromaDB not available, using JSON fallback: {e}")

    # =========================================================================
    # STEP 7: CITE (Citation Chains)
    # =========================================================================
    def build_citation_chains(self, papers: List[PaperMeta]):
        """Build forward + backward citation graph."""
        print(f"\n[7/12] CITE: Building citation chains...")

        cite_path = self.output_dir / "citation_graph.json"
        if cite_path.exists():
            print("  Resumed from cache")
            return json.loads(cite_path.read_text())

        # Use top 20 papers (or fewer in quick mode)
        top_n = 10 if self.depth == "quick" else 20
        top_papers = sorted(papers, key=lambda p: p.score, reverse=True)[:top_n]

        nodes = {}
        edges = []
        corpus_ids = {p.paper_id for p in papers}

        for p in top_papers:
            if not p.paper_id or p.paper_id.startswith("arxiv:"):
                continue
            nodes[p.paper_id] = {"id": p.paper_id, "title": p.title, "year": p.year,
                                  "citations": p.citation_count, "in_corpus": True}

            # Forward citations
            data = self._api_get(
                f"{SS_BASE}/paper/{p.paper_id}/citations",
                params={"fields": "title,year,citationCount", "limit": 50},
                delay=SEMANTIC_SCHOLAR_DELAY
            )
            if data and "data" in data:
                for c in data["data"]:
                    cp = c.get("citingPaper", {})
                    cid = cp.get("paperId", "")
                    if cid and cid not in nodes:
                        nodes[cid] = {"id": cid, "title": cp.get("title", ""),
                                       "year": cp.get("year"), "citations": cp.get("citationCount", 0),
                                       "in_corpus": cid in corpus_ids}
                    if cid:
                        edges.append({"from": cid, "to": p.paper_id, "type": "cites"})

            # Backward references
            data = self._api_get(
                f"{SS_BASE}/paper/{p.paper_id}/references",
                params={"fields": "title,year,citationCount", "limit": 50},
                delay=SEMANTIC_SCHOLAR_DELAY
            )
            if data and "data" in data:
                for c in data["data"]:
                    cp = c.get("citedPaper", {})
                    cid = cp.get("paperId", "")
                    if cid and cid not in nodes:
                        nodes[cid] = {"id": cid, "title": cp.get("title", ""),
                                       "year": cp.get("year"), "citations": cp.get("citationCount", 0),
                                       "in_corpus": cid in corpus_ids}
                    if cid:
                        edges.append({"from": p.paper_id, "to": cid, "type": "cites"})

        graph_data = {"nodes": list(nodes.values()), "edges": edges}
        cite_path.write_text(json.dumps(graph_data, indent=2))
        print(f"  Citation graph: {len(nodes)} nodes, {len(edges)} edges")
        return graph_data

    # =========================================================================
    # STEP 8: EXTRACT (Entities + Claims)
    # =========================================================================
    def extract_knowledge(self, papers: List[PaperFull]) -> Dict:
        """Extract methods, datasets, claims from each paper using LLM."""
        print(f"\n[8/12] EXTRACT: Extracting knowledge from {len(papers)} papers...")

        know_path = self.output_dir / "knowledge.json"
        if know_path.exists():
            data = json.loads(know_path.read_text())
            if len(data.get("papers", [])) > 0:
                print(f"  Resumed: {len(data['papers'])} papers from cache")
                return data

        knowledge = {"papers": [], "all_methods": [], "all_datasets": [], "all_models": [], "all_claims": []}

        for i, p in enumerate(papers):
            text = p.full_text[:4000] if p.full_text else p.meta.abstract[:2000]
            if not text or len(text) < 50:
                continue

            prompt = f"""Analyze this research paper and extract structured information.

Title: {p.meta.title}
Year: {p.meta.year}
Text (excerpt):
{text}

Extract as JSON:
{{
  "methods": ["method1", "method2"],
  "datasets": ["dataset1", "dataset2"],
  "models": ["model1", "model2"],
  "key_findings": ["finding1", "finding2"],
  "claims": [{{"text": "claim text", "confidence": "high/medium/low"}}],
  "limitations": ["limitation1"]
}}

Return ONLY valid JSON."""

            try:
                result = self._llm_extract(prompt)
                # Parse JSON from response
                result = result.strip()
                if result.startswith("```"):
                    result = re.sub(r'^```\w*\n?', '', result)
                    result = re.sub(r'\n?```$', '', result)
                parsed = json.loads(result)
                parsed["paper_id"] = p.meta.paper_id
                parsed["title"] = p.meta.title
                parsed["year"] = p.meta.year
                knowledge["papers"].append(parsed)

                for m in parsed.get("methods", []):
                    if m not in knowledge["all_methods"]:
                        knowledge["all_methods"].append(m)
                for d in parsed.get("datasets", []):
                    if d not in knowledge["all_datasets"]:
                        knowledge["all_datasets"].append(d)
                for m in parsed.get("models", []):
                    if m not in knowledge["all_models"]:
                        knowledge["all_models"].append(m)
                for c in parsed.get("claims", []):
                    knowledge["all_claims"].append({**c, "paper_id": p.meta.paper_id, "year": p.meta.year})

            except Exception as e:
                self.errors.append(f"Extract error {p.meta.paper_id}: {e}")

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(papers)}")

        know_path.write_text(json.dumps(knowledge, indent=2))
        print(f"  Extracted: {len(knowledge['all_methods'])} methods, {len(knowledge['all_datasets'])} datasets, "
              f"{len(knowledge['all_models'])} models, {len(knowledge['all_claims'])} claims")
        return knowledge

    # =========================================================================
    # STEP 9: GRAPH (Knowledge Graph)
    # =========================================================================
    def build_knowledge_graph(self, knowledge: Dict, citation_data: Dict) -> Any:
        """Build NetworkX knowledge graph."""
        print(f"\n[9/12] GRAPH: Building knowledge graph...")

        graph_path = self.output_dir / "graph.json"
        stats_path = self.output_dir / "graph_stats.md"

        import networkx as nx
        G = nx.DiGraph()

        # Add paper nodes
        for p in knowledge.get("papers", []):
            G.add_node(p["paper_id"], type="paper", title=p.get("title", ""),
                       year=p.get("year"), label=p.get("title", "")[:50])

        # Add method/dataset/model nodes and edges
        method_counts = {}
        dataset_counts = {}
        model_counts = {}

        for p in knowledge.get("papers", []):
            pid = p["paper_id"]
            for m in p.get("methods", []):
                mn = f"method:{m}"
                method_counts[m] = method_counts.get(m, 0) + 1
                G.add_node(mn, type="method", name=m)
                G.add_edge(pid, mn, relation="USES")
            for d in p.get("datasets", []):
                dn = f"dataset:{d}"
                dataset_counts[d] = dataset_counts.get(d, 0) + 1
                G.add_node(dn, type="dataset", name=d)
                G.add_edge(pid, dn, relation="EVALUATES_ON")
            for m in p.get("models", []):
                mdn = f"model:{m}"
                model_counts[m] = model_counts.get(m, 0) + 1
                G.add_node(mdn, type="model", name=m)
                G.add_edge(pid, mdn, relation="TESTS")
            for c in p.get("claims", []):
                cn = f"claim:{pid}:{c.get('text', '')[:50]}"
                G.add_node(cn, type="claim", text=c.get("text", ""), confidence=c.get("confidence", ""))
                G.add_edge(pid, cn, relation="CLAIMS")

        # Add citation edges
        for e in citation_data.get("edges", []):
            if e["from"] in G and e["to"] in G:
                G.add_edge(e["from"], e["to"], relation="CITES")

        # Save graph
        from networkx.readwrite import json_graph
        graph_path.write_text(json.dumps(json_graph.node_link_data(G), indent=2))

        # Generate stats
        top_methods = sorted(method_counts.items(), key=lambda x: x[1], reverse=True)[:15]
        top_datasets = sorted(dataset_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        top_models = sorted(model_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        stats = f"""# Knowledge Graph Stats: {self.topic}
Generated: {datetime.now().isoformat()}

## Overview
- Nodes: {G.number_of_nodes()}
- Edges: {G.number_of_edges()}
- Papers: {sum(1 for _, d in G.nodes(data=True) if d.get('type') == 'paper')}
- Methods: {len(method_counts)}
- Datasets: {len(dataset_counts)}
- Models: {len(model_counts)}
- Claims: {sum(1 for _, d in G.nodes(data=True) if d.get('type') == 'claim')}

## Most Used Methods
| Method | Papers |
|--------|--------|
""" + "\n".join(f"| {m} | {c} |" for m, c in top_methods) + """

## Most Tested Models
| Model | Papers |
|-------|--------|
""" + "\n".join(f"| {m} | {c} |" for m, c in top_models) + """

## Most Used Datasets
| Dataset | Papers |
|---------|--------|
""" + "\n".join(f"| d | {c} |" for d, c in top_datasets) + """

## Isolated Papers
"""
        # Find isolated papers (no connections to methods/datasets)
        isolated = [n for n, d in G.nodes(data=True)
                    if d.get('type') == 'paper' and G.degree(n) <= 1]
        stats += f"Papers with ≤1 connection: {len(isolated)}\n"
        for n in isolated[:5]:
            stats += f"- {G.nodes[n].get('title', n)}\n"

        stats_path.write_text(stats)
        print(f"  Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
        return G

    # =========================================================================
    # STEP 10: VERIFY (Claims Matrix)
    # =========================================================================
    def build_claims_matrix(self, knowledge: Dict):
        """Build claim verification matrix."""
        print(f"\n[10/12] VERIFY: Building claims matrix...")

        matrix_path = self.output_dir / "claims_matrix.md"
        claims = knowledge.get("all_claims", [])
        if not claims:
            matrix_path.write_text("# Claims Matrix\n\nNo claims extracted.\n")
            print("  No claims to verify")
            return

        # Group similar claims using LLM
        claims_text = "\n".join(f"- [{c.get('paper_id','')}] ({c.get('year','')}) {c.get('text','')}"
                               for c in claims[:60])

        prompt = f"""Analyze these research claims and identify themes, agreements, and contradictions.

Claims:
{claims_text}

Return JSON:
{{
  "themes": [
    {{
      "claim": "summary of the claim theme",
      "supporting": ["paper_id1", "paper_id2"],
      "contradicting": ["paper_id3"],
      "confidence_pct": 75,
      "trend": "growing|declining|stable",
      "status": "ESTABLISHED|LIKELY TRUE|CONTESTED|LIKELY FALSE|EMERGING"
    }}
  ]
}}

Focus on finding CONTRADICTIONS — claims where papers disagree.
Return ONLY valid JSON."""

        try:
            result = self._llm_extract(prompt)
            result = result.strip()
            if result.startswith("```"):
                result = re.sub(r'^```\w*\n?', '', result)
                result = re.sub(r'\n?```$', '', result)
            themes = json.loads(result).get("themes", [])
        except Exception as e:
            self.errors.append(f"Claims matrix error: {e}")
            themes = []

        md = f"""# Claims Matrix: {self.topic}
Generated: {datetime.now().isoformat()}

| # | Claim | Supporting | Contradicting | Confidence | Trend | Status |
|---|-------|-----------|---------------|------------|-------|--------|
"""
        for i, t in enumerate(themes, 1):
            sup = ", ".join(t.get("supporting", [])[:3])
            con = ", ".join(t.get("contradicting", [])[:3]) or "—"
            md += f"| {i} | {t.get('claim', '')} | {sup} | {con} | {t.get('confidence_pct', '?')}% | {t.get('trend', '?')} | {t.get('status', '?')} |\n"

        md += f"\n\n## Raw Claims ({len(claims)} total)\n"
        for c in claims[:30]:
            md += f"- **[{c.get('year', '')}]** {c.get('text', '')} *(confidence: {c.get('confidence', '?')})* — {c.get('paper_id', '')}\n"

        matrix_path.write_text(md)
        contradictions = sum(1 for t in themes if t.get("contradicting"))
        print(f"  Claims matrix: {len(themes)} themes, {contradictions} with contradictions")

    # =========================================================================
    # STEP 11: TIMELINE
    # =========================================================================
    def build_timeline(self, papers: List[PaperMeta], knowledge: Dict):
        """Build temporal analysis."""
        print(f"\n[11/12] TIMELINE: Building temporal analysis...")

        timeline_path = self.output_dir / "timeline.md"

        # Papers per year
        year_counts = {}
        for p in papers:
            y = p.year or 0
            if y > 0:
                year_counts[y] = year_counts.get(y, 0) + 1

        # Method timeline
        method_years = {}
        for p in knowledge.get("papers", []):
            year = p.get("year")
            if not year:
                continue
            for m in p.get("methods", []):
                if m not in method_years:
                    method_years[m] = []
                method_years[m].append(year)

        md = f"""# Field Evolution: {self.topic}
Generated: {datetime.now().isoformat()}

## Papers Over Time
"""
        max_count = max(year_counts.values()) if year_counts else 1
        for y in sorted(year_counts.keys()):
            bar = "█" * int(year_counts[y] / max_count * 30)
            md += f"{y}: {bar} ({year_counts[y]} papers)\n"

        md += "\n## Method Timeline\n"
        md += "| Method | First Seen | Peak Year | Still Active | Papers |\n"
        md += "|--------|-----------|-----------|-------------|--------|\n"
        for m, years in sorted(method_years.items(), key=lambda x: -len(x[1])):
            if len(years) < 2:
                continue
            first = min(years)
            from collections import Counter
            yc = Counter(years)
            peak = yc.most_common(1)[0][0]
            active = "Growing" if max(years) >= CURRENT_YEAR - 1 else "Declining"
            md += f"| {m} | {first} | {peak} | {active} | {len(years)} |\n"

        # Emerging (last 12 months)
        md += "\n## Emerging (Last 12 months)\n"
        recent_methods = set()
        for p in knowledge.get("papers", []):
            if (p.get("year") or 0) >= CURRENT_YEAR - 1:
                for m in p.get("methods", []):
                    recent_methods.add(m)
        all_old_methods = set()
        for p in knowledge.get("papers", []):
            if (p.get("year") or 0) < CURRENT_YEAR - 1:
                for m in p.get("methods", []):
                    all_old_methods.add(m)
        new_methods = recent_methods - all_old_methods
        if new_methods:
            for m in new_methods:
                md += f"- **{m}** (new)\n"
        else:
            md += "- No exclusively new methods detected in last 12 months\n"

        timeline_path.write_text(md)
        print(f"  Timeline: {len(year_counts)} years, {len(method_years)} methods tracked")

    # =========================================================================
    # STEP 12: OUTPUT (Dossier)
    # =========================================================================
    def generate_dossier(self, papers: List[PaperMeta], full_papers: List[PaperFull], knowledge: Dict):
        """Generate final DOSSIER.md."""
        print(f"\n[12/12] OUTPUT: Generating dossier...")

        # Gather all info for LLM synthesis
        top10 = sorted(papers, key=lambda p: p.score, reverse=True)[:10]
        methods = knowledge.get("all_methods", [])[:20]
        models = knowledge.get("all_models", [])[:15]
        claims_text = "\n".join(f"- {c.get('text', '')}" for c in knowledge.get("all_claims", [])[:40])

        papers_summary = "\n".join(
            f"- [{p.year}] {p.title} (citations: {p.citation_count}, score: {p.score:.2f})"
            for p in top10
        )

        prompt = f"""You are synthesizing a research dossier on: "{self.topic}"

Based on {len(papers)} papers analyzed, here is the extracted knowledge:

TOP 10 PAPERS:
{papers_summary}

METHODS FOUND: {', '.join(methods)}
MODELS STUDIED: {', '.join(models)}

KEY CLAIMS:
{claims_text}

Write a comprehensive dossier with these sections:
1. FIELD OVERVIEW — What is this field about? Size, growth, key players
2. CURRENT CONSENSUS — What do most researchers agree on?
3. ACTIVE DEBATES — Where do researchers disagree?
4. CONTRADICTIONS — Claims that directly conflict
5. RESEARCH GAPS — What hasn't been studied?
6. EMERGING TRENDS — What's new in last 12 months?
7. KEY PAPERS — Top 10 must-read papers with 1-paragraph summaries
8. KNOWLEDGE GRAPH SUMMARY — Most connected entities
9. RECOMMENDED QUERIES — 10 RAG queries a report-writing agent should ask
10. META — Stats

Be specific, cite paper titles, and be opinionated about what matters.
Write in markdown. Be comprehensive but concise."""

        dossier_content = self._llm_extract(prompt, system="You are a senior research analyst. Write a structured, insightful research dossier in markdown.")

        # Add meta section
        elapsed = time.time() - self.start_time
        meta = f"""

---

## META — Pipeline Statistics
- **Topic:** {self.topic}
- **Papers discovered:** {len(papers)}
- **Papers analyzed:** {len(full_papers)}
- **Full text collected:** {sum(1 for p in full_papers if not p.abstract_only)}
- **Abstract only:** {sum(1 for p in full_papers if p.abstract_only)}
- **Methods found:** {len(knowledge.get('all_methods', []))}
- **Claims extracted:** {len(knowledge.get('all_claims', []))}
- **API cost:** ${self.cost.total_cost_usd:.4f}
- **Time:** {elapsed/60:.1f} minutes
- **Errors:** {len(self.errors)}
- **Generated:** {datetime.now().isoformat()}
"""

        dossier_path = self.output_dir / "DOSSIER.md"
        dossier_path.write_text(f"# Research Dossier: {self.topic}\n\n{dossier_content}\n{meta}")

        # README
        readme = f"""# Research Base: {self.topic}

Generated by `prepare.py` on {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Files
- `DOSSIER.md` — Main dossier for agents to read
- `papers/` — Full text of collected papers + metadata.json
- `embeddings/` — Vector store (ChromaDB + JSON fallback)
- `knowledge.json` — Extracted entities, methods, claims
- `citation_graph.json` — Citation network
- `graph.json` — NetworkX knowledge graph
- `graph_stats.md` — Human-readable graph analysis
- `claims_matrix.md` — Claim verification with contradictions
- `timeline.md` — Temporal field evolution

## Usage
```python
# Load embeddings for RAG
import json
data = json.load(open("embeddings/embeddings.json"))
chunks = data["chunks"]  # [{{"text": ..., "meta": ...}}]
embeddings = data["embeddings"]  # [[float, ...], ...]
```
"""
        (self.output_dir / "README.md").write_text(readme)

        # Run log
        run_log = {
            "topic": self.topic,
            "slug": self.slug,
            "depth": self.depth,
            "max_papers": self.max_papers,
            "papers_discovered": len(papers),
            "papers_analyzed": len(full_papers),
            "full_text": sum(1 for p in full_papers if not p.abstract_only),
            "abstract_only": sum(1 for p in full_papers if p.abstract_only),
            "cost": asdict(self.cost),
            "errors": self.errors,
            "elapsed_seconds": elapsed,
            "timestamp": datetime.now().isoformat()
        }
        (self.output_dir / "run_log.json").write_text(json.dumps(run_log, indent=2))

        print(f"\n{'='*60}")
        print(f"✅ DOSSIER COMPLETE: {dossier_path}")
        print(f"   Papers: {len(full_papers)} ({sum(1 for p in full_papers if not p.abstract_only)} full text)")
        print(f"   Cost: ${self.cost.total_cost_usd:.4f}")
        print(f"   Time: {elapsed/60:.1f} minutes")
        print(f"   Errors: {len(self.errors)}")
        print(f"{'='*60}")

    # =========================================================================
    # RUN
    # =========================================================================
    def run(self):
        """Execute the full pipeline."""
        print(f"\n{'='*60}")
        print(f"🚀 Research Preparation Pipeline")
        print(f"   Topic: {self.topic}")
        print(f"   Papers: {self.max_papers} | Depth: {self.depth}")
        print(f"   Output: {self.output_dir}")
        print(f"{'='*60}")

        # Step 1: Discover
        all_papers = self.discover()

        # Step 2: Filter
        top_papers = self.filter_papers(all_papers)

        # Step 3: Collect
        full_papers = self.collect_papers(top_papers)

        # Step 4-6: Chunk + Embed + Store
        self.build_vector_store(full_papers)

        # Step 7: Citation chains
        citation_data = self.build_citation_chains(top_papers)

        # Step 8: Extract knowledge
        knowledge = self.extract_knowledge(full_papers)

        # Step 9: Knowledge graph
        self.build_knowledge_graph(knowledge, citation_data)

        # Step 10: Claims matrix
        self.build_claims_matrix(knowledge)

        # Step 11: Timeline
        self.build_timeline(top_papers, knowledge)

        # Step 12: Dossier
        self.generate_dossier(top_papers, full_papers, knowledge)


def main():
    parser = argparse.ArgumentParser(description="Research Preparation Pipeline — Phase 0")
    parser.add_argument("topic", help="Research topic (e.g., 'LLM Trust Calibration')")
    parser.add_argument("--papers", type=int, default=50, help="Number of top papers to analyze (default: 50)")
    parser.add_argument("--depth", choices=["full", "quick"], default="full", help="Depth: full or quick")
    args = parser.parse_args()

    preparer = ResearchPreparer(topic=args.topic, max_papers=args.papers, depth=args.depth)
    preparer.run()


if __name__ == "__main__":
    main()

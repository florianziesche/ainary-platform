---
type: knowledge
last_verified: 2026-02-15
status: evergreen
created: 2026-02-01
tier: KNOWLEDGE
expires: 2027-02-19
---

# Research Paper Clustering Pipeline

*For analyzing 2000+ paper corpus to identify research gaps.*

---

## Pipeline Architecture

```
1. Data Ingestion (PDFs → structured JSON)
   └── PyPDF2 for text extraction
   
2. Problem Extraction (Claude API)
   └── Structured prompts for problem/solution extraction
   
3. Embedding Generation (Specter2)
   └── allenai/specter2 via sentence-transformers
   
4. Clustering (HDBSCAN on UMAP-reduced embeddings)
   └── min_cluster_size=10, min_samples=5
   
5. Visualization (Plotly 3D scatter)
   └── Interactive HTML export
```

---

## Key Technical Decisions

### Embedding Model: Specter2
- Specifically trained on scientific papers
- Better semantic capture than general models
- HuggingFace: `allenai/specter2`

### Dimensionality Reduction: UMAP
- Preserves both local AND global structure (better than t-SNE)
- Faster on large corpora
- Non-linear (better than PCA)

```python
umap.UMAP(
    n_components=2,        # Or 3 for 3D visualization
    n_neighbors=15,        # Balance local/global
    min_dist=0.1,          # Allow tight clusters
    metric='cosine',       # Semantic similarity
    random_state=42        # Reproducibility
)
```

### Clustering: HDBSCAN
- **No preset K needed** — finds natural groupings
- Handles irregular cluster shapes
- Identifies noise points

```python
hdbscan.HDBSCAN(
    min_cluster_size=10,           # Minimum papers per cluster
    min_samples=5,                 # Core point threshold
    metric='euclidean',            # On UMAP-reduced space
    cluster_selection_method='eom' # Excess of mass
)
```

---

## Why This Over Alternatives

| vs K-means | vs t-SNE | vs PCA |
|------------|----------|--------|
| No preset K | Better global structure | Non-linear |
| Non-spherical clusters | Faster on large corpora | Preserves neighborhoods |
| Noise detection | Reproducible | |

---

## Critical Insight

> "Keep embeddings high-dimensional (768+ dims) for clustering, only reduce to 3D for visualization."

---

## Paper URL Domains to Accept

```python
PAPER_DOMAINS = [
    'arxiv.org',
    'openreview.net',
    'aclanthology.org',
    'papers.nips.cc',
    'dl.acm.org',
    'ieeexplore.ieee.org',
    'proceedings.mlr.press'
]
```

---

*Source: [[Claude]] extraction (mangomedical) 2026-02-01*
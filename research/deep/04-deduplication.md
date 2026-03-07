# Deep Research Report: Deduplication
**Topic 4 of 22 — GAP Research for Ainary Research Network**
**Date:** 2026-03-06
**Researcher:** Mia ♔ (Single Agent, D-200)
**Sources Read:** 34 | **Saturation:** Reached at source 30 (3 consecutive no-new-info)

---

## BLUF (Bottom Line Up Front)

Deduplication is the single highest-leverage data preprocessing step for LLM training and knowledge systems. Duplicate training data causes **verbatim memorization** (>1% of LLM output copied from training data), **privacy leakage** (10× duplicated sequences are generated ~1000× more), **compute waste**, and **benchmark contamination** (8–11% inflated scores). The field has converged on **MinHash LSH** as the dominant fuzzy deduplication method (used by Llama 3, FineWeb, Dolma, The Pile), with **LSHBloom** (PVLDB 2025) achieving 12× faster runtime and 18× less disk space as a drop-in replacement. For knowledge graphs and RAG systems, deduplication is equally critical but underexplored — **DEG-RAG** (2025) shows that entity resolution alone drastically reduces graph size while improving QA performance. For Ainary's knowledge graph, the recommended architecture combines: (1) exact dedup via Bloom filters for ingestion, (2) MinHash LSH / LSHBloom for fuzzy document dedup, (3) embedding-based SemDeDup for semantic dedup of claims/facts, and (4) entity resolution for graph-level dedup.

---

## 1. Problem Definition & Why Deduplication Matters

### 1.1 The Scale of Duplication

Web-scraped datasets contain massive redundancy. Lee et al. (ACL 2022) found that in C4, a single 61-word English sentence was repeated **over 60,000 times**. After deduplication, they removed 19.4% of C4's content as exact-substring duplicates and 3.04% as near-duplicates.

**Key quantitative findings:**
- **>1% of unprompted LLM output** is copied verbatim from training data (Lee et al., 2022)
- **>4% of validation sets** overlap with training data in standard datasets (Lee et al., 2022)
- Deduplication reduces memorized text emission by **10×** (Lee et al., 2022)
- An **800M parameter model** can be degraded to **400M performance** by repeating just 0.1% of data 100 times (Hernandez et al., 2022)
- A sequence present **10 times** in training data is generated **~1000 times more often** than a singleton (Kandpal et al., ICML 2022)

### 1.2 Four Harms of Duplication

| Harm | Mechanism | Evidence |
|------|-----------|----------|
| **Compute waste** | Repeated examples provide zero new information but consume same compute | Zilliz 2025; every major pipeline doc |
| **Memorization & privacy** | Models memorize duplicated sequences, enabling extraction attacks | Carlini et al. ICLR 2023; Kandpal et al. 2022 |
| **Overfitting & degradation** | Data repetition damages induction heads, shifting from generalization to memorization | Hernandez et al. 2022 (Anthropic) |
| **Benchmark contamination** | Train-test overlap inflates scores by 8–11% | LSHBloom (PVLDB 2025); data contamination surveys |

### 1.3 Ainary Relevance

For a knowledge graph platform, deduplication operates at three levels:
1. **Document level:** Removing duplicate source documents before ingestion
2. **Claim/fact level:** Deduplicating extracted claims and triples
3. **Entity level:** Merging duplicate entity nodes (covered in Topic 3: Entity Resolution)

---

## 2. Taxonomy of Deduplication Methods

### 2.1 Three Strategies

| Strategy | How It Works | Precision | Cost | Best For |
|----------|-------------|-----------|------|----------|
| **Exact matching** | Cryptographic hash (MD5, SHA1) of full document or n-grams | Perfect for identical | Very low | Byte-identical duplicates |
| **Fuzzy/approximate** | MinHash, SimHash, LSH — probabilistic near-duplicate detection | High (tunable) | Moderate | Near-duplicates (formatting differences, boilerplate) |
| **Semantic** | Embedding-based clustering (SemDeDup, D4) | High for meaning | High (needs inference) | Semantically equivalent but textually different content |

### 2.2 Resolution Levels

- **Document-level:** Most common; entire documents compared (MinHash LSH)
- **Paragraph-level:** Used by Dolma, DataComp-LM; Bloom filter on paragraphs
- **Substring-level:** Suffix array approach (Lee et al.); finds repeated substrings of length ≥N
- **Line-level:** CCNet approach; SHA1 hashing per line (used by Llama 3)
- **N-gram level:** Big Friendly Filter (DataComp-LM); proportion of duplicated n-grams

---

## 3. Core Algorithms — Deep Technical Analysis

### 3.1 MinHash (Broder, 1997)

**The foundational algorithm.** Originally developed for AltaVista to detect duplicate web pages.

**How it works:**
1. Decompose each document into a set of shingles (character or word n-grams)
2. Apply k independent hash functions to each shingle set
3. For each hash function, retain the minimum hash value → produces a fixed-length MinHash signature
4. **Key property:** P(MinHash_i(A) = MinHash_i(B)) = Jaccard(A, B)

**Complexity:** O(k × |shingles|) per document for signature generation; comparing two signatures is O(k).

**Limitations:** Still requires O(N²) pairwise comparisons of signatures without LSH.

### 3.2 MinHash LSH (Leskovec et al.)

**The workhorse of modern deduplication pipelines.**

**Extension over MinHash:**
1. Arrange MinHash signatures into a matrix (documents × hash functions)
2. Divide signature rows into **b bands** of **r rows** each
3. Hash each band independently into buckets
4. If two documents collide in **any** band → candidate pair
5. **S-curve probability:** P(candidate) = 1 - (1 - s^r)^b where s = Jaccard similarity

**Tuning trade-offs:**
- More bands (b↑) → higher recall, more false positives
- More rows per band (r↑) → higher precision, more false negatives
- Standard settings: Jaccard threshold 0.7–0.8, using 128–256 hash functions

**Used by:** Llama 3, FineWeb, The Pile, RedPajama, Dolma, DataComp-LM (all major open LLM datasets)

**Scalability bottleneck:** The LSH index grows extremely large. For peS2o (39M docs): >35 hours on 32-core node, >200GB disk. For DOLMA (5B docs): the index would reach ~277TB.

### 3.3 SimHash (Charikar, 2002)

**Alternative to MinHash — uses cosine similarity instead of Jaccard.**

**How it works:**
1. Extract features (words, n-grams) with weights (TF-IDF)
2. Hash each feature to a b-bit value (typically 64-bit)
3. For each bit position: if bit=1, add weight; if bit=0, subtract weight
4. Final fingerprint: each bit = sign of accumulated vector at that position
5. **Similarity:** Hamming distance of fingerprints ≈ cosine distance

**Key properties:**
- Produces a single compact fingerprint (64 bits) per document
- Comparison is O(1): XOR + popcount
- **Typical thresholds:** distance ≤3 → 95%+ similar; distance ≤10 → ~84–94%; distance >30 → unrelated

**Advantage over MinHash:** Much smaller representation (64 bits vs. hundreds of hash values). Ideal when storage is critical.
**Disadvantage:** Less accurate for set-similarity; MinHash is theoretically better for Jaccard estimation.

**Used by:** Google's web crawler for duplicate web page detection (Manku et al., WWW 2007).

### 3.4 Suffix Array / ExactSubstr (Lee et al., 2022)

**Finds all repeated substrings of length ≥ threshold in a corpus.**

**How it works:**
1. Concatenate all documents into one massive byte array
2. Build a suffix array (sorted array of all suffixes) — O(N) time, O(N) space
3. Walk the suffix array to find adjacent entries sharing long prefixes
4. Output all positions where substring of length ≥ threshold is duplicated

**Implementation:** Google Research released a Rust implementation supporting 64-bit pointers for datasets >4GB. Requires ~2× dataset size in RAM for the suffix array.

**Unique capability:** Finds **substring-level** duplicates that document-level methods miss entirely. A document may contain a 200-word duplicated passage even if the overall document is unique.

**Limitation:** Memory-intensive (suffix array = 8× document size for 64-bit pointers); requires the entire corpus in memory or sophisticated chunking.

### 3.5 Bloom Filter Approaches

**Space-efficient exact matching.** Used by Dolma, RedPajama, DataComp-LM.

**How it works:**
1. Hash each document/paragraph/n-gram with k hash functions
2. Set corresponding bits in a bit array
3. On insertion: if all k bits already set → duplicate
4. **False positive rate:** (1 - e^(-kn/m))^k where n=items, m=array size

**Variants:**
- **Dolma:** Bloom filter on paragraph hashes for exact paragraph dedup
- **DataComp-LM Big Friendly Filter:** Bloom filter on n-grams; if proportion of duplicated n-grams exceeds threshold, remove document
- **CCNet:** SHA1 hashing per line, stored for comparison (not strictly Bloom, but same principle)

### 3.6 LSHBloom (Khan et al., PVLDB 2025) ⭐ SOTA

**The most important recent advance — drop-in replacement for MinHash LSH.**

**Key insight:** Replace the expensive prefix-tree/suffix-array LSH index with lightweight Bloom filters. One Bloom filter per band of the MinHash signature matrix.

**Performance on peS2o (39M academic documents):**
- **12× faster** than MinHash LSH
- **18× less disk space** (11GB vs. 200GB)
- **Near-zero false positive increase** (as low as 1e-5)
- Same deduplication quality (precision/recall/F1)

**Scaling extrapolation:** At several billion documents, LSHBloom promises **250% speedup** and **54× space advantage** over traditional MinHash LSH.

**Why it matters:** Makes high-quality fuzzy deduplication tractable at internet scale without sacrificing accuracy. Previously, only heuristic methods (exact hash, CCNet line-dedup) could handle billions of documents.

### 3.7 SemDeDup (Abbas et al., 2023)

**Semantic deduplication using pre-trained embeddings.**

**How it works:**
1. Embed each document using a pre-trained model (e.g., CLIP, sentence-transformers)
2. Cluster embeddings with k-means into k clusters
3. Within each cluster, identify pairs with cosine similarity above threshold
4. Remove semantic duplicates (keeping one representative)

**Results on LAION (vision-language):**
- Can remove **50% of data** with minimal performance loss → halves training time
- Performance **increases out of distribution** after dedup
- On C4 (text): improves over prior approaches while providing efficiency gains

**Integration:** NVIDIA NeMo Curator includes GPU-accelerated SemDeDup implementation.

**Limitation:** Requires running a pre-trained model for inference on every document → expensive at scale. The D4 paper (Tirumala et al., NeurIPS 2023) extends this with diversification, achieving **20% training efficiency gains** and **up to 2% downstream accuracy improvement**.

---

## 4. What Major LLMs Actually Do

| Model | Dedup Method | Details |
|-------|-------------|---------|
| **Llama 3** | MinHash + line-level (CCNet) + URL dedup | MinHash over entire dataset; CCNet for lines repeated >6×; URL dedup for web data |
| **FineWeb** (HuggingFace) | MinHash LSH | Within-dump dedup effective; cross-dump dedup found NOT helpful (surprising finding) |
| **FineWeb2** | MinHash LSH | Extended to 1000+ languages, 20TB |
| **Dolma** (OLMo) | Bloom filter paragraph dedup | Exact matching on paragraph hashes |
| **DataComp-LM** | Big Friendly Filter (Bloom on n-grams) | Dual document + paragraph level; threshold-based |
| **RedPajama** | Bloom filter (exact) + MinHash LSH (fuzzy) | Both approaches combined |
| **The Pile** | MinHash LSH | Fuzzy deduplication |
| **RefinedWeb** (Falcon) | MinHash LSH | Outperformed curated corpora with web data only |
| **C4** | Heuristic only (line-level) | No true dedup; just quality filtering. Known to contain massive duplicates |
| **SlimPajama** | MinHash LSH | 627B token cleaned + deduplicated version of RedPajama |

**Key insight from FineWeb:** Deduplication **within** a CommonCrawl dump was effective, but deduplication **across** dumps was not beneficial. This is counterintuitive and suggests that cross-dump duplicates may actually be high-quality content worth keeping.

---

## 5. Scaling & Performance

### 5.1 GPU Acceleration

**FED Framework (Son et al., 2025):**
- GPU-accelerated MinHash LSH for GPU clusters
- **107× faster** than CPU-based SlimPajama dedup (64 CPU cores)
- **6.3× faster** than NVIDIA NeMo Curator GPU implementation
- MinHash signature generation: **260× speedup** over CPU baseline
- 1.2 trillion tokens deduplicated in **6 hours** on 4 nodes (16 GPUs)
- Maintains Jaccard similarity >0.96 vs. standard MinHash

**NVIDIA NeMo Curator:**
- Three dedup approaches: exact (MD5), fuzzy (MinHash LSH), semantic (SemDeDup)
- All GPU-accelerated via RAPIDS/cuDF
- Production-grade, integrated with NeMo training pipeline

**Milvus 2.6 (Zilliz):**
- Native MinHash LSH as first-class indexing primitive
- uint32 vector support (critical: float32 loses precision for MinHash values >16M)
- Processed 30GB files with 780-dim int32 signatures in **4 minutes** (vs. 15-minute requirement)
- Scales horizontally across terabytes

### 5.2 Scaling Laws for Repeated Data

**Hernandez et al. (Anthropic, 2022) — Critical findings:**
- **Double descent phenomenon:** Repeated data causes test loss to increase midway through training, then partially recover
- **Disproportionate harm:** 0.1% of data repeated 100× degrades 800M model to 400M performance
- **Mechanistic cause:** Data repetition damages induction heads (key generalization circuits), shifting model capacity from generalization to memorization
- **Implication:** Even imperfect deduplication is enormously valuable

**Muennighoff et al. (NeurIPS 2023) — Data-constrained scaling:**
- Training with up to **4 epochs** of repeated data yields negligible changes to loss vs. unique data
- Beyond 4 epochs: diminishing returns accelerate rapidly
- Data-constrained scaling laws suggest training **smaller models for more epochs** rather than larger models on repeated data

---

## 6. Deduplication for Knowledge Graphs & RAG

### 6.1 The Underexplored Frontier

Most dedup research focuses on LLM training data. For knowledge graphs and RAG systems, dedup is equally critical but far less studied.

**DEG-RAG (Zheng et al., 2025) — First comprehensive treatment:**
- Problem: LLM-generated KGs contain massive noise — redundant entities and unreliable relations
- GraphRAG, LightRAG, HippoRAG all "rely on string-matching heuristics to merge similar entities, leaving many duplicates unresolved"
- **Solution:** Two-stage denoising:
  1. **Entity resolution:** Eliminates redundant entities (blocking + embedding similarity + merging)
  2. **Triple reflection:** Removes erroneous relations using LLM verification
- **Result:** "Straightforward approach not only drastically reduces graph size but also consistently improves QA performance across diverse popular Graph-based RAG variants"

### 6.2 OpenCTI — Production KG Dedup

OpenCTI (cyber threat intelligence platform) implements deterministic deduplication in its KG:

**Approach:** Generate deterministic IDs from "ID Contributing Properties" per entity type:
- Attack Pattern: (name OR alias) AND optional x_mitre_id
- Campaign: name OR alias
- Indicator: pattern OR alias

**Relationship dedup:** Based on type + source + target + time window (±30 days)

**Name/alias management:** Names and aliases form a set of unique values — no overlap allowed. This prevents the same entity from existing under different names.

**Key insight for Ainary:** Deterministic ID generation from canonical properties is simple but effective for structured entities. Combined with embedding-based similarity for unstructured text, this provides multi-level dedup.

### 6.3 Claim-Level Dedup for Knowledge Graphs

For Ainary's claim-based knowledge graph, deduplication of extracted claims is a distinct problem:
- **Exact claim dedup:** Hash-based matching of normalized claim text
- **Semantic claim dedup:** Embedding similarity between claims (same as SemDeDup but at claim granularity)
- **Entailment-based dedup:** If claim A entails claim B and vice versa → merge (bidirectional NLI)
- **Graph-structural dedup:** If two claims have the same subject, predicate, and object (after entity resolution) → merge

---

## 7. Practical Tooling Landscape

### 7.1 Open-Source Tools

| Tool | Language | Methods | Scale | Notes |
|------|----------|---------|-------|-------|
| **text-dedup** (ChenghaoMou) | Python | MinHash, SimHash, Bloom Filter, Suffix Array | Medium-Large | All-in-one; HuggingFace integration; most popular |
| **deduplicate-text-datasets** (Google) | Rust + Python | Suffix Array (ExactSubstr), NearDup | Large | Original Lee et al. implementation; very fast |
| **datasketch** | Python | MinHash, LSH, HyperLogLog, Weighted MinHash | Medium | Library-level; widely used as building block |
| **NeMo Curator** (NVIDIA) | Python/CUDA | Exact, MinHash LSH, SemDeDup | Very Large (GPU) | Production-grade; GPU-accelerated |
| **FED** | CUDA/Python | MinHash LSH (GPU-optimized) | Very Large (GPU) | 107× faster than CPU baseline |
| **Milvus 2.6** | Go/C++ | MinHash LSH (native indexing) | Trillion-scale | Database-integrated dedup |
| **Trafilatura** | Python | SimHash | Medium | Web scraping + dedup integrated |

### 7.2 Evaluation Benchmarks

The Springer Nature evaluation (2025) compared 5 algorithms on large text corpora:
- **MinHash/LSH:** Best overall precision-recall balance
- **Exact Hashes:** Perfect precision, zero recall for near-duplicates
- **SimHash:** Good speed, slightly lower recall than MinHash
- **Scalable Bloom Filter:** Good for exact matching, no fuzzy capability
- **Suffix Array:** Best for substring-level dedup, highest memory cost

---

## 8. Open Problems & Research Frontiers

### 8.1 Cross-Domain Dedup
FineWeb found cross-dump dedup unhelpful. But for knowledge graphs ingesting from multiple domains, cross-source dedup is essential. No consensus on best approach.

### 8.2 Semantic Dedup at Scale
SemDeDup requires embedding inference on every document — too expensive for internet-scale. LSHBloom solves the fuzzy-matching bottleneck but not the semantic gap.

### 8.3 Claim-Level Dedup
No standard benchmark or method for deduplicating extracted claims/facts. This is a gap Ainary could fill.

### 8.4 Incremental Dedup
Most methods assume batch processing. For a growing knowledge graph, incremental dedup (checking new documents against existing corpus) is needed. MinHash LSH supports this but at increasing cost.

### 8.5 Multilingual Dedup
FineWeb2 extended dedup to 1000+ languages, but cross-lingual dedup (same content in different languages) remains largely unsolved.

### 8.6 Dedup + Quality Filtering
D4 showed that dedup + diversification (selecting diverse data after dedup) yields 20% training efficiency gains. The interaction between dedup and quality filtering is underexplored.

---

## 9. Recommended Architecture for Ainary

### 9.1 Ingestion Pipeline (4-Stage Dedup)

```
Stage 1: URL/Metadata Dedup
  → Exact match on URL, DOI, or source ID
  → Fast, removes obvious duplicates

Stage 2: Exact Content Dedup
  → Bloom filter on document/paragraph hashes
  → Catches byte-identical content from different sources

Stage 3: Fuzzy Document Dedup
  → LSHBloom (or MinHash LSH if <100M docs)
  → Jaccard threshold 0.8, 128 hash functions
  → Catches near-duplicates (formatting, boilerplate differences)

Stage 4: Semantic Claim Dedup
  → After claim extraction: embed claims with sentence-transformer
  → Cluster + cosine similarity within clusters (SemDeDup approach)
  → Merge semantically equivalent claims
```

### 9.2 Graph-Level Dedup (Continuous)

```
Entity Resolution (from Topic 3):
  → SBERT blocking + pairwise similarity + graph clustering

Triple Dedup:
  → After entity resolution, merge triples with same (resolved_subject, predicate, resolved_object)
  → Confidence aggregation: keep highest confidence, merge sources

Claim Dedup:
  → Bidirectional NLI between claims within same topic cluster
  → If mutual entailment > 0.9 → merge
```

### 9.3 Technology Choices

| Component | Recommended | Alternative | Why |
|-----------|------------|-------------|-----|
| Document fuzzy dedup | LSHBloom | MinHash LSH via text-dedup | 12× faster, 18× less disk; same quality |
| Exact dedup | Bloom filter | SHA256 hash | Space-efficient; built into most tools |
| Semantic dedup | SemDeDup via NeMo Curator | Custom SBERT + k-means | GPU-accelerated; proven at scale |
| Claim dedup | Custom (SBERT + NLI) | — | No off-the-shelf solution exists |
| Substring dedup | Suffix array (Google Rust impl) | — | Only method for substring-level |
| Graph entity dedup | See Topic 3 recommendations | — | Llama-8B + SBERT + graph clustering |

---

## 10. Source Registry

| # | Source | Type | Year | Admiralty | EIJA | Key Contribution |
|---|--------|------|------|-----------|------|------------------|
| 1 | Lee et al., "Deduplicating Training Data Makes Language Models Better" (ACL 2022) | Paper | 2022 | A1 | E-confirmed | Foundational paper; ExactSubstr + NearDup; >1% verbatim memorization |
| 2 | Khan et al., "LSHBloom: Internet-Scale Text Deduplication" (PVLDB 2025) | Paper | 2025 | A1 | E-confirmed | 12× faster, 18× less disk than MinHash LSH; SOTA |
| 3 | Abbas et al., "SemDeDup" (arXiv 2023) | Paper | 2023 | A2 | I-likely | Semantic dedup via embeddings; 50% data removal with minimal loss |
| 4 | Tirumala et al., "D4: Document De-Duplication and Diversification" (NeurIPS 2023) | Paper | 2023 | A1 | E-confirmed | 20% training efficiency gains; diversification beyond dedup |
| 5 | Hernandez et al., "Scaling Laws and Interpretability of Learning from Repeated Data" (Anthropic 2022) | Paper | 2022 | A1 | E-confirmed | 0.1% data repeated 100× → 2× model degradation; damages induction heads |
| 6 | Kandpal et al., "Deduplicating Training Data Mitigates Privacy Risks" (ICML 2022) | Paper | 2022 | A1 | E-confirmed | 10× duplicated → ~1000× more generated; privacy attack near-chance on deduped data |
| 7 | Carlini et al., "Quantifying Memorization Across Neural Language Models" (ICLR 2023) | Paper | 2023 | A1 | E-confirmed | Model size, duplication, context length impact extraction; memorization grows superlinearly |
| 8 | Muennighoff et al., "Scaling Data-Constrained Language Models" (NeurIPS 2023) | Paper | 2023 | A1 | E-confirmed | ≤4 epochs negligible loss; data-constrained scaling laws |
| 9 | Broder, "On the Resemblance and Containment of Documents" (1997) | Paper | 1997 | A1 | E-confirmed | Foundational: MinHash, shingling, Jaccard similarity for document comparison |
| 10 | Charikar, "Similarity Estimation via Random Projections" (2002) | Paper | 2002 | A1 | E-confirmed | SimHash algorithm; cosine similarity via random projections |
| 11 | Manku et al., "Detecting Near-Duplicates for Web Crawling" (WWW 2007) | Paper | 2007 | A1 | E-confirmed | SimHash for multi-billion page web dedup at Google |
| 12 | Penedo et al., "FineWeb Datasets" (NeurIPS 2024) | Paper | 2024 | A1 | E-confirmed | Within-dump dedup effective; cross-dump dedup NOT helpful |
| 13 | Penedo et al., "FineWeb2" (arXiv 2025) | Paper | 2025 | A2 | I-likely | Pipeline scaled to 1000+ languages, 20TB |
| 14 | Zilliz, "Data Dedup at Trillion Scale" (Blog 2025) | Blog | 2025 | B3 | I-likely | Practical MinHash LSH in Milvus 2.6; uint32 precision issues |
| 15 | Son et al., "FED: Fast and Efficient Dataset Deduplication" (arXiv 2025) | Paper | 2025 | A2 | I-likely | GPU-accelerated: 107× faster CPU, 6.3× faster NeMo; 1.2T tokens in 6h |
| 16 | Google Research, "deduplicate-text-datasets" (GitHub) | Tool | 2022 | A2 | E-confirmed | Rust implementation of suffix array dedup; ExactSubstr + NearDup |
| 17 | ChenghaoMou, "text-dedup" (GitHub/PyPI) | Tool | 2023 | B2 | I-likely | All-in-one Python toolkit: MinHash, SimHash, Bloom, Suffix Array |
| 18 | datasketch library (ekzhu) | Tool | — | B2 | I-likely | Python library: MinHash, LSH, HyperLogLog; widely used building block |
| 19 | NVIDIA NeMo Curator | Tool | 2024 | A3 | I-likely | GPU-accelerated exact, fuzzy, semantic dedup; production-grade |
| 20 | OpenCTI Documentation, "Deduplication" | Docs | — | B2 | E-confirmed | Production KG dedup: deterministic IDs from contributing properties |
| 21 | Huaman et al., "Duplication Detection in Knowledge Graphs" (EKAW 2020) | Paper | 2020 | B2 | I-likely | Survey of DD methods/tools for KGs; DD workflow proposal |
| 22 | Zheng et al., "DEG-RAG: Denoising KGs for RAG" (arXiv 2025) | Paper | 2025 | A2 | I-likely | Entity resolution + triple reflection for LLM-generated KGs |
| 23 | Springer Nature, "Evaluation of Document Deduplication Algorithms" (2025) | Paper | 2025 | A2 | E-confirmed | Comparative eval of 5 algorithms on large text corpora |
| 24 | SimHash explainer (dev.to, 2025) | Article | 2025 | C3 | A-unknown | Clear practical explanation of SimHash algorithm, thresholds |
| 25 | Preferred Networks, "Improve MinHashLSH for Dedup" (Blog 2025) | Blog | 2025 | B3 | I-likely | Independent validation of Bloom filter integration with MinHash LSH |
| 26 | Soldaini et al., "Dolma" dataset documentation | Docs | 2024 | A2 | E-confirmed | Bloom filter paragraph dedup in practice |
| 27 | Li et al., "DataComp-LM / DCLM" | Paper | 2024 | A1 | E-confirmed | Big Friendly Filter for n-gram dedup; dual document+paragraph level |
| 28 | DatologyAI, "Curating Our Way to SOTA Text Dataset" (Blog) | Blog | 2025 | B3 | I-likely | Practical insights on dedup in LLM data pipelines; FineWeb cross-dump finding |
| 29 | Silcock et al., "Noise-robust De-duplication at Scale" (ICLR 2023) | Paper | 2023 | A2 | I-likely | Robust dedup for noisy/OCR'd historical documents |
| 30 | conanhujinming, "High-Performance Text Dedup Toolkit" (GitHub) | Tool | 2024 | B3 | I-likely | CDC + SimHash pipeline; multi-stage approach |
| 31 | Xia et al., "FastCDC" (USENIX ATC 2016, IEEE TPDS 2020) | Paper | 2020 | A2 | E-confirmed | Content-Defined Chunking: 3-10× faster than Rabin-based CDC |
| 32 | Kili Technology, "What Can We Learn from FineWeb" (Blog 2024) | Blog | 2024 | C3 | I-likely | FineWeb insights: meticulous curation, rigorous filtering |
| 33 | Data contamination survey (arxiv 2025) | Paper | 2025 | A2 | I-likely | Comprehensive survey on benchmark leakage; dedup as mitigation |
| 34 | Wikipedia, "MinHash" | Reference | — | C2 | E-confirmed | Historical context: originally used by AltaVista search engine |

---

## 11. Confidence & Gaps

**Confidence: 92%** — High confidence in algorithmic landscape and practical recommendations. The field is well-documented with many production deployments.

**Remaining uncertainties:**
- Claim-level dedup benchmarks don't exist → Ainary would need to create one
- Optimal Jaccard threshold for knowledge graph dedup (vs. LLM training data) unclear
- Interaction between entity resolution and claim dedup under-studied
- Cross-lingual dedup for multilingual knowledge graphs is an open problem

**Connection to other topics:**
- **Topic 3 (Entity Resolution):** Dedup at entity level → same techniques, different granularity
- **Topic 1 (Contradiction Detection):** After dedup, remaining claims should be checked for contradictions
- **Topic 2 (Verified Truths):** Deduplicated claims feed into consensus/verification pipeline
- **Topic 6 (Hallucination Prevention):** Dedup reduces memorization → reduces one source of hallucination

---

*Generated following Research Protocol (RESEARCH-PROTOCOL.md). Hypothesis-first, MECE structure, saturation-based stopping.*

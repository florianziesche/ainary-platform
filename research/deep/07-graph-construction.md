# Topic 7: Knowledge Graph Construction
## Deep Research Report — Ainary Research Network

**Date:** 2026-03-06
**Sources:** 33 (saturation at 29)
**Status:** COMPLETE
**BLUF:** LLM-driven KG construction has shifted from rigid pipeline systems to generative, schema-adaptive frameworks. The field is split between **schema-based** (precision, consistency) and **schema-free** (flexibility, scalability) paradigms. **EDC (Extract-Define-Canonicalize)** is the current SOTA framework (EMNLP 2024), outperforming fine-tuned models on large schemas without parameter tuning. **GraphRAG** (Microsoft) established the dominant paradigm for LLM→KG→RAG pipelines. **AutoSchemaKG** achieves 92% alignment with human-crafted schemas autonomously. **KGGEN** (NeurIPS 2025) solves entity/relation clustering post-extraction. Key gap for Ainary: no existing system constructs **claim-level** knowledge graphs with provenance, confidence scoring, and cross-source consistency — all systems extract entity-relation triples, not verified claims.

---

## 1. TAXONOMY OF KG CONSTRUCTION APPROACHES

### 1.1 Classical Three-Layer Pipeline
| Layer | Function | Traditional Methods |
|-------|----------|-------------------|
| **Ontology Engineering** | Define schema (classes, properties, constraints) | Manual (Protégé), METHONTOLOGY, NeOn |
| **Knowledge Extraction** | Extract entities, relations, attributes from text | Rule-based → BiLSTM-CRF → Transformers |
| **Knowledge Fusion** | Integrate, deduplicate, align across sources | Lexical similarity, embedding alignment |

**Three enduring challenges** (Bian et al. 2025 survey):
1. Scalability and data sparsity
2. Expert dependency and rigidity
3. Pipeline fragmentation → cumulative error propagation
- **Source:** Bian et al. 2025, arxiv 2510.20345 [A2/C5]

### 1.2 LLM-Driven Paradigm Shift
LLMs enable three key mechanisms:
1. **Generative knowledge modeling:** Synthesize structured representations directly from text
2. **Semantic unification:** Integrate heterogeneous sources via natural language grounding
3. **Instruction-driven orchestration:** Coordinate via prompt-based interaction

Two complementary paradigms:
| Paradigm | Focus | Strengths | Weaknesses |
|----------|-------|-----------|------------|
| **Schema-based** | Structure, normalization, consistency | Precise, interpretable, governed | Rigid, limited cross-domain |
| **Schema-free** | Flexibility, adaptability, open discovery | Scalable, no expert dependency | Noisy, requires canonicalization |

- **Source:** Bian et al. 2025 survey [A2/C5]

---

## 2. ONTOLOGY CONSTRUCTION

### 2.1 Top-Down: LLMs as Ontology Assistants

#### Competency Question (CQ)-Based
- **Ontogenia** (Lippolis et al. 2025): Metacognitive Prompting + Ontology Design Patterns → self-reflection during synthesis
- **CQbyCQ** (Saeedizade & Blomqvist 2024): Directly translate CQs → OWL schemas
- LLMs now approach quality of **junior human modelers** for ontology design
- **Source:** Lippolis et al. 2025; Saeedizade & Blomqvist 2024 [A2/C5]

#### Natural Language-Based
- **LLMs4OL** (Giglou et al. 2023): Verified LLMs' capacity for concept identification, relation extraction, semantic pattern induction
- **NeOn-GPT** (Fathallah et al. 2025): End-to-end prompt-driven workflows for complex scientific domains
- **LKD-KGC** (Sun et al. 2025): Rapid schema induction via entity type clustering
- **Source:** Various [A2-B3/C4-5]

### 2.2 Bottom-Up: Ontologies FOR LLMs

#### GraphRAG Paradigm (Microsoft, Edge et al. 2024)
**The most influential KG construction framework of 2024:**
- Two-stage pipeline: (1) LLM extracts entity knowledge graph from documents → (2) Leiden community detection → community summaries
- Uses **rich descriptive text** for nodes (not concise triples) — aligned with LLM capabilities
- Query-focused summarization: community summaries → partial responses → final summary
- Open-sourced 2024, widely adopted
- **Key difference from traditional KGs:** Heterogeneous, descriptive nodes vs. concise triples
- **Source:** Edge et al. 2024, arxiv 2404.16130 [A1/C6]

#### OntoRAG (Tiwari et al. 2025)
- Data-driven ontology construction from instance-level graphs
- "Data-to-schema" process: extract open KG → cluster → generalize to ontological concepts
- **Source:** Tiwari et al. 2025 [B3/C4]

### 2.3 Enterprise Ontology Construction

#### OntoEKG (2026)
- LLM-driven pipeline for enterprise KGs from unstructured data
- Two phases: Extraction (classes + properties) → Entailment (hierarchy construction) → RDF serialization
- Best result: F1 = 0.724 (fuzzy match) in Data domain
- **Identified limitations:** Scope definition is hard for LLMs; confuse individuals vs classes; hierarchy directionality errors
- **Critical gap:** No comprehensive benchmark for end-to-end ontology construction from text
- **Source:** OntoEKG 2026, arxiv 2602.01276 [A2/C5]

---

## 3. KNOWLEDGE EXTRACTION

### 3.1 Schema-Based Extraction

#### Static Schema-Driven
- **KARMA** (Lu & Wang 2025): Multi-agent architecture for schema-guided extraction
- **Kommineni et al. 2024:** CQ generation → ontology → ABox population under strict supervision
- **ODKE+** (Khorshidi et al. 2025): Ontology snippets as dynamic context-aware prompts
- **Source:** Various [A2-B3/C4-5]

#### Dynamic Schema-Based
- **AutoSchemaKG** (Bai et al. 2025, HKUST): **92% semantic alignment with human-crafted schemas, zero manual intervention**
  - Induces schemas from large-scale corpora via unsupervised clustering
  - Multi-stage prompts tailored to different relation types
  - Schema evolves iteratively with extracted content
  - ATLAS KG family: fully autonomous, no predefined schemas
- **AdaKGC** (Ye et al. 2023): Schema-Enriched Prefix Instruction + Schema-Constrained Dynamic Decoding → adapts without retraining
- **Source:** Bai et al. 2025, arxiv 2505.23628 [A1/C6]; Ye et al. 2023 [A2/C5]

### 3.2 Schema-Free Extraction

#### EDC — Extract-Define-Canonicalize (Zhang & Soh, EMNLP 2024)
**Current SOTA for LLM-based KGC:**
1. **Extract:** Open information extraction via LLM (few-shot prompting)
2. **Define:** LLM generates natural language definitions for each schema component
3. **Canonicalize:** Standardize via vector similarity + LLM verification
   - Target Alignment mode (with existing schema)
   - Self Canonicalization mode (no schema → auto-generate)
4. **+Refinement (EDC+R):** Schema Retriever retrieves relevant schema elements → RAG-like improvement

**Key results:**
- Outperforms fine-tuned models (REGEN, GenIE, REBEL) on large schemas
- Scales to 200+ relation types (prior LLM methods limited to <10)
- No parameter tuning needed
- Benchmarks: WebNLG (159 relation types), REBEL (200), Wiki-NRE (45)
- **Source:** Zhang & Soh 2024, EMNLP [A1/C6]

#### KGGEN (Mo et al. 2025, NeurIPS)
- Multi-stage: (1) Extract entities + relations → (2) Aggregate across sources → (3) Iterative clustering
- LLM-guided clustering merges equivalent entities/relations beyond surface matching
- Progressive triple extraction + semantic grouping
- Open-source: `kg-gen` library
- **Source:** Mo et al. 2025 [A1/C6]

#### REBEL (Babelscape, EMNLP 2021)
- Seq2seq model (BART-based) for end-to-end relation extraction
- 200+ relation types
- Still widely used as baseline and in production pipelines
- **Source:** Cabot & Navigli 2021 [A1/C6]

---

## 4. KNOWLEDGE FUSION & POST-PROCESSING

### 4.1 Entity Alignment
- Classical: Lexical + structural similarity (Zeng et al. 2021)
- Modern: Embedding-based alignment in shared vector spaces (Zhu et al. 2024)
- LLM-enhanced: Semantic cues for alignment robustness (Liu et al. 2022)
- **Source:** Various [A2/C5]

### 4.2 Canonicalization Challenge
- Core problem: Multiple semantically equivalent relations ("profession" / "job" / "occupation")
- Clustering-based methods prone to over-generalization (CESI puts "is brother of" and "was professor of" in same cluster)
- EDC's LLM-verified canonicalization alleviates this
- **Source:** EDC paper [A1/C6]

### 4.3 Quality Evaluation

#### Hallucination in KG Construction (Ghanem et al. 2025)
- KG construction from text suffers from both **hallucination** (invented triples) and **omission** (missed triples)
- Proposed metrics: hallucination rate + omission rate + graph similarity
- Fine-tuned models improve accuracy but **worse generalization**
- **Source:** Ghanem et al. 2025, arxiv 2502.05239 [A2/C5]

#### GraphEval (Sansford et al. 2024, Amazon)
- KG-based LLM hallucination evaluation framework
- Identifies specific triples prone to hallucination
- More granular than sentence-level approaches
- **Source:** Sansford et al. 2024 [A2/C5]

---

## 5. PRODUCTION-READY TOOLS & PIPELINES

| Tool/System | Type | Key Feature | Year |
|-------------|------|-------------|------|
| **GraphRAG** (Microsoft) | Open-source pipeline | Community detection + summaries | 2024 |
| **LLMGraphTransformer** (LangChain/Neo4j) | Library module | Simple text→graph API | 2024 |
| **Neo4j LLM Graph Builder** | Application | UI-driven graph construction | 2024 |
| **LightRAG** | Framework | 10× token reduction vs GraphRAG | 2024 |
| **REBEL** (Babelscape) | Model | End-to-end seq2seq extraction | 2021 |
| **EDC** (NUS) | Framework | Schema-free + canonicalization | 2024 |
| **KGGEN/kg-gen** | Library | Extract + aggregate + cluster | 2025 |
| **AutoSchemaKG/ATLAS** | Framework | Fully autonomous, no schema needed | 2025 |
| **ATOM** (formerly iText2KG) | Framework | Temporal KG, incremental updates | 2025 |

### Cost Considerations
- Open-source LLMs: ~$0.83/M tokens vs proprietary ~$6.03/M tokens (7.3× cheaper)
- GraphRAG is computationally expensive → LightRAG achieves comparable accuracy with 10× fewer tokens
- LinkedIn's GraphRAG: Reduced ticket resolution from 40 to 15 hours (63% improvement)
- **Source:** whatllm.org 2025; Branzan 2025 [B3/C4]

---

## 6. BENCHMARKS

| Benchmark | Task | Schema Size | Year |
|-----------|------|-------------|------|
| **Text2KGBench** | Ontology-driven KG from text | Ontology-guided | ISWC 2023 |
| **WebNLG+2020** | Semantic parsing (text↔triples) | 159 relation types | 2020 |
| **REBEL** | Relation extraction | 200+ types | 2021 |
| **Wiki-NRE** | Relation extraction | 45 types | 2019 |
| **OSKGC** | Ontology schema KG construction | Instance-level | 2025 |
| **OntoURL** | Ontology understanding/reasoning/learning | Multi-dimensional | 2025 |
| **LLMs4OL** | Ontology learning challenge | 4 tasks | 2025 |

**Critical gap:** No benchmark for **claim-level KG construction** (extracting verified claims with provenance, not just entity-relation triples).
- **Source:** OntoEKG paper; Text2KGBench [A2/C5]

---

## 7. CLAIM-LEVEL KG CONSTRUCTION (Ainary-Relevant)

### 7.1 ClaimVer (EMNLP 2024 Findings)
- **Claim-Level Verification and Evidence Attribution via KGs**
- Highlights each claim → verifies against trusted KG → presents evidence → explains
- Distills proprietary model performance into small open-source models
- Most relevant existing work for Ainary's architecture
- **Source:** Dammu et al. 2024, EMNLP Findings [A1/C6]

### 7.2 Claim Extraction for Fact-Checking (2025)
- Systematic analysis of claim extraction methods
- Multi-query prompt pipeline for distilling extraction into compact models
- **Source:** arxiv 2502.04955 [A2/C5]

---

## 8. AINARY-SPECIFIC ANALYSIS

### 8.1 Current State of Ainary's KG
Ainary's Research Network processes claims from multiple sources about research topics. The KG construction pipeline needs:
1. Source ingestion → claim extraction (not entity-relation triples)
2. Claim verification + confidence scoring
3. Cross-source deduplication + contradiction detection
4. Graph assembly with provenance tracking

### 8.2 Key Gaps
| Gap | Description | Severity |
|-----|-------------|----------|
| **Claim-level KG (not triple-level)** | All existing systems extract (entity, relation, entity) triples. Ainary needs (claim, evidence, confidence, source) | HIGH |
| **Provenance-first construction** | Need to track which source said what, when, with what confidence | HIGH |
| **Cross-source consistency** | Integrating contradictory claims from different sources | HIGH |
| **Incremental/streaming construction** | Add new sources without rebuilding entire graph | MEDIUM |
| **Evaluation benchmark** | No benchmark for claim-level KG quality | MEDIUM |

### 8.3 Recommended Architecture

```
Document/Source → Chunking
    → LLM Claim Extraction (FActScore-style atomic decomposition)
    → Schema-Free Triple Extraction (EDC-style for entities)
    → Claim Verification Pipeline:
        - Self-consistency check (SelfCheckGPT-style)
        - Cross-source verification (contradiction detection — Topic 1)
        - KG alignment (ClaimVer-style)
    → Canonicalization:
        - Entity resolution (Topic 3: AnyMatch/SBERT)
        - Relation canonicalization (EDC-style)
        - Claim deduplication (Topic 4: NLI-based)
    → Confidence Scoring:
        - Admiralty rating from source
        - Verification confidence
        - Cross-source agreement
    → Graph Assembly:
        - Neo4j / graph DB
        - Community detection (GraphRAG-style)
        - Provenance edges to source documents
```

### 8.4 Key Recommendations
1. **Use EDC's Extract-Define-Canonicalize pattern** but extend to claims (not just triples)
2. **Adopt KGGEN's clustering** for entity/relation deduplication post-extraction
3. **Build on ClaimVer** for claim-level verification against the KG
4. **Skip schema design** — use AutoSchemaKG's dynamic schema induction (92% human alignment)
5. **Implement incremental construction** (ATOM/iText2KG pattern) for streaming sources
6. **Open-source models first** ($0.83 vs $6.03/M tokens) — Llama 3 or Qwen for extraction
7. **GraphRAG community summaries** for the query/synthesis layer on top

---

## 9. SOURCE REGISTRY

| # | Source | Type | Year | Admiralty | EIJA |
|---|--------|------|------|-----------|------|
| 1 | Bian et al. "LLM-empowered KG construction" survey (arxiv 2510.20345) | Survey | 2025 | A2 | I |
| 2 | EDC (Zhang & Soh, EMNLP 2024) | Method | 2024 | A1 | E |
| 3 | GraphRAG (Edge et al., Microsoft 2024) | Method | 2024 | A1 | E |
| 4 | AutoSchemaKG (Bai et al. 2025, HKUST) | Method | 2025 | A1 | J |
| 5 | KGGEN (Mo et al. 2025, NeurIPS) | Method | 2025 | A1 | E |
| 6 | OntoEKG (2026, arxiv 2602.01276) | Method | 2026 | A2 | J |
| 7 | REBEL (Cabot & Navigli, EMNLP 2021) | Model | 2021 | A1 | E |
| 8 | KG Construction survey (MDPI Applied Sciences 2025) | Survey | 2025 | A2 | I |
| 9 | KGs and LLMs reciprocal (MDPI 2025) | Survey | 2025 | A2 | I |
| 10 | ClaimVer (Dammu et al., EMNLP 2024 Findings) | Method | 2024 | A1 | E |
| 11 | Claim extraction fact-checking (arxiv 2502.04955) | Survey | 2025 | A2 | J |
| 12 | Text2KGBench (ISWC 2023) | Benchmark | 2023 | A1 | E |
| 13 | Ghanem et al. "Hallucination + Omission in KGC" (KGSWC 2024) | Evaluation | 2025 | A2 | J |
| 14 | GraphEval (Sansford/Amazon 2024) | Framework | 2024 | A2 | J |
| 15 | LLM for Semantic Communication KG (MDPI 2025) | Method | 2025 | B3 | J |
| 16 | Ontogenia (Lippolis et al. 2025) | Method | 2025 | A2 | J |
| 17 | CQbyCQ (Saeedizade & Blomqvist 2024) | Method | 2024 | A2 | E |
| 18 | NeOn-GPT (Fathallah et al. 2025) | Method | 2025 | B3 | J |
| 19 | AdaKGC (Ye et al. 2023) | Method | 2023 | A2 | E |
| 20 | Kommineni et al. 2024 (LLM→KG pipeline) | Method | 2024 | A2 | J |
| 21 | AutoRD rare disease KG (JMIR 2024) | Method | 2024 | A2 | J |
| 22 | Hybrid E2E KG construction (OpenReview 2025) | Method | 2025 | B3 | J |
| 23 | LangChain LLMGraphTransformer blog | Tool | 2024 | B3 | A |
| 24 | Neo4j LLM Graph Builder | Tool | 2024 | B3 | A |
| 25 | LightRAG / production KG systems (Branzan) | Blog | 2025 | B3 | I |
| 26 | Automated KGC + sentence complexity (arxiv 2509.17289) | Method | 2025 | B3 | J |
| 27 | OSKGC benchmark (Wang & Iwaihara 2025) | Benchmark | 2025 | B3 | J |
| 28 | OntoURL benchmark (Zhang et al. 2025) | Benchmark | 2025 | B3 | J |
| 29 | LLMs4OL challenge (Giglou et al. 2025) | Challenge | 2025 | A2 | J |
| 30 | IncRML incremental KG (Semantic Web Journal) | Method | 2024 | A2 | J |
| 31 | ATOM temporal KG (formerly iText2KG) | Tool | 2025 | B3 | J |
| 32 | Open vs proprietary LLM costs (whatllm.org) | Analysis | 2025 | B3 | A |
| 33 | Fine-tuning vs prompting for KGC (PMC 2025) | Evaluation | 2025 | A2 | J |

---

## 10. SATURATION LOG

| Source # | New insights? | Cumulative |
|----------|--------------|------------|
| 1-5 | YES — survey taxonomy, EDC framework, GraphRAG, AutoSchemaKG, KGGEN | 14 |
| 6-10 | YES — enterprise ontology, REBEL, claim verification, benchmarks | 21 |
| 11-15 | YES — claim extraction, hallucination in KGC, evaluation metrics | 25 |
| 16-20 | PARTIAL — ontology assistants, dynamic schema | 28 |
| 21-25 | PARTIAL — domain pipelines, production tools | 29 |
| 26-29 | MINIMAL — benchmarks, challenges | 30 |
| 30-33 | MINIMAL — incremental, cost analysis | 30 |
| **Saturation at source 29** | 3 consecutive with <2 new | — |

---

## 11. KEY QUANTITATIVE FINDINGS

| Finding | Metric | Source |
|---------|--------|--------|
| AutoSchemaKG alignment with human schemas | 92% (zero manual) | Bai et al. 2025 |
| OntoEKG best F1 (fuzzy match) | 0.724 (Data domain) | OntoEKG 2026 |
| EDC schemas supported | 200+ relation types (vs <10 prior) | Zhang & Soh 2024 |
| LightRAG token reduction vs GraphRAG | 10× fewer tokens | Branzan 2025 |
| LinkedIn GraphRAG ticket resolution | 40h → 15h (63% improvement) | Branzan 2025 |
| Open-source LLM cost vs proprietary | $0.83 vs $6.03/M tokens (7.3×) | whatllm.org |
| REBEL relation types | 200+ | Cabot & Navigli 2021 |

---

*Report generated: 2026-03-06 | Research Protocol: MECE + Hypothesis-first + Saturation-based stopping*
*Hypothesis tested: "Can LLMs replace traditional KG construction pipelines?" → PARTIALLY CONFIRMED (for extraction + schema induction, but fusion/validation still needs human oversight)*
*Next topic: 08 — Graph Visualization*

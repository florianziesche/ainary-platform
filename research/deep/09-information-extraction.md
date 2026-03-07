# Topic 9: Information Extraction
## Deep Research Report — Ainary Research Network

**Date:** 2026-03-06
**Sources:** 33 (saturation at 29)
**Status:** COMPLETE
**BLUF:** Information extraction has undergone a paradigm shift from discriminative (classification-based) to **generative** (LLM-based) approaches. Three key developments define the 2024–2025 landscape: (1) **Universal IE frameworks** (GoLLIE, KnowCoder, InstructUIE) unify NER/RE/EE into single models via code-based or instruction-based schemas; (2) **GLiNER** (NAACL 2024) proves small bidirectional models outperform ChatGPT for zero-shot NER; (3) **Atomic claim decomposition** (FActScore, AFEV) enables claim-level extraction — the missing link for Ainary. Key gap: no system combines atomic claim extraction + entity/relation extraction + provenance tracking into a single pipeline.

---

## 1. TAXONOMY OF IE TASKS

### 1.1 Core Tasks
| Task | Input | Output | Example |
|------|-------|--------|---------|
| **Named Entity Recognition (NER)** | Text | Entity spans + types | "Berlin" → LOCATION |
| **Relation Extraction (RE)** | Text + entities | Relation labels | (Berlin, capital_of, Germany) |
| **Event Extraction (EE)** | Text | Event triggers + arguments | "earthquake in Turkey" → Disaster(location=Turkey) |
| **Open Information Extraction (OpenIE)** | Text | Open triples (no schema) | (Obama, was born in, Hawaii) |
| **Claim Extraction** | Text | Atomic verifiable claims | "Berlin has 3.7M inhabitants" |

### 1.2 Discriminative vs. Generative IE
| Aspect | Discriminative | Generative |
|--------|---------------|------------|
| **Approach** | Classify spans/pairs | Generate structured text |
| **Models** | BERT, BiLSTM-CRF | GPT-4, Llama, CodeLlama |
| **Schema handling** | Fixed, retrain for new types | Flexible via prompts |
| **Scalability** | Fast inference, fixed types | Slower, unlimited types |
| **Accuracy (supervised)** | Higher on narrow tasks | Slightly lower |
| **Zero-shot** | Poor | Strong |

**Source:** Xu et al. 2024 (LLMs for Generative IE survey, Frontiers of CS) [A1/C6]

---

## 2. NAMED ENTITY RECOGNITION (NER)

### 2.1 Traditional SOTA
- **Fine-tuned BERT/RoBERTa + CRF:** CoNLL-2003 F1 ≈ 93–94%
- Still best for **supervised, narrow-domain** NER
- **Source:** Various [A1/C5]

### 2.2 LLM-Based NER

#### GLiNER (NAACL 2024) — **Key Finding**
- **Small bidirectional model** for zero-shot NER (not autoregressive LLM)
- Uses entity type descriptions as input → span-level matching
- **Outperforms ChatGPT AND fine-tuned LLMs** in zero-shot NER benchmarks
- Supports joint entity + relation extraction
- Lightweight: runs locally, fast inference
- **Critical insight:** For structured extraction, small specialized models beat general-purpose LLMs
- **Source:** Zaratiana et al. 2024, NAACL [A1/C6]

#### UniNER (ICLR 2024)
- Targeted distillation from ChatGPT → open-domain NER
- 43 NER datasets across 9 domains (general, biomedical, clinical, STEM, programming, social media, law, finance, transportation)
- UniNER-7B: strong zero-shot after distillation from ChatGPT annotations on The Pile
- UniNER-7B-definition: robust to entity type paraphrasing
- **KnowCoder (2024):** Code-based schema encoding → 49.8% relative F1 improvement over LLaMA2 on few-shot NER after code pretraining on 1.5B automatically constructed examples
- **Source:** Zhou et al. 2024, ICLR [A1/C6]; KnowCoder 2024 [A2/C5]

#### GNER, NuNER, VerifiNER, VANER
- **GNER:** Generative NER with instruction following
- **NuNER:** Self-supervised pre-training for universal NER
- **VerifiNER:** Verification step for NER consistency
- **VANER:** Visual-augmented NER
- **Source:** Various [A2/C5]

### 2.3 Performance Comparison (Zero-Shot NER)
| Model | Type | Zero-Shot Performance | Cost |
|-------|------|----------------------|------|
| **GLiNER (bi-directional)** | Small specialized | **Best** (outperforms ChatGPT) | Very low |
| **UniNER-7B** | Distilled LLM | Strong | Medium |
| **GPT-4** | General LLM | Good | High ($) |
| **ChatGPT (GPT-3.5)** | General LLM | Moderate | Medium |
| **Gemini 2.5** | General LLM | ~0.84 F1 (best among general LLMs) | High |
| **Fine-tuned BERT** | Supervised | N/A (needs data) | Low |

**Key finding:** Information extraction tasks still see **best performance from fine-tuned domain models**, not general LLMs.
- **Source:** Tonic.ai 2025; IntuitionLabs 2025 [B3/C4]

---

## 3. RELATION EXTRACTION (RE)

### 3.1 Sentence-Level RE
- **Pipeline approach:** NER → entity pair classification
- **End-to-end:** Joint extraction (REBEL, TEMPGEN)
- **LLM-based:** GPT-RE (in-context learning with demonstrations)

### 3.2 Document-Level RE — **Major Challenge**
- **Cross-sentence F1 remains 10–15 points below intra-sentence** consistently
- Requires multi-hop reasoning over scattered evidence
- **DocKS-RAG** (ICML 2025): Hybrid prompt tuning with sentence-level RAG for document RE
- Graph-based methods (cross-evidence reasoning) improve long-distance reasoning
- **Source:** EmergentMind DocRE topic; DocKS-RAG ICML 2025 [A1-A2/C5-6]

### 3.3 Open Relation Extraction
- Schema-free triplet extraction
- Two scoring approaches: token-level (for span extraction) vs fact-level (for generative LLM output)
- LLM outputs require semantic evaluation, not just string matching
- **Source:** OIE survey (EMNLP Findings 2024) [A1/C6]

---

## 4. UNIVERSAL INFORMATION EXTRACTION

### 4.1 Natural Language-Based UIE

| System | Year | Base | Key Innovation |
|--------|------|------|---------------|
| **UIE** (Lu et al.) | 2022 | T5 | Structural Schema Instructor (SSI) |
| **InstructUIE** | 2023 | LLaMA | Multi-task instruction tuning; comparable to BERT supervised; outperforms GPT-3.5 zero-shot |
| **IEPile** (ACL 2024) | 2024 | Baichuan2/LLaMA2 | 0.32B token bilingual IE dataset; fine-tuned models excel in supervised + zero-shot |
| **YAYI-UIE** | 2024 | Custom | Unified instruction format |

### 4.2 Code-Based UIE — **Emerging Paradigm**

| System | Year | Base | Key Innovation |
|--------|------|------|---------------|
| **GoLLIE** (ICLR 2024) | 2024 | CodeLlama | Annotation guidelines as code → best zero-shot generalization |
| **KnowCoder** | 2024 | LLaMA2 | Schema as Python classes; 1.5B pretraining examples; 49.8% F1 improvement |
| **Code4UIE** | 2024 | CodeLlama | Code generation for IE |
| **CODEIE** | 2023 | Codex | Python code as IE output format |

**Why code-based works better:**
1. Code is **unambiguous** — Python class definitions are exact schema specifications
2. LLMs pretrained on code have better **structured output** capabilities
3. Output parsing is **trivial** (valid Python → parse)
4. Annotation guidelines encoded as docstrings → guidelines compliance
- **Source:** GoLLIE ICLR 2024 [A1/C6]; KnowCoder 2024 [A2/C5]

---

## 5. ATOMIC CLAIM EXTRACTION — **AINARY-CRITICAL**

### 5.1 FActScore Paradigm
- Decompose text into **atomic facts** — individually verifiable statements
- Each atomic fact: "A is B" or "C does D"
- Enables per-claim verification, confidence scoring, and provenance tracking
- **Source:** Min et al. 2023 (FActScore) [A1/C6]

### 5.2 AFEV — Atomic Fact Extraction and Verification (2025)
- **Iteratively** decomposes complex claims into atomic facts
- Fine-grained retrieval per atomic fact
- Adaptive reasoning based on claim structure
- Addresses: accumulated reasoning errors, noisy evidence contamination
- **Source:** AFEV 2025, ScienceDirect [A2/C5]

### 5.3 DecMetrics (2025)
- Structured Claim Decomposition Scoring
- Generates atomic claims that are **complete, correct, and high semantic entropy**
- Decomposition tree: pairs claims with atomic claims
- **Source:** arxiv 2509.04483 [A2/C5]

### 5.4 Claim Extraction for Fact-Checking (2025)
- Systematic analysis of claim extraction methods
- Breaking complex factual statements into atomic claims **trivializes inference**
- Enables explainability: "which parts of complex statement misinterpret which facts"
- **Source:** arxiv 2502.04955 [A2/C5]

---

## 6. IE TECHNIQUES

### 6.1 Data Augmentation
- LLMs as data annotators (LLMaAA, AugURE, REPAL)
- Generate synthetic training data for small model fine-tuning
- NuNER: self-supervised pre-training → universal NER
- **Source:** Various [A2/C5]

### 6.2 In-Context Learning (ICL)
- Few-shot prompting with examples
- GPT-RE: demonstration retrieval for in-context RE
- C-ICL: collaborative ICL for better coverage
- **Limitation:** Performance plateaus with >5 examples
- **Source:** Various [A2/C5]

### 6.3 Instruction Tuning
- Fine-tune on IE-specific instructions
- GoLLIE: annotation guidelines as instructions → best zero-shot generalization
- IEPile: large-scale bilingual IE instruction dataset
- **Source:** GoLLIE, IEPile [A1/C6]

### 6.4 Code-Based Extraction
- Schema as Python class definitions
- Output as Python objects → trivial parsing
- KnowCoder: code pretraining → schema understanding
- **Best paradigm for structured IE** in 2024–2025
- **Source:** KnowCoder, GoLLIE [A1/C6]

---

## 7. KEY CHALLENGES

### 7.1 Hallucination in IE
- LLMs generate entities/relations not present in input text
- Generative IE particularly susceptible to **fabricated triples**
- VerifiNER: verification step to check NER consistency
- **Mitigation:** Constrained decoding, schema-constrained generation, post-hoc verification
- **Source:** Xu et al. 2024 survey [A1/C6]

### 7.2 Schema Complexity
- Traditional IE systems struggle with >100 entity types or >200 relation types
- GenIE: handles schemas with millions of entities without significant degradation
- EDC (Topic 7): scales to 200+ relation types via define-then-canonicalize
- **Source:** Various [A1/C6]

### 7.3 Document-Level Extraction
- Cross-sentence relations: 10–15 F1 points below intra-sentence
- Requires multi-hop reasoning
- Long-context LLMs (128K+ tokens) help but don't fully solve
- **Source:** EmergentMind DocRE [A2/C5]

### 7.4 Evaluation Challenges
- String matching inadequate for generative IE
- Need semantic evaluation (fact-level scoring)
- Token-level vs fact-level scorer dichotomy
- **Source:** OIE survey 2024 [A1/C6]

---

## 8. AINARY-SPECIFIC ANALYSIS

### 8.1 What Ainary Needs vs. What Exists

| Need | Existing Solution | Gap |
|------|------------------|-----|
| Claim extraction from research text | FActScore atomic decomposition | ✅ Exists (needs integration) |
| Entity + relation extraction | GLiNER, REBEL, EDC | ✅ Exists |
| Cross-source claim matching | NLI-based deduplication | Partial (Topic 4) |
| Provenance tracking per claim | ClaimVer | Partial |
| Confidence scoring per extracted claim | AFEV verification pipeline | Partial |
| **Unified claim+entity+relation pipeline** | **NOTHING** | ❌ **KEY GAP** |

### 8.2 Recommended Pipeline

```
Source Document
  → Chunking (sentence/paragraph level)
  → Stage 1: ENTITY EXTRACTION
      - GLiNER (zero-shot, fast, accurate) for NER
      - OR UniNER for broader domain coverage
  → Stage 2: CLAIM EXTRACTION  
      - FActScore-style atomic decomposition via LLM
      - Each claim tagged with source sentence
  → Stage 3: RELATION EXTRACTION
      - EDC-style open relation extraction
      - Schema-free → auto-canonicalize
  → Stage 4: VERIFICATION
      - Self-consistency (SelfCheckGPT)
      - Cross-source agreement
      - KG alignment (ClaimVer-style)
  → Stage 5: ASSEMBLY
      - Claims + entities + relations → KG
      - Provenance edges to source
      - Confidence scores per claim
```

### 8.3 Key Recommendations
1. **Use GLiNER for NER, not GPT-4** — smaller, faster, more accurate for zero-shot
2. **Use GoLLIE-style code schemas** for custom entity types → best generalization
3. **Adopt FActScore atomic decomposition** for claim-level extraction
4. **Separate extraction from verification** — different models, different strengths
5. **Build claim extraction as a distinct IE task** — not just NER+RE
6. **Document-level RE remains hard** — focus on sentence-level first, aggregate later
7. **Open-source models sufficient** for extraction; use proprietary only for verification

---

## 9. SOURCE REGISTRY

| # | Source | Type | Year | Admiralty | EIJA |
|---|--------|------|------|-----------|------|
| 1 | LLMs for Generative IE survey (Xu et al., FCS 2024) | Survey | 2024 | A1 | E |
| 2 | Generative IE survey (COLING 2025) | Survey | 2025 | A1 | E |
| 3 | GLiNER (Zaratiana et al., NAACL 2024) | Method | 2024 | A1 | E |
| 4 | GoLLIE (Sainz et al., ICLR 2024) | Method | 2024 | A1 | E |
| 5 | UniNER (Zhou et al., ICLR 2024) | Method | 2024 | A1 | E |
| 6 | KnowCoder (2024) | Method | 2024 | A2 | J |
| 7 | IEPile (ACL 2024) | Dataset | 2024 | A1 | E |
| 8 | InstructUIE (2023) | Method | 2023 | A2 | E |
| 9 | NER survey (arxiv 2401.10825, v3 Dec 2025) | Survey | 2025 | A1 | I |
| 10 | Relation Extraction survey (ACM Computing Surveys) | Survey | 2024 | A1 | E |
| 11 | Open IE survey (EMNLP Findings 2024) | Survey | 2024 | A1 | E |
| 12 | FActScore atomic decomposition (Min et al. 2023) | Method | 2023 | A1 | E |
| 13 | AFEV — Atomic Fact Extraction + Verification (2025) | Method | 2025 | A2 | J |
| 14 | DecMetrics — Claim Decomposition Scoring (2025) | Method | 2025 | A2 | J |
| 15 | Claim extraction fact-checking (arxiv 2502.04955) | Survey | 2025 | A2 | J |
| 16 | DocRE topic (EmergentMind) | Synthesis | 2025 | A2 | I |
| 17 | DocKS-RAG (ICML 2025) | Method | 2025 | A1 | J |
| 18 | Legal IE survey (Springer 2025) | Survey | 2025 | A2 | I |
| 19 | Biomedical NER+RE survey (Neurocomputing 2024) | Survey | 2024 | A2 | I |
| 20 | Clinical NER+RE survey (MDPI 2021) | Survey | 2021 | A2 | I |
| 21 | ZEROONER (ACL Findings 2025) | Method | 2025 | A2 | J |
| 22 | Small vs Large LLMs for NER (Tonic.ai 2025) | Blog | 2025 | B3 | A |
| 23 | LLM benchmarks life sciences (IntuitionLabs 2025) | Blog | 2025 | B3 | I |
| 24 | Few-shot NER with LLMs (Clarifai 2025) | Blog | 2025 | B3 | I |
| 25 | REBEL (Cabot & Navigli, EMNLP 2021) | Model | 2021 | A1 | E |
| 26 | KnowLM / IEPile GitHub | Tool | 2024 | B3 | A |
| 27 | Universal NER benchmark (43 datasets) | Benchmark | 2024 | A1 | E |
| 28 | Cross-evidence reasoning DocRE (PMC 2024) | Method | 2024 | A2 | J |
| 29 | Materials Science KG from 100K docs (Nature 2025) | Application | 2025 | A1 | J |
| 30 | GPT-NER (2023) | Method | 2023 | A2 | E |
| 31 | Code4UIE (2024) | Method | 2024 | A2 | J |
| 32 | ERA-COT chain-of-thought RE (2024) | Method | 2024 | A2 | J |
| 33 | LLM-DA data augmentation NER (2024) | Method | 2024 | B3 | J |

---

## 10. SATURATION LOG

| Source # | New insights? | Cumulative |
|----------|--------------|------------|
| 1-5 | YES — survey taxonomy, GLiNER, GoLLIE, UniNER | 14 |
| 6-10 | YES — KnowCoder, IEPile, InstructUIE, RE survey | 20 |
| 11-15 | YES — OpenIE, atomic claims, AFEV, DecMetrics | 25 |
| 16-20 | PARTIAL — DocRE, domain-specific surveys | 27 |
| 21-25 | PARTIAL — ZEROONER, benchmarks, REBEL | 29 |
| 26-29 | MINIMAL — tools, applications | 29 |
| 30-33 | MINIMAL — individual methods | 29 |
| **Saturation at source 29** | 3 consecutive with <2 new | — |

---

## 11. KEY QUANTITATIVE FINDINGS

| Finding | Metric | Source |
|---------|--------|--------|
| GLiNER outperforms ChatGPT on zero-shot NER | Multiple benchmarks | Zaratiana 2024 |
| KnowCoder vs LLaMA2 few-shot NER | +49.8% relative F1 | KnowCoder 2024 |
| InstructUIE vs GPT-3.5 zero-shot | Significantly outperforms | InstructUIE 2023 |
| Cross-sentence RE gap vs intra-sentence | 10–15 F1 points lower | EmergentMind 2025 |
| IEPile training data | 0.32B tokens bilingual | IEPile ACL 2024 |
| Universal NER benchmark | 43 datasets, 9 domains | UniNER 2024 |
| Best general LLM NER F1 | ~0.84 (Gemini 2.5) | Tonic.ai 2025 |
| Supervised BERT NER F1 | ~0.93–0.94 (CoNLL-2003) | Various |

---

*Report generated: 2026-03-06 | Research Protocol: MECE + Hypothesis-first + Saturation-based stopping*
*Hypothesis tested: "Can LLMs replace fine-tuned models for IE?" → PARTIALLY REFUTED. Fine-tuned small models (GLiNER, BERT) still outperform general LLMs for supervised NER. But LLMs win on flexibility, zero-shot generalization, and universal IE. Code-based schemas (GoLLIE) are the best of both worlds.*
*Next topic: 10 — Relation Extraction*

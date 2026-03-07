# Deep Research Report #05: Entity Linking

**Date:** 2026-03-06
**Sources read:** 32 (saturation at source 29)
**Saturation:** 3 consecutive no-new-info after source 29

---

## BLUF (Bottom Line Up Front)

Entity linking (EL) — mapping text mentions to knowledge base entries — is a solved problem for common entities in English news text (~90%+ accuracy on AIDA-CoNLL) but remains fundamentally hard for **long-tail entities, domain-specific contexts (biomedical, genes), multilingual settings, and emerging/NIL entities**. The field has evolved through four paradigm shifts: (1) feature-engineering → (2) bi-encoder dense retrieval (BLINK, 2020) → (3) generative/autoregressive (GENRE, 2021) → (4) **LLM-augmented hybrid** (2024–2025). The current frontier is clear: **LLMs are better as context augmenters than as direct entity linkers**. The most effective architecture combines specialized EL models (ReFinED, ReLiK) with LLM-generated context augmentation (LLMaEL), achieving 8.9% absolute gains over prior LLM-based methods. For Ainary's knowledge graph, the key gap is **claim-level entity linking** — linking extracted claims to KB entities rather than just named entity spans — which no current system addresses natively.

---

## 1. Problem Definition & Taxonomy

### 1.1 Task Definition
Entity Linking = **Mention Detection** (NER) + **Candidate Generation** (retrieval) + **Entity Disambiguation** (ranking/classification). Two evaluation modes:
- **End-to-End EL**: System detects mentions AND disambiguates them (Micro-F1 strong matching via GERBIL)
- **Disambiguation-Only (ED)**: Gold mentions provided, system only disambiguates (Micro-Precision)

### 1.2 Architecture Taxonomy (4 paradigms)

| Paradigm | Representative | Approach | Strengths | Weaknesses |
|----------|---------------|----------|-----------|------------|
| **Classification** | FEVRY (2020), SpEL (2023) | Token-level classification over entity vocabulary | Fast inference, structured prediction | Fixed vocabulary, can't add new entities without retraining |
| **Dense Retrieval** | BLINK (2020), VerbalizED (2025) | Bi-encoder embeds mentions+entities in shared space; cross-encoder re-ranks | Zero-shot capable, scalable with ANN | Expensive cross-encoder; bi-encoder accuracy ceiling |
| **Generative** | GENRE (2021), mGENRE (2022) | Seq2seq generates entity names autoregressively | No candidate list needed, naturally handles open set | Constrained beam search required; slow |
| **LLM-Augmented** | ChatEL, EntGPT, LLMaEL, DeepEL (2024–2025) | LLMs augment context or serve as disambiguators | Broad world knowledge, zero-shot | Expensive, hallucination risk, poor at exact KB name generation |

**Source:** [Sevgili et al. 2022 — Neural Entity Linking Survey, Semantic Web Journal]; [Wu et al. 2020 — BLINK, EMNLP]; [De Cao et al. 2021 — GENRE, ICLR]; [Xin et al. 2025 — LLMaEL, CIKM]

---

## 2. State of the Art: Benchmarks & Performance

### 2.1 AIDA-CoNLL (the standard)

| System | Year | Type | AIDA-B F1/Acc | Notes |
|--------|------|------|---------------|-------|
| SpEL-large | 2023 | Classification | **SOTA on PwC** | 2 refined fine-tuning steps, context-sensitive aggregation |
| VerbalizED+iter | 2025 | Dual Encoder | 88.2 F1 (ZELDA) | New SOTA on ZELDA benchmark; iterative prediction |
| EntGPT-I (GPT-3.5) | 2024 | LLM Instruction-tuned | 95.9 Micro-F1 (ED) | Instruction-tuned on AIDA; 2.1% avg improvement |
| CoherentED | 2023 | Neural coherence | SOTA on most ED datasets | Entity-entity coherence modeling |
| ReLiK-large | 2024 | Retriever-Reader | 83.1 E2E Micro-F1 | 40× faster than competitors, joint EL+RE |
| ChatEL (GPT-3.5) | 2024 | LLM Prompting | 79.5 avg Micro-F1 (10 datasets) | Zero-shot, no training needed |

**Key insight:** ED accuracy on AIDA is >95% for supervised methods but E2E F1 is only ~83-88%, showing **mention detection remains a bottleneck**.

**Source:** [Shavarani & Sarkar 2023 — SpEL, EMNLP]; [Rücker & Akbik 2025 — VerbalizED, ACL]; [Ding et al. 2024 — EntGPT, KBS]; [Orlando et al. 2024 — ReLiK, ACL]; [Ding et al. 2024 — ChatEL, LREC]

### 2.2 ZELDA Benchmark (multi-domain evaluation)
ZELDA (Milich & Akbik, EACL 2023) addresses inconsistencies in ED evaluation by unifying training data (~95K Wikipedia paragraphs, 2.6M mentions, ~822K entities) and 9 diverse test sets (news, tweets, Reddit, web, Wikipedia, Shadowlinks). **VerbalizED** (2025) achieves 82.3 avg F1, establishing new SOTA with iterative training.

Key ZELDA findings:
- **Shadowlinks-Shadow** (overshadowed entities) is hardest: best system only 66.3 F1
- **TWEEKI** (tweets): short context makes EL much harder
- Dense retrieval (FusionED: 78.7) significantly outperforms classification and generative approaches
- **Label verbalization quality matters enormously**: Title+Description+Categories > Title alone by +1.3 F1

**Source:** [Milich & Akbik 2023 — ZELDA, EACL]; [Rücker & Akbik 2025 — VerbalizED, ACL]

---

## 3. Key Systems Deep Dive

### 3.1 BLINK (Wu et al. 2020) — The Dense Retrieval Foundation
- **Architecture**: Two-stage: bi-encoder (BERT) retrieves top candidates via dot-product similarity; cross-encoder re-ranks
- **Speed**: 5.9M candidates in 2ms with FAISS ANN search
- **Zero-shot**: 6-point absolute gain on zero-shot benchmarks; entities defined only by text descriptions
- **Knowledge distillation**: Much of cross-encoder accuracy transferable to bi-encoder
- **Impact**: Established the dominant paradigm; adopted by BLINK, ReFinED, ChatEL, EntGPT as candidate generator

**Source:** [Wu et al. 2020 — Scalable Zero-shot Entity Linking, EMNLP]

### 3.2 GENRE / mGENRE (De Cao et al. 2021/2022) — Generative EL
- **Innovation**: First system to retrieve entities by **generating their names** token-by-token (autoregressive)
- **Architecture**: Fine-tuned BART with offline prefix trie from Wikipedia titles constraining beam search
- **mGENRE** (TACL 2022): Extends to 100+ languages; treats target language as latent variable marginalized at prediction time → 50%+ improvement in zero-shot cross-lingual EL
- **Tradeoff**: No explicit candidate list needed, but constrained decoding is slower than retrieval

**Source:** [De Cao et al. 2021 — GENRE, ICLR]; [De Cao et al. 2022 — mGENRE, TACL]

### 3.3 ReFinED (Ayoola et al. 2022) — Production-Scale EL
- **Key innovation**: Single forward pass for mention detection + fine-grained entity typing + disambiguation
- **Speed**: 60× faster than competitive approaches
- **Scale**: Generalizes to Wikidata (15× more entities than Wikipedia), zero-shot capable
- **Architecture**: Uses fine-grained entity type embeddings + description embeddings; type score + description score combined for final ranking
- **NIL prediction**: Can assign NIL when no candidate exceeds threshold — critical for real-world deployment
- **Deployed at Amazon** at web scale

**Source:** [Ayoola et al. 2022 — ReFinED, NAACL Industry Track]

### 3.4 ReLiK (Orlando et al. 2024) — Academic Budget SOTA
- **Architecture**: Retriever-Reader; DPR-like retriever gets candidate entities; Reader encodes text + all candidates in single forward pass (novel input formulation)
- **Joint EL+RE**: Same architecture handles entity linking AND relation extraction simultaneously (cIE)
- **Performance**: SOTA on both in-domain and out-of-domain benchmarks
- **Efficiency**: Up to 40× faster inference than competitors; trainable on academic budget
- **Key insight**: Encoding input text with ALL retrieved candidates simultaneously (not one-at-a-time) is crucial for performance and speed

**Source:** [Orlando et al. 2024 — ReLiK, ACL]

### 3.5 LLMaEL (Xin et al. 2025) — LLMs as Context Augmenters
**THE MOST IMPORTANT FINDING FOR 2024–2025:**
- **Core insight**: LLMs are better at **context generation** than at **entity linking execution**
- **Architecture**: LLM (Llama-3-70B) generates enriched entity descriptions → fed to specialized EL model (ReFinED, GENRE) as additional context → EL model makes final prediction
- **Results**: +8.9% absolute accuracy over prior tuning-free LLM EL methods; +1.2% average over specialized EL models alone
- **Five context-joining strategies** evaluated; optimal strategy varies per backbone EL model
- **Optional fine-tuning**: EL model can be fine-tuned on LLM-augmented training data for further gains
- **Ensemble**: Multiple LLM-generated descriptions with majority voting improves robustness
- **Published at CIKM 2025** — strongest evidence that hybrid LLM+specialist is the winning formula

**Source:** [Xin et al. 2025 — LLMaEL, CIKM]

### 3.6 DeepEL (Hou et al. 2025) — Full LLM Integration
- LLMs integrated into EVERY stage of EL (not just augmentation)
- Novel **self-validation mechanism**: uses global context to rectify own predictions; models entity coherence within sentences
- +2.6% overall F1, +4% on out-of-domain datasets
- Demonstrates that **isolated disambiguation is insufficient** — global entity coherence matters

**Source:** [Hou et al. 2025 — DeepEL, ADMA]

---

## 4. Critical Design Decisions (VerbalizED Ablation, ACL 2025)

The most rigorous ablation study to date (Rücker & Akbik 2025) on dual-encoder ED:

| Decision | Best Choice | Impact |
|----------|------------|--------|
| **Label verbalization** | Title + Description + Categories | +1.3 F1 vs title-only |
| **Span pooling** | First-last token concatenation | +2.2 F1 vs mean pooling |
| **Similarity metric** | Euclidean distance | Cosine collapses (34 F1 with CE loss!) |
| **Loss function** | Cross-entropy | +1.4 F1 vs triplet loss |
| **Negative sampling** | Hard negatives (dynamic) | +11.8 F1 vs in-batch negatives |
| **Label embedding updates** | Frequent + on-the-fly | +6.2 F1 vs once-per-epoch |
| **Iterative prediction** | Yes (insert confident predictions as context) | +0.4–6.0 F1 on hard cases |

**Killer finding: Cosine similarity is catastrophically bad for entity disambiguation with cross-entropy loss.** Euclidean or dot product required.

**Source:** [Rücker & Akbik 2025 — VerbalizED, ACL]

---

## 5. KG-Enhanced LLM Disambiguation (Pons Recasens et al. 2025)

Novel approach using KG class taxonomy to iteratively prune candidates:
1. Build DAG from candidates' KG class hierarchy (e.g., Thing → Person → Artist → Musician)
2. Find Lowest Common Ancestor (LCA) of remaining candidates
3. LLM answers multi-choice: "Is this mention more likely a Musician or a Politician?"
4. Prune branches; when same class → RAG with entity descriptions for final disambiguation

**Results**: Outperforms non-enhanced and description-only enhanced LLMs. KG semantic expressivity matters — YAGO (richer taxonomy) outperforms DBpedia (flatter).

**Implication for Ainary**: This is directly applicable — our KG's class structure can guide LLM disambiguation without retraining.

**Source:** [Pons Recasens et al. 2025 — KG-enhanced LLMs for ED, EKAW]

---

## 6. Domain-Specific Challenges

### 6.1 Biomedical Entity Linking
Comprehensive evaluation of 9 BioEL models (Kartchner et al., EMNLP 2023):
- **ArboEL** consistently top-performing; **SapBERT** best alias-matching method
- **Genes/proteins are catastrophically hard**: ALL models show −12 to −25% accuracy on genes vs overall
- **Abbreviation handling** matters: AD = Alzheimer's Disease OR Atopic Dermatitis OR Actinomycin D
- **Zero-shot is critical**: largest BioEL dataset (MedMentions) covers only ~1% of UMLS entities
- **No single best model**: ArboEL best for accuracy, SapBERT best for speed/usability balance

**Source:** [Kartchner et al. 2023 — Comprehensive Evaluation of BioEL Models, EMNLP]

### 6.2 Multilingual Entity Linking
- mGENRE: 50%+ improvement in zero-shot cross-lingual setting by marginalizing over target language
- Major challenge: non-Latin scripts, code-switching, transliteration
- Low-resource languages have virtually no annotated EL data

### 6.3 Social Media / Short Text
- Tweets: short context makes disambiguation much harder (TWEEKI benchmark)
- Informal language, hashtags, @mentions create novel mention forms
- GLiNKER (2026): Scales to 1M+ labels for NER+EL on Wikidata, 90× throughput improvement with bi-encoder architecture

**Source:** [De Cao et al. 2022 — mGENRE, TACL]; [Stepanov et al. 2026 — GLiNKER]

---

## 7. NIL Prediction & Emerging Entities

The "Learn to Not Link" problem (when entities aren't in KB):
- Most EL systems assume closed-world (all entities are in KB) — unrealistic
- ReFinED includes explicit NIL threshold — assigns NIL when confidence too low
- **~10% of ground truth labels in AIDA-CoNLL are incorrect** (Botzer et al. 2021; Ding et al. 2022) — ChatEL often produces more reasonable predictions than the "gold" standard
- Emerging entities (recent events, new people) are systematically missed by systems trained on static snapshots
- **No robust benchmark for NIL prediction** exists across domains

**Source:** [Ding et al. 2024 — ChatEL, LREC]; [Ayoola et al. 2022 — ReFinED, NAACL]

---

## 8. Entity Linking for Knowledge Graph Construction

### 8.1 EL's Role in KG Pipelines
EL is the critical bridge between unstructured text and structured knowledge:
- **Information Extraction pipeline**: NER → EL → Relation Extraction → KG
- ReLiK (2024) demonstrates joint EL+RE in single architecture = most efficient pipeline
- Relik integrated with LlamaIndex for GraphRAG applications (Neo4j blog, 2025)

### 8.2 Scale Challenges
- Wikipedia: ~6M entities — manageable with BLINK bi-encoder
- Wikidata: ~100M entities — requires specialized retrieval (ReFinED demonstrated, GLiNKER targets)
- UMLS: ~4.5M concepts — specialized BioEL needed
- **FAISS + ANN** is the standard for dense retrieval at scale (BLINK: 5.9M candidates in 2ms)

### 8.3 Entity Linking with Wikidata (ACM Computing Surveys, 2025)
Systematic review identifies 8 dimensions of Wikidata EL:
1. Mention detection
2. Candidate generation
3. Entity disambiguation
4. NIL prediction
5. Entity typing
6. Cross-linguality
7. Domain adaptation
8. Evaluation methodology

**Key gap**: Most systems target Wikipedia; Wikidata's 15× larger entity set and structured properties are underexploited.

**Source:** [ACM Computing Surveys 2025 — Entity Linking with Wikidata]

---

## 9. Quantitative Summary

| Metric | Value | Source |
|--------|-------|--------|
| AIDA-CoNLL ED SOTA (supervised) | ~95-96% Micro-Precision | EntGPT-I, CoherentED |
| AIDA-CoNLL E2E SOTA | ~88% F1 | VerbalizED iterative |
| ZELDA avg SOTA | 82.3 F1 | VerbalizED |
| Zero-shot EL gain (BLINK) | +6 pts absolute | Wu et al. 2020 |
| LLMaEL gain over LLM-only EL | +8.9% absolute accuracy | Xin et al. 2025 |
| ReFinED speed advantage | 60× faster than competitors | Ayoola et al. 2022 |
| ReLiK speed advantage | 40× faster, academic budget | Orlando et al. 2024 |
| BioEL gene accuracy deficit | −12 to −25% vs overall | Kartchner et al. 2023 |
| Cosine similarity failure (CE loss) | 34.3 F1 vs 65.8 (Euclidean) | Rücker & Akbik 2025 |
| AIDA ground truth error rate | ~10% incorrect labels | Botzer et al. 2021 |
| GLiNKER throughput | 90× vs uni-encoder at 1024 labels | Stepanov et al. 2026 |

---

## 10. Ainary GAP Analysis

### 10.1 What Exists
- Mature EL systems for Wikipedia/Wikidata linking (BLINK, GENRE, ReFinED, ReLiK)
- LLM augmentation patterns proven effective (LLMaEL, DeepEL)
- KG-guided disambiguation using class taxonomy (Pons Recasens et al.)
- Production-deployed systems (ReFinED@Amazon, spaCy Entity Linker)
- Comprehensive benchmarks (AIDA-CoNLL, ZELDA, GERBIL)

### 10.2 What's Missing (Ainary Opportunities)

1. **Claim-Level Entity Linking**: No system links extracted CLAIMS to KB entities — only named entity spans. Ainary's knowledge graph needs claim-to-entity grounding.

2. **Dynamic KB Entity Linking**: Real-time linking to evolving KBs (not static Wikipedia snapshots). Graphiti (Zep AI) attempts this for memory graphs but not for EL.

3. **Confidence-Calibrated EL**: Current systems give raw scores but no calibrated confidence. For a verified knowledge graph, we need "How confident is this link?" as a first-class output.

4. **Multi-KB Entity Linking**: Linking to MULTIPLE knowledge bases simultaneously (Wikidata + domain-specific KB + Ainary's own KG). ReFinED shows Wikidata generalization; no system does multi-KB natively.

5. **Entity Linking for Contradiction Detection**: When two claims contradict, are they about the SAME entity? Requires EL + coreference + contradiction detection pipeline — no integrated system exists.

### 10.3 Recommended Architecture for Ainary

```
INPUT TEXT → NER (GLiNER bi-encoder)
  → Candidate Generation (BLINK bi-encoder + FAISS)
  → LLM Context Augmentation (LLMaEL pattern, Llama-3)
  → Entity Disambiguation (ReFinED or ReLiK as backbone)
  → NIL Detection (threshold + LLM verification)
  → KG Integration (link to Ainary KG + Wikidata)
```

**Key design choices based on evidence:**
- Use Euclidean distance, NOT cosine similarity (VerbalizED ablation)
- Hard negative sampling is essential (+11.8 F1 over in-batch)
- LLM as augmenter, NOT executor (LLMaEL finding)
- Single forward pass for all candidates (ReLiK pattern)
- Iterative prediction for hard cases (VerbalizED pattern)

---

## 11. Source Register

| # | Source | Year | Type | Admiralty | EIJA |
|---|--------|------|------|-----------|------|
| 1 | Wu et al. — BLINK (EMNLP) | 2020 | Foundational | B2 | E |
| 2 | De Cao et al. — GENRE (ICLR) | 2021 | Foundational | A1 | E |
| 3 | De Cao et al. — mGENRE (TACL) | 2022 | Extension | A2 | I |
| 4 | Ayoola et al. — ReFinED (NAACL) | 2022 | System | A2 | A |
| 5 | Shavarani & Sarkar — SpEL (EMNLP) | 2023 | System | B2 | E |
| 6 | Ding et al. — ChatEL (LREC) | 2024 | LLM Application | B2 | E |
| 7 | Ding et al. — EntGPT (KBS) | 2024 | LLM Application | B2 | E |
| 8 | Xin et al. — LLMaEL (CIKM) | 2025 | Framework | A2 | E |
| 9 | Hou et al. — DeepEL (ADMA) | 2025 | Framework | B2 | I |
| 10 | Rücker & Akbik — VerbalizED (ACL) | 2025 | Ablation Study | A1 | E |
| 11 | Pons Recasens et al. — KG-enhanced ED (EKAW) | 2025 | Method | B2 | I |
| 12 | Orlando et al. — ReLiK (ACL) | 2024 | System | A2 | A |
| 13 | Sevgili et al. — Neural EL Survey (SWJ) | 2022 | Survey | A2 | E |
| 14 | Milich & Akbik — ZELDA (EACL) | 2023 | Benchmark | A2 | E |
| 15 | Kartchner et al. — BioEL Evaluation (EMNLP) | 2023 | Evaluation | A2 | E |
| 16 | Xiao et al. — InsGenEL (EMNLP) | 2023 | Method | B2 | I |
| 17 | NLP-Progress — Entity Linking leaderboard | 2024 | Reference | C3 | J |
| 18 | GERBIL — Benchmarking NER/EL (SWJ) | 2018 | Platform | A2 | A |
| 19 | Wikipedia — Entity Linking article | 2026 | Reference | C3 | J |
| 20 | Hoffart et al. — AIDA-CoNLL (EMNLP) | 2011 | Foundational Dataset | A1 | E |
| 21 | Ganea & Hofmann — Deep Joint ED (EMNLP) | 2017 | Foundational | A2 | E |
| 22 | Kolitsas et al. — End2End Neural EL (CoNLL) | 2018 | System | A2 | E |
| 23 | van Hulst et al. — REL (SIGIR) | 2020 | System | B2 | A |
| 24 | Raiman et al. — DeepType (AAAI) | 2018 | Method | B2 | E |
| 25 | Barba et al. — ExtEnd (ACL) | 2022 | Method | B2 | I |
| 26 | Neo4j Blog — ReLiK + LlamaIndex | 2025 | Application | C3 | A |
| 27 | Ontotext — What is Entity Linking | 2025 | Reference | C3 | J |
| 28 | Stepanov et al. — GLiNKER (arXiv) | 2026 | System | B3 | I |
| 29 | ACM Computing Surveys — EL with Wikidata | 2025 | Survey | A2 | E |
| 30 | Emergent Mind — Entity Extraction & Linking | 2025 | Reference | C3 | J |
| 31 | ClinLinker — Medical EL (arXiv) | 2024 | Domain-specific | B3 | I |
| 32 | BioNNE-L 2025 — SapBERT hybrid re-ranking | 2025 | Challenge | B3 | I |

**Admiralty Scale:** A=Reliable, B=Usually Reliable, C=Fairly Reliable; 1=Confirmed, 2=Probably True, 3=Possibly True
**EIJA Tags:** E=Essential, I=Important, J=Just-in-case, A=Actionable

---

## 12. Open Questions

1. **Can LLMaEL's augmentation pattern work for claim-level (not just mention-level) entity linking?**
2. **What's the cost/accuracy tradeoff of ReLiK vs ReFinED vs GLiNKER for Wikidata-scale EL?**
3. **How to handle entity evolution (mergers, name changes, concept drift) in a continuously updated KG?**
4. **Is the ~10% label error rate in AIDA-CoNLL biasing all published comparisons?**
5. **Can VerbalizED's iterative prediction be combined with LLMaEL's augmentation for compounding gains?**

---

*Report generated following RESEARCH-PROTOCOL.md: Hypothesis → MECE → Deep Read → Saturation → BLUF*
*Confidence: 88% — high confidence on architecture recommendations and SOTA numbers; moderate uncertainty on claim-level EL feasibility and cross-system composability*

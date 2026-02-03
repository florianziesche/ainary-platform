# Substack Article #3 — Outline

**Title:** "Building AI Systems That Actually Work: What I Learned From 1000 Hours of Edge Cases"

**Publish Date:** February 17, 2026 (tentative)

**Goal:** Establish authority on production AI, attract consulting leads

---

## Hook

The dirty secret of AI: Most implementations fail.

Not because the technology doesn't work. Because people build demos, not systems.

After 5 years building AI products and recently architecting a system with <0.2% hallucination rate, here's what I've learned about the difference.

---

## Section 1: Demo vs System (The Real Gap)

**Key points:**
- Demo = Works on 10 examples
- System = Works on 10,000 edge cases
- The gap is 90% of the work

**Example:**
- Legal AI demo: "Look, it answers questions!"
- Legal AI system: "It handles ambiguous questions, conflicting documents, missing information, and tells users when it's uncertain"

**Takeaway:** The demo gets you the meeting. The system keeps you the customer.

---

## Section 2: The Architecture That Actually Works

**Multi-agent verification:**
1. Questioner — Understands what user really wants
2. Researcher — Finds relevant information
3. Validator — Checks every claim against source
4. Reporter — Formats response with citations

**Why this works:**
- Each agent specialized (better than one generalist)
- Errors caught at multiple stages
- Audit trail built-in

**Diagram:** [Create visual of agent flow]

---

## Section 3: Retrieval > Generation (The 80/20)

**Key insight:** 80% of accuracy gains come from better retrieval, not better prompts.

**The stack:**
- BM25 for exact matching (legal terms, product names)
- Dense vectors for semantic similarity
- Cross-encoder re-ranking for precision
- Confidence scoring for uncertainty

**Common mistake:** Focusing on prompt engineering while retrieval is broken.

**Analogy:** It's like optimizing a chef's recipe when the ingredients are rotten.

---

## Section 4: Confidence Scores Change Everything

**Problem:** AI says everything with the same confidence.
**Solution:** Explicit uncertainty indicators.

**Categories:**
- High (>90%): Direct quote from source
- Medium (70-90%): Paraphrase with citation
- Low (<70%): Inference flagged for review

**Result:** User trust increased dramatically when they could see confidence levels.

**Quote:** "I'd rather know the AI is unsure than be confidently wrong."

---

## Section 5: The Audit Trail Is Non-Negotiable

**For enterprise:**
- Every answer must be traceable
- Every decision must be logged
- Every source must be verifiable

**What to log:**
- Input query
- Retrieved chunks
- Agent decisions
- Output + citations
- Confidence scores
- User feedback

**Why:** Compliance, debugging, improvement, trust.

---

## Section 6: Edge Cases Are The Job

**List of edge cases that broke our system:**
1. Documents with same title, different content
2. Contradictory information in same corpus
3. Questions that span multiple documents
4. "I don't know" is a valid answer
5. User asks about things not in corpus

**Time spent:**
- 20% on happy path
- 80% on edge cases

**Quote:** "Building AI is 20% AI, 80% engineering."

---

## Section 7: Domain Expertise Required

**Generic RAG templates don't work for:**
- Legal (precise terminology matters)
- Medical (safety critical)
- Financial (regulatory requirements)
- Technical (specificity matters)

**What you need:**
- Someone who understands the domain
- Access to real users during development
- Iteration based on actual failures

---

## Conclusion: The Checklist

**Before you ship:**
- [ ] Multi-agent or single agent? (Multi better for accuracy)
- [ ] Retrieval tested independently?
- [ ] Confidence scores shown to users?
- [ ] Audit trail implemented?
- [ ] Edge cases documented and handled?
- [ ] Domain expert reviewed?
- [ ] Real users tested (not just you)?

---

## CTA

If you're building AI systems and want them to actually work:

1. Subscribe for more technical deep-dives
2. Check out my consulting services (link)
3. Reply with your biggest AI implementation challenge

---

## Notes for Writing

- **Tone:** Technical but accessible
- **Length:** 2,500-3,500 words
- **Visuals:** 2-3 diagrams (architecture, retrieval stack, confidence scoring)
- **Social proof:** Reference the 0.18% hallucination rate case study

---

*Draft status: Outline complete. Ready to write.*

---
version: 1.0.1
status: current
review_date: 2026-03-19
owner: florian
type: claims-ledger
created: 2026-02-19
last_updated: 2026-02-19
total_claims: 15
tier: OPERATIONAL
expires: 2026-08-20
---

# Claims Ledger

**Purpose:** Central repository for all research claims used across [[AI]] research reports and articles. Each claim is independently verified and cross-referenced to ensure factual accuracy and allow for systematic invalidation when contradicting evidence emerges.

**Version:** 1.0.1  
**Status:** Current  
**Owner:** Florian Ziesche  
**Review Date:** 2026-03-19

---

## Source Files (Consolidated)

This ledger consolidates the following 15 original claim files:

1. [[C001 — 67% of security alerts are ignored by SOC analysts]]
2. [[C002 — 84% of LLM outputs are overconfident (verbalized confidence]]
3. [[C003 — Tool calling fails 3-15% of the time in production agent sys]]
4. [[C004 — 6% of companies achieve 'AI High Performer' status with 2-3x]]
5. [[C005 — MemoryGraft attack achieves >95% memory injection success ra]]
6. [[C006 — 80-99% false positive rate in healthcare alert systems]]
7. [[C007 — Each reminder reduces response rate by 30% (alert fatigue)]]
8. [[C008 — Klarna saved $60M with AI agents but reversed deployment due]]
9. [[C009 — VW Cariad $7.5B loss attributed to AI orchestration complexi]]
10. [[C010 — 96% of security breaches are disclosed by the attacker, not]]
11. [[C011 — LangChain grew from 0 to 100k GitHub stars in approximately]]
12. [[C012 — Vercel achieved $200M ARR via DX-first design philosophy]]
13. [[C013 — Air Canada held legally liable for chatbot hallucination]]
14. [[C014 — Grok RAG poisoning contaminated thousands of responses befor]]
15. [[C015 — Waymo required 7 collisions before issuing recall]]

**Location:** `20_Areas/[[AI]]-Research/Claims/`  
**Original files:** Preserved (not deleted) for reference

---

## Table of Contents

1. [C001 — 67% of security alerts are ignored by SOC analysts](#c001--67-of-security-alerts-are-ignored-by-soc-analysts)
2. [C002 — 84% of [[LLM]] outputs are overconfident](#c002--84-of-[[LLM]]-outputs-are-overconfident)
3. [C003 — Tool calling fails 3-15% of the time in production](#c003--tool-calling-fails-3-15-of-the-time-in-production)
4. [C004 — 6% of companies achieve [[AI]] High Performer status](#c004--6-of-companies-achieve-ai-high-performer-status)
5. [C005 — MemoryGraft attack achieves >95% success rate](#c005--memorygraft-attack-achieves-95-success-rate)
6. [C006 — 80-99% false positive rate in healthcare alert systems](#c006--80-99-false-positive-rate-in-healthcare-alert-systems)
7. [C007 — Each reminder reduces response rate by 30%](#c007--each-reminder-reduces-response-rate-by-30)
8. [C008 — Klarna saved $60M but reversed [[AI]] agent deployment](#c008--klarna-saved-60m-but-reversed-ai-agent-deployment)
9. [C009 — VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity](#c009--vw-cariad-75b-loss-attributed-to-ai-orchestration-complexity)
10. [C010 — 96% of security breaches disclosed by attacker](#c010--96-of-security-breaches-disclosed-by-attacker)
11. [C011 — LangChain grew to 100k GitHub stars in ~1 year](#c011--langchain-grew-to-100k-github-stars-in-1-year)
12. [C012 — Vercel achieved $200M ARR via DX-first philosophy](#c012--vercel-achieved-200m-arr-via-dx-first-philosophy)
13. [C013 — Air Canada held legally liable for chatbot hallucination](#c013--air-canada-held-legally-liable-for-chatbot-hallucination)
14. [C014 — Grok RAG poisoning contaminated thousands of responses](#c014--grok-rag-poisoning-contaminated-thousands-of-responses)
15. [C015 — Waymo required 7 collisions before issuing recall](#c015--waymo-required-7-collisions-before-issuing-recall)

---

## C001 — 67% of security alerts are ignored by SOC analysts

**Confidence:** HIGH  
**Source:** Vectra 2023 (n=2,000 SOC professionals)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-010]]
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C002 — 84% of [[LLM]] outputs are overconfident

**Full Claim:** 84% of [[LLM]] outputs are overconfident (verbalized confidence exceeds actual accuracy)

**Confidence:** HIGH  
**Source:** PMC/12249208 (9 models, 351 scenarios)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-009]]
- [[AR-010]]
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C003 — Tool calling fails 3-15% of the time in production

**Full Claim:** Tool calling fails 3-15% of the time in production agent systems

**Confidence:** MEDIUM  
**Source:** Michael Hannecke practitioner data + McDonald's case study  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-010]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C004 — 6% of companies achieve [[AI]] High Performer status

**Full Claim:** 6% of companies achieve '[[AI]] High Performer' status with 2-3x productivity gains

**Confidence:** HIGH  
**Source:** McKinsey State of [[AI]] 2025 (n=1,993 companies)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-012]]
- [[AR-004]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C005 — MemoryGraft attack achieves >95% success rate

**Full Claim:** MemoryGraft attack achieves >95% memory injection success rate

**Confidence:** HIGH  
**Source:** MINJA research (2024)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-010]]
- [[AR-014]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C006 — 80-99% false positive rate in healthcare alert systems

**Confidence:** MEDIUM  
**Source:** Healthcare IT literature synthesis  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C007 — Each reminder reduces response rate by 30%

**Full Claim:** Each reminder reduces response rate by 30% (alert fatigue)

**Confidence:** MEDIUM  
**Source:** Behavioral economics research  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C008 — Klarna saved $60M but reversed [[AI]] agent deployment

**Full Claim:** Klarna saved $60M with [[AI]] agents but reversed deployment due to trust failures

**Confidence:** MEDIUM  
**Source:** Public company statements + media reporting  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-012]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C009 — VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity

**Confidence:** MEDIUM  
**Source:** Industry reporting + company announcements  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-007]]
- [[AR-010]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C010 — 96% of security breaches disclosed by attacker

**Full Claim:** 96% of security breaches are disclosed by the attacker, not internal detection

**Confidence:** MEDIUM  
**Source:** Cybersecurity industry reports  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-010]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C011 — LangChain grew to 100k GitHub stars in ~1 year

**Full Claim:** LangChain grew from 0 to 100k GitHub stars in approximately 1 year

**Confidence:** MEDIUM  
**Source:** GitHub star history (approximation)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-013]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C012 — Vercel achieved $200M ARR via DX-first philosophy

**Full Claim:** Vercel achieved $200M ARR via DX-first design philosophy

**Confidence:** MEDIUM  
**Source:** Public announcements + funding rounds  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-013]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C013 — Air Canada held legally liable for chatbot hallucination

**Confidence:** HIGH  
**Source:** Court ruling 2024  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-010]]
- [[AR-001]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C014 — Grok RAG poisoning contaminated thousands of responses

**Full Claim:** Grok RAG poisoning contaminated thousands of responses before detection

**Confidence:** HIGH  
**Source:** Security disclosure 2024  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-010]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C015 — Waymo required 7 collisions before issuing recall

**Confidence:** HIGH  
**Source:** NHTSA reporting + media  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-010]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## Statistics

- **Total Claims:** 15
- **High Confidence:** 7 (47%)
- **Medium Confidence:** 8 (53%)
- **Cross-Referenced:** 6 (40%)
- **Most Used Claim:** C002, C010, C014, C015 (in [[AR-010]])

## Review Process

This ledger should be reviewed quarterly (next: 2026-03-19) to:
1. Verify all claims remain current
2. Update cross-references
3. Remove invalidated claims
4. Add new verified claims from recent research

---

*Created: 2026-02-19 by Phase 2 Consolidation*  
*Original files preserved in: 20_Areas/[[AI]]-Research/Claims/C001-C015.md*

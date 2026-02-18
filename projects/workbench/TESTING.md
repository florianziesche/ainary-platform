# Testing — Execution Platform (ISO 9001 aligned)

**Version:** 1.0 | **Date:** 2026-02-19

> See also: [ARCHITECTURE.md](ARCHITECTURE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [DB-SCHEMA.md](DB-SCHEMA.md)

---

## 1. Test Strategy

**Objective:** Ensure platform reliability, prevent regressions, and maintain output quality.

**Approach:** Backend-first testing. Every API endpoint should have at least one test covering the happy path. Quality gates (corrections, pre-flight checks, trust scoring) are tested as integration tests through the API layer.

**Priority order:**
1. API endpoint coverage (data integrity)
2. Quality layer logic (corrections, pre-flight, trust)
3. End-to-end workflows (planned)

---

## 2. Test Types

| Type | Tool | Scope | Status |
|------|------|-------|--------|
| Unit Tests | pytest | Individual functions, helpers | Partial |
| Integration Tests | pytest + httpx | API endpoints, DB interactions | Active |
| Manual Testing | Browser | UI interactions, visual checks | Ongoing |
| End-to-End | Playwright (planned) | Full user workflows | Not started |
| Load Testing | — | Performance under stress | Not started |

### Integration Tests (Primary)

Tests run against a temporary in-memory SQLite database. Each test creates its own data, calls the API via `httpx.AsyncClient`, and asserts the response.

```python
# Example: Test topic creation
async def test_create_topic(client):
    response = await client.post("/api/topics", json={"name": "Test Topic"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Topic"
```

---

## 3. Current Coverage

| Metric | Value |
|--------|-------|
| Total Tests | 56 |
| API Endpoints | ~85 |
| Endpoint Coverage | ~66% |
| Test File | `backend/test_api.py` |
| Last Run | 2026-02-19 |

### Coverage by Area

| Area | Endpoints | Tests | Coverage |
|------|-----------|-------|----------|
| Topics (CRUD) | 11 | 10 | 91% |
| Folders | 5 | 4 | 80% |
| Messages | 3 | 3 | 100% |
| Steps | 3 | 3 | 100% |
| Documents | 3 | 3 | 100% |
| Corrections | 3 | 3 | 100% |
| Trust / Skills | 3 | 3 | 100% |
| Events | 2 | 2 | 100% |
| Quality Standards | 8 | 6 | 75% |
| Pipeline | 1 | 1 | 100% |
| Preferences | 4 | 3 | 75% |
| Findings | 10 | 5 | 50% |
| Actions (CV, etc.) | 5 | 2 | 40% |
| Utility / Health | 4 | 3 | 75% |
| WebSocket | 1 | 0 | 0% |
| Connections | 5 | 3 | 60% |
| Proposals / Votes | 4 | 2 | 50% |

---

## 4. Running Tests

```bash
# Full test suite
cd backend && python3 -m pytest test_api.py -v

# Single test
python3 -m pytest test_api.py -v -k "test_create_topic"

# With output
python3 -m pytest test_api.py -v -s

# Coverage report (requires pytest-cov)
python3 -m pytest test_api.py --cov=app --cov-report=term-missing
```

**Prerequisites:** All pip dependencies installed (`fastapi`, `uvicorn`, `httpx`, `python-multipart`). No external services required — tests use in-memory SQLite.

---

## 5. Quality Gates

Beyond automated tests, the platform enforces quality through built-in mechanisms:

### Correction System
- 29+ learned rules from past mistakes
- Each correction has: rule, category, severity, violation_count
- Violations tracked automatically — high-violation rules get escalated

### Pre-Flight Checks
- Run automatically before output delivery
- Check against all active corrections + quality standards
- Score: 0-100%. Below 80% = WARNING badge

### Quality Standards
- 18 standards across output types (email, research, CV, etc.)
- Each standard has a 15-point checklist
- Standards can be promoted/demoted based on effectiveness

### Finding Promotion Gates
- Findings progress through: DRAFT → REVIEW → VERIFIED → PUBLISHED
- Each promotion requires quality criteria to be met
- Prevents unverified claims from reaching output

### Trust Scoring
- 9 skill categories with independent scores
- Score < 50 → REVIEW required (human approval)
- Score > 80 → AUTO (AI can act independently)
- Every correction adjusts the relevant skill score

---

## 6. Known Gaps

| Gap | Risk | Priority |
|-----|------|----------|
| No frontend tests | UI regressions undetected | HIGH |
| No end-to-end tests | Workflow breakage undetected | HIGH |
| No WebSocket tests | Real-time updates untested | MEDIUM |
| No load/stress tests | Unknown performance limits | LOW |
| No mutation testing | Test quality unverified | LOW |
| Coverage < 70% | Endpoint regressions possible | MEDIUM |

---

## 7. Improvement Plan

| Priority | Action | Target | Status |
|----------|--------|--------|--------|
| HIGH | Increase endpoint coverage to 85%+ | Q1 2026 | In Progress |
| HIGH | Add Playwright E2E tests for core workflows | Q2 2026 | Planned |
| MEDIUM | Add WebSocket connection tests | Q1 2026 | Planned |
| MEDIUM | CI pipeline (run tests on commit) | Q2 2026 | Planned |
| LOW | Add pytest-cov for line-level coverage | Q1 2026 | Planned |
| LOW | Load testing with locust | Q3 2026 | Planned |

### Target Workflows for E2E

1. Create topic → add message → receive AI response → approve
2. Create correction → trigger pre-flight → verify correction applied
3. Upload document → view in topic → delete
4. Move topic between folders → verify pipeline update

---

*This document is reviewed quarterly. Last review: 2026-02-19.*

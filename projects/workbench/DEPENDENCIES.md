# Dependencies — Ainary Execution Platform

**Version:** 0.12.5 | **Date:** 2026-02-19

> See also: [DOCUMENTATION.md](DOCUMENTATION.md) · [ARCHITECTURE.md](ARCHITECTURE.md)

---

## Runtime

| Component | Version | Notes |
|-----------|---------|-------|
| Python | 3.14.2 | Clang 17.0.0 (arm64) |
| SQLite | 3.51.2 | WAL mode enabled |

## Python Dependencies

| Package | Type | Purpose |
|---------|------|---------|
| fastapi | pip | Web framework — async, auto-docs, Pydantic validation |
| uvicorn | pip | ASGI server for FastAPI |
| httpx | pip | Async HTTP client for AI API calls (OpenAI, Anthropic) |
| python-multipart | pip | File upload support (multipart form data) |
| pydantic | pip | Request/response validation (bundled with FastAPI) |
| starlette | pip | ASGI toolkit (bundled with FastAPI) |
| sqlite3 | stdlib | Database driver |
| json | stdlib | JSON serialization |
| os / pathlib | stdlib | File system operations |
| asyncio | stdlib | Async support |
| math | stdlib | Compound score calculations (exp, log) |
| re | stdlib | Pre-Flight L1 regex matching |
| datetime | stdlib | Timestamps and date math |
| subprocess | stdlib | Email sending via `gog` CLI |
| mimetypes | stdlib | File type detection for viewer |
| html | stdlib | XSS escaping in file viewer |
| shutil | stdlib | Disk usage for health checks |

## External Services

| Service | Usage | Config |
|---------|-------|--------|
| OpenAI API (gpt-4o-mini) | AI chat, streaming, Mia Bridge | `OPENAI_API_KEY` env var |
| Anthropic API (claude-sonnet) | AI chat (alternative provider) | `ANTHROPIC_API_KEY` env var |
| gog CLI → Gmail API | Email sending | Pre-configured on host |
| Chrome Headless | CV PDF generation (via cv_generator.py) | Installed on host |

## Internal Modules

| File | Purpose |
|------|---------|
| `app.py` | Main backend (~3900 LOC) |
| `cv_generator.py` | CV/PDF generation engine |
| `test_api.py` | Test suite (44 tests) |
| `seed.py` | Initial data seeding |
| `seed_messages.py` | Message seeding |
| `seed_remaining.py` | Additional seed data |

## Frontend (Zero Dependencies)

- Vanilla JS — no npm, no build step, no framework
- Single `index.html` file
- CSS-in-HTML (no external stylesheets)
- Inter font (loaded via Google Fonts CDN)

---

*Zero npm dependencies. 4 pip packages. Ships with `python3 app.py`.*

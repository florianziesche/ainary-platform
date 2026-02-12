# OpenClaw Skill Library Audit
*Generated: 2026-02-10*

---

## Executive Summary

- **Total Skills:** 62
  - System Skills: 52
  - Custom Skills: 10
- **Identified Overlaps:** 8 potential consolidations
- **Usage Distribution:** 15 high-use, 25 medium-use, 22 low-use/specialized

---

## 1. System Skills (52)

### Communication & Messaging (8)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| bluebubbles | iMessage via BlueBubbles | HIGH | → imsg |
| imsg | iMessage/SMS CLI | HIGH | → bluebubbles |
| discord | Discord bot control | MEDIUM | — |
| slack | Slack integration | LOW | — |
| himalaya | Email (IMAP/SMTP) | MEDIUM | → gog |
| voice-call | Voice calls | LOW | — |
| trello | Trello boards | LOW | — |
| gog | Google Workspace (Gmail, Cal, Drive) | HIGH | → himalaya |

**Overlap Analysis:**
- `bluebubbles` ↔ `imsg`: Beide iMessage, BlueBubbles empfohlen → Konsolidieren?
- `himalaya` ↔ `gog`: Beide Email (IMAP vs Google) → Komplementär, behalten

### Productivity & Notes (7)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| notion | Notion API | HIGH | — |
| obsidian | Obsidian vaults (Markdown) | HIGH | → bear-notes, apple-notes |
| bear-notes | Bear notes CLI | LOW | → obsidian |
| apple-notes | Apple Notes (memo CLI) | MEDIUM | → obsidian |
| apple-reminders | Apple Reminders | MEDIUM | — |
| things-mac | Things app (macOS) | LOW | — |
| oracle | (Description cut off) | UNKNOWN | — |

**Overlap Analysis:**
- `obsidian` ↔ `bear-notes` ↔ `apple-notes`: Alle note-taking → Florian nutzt Obsidian primary

### Development & Coding (5)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| github | GitHub CLI (gh) | HIGH | — |
| coding-agent | Run Codex/Claude Code | MEDIUM | — |
| tmux | tmux session management | MEDIUM | — |
| clawhub | Skill search/install | MEDIUM | — |
| skill-creator | Create new skills | MEDIUM | — |

### AI & Models (7)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| gemini | Gemini CLI | MEDIUM | — |
| openai-image-gen | OpenAI DALL-E batch | LOW | → nano-banana-pro |
| nano-banana-pro | Gemini image gen/edit | LOW | → openai-image-gen |
| openai-whisper | Local Whisper (STT) | LOW | → openai-whisper-api |
| openai-whisper-api | Whisper API (STT) | MEDIUM | → openai-whisper |
| sag | ElevenLabs TTS | MEDIUM | → sherpa-onnx-tts |
| sherpa-onnx-tts | Local TTS | LOW | → sag |

**Overlap Analysis:**
- `openai-image-gen` ↔ `nano-banana-pro`: Beide image gen → Verschiedene Anbieter, behalten
- `openai-whisper` ↔ `openai-whisper-api`: Local vs API → Komplementär
- `sag` ↔ `sherpa-onnx-tts`: Cloud vs local TTS → Komplementär

### Media & Content (8)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| summarize | Content summarization | MEDIUM | — |
| gifgrep | GIF search/download | LOW | — |
| video-frames | Extract video frames | LOW | — |
| nano-pdf | Edit PDFs with NLP | LOW | — |
| blogwatcher | Monitor RSS/Atom feeds | LOW | — |
| songsee | (Music related) | LOW | — |
| spotify-player | Spotify control | LOW | — |
| sonoscli | Sonos control | LOW | — |

### Smart Home & IoT (5)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| openhue | Philips Hue control | LOW | — |
| eightctl | Eight Sleep control | LOW | — |
| blucli | BluOS CLI | LOW | — |
| camsnap | RTSP/ONVIF camera capture | LOW | — |
| peekaboo | (Description missing) | UNKNOWN | — |

### Location & Places (2)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| goplaces | Google Places API (New) | MEDIUM | → local-places |
| local-places | Google Places proxy | LOW | → goplaces |

**Overlap Analysis:**
- `goplaces` ↔ `local-places`: Beide Google Places → Konsolidieren zu goplaces

### Utilities & System (10)
| Name | Description | Usage | Overlap |
|------|-------------|-------|---------|
| 1password | 1Password CLI | HIGH | — |
| healthcheck | Security hardening | LOW | — |
| session-logs | Session logging | LOW | — |
| model-usage | Cost tracking (CodexBar) | LOW | — |
| canvas | HTML display on nodes | MEDIUM | — |
| mcporter | MCP server control | MEDIUM | — |
| food-order | Foodora reorder (ordercli) | LOW | — |
| ordercli | Food ordering | LOW | → food-order |
| wacli | (Description missing) | UNKNOWN | — |
| weather | Weather info | MEDIUM | — |

---

## 2. Custom Skills (10)

| Name | Category | Usage | Overlap | Description |
|------|----------|-------|---------|-------------|
| capability-evolver | Meta/Core | LOW | — | Self-evolution engine |
| research | Knowledge Work | HIGH | — | Research SOP |
| sota-brief | Knowledge Work | MEDIUM | ↔ research | Weekly SOTA generator |
| cv-design | Design/Documents | MEDIUM | → vc-application | LaTeX CV design |
| vc-application | Career | MEDIUM | ↔ cv-design | VC job applications |
| presentation-design | Design/Documents | LOW | ↔ pptx-design, report-design | General presentations |
| pptx-design | Design/Documents | MEDIUM | ↔ presentation-design | python-pptx PowerPoint |
| report-design | Design/Documents | MEDIUM | ↔ presentation-design | PDF reports |

**Overlap Analysis:**
- `cv-design` ↔ `vc-application`: CV design + VC application → Ähnlicher Scope, evtl. mergen
- `presentation-design` ↔ `pptx-design` ↔ `report-design`: Alle Design/Documents → Komplementär (verschiedene Outputs)
- `sota-brief` nutzt `research` → Spezialisierung, behalten

---

## 3. Semantic Overlap Matrix

### High Overlap (Consider Consolidation)
1. **iMessage:** `bluebubbles` + `imsg` → Pick one (BlueBubbles recommended)
2. **Places:** `goplaces` + `local-places` → Use goplaces
3. **Food:** `food-order` + `ordercli` → Same tool, merge

### Medium Overlap (Complementary, Keep Both)
4. **Email:** `himalaya` (IMAP) + `gog` (Google) → Different protocols
5. **Notes:** `obsidian` (primary) + `bear-notes` + `apple-notes` → Different ecosystems
6. **Image Gen:** `openai-image-gen` + `nano-banana-pro` → Different providers
7. **STT:** `openai-whisper` (local) + `openai-whisper-api` → Local vs cloud
8. **TTS:** `sag` (ElevenLabs) + `sherpa-onnx-tts` → Cloud vs local

### Low Overlap (Specialized, Keep)
- All custom design skills (different output formats)
- Smart home skills (different devices)
- Development tools (different purposes)

---

## 4. Usage Frequency Estimate

### HIGH (Daily/Multiple Times per Day) — 15 skills
- bluebubbles/imsg
- notion
- obsidian
- github
- 1password
- gog (Email/Calendar)
- discord
- research
- himalaya
- coding-agent
- canvas
- mcporter
- goplaces
- sag
- openai-whisper-api

### MEDIUM (Weekly) — 25 skills
- apple-notes
- apple-reminders
- tmux
- clawhub
- skill-creator
- gemini
- summarize
- weather
- sota-brief
- cv-design
- vc-application
- pptx-design
- report-design
- slack
- nano-banana-pro
- blogwatcher
- nano-pdf
- video-frames
- session-logs
- model-usage
- food-order

### LOW (Monthly or Specialized) — 22 skills
- bear-notes
- things-mac
- openai-image-gen
- openai-whisper
- sherpa-onnx-tts
- gifgrep
- songsee
- spotify-player
- sonoscli
- openhue
- eightctl
- blucli
- camsnap
- peekaboo
- local-places
- healthcheck
- trello
- voice-call
- wacli
- oracle
- ordercli
- capability-evolver
- presentation-design

---

## 5. Recommendations

### Immediate Actions
1. **Merge:** `food-order` + `ordercli` (same tool)
2. **Deprecate:** Choose `bluebubbles` OR `imsg` (recommend bluebubbles)
3. **Merge:** `goplaces` should replace `local-places`

### Consider for Future
4. **Document:** Usage patterns for `obsidian` vs `bear-notes` vs `apple-notes` → Establish primary
5. **Review:** `cv-design` + `vc-application` → Could be one skill with LaTeX templates
6. **Audit:** Unknown skills: `oracle`, `peekaboo`, `wacli` → Get descriptions

### Skill Gaps (Potential New Skills)
- **LinkedIn scraping/automation** (for job search)
- **CRM/contact management** (for networking)
- **Finance tracking** (expenses, revenue)
- **Meeting scheduler** (Calendly-like)

---

## 6. Skill Count by Category

| Category | System | Custom | Total |
|----------|--------|--------|-------|
| Communication | 8 | 0 | 8 |
| Productivity/Notes | 7 | 0 | 7 |
| Development | 5 | 0 | 5 |
| AI/Models | 7 | 0 | 7 |
| Media/Content | 8 | 0 | 8 |
| Smart Home/IoT | 5 | 0 | 5 |
| Location | 2 | 0 | 2 |
| Utilities/System | 10 | 0 | 10 |
| Knowledge Work | 0 | 2 | 2 |
| Design/Documents | 0 | 4 | 4 |
| Meta/Core | 0 | 1 | 1 |
| Career | 0 | 1 | 1 |
| **TOTAL** | **52** | **10** | **62** |

---

*End of Audit*

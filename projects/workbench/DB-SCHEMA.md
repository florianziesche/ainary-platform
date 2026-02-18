# Database Schema — Ainary Execution Platform

**Version:** 0.12.5 | **Date:** 2026-02-19 | **Engine:** SQLite 3.51.2 (WAL mode)

> Reference documentation for all 27 tables in `workbench.db`.
> See also: [DOCUMENTATION.md](DOCUMENTATION.md) · [ARCHITECTURE.md](ARCHITECTURE.md) · [FORMULAS.md](FORMULAS.md)

---

## activity_feed

Activity log for all agent actions. Powers the Activity Feed, Digest, and Impact Summary.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| agent | TEXT | NULL | Agent name (HUNTER, WRITER, RESEARCHER, OPERATOR, DEALMAKER) |
| action | TEXT | NULL | Action performed (e.g. "email_sent", "cv_generated") |
| detail | TEXT | NULL | Human-readable description |
| result | TEXT | 'success' | Outcome: success, failed, skipped |
| impact_type | TEXT | NULL | Category: revenue, pipeline, quality, system |
| impact_value | REAL | 0 | Numeric impact (e.g. revenue amount, count) |
| date | TEXT | NULL | ISO date (YYYY-MM-DD) |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |

---

## backlog

Prioritized backlog items for task management.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| description | TEXT | NULL | Task description |
| source | TEXT | 'florian' | Who created it (florian, mia, system) |
| priority | TEXT | 'NORMAL' | NOW, HIGH, NORMAL, LOW |
| status | TEXT | 'backlog' | backlog, in_progress, done, cancelled |
| assigned_to | TEXT | NULL | Agent or person assigned |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TIMESTAMP | CURRENT_TIMESTAMP | Last update time |

---

## confidence_history

Audit trail for all confidence changes on findings. Enables Bayesian update tracking.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| finding_id | TEXT | NULL | FK → findings.id |
| old_confidence | REAL | NULL | Previous confidence value (0.0–1.0) |
| new_confidence | REAL | NULL | New confidence value (0.0–1.0) |
| reason | TEXT | NULL | Why confidence changed |
| source | TEXT | NULL | Source type that triggered the change |
| created_at | TEXT | CURRENT_TIMESTAMP | When the change occurred |

---

## connections

Directed graph edges between topics. Enables cross-stage pipeline tracking.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| from_topic | TEXT | NULL | FK → topics.id (source) |
| to_topic | TEXT | NULL | FK → topics.id (target) |
| relation | TEXT | NULL | Relationship label (e.g. "feeds_into", "blocks") |

---

## corrections

Learned rules from user feedback. Core of the Correction Propagation engine.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| rule | TEXT | NULL | Human-readable correction rule |
| category | TEXT | 'general' | design, content, process, tone, facts |
| wrong | TEXT | '' | Example of wrong output |
| rght | TEXT | '' | Example of correct output |
| source_topic | TEXT | NULL | Topic where correction originated |
| severity | INTEGER | 2 | 1=minor, 2=standard, 3=critical |
| active | INTEGER | 1 | Whether this rule is enforced |
| violation_count | INTEGER | 0 | Times this rule was violated |
| last_violated | TEXT | NULL | ISO timestamp of last violation |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |
| patterns | TEXT | '[]' | JSON array of regex patterns for L1 matching |
| output_types | TEXT | '[]' | JSON array of applicable output types (or ["all"]) |

---

## daily_scores

Daily standup scores. One row per day. Powers the standup history chart.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| date | TEXT | NULL | ISO date (YYYY-MM-DD), unique per day |
| score_reset | INTEGER | 100 | Starting score for the day |
| score_current | INTEGER | 100 | Current calculated score |
| score_ema | REAL | 100.0 | 7-day Exponential Moving Average |
| tasks_committed | INTEGER | 0 | Number of committed tasks |
| tasks_completed | INTEGER | 0 | Number of completed committed tasks |
| tasks_extra | INTEGER | 0 | Number of bonus tasks completed |
| sends | INTEGER | 0 | Number of sends (emails, applications) |
| notes | TEXT | NULL | Daily notes |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TIMESTAMP | CURRENT_TIMESTAMP | Last update time |

---

## daily_tasks

Individual standup tasks within a day.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| date | TEXT | NULL | ISO date (YYYY-MM-DD) |
| description | TEXT | NULL | Task description |
| type | TEXT | 'committed' | committed or extra |
| status | TEXT | 'pending' | pending, done, missed |
| is_send | INTEGER | 0 | 1 if this is a send action (bonus points) |
| points | INTEGER | 0 | Calculated points for this task |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TIMESTAMP | CURRENT_TIMESTAMP | Last update time |

---

## decisions

Decision log. Tracks Mia recommendations vs. Florian's actual decisions.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| decision_id | TEXT | NULL | Unique decision identifier (e.g. "D-001") |
| date | TEXT | NULL | ISO date of decision |
| question | TEXT | NULL | Decision question |
| options | TEXT | NULL | Available options (text or JSON) |
| mia_recommendation | TEXT | NULL | What Mia recommended |
| florian_decision | TEXT | NULL | What Florian chose |
| recommendation_followed | INTEGER | 1 | 1 = followed, 0 = overridden |
| reason | TEXT | NULL | Rationale for the decision |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |

---

## documents

Files and references attached to topics.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| topic_id | TEXT | NULL | FK → topics.id |
| name | TEXT | NULL | Display name |
| path | TEXT | NULL | Relative file path (projects/workbench/uploads/...) |
| url | TEXT | NULL | External URL |
| doc_type | TEXT | 'file' | file, pdf, html, md, txt, doc, ref |
| kind | TEXT | 'doc' | doc (document) or ref (reference) |

---

## eval_responses

Evaluation questionnaire responses.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| question_id | INTEGER | NULL | Reference to question |
| answers | TEXT | NULL | JSON array of selected answers |
| session_date | TEXT | NULL | Date of evaluation session |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## events

Audit log for all system events. Every state change, upload, feedback action is logged here.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| topic_id | TEXT | NULL | FK → topics.id (nullable for global events) |
| event_type | TEXT | NULL | Event category (state_change, file_uploaded, trust_feedback, action_queued, etc.) |
| detail | TEXT | '{}' | JSON payload with event-specific data |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## findings

Core knowledge engine table. Each row is a claim/finding with confidence tracking.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | TEXT | PK | Unique ID (RF-001, RF-002, ...) |
| claim | TEXT | NULL | The finding/claim text |
| context | TEXT | NULL | Additional context |
| confidence | REAL | 0.50 | Current confidence (0.0–1.0) |
| status | TEXT | 'alive' | alive, contested, dead |
| killed_by | TEXT | NULL | What killed this finding |
| source_type | TEXT | NULL | own_hypothesis, conversation, industry_report, academic_paper, own_data, revenue_validated |
| source_detail | TEXT | NULL | Source description |
| extracted_from | TEXT | NULL | Original document/conversation |
| tags | TEXT | '[]' | JSON array of tags |
| research_line | TEXT | NULL | Associated research line |
| used_in_systems | TEXT | '[]' | JSON array of system references |
| used_in_content | TEXT | '[]' | JSON array of content references |
| used_in_revenue | TEXT | '[]' | JSON array of revenue references |
| supports | TEXT | '[]' | JSON array of finding IDs this supports |
| contradicts | TEXT | '[]' | JSON array of finding IDs this contradicts |
| derived_from | TEXT | '[]' | JSON array of parent finding IDs |
| compound_score | REAL | 0.0 | Calculated compound score (see FORMULAS.md) |
| topic_id | TEXT | NULL | FK → topics.id |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TEXT | CURRENT_TIMESTAMP | Last update time |
| verified | INTEGER | 0 | 1 = human-verified |
| source_url | TEXT | NULL | URL of source |
| stage | TEXT | 'research' | Pipeline stage: research, systems, content, revenue |
| evidence_type | TEXT | NULL | E=Empirical, I=Industry, J=Journalistic, A=Anecdotal |
| impact | TEXT | 'MEDIUM' | LOW, MEDIUM, HIGH |
| impact_estimate | TEXT | NULL | Estimated impact description |
| sources_count | INTEGER | 0 | Number of independent sources |

---

## folders

Hierarchical folder structure for topic organization.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | TEXT | PK | Unique folder ID |
| name | TEXT | NULL | Display name |
| parent_id | TEXT | NULL | FK → folders.id (self-referencing) |
| position | INTEGER | 0 | Sort order within parent |
| color | TEXT | NULL | CSS color for UI |
| icon | TEXT | NULL | Icon identifier |
| collapsed | INTEGER | 0 | 1 = collapsed in UI |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## messages

Conversation messages within topics.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| topic_id | TEXT | NULL | FK → topics.id |
| sender | TEXT | NULL | human, mia, system |
| content | TEXT | NULL | Message text |
| msg_type | TEXT | 'text' | text, system, error |
| meta | TEXT | '{}' | JSON metadata |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## monthly_goals

Monthly goal tracking for the Executive Board.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| month | TEXT | NULL | YYYY-MM format |
| description | TEXT | NULL | Goal description |
| target_value | INTEGER | 1 | Target metric |
| current_value | INTEGER | 0 | Current progress |
| status | TEXT | 'pending' | pending, in_progress, done, missed |
| sort_order | INTEGER | 0 | Display order |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TIMESTAMP | CURRENT_TIMESTAMP | Last update time |

---

## preferences

Learned user preferences per scope. Schema for preference learning engine.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| scope | TEXT | NULL | Preference scope (e.g. "email", "linkedin", "global") |
| key | TEXT | NULL | Preference key |
| value | TEXT | NULL | Preference value |
| confidence | INTEGER | 50 | Confidence in this preference (0–100) |
| data_points | INTEGER | 0 | Number of observations |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TEXT | CURRENT_TIMESTAMP | Last update time |

---

## proposals

AI-generated recommendations with options, attached to messages.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| message_id | INTEGER | NULL | FK → messages.id |
| proposal_type | TEXT | NULL | Type: Recommendation, Confirmation, Priority, Clarification, etc. |
| content | TEXT | NULL | Proposal description |
| confidence | INTEGER | NULL | AI confidence (0–100) |
| confidence_reason | TEXT | NULL | Why this confidence level |
| options | TEXT | '[]' | JSON array of options [{title, recommended, description, draft?}] |
| chosen_option | TEXT | NULL | Selected option letter (A, B, C) |
| meta | TEXT | '{}' | JSON metadata |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## quality_standards

Per-output-type quality rules. Applied in Pre-Flight L2 checks.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| rule | TEXT | NULL | Quality standard description |
| category | TEXT | 'general' | Standard category |
| output_type | TEXT | 'general' | Applicable output type (email, linkedin, blog, report, website, general) |
| active | INTEGER | 1 | Whether this standard is enforced |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## research_lines

Research line definitions for organizing findings.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | TEXT | PK | Unique ID |
| name | TEXT | NULL | Research line name |
| description | TEXT | NULL | Description |
| status | TEXT | 'active' | active, completed, abandoned |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## revenue_events

Revenue tracking for Executive Board KPIs.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| amount | REAL | NULL | Revenue amount in EUR |
| source | TEXT | NULL | Revenue source description |
| description | TEXT | NULL | Detail |
| date | TEXT | NULL | ISO date |
| created_at | TIMESTAMP | CURRENT_TIMESTAMP | Row creation time |

---

## running_tasks

Currently executing background tasks.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| description | TEXT | NULL | Task description |
| agent | TEXT | NULL | Executing agent |
| status | TEXT | 'running' | running, completed, failed |
| started_at | TIMESTAMP | CURRENT_TIMESTAMP | Start time |
| completed_at | TIMESTAMP | NULL | Completion time |
| result | TEXT | NULL | Result or error message |

---

## steps

Progress tracking steps within topics.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| topic_id | TEXT | NULL | FK → topics.id |
| label | TEXT | NULL | Step description |
| done | INTEGER | 0 | 1 = completed |
| position | INTEGER | 0 | Sort order |

---

## topics

Core work items. The primary entity in the platform.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | TEXT | PK | Unique topic ID |
| name | TEXT | NULL | Topic name |
| stage | TEXT | 'revenue' | Pipeline stage: research, systems, content, revenue |
| parent_id | TEXT | NULL | Parent topic (unused in current version) |
| progress | INTEGER | 0 | Completion percentage (0–100), auto-calculated from steps |
| meta | TEXT | '{}' | JSON metadata (contact, email, potential, deadline, output_type, etc.) |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |
| updated_at | TEXT | CURRENT_TIMESTAMP | Last update time |
| folder_id | TEXT | NULL | FK → folders.id |
| folder_position | INTEGER | 0 | Sort order within folder |
| state | TEXT | 'active' | State machine: active, running, blocked, done, error, archived |
| priority | TEXT | 'NORMAL' | NOW, HIGH, NORMAL, LOW |
| priority_reason | TEXT | '' | Why this priority |
| priority_confidence | INTEGER | 50 | Confidence in priority (0–100) |

---

## trust_scores

Agent-level trust scores (legacy, before per-skill trust).

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| agent | TEXT | PK | Agent name |
| score | INTEGER | 0 | Current trust score |
| total_votes | INTEGER | 0 | Total feedback count |
| up_votes | INTEGER | 0 | Positive feedback count |
| down_votes | INTEGER | 0 | Negative feedback count |
| updated_at | TEXT | CURRENT_TIMESTAMP | Last update time |

---

## trust_skills

Per-skill Bayesian trust scores. Powers the graduated autonomy system.

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| skill | TEXT | PK | Skill name (research, email, cv, linkedin, etc.) |
| score | INTEGER | 50 | Bayesian trust score (0–100) |
| total | INTEGER | 0 | Total feedback count |
| up | INTEGER | 0 | Positive feedback count |
| down | INTEGER | 0 | Negative feedback count |
| updated_at | TEXT | CURRENT_TIMESTAMP | Last update time |

---

## votes

User votes on proposals (up/down).

| Column | Type | Default | Description |
|--------|------|---------|-------------|
| id | INTEGER | PK AUTO | Primary key |
| proposal_id | INTEGER | NULL | FK → proposals.id |
| direction | TEXT | NULL | up or down |
| created_at | TEXT | CURRENT_TIMESTAMP | Row creation time |

---

## Entity Relationship Summary

```
folders 1──∞ topics 1──∞ messages 1──∞ proposals 1──∞ votes
                │
                ├──∞ steps
                ├──∞ documents
                ├──∞ events
                ├──∞ findings 1──∞ confidence_history
                └──∞ connections (self-referencing)

daily_scores 1──∞ daily_tasks (by date)
corrections (global)
quality_standards (global)
trust_skills (global)
trust_scores (global, legacy)
preferences (global)
decisions (global)
backlog (global)
activity_feed (global)
revenue_events (global)
monthly_goals (global)
research_lines (global)
running_tasks (global)
eval_responses (global)
```

---

*27 tables. Generated from live schema inspection on 2026-02-19.*

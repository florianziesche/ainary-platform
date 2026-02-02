# 📋 Task Kanban Board

*Visualize work. Limit WIP. Deliver consistently.*

---

## Board Views

### 🔄 Kanban View

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│    📥 BACKLOG   │   🏃 IN PROGRESS │    👀 REVIEW    │    ✅ DONE      │
│    (No Limit)   │     (WIP: 3)    │     (WIP: 2)    │                 │
├─────────────────┼─────────────────┼─────────────────┼─────────────────┤
│                 │                 │                 │                 │
│  [Task Card]    │  [Task Card]    │  [Task Card]    │  [Task Card]    │
│                 │                 │                 │                 │
│  [Task Card]    │  [Task Card]    │                 │  [Task Card]    │
│                 │                 │                 │                 │
│  [Task Card]    │                 │                 │  [Task Card]    │
│                 │                 │                 │                 │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

---

## Task Card Template

### [Task Title]

| Field | Value |
|-------|-------|
| **ID** | TSK-### |
| **Priority** | 🔴 High / 🟡 Medium / 🟢 Low |
| **Type** | Feature / Bug / Task / Research |
| **Assignee** | |
| **Due Date** | |
| **Estimate** | h / points |

**Description:**
> 

**Acceptance Criteria:**
- [ ] 
- [ ] 

**Blocked By:** 
**Blocks:** 

---

## Task Database

| ID | Task | Status | Priority | Assignee | Due | Est. |
|----|------|--------|----------|----------|-----|------|
| TSK-001 | | 📥 | 🔴 | | | |
| TSK-002 | | 🏃 | 🟡 | | | |
| TSK-003 | | 👀 | 🟢 | | | |
| TSK-004 | | ✅ | | | | |

---

## Status Definitions

| Status | Icon | Description | Exit Criteria |
|--------|------|-------------|---------------|
| **Backlog** | 📥 | Waiting to be started | Prioritized, requirements clear |
| **In Progress** | 🏃 | Actively being worked on | Work started |
| **Review** | 👀 | Waiting for review/approval | Work complete, needs check |
| **Done** | ✅ | Complete and shipped | Accepted, deployed |
| **Blocked** | 🚫 | Cannot proceed | Blocker identified |

---

## Priority Matrix

|  | Urgent | Not Urgent |
|--|--------|------------|
| **Important** | 🔴 Do First | 🟡 Schedule |
| **Not Important** | 🟠 Delegate | 🟢 Eliminate |

---

## Weekly Metrics

| Week | Backlog | In Progress | Done | Lead Time | Cycle Time |
|------|---------|-------------|------|-----------|------------|
| W1 | | | | days | days |
| W2 | | | | days | days |
| W3 | | | | days | days |
| W4 | | | | days | days |

---

## Filters & Views

### By Priority
- 🔴 High Priority Tasks
- 🟡 Medium Priority Tasks
- 🟢 Low Priority Tasks

### By Assignee
- My Tasks
- Unassigned
- [Team Member]

### By Type
- Features
- Bugs
- Research
- Admin

### By Due Date
- Overdue
- Due This Week
- Due Next Week
- No Due Date

---

## Quick Add

**New Task:**
| Field | Value |
|-------|-------|
| Title | |
| Priority | 🔴 🟡 🟢 |
| Assignee | |
| Due | |
| Description | |

---

## WIP Limits

| Column | Limit | Current | Status |
|--------|-------|---------|--------|
| In Progress | 3 | | 🟢 🟡 🔴 |
| Review | 2 | | 🟢 🟡 🔴 |

**Why WIP Limits?**
- Focus on finishing, not starting
- Reduce context switching
- Surface bottlenecks quickly

---

## Archive (Completed)

| ID | Task | Completed | Cycle Time |
|----|------|-----------|------------|
| | | | |
| | | | |

---

*Template by Florian Ziesche • CEO Framework*

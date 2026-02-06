---
date: {{date:YYYY-MM-DD}}
week: {{date:YYYY-[W]WW}}
type: weekly-review
tags:
  - review
  - weekly
created: {{date:YYYY-MM-DD HH:mm}}
---

# Weekly Review — Week {{date:WW, YYYY}}

**Week of:** {{date:MMMM DD, YYYY}}  
**Review completed:** {{date:YYYY-MM-DD}}

---

## 📊 Week at a Glance

**Overall rating:** ⭐️⭐️⭐️⭐️⭐️ (1-5)

**Energy level:** 🔋🔋🔋🔋🔋 (1-5)

**Focus quality:** 🎯🎯🎯🎯🎯 (1-5)

**One-word summary:**  

---

## ✅ Wins This Week

*What went well? What are you proud of?*

1. 
2. 
3. 

---

## 📉 Challenges & Learnings

*What was hard? What did you learn?*

**Challenges:**
- 

**Lessons learned:**
- 

**What to do differently:**
- 

---

## 📋 Inbox Processing

**Items in Inbox:** [X]

- [ ] Move notes to proper folders
- [ ] Delete noise
- [ ] Create links
- [ ] Extract action items

**Notes processed:**
- [[]] → moved to [folder]
- [[]] → deleted (not relevant)
- [[]] → linked to [[]]

---

## 🎯 Projects Review

*Check status of all active projects.*

```dataview
TABLE status, progress, deadline
FROM "10-Projects"
WHERE status != "archived"
SORT priority DESC
```

**Updates:**
- **[[Project A]]:** 
  - Status: 
  - Progress this week: 
  - Blockers: 
  - Next steps: 

- **[[Project B]]:** 
  - Status: 
  - Progress this week: 
  - Blockers: 
  - Next steps: 

**Projects to archive:**
- [ ] [[]]

---

## 👥 People Review

*Who did you connect with? Who needs follow-up?*

**Talked to:**
- [[]] — [[meeting note or context]]
- [[]]

**Need to follow up:**
- [ ] [[Person]] — [what to do]
- [ ] 

**Haven't talked to in a while (should reach out):**
- [[]]

---

## ✅ Tasks Review

**Tasks completed this week:**
- [x] 
- [x] 

**Tasks rolled over (not done):**
- [ ] 
  - Why not done: 
  - Still relevant: Yes/No
  - Move to: [when/where]

**Recurring tasks:**
- [ ] Check if recurring tasks are still needed
- [ ] Update or remove outdated ones

---

## 📚 Knowledge Review

**Notes created this week:**

```dataview
TABLE type, tags
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
LIMIT 10
```

**Best note:**  
[[]] — because:

**Notes to expand:**
- [[]]

**Notes to link:**
- [[]] ↔ [[]]

---

## 🧠 Insights & Patterns

*What patterns did you notice? Themes that emerged?*

**Themes this week:**
- 
- 

**Recurring thoughts:**
- 

**Ideas worth exploring:**
- 

---

## 📖 Content Consumed

**Books:**
- [[]] — [progress or status]

**Articles/Essays:**
- [Title](URL) — key takeaway: 

**Podcasts/Videos:**
- [Title](URL) — main idea: 

**Best thing I read/watched:**  


---

## 🎬 Next Week Planning

### Top 3 Priorities

1. **[[Project/Area]]** — [specific outcome]
2. **[[Project/Area]]** — [specific outcome]
3. **[[Project/Area]]** — [specific outcome]

### Key Tasks

**Must do:**
- [ ] 
- [ ] 
- [ ] 

**Should do:**
- [ ] 
- [ ] 

**Nice to have:**
- [ ] 

### Scheduled

**Meetings:**
- [[YYYY-MM-DD]] — [[Meeting with X]]
- [[YYYY-MM-DD]] — [[Meeting with Y]]

**Deadlines:**
- [[YYYY-MM-DD]] — [[Deliverable]]

**Blocks for deep work:**
- Monday AM: [Project]
- Wednesday AM: [Project]
- Friday AM: [Review]

---

## 🧹 Cleanup Tasks

- [ ] Archive completed projects
- [ ] Update project statuses and progress
- [ ] Review and update person notes
- [ ] Fix broken links (if any)
- [ ] Tag cleanup (merge redundant tags)
- [ ] Update dashboards

---

## 💡 Experiments & Habits

**Habit tracker:**

| Habit | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Total |
|-------|-----|-----|-----|-----|-----|-----|-----|-------|
| Daily note | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 6/7 |
| Exercise | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 4/7 |
| Deep work block | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | 4/7 |
| Read 30min | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 6/7 |

**New experiment to try:**


**Experiment to stop:**


---

## 🎯 Goal Progress

*Check in on quarterly/yearly goals.*

**Q1 2026 Goals:**

| Goal | Target | Current | Progress |
|------|--------|---------|----------|
| [Goal 1] | [Target] | [Current] | [%] |
| [Goal 2] | [Target] | [Current] | [%] |
| [Goal 3] | [Target] | [Current] | [%] |

**On track / Behind / Ahead?**


**Adjustments needed:**


---

## 🌟 Gratitude

*Three things I'm grateful for this week:*

1. 
2. 
3. 

---

## 📝 Free Reflection

*Anything else on your mind?*



---

## ✅ Review Checklist

- [ ] Processed Inbox (00-Inbox/)
- [ ] Reviewed all active projects
- [ ] Updated project statuses
- [ ] Reviewed people notes + follow-ups
- [ ] Checked tasks (done, rolled over, deleted)
- [ ] Archived completed items
- [ ] Cleaned up tags
- [ ] Set top 3 priorities for next week
- [ ] Scheduled deep work blocks
- [ ] Reviewed habit tracker
- [ ] Checked goal progress

---

> [!success] Review Complete!
> You've processed the week and set yourself up for success.
> 
> **Next review:** [[{{date:YYYY-MM-DD|TP_NEXT_WEEK:+7 days}}]]

> [!tip] Weekly Review Tips
> - Block 30-60 minutes every Friday or Sunday
> - Don't skip this — it's the secret to the system working
> - Use queries to surface what needs attention
> - Be honest about what's working and what's not
> - Adjust the template to fit your needs

---

**Previous review:** [[{{date:YYYY-MM-DD|TP_LAST_WEEK:-7 days}}]]  
**Next review:** [[{{date:YYYY-MM-DD|TP_NEXT_WEEK:+7 days}}]]

---

*Template version 1.0*

# Obsidian Standards Audit — v2 (Deep Review)

*Generated: 2026-02-17 | Auditor: Mia*
*Method: Full read of all 24 Obsidian files + 6 active workspace standards. Each decision stress-tested.*

---

## Summary
- **Total files:** 24
- **KEEP:** 4
- **ARCHIVE:** 18
- **DELETE:** 2

**Result: 24 → 4 files.** Each one passes the test: "If Florian had only 5 files in this folder, would THIS one make the cut?"

---

## The 4 Files That Earn Their Place

### 1. Twin.md ✅ KEEP
- **Lines:** 167
- **Purpose:** Mia's autonomous decision model — when to act vs. ask Florian
- **Why it stays:** AGENTS.md explicitly says "Check TWIN.md" before every task. This is operationally active. The autonomy rules (format, language, priority, escalation), calibration log, and drift detection are unique — nothing in workspace replicates this. It's the decision engine for Mia's independence.
- **Quality:** High — calibrated against real decisions (KW06 log shows 2/4 match rate)
- **Overlap:** None in workspace. Should be COPIED to `workspace/standards/TWIN.md` since AGENTS.md references it.
- **McKinsey test:** Yes — it's a decision rights matrix. Every consulting firm has one.
- **Confidence:** 95%
- **⚠️ Action needed:** Copy to workspace so Mia can reference it without Obsidian access.

### 2. Mental-Models-Lookup.md ✅ KEEP
- **Lines:** 262
- **Purpose:** Situation → mental model → action lookup (8 situations: negotiating, stuck, hard decisions, writing, building, AI agents, quality, strategy)
- **Why it stays:** Challenge I asked myself: "Isn't this just a summary of business books?" Answer: No — the value is the LOOKUP FORMAT. When Mia faces a negotiation, she doesn't need to re-derive Voss/Cialdini — she looks up the action line. The "Managing AI Agents" section (DECO framework, Trust Curve) is directly operational. The quick reference table at the bottom is genuine decision support.
- **Quality:** High — actionable, well-organized, each situation has concrete "Action:" line
- **Overlap:** None anywhere in workspace or Obsidian
- **McKinsey test:** Yes — this is literally how consultants use frameworks. Match situation → apply model.
- **Confidence:** 90%

### 3. 3-Lean-Checklists.md ✅ KEEP
- **Lines:** 254
- **Purpose:** Three 7-item checklists (Content, Outreach, Deliverable) based on Munger/Gawande
- **Why it stays:** Challenge I asked myself: "Don't the workspace standards already have checklists?" Answer: RESEARCH-PROTOCOL and SYNTHESIS-PROTOCOL have THEIR OWN checklists for research/synthesis. But the OUTREACH checklist (personalized hook, value first, one clear ask, proof of relevance, brevity, low-friction response, typo check) exists NOWHERE else. And the before/after examples are genuinely useful teaching material — the "Before" LinkedIn email vs "After" is something I'd re-read before drafting outreach.
- **Quality:** High — the examples alone justify the file
- **Overlap:** Content checklist partially overlaps with CONTENT-VOICE.md. Deliverable checklist partially overlaps with SYNTHESIS-PROTOCOL.md. But Outreach checklist is unique.
- **McKinsey test:** Yes — checklists are Gawande's central thesis, and the "killer items" framing is Munger. Solid intellectual foundation.
- **Confidence:** 85% — borderline because of partial overlap, but the Outreach checklist and examples tip it to KEEP

### 4. DESIGN-SYSTEM.md ✅ KEEP
- **Lines:** 605
- **Purpose:** Full component CSS for the Intelligence Platform — cards, buttons, badges, pricing, navigation, inputs, spacing system
- **Why it stays:** I initially marked this ARCHIVE. Wrong. Challenge: "Where does Mia get component CSS if this is archived?" Answer: Nowhere. Workspace BRAND.md = 50 lines (colors + fonts only). WEBSITE-DESIGN-GUIDE.md = copywriting + marketing frameworks, zero CSS. This is the ONLY file with production-ready component code: card styles, button hierarchy (primary/secondary/ghost), badge styling, pricing card layout, input fields, navigation bar, spacing system, responsive breakpoints. Without it, every HTML build starts from scratch.
- **Quality:** High — copy-paste-ready CSS, internally consistent design system
- **Overlap:** Color values CONFLICT with BRAND.md (this file: Indigo #6366f1 as primary + Gold #c8aa50 as special; BRAND.md: Gold-only). Font stack also differs (this file: Geist for headlines; BRAND.md: Inter Display). These conflicts MUST be resolved.
- **McKinsey test:** Not applicable (this is a dev reference, not a strategy doc). But the equivalent test: "Would a designer reference this?" — yes, absolutely.
- **Confidence:** 80% — high value but the BRAND.md conflicts are a real problem
- **⚠️ Action needed:** Florian must decide: Is the website Indigo+Gold (DESIGN-SYSTEM) or Gold-only (BRAND.md)? Geist or Inter Display for headlines? Reconcile, then update whichever file is wrong.

---

## The 18 Files to Archive

### Quality-Check Cluster (4 files → all ARCHIVE)

These 4 files are variations on the same theme: "check your work before delivering." The workspace standards (RESEARCH-PROTOCOL, SYNTHESIS-PROTOCOL, CONTENT-VOICE, FLORIAN.md) already embed quality checks. Keeping any of these creates redundant process layers.

#### Output-Preflight.md → ARCHIVE
- **Lines:** 285
- **Purpose:** 6 meta-rules + 5 pre-output questions
- **Quality:** High — this is genuinely well-written. The 6 meta-rules (Answer-First, Audience-Tag, Confidence, So-What, Source, Flag-Gaps) are excellent.
- **Why archive anyway:** Every one of the 6 meta-rules is already embedded in the active workspace standards. Answer-First = SYNTHESIS-PROTOCOL's SCQA. Confidence = SYNTHESIS-PROTOCOL's calibrated language. Source = RESEARCH-PROTOCOL's Admiralty system. The 5 pre-output questions are good but Florian never references this file — Mia loads the workspace standards directly.
- **Confidence:** 85% — high quality content, but redundant with active standards

#### Before-Any-Output.md → ARCHIVE
- **Lines:** 69
- **Purpose:** Short pre-flight checklist
- **Why archive:** File literally describes itself as "Kurzform" of Output-Preflight. If the long version is archived, the short version goes too. The 2 unique items ("search INDEX.md first", "check encoding") are one-liners that belong in AGENTS.md, not a standalone file.
- **Confidence:** 95%

#### Definition-of-Done.md → ARCHIVE
- **Lines:** 164
- **Purpose:** "Ready-to-send" package concept
- **Why archive:** The core insight ("Meine Fertig = 30%, Florians Fertig = 100%") is already captured in workspace FLORIAN.md ("Florian nutzt Outputs die er SOFORT verwenden kann"). The package structures (outreach/ready-to-send/, content/ready-to-publish/) were designed but never implemented — they're aspirational architecture. The hidden expectations table is good but it's 5 rows of common sense.
- **Confidence:** 88%

#### DONE-GAP-DETECTOR.md → ARCHIVE
- **Lines:** 65
- **Purpose:** Adversarial self-check + completion scoring
- **Why archive:** The adversarial framing ("What is WRONG?") is a good principle — but it's a behavioral habit, not a document you reference. The completion score (10%-100%) duplicates the confidence ratings in SYNTHESIS-PROTOCOL. The adversarial questions by context (research, emails, code, strategy) are useful but could be 4 lines in AGENTS.md.
- **Confidence:** 85%

---

### Sub-Agent Routing Cluster (3 files → all ARCHIVE)

Three files about the same topic: when to spawn sub-agents. None are actively referenced — workspace AGENTS.md handles routing. The Γ-metric system they all reference was never implemented (no gamma-log.jsonl exists).

#### AGENT-DECISION-FRAMEWORK.md → ARCHIVE
- **Lines:** 490
- **Purpose:** Detailed framework for sub-agent spawning with Γ-metric tracking
- **Why archive:** 490 lines of theoretical infrastructure for a system that was never measured. The Γ-metric is clever but requires logging that doesn't exist. OpenClaw handles routing decisions operationally; this is over-engineered process documentation.
- **Confidence:** 95%

#### MULTI-AGENT-RULES.md → ARCHIVE
- **Lines:** 240
- **Purpose:** Single vs multi-agent decision tree
- **Why archive:** Covers the same ground as AGENT-DECISION-FRAMEWORK with different formatting. The decision tree is simpler but still redundant with AGENTS.md.
- **Confidence:** 95%

#### SPAWN-DECISION-QUICKREF.md → ARCHIVE
- **Lines:** 169
- **Purpose:** Quick reference card for the above two files
- **Why archive:** A quick-reference card for documents that are themselves being archived. The 3-second decision ("Output < 15k tokens? → NO SUB-AGENT") is already intuitive.
- **Confidence:** 95%

---

### Obsidian Vault Management Cluster (4 files → all ARCHIVE)

Setup-phase documentation for a vault restructuring that's already complete.

#### VAULT-ARCHITECTURE.md → ARCHIVE
- **Lines:** 209
- **Purpose:** Vault folder structure design
- **Why archive:** Describes a restructuring that was implemented. The folder numbers in the file ("50-Standards/") don't even match reality ("60_Resources/Standards/"). It's a historical design document.
- **Confidence:** 92%

#### LINKING-RULES.md → ARCHIVE
- **Lines:** 112
- **Purpose:** 7 rules for when/how to link Obsidian notes
- **Why archive:** Well-researched (6 sources) but the vault is stable now. The 7 rules are good practice but Mia doesn't need a 112-line guide to know "link with context, max 3-5 per file." The rules were needed during restructuring, not as a permanent reference.
- **Confidence:** 85%

#### OBSIDIAN-LINKING-PROTOCOL.md → ARCHIVE
- **Lines:** 72
- **Purpose:** Technical wikilink rules (no paths, backlinks, validation)
- **Why archive:** Created after sub-agent linking failures. The failure patterns are documented; the fix ("use filename only, not path") is now known. Troubleshooting doc, not a standard.
- **Confidence:** 90%

#### OBSIDIAN-VAULT-QA.md → ARCHIVE
- **Lines:** 87
- **Purpose:** Bash validation script for vault health
- **Why archive:** This is a script, not a standard. If needed, it should live in scripts/ or 99-System/. The vault is healthy; this is a maintenance tool, not something Florian opens as a reference.
- **Confidence:** 90%

---

### Voice/Writing Cluster (2 files → both ARCHIVE)

Superseded by workspace BRAND.md (Voice section) + CONTENT-VOICE.md.

#### VOICE-GUIDE.md → ARCHIVE
- **Lines:** 89
- **Purpose:** Anti-LLM writing standard + Florian's real style
- **Why archive:** workspace CONTENT-VOICE.md (30 lines) captures the essential rules: anti-LLM tells, Florian's voice, public content rules. This 89-line version has more detail (specific word-tells, interpunktion-tells, checklist) but it's the source document that was distilled into the workspace version. The distillation is sufficient.
- **Confidence:** 88%

#### VOICE.md → ARCHIVE
- **Lines:** 44
- **Purpose:** How Mia sounds (phrases, tone, formatting)
- **Why archive:** Content is distributed across workspace files. BRAND.md has Voice section. CONTENT-VOICE.md has writing rules. SOUL.md has Mia's personality. The "♔" signature and specific phrases ("Notiert.", "Läuft.") belong in SOUL.md. This file splits voice rules across too many locations.
- **Confidence:** 88%

---

### Brand/CI (1 file → ARCHIVE)

#### Corporate-Identity.md → ARCHIVE
- **Lines:** 115
- **Purpose:** Ainary Ventures CI — fonts, colors, spacing
- **Why archive:** workspace BRAND.md is the active standard. This Obsidian version uses different values (no Indigo, no Geist, different spacing). Keeping both creates ambiguity about which is the source of truth. BRAND.md wins.
- **Confidence:** 95%

---

### Process/Behavioral (2 files → both ARCHIVE)

#### ANTI-SYCOPHANCY.md → ARCHIVE
- **Lines:** 204
- **Purpose:** Counter to track if Mia disagrees enough
- **Why archive:** Counter still at 0 since creation (2026-02-10). Interaction log empty. The pushback examples are good but Mia doesn't need example scripts to disagree — she needs the PRINCIPLE ("push back when warranted"), which is in AGENTS.md. 204 lines for an unused tracking system.
- **Confidence:** 90%

#### SOURCE-REQUIREMENT.md → ARCHIVE
- **Lines:** 269
- **Purpose:** Rules for citing sources in persistent files
- **Why archive:** 269 lines for one rule: "cite your sources or don't write the fact." The principle is already embedded in RESEARCH-PROTOCOL (Admiralty system) and OUTPUT-PREFLIGHT (Rule 5). The examples are useful but the core message doesn't need its own file.
- **Confidence:** 90%

---

### Navigation (1 file → ARCHIVE)

#### Standards-MOC.md → ARCHIVE
- **Lines:** 28
- **Purpose:** Map of Content listing all standards
- **Why archive:** After this audit, the folder has 4 files. A navigation index for 4 files is overhead. If the folder grows past 8 files, recreate it.
- **Confidence:** 90%

---

## The 2 Files to Delete

### Florian.md → DELETE
- **Lines:** 128
- **Purpose:** Predictive model of Florian's preferences
- **Why delete:** Content is near-identical to workspace `standards/FLORIAN.md` (114 lines). The Obsidian version has 14 extra lines: YAML frontmatter + Related section. Zero unique content. True duplicate.
- **Confidence:** 98%

### Research-Protocol.md → DELETE
- **Lines:** 152
- **Purpose:** Pre-research → execution → BLUF protocol
- **Why delete:** Content is near-identical to workspace `standards/RESEARCH-PROTOCOL.md` (141 lines). The Obsidian version has 11 extra lines: YAML frontmatter + Related section. Zero unique content. True duplicate.
- **Confidence:** 98%

---

## Decisions Needed from Florian

### 1. DESIGN-SYSTEM.md vs BRAND.md — Color Conflict
| Element | DESIGN-SYSTEM.md | BRAND.md |
|---------|-----------------|----------|
| Primary accent | Indigo #6366f1 | Gold #c8aa50 |
| Special accent | Gold #c8aa50 | (none) |
| Headline font | Geist | Inter Display |
| Background | #08080c | #0a0a0a |

**Question:** Is the website Indigo+Gold (DESIGN-SYSTEM) or Gold-only (BRAND.md)? Which is the source of truth? Whichever is wrong needs updating.

### 2. Twin.md — Copy to Workspace?
AGENTS.md references TWIN.md but it only exists in Obsidian. Should I copy it to `workspace/standards/TWIN.md`?

---

## Action Plan (When Approved)

```bash
# 1. Create archive folder
mkdir -p "/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/80-Archive/Standards-Archived-2026-02-17/"

# 2. Move 18 files to archive
# (list of mv commands for each file)

# 3. Delete 2 true duplicates
# (or move to archive if Florian prefers safety)

# 4. Result: Standards/ contains only:
#    - 3-Lean-Checklists.md
#    - DESIGN-SYSTEM.md
#    - Mental-Models-Lookup.md
#    - Twin.md
```

---

## Post-Audit Reflection

**What I nearly got wrong (v1 → v2):**

DESIGN-SYSTEM.md was initially marked ARCHIVE. On deeper review, it's the ONLY source of component CSS (cards, buttons, badges, pricing, navigation, inputs). Workspace BRAND.md has colors/fonts but zero component code. WEBSITE-DESIGN-GUIDE.md has copywriting but zero CSS. Archiving DESIGN-SYSTEM.md would mean every HTML build starts from scratch. Changed to KEEP.

The 4 "consolidate" files (Before-Any-Output, DONE-GAP-DETECTOR, Definition-of-Done, Output-Preflight) were initially marked for merging into 3-Lean-Checklists. On reflection, the unique bits from each are 1-4 lines — not worth the effort of merging. The workspace standards already embed quality checks. Changed all 4 to ARCHIVE.

**Pattern I noticed:** 15 of the 24 files were generated from a single "Board of Advisors" AI brainstorming session (Feb 8-10, 2026). That session produced useful thinking but too many artifacts. The thinking is now distilled into the 6 workspace standards. The artifacts can go.

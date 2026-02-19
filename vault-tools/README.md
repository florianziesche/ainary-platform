# Hierarchical Knowledge System — Obsidian Vault Tools

Built: 2026-02-19  
Status: **Deployed & Tested**

## Overview

Three Python scripts that implement a tiered knowledge hierarchy for the Obsidian vault:
- **CORE** (2x boost): Identity, decisions, verified truths
- **KNOWLEDGE** (1.5x boost): Resources, patterns, connections
- **OPERATIONAL** (1x boost): Projects, people, areas
- **EPHEMERAL** (0.5x boost): Daily notes, inbox, triage

## Scripts

### 1. `tag_tiers.py` — Frontmatter Tier Tagger (238 LOC)

Auto-assigns tier and expiry dates based on path rules.

**Usage:**
```bash
python tag_tiers.py              # Dry-run (shows changes)
python tag_tiers.py --apply      # Write changes to files
python tag_tiers.py --path DIR   # Process specific directory
```

**Tier Assignment Rules:**
- `verified-truths.md`, `decisions.md`, `SOUL.md`, `AGENTS.md` → CORE
- `knowledge/*.md`, `60_Resources/**/*.md`, `connections.md` → KNOWLEDGE
- `projects.md`, `people.md`, `20_Areas/**/*.md` → OPERATIONAL
- `daily/*.md`, `00_Inbox/**/*.md`, `triage/*.md` → EPHEMERAL

**Expiry Calculation:**
- CORE: none (permanent)
- KNOWLEDGE: 1 year from file mtime
- OPERATIONAL: 6 months from file mtime
- EPHEMERAL: 90 days from file mtime

**Test Results:**
```
Total files: 664
  - CORE: 4
  - KNOWLEDGE: 150
  - OPERATIONAL: 376
  - EPHEMERAL: 132
Actions:
  - Added frontmatter: 206
  - Updated frontmatter: 456
  - Unchanged: 2
```

### 2. `conflict_resolver.py` — Contradiction Detector (262 LOC)

Detects contradictions across tiered notes using TF-IDF search.

**Usage:**
```bash
python conflict_resolver.py "claim or query"
python conflict_resolver.py --scan              # Scan all CRTs
python conflict_resolver.py "query" --json      # JSON output
```

**Features:**
- TF-IDF similarity search across vault
- Tier-boosted relevance scoring
- Number/claim extraction with context
- Cross-tier conflict detection
- CRT validation against vault

**Test Results:**
```
Query: "ECE calibration"
  - Found 10 related notes
  - No contradictions detected

CRT Scan:
  - Scanned 27 CRTs
  - 6 CRTs with potential conflicts
  - Conflicts: CT-003, CT-008, CT-009, CT-011, CT-014, CT-025
```

### 3. `freshness_enforcer.py` — Expiry & Degradation (264 LOC)

Tracks knowledge freshness and auto-degrades stale notes.

**Usage:**
```bash
python freshness_enforcer.py --report           # Show status (default)
python freshness_enforcer.py --degrade          # Move STALE notes down one tier
python freshness_enforcer.py --status STALE     # Filter by status
python freshness_enforcer.py --json             # JSON output
```

**Status Categories:**
- **FRESH**: More than 30 days until expiry
- **AGING**: Within 30 days of expiry
- **STALE**: Past expiry date

**Tier Degradation:**
CORE → KNOWLEDGE → OPERATIONAL → EPHEMERAL

**Test Results:**
```
Total files scanned: 664
Files with expiry field: 662

Status breakdown:
  - FRESH: 662
    - CORE: 4
    - KNOWLEDGE: 150
    - OPERATIONAL: 376
    - EPHEMERAL: 132
  - AGING: 0
  - STALE: 0

(All files currently FRESH - system just initialized)
```

## Design Constraints

✓ Python 3 stdlib only (no external dependencies)  
✓ Each script < 300 LOC  
✓ Regex-based frontmatter parsing (no PyYAML)  
✓ Handles edge cases: binary files, empty files, malformed YAML  
✓ Dry-run mode by default for safety  

## Integration Points

- **RAG Layer**: `~/.openclaw/workspace/projects/research-pipeline/rag_layer.py`
  - Already implements tier boosting (TIER_BOOST dict)
  - Compatible with these tier assignments

- **CRTs**: `~/.openclaw/workspace/research-base/compounding-research-truths.json`
  - 27 verified truths
  - Conflict scanner validates against vault

- **Vault Structure**: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/`
  - 664 markdown files
  - Organized by tier: 70_Mia (CORE), 60_Resources (KNOWLEDGE), 20_Areas (OPERATIONAL), etc.

## Next Steps

1. **Automate freshness checks**: Run `freshness_enforcer.py` weekly via cron
2. **Monitor conflicts**: Schedule `conflict_resolver.py --scan` monthly
3. **Review AGING notes**: Manual review before they become STALE
4. **Refine tier rules**: Adjust path-based rules as vault structure evolves
5. **Integrate with RAG**: Ensure rag_layer.py reads tier frontmatter

## Example Workflow

```bash
# 1. Tag all vault files with tiers (one-time setup)
cd ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/System_OS/vault-index
python tag_tiers.py --apply

# 2. Check for conflicts in a research claim
python conflict_resolver.py "RLHF improves calibration"

# 3. Weekly: Check freshness and degrade stale notes
python freshness_enforcer.py --report
python freshness_enforcer.py --degrade  # if STALE notes found

# 4. Monthly: Validate CRTs against vault
python conflict_resolver.py --scan --json > crt-conflicts.json
```

## Files Modified

**Frontmatter added/updated in 662 files:**
```yaml
---
tier: CORE | KNOWLEDGE | OPERATIONAL | EPHEMERAL
expires: YYYY-MM-DD | none
---
```

**Key CORE files:**
- `70_Mia/verified-truths.md`
- `70_Mia/decisions.md`
- `70_Mia/MEMORY-INDEX.md`
- `70_Mia/USER.md`

**Sample KNOWLEDGE files:**
- `60_Resources/**/*.md` (129 files)
- `70_Mia/knowledge/*.md` (21 files)
- `connections.md`, `patterns.md`

## Maintenance

- **Add new tier rule**: Edit `TIER_RULES` in `tag_tiers.py`
- **Adjust expiry periods**: Edit `EXPIRY_DELTA` dict
- **Change tier hierarchy**: Update `TIER_RANK` in `conflict_resolver.py`
- **Custom degradation**: Modify `TIER_DEGRADATION` in `freshness_enforcer.py`

All changes are version-controlled in `~/.openclaw/workspace/vault-tools/`.

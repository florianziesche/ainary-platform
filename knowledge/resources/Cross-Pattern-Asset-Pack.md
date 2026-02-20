---
type: note
last_verified: 2026-02-15
status: active
created: 2026-02-11
tags: []
tier: KNOWLEDGE
expires: 2027-02-19
---

# Cross-Pattern Asset Pack

**Erstellt:** 2026-02-11  
**Source:** Cross-Pattern Insights Audit  
**Purpose:** Actionable assets für Consulting, Content, [[VC]] Pitches

---

## ATOMIC NOTES

### AB-crosspattern-NOTE-0001: Agent Teams für Parallele Research

**This answers:** "How can we make investigative research 10x faster without sacrificing quality?"

**Content:**
- [[Claude]] Opus 4.6 introduced Agent Teams (Feb 5, 2026) - multiple agents work in parallel with autonomous coordination
- Perfect for read-heavy, independent subtasks (research, analysis, data gathering)
- Investigative journalism use case: 1 story requires research on multiple entities (people, companies, agencies)
  - Traditional: 1 reporter sequentially researches A, then B, then C (3 weeks)
  - Agent Teams: 3 agents parallel research A, B, C + synthesis (3 days)
  - 10x time compression
- Real-world example: Corruption investigation
  - Agent 1: Company records (Handelsregister, financials, connections)
  - Agent 2: Politicians (side income, committee memberships, voting records)
  - Agent 3: Government agency (permits, contracts, protocols)
  - Synthesis: Cross-reference findings ("Company X owned by brother of Politician Y who sits on Committee Z that approved permit")
- Key limitation: Synthesis is NOT automatic - needs 4th agent or human to connect dots
- Cost consideration: 3x parallel agents = 3x [[API]] costs (but 10x time savings)

**Classification:** DERIVED
- Pattern exists (Agent Teams verified)
- Application to journalism is interpretation, but highly plausible

**Confidence:** HIGH
- Feature is bleeding-edge (< 1 week old)
- Use case is obvious but unoccupied
- Value proposition is clear (time compression)

**Sources:**
- Anthropic [[Claude]] Opus 4.6 documentation (Feb 2026)
- Original novelty check: ZERO results for "agent teams investigative journalism"

**Tags:** #agent-teams #investigative-journalism #parallel-processing #media #freie-presse #research-automation

**Failure Modes:**
- Synthesis challenge (connecting dots across reports)
- Source quality (agents don't verify trustworthiness)
- Cost explosion (weeks-long investigations)
- Skill gap (journalists must learn orchestration)

**When to Use:**
- Initial research phase of investigations (1-2 days)
- When research is parallelizable (independent entities)
- When speed matters (breaking story, deadline pressure)

**When NOT to Use:**
- Deep dives requiring sequential understanding
- Stories with single entity focus
- Budget-constrained projects

---

### AB-crosspattern-NOTE-0002: Browser Use für Legacy System Integration

**This answers:** "How can we integrate legacy systems without APIs or expensive rewrites?"

**Content:**
- Browser Use Framework = [[AI]] agents control browser via screenshots/actions
- Intelligent automation beyond brittle RPA (CAPTCHA bypass, context-aware, adaptive)
- OZG (Onlinezugangsgesetz) use case: German municipalities must digitize citizen services
  - Problem: Legacy Fachverfahren (specialized software) have no APIs
  - Traditional solution: Expensive rewrite or wait for vendor [[API]]
  - Browser Use solution: Agent operates legacy UI as interface layer
- Workflow:
  1. Citizen submits request via OZG portal
  2. Browser Use agent receives request
  3. Agent logs into legacy Fachverfahren
  4. Agent fills forms, submits data (UI-driven)
  5. Agent returns response to citizen
- This is RPA 2.0: [[AI]]-based = resilient to UI changes (unlike traditional RPA)
- Real-world impact: 11,000 German municipalities need OZG compliance (deadline-driven market)

**Classification:** DERIVED
- Technology exists (Browser Use verified)
- Application to OZG is interpretation, addresses real problem

**Confidence:** HIGH
- Novelty verified (ZERO results for "Browser Use OZG")
- Urgent problem (regulatory deadline)
- Concrete customer (Glashütte municipality)

**Sources:**
- Browser Use Framework (open-source)
- OZG regulatory requirements
- Original novelty check confirmed

**Tags:** #browser-use #ozg #government #rpa #legacy-systems #automation #kommunalverwaltung #glashütte

**Failure Modes:**
- UI changes break automation (RPA brittleness)
- Security/credential management risks
- Transaction integrity (partial form fills)
- Regulatory compliance uncertainty
- "Workaround" perception (not real solution)

**When to Use:**
- Legacy systems with no [[API]] roadmap
- Regulatory deadlines (OZG)
- Bridge solution until proper [[API]] available
- Low-volume transactions (automation overhead acceptable)

**When NOT to Use:**
- High-volume critical transactions
- Systems with [[API]] alternatives
- Highly dynamic UIs
- Security-critical processes without proper controls

---

### AB-crosspattern-NOTE-0003: Workflow Memory für Repetitive Engineering

**This answers:** "How can systems learn from past work to accelerate repetitive tasks?"

**Content:**
- Workflow Memory (Wang et al. Sept 2024): Agents learn reusable workflows from completed tasks
- When similar task appears → workflow is retrieved, adapted, reused
- Result: Faster execution, higher consistency
- CNC manufacturing use case: Part quoting/calculation is highly repetitive
  - First time: Agent quotes turned part (select material → choose machine → plan operations → calculate time/cost)
  - Workflow saved as "Turned-Part-Standard-Workflow"
  - Next turned part: Agent starts with saved workflow, adapts (different diameter, tolerance)
  - After 100 quotes: Agent has library of workflows (turned parts, milled parts, sheet metal, etc.)
- Value proposition:
  - Speed: Quote in 2 minutes instead of 2 hours
  - Consistency: Same approach for similar parts
  - Learning curve: System gets better over time
- Key insight: CAM software doesn't "remember" - every calculation from scratch
- Workflow Memory changes this: System accumulates procedural knowledge

**Classification:** DERIVED
- Pattern exists (Workflow Memory paper verified: Sept 2024)
- Application to manufacturing is interpretation

**Confidence:** HIGH
- Cutting-edge research (paper from Sept 2024)
- Novelty verified (ZERO results for "workflow memory manufacturing CNC")
- Clear value proposition (time + consistency)

**Sources:**
- Workflow Memory paper (Wang et al. Sept 2024)
- Original novelty check confirmed

**Tags:** #workflow-memory #cnc #manufacturing #engineering #calculation #cam-software #procedural-learning

**Failure Modes:**
- Workflow variability (every part is different)
- Domain knowledge gap (agent doesn't understand physics)
- ERP integration complexity
- Change management (engineers trust experience over [[AI]])
- ROI delay (needs 50-100 training samples)

**When to Use:**
- Repetitive engineering tasks with patterns
- After accumulating training data (50+ samples)
- Where speed + consistency matter
- Industries with high quote volume

**When NOT to Use:**
- Highly custom/unique projects
- Safety-critical calculations without verification
- Before proper domain constraints are implemented
- Without ERP integration plan

---

### AB-crosspattern-NOTE-0004: Hierarchical Memory für Institutional Knowledge

**This answers:** "How can organizations retain and leverage institutional knowledge over time?"

**Content:**
- MemGPT + Generative Agents architecture: Hierarchical memory with reasoning layers
  - Observations: Raw inputs captured
  - Reflections: Patterns recognized, insights generated
  - Planning: Actions/questions suggested based on memory
- Beat reporting use case: Journalists cover specific areas (politics, business, local)
  - Current state: Chaos (notes scattered, archive fragmented, knowledge in reporter's head)
  - When reporter leaves → institutional knowledge lost
- Hierarchical memory system for reporters:
  - **Observations layer:** Every story, interview, source, event captured
  - **Reflections layer:** System recognizes patterns ("This politician appears frequently in construction projects", "This company wins unusual number of public contracts")
  - **Planning layer:** Suggests follow-up stories, interview questions, archive searches
- Value proposition:
  - Better stories (connections human might miss)
  - Faster research (instant recall vs. manual archive search)
  - Institutional continuity (knowledge persists when reporters change)
- Differentiation: Generic [[AI]] archives exist (CJR, IBM), but NO systems with reflection/planning layers from agent research

**Classification:** DERIVED
- Pattern exists (MemGPT arXiv 2310.08560, Generative Agents Stanford 2023)
- Application to journalism is interpretation, never tested

**Confidence:** MEDIUM-HIGH
- Papers verified, pattern is correct
- Novelty confirmed (reflection/planning layer not applied to journalism)
- BUT: Significant execution risks (data quality, hallucination, adoption)

**Sources:**
- MemGPT paper (arXiv 2310.08560)
- Generative Agents paper (Stanford 2023)
- CJR [[AI]] archive articles (for comparison)

**Tags:** #hierarchical-memory #journalism #beat-reporting #institutional-knowledge #memgpt #generative-agents #media

**Failure Modes:**
- Data quality (reporter notes are messy)
- Reflection hallucination (false pattern recognition)
- Planning irrelevance (suggestions don't match editorial priorities)
- Institutional resistance (reporters trust own memory)
- Cost/latency (real-time reflection is expensive)

**When to Use:**
- Established beats with archive history
- After data cleanup/structuring
- With human-in-the-loop for reflections
- Where institutional memory loss is painful

**When NOT to Use:**
- Breaking news (no time for reflection)
- New beats (no historical data)
- Without budget for proper implementation
- Where reporter turnover is low

---

### AB-crosspattern-NOTE-0005: Computer Use für Legacy Data Migration

**This answers:** "How can we extract value from legacy systems without APIs?"

**Content:**
- [[Claude]] Computer Use: Agent operates UI via screenshots/actions
- Works even when no [[API]] exists (legacy systems, outdated software)
- Media archive monetization use case:
  - Problem: Millions of archive articles in legacy CMS (1990s systems, no [[API]])
  - Traditional solution: Manual migration (impossible scale) or leave dormant
  - Computer Use solution: Agent operates legacy UI to extract content
- Workflow:
  1. Agent logs into old CMS
  2. Searches/browses articles
  3. Extracts content (handles OCR for scanned documents)
  4. Cleans/formats for modern system
  5. Imports into new CMS
  6. Enables monetization (premium content, research access)
- Key advantage: No [[API]] required, no vendor cooperation needed
- Real-world challenge: Archive articles from 1990s have monetization unclear (who buys old local news?)

**Classification:** DERIVED
- Technology exists ([[Claude]] Computer Use verified)
- Application to archive migration is interpretation

**Confidence:** MEDIUM-HIGH
- Novelty verified (Computer Use for media archives not found)
- Technical feasibility likely (Computer Use can handle legacy UIs)
- BUT: Market risk (monetization unclear) + UI complexity risk

**Sources:**
- [[Claude]] Computer Use documentation (Anthropic)
- Original novelty check confirmed

**Tags:** #computer-use #legacy-systems #archive #media #migration #monetization #cms

**Failure Modes:**
- Legacy UI complexity (Flash, Java applets unsupported)
- Data quality (OCR errors, bad formatting)
- Cost/speed (millions of articles = months + high [[API]] costs)
- Legal/copyright issues (old content rights unclear)
- Market validation missing (who pays for old content?)

**When to Use:**
- After market validation (confirm someone will pay)
- For high-value archive content
- As pilot (top articles first, not full archive)
- With budget for cleanup/QA

**When NOT to Use:**
- Without market validation
- For low-value content
- Systems that Computer Use can't handle (Flash, etc.)
- Before legal/copyright review

---

### AB-crosspattern-NOTE-0006: Reflexion für Autonomous Quality Control

**This answers:** "How can [[AI]] systems improve their own output quality without human feedback?"

**Content:**
- Reflexion + Self-Refine pattern: Generate → Self-Critique → Refine → Repeat
- Agent produces output, critiques itself based on criteria, generates improved version
- Autonomous quality improvement loop
- Coding agent use case:
  - Traditional code generator: Produces code, if wrong → human must debug
  - Reflexion agent: Produces code → tests → self-critiques ("failed because edge case not handled") → generates new code → tests again
  - Built-in QA layer
- Value proposition for "Coding Agents replace Co-Founders" pitch:
  - Co-Founder writes code + makes mistakes → Founder must review/debug (overhead)
  - Reflexion Agent writes code + self-corrects → Much lower founder overhead
  - This is THE differentiator between "dumb code generator" and "intelligent coding partner"
- Limitation: Self-critique catches obvious errors (test failures), not architecture/security/performance issues
- Better framing: "Coding Agents reduce Co-Founder need" (not "replace")

**Classification:** INTERPRETATION
- Pattern exists (Reflexion NeurIPS 2023, Self-Refine NeurIPS 2023)
- Connection to "why coding agents > co-founders" is argumentative, not research

**Confidence:** HIGH (as framing)
- Papers verified
- Logic is sound (self-QA is real advantage)
- Good pitch angle for [[VC]] (Keynostic)
- BUT: Not a research insight, just reframing existing tech

**Sources:**
- Reflexion paper (NeurIPS 2023)
- Self-Refine paper (NeurIPS 2023)

**Tags:** #reflexion #self-refine #coding-agents #quality-control #autonomous-improvement #vc-pitch #keynostic

**Failure Modes:**
- Self-critique misses non-obvious issues
- Over-claiming "replace co-founder" (co-founder does more than code)
- [[VC]] skepticism (agents are hype)

**When to Use:**
- In [[VC]] pitch (Keynostic) to explain why coding agents work
- Internal communication (not public article - too polarizing)
- Positioning coding agent products

**When NOT to Use:**
- Public content (would generate backlash)
- When speaking to engineers (they know limitations)
- Over-simplified "[[AI]] replaces humans" narrative

---

## PLAYBOOKS

### PLAYBOOK #1: Agent Teams Investigative Research Pilot

**Trigger:** Media organization wants to accelerate investigative research without adding headcount

**Goal:** Compress 3-week sequential research into 3-day parallel research using Agent Teams

**Inputs:**
- Investigative story topic (e.g., "Corruption in public construction contracts")
- List of entities to research (people, companies, agencies)
- Access to research tools (web search, databases, public records)
- Budget for [[API]] costs (estimate: 3x normal for parallel agents)

**Steps:**

1. **Story Decomposition (1 hour)**
   - Break story into independent research streams
   - Example: Stream A = Companies, Stream B = Politicians, Stream C = Government agencies
   - Define research questions for each stream
   - Ensure streams are truly independent (no dependencies)

2. **Agent Team Setup (2 hours)**
   - Configure 3 agents (one per stream)
   - Define research scope for each:
     - Agent A: "Research companies involved: ownership, financials, public contracts, connections"
     - Agent B: "Research politicians mentioned: committee memberships, voting records, side income, family ties"
     - Agent C: "Research government agency: permits issued, contract awards, protocol records"
   - Set constraints (time limit, source types, output format)
   - Configure [[API]] rate limits/budgets

3. **Parallel Execution (1-2 days)**
   - Launch all 3 agents simultaneously
   - Monitor progress (check intermediate outputs)
   - Intervene if agent goes off-track
   - Agents work independently, produce separate reports

4. **Synthesis Phase (1 day)**
   - Option A: 4th Agent for automated synthesis
     - Prompt: "Cross-reference findings from Agent A, B, C. Identify connections, contradictions, patterns."
   - Option B: Human synthesis (recommended for first pilots)
     - Journalist reads all 3 reports
     - Manually connects dots
     - Validates findings
   - Output: Integrated research brief with cross-references

5. **Verification (Human, always required)**
   - Check source quality (agents provide links, human verifies trustworthiness)
   - Validate key claims (especially connections between entities)
   - Flag unverified information for deeper investigation
   - Ensure no hallucination (agents sometimes "connect" things that aren't connected)

6. **Story Development (Normal journalism process)**
   - Use research brief as foundation
   - Conduct interviews, gather documents
   - Write story with verified facts

**Outputs:**
- 3 independent research reports (one per agent)
- 1 integrated synthesis brief
- List of verified facts vs. unverified leads
- Time saved metric (compare to traditional sequential research)

**Failure Modes + Mitigations:**

| Failure Mode | Mitigation |
|--------------|------------|
| Synthesis misses connections | Human synthesis for first 3 pilots, then evaluate automated |
| Agents cite low-quality sources | Constrain agents to specific source types (official records, reputable media) |
| Cost explosion (long investigations) | Set budget cap, use Agent Teams only for initial research (1-2 days) |
| Journalist skill gap (can't orchestrate) | Provide templates, conduct 1-day training |
| Output quality varies by agent | Standardize output format, review prompts iteratively |

**Acceptance Criteria:**
- Research completed in ≤3 days (vs. 3 weeks baseline)
- ≥80% of findings are verified as accurate
- Cost ≤ 5x normal research cost (acceptable for 7x time savings)
- Journalist satisfaction ≥7/10 ("would use again")

**Success Metrics:**
- Time compression ratio (baseline / agent team time)
- Accuracy rate (verified findings / total findings)
- Cost per investigation
- Stories published from agent-assisted research

**Timeline:** 4-week pilot
- Week 1: Setup + training
- Week 2-3: Execute 2 investigations with Agent Teams
- Week 4: Evaluation + decision (continue/expand/stop)

**Who This Is For:**
- Freie Presse (concrete pitch)
- Investigative journalism teams at media organizations
- Newsrooms with research capacity constraints

---

### PLAYBOOK #2: Browser Use OZG Integration Pilot

**Trigger:** German municipality needs OZG compliance but has legacy Fachverfahren without APIs

**Goal:** Enable citizen self-service via OZG portal without migrating/rewriting legacy systems

**Inputs:**
- 1 legacy Fachverfahren (specialized software) to integrate
- OZG portal with citizen-facing forms
- Service-account credentials for legacy system
- Compliance/security requirements documentation

**Steps:**

1. **System Assessment (1 week)**
   - Audit legacy Fachverfahren:
     - Is UI accessible via browser? (or desktop-only?)
     - Authentication method? (login, certificates, etc.)
     - Form complexity? (simple fields or complex workflows?)
     - Does it use unsupported tech? (Flash, Java applets)
   - Decision: GO/NO-GO for Browser Use approach
   - Document UI workflows (screenshots, field mappings)

2. **Proof-of-Concept (1 week)**
   - Build minimal Browser Use agent
   - Test ONE workflow (simplest use case)
   - Example: "Citizen requests Gewerbeanmeldung → Agent fills legacy Gewerbe-System"
   - Validate: Agent can login, fill form, submit, extract confirmation
   - Measure: Success rate, error types, latency

3. **Security/Compliance Review (1 week, parallel with PoC)**
   - Credential management strategy (where/how stored?)
   - DSGVO compliance check (data flows, logging)
   - [[AI]] Act compliance (if applicable)
   - Transaction logging for audit trail
   - Fallback procedures (what if agent fails mid-transaction?)
   - Decision: APPROVED/BLOCKED/CONDITIONS

4. **Production Build (2 weeks, if approved)**
   - Robust error handling (retry logic, human escalation)
   - Transaction wrapper (rollback if partial completion)
   - Monitoring dashboard (success rate, latencies, errors)
   - Alerting (when agent fails repeatedly)
   - Credential vault integration
   - Logging/audit trail

5. **Testing (1 week)**
   - Test all workflows (happy path + edge cases)
   - Simulate UI changes (does agent adapt?)
   - Load testing (can it handle peak volume?)
   - Security testing (credential leakage, injection attacks)
   - Acceptance testing with end-users (Sachbearbeiter)

6. **Deployment (1 week)**
   - Soft launch (limited user group)
   - Monitor closely (daily check-ins)
   - Collect feedback (users, Sachbearbeiter)
   - Tune prompts/logic based on real usage
   - Full launch after 2 weeks stable operation

**Outputs:**
- Browser Use agent integrated with 1 Fachverfahren
- Citizen self-service via OZG portal
- Monitoring dashboard
- Documentation (for scaling to more Fachverfahren)

**Failure Modes + Mitigations:**

| Failure Mode | Mitigation |
|--------------|------------|
| UI changes break agent | Monitoring + alerts, rapid fix process, maintain UI screenshots for version control |
| Credential security breach | Use dedicated service-account, credential vault, rotate regularly, audit access |
| Transaction integrity failure | Transaction wrapper with rollback, confirmation checks, human review queue |
| Regulatory non-compliance | Legal review BEFORE build, document compliance measures, audit trail |
| Agent is "workaround" perception | Frame as "bridge solution until [[API]] available", set expectations |

**Acceptance Criteria:**
- ≥80% automation rate (20% may need human intervention)
- <5% error rate (errors = failed transactions)
- <2 minute latency per transaction
- DSGVO/Security compliance confirmed
- Sachbearbeiter satisfaction ≥7/10

**Success Metrics:**
- Automation rate (automated transactions / total transactions)
- Error rate
- Time saved (vs. manual Sachbearbeiter processing)
- Citizen satisfaction (survey after using OZG portal)

**Timeline:** 6-week pilot
- Week 1: Assessment
- Week 2: PoC + Security Review
- Week 3-4: Production Build
- Week 5: Testing
- Week 6: Deployment + Evaluation

**Who This Is For:**
- Glashütte municipality (concrete pitch)
- German municipalities with OZG compliance deadline
- Government agencies with legacy system integration needs

---

### PLAYBOOK #3: Workflow Memory CNC Calculation System

**Trigger:** Manufacturing company wants faster, more consistent part quoting/calculation

**Goal:** Build [[AI]] system that learns from past calculations to accelerate future quotes

**Inputs:**
- Historical calculation data (50-100 past quotes minimum)
  - Part specs (geometry, material, tolerances)
  - Machine selected
  - Operations planned
  - Time/cost calculated
  - Actual results (if available)
- Access to current systems:
  - CAD/CAM software
  - ERP (machine database, material prices)
  - Knowledge base (machining parameters, tool catalogs)

**Steps:**

1. **Data Audit (1 week)**
   - Review historical calculations
   - Assess data quality:
     - Are specs structured? (or free text?)
     - Are workflows documented? (or just final numbers?)
     - Are results tracked? (did quotes match actual?)
   - Identify patterns (do similar parts follow similar workflows?)
   - Decision: Sufficient data? (if <50 quality samples → delay until more data)

2. **Workflow Taxonomy (1 week)**
   - Categorize part types (turned parts, milled parts, sheet metal, etc.)
   - Define workflow templates for each category
   - Example Turned Part Workflow:
     - Step 1: Select material (based on spec requirements)
     - Step 2: Select machine (based on size, tolerance)
     - Step 3: Plan operations (facing, turning, threading, etc.)
     - Step 4: Calculate time (based on material, machine, operations)
     - Step 5: Calculate cost (time × rate + material + setup)
   - Document decision rules (when to deviate from template)

3. **Prototype Build (2 weeks)**
   - Build simple workflow memory system
   - Start with ONE part category (e.g., turned parts)
   - Train on historical data (50+ samples)
   - Implement:
     - Workflow retrieval (find similar past part)
     - Workflow adaptation (adjust for differences)
     - Workflow execution (generate quote)
   - Test on holdout set (10 parts not in training data)
   - Measure accuracy (quote vs. actual, if data available)

4. **Domain Constraints (1 week, parallel with prototype)**
   - Encode machining rules (physics-based constraints)
   - Examples:
     - Material X requires cutting speed Y
     - Machine A cannot handle tolerance <0.01mm
     - Tool B has max depth of cut Z
   - Integrate with workflow system (prevent impossible workflows)
   - Review with machinist/engineer (validate rules)

5. **ERP Integration (2 weeks)**
   - Connect to machine database (availability, capabilities, hourly rates)
   - Connect to material pricing (real-time or periodic updates)
   - Connect to CAD/CAM (if possible, for geometry understanding)
   - Build interface for engineer:
     - Input: Part specs (upload CAD or manual entry)
     - Output: Recommended workflow + quote
     - Override: Engineer can modify workflow if needed

6. **Pilot Testing (4 weeks)**
   - Deploy to 2-3 engineers (early adopters)
   - Use for real quotes (compare to manual calculations)
   - Collect feedback:
     - Accuracy? (quote vs. manual)
     - Speed? (time saved)
     - Usability? (UI, workflow suggestions)
     - Trust? (do engineers accept recommendations?)
   - Iterate on workflows based on feedback
   - Track metrics (see below)

7. **Expansion (if pilot successful)**
   - Add more part categories (milled, sheet metal, etc.)
   - Train more engineers
   - Integrate with quoting process (formal approval workflow)
   - Expand to other departments (sales can generate rough quotes)

**Outputs:**
- Workflow Memory system for part quoting
- Library of learned workflows (grows over time)
- Faster quoting (2 min vs. 2 hours)
- More consistent quotes (same approach for similar parts)

**Failure Modes + Mitigations:**

| Failure Mode | Mitigation |
|--------------|------------|
| Workflow variability too high | Start with most standardized part category, expand gradually |
| Agent suggests impossible workflows | Domain constraints (physics-based rules), engineer override always available |
| ERP integration too complex | Start standalone, integrate incrementally |
| Engineers don't trust [[AI]] | Position as assistant (not replacement), show accuracy data, allow overrides |
| ROI delayed (needs training data) | Set expectations (6-12 months to full value), show incremental improvements |

**Acceptance Criteria:**
- Quote accuracy ≥90% (within 10% of actual cost, if tracked)
- Time savings ≥50% (2 min vs. 2 hours)
- Engineer adoption ≥70% (using for majority of quotes)
- System learns (workflow library grows, accuracy improves over time)

**Success Metrics:**
- Quotes generated (manual vs. [[AI]]-assisted)
- Time per quote (before vs. after)
- Quote accuracy (predicted vs. actual)
- Engineer satisfaction (survey)
- Workflow library size (number of learned patterns)

**Timeline:** 12-week pilot
- Week 1: Data Audit
- Week 2: Workflow Taxonomy
- Week 3-4: Prototype Build + Domain Constraints
- Week 5-6: ERP Integration
- Week 7-10: Pilot Testing
- Week 11-12: Evaluation + Expansion Decision

**Who This Is For:**
- Manufacturing companies with high quote volume
- CNC shops, job shops, contract manufacturers
- ERP vendors (as product feature)

---

## TEMPLATES

### TEMPLATE #1: Cross-Pattern Consulting Pitch

**Title:** [Pattern Name] for [Industry/Company]

---

#### 1. THE PROBLEM (1 slide)

**Current State:**
- [Company/Industry] faces [specific problem]
- Example: "Media organizations lose institutional knowledge when reporters leave"
- Impact: [quantify pain - time, money, quality]

**Why Now:**
- [Trigger: regulatory deadline, competitive pressure, technology maturity]
- Example: "OZG compliance deadline, legacy systems without APIs"

**Why Traditional Solutions Fail:**
- [Expensive, slow, incomplete, not adopted]
- Example: "Rewriting legacy systems costs millions, takes years"

---

#### 2. THE INSIGHT (1 slide)

**Pattern from [[AI]] Research:**
- [Name + 1-sentence description]
- Example: "Hierarchical Memory (MemGPT): Observations → Reflections → Planning"

**Cross-Domain Application:**
- [[AI]] Research developed this for [original use case]
- We apply it to [your industry]
- **Nobody else has done this**

**Why This Works:**
- [Explain pattern-to-problem fit]
- Example: "Beat reporting IS a memory problem - capture, recognize patterns, suggest actions"

---

#### 3. THE SOLUTION (2 slides)

**How It Works:**
- [Simple diagram or workflow]
- [3-5 key steps]
- Example Agent Teams workflow: Story → Decompose → Parallel Research → Synthesis

**What You Get:**
- [Concrete outcomes, quantified]
- Example: "3-day investigations instead of 3 weeks = 7x faster"
- [Secondary benefits]
- Example: "Institutional knowledge retained when reporters change"

**Differentiation:**
- Vs. [Alternative A]: [Why better]
- Vs. [Alternative B]: [Why better]
- Example: "Vs. generic [[AI]] archive: We have reflection/planning layers, not just search"

---

#### 4. PROOF POINTS (1 slide)

**Research Validation:**
- [Paper citations, verified sources]
- Example: "MemGPT (arXiv 2310.08560), Generative Agents (Stanford 2023)"

**Novelty Confirmed:**
- [Web search results showing nobody else doing this]
- Example: "ZERO results for 'hierarchical memory journalism'"

**Similar Successes:**
- [Adjacent use cases where pattern worked]
- Example: "Workflow Memory used in [other domain], showed [results]"

---

#### 5. PILOT PROPOSAL (2 slides)

**Approach:**
- [6-12 week pilot]
- [Specific scope: 1 use case, 2-3 users, defined deliverable]
- Example: "6-week OZG pilot: Integrate 1 Fachverfahren, 80% automation target"

**Timeline:**
- Week 1-2: [Setup]
- Week 3-6: [Build/Test]
- Week 7-8: [Deploy/Evaluate]

**Investment:**
- [Consulting fees or build costs]
- [[[API]]/infrastructure costs]
- [Time commitment from client]

**Success Metrics:**
- [3-5 measurable outcomes]
- Example: "≥80% automation rate, <5% error rate, ≥7/10 user satisfaction"

**Decision Point:**
- After pilot: GO/NO-GO for production rollout
- If GO: [Expansion plan]
- If NO-GO: [No further commitment]

---

#### 6. WHY US (1 slide)

**Domain Expertise:**
- [Your background in industry]
- Example: "Worked with Freie Presse on [project], understand media workflows"

**Technical Depth:**
- [Your [[AI]]/research credentials]
- Example: "Deep knowledge of agent architectures from [[AI]] research"

**Track Record:**
- [Past successes, if any]
- If none: "Bringing cutting-edge research to real-world problems"

---

### TEMPLATE #2: Cross-Pattern Article (Substack/Blog)

**Title Format:** "How [[[AI]] Pattern] Could Transform [Industry]"

**Subtitle:** [One-line value prop]

---

#### OPENING HOOK (2-3 paragraphs)

**Start with the pain:**
- [Concrete story or scenario showing the problem]
- Example: "When veteran crime reporter Sarah retired, the newsroom lost 20 years of source relationships and investigative leads. There was no system to capture her knowledge."

**Introduce the surprising connection:**
- "Meanwhile, in [[AI]] research labs, scientists solved a similar problem for game-playing agents."
- [Hook: "What if we applied their solution to journalism?"]

---

#### THE PATTERN EXPLAINED (3-4 paragraphs)

**What is [Pattern Name]:**
- [Explain in plain language, no jargon]
- Example: "MemGPT gives [[AI]] agents a 'second brain' - they store observations, recognize patterns, and plan future actions."

**Where it came from:**
- [Research context, but accessible]
- Example: "Developed at Berkeley/Stanford for [[AI]] agents that need long-term memory"

**How it works:**
- [Simple breakdown, maybe use analogy]
- Example: "Think of it like a reporter's notebook (observations) + editorial meeting (reflections) + assignment desk (planning)"

---

#### THE CROSS-DOMAIN APPLICATION (4-5 paragraphs)

**The connection:**
- [Why pattern fits your industry problem]
- Example: "Beat reporting is fundamentally a memory problem..."

**How it would work in practice:**
- [Concrete workflow, specific example]
- Use STORY format: Before/After
- Example:
  - **Before:** Reporter manually searches archive for 2 hours, finds 3 relevant past stories, might miss connections
  - **After:** System instantly recalls all related stories + reflections ("This company appeared in 5 scandals") + suggests follow-ups

**What makes this different:**
- [Vs. existing solutions in your industry]
- Example: "This isn't just better search - it's the reflection and planning layers that make it powerful"

---

#### REALITY CHECK (2-3 paragraphs)

**Challenges + limitations:**
- [Be honest about failure modes]
- Example: "Yes, [[AI]] could hallucinate patterns that don't exist. That's why human verification is essential."

**Why it's still worth it:**
- [Even with limitations, value prop holds]
- Example: "Even with human oversight, this is 10x faster than manual research"

**What needs to happen:**
- [Conditions for success]
- Example: "Organizations need to invest in data cleanup and change management, not just tech"

---

#### IMPLICATIONS (2-3 paragraphs)

**If this works:**
- [Broader impact on industry]
- Example: "Investigative journalism could scale - one reporter could tackle stories that used to require teams"

**Who benefits:**
- [Stakeholders]
- Example: "Small newsrooms could compete with large metros, underserved communities get better coverage"

**What comes next:**
- [Related patterns, future possibilities]
- Example: "This is just memory - combine with Agent Teams for parallel research, and you have a new investigative workflow"

---

#### CLOSING (1-2 paragraphs)

**Call to action:**
- For practitioners: "If you work in [industry], consider how [pattern] could apply to your specific workflow"
- For builders: "This is an open opportunity - nobody's built this yet"
- For investors: "The cross-domain pattern matching approach reveals underserved markets"

**Final thought:**
- [Zoom out, bigger picture]
- Example: "[[AI]] research moves fast. The patterns emerging today will reshape industries tomorrow - but only if we bridge the gap between research and real-world problems."

---

#### OPTIONAL: REFERENCES SECTION

- List papers cited (with links)
- List companies/projects mentioned
- Disclaimer: "This article explores potential applications, not proven solutions. Implementation requires careful pilot testing."

---

## ASSET PACK COMPLETE

**Summary:**
- **6 Atomic Notes** created (Top validated insights)
- **3 Playbooks** created (Top 3 insights: Agent Teams, Browser Use, Workflow Memory)
- **2 Templates** created (Consulting Pitch + Article)

**Next Steps:**
1. Use Template #2 to write article on Insight #7 (Agent Teams) - PUBLISH THIS WEEK
2. Use Template #1 to create pitch deck for Freie Presse (Agent Teams Pilot)
3. Use Template #1 to create pitch deck for Glashütte (Browser Use OZG Pilot)
4. Build simple prototype for Insight #2 (Workflow Memory CNC) - 2-4 weeks

**High-Confidence Assets (Ready to Use):**
- AB-crosspattern-NOTE-0001 (Agent Teams) ✅
- AB-crosspattern-NOTE-0002 (Browser Use OZG) ✅
- AB-crosspattern-NOTE-0003 (Workflow Memory CNC) ✅
- Playbook #1 (Agent Teams) ✅
- Playbook #2 (Browser Use OZG) ✅
- Playbook #3 (Workflow Memory) ✅

**Medium-Confidence Assets (Use with Caveats):**
- AB-crosspattern-NOTE-0004 (Hierarchical Memory) - Thought leadership, not pitch
- AB-crosspattern-NOTE-0005 (Computer Use Archive) - Validate market first
- AB-crosspattern-NOTE-0006 (Reflexion Coding) - Internal pitch only

---

*End of Asset Pack*

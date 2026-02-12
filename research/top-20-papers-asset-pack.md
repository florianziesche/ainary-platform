# Top 20 AI Agent Papers — ASSET PACK

**Created:** 2026-02-11  
**For:** OpenClaw/Mia — Compound Machine  
**Purpose:** Reusable knowledge assets from research audit

---

## 📦 CONTENTS

1. [Atomic Notes](#atomic-notes) — Top 10 Papers distilled
2. [Playbooks](#playbooks) — 3 reusable processes
3. [Templates](#templates) — 2 reusable structures

---

# ATOMIC NOTES

## Top 10 Papers — Kernkonzepte & Nutzung

---

### AB-papers-NOTE-0001: ReAct Pattern

**ID:** AB-papers-NOTE-0001  
**Created:** 2026-02-11  
**Classification:** Evidenced (Paper existiert, weit reproduziert)  
**Confidence:** 95%  
**Sources:** ArXiv 2210.03629, AutoGPT/LangChain Implementations

**This answers:** "Was ist ReAct und wie nutzen wir es in OpenClaw/Mia?"

**Core Concept:**
ReAct = **Reasoning + Acting** in interleaved Pattern:
1. **Thought:** Agent denkt laut ("I need to search for...")
2. **Action:** Agent führt Tool-Call aus (z.B. `search[query]`)
3. **Observation:** Agent sieht Ergebnis
4. **Repeat:** Bis Task erledigt ist

**Why it matters:**
- Befreit Agents aus reinem Text-Modus → können in Umgebungen handeln
- Fundament für moderne Agent-Frameworks (AutoGPT, LangChain, alle nutzen ReAct)
- Einfach zu implementieren (nur Prompt-Engineering)

**How we use it:**
```python
# Pseudo-Code für ReAct-Loop in Mia
while not task_complete:
    thought = llm.generate_thought(context)  # "I should check the calendar"
    action = llm.select_action(thought)      # "calendar.get_events(today)"
    observation = execute_action(action)     # [Meeting at 3pm...]
    context.add(thought, action, observation)
    if is_goal_reached(context):
        break
```

**Known Limitations:**
- Kann in Loops stecken bleiben → Max-Iteration-Limit setzen (z.B. 10)
- Bei schlechten Tools: Garbage-In/Garbage-Out
- Keine Memory-Persistenz → kombinieren mit MemGPT

**Related Notes:**
- AB-papers-NOTE-0002 (MemGPT — für Memory)
- AB-papers-NOTE-0003 (Reflexion — für Self-Improvement)

**Tags:** #architecture #core #foundational #mvp

---

### AB-papers-NOTE-0002: MemGPT Memory System

**ID:** AB-papers-NOTE-0002  
**Created:** 2026-02-11  
**Classification:** Evidenced (Paper + Open-Source Implementation)  
**Confidence:** 90%  
**Sources:** ArXiv 2310.08560, MemGPT GitHub

**This answers:** "Wie managed Mia Memory über Context-Window hinaus?"

**Core Concept:**
MemGPT behandelt Context-Window wie **Virtual Memory in einem OS**:
- **Main Context** = RAM (aktiver Kontext, z.B. 8k tokens)
- **External Storage** = Disk (persistentes Memory, unbegrenzt)
- **Paging** = Agent entscheidet, wann Daten rein/raus

**Memory Hierarchy:**
```
┌─────────────────────┐
│  Main Context (RAM) │  ← Aktuelle Konversation
├─────────────────────┤
│ Short-Term Storage  │  ← Recent Sessions
├─────────────────────┤
│ Long-Term Storage   │  ← Fakten, Präferenzen, Lessons
└─────────────────────┘
```

**Why it matters:**
- Löst Context-Window-Problem → unbegrenzte Konversationen
- Agent kann sich an alte Projekte/Präferenzen erinnern
- Selbst-managed (Agent entscheidet, was wichtig ist)

**How we use it:**
```python
# Für Mia: Memory-Schichten
class MiaMemory:
    main_context: list[Message]      # Letzte N Messages (im Context)
    short_term: VectorDB              # Embeddings der letzten Sessions
    long_term: KnowledgeGraph         # Fakten, Präferenzen, Lessons
    
    def page_in(self, query):
        # Wenn Main Context voll → relevante Memories aus Storage holen
        relevant = self.short_term.search(query)
        self.main_context.add(relevant)
    
    def page_out(self, threshold=0.5):
        # Wenn Main Context voll → unwichtige Memories raus
        for msg in self.main_context:
            if importance(msg) < threshold:
                self.short_term.store(msg)
                self.main_context.remove(msg)
```

**Known Limitations:**
- Paging-Decisions können suboptimal sein (Agent schätzt Wichtigkeit falsch)
- Braucht gute Prompts für Memory-Management
- Storage-Retrieval muss schnell sein (sonst Latenz)

**Related Notes:**
- AB-papers-NOTE-0004 (RAG — für Dokument-Retrieval)
- AB-papers-NOTE-0001 (ReAct — für Action-Loop)

**Tags:** #memory #architecture #mvp #critical

---

### AB-papers-NOTE-0003: Reflexion Self-Improvement

**ID:** AB-papers-NOTE-0003  
**Created:** 2026-02-11  
**Classification:** Evidenced (Paper + Reproduced Results)  
**Confidence:** 90%  
**Sources:** ArXiv 2303.11366

**This answers:** "Wie lernt Mia aus Fehlern?"

**Core Concept:**
Reflexion = **Verbales Reinforcement Learning**:
1. **Execute:** Agent führt Task aus
2. **Get Feedback:** Test failed / Error message / User feedback
3. **Reflect:** Agent analysiert, was schief ging ("I should try X instead of Y")
4. **Retry:** Agent versucht es erneut mit neuem Ansatz
5. **Store Reflection:** Episodisches Memory speichert Learnings

**Why it matters:**
- Agents lernen aus Fehlern **ohne menschliches Feedback**
- Self-Critique → kontinuierliche Verbesserung
- Funktioniert bei Code, Writing, Reasoning

**How we use it:**
```python
# Reflexion-Loop für Mia
def solve_task_with_reflexion(task, max_attempts=3):
    reflections = []
    for attempt in range(max_attempts):
        solution = agent.generate_solution(task, reflections)
        feedback = evaluate(solution, task)
        
        if feedback.success:
            return solution
        
        # Reflect on failure
        reflection = agent.reflect(
            task=task,
            attempt=solution,
            feedback=feedback,
            previous_reflections=reflections
        )
        reflections.append(reflection)
    
    return None  # Failed after max attempts
```

**Example:**
```
Task: Fix bug in Python function
Attempt 1: Changed variable name → Test failed
Reflection: "Changing the variable name doesn't address the logic error. 
             I should look at the conditional statement instead."
Attempt 2: Fixed conditional → Test passed ✓
```

**Known Limitations:**
- Kann in Reflection-Loops geraten (endloses "Ich sollte..." ohne Fortschritt)
- Braucht Max-Iteration-Limit (z.B. 3 Attempts)
- Nur so gut wie Feedback (schlechtes Feedback = schlechte Reflections)

**Related Notes:**
- AB-papers-NOTE-0005 (Self-Refine — für Output-Qualität)
- AB-papers-NOTE-0001 (ReAct — für Action-Loop)

**Tags:** #self-improvement #learning #mvp #iteration

---

### AB-papers-NOTE-0004: RAG für Private Knowledge

**ID:** AB-papers-NOTE-0004  
**Created:** 2026-02-11  
**Classification:** Evidenced (Industry Standard)  
**Confidence:** 95%  
**Sources:** ArXiv 2005.11401, Production Deployments

**This answers:** "Wie greift Mia auf Florian's private Dokumente zu?"

**Core Concept:**
RAG = **Retrieval-Augmented Generation**:
1. **Index:** Dokumente → Embeddings → Vector DB
2. **Retrieve:** User Query → Search Vector DB → Top-K relevante Chunks
3. **Augment:** Top-K Chunks + Query → LLM Context
4. **Generate:** LLM generiert Antwort basierend auf echten Dokumenten

**Why it matters:**
- LLM kann auf **aktuelle, private Daten** zugreifen (nicht nur Training-Data)
- Reduziert Halluzination (LLM zitiert echte Dokumente)
- Skaliert besser als "alles in Context packen"

**How we use it:**
```python
# RAG für Mia auf Obsidian/Notion
class MiaRAG:
    def __init__(self):
        self.vector_db = Chroma()  # oder Pinecone, Weaviate, etc.
        self.embed_model = OpenAIEmbeddings()
    
    def index_documents(self, docs):
        # Obsidian Notes, Notion Pages, Code-Repos
        chunks = self.chunk_documents(docs)  # Split into ~500 token chunks
        embeddings = self.embed_model.embed(chunks)
        self.vector_db.add(chunks, embeddings)
    
    def retrieve(self, query, top_k=5):
        query_embedding = self.embed_model.embed(query)
        relevant_chunks = self.vector_db.search(query_embedding, k=top_k)
        return relevant_chunks
    
    def generate(self, query):
        context = self.retrieve(query)
        prompt = f"Based on these documents:\n{context}\n\nAnswer: {query}"
        answer = llm.generate(prompt)
        return answer
```

**Chunking Best Practices:**
- **Size:** 300-500 tokens per chunk (zu klein = kein Kontext, zu groß = irrelevant)
- **Overlap:** 50-100 tokens (für Kontext-Kontinuität)
- **Metadata:** Speichere Source, Date, Tags für Filtering

**Known Limitations:**
- **Retrieval-Qualität ist KRITISCH:** Schlechte Embeddings → schlechte Chunks → schlechte Antworten
- **Chunking ist eine Kunst:** Dokumente sinnvoll splitten ist schwierig
- **Cost:** Embedding-DB + Retrieval + LLM ist teuer (aber skaliert besser als Finetuning)

**Related Notes:**
- AB-papers-NOTE-0002 (MemGPT — für Session-Memory)
- AB-papers-NOTE-0006 (Chain-of-Thought — für Reasoning)

**Tags:** #memory #knowledge #mvp #critical

---

### AB-papers-NOTE-0005: Self-Refine Output Quality

**ID:** AB-papers-NOTE-0005  
**Created:** 2026-02-11  
**Classification:** Evidenced (Paper + Wide Reproduction)  
**Confidence:** 90%  
**Sources:** ArXiv 2303.17651

**This answers:** "Wie verbessert Mia Output-Qualität iterativ?"

**Core Concept:**
Self-Refine = **Generate → Feedback → Refine → Repeat**:
1. **Generate:** LLM produziert initialen Output (Code, Email, Text)
2. **Self-Feedback:** LLM gibt sich selbst Feedback ("This could be more concise")
3. **Refine:** LLM verbessert Output basierend auf Feedback
4. **Repeat:** Bis "good enough" (z.B. 2-3 Iterationen)

**Why it matters:**
- **Kein externes Feedback nötig** → LLM ist sein eigener Critic
- Funktioniert sofort (keine Finetuning)
- Verbessert Qualität signifikant (z.B. Code-Readability +30%)

**How we use it:**
```python
# Self-Refine für Mia's Outputs
def self_refine(initial_output, task, iterations=2):
    current = initial_output
    
    for i in range(iterations):
        # LLM gibt sich selbst Feedback
        feedback = llm.critique(
            output=current,
            task=task,
            criteria=["clarity", "conciseness", "correctness"]
        )
        
        if feedback.is_good_enough:
            break
        
        # LLM verbessert basierend auf Feedback
        current = llm.refine(
            output=current,
            feedback=feedback
        )
    
    return current
```

**Example:**
```
Task: Write professional email
Initial: "Hey, I was wondering if you could maybe help me with..."
Feedback: "Too casual. Use professional tone. Be more direct."
Refined: "Dear [Name], I would appreciate your assistance with..."
```

**Known Limitations:**
- **Overfitting-Risk:** Zu viele Iterationen können Output verschlechtern (z.B. zu formal)
- **Stop-Kriterium nötig:** "Good enough" definieren (sonst endlose Iterations)
- **Cost:** Jede Iteration = 2 LLM-Calls (Critique + Refine)

**Related Notes:**
- AB-papers-NOTE-0003 (Reflexion — für Task-Level Learning)
- AB-papers-NOTE-0006 (CoT — für Reasoning)

**Tags:** #quality #iteration #mvp #simple

---

### AB-papers-NOTE-0006: Chain-of-Thought Reasoning

**ID:** AB-papers-NOTE-0006  
**Created:** 2026-02-11  
**Classification:** Evidenced (10,000+ Citations)  
**Confidence:** 95%  
**Sources:** ArXiv 2201.11903, Industry Standard

**This answers:** "Wie denkt Mia Schritt-für-Schritt?"

**Core Concept:**
CoT = **"Let's think step by step"**:
- Statt direkter Antwort → LLM zeigt **intermediate reasoning steps**
- Durch Beispiele (few-shot) lernt LLM, wie man "laut denkt"
- Drastisch bessere Performance bei komplexen Tasks (z.B. Math +50%)

**Why it matters:**
- **Trivial zu implementieren** (nur Prompt-Änderung)
- **Enormer Nutzen** (funktioniert bei fast allen komplexen Tasks)
- **Debuggable** (man sieht, WIE der Agent denkt)

**How we use it:**
```python
# CoT für Mia
def solve_with_cot(task):
    prompt = f"""
Task: {task}

Let's solve this step by step:
1. First, I need to understand what is being asked...
2. Then, I should identify the key information...
3. Next, I can...
4. Finally, I conclude that...

Answer: [final answer]
"""
    return llm.generate(prompt)
```

**Example:**
```
Task: Calculate (23 × 4) + (15 ÷ 3)

CoT Reasoning:
1. First, I'll calculate 23 × 4 = 92
2. Then, I'll calculate 15 ÷ 3 = 5
3. Finally, I'll add 92 + 5 = 97

Answer: 97 ✓
```

**Few-Shot vs. Zero-Shot:**
- **Few-Shot CoT:** Gib Beispiele von CoT-Reasoning (besser für schwierige Tasks)
- **Zero-Shot CoT:** Einfach "Let's think step by step" anhängen (funktioniert überraschend gut!)

**Known Limitations:**
- **Verbose:** CoT produziert viel Text (höhere Latenz/Cost)
- **Nicht immer nötig:** Für triviale Tasks ist CoT Overkill
- **Kann halluzinieren:** LLM kann falsche Steps zeigen (aber insgesamt besser als ohne CoT)

**Related Notes:**
- AB-papers-NOTE-0007 (Tree of Thoughts — für komplexere Reasoning)
- AB-papers-NOTE-0005 (Self-Refine — für Output-Qualität)

**Tags:** #reasoning #core #mvp #simple

---

### AB-papers-NOTE-0007: AutoGen Multi-Agent

**ID:** AB-papers-NOTE-0007  
**Created:** 2026-02-11  
**Classification:** Evidenced (Open-Source Framework, Active Use)  
**Confidence:** 85%  
**Sources:** ArXiv 2308.08155, AutoGen GitHub

**This answers:** "Wie bauen wir spezialisierte Sub-Agents für Mia?"

**Core Concept:**
AutoGen = **Multi-Agent-Konversationen**:
- Mehrere Agents mit **unterschiedlichen Rollen** (z.B. Coder, Reviewer, Tester)
- Agents **chatten miteinander** um komplexe Tasks zu lösen
- **Orchestrator** koordiniert Conversation-Flow

**Why it matters:**
- **Multi-Agent > Monolith** für komplexe Tasks
- **Spezialisierung:** Jeder Agent ist Experte in seinem Bereich
- **Skalierbarkeit:** Neue Agents einfach hinzufügen

**How we use it:**
```python
# AutoGen-Style Multi-Agent für Mia
class MiaMultiAgent:
    def __init__(self):
        self.agents = {
            "researcher": ResearchAgent(),
            "writer": WriterAgent(),
            "coder": CoderAgent(),
            "reviewer": ReviewerAgent()
        }
        self.orchestrator = Orchestrator()
    
    def solve_complex_task(self, task):
        # Orchestrator plant Workflow
        plan = self.orchestrator.plan(task)  
        # → [researcher, writer, reviewer]
        
        context = {}
        for agent_name in plan:
            agent = self.agents[agent_name]
            result = agent.execute(task, context)
            context[agent_name] = result
        
        return context["reviewer"].final_output
```

**Example Workflow:**
```
Task: "Write a blog post about AI Agents"

Orchestrator Plan:
1. Researcher → Finds relevant papers and facts
2. Writer → Drafts blog post based on research
3. Reviewer → Checks for clarity, accuracy, flow
4. Writer → Refines based on feedback

Output: Polished blog post ✓
```

**Role Design Best Practices:**
- **Clear Responsibilities:** Jeder Agent hat ONE job
- **Well-Defined Inputs/Outputs:** Agent weiß, was er bekommt und produziert
- **Communication Protocol:** Agents nutzen strukturierte Messages (JSON)

**Known Limitations:**
- **Overhead:** Mehr Agents = mehr API-Calls = höhere Cost
- **Debugging schwierig:** Wer hat den Fehler gemacht?
- **Design ist KRITISCH:** Schlechte Rollen-Definition = Chaos

**Related Notes:**
- AB-papers-NOTE-0001 (ReAct — für Single-Agent Loop)
- AB-papers-NOTE-0008 (MCP — für Tool-Integration)

**Tags:** #multi-agent #architecture #v2 #scaling

---

### AB-papers-NOTE-0008: MCP Standard für Tools

**ID:** AB-papers-NOTE-0008  
**Created:** 2026-02-11  
**Classification:** Evidenced (Linux Foundation, Industry Adoption)  
**Confidence:** 90%  
**Sources:** Anthropic MCP Announcement, modelcontextprotocol.io

**This answers:** "Wie integriert Mia Tools standardisiert?"

**Core Concept:**
MCP = **Model Context Protocol** (wie USB für AI Agents):
- **Ein Standard** für alle Tool-Integrations (statt custom Connectors)
- **MCP Server:** Tool-Provider bietet standardisierte API
- **MCP Client:** Agent nutzt standardisiertes Protocol
- **Interoperabilität:** Jeder Agent kann jeden MCP-Server nutzen

**Why it matters:**
- **Löst Fragmentierung:** Statt N × M Integrations → N Server + M Clients
- **Industry-backed:** Anthropic, OpenAI, Google, Microsoft, AWS alle dabei
- **Future-proof:** Wird DER Standard für Agent-Tool-Integration

**How we use it:**
```python
# Mia nutzt MCP für Tool-Integration
class MiaMCPClient:
    def __init__(self):
        self.servers = {
            "calendar": MCPServer("mcp://calendar.local"),
            "email": MCPServer("mcp://gmail.com/api"),
            "notion": MCPServer("mcp://notion.so/api"),
            "obsidian": MCPServer("mcp://obsidian.local")
        }
    
    def use_tool(self, tool_name, params):
        server = self.servers[tool_name]
        result = server.call(params)
        return result
```

**MCP vs. Custom Integration:**

| Approach | MCP | Custom |
|----------|-----|--------|
| **Development:** | Nutze existierende MCP-Server | Baue jeden Connector selbst |
| **Maintenance:** | Server-Updates automatisch | Jedes API-Change = eigener Fix |
| **Interoperability:** | Andere Agents können nutzen | Nur für dich |
| **Future-proof:** | Industry-Standard | Kann obsolet werden |

**Known Limitations:**
- **Noch früh:** MCP ist neu (2025/2026), Ecosystem wächst noch
- **Nicht alles hat MCP-Server:** Für Nischen-Tools musst du selbst bauen
- **Performance:** Extra Layer kann Latenz hinzufügen (aber minimal)

**Related Notes:**
- AB-papers-NOTE-0001 (ReAct — für Tool-Use Pattern)
- AB-papers-NOTE-0007 (AutoGen — für Multi-Agent)

**Tags:** #infrastructure #tools #mvp #standard

---

### AB-papers-NOTE-0009: LLM Agent Survey (Reference)

**ID:** AB-papers-NOTE-0009  
**Created:** 2026-02-11  
**Classification:** Evidenced (1000+ Citations, Continuously Updated)  
**Confidence:** 95%  
**Sources:** ArXiv 2308.11432, GitHub Repo

**This answers:** "Was ist der State-of-the-Art für LLM Agents?"

**Core Concept:**
Comprehensive Survey über **LLM-based Autonomous Agents**:
- **Architecture:** Perception, Planning, Action Modules
- **Applications:** Code, Robotics, Web Navigation, Games
- **Evaluation:** Benchmarks, Metrics, Challenges
- **Future Directions:** Open Problems

**Why it matters:**
- **Beste Übersicht** über das gesamte Feld (300+ Papers referenziert)
- **Kontinuierlich updated** (GitHub Repo mit neuesten Papers)
- **Praktische Taxonomie** (hilft bei Design-Entscheidungen)

**Key Takeaways für OpenClaw/Mia:**

**Agent Architecture (3 Modules):**
```
┌─────────────────────────────────────┐
│         PERCEPTION                  │
│  (Multimodal Input, Memory, RAG)    │
└──────────────┬──────────────────────┘
               ↓
┌──────────────────────────────────────┐
│         PLANNING                     │
│  (CoT, ToT, ReAct, Reflexion)        │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│         ACTION                       │
│  (Tool Use, Code Exec, API Calls)    │
└──────────────────────────────────────┘
```

**Best Practices (from Survey):**
1. **Modular Design:** Perception/Planning/Action getrennt (einfacher zu debuggen)
2. **Memory Hierarchy:** Short-term + Long-term (wie MemGPT)
3. **Human-in-the-Loop:** Für kritische Entscheidungen
4. **Evaluation:** Track Success Rate, Cost, Latency

**Related Notes:**
- AB-papers-NOTE-0001 (ReAct)
- AB-papers-NOTE-0002 (MemGPT)
- AB-papers-NOTE-0006 (CoT)

**Tags:** #reference #survey #architecture #comprehensive

---

### AB-papers-NOTE-0010: Self-Consistency for Robustness

**ID:** AB-papers-NOTE-0010  
**Created:** 2026-02-11  
**Classification:** Evidenced (2000+ Citations, Widely Used)  
**Confidence:** 90%  
**Sources:** ArXiv 2203.11171

**This answers:** "Wie macht Mia kritische Entscheidungen robuster?"

**Core Concept:**
Self-Consistency = **Sample Multiple + Majority Vote**:
1. **Sample N Reasoning Paths** (mit Temperature > 0, z.B. N=5)
2. **Extract Answers** aus jedem Path
3. **Majority Vote** → finale Antwort

**Why it matters:**
- **Drastisch höhere Accuracy** (z.B. von 60% → 80%)
- **Robust gegen einzelne Fehler** (ein falscher Path wird überstimmt)
- **Trivial zu implementieren** (nur N LLM-Calls + Voting)

**How we use it:**
```python
# Self-Consistency für Mia's kritische Entscheidungen
def decide_with_self_consistency(task, n_samples=5):
    answers = []
    
    for i in range(n_samples):
        # Sample mit Temperature > 0 (für Diversity)
        reasoning = llm.generate(task, temperature=0.7)
        answer = extract_answer(reasoning)
        answers.append(answer)
    
    # Majority Vote
    final_answer = most_common(answers)
    confidence = count(final_answer) / n_samples
    
    return final_answer, confidence
```

**Example:**
```
Task: "Should I send this email now or wait?"

Sample 1: "Wait (recipient is in different timezone)"
Sample 2: "Send now (urgent matter)"
Sample 3: "Wait (better to send during business hours)"
Sample 4: "Wait (recipient might be offline)"
Sample 5: "Wait (not time-sensitive)"

Majority Vote: WAIT (4/5) → Confidence 80%
```

**When to use:**
- **Kritische Entscheidungen:** Email senden, Code deployen, Datei löschen
- **Unsichere Reasoning:** Wenn Task mehrdeutig ist
- **High-Stakes Actions:** Wenn Fehler teuer sind

**Known Limitations:**
- **Cost:** N × LLM-Calls (z.B. 5× teurer als Single-Call)
- **Latenz:** N × Zeit (können parallel machen, aber trotzdem langsamer)
- **Nicht immer nötig:** Für triviale Tasks ist Overkill

**Related Notes:**
- AB-papers-NOTE-0006 (CoT — für Reasoning)
- AB-papers-NOTE-0005 (Self-Refine — für Qualität)

**Tags:** #robustness #critical #decision-making #quality

---

# PLAYBOOKS

## 3 Reusable Processes

---

## PLAYBOOK 1: Paper Evaluation in 15 Min

**Purpose:** Schnell neue Papers bewerten ohne vollständiges Lesen  
**When to use:** Wenn neues Paper erscheint und du entscheiden musst ob relevant  
**Time:** 15 Minuten

### Schritte:

**1. META-CHECK (2 Min)**
- [ ] ArXiv-Link öffnen
- [ ] Autoren checken (bekannte Namen? Affiliation?)
- [ ] Zitationen checken (Google Scholar, Semantic Scholar)
- [ ] Datum checken (wie aktuell?)
- [ ] Code verfügbar? (GitHub Link?)

**Red Flags:**
- ❌ Keine bekannten Autoren + keine Zitationen + >6 Monate alt → wahrscheinlich nicht wichtig
- ❌ Keine Code-Verfügbarkeit + "State-of-the-art claims" → skeptisch sein

**2. ABSTRACT + INTRO (5 Min)**
- [ ] Lies Abstract: Was ist die **Kernidee**?
- [ ] Lies Intro: Was ist das **Problem** und warum ist es wichtig?
- [ ] Überfliege Related Work: Wie ordnet sich das Paper ein?

**Ask yourself:**
- Was ist NEU an diesem Paper? (vs. existierende Lösungen)
- Ist das Problem RELEVANT für uns?

**3. RESULTS + FIGURES (5 Min)**
- [ ] Überspringe Methodology (für jetzt)
- [ ] Gehe direkt zu Results Section
- [ ] Schaue Tabellen/Graphs an: Was sind die **Kernresultate**?
- [ ] Lies Discussion/Conclusion: Was sind **Limitations**?

**Ask yourself:**
- Sind die Ergebnisse beeindruckend? (vs. Baselines)
- Sind die Experimente realistisch? (oder nur Toy-Examples)
- Was sind bekannte Failures/Limitations?

**4. PRACTICAL BUILDABILITY (3 Min)**
Score auf 3 Dimensionen (1-10):

**Theoretical Impact:**
- 1-3: Incremental improvement
- 4-7: Solid contribution
- 8-10: Paradigm shift

**Practical Buildability:**
- 1-3: Braucht Wochen + Expertise
- 4-7: Code existiert, moderat komplex
- 8-10: Trivial zu implementieren (z.B. Prompt-Change)

**Relevance for Us:**
- 1-3: Interessant, aber nicht direkt relevant
- 4-7: Könnte nützlich sein für spezifische Tasks
- 8-10: MÜSSEN wir nutzen

**Final Score = Buildability × Relevance**

**Decision:**
- Score >50 → **Deep-Dive** (lies Methodology, implementiere)
- Score 30-50 → **Monitor** (merke dir, revisit später)
- Score <30 → **Skip** (nicht relevant für uns)

---

## PLAYBOOK 2: Paper-Konzept in OpenClaw/Mia implementieren

**Purpose:** Systematisch Paper-Ideen in Code übersetzen  
**When to use:** Wenn du entschieden hast, ein Paper zu nutzen  
**Time:** Variable (Stunden bis Tage)

### Phase 1: VERSTEHEN (30-60 Min)

**1. Kernkonzept extrahieren:**
- [ ] Lies Methodology Section vollständig
- [ ] Erstelle Flussdiagramm des Algorithmus
- [ ] Identifiziere **kritische Komponenten** (was MUSS funktionieren?)

**2. Code-Review (wenn verfügbar):**
- [ ] Clone GitHub Repo
- [ ] Lies README + Docs
- [ ] Finde **Haupt-Entry-Point** (meist `main.py` oder `run.py`)
- [ ] Identifiziere **Dependencies** (welche Libraries?)

**3. Atomic Note erstellen:**
- [ ] Nutze Template AB-papers-NOTE-XXXX
- [ ] Dokumentiere Kernkonzept, Use-Case, Limitations

### Phase 2: PROTOTYPE (1-3 Stunden)

**1. Minimal Viable Implementation:**
- [ ] Erstelle EINFACHSTE Version (ignore edge cases)
- [ ] Nutze existierenden Code wenn möglich (don't reinvent)
- [ ] Teste mit EINEM Beispiel (funktioniert Kernidee?)

**2. Integration-Check:**
- [ ] Wo gehört das hin in Mia's Architektur?
  - Core Loop (ReAct)? → `agent/core.py`
  - Memory System? → `agent/memory.py`
  - Tool? → `agent/tools/`
  - Utility? → `agent/utils.py`

**3. Quicktest:**
```python
# Standalone Test (bevor Integration)
def test_new_feature():
    input = "test case"
    output = new_feature(input)
    assert output == expected
    print("✓ Feature works!")
```

### Phase 3: REFINE (2-5 Stunden)

**1. Robustheit:**
- [ ] Error-Handling hinzufügen
- [ ] Edge-Cases behandeln
- [ ] Logging hinzufügen (für Debugging)

**2. Integration:**
- [ ] Feature in Mia's Main-Loop integrieren
- [ ] Config-Options hinzufügen (feature toggle)
- [ ] Tests schreiben (Unit + Integration)

**3. Dokumentation:**
- [ ] Docstrings für Functions
- [ ] Update README (new feature)
- [ ] Example-Usage dokumentieren

### Phase 4: EVALUATE (1 Stunde)

**1. Performance-Check:**
- [ ] Latenz messen (wie viel langsamer?)
- [ ] Cost messen (wie viel teurer?)
- [ ] Quality messen (wie viel besser?)

**2. Decision:**
- Wenn Performance/Quality-Gain > Cost/Latency → **KEEP**
- Wenn nicht → **REMOVE** oder **MAKE OPTIONAL**

**3. Lessons Learned:**
- [ ] Update `failures/output-tracker.md`
- [ ] Was hat funktioniert? Was nicht?
- [ ] Update FLORIAN.md (falls relevant für Präferenzen)

---

## PLAYBOOK 3: Paper-Insights in Content verwandeln

**Purpose:** Von Paper-Reading zu Blog/Tweet/Artikel  
**When to use:** Wenn du Paper-Insights teilen willst  
**Time:** 1-2 Stunden (Draft), 30 Min (Distribution)

### Phase 1: SYNTHESIS (30 Min)

**1. Key Insights extrahieren:**
- [ ] Was ist die **eine große Idee** aus dem Paper?
- [ ] Warum sollte **jemand anders** das interessant finden?
- [ ] Was kann man **sofort nutzen**?

**2. Angle finden:**
Choose ONE:
- **Practical:** "How to implement X in 10 lines of code"
- **Critical:** "Why Paper X is overhyped (and what actually works)"
- **Explanatory:** "Understanding X: The concept that changed Y"
- **Comparative:** "ReAct vs. Reflexion: When to use which?"

**3. Outline erstellen:**
```markdown
# Title: [Catchy + Clear]

## Hook (1 paragraph)
- Problem statement
- Why now?

## Core Concept (2-3 paragraphs)
- Explain the idea (ELI5)
- Why it matters
- How it works (simple example)

## Practical Use (2-3 paragraphs)
- How can YOU use this?
- Code example / Implementation
- Known pitfalls

## Conclusion (1 paragraph)
- Key Takeaway
- Call-to-Action (try it / read more / discuss)
```

### Phase 2: WRITE (30-60 Min)

**1. Draft (No Editing!):**
- [ ] Write FAST (get ideas out)
- [ ] Use simple language (avoid jargon unless necessary)
- [ ] Add code examples (practical > theoretical)
- [ ] Include visuals if possible (diagrams, tables)

**2. Self-Refine (15 Min):**
- [ ] Run through Self-Refine loop (AB-papers-NOTE-0005)
- [ ] Check: Clarity, Conciseness, Correctness
- [ ] Remove fluff (every sentence should add value)

**3. Florian-Check:**
- [ ] Würde Florian das lesen? (his test: "Do I learn something NEW in 2 minutes?")
- [ ] Tone: Direct, insightful, founder-operator perspective
- [ ] No bullshit: If you're not sure, say so

### Phase 3: DISTRIBUTE (30 Min)

**Multi-Channel Repurposing:**

**Blog Post (Substack/Medium):**
- [ ] Full article (800-1500 words)
- [ ] Add SEO-friendly title
- [ ] Include links to Paper, Code, Related Posts

**LinkedIn Post:**
- [ ] Summary (300-500 words)
- [ ] Emphasize **practical value**
- [ ] Add "Read full article" CTA

**Twitter Thread:**
- [ ] 5-7 tweets
- [ ] Tweet 1: Hook (problem + solution teaser)
- [ ] Tweet 2-5: Core concept (bite-sized)
- [ ] Tweet 6: Code example or visual
- [ ] Tweet 7: Conclusion + link to full article

**Email Newsletter (if applicable):**
- [ ] Personal intro ("Why I read this paper...")
- [ ] Summary + Insights
- [ ] Link to full article

**Template Beispiel (Twitter Thread):**
```
🧵 I just read [Paper Name] and it's a game-changer for [use-case].

Here's what you need to know (and how to use it):

1/7

---

The problem: [Current state is X, but we want Y]

Most people try [common approach], but it fails because [limitation].

2/7

---

[Paper Name] solves this with [core concept]:

Instead of X, they do Y.

The key insight: [one sentence explanation]

3/7

---

How it works (simplified):

1. [Step 1]
2. [Step 2]
3. [Step 3]

Example: [concrete example]

4/7

---

You can implement this in ~10 lines of code:

[code snippet or pseudocode]

5/7

---

Known limitations:
- [Limitation 1]
- [Limitation 2]

When to use: [use-case]
When to skip: [anti-use-case]

6/7

---

Key Takeaway: [one sentence]

If you're building [X], you should try [Y].

Full breakdown + code: [link to blog]

7/7
```

---

# TEMPLATES

## 2 Reusable Structures

---

## TEMPLATE 1: Paper Evaluation Template

**Purpose:** Wiederverwendbar für jedes neue Paper  
**Format:** Markdown (für Obsidian/Notion)

```markdown
# Paper Evaluation: [Paper Title]

**Evaluated:** [YYYY-MM-DD]  
**Evaluator:** [Your Name / Mia]  
**Time Spent:** [X minutes]

---

## 📋 META

- **Title:** [Full Title]
- **Authors:** [Names + Affiliations]
- **Published:** [Date + Venue (e.g., "October 2022, ICLR 2023")]
- **ArXiv:** [Link]
- **Code:** [GitHub Link or "N/A"]
- **Citations:** [Number + Source (e.g., "5000+ (Semantic Scholar)")]

---

## 🎯 CORE CONCEPT

**In one sentence:**
[What is the key idea?]

**Problem it solves:**
[What existing problem does this address?]

**How it works (simplified):**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Key Innovation:**
[What is NEW compared to prior work?]

---

## 📊 RESULTS

**Key Findings:**
- [Finding 1 + metric]
- [Finding 2 + metric]
- [Finding 3 + metric]

**Baselines Compared:**
- [Baseline 1]
- [Baseline 2]

**Performance Gains:**
- [Metric]: Baseline X → This Paper Y (+Z%)

---

## ⚠️ LIMITATIONS

**Known Issues (from paper):**
- [Limitation 1]
- [Limitation 2]

**Community Criticism (if any):**
- [Critique 1]
- [Critique 2]

**What doesn't work in practice:**
- [Failure mode 1]
- [Failure mode 2]

---

## 📈 SCORES

**Theoretical Impact:** [1-10] / 10  
**Justification:** [Why this score?]

**Practical Buildability:** [1-10] / 10  
**Justification:** [Why this score?]

**Relevance for Us:** [1-10] / 10  
**Justification:** [Why this score?]

**FINAL SCORE:** [Buildability × Relevance] = [Score]

---

## 🎯 DECISION

**Action:** [SOFORT NUTZEN / MITTELFRISTIG / SPÄTER / SKIP]

**Reasoning:**
[Why this decision?]

**Next Steps (if relevant):**
- [ ] Read Methodology Section
- [ ] Clone GitHub Repo
- [ ] Prototype Feature X
- [ ] Integrate into [System]

---

## 🔗 RELATED

**Related Papers:**
- [Paper 1 + ArXiv Link]
- [Paper 2 + ArXiv Link]

**Related Concepts:**
- [Concept 1]
- [Concept 2]

**Tags:** #[tag1] #[tag2] #[tag3]

---

## 💡 ATOMIC NOTE (if score >50)

**Created:** [ ] Yes / [ ] No  
**Note ID:** [AB-papers-NOTE-XXXX]  
**Location:** [Path to note]

---

*Template version: 1.0*  
*Last updated: 2026-02-11*
```

---

## TEMPLATE 2: Paper-to-Article Template (Substack Format)

**Purpose:** Von Paper zu publishable Artikel  
**Format:** Markdown (Substack/Medium-ready)

```markdown
# [Catchy Title: Promise + Intrigue]

**Subtitle:** [What you'll learn in one sentence]

---

## The Problem

[2-3 sentences describing current pain point]

Most people try [common approach], but it fails because [reason].

What if there was a better way?

---

## Enter: [Paper Name]

Researchers at [Institution] just published [Paper Name], and it's changing how we think about [topic].

**The key insight:** [One sentence explanation]

Here's what you need to know.

---

## How It Works (The Simple Version)

[Explain concept like you're talking to a smart friend who's not an expert]

Think of it like this: [Analogy]

The process:
1. [Step 1 — plain language]
2. [Step 2 — plain language]
3. [Step 3 — plain language]

**Example:**
[Concrete example that illustrates the concept]

---

## Why This Matters

Before this paper, [old way].

Now, [new way].

**Real-world impact:**
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

---

## How You Can Use This (Right Now)

[Practical implementation section]

**Option 1: The Quick Win** (5 minutes)
[Simplest way to apply the concept]

```[language]
[Code snippet or step-by-step]
```

**Option 2: The Deep Dive** (1-2 hours)
[More involved implementation]

**Resources:**
- Paper: [ArXiv Link]
- Code: [GitHub Link]
- [Other relevant resources]

---

## What Doesn't Work (Be Honest)

This isn't a silver bullet. Here's what you should know:

**Limitations:**
- [Limitation 1 + why it matters]
- [Limitation 2 + why it matters]

**When to use this:**
- [Use case 1]
- [Use case 2]

**When to skip this:**
- [Anti-use-case 1]
- [Anti-use-case 2]

---

## The Big Picture

[Connect to broader trends or implications]

[Paper Name] is part of a bigger shift: [trend].

Other papers to watch:
- [Related Paper 1]
- [Related Paper 2]

---

## Key Takeaway

[One sentence summary of main point]

**Your next step:**
[Clear call-to-action — try it, read more, share thoughts, etc.]

---

**Further Reading:**
- Full paper: [Link]
- Related articles: [Link]
- My other AI posts: [Link]

**Discussion:**
What do you think? Have you tried this? [Invite comments]

---

*Written by [Your Name] | [Date]*  
*Subscribe for more AI insights: [Link]*
```

---

## 📌 USAGE NOTES

### For Atomic Notes:
- **Storage:** `$OBSIDIAN/60_Resources/Knowledge/Papers/`
- **Naming:** `AB-papers-NOTE-[XXXX]-[Short-Title].md`
- **Linking:** Cross-reference other notes with `[[Note-ID]]`
- **Tags:** Use consistent tags (#mvp, #architecture, #memory, etc.)

### For Playbooks:
- **When to use:** Before starting any new task in the domain
- **Customization:** Adapt steps to your context (skip what's not relevant)
- **Iteration:** Update playbook based on lessons learned

### For Templates:
- **Duplication:** Copy template, don't edit original
- **Completion:** Check off [ ] boxes as you go
- **Version Control:** Note template version for future updates

---

**Asset Pack Version:** 1.0  
**Created:** 2026-02-11  
**Maintained by:** Mia (OpenClaw)  
**Last Updated:** 2026-02-11

---

*These assets are LIVING DOCUMENTS — update them as you learn!*

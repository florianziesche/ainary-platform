# Etched Angle — Agent Benchmark: Apple Silicon vs. Cloud

## Why:
Brian Schechter sits on Etched.ai's board (AI chip company).
A benchmark comparing agent performance on local hardware vs. cloud = content he cares about.
If published well → reaches Brian through Etched connection.

## Benchmark Plan:

### Setup:
1. **Local:** Ollama on MacBook Air M2 (8GB) — Llama 3 8B, Phi-3, Mistral 7B
2. **Cloud:** OpenAI GPT-4o-mini, Claude Haiku, Gemini Flash
3. **Task set:** 10 real agent tasks from daily OpenClaw usage:
   - Research synthesis (web search → summary)
   - Email draft from context
   - Code generation (Python function)
   - Memory retrieval + reasoning
   - Multi-step planning
   - Document analysis
   - Data extraction
   - Creative writing
   - Decision support (with confidence scoring)
   - Tool orchestration (multi-tool chain)

### Metrics:
- **Latency:** Time to first token, total completion time
- **Quality:** 1-5 score per task (human-rated by Florian)
- **Cost:** $/task for cloud, electricity estimate for local
- **Trust Score:** Does the output pass confidence threshold?

### Output:
1. Blog post: "I ran 10 agent tasks on Apple Silicon vs. Cloud. Here's what surprised me."
2. GitHub repo with benchmark scripts + results
3. LinkedIn post (shorter version)
4. Twitter thread tagging @Etched_AI

### Key Hypotheses:
- Local is fast enough for 60-70% of agent tasks
- Cloud wins on complex reasoning (>1000 token outputs)
- Trust scoring works better with local (deterministic, reproducible)
- Cost: local wins after ~100 tasks/day breakeven

### Timeline:
- Install Ollama + models: 1h
- Run benchmarks: 2-3h
- Write up: 2h
- Total: 1 day

## Connection to Primary:
- Shows exactly what OIR would do: "testing new frameworks as they launch, stress-testing capabilities"
- Hardware angle = Etched relevance → Brian's attention
- Published results = proof of builder mentality
- GitHub repo = fills the "empty GitHub" gap

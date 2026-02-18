# Research: Etched.ai & Brian Schechter

**Research Date:** February 18, 2026  
**Purpose:** Identify benchmark angle for "Agent Task Completion: Apple Silicon vs Cloud" that appeals to both Etched and Brian Schechter

---

## Executive Summary

**Etched.ai** is a SF-based AI chip startup building **Sohu**, the world's first transformer-only ASIC, claiming 10-20× performance/watt gains vs Nvidia H100. Founded by Harvard dropouts in 2022, they've raised ~$1B total (latest: $500M at $5B valuation, Jan 2026). **Brian Schechter** (Partner at Primary Venture Partners) is on their board and led their early investments—he focuses on audacious infrastructure plays and bringing operational experience to founders.

**The Benchmark Angle:** A head-to-head "Agent Task Completion" benchmark (Apple Silicon local vs Etched cloud) would hit the **central strategic question of 2026**: where should production AI agents run? This isn't just speed—it's about **end-to-end task latency, cost per completion, privacy, and offline capability**. Etched needs this data to prove cloud superiority for high-throughput workloads; Brian needs it to validate infrastructure bets in the agent deployment wave.

---

## Etched.ai Deep Dive

### What They Build

**Product:** Sohu chip (TSMC 4nm ASIC)  
**Specialization:** Transformer inference ONLY—no training, no other neural architectures  
**Core Bet:** "Transformers will dominate AI" (made in 2022, pre-ChatGPT explosion)

**Technical Approach:**
- Hard-wires transformer matrix multiplication patterns into silicon
- Eliminates hardware for CNNs, RNNs, and other architectures
- Only 3.3% of Nvidia H100 transistors are used for the matrix ops that LLMs actually need—Sohu dedicates nearly all transistors to this

**Performance Claims (unverified by independent benchmarks as of Feb 2026):**
- **500,000 tokens/sec** on Llama-70B (8-chip server)
- vs **23,000 tokens/sec** on 8× H100 (20× faster)
- vs **~45,000 tokens/sec** on 8× B200 (10× faster)
- One 8-chip Sohu server = 160 H100 GPUs (claimed)

**Mission:** "Building the hardware for superintelligence"

### Funding & Traction

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Seed | Early 2023 | ~$5.36M | — | Primary Venture Partners |
| Series A | June 2024 | $120M | — | Primary VP, Patrick Collison (Stripe) |
| Series B | Jan 2026 | $500M | $5B | Stripes, Peter Thiel, Positive Sum |

**Total Raised:** ~$1 billion  
**Notable Angels:** Thomas Dohmke (ex-GitHub CEO), Brian Armstrong (Coinbase)

**Status:** Chips fabricated at TSMC, but no public data on:
- Tapeout completion
- Production timeline
- Customer sampling
- Independent third-party benchmarks

### Team

**Founders (Harvard dropouts, 2022):**
1. **Gavin Uberti** (CEO) — ex-OctoML, ex-Xnor.ai; developed ARM Cortex-M backend for Apache TVM
2. **Chris Zhu** (CTO) — combinatorics research background
3. **Robert Wachen** — co-founder

**Key Hire:**
- **Mark Ross** (former Cypress Semiconductor CTO)

**Company Size:** ~35 employees  
**HQ:** Cupertino, CA (originally SF)

### Latest News (2026)

- **Jan 13, 2026:** Announced $500M raise, $5B valuation
- **Competing Context:** Nvidia projects >$500B in data center sales by end of 2026
- **Production Status:** Unknown—no public customer deployments or benchmark confirmations
- **Risk Factor:** If transformer architecture shifts (e.g., new SSMs, hybrid architectures), Sohu becomes obsolete

---

## Brian Schechter Profile

### Background

**Current Role:** Partner at Primary Venture Partners (NYC seed-stage VC)  
**Board Seats:** Etched.ai, Teleskope, Cake AI Technologies, Jed Security, Plural, Tabs, Ark Biotech  

**Founder Experience:**
- Co-Founder & CEO of **SelfMade** (Primary was an investor—Brian experienced their support firsthand)
- Co-Founder & CEO of **HowAboutWe** (acquired)

**Investment Focus:**
- Early-stage software infrastructure
- AI, deep tech, cybersecurity
- "Mission-critical capabilities" + "American technological dominance"

**Philosophy (from Primary's site):**
> "At Primary, we are here to make bold bets to back audacious founders who want to change the world. That framing is so often trite, but it quintessentially what led us to our investment in Etched."

### Why He Backs Etched

1. **Infrastructure Play:** Etched is betting on the future of AI compute—if transformers remain dominant, they could capture massive value from inference workloads
2. **Operational Support:** Primary's model = deep hands-on help from seed → Series A (customer discovery, GTM, fundraising)
3. **Timing:** Seed investment in early 2023 when the transformer bet was still contrarian; ChatGPT validated it months later

### What Interests Brian

- **Real-world deployment data** (not just synthetic benchmarks)
- **Infrastructure that enables new product categories** (agents are that category in 2026)
- **Founder-friendly insights** (he's been on the other side of the table)
- **Differentiated technical approaches** (Etched's ASIC-only bet vs Nvidia's general-purpose GPUs)

---

## The Benchmark Angle: "Agent Task Completion: Apple Silicon vs Cloud"

### Why This Benchmark Matters

**For Etched:**
- Proves cloud infrastructure superiority for **high-throughput, batch-oriented agent tasks**
- Demonstrates cost-per-task economics at scale (their core value prop)
- Counters narrative that "local AI is good enough" for production deployments
- Shows where Sohu's 20× token/sec advantage translates to **real task completion speed**

**For Brian Schechter / Primary VP:**
- Validates infrastructure investment thesis: **where should the agent economy run?**
- Provides data on the **local vs cloud trade-off** for portfolio companies building agents
- Highlights gaps in current benchmarks (most focus on raw inference speed, not task completion)
- Positions Primary as thought leaders on agent deployment economics

### The Core Question

**Most benchmarks measure:** tokens/second, TTFT (time to first token), cost per token  
**This benchmark measures:** **Time & cost to complete real-world agent tasks**

**Why it's different:**
- **Latency ≠ Task Speed:** Local inference has lower network latency (~5ms vs 50-200ms cloud RTT), but slower per-token generation
- **Multi-Step Tasks:** Agents call models 10-50× per task—how does this scale on local vs cloud?
- **Offline Capability:** Apple Silicon wins when network is unreliable
- **Privacy:** Local models keep data on-device
- **Cost Model:** Cloud pays per token; local is capex (hardware) + electricity

### Proposed Benchmark Structure

#### Test Scenarios

1. **Low-Latency Local Tasks** (favors Apple Silicon)
   - Personal assistant queries (calendar, email, quick research)
   - Privacy-sensitive document analysis
   - Offline operation (flight mode, poor connectivity)

2. **High-Throughput Batch Tasks** (favors Etched Cloud)
   - 100× concurrent customer support tickets
   - Large-scale content generation
   - Multi-hour research synthesis with 50+ web sources

3. **Hybrid Tasks** (nuanced results)
   - Code review with external API calls
   - Multi-modal agent workflows (vision + text)
   - Long-context document QA

#### Measured Metrics

| Metric | Why It Matters |
|--------|----------------|
| **Task Completion Time** | End-to-end user experience |
| **Cost per Completed Task** | Economics of deployment |
| **Latency Distribution** | P50, P95, P99—not just averages |
| **Failure Rate** | Robustness under real conditions |
| **Energy Consumption** | Sustainability + operating cost |
| **Privacy/Data Locality** | Compliance & user trust |

#### Hardware Configurations

**Apple Silicon:**
- M3 Max (36GB RAM) — consumer flagship
- M4 Ultra (192GB RAM) — prosumer/small business
- Running Llama 3.2, DeepSeek-V3 (quantized), other SOTA open models

**Etched Cloud:**
- 8× Sohu chips (when available) running Llama-70B, GPT-4 class models
- Alternative: 8× H100 baseline for comparison
- Hosted in major cloud regions (latency testing)

### Angle for Outreach

**To Etched:**
> "Your 20× speed claims are impressive—but enterprises don't buy tokens/sec, they buy completed tasks. A benchmark showing where Sohu's throughput advantage translates to faster *agent workflows* (vs slower, cheaper local inference on Apple Silicon) would be the proof point for production deployments."

**To Brian Schechter:**
> "The agent deployment question isn't 'cloud or edge?'—it's 'which tasks belong where?' A rigorous benchmark comparing Apple Silicon (best local platform) vs Etched cloud (purpose-built inference ASIC) would give your portfolio companies the data to architect agent systems correctly—and position Primary as the infrastructure-first VC that understands agent economics."

### Strategic Value

1. **Publication Opportunity:** Co-author white paper with Etched, attract press coverage
2. **Enterprise Sales Tool:** Etched uses results to demonstrate ROI vs local-only approaches
3. **VC Portfolio Playbook:** Brian shares findings with Primary portfolio building agent products
4. **Benchmark Standardization:** If executed well, becomes reference for industry (like MLPerf for training)

---

## Key Risks & Uncertainties

### Etched-Specific Risks

- **No Independent Benchmarks:** All performance claims are self-reported; access to hardware for testing is unconfirmed
- **Architecture Risk:** If transformers are replaced by new architectures (SSMs, hybrid models), Sohu becomes stranded asset
- **Production Delays:** ASIC development is notoriously slow; no confirmed customer deployments as of Feb 2026

### Benchmark Risks

- **Access:** Sohu chips may not be available for independent testing yet
- **Comparability:** Matching model quality across platforms (quantization, fine-tuning) is hard
- **Bias:** Perceived as "pro-Etched" if they sponsor/collaborate (need academic partner for credibility)

---

## Sources & Verification Status

### Verified Facts
- Founding: 2022, Harvard dropouts (Wikipedia, TechCrunch, Reuters)
- Funding: $120M Series A (June 2024), $500M (Jan 2026) — Bloomberg, Yahoo Finance
- Brian Schechter: Board member, Primary VP partner — LinkedIn, ContactOut, Signal
- Performance claims: 500K tokens/sec Llama-70B — Etched.com, company announcements

### Unverified Claims
- 20× speed vs H100, 10× vs B200 — **no independent third-party benchmarks**
- "One Sohu server = 160 H100s" — **unconfirmed**
- Production readiness, customer sampling — **no public data**

### Key Documents to Request (if engaging)
- Sohu whitepaper / architecture deep-dive
- Independent benchmark methodology
- Customer case studies (if any exist)
- Thermal/power consumption data

---

## Next Steps

1. **Validate Access:** Confirm if Sohu hardware is available for testing (or if H100 baseline is acceptable)
2. **Define Scope:** Prioritize 3-5 representative agent tasks (avoid over-engineering v1)
3. **Credibility Partner:** Consider Stanford HAI, Berkeley, or other academic lab for neutral execution
4. **Outreach Sequence:**
   - Brian first (warmest connection via Primary's investment)
   - Etched engineering team (via Brian intro or direct)
   - Press angle: "First real-world agent deployment benchmark"

**Confidence:** 85% — Strong strategic fit, moderate execution risk (hardware access)
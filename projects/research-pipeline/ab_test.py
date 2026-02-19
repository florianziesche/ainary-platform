#!/usr/bin/env python3
"""
A/B Test: OpenAI GPT-4o vs Claude Sonnet — Same pipeline, same topic, compare outputs.
"""
import json, os, sys, time, re, hashlib
from pathlib import Path
from datetime import datetime

# Brave API key
BRAVE_KEY = json.load(open(Path.home() / ".openclaw/openclaw.json"))["tools"]["web"]["search"]["apiKey"]
OPENAI_KEY = os.environ.get("OPENAI_API_KEY") or json.load(open(Path.home() / ".openclaw/openclaw.json"))["env"]["OPENAI_API_KEY"]
OAUTH_TOKEN = None

def _load_oauth():
    path = Path.home() / ".openclaw/agents/main/agent/auth-profiles.json"
    data = json.loads(path.read_text())
    for pid in ["anthropic:default", "anthropic:manual"]:
        t = data.get("profiles", {}).get(pid, {}).get("token", "")
        if t.startswith("sk-ant-oat01-"):
            return t
    return None

OAUTH_TOKEN = _load_oauth()

def call_openai(prompt, max_tokens=16000):
    from openai import OpenAI
    c = OpenAI(api_key=OPENAI_KEY)
    r = c.chat.completions.create(model="gpt-4o", max_tokens=max_tokens, temperature=0, messages=[{"role":"user","content":prompt}])
    return r.choices[0].message.content, r.usage.total_tokens

def call_sonnet(prompt, max_tokens=16000):
    import httpx
    r = httpx.post("https://api.anthropic.com/v1/messages",
        headers={"Authorization": f"Bearer {OAUTH_TOKEN}", "anthropic-version": "2023-06-01",
                 "anthropic-beta": "oauth-2025-04-20", "content-type": "application/json"},
        json={"model": "claude-sonnet-4-20250514", "max_tokens": max_tokens,
              "messages": [{"role": "user", "content": prompt}]},
        timeout=httpx.Timeout(connect=30, read=600, write=30, pool=30))
    if r.status_code != 200:
        raise RuntimeError(f"Sonnet error {r.status_code}: {r.text[:200]}")
    d = r.json()
    tokens = d["usage"]["input_tokens"] + d["usage"]["output_tokens"]
    return d["content"][0]["text"], tokens

def brave_search(queries, max_results=5):
    import urllib.request, urllib.parse
    results = []
    for q in queries[:4]:
        try:
            url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(q)}&count={max_results}"
            req = urllib.request.Request(url, headers={"X-Subscription-Token": BRAVE_KEY, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                for w in data.get("web", {}).get("results", []):
                    results.append(f"- {w['title']}: {w.get('description','')} ({w['url']})")
        except Exception as e:
            print(f"  [WARN] Brave: {e}")
    return "\n".join(results)

def build_prompt(topic, web_evidence=""):
    return f"""You are a senior research analyst. Write a detailed executive research report on:

**{topic}**

Requirements:
1. Start with a Beipackzettel (metadata table: Research Type, Data Source, Confidence, Limitations)
2. Executive Summary (lead with something an expert DOESN'T already know)
3. 5-8 Key Findings — each with specific evidence, numbers, source references [S1]-[S10]
4. "Do Not Deploy If" section (3-5 risk scenarios)
5. Recommendations (actionable, with timeline)
6. Source List with URLs/DOIs

Rules:
- Every factual claim needs a source reference [S#]
- No LLM phrases: landscape, synergy, cutting-edge, game-changer, delve, tapestry
- If no source exists for a claim: mark as "author estimate"
- Be specific: numbers > adjectives, dates > "recently", names > "researchers"
- Research Type must be "Expert Synthesis" and Data Source "Secondary" (be honest)

{f'## Web Evidence (use these sources):{chr(10)}{web_evidence}' if web_evidence else ''}

Write 3000-5000 words. Be thorough but honest about limitations."""

def extract_claims(report, call_fn):
    prompt = f"""Extract the 15 most important factual claims from this report. For each:
- text: the claim (verbatim or close)
- has_source: true if it references [S#], false otherwise
- source_quality: "tier1" (peer-reviewed/DOI), "tier2" (preprint/vendor report), "tier3" (blog/unknown), "none"
- verification: "verified" (specific source cited with URL/DOI), "partial" (source mentioned but vague), "unverifiable" (no source)
- admiralty: Rating from A1 (reliable source, confirmed) to F6 (unreliable, unconfirmed). 
  IMPORTANT: Default should be C3 (fairly reliable, possibly true). Only use A1 if there's a specific DOI or peer-reviewed reference.
  B2 = usually reliable + probably true. D4 = not usually reliable + doubtful.
- weight: "load-bearing" (conclusion depends on this), "supporting", "contextual"

Be SKEPTICAL. Most claims without DOIs should be C3 or worse. "Author estimate" = D4.
Output as JSON array only.

REPORT:
{report[:12000]}"""
    result, _ = call_fn(prompt, max_tokens=4000)
    try:
        return json.loads(re.search(r'\[.*\]', result, re.DOTALL).group())
    except:
        return []

# Confidence formula
ADMIRALTY = {"A1":0.95,"A2":0.85,"B1":0.8,"B2":0.7,"B3":0.6,"C1":0.55,"C2":0.5,"C3":0.4,
             "D1":0.35,"D2":0.3,"D3":0.25,"D4":0.2,"E1":0.15,"E2":0.1,"F1":0.05,"F3":0.02,"F6":0.01}
VERIFICATION = {"verified":1.0, "partial":0.5, "unverifiable":0.1}
WEIGHT = {"load-bearing":1.0, "supporting":0.6, "contextual":0.3}

def compute_confidence(claims):
    if not claims: return 0, []
    computed = []
    for c in claims:
        adm = ADMIRALTY.get(c.get("admiralty","C3"), 0.4)
        ver = VERIFICATION.get(c.get("verification","partial"), 0.3)
        rec = max(0.5, 1.0 - (2026 - c.get("recency_year", 2024)) * 0.1)
        conf = adm * ver * rec
        w = WEIGHT.get(c.get("weight","supporting"), 0.5)
        computed.append({"text": c.get("text","")[:80], "confidence": round(conf,4), "weight": w,
                        "admiralty": c.get("admiralty","?"), "verification": c.get("verification","?")})
    wsum = sum(c["confidence"] * c["weight"] for c in computed)
    wtot = sum(c["weight"] for c in computed)
    return round(wsum/wtot, 4) if wtot else 0, computed

def count_llm_phrases(text):
    phrases = ["landscape", "synergy", "cutting-edge", "game-changer", "delve", "tapestry",
               "it's worth noting", "in today's world", "paradigm shift", "holistic"]
    return sum(1 for p in phrases if p.lower() in text.lower())

def main():
    topic = "Trust Calibration for AI Agents"
    out_dir = Path.home() / ".openclaw/workspace/research/experiments/ab-test"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print(f"A/B TEST: GPT-4o vs Claude Sonnet")
    print(f"Topic: {topic}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)

    # Shared: Brave Search
    print("\n[1/5] Brave Search...")
    queries = [f"{topic} peer-reviewed 2024 2025", f"{topic} empirical study",
               f"{topic} systematic review", f"{topic} benchmark evaluation"]
    web_evidence = brave_search(queries)
    print(f"  Found {web_evidence.count(chr(10))+1} results")
    (out_dir / "web-evidence.txt").write_text(web_evidence)

    prompt = build_prompt(topic, web_evidence)
    print(f"  Prompt: {len(prompt)} chars")

    results = {}

    # --- Model A: GPT-4o ---
    print("\n[2/5] GPT-4o producing report...")
    t0 = time.time()
    report_a, tokens_a = call_openai(prompt)
    time_a = time.time() - t0
    print(f"  Done in {time_a:.1f}s, {len(report_a)} chars, {tokens_a} tokens")
    (out_dir / "report-gpt4o.md").write_text(report_a)

    print("  Extracting claims (GPT-4o evaluator)...")
    claims_a = extract_claims(report_a, call_openai)
    conf_a, details_a = compute_confidence(claims_a)
    llm_a = count_llm_phrases(report_a)

    results["gpt4o"] = {
        "model": "GPT-4o", "chars": len(report_a), "tokens": tokens_a,
        "time_s": round(time_a, 1), "confidence": conf_a, "n_claims": len(claims_a),
        "llm_phrases": llm_a, "claims": details_a
    }
    print(f"  Confidence: {conf_a:.1%}, Claims: {len(claims_a)}, LLM phrases: {llm_a}")

    # --- Model B: Claude Sonnet ---
    print("\n[3/5] Claude Sonnet producing report...")
    t0 = time.time()
    report_b, tokens_b = call_sonnet(prompt)
    time_b = time.time() - t0
    print(f"  Done in {time_b:.1f}s, {len(report_b)} chars, {tokens_b} tokens")
    (out_dir / "report-sonnet.md").write_text(report_b)

    # Use Sonnet to evaluate its own claims (fair: each model evaluates itself)
    print("  Extracting claims (Sonnet evaluator)...")
    claims_b = extract_claims(report_b, call_sonnet)
    conf_b, details_b = compute_confidence(claims_b)
    llm_b = count_llm_phrases(report_b)

    results["sonnet"] = {
        "model": "Claude Sonnet 4", "chars": len(report_b), "tokens": tokens_b,
        "time_s": round(time_b, 1), "confidence": conf_b, "n_claims": len(claims_b),
        "llm_phrases": llm_b, "claims": details_b
    }
    print(f"  Confidence: {conf_b:.1%}, Claims: {len(claims_b)}, LLM phrases: {llm_b}")

    # --- Cross-evaluation: Sonnet evaluates GPT-4o, GPT-4o evaluates Sonnet ---
    print("\n[4/5] Cross-evaluation...")
    print("  Sonnet evaluating GPT-4o report...")
    claims_a_by_b = extract_claims(report_a, call_sonnet)
    conf_a_by_b, _ = compute_confidence(claims_a_by_b)
    results["gpt4o"]["cross_confidence"] = conf_a_by_b
    print(f"  GPT-4o confidence (by Sonnet): {conf_a_by_b:.1%}")

    print("  GPT-4o evaluating Sonnet report...")
    claims_b_by_a = extract_claims(report_b, call_openai)
    conf_b_by_a, _ = compute_confidence(claims_b_by_a)
    results["sonnet"]["cross_confidence"] = conf_b_by_a
    print(f"  Sonnet confidence (by GPT-4o): {conf_b_by_a:.1%}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("[5/5] RESULTS")
    print("=" * 60)
    print(f"{'Metric':<25} {'GPT-4o':>12} {'Sonnet':>12}")
    print("-" * 50)
    print(f"{'Report length':.<25} {len(report_a):>10} ch {len(report_b):>10} ch")
    print(f"{'Tokens used':.<25} {tokens_a:>12} {tokens_b:>12}")
    print(f"{'Time':.<25} {time_a:>10.1f}s {time_b:>10.1f}s")
    print(f"{'Self-confidence':.<25} {conf_a:>11.1%} {conf_b:>11.1%}")
    print(f"{'Cross-confidence':.<25} {conf_a_by_b:>11.1%} {conf_b_by_a:>11.1%}")
    print(f"{'Claims extracted':.<25} {len(claims_a):>12} {len(claims_b):>12}")
    print(f"{'LLM phrases':.<25} {llm_a:>12} {llm_b:>12}")
    print(f"{'Avg claim confidence':.<25} {conf_a:>11.1%} {conf_b:>11.1%}")

    # Winner
    avg_a = (conf_a + conf_a_by_b) / 2
    avg_b = (conf_b + conf_b_by_a) / 2
    winner = "GPT-4o" if avg_a > avg_b else "Sonnet" if avg_b > avg_a else "TIE"
    print(f"\n{'Avg confidence (both evals)':.<25} {avg_a:>11.1%} {avg_b:>11.1%}")
    print(f"\n>>> WINNER: {winner} <<<")

    results["summary"] = {
        "winner": winner, "avg_confidence_gpt4o": avg_a, "avg_confidence_sonnet": avg_b,
        "timestamp": datetime.now().isoformat(), "topic": topic
    }
    (out_dir / "results.json").write_text(json.dumps(results, indent=2))
    print(f"\nResults: {out_dir / 'results.json'}")

if __name__ == "__main__":
    main()

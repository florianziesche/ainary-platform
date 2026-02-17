#!/usr/bin/env python3
"""
Ainary Research Pipeline — Multi-Model Report Generator
Uses Anthropic API with smart model routing to maximize $200 budget.
"""

import anthropic
import json
import os
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

# --- Config ---
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
RESEARCH_DIR = WORKSPACE / "projects/platform-website/research"
TEMPLATE_PATH = RESEARCH_DIR / "state-of-agent-trust-2026/index.html"
INBOX_DIR = WORKSPACE / "research/inbox"

MODELS = {
    "extract": "claude-haiku-4-5-20250514",
    "synthesize": "claude-sonnet-4-5-20250514",
    "write": "claude-opus-4-20250514",
    "quality": "claude-sonnet-4-5-20250514",
}

MAX_TOKENS = {
    "extract": 4096,
    "synthesize": 8192,
    "write": 16384,
    "quality": 4096,
}

@dataclass
class Paper:
    title: str
    url: str
    date: str = ""
    authors: str = ""
    abstract: str = ""
    key_findings: list = field(default_factory=list)
    relevance: int = 0  # 1-5
    
@dataclass  
class ReportConfig:
    report_id: str           # e.g. "AR-041"
    title: str
    slug: str                # e.g. "ai-governance-2026"
    topic: str               # Search query / topic description
    num_papers: int = 10
    sections: list = field(default_factory=list)
    papers: list = field(default_factory=list)
    synthesis: str = ""
    html: str = ""
    confidence: int = 0

class ResearchPipeline:
    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.total_cost = 0.0
        self.token_log = []
        
    def _call(self, model_key: str, system: str, user: str, temperature: float = 0.3) -> str:
        """Call Anthropic API with model routing and cost tracking."""
        model = MODELS[model_key]
        max_tokens = MAX_TOKENS[model_key]
        
        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}]
        )
        
        # Track usage
        usage = response.usage
        self.token_log.append({
            "model": model,
            "stage": model_key,
            "input": usage.input_tokens,
            "output": usage.output_tokens,
            "timestamp": datetime.now().isoformat()
        })
        
        return response.content[0].text

    # --- Stage 1: Paper Discovery ---
    def discover_papers(self, config: ReportConfig) -> list[Paper]:
        """Use Haiku to find and extract papers for a topic."""
        print(f"📡 Stage 1: Discovering papers for '{config.topic}'...")
        
        # Search arxiv and web for papers
        search_prompt = f"""Find the {config.num_papers} most important and recent academic papers about: {config.topic}

For each paper, provide:
- title (exact)
- arxiv URL or DOI (exact, verified)
- date (YYYY-MM)
- authors (first author et al.)
- 2-sentence abstract summary
- relevance score 1-5 (5 = directly relevant to AI agents, trust, memory, or governance)

Output as JSON array. Only include papers you are confident exist."""

        result = self._call("extract", 
            "You are a research assistant. Output valid JSON only.", 
            search_prompt)
        
        try:
            papers_data = json.loads(result.strip().strip("```json").strip("```"))
            papers = [Paper(**p) if isinstance(p, dict) else Paper(title="?", url="?") for p in papers_data]
            print(f"   Found {len(papers)} papers")
            return papers
        except json.JSONDecodeError:
            print(f"   ⚠️ JSON parse error, attempting extraction...")
            return []

    # --- Stage 2: Paper Extraction ---
    def extract_findings(self, paper: Paper) -> Paper:
        """Use Haiku to extract key findings from a paper."""
        print(f"   📄 Extracting: {paper.title[:60]}...")
        
        extract_prompt = f"""Analyze this paper:
Title: {paper.title}
URL: {paper.url}
Authors: {paper.authors}
Date: {paper.date}

Extract:
1. Main thesis (1 sentence)
2. Key findings (3-5 bullet points)
3. Methodology summary
4. Limitations acknowledged
5. How this relates to AI agent trust, memory, or governance
6. Confidence in findings (E=Evidenced, I=Interpretation, J=Judgment, A=Assumption)

Be precise. Only state what the paper actually claims."""

        result = self._call("extract",
            "You are a precise research analyst. Extract facts, not opinions.",
            extract_prompt)
        
        paper.key_findings = result.split("\n")
        return paper

    # --- Stage 3: Synthesis ---
    def synthesize(self, config: ReportConfig) -> str:
        """Use Sonnet to synthesize findings across papers."""
        print(f"🔬 Stage 3: Synthesizing {len(config.papers)} papers...")
        
        findings_text = "\n\n".join([
            f"## {p.title} ({p.date})\n{chr(10).join(p.key_findings)}"
            for p in config.papers
        ])
        
        synth_prompt = f"""You have findings from {len(config.papers)} papers about: {config.topic}

{findings_text}

Synthesize into:
1. **Consensus** — What do most papers agree on?
2. **Contradictions** — Where do papers disagree?
3. **Gaps** — What's missing from the literature?
4. **Trends** — What direction is the field moving?
5. **Practitioner Implications** — What should someone building AI agents do differently based on this research?
6. **Confidence Assessment** — How strong is the overall evidence? (0-100%)

Be opinionated. This is for a practitioner report, not an academic survey."""

        config.synthesis = self._call("synthesize",
            "You are a senior AI research analyst at Ainary Ventures. Direct, opinionated, evidence-based.",
            synth_prompt, temperature=0.5)
        
        print(f"   Synthesis complete ({len(config.synthesis)} chars)")
        return config.synthesis

    # --- Stage 4: Report Writing ---
    def write_report(self, config: ReportConfig) -> str:
        """Use Opus to write the final HTML report."""
        print(f"✍️ Stage 4: Writing {config.report_id}...")
        
        # Load HTML template
        template = TEMPLATE_PATH.read_text() if TEMPLATE_PATH.exists() else "<html><body>{content}</body></html>"
        
        write_prompt = f"""Write research report {config.report_id}: "{config.title}"

## Synthesis of {len(config.papers)} papers:
{config.synthesis}

## Papers cited:
{json.dumps([{"title": p.title, "url": p.url, "date": p.date} for p in config.papers], indent=2)}

## Requirements:
- Use this HTML template structure (dark mode, mono fonts, AR-001 style)
- Report ID: {config.report_id}
- Confidence scores per section
- E/I/J/A badges on claims
- Back cover: gold dot, "Ainary", "AI strategy - research - implementation. By someone who built the systems first.", contact → https://ainaryventures.com/contact.html, © 2026
- Tone: Direct, opinionated, Florian Ziesche's voice
- 3000-5000 words
- All citations linked

## Sections:
{json.dumps(config.sections, indent=2)}

Output the complete HTML file."""

        config.html = self._call("write",
            "You are Florian Ziesche, founder of Ainary Ventures. Write in first person where appropriate. Direct, no filler. Evidence-based but opinionated.",
            write_prompt, temperature=0.4)
        
        print(f"   Report written ({len(config.html)} chars)")
        return config.html

    # --- Stage 5: Quality Gate ---
    def quality_check(self, config: ReportConfig) -> dict:
        """Use Sonnet to audit the report."""
        print(f"🔍 Stage 5: Quality gate for {config.report_id}...")
        
        qa_prompt = f"""Audit this research report:

{config.html[:10000]}... [truncated]

Check:
1. Are all paper citations present with correct URLs?
2. Are confidence scores assigned to each section?
3. Is the HTML valid (balanced tags)?
4. Are there unsupported claims (no citation)?
5. Is the tone consistent (direct, opinionated, not academic)?
6. Word count estimate?
7. Overall quality score (0-100)?

Output as JSON with keys: citations_ok, confidence_ok, html_valid, unsupported_claims, tone_ok, word_count, quality_score, issues[]"""

        result = self._call("quality",
            "You are a strict quality auditor. Find problems.",
            qa_prompt)
        
        try:
            return json.loads(result.strip().strip("```json").strip("```"))
        except:
            return {"quality_score": 0, "issues": ["Could not parse QA result"]}

    # --- Stage 6: Publish ---
    def publish(self, config: ReportConfig) -> str:
        """Save report and optionally deploy."""
        output_dir = RESEARCH_DIR / config.slug
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "index.html"
        
        output_path.write_text(config.html)
        print(f"💾 Saved to {output_path}")
        
        return str(output_path)

    # --- Full Pipeline ---
    def run(self, config: ReportConfig, deploy: bool = False) -> ReportConfig:
        """Run the full pipeline for one report."""
        print(f"\n{'='*60}")
        print(f"🚀 Starting pipeline for {config.report_id}: {config.title}")
        print(f"{'='*60}\n")
        
        # Stage 1: Discover
        config.papers = self.discover_papers(config)
        
        # Stage 2: Extract
        for i, paper in enumerate(config.papers):
            config.papers[i] = self.extract_findings(paper)
        
        # Stage 3: Synthesize
        self.synthesize(config)
        
        # Stage 4: Write
        self.write_report(config)
        
        # Stage 5: Quality
        qa = self.quality_check(config)
        config.confidence = qa.get("quality_score", 0)
        print(f"   Quality score: {config.confidence}/100")
        if qa.get("issues"):
            for issue in qa["issues"][:3]:
                print(f"   ⚠️ {issue}")
        
        # Stage 6: Publish
        path = self.publish(config)
        
        # Deploy if requested
        if deploy:
            print("🚀 Deploying...")
            subprocess.run(
                ["npx", "vercel", "--prod", "--yes"],
                cwd=str(RESEARCH_DIR.parent),
                capture_output=True
            )
        
        # Cost summary
        total_input = sum(t["input"] for t in self.token_log)
        total_output = sum(t["output"] for t in self.token_log)
        print(f"\n📊 Token usage: {total_input:,} in / {total_output:,} out")
        print(f"   Saved to: {path}")
        
        return config

    def run_batch(self, configs: list[ReportConfig], deploy: bool = False):
        """Run pipeline for multiple reports."""
        results = []
        for config in configs:
            try:
                result = self.run(config, deploy=deploy)
                results.append(result)
            except Exception as e:
                print(f"❌ Failed {config.report_id}: {e}")
                results.append(config)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"📋 BATCH COMPLETE: {len(results)} reports")
        print(f"{'='*60}")
        for r in results:
            status = "✅" if r.confidence > 70 else "⚠️"
            print(f"   {status} {r.report_id}: {r.title} ({r.confidence}%)")
        
        total_input = sum(t["input"] for t in self.token_log)
        total_output = sum(t["output"] for t in self.token_log)
        print(f"\n📊 Total tokens: {total_input:,} in / {total_output:,} out")
        
        # Save token log
        log_path = INBOX_DIR / f"pipeline-log-{datetime.now().strftime('%Y-%m-%d')}.json"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(json.dumps(self.token_log, indent=2))
        print(f"   Log: {log_path}")


# --- Example Report Configs ---
EXAMPLE_REPORTS = [
    ReportConfig(
        report_id="AR-041",
        title="AI Governance Frameworks — What Actually Works in 2026",
        slug="ai-governance-frameworks-2026",
        topic="AI governance frameworks enterprise implementation 2026 ISO 42001 NIST",
        sections=["Executive Summary", "The Landscape", "ISO 42001 in Practice", "NIST AI RMF", "EU AI Act Compliance", "What Enterprises Actually Do", "Recommendations", "Methodology"],
    ),
    ReportConfig(
        report_id="AR-042",
        title="The State of Multi-Agent Systems — From Research to Production",
        slug="multi-agent-systems-2026",
        topic="multi-agent systems production deployment 2026 orchestration coordination",
        sections=["Executive Summary", "Academic Landscape", "Production Deployments", "Orchestration Patterns", "Failure Modes", "Cost Analysis", "Recommendations", "Methodology"],
    ),
    ReportConfig(
        report_id="AR-043",
        title="AI Due Diligence for VCs — A Technical Framework",
        slug="ai-due-diligence-framework-2026",
        topic="AI startup due diligence technical evaluation framework venture capital 2026",
        sections=["Executive Summary", "Why Technical DD Matters", "The Framework", "Model Risk", "Data Moat Assessment", "Team Evaluation", "Red Flags", "Case Studies", "Recommendations", "Methodology"],
    ),
]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ainary Research Pipeline")
    parser.add_argument("--report", type=int, help="Run specific report (0-indexed)")
    parser.add_argument("--all", action="store_true", help="Run all example reports")
    parser.add_argument("--deploy", action="store_true", help="Deploy after writing")
    parser.add_argument("--custom", type=str, help="Custom topic (creates AR-044)")
    args = parser.parse_args()
    
    pipeline = ResearchPipeline()
    
    if args.custom:
        config = ReportConfig(
            report_id="AR-044",
            title=args.custom,
            slug=args.custom.lower().replace(" ", "-")[:40],
            topic=args.custom,
        )
        pipeline.run(config, deploy=args.deploy)
    elif args.all:
        pipeline.run_batch(EXAMPLE_REPORTS, deploy=args.deploy)
    elif args.report is not None:
        pipeline.run(EXAMPLE_REPORTS[args.report], deploy=args.deploy)
    else:
        print("Usage:")
        print("  python pipeline.py --report 0       # Run AR-041")
        print("  python pipeline.py --all             # Run all")
        print("  python pipeline.py --custom 'topic'  # Custom report")
        print(f"\nAvailable: {[r.report_id for r in EXAMPLE_REPORTS]}")
        print(f"Budget: $200 ≈ 149 reports at ~$1.34/report")

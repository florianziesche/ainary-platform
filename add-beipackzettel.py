#!/usr/bin/env python3
"""Add Beipackzettel (Confidence Framework + Transparency Note) to reports."""

import re

BASE = "/Users/florianziesche/.openclaw/workspace/projects/platform-website/research"

# Report configs: (dir, report_id, confidence_pct, insert_before_exec_pattern, sources_desc, strongest, weakest, invalidation, limitations, section_num_transparency)
reports = [
    {
        "dir": "one-person-ai-company-2026",
        "id": "AR-033",
        "title": "How One Founder Replaced a Team with AI Agents",
        "confidence": 78,
        "confidence_label": "Medium-High",
        "sources_total": 10,
        "sources_desc": "10 sources: 5 internal production data (git logs, API billing, cron configs, daily notes, OpenClaw analytics), 3 external references (Anthropic pricing, OpenClaw documentation, industry benchmarks), 2 synthesis documents (SYNTHESIS-v2.md conversation analysis, output tracker).",
        "badge_summary": "45 [E]videnced, 12 [I]nterpretation, 11 [J]udgment, 2 [A]ssumption",
        "evidence_note": "Heavily evidenced — this is a case study built primarily on first-party production data (git commits, API bills, cron logs), making most claims directly verifiable.",
        "strongest": "Git log data (35 commits verifiable), API billing records ($78.32 monthly cost), cron execution logs — all first-party, auditable production data.",
        "weakest": "The claim that this approach generalizes beyond the author's specific use case. One founder's experience with AI agents does not constitute a replicable methodology. Selection bias: only successful workflows are reported in detail.",
        "invalidation": "If (a) the 35-commit output is shown to require significant human rework not disclosed, (b) API costs scale non-linearly with realistic workloads, or (c) the approach fails when replicated by others with similar technical skill.",
        "limitations": [
            "<strong>N=1 case study.</strong> All production data comes from a single founder's workflow. Generalizability is unknown.",
            "<strong>Survivorship bias.</strong> Failed experiments and abandoned approaches receive less coverage than successful ones.",
            "<strong>Cost calculations assume current pricing.</strong> API pricing changes frequently; the $78/month figure is a snapshot, not a guarantee.",
            "<strong>Quality assessment is self-reported.</strong> The claim that output matches a '5-person team' lacks independent validation or quality benchmarking.",
            "<strong>Technical prerequisites not fully quantified.</strong> The founder's existing technical skills are a significant confound not controlled for.",
        ],
        # Insert Part 1 before exec-summary div
        "part1_before": '<div class="page" id="exec-summary">',
        # Insert Part 2 before back-cover
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "12",
        "toc_how_to_read_num": None,  # already has how-to-read
        "has_how_to_read": True,
    },
    {
        "dir": "agentic-patterns-2026",
        "id": "AR-035",
        "title": "The 3 Agentic Patterns That Actually Matter",
        "confidence": 62,
        "confidence_label": "Medium",
        "sources_total": 8,
        "sources_desc": "8 sources: 2 pattern taxonomies (Beam.ai, Rana/Medium), 2 enterprise architecture guides (Microsoft Azure, Google Cloud), 1 enterprise consulting analysis (Dextralabs), 3 internal sources (AGENTS.md configuration, OpenClaw community research, SYNTHESIS-v2 evolution experiment).",
        "badge_summary": "4 [E]videnced, 2 [I]nterpretation, 12 [J]udgment, 1 [A]ssumption",
        "evidence_note": "Heavily judgment-based — the core thesis (3 patterns matter, 6 don't) is an opinionated assessment from production experience, not a controlled comparison.",
        "strongest": "Pattern taxonomy from established sources (Microsoft Azure, Google Cloud architecture docs). Internal production validation over 4+ months of daily use.",
        "weakest": "The ranking of patterns (which 3 matter vs. which 6 don't) is based on one solo operator's experience. No controlled experiment comparing pattern effectiveness. Enterprise patterns dismissed as irrelevant may work well at scale.",
        "invalidation": "If (a) solo operators report success with the 6 'dismissed' patterns, (b) the 3 recommended patterns fail in different tool ecosystems, or (c) a controlled study shows pattern effectiveness is context-independent.",
        "limitations": [
            "<strong>Solo-operator bias.</strong> Patterns are evaluated from one person's perspective. Enterprise teams with different constraints may reach opposite conclusions.",
            "<strong>No controlled comparison.</strong> The '3 that matter' thesis is based on production intuition, not A/B testing or systematic measurement.",
            "<strong>Tool-ecosystem dependent.</strong> Results are specific to the OpenClaw/Claude stack. Other agent frameworks may favor different patterns.",
            "<strong>Limited source diversity.</strong> Only 8 sources, with 3 being internal. No academic research on pattern effectiveness.",
            "<strong>Recency bias.</strong> 4 months of production use may not capture long-term pattern evolution or failure modes.",
        ],
        "part1_before": '<div class="page" id="exec-summary">',
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "10",
        "has_how_to_read": False,
    },
    {
        "dir": "agent-trust-q1-update-2026",
        "id": "AR-036",
        "title": "State of AI Agent Trust — Q1 2026 Update",
        "confidence": 71,
        "confidence_label": "Medium-High",
        "sources_total": 32,
        "sources_desc": "32 sources total: 24 from AR-001 baseline + 8 new (5 web-sourced, 2 academic/arxiv, 1 internal research scan). Covers industry reports, academic papers, security disclosures, and practitioner analysis.",
        "badge_summary": "16 [E]videnced, 9 [I]nterpretation, 4 [J]udgment, 1 [A]ssumption",
        "evidence_note": "Mostly evidenced — this update tracks concrete developments (ClawHub malicious skills count, new arxiv papers, personnel moves) against the AR-001 baseline thesis.",
        "strongest": "ClawHavoc security disclosure (341 malicious skills, independently verifiable), AgentAuditor benchmark results (arxiv:2602.09341, peer-reviewable), Manus launch metrics (public product launch).",
        "weakest": "The net confidence adjustment (-2% from 73% to 71%) is a subjective synthesis, not a mathematical derivation. The weighting of positive vs. negative signals is judgment-based.",
        "invalidation": "If (a) the ClawHub malicious skills are shown to be benign misclassifications, (b) the AR-001 Trust Race Model is externally validated (raising confidence), or (c) new evidence fundamentally contradicts the capability-governance gap thesis.",
        "limitations": [
            "<strong>48-hour update window.</strong> This update covers developments within ~2 weeks of AR-001. Short time horizons amplify noise over signal.",
            "<strong>Confidence adjustment is subjective.</strong> The -2% revision (73% → 71%) reflects the author's judgment, not a formal methodology.",
            "<strong>Builds on AR-001's limitations.</strong> All limitations from the original report (no independent TCO data, benchmark-only multi-agent data, vendor-sponsored surveys) still apply.",
            "<strong>Security disclosure sourcing.</strong> The ClawHavoc/Koi Security findings have not been independently replicated at time of publication.",
            "<strong>Selection bias in updates.</strong> Only developments that affect the AR-001 thesis are covered; neutral developments are omitted.",
        ],
        "part1_before": '<!-- ==================== SECTION 1: WHAT CHANGED ==================== -->',
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "9",
        "has_how_to_read": False,
    },
    {
        "dir": "agent-security-2026",
        "id": "AR-037",
        "title": "AI Agent Security — Why Your Agent Infrastructure Is a Target",
        "confidence": 68,
        "confidence_label": "Medium",
        "sources_total": 14,
        "sources_desc": "14 sources: 4 security research/disclosures (ClawHavoc, Koi Security, Adversa AI, Obsidian Security), 3 industry reports (OWASP, Gartner, Precedence Research), 3 academic/technical (arxiv papers, NIST frameworks), 4 trade publications (TechRepublic, SecurityWeek, Forbes, DarkReading).",
        "badge_summary": "Claims classified throughout with section-level confidence scores (90%+, 80-89%, 70-79%, 60-69%)",
        "evidence_note": "Mixed evidence quality — threat examples are well-documented but attack surface projections and defensive recommendations involve significant interpretation and judgment.",
        "strongest": "ClawHub 341 malicious skills finding (primary security research), February 13 agent identity theft incident (documented disclosure), OWASP Top 10 for LLM Applications (established framework).",
        "weakest": "Defensive recommendations are largely judgment-based — no evidence that specific countermeasures reduce agent-specific attack success rates. Market size projections ($8.4B by 2032) are single-source estimates.",
        "invalidation": "If (a) agent security incidents remain rare despite growing deployment, (b) existing enterprise security frameworks prove sufficient for agent threats, or (c) the ClawHub attack vector is patched and no comparable vectors emerge.",
        "limitations": [
            "<strong>Threat landscape is rapidly evolving.</strong> Specific attack vectors and statistics may be outdated within weeks of publication.",
            "<strong>No controlled efficacy data for defenses.</strong> Recommended countermeasures are based on security best practices, not measured agent-specific effectiveness.",
            "<strong>Attacker capability is estimated, not measured.</strong> Projections of future attack sophistication are extrapolations, not empirical findings.",
            "<strong>Enterprise bias.</strong> Security recommendations assume organizational resources; solo operators and small teams face different threat models.",
            "<strong>Vendor-adjacent sourcing.</strong> Several security sources (Obsidian Security, Adversa AI) are vendors with commercial interests in the threat landscape they describe.",
        ],
        "part1_before": '<div class="page" id="exec-summary">',
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "10",
        "has_how_to_read": False,
    },
    {
        "dir": "ai-agent-costs-2026",
        "id": "AR-038",
        "title": "The Cost of AI Agents — What Nobody Talks About",
        "confidence": 70,
        "confidence_label": "Medium",
        "sources_total": 12,
        "sources_desc": "12 sources: 6 internal production data (API billing, token logs, cron execution records, sub-agent accuracy tracking, disk usage monitoring, Anthropic billing dashboard), 4 external references (Anthropic pricing documentation, industry cost benchmarks, competitor pricing), 2 analytical frameworks (TCO modeling, waste classification taxonomy).",
        "badge_summary": "10 [E]videnced, 12 [I]nterpretation, 16 [J]udgment, 1 [A]ssumption",
        "evidence_note": "Production data is strong but interpretations are extensive — the report extrapolates from one system's costs to general principles, and many recommendations are judgment calls.",
        "strongest": "Token usage logs and API billing (first-party, auditable), 44GB log file measurement (directly verifiable), per-cron cost breakdowns (production data with timestamps).",
        "weakest": "Generalization from single-system costs to industry-wide claims. The '20% sub-agent waste' finding is from one pipeline and may not represent typical deployments. Cost optimization recommendations lack controlled before/after measurement.",
        "invalidation": "If (a) API pricing drops make cost optimization irrelevant, (b) other production deployments show fundamentally different cost structures, or (c) the 'hidden costs' identified are already well-known in the practitioner community.",
        "limitations": [
            "<strong>Single production environment.</strong> All cost data comes from one AI agent stack (OpenClaw + Claude). Different architectures may have different cost profiles.",
            "<strong>Pricing snapshot.</strong> All costs reflect February 2026 Anthropic pricing. Rapid price changes could invalidate specific figures within months.",
            "<strong>Optimization recommendations untested at scale.</strong> Cost-saving strategies are proposed but not validated across diverse deployments.",
            "<strong>Hidden costs may be incomplete.</strong> The report identifies several overlooked costs but cannot claim exhaustiveness — unknown unknowns likely exist.",
            "<strong>Heavy judgment component.</strong> 16 of 39 classified claims are [J]udgment, meaning recommendations reflect values and priorities, not just evidence.",
        ],
        "part1_before": '<div class="page" id="s1">',
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "11",
        "has_how_to_read": False,
    },
    {
        "dir": "agent-evolution-2026",
        "id": "AR-040",
        "title": "AI Agent Evolution — What 100 Agents Taught Us About Self-Improvement",
        "confidence": 58,
        "confidence_label": "Medium-Low",
        "sources_total": 8,
        "sources_desc": "8 sources: 1 primary experiment (100 Claude agents, 10 groups, 222,000 characters of output), 3 theoretical frameworks (Donella Meadows system dynamics, OODA loop, emergence theory), 2 internal references (AGENTS.md, SYNTHESIS-v2), 2 external references (meta-learning literature, AI safety research).",
        "badge_summary": "3 [E]videnced, 3 [I]nterpretation, 3 [J]udgment, 3 [A]ssumption",
        "evidence_note": "Highly experimental and interpretive — the core findings (6 laws, 4 engines) are synthesized from AI-generated output, not validated against real-world agent improvement data.",
        "strongest": "The experiment itself is reproducible (100 agents, same prompt, documented methodology). Convergence patterns across independent agent groups provide internal consistency.",
        "weakest": "AI agents theorizing about AI agent improvement is inherently circular. The '6 laws' are a synthesis of what agents say about self-improvement, not measured effects of actual self-improvement. No validation against real agent performance metrics.",
        "invalidation": "If (a) the 6 laws are tested and show no correlation with actual agent improvement, (b) different model families produce fundamentally different convergence patterns, or (c) the 'laws' are shown to be artifacts of Claude's training data rather than genuine insights.",
        "limitations": [
            "<strong>Circular methodology.</strong> Asking AI agents how to improve AI agents may reflect training data biases rather than genuine insights about improvement.",
            "<strong>Single model family.</strong> All 100 agents were Claude instances. GPT-4, Gemini, or open-source models may converge on different principles.",
            "<strong>No empirical validation.</strong> The 6 laws and 4 engines have not been tested against measurable agent performance improvements.",
            "<strong>Emergence claims are interpretive.</strong> Whether agent groups truly 'converged' or simply drew from similar training distributions is an open question.",
            "<strong>Small effective sample.</strong> 10 groups of 10 agents each — group-level convergence with n=10 groups has limited statistical power.",
            "<strong>Framework originality risk.</strong> The 6 laws / 4 engines framework is entirely original and unvalidated by external researchers.",
        ],
        "part1_before": '<div class="page" id="exec-summary">',
        "part2_before": '<div class="back-cover">',
        "transparency_section_num": "11",
        "has_how_to_read": False,
    },
]

def make_part1(r):
    """Generate Confidence Framework HTML (Part 1)."""
    return f"""
<!-- ==================== HOW TO READ / CONFIDENCE FRAMEWORK ==================== -->
<div class="page" id="how-to-read">
  <h2>How to Read This Report</h2>

  <p>Every claim in this report carries a classification badge and confidence level. This is not decoration — it tells you how much weight to put on each statement.</p>

  <table class="how-to-read-table">
    <tr>
      <th>Badge</th>
      <th>Meaning</th>
    </tr>
    <tr>
      <td><span class="badge badge-e">E</span> Evidenced</td>
      <td>Backed by external, citable source(s) or verifiable first-party data</td>
    </tr>
    <tr>
      <td><span class="badge badge-i">I</span> Interpretation</td>
      <td>Reasoned inference from multiple sources</td>
    </tr>
    <tr>
      <td><span class="badge badge-j">J</span> Judgment</td>
      <td>Recommendation based on evidence + values</td>
    </tr>
    <tr>
      <td><span class="badge badge-a">A</span> Assumption</td>
      <td>Stated but not proven</td>
    </tr>
  </table>

  <table class="how-to-read-table" style="margin-top: 16px;">
    <tr>
      <th>Confidence</th>
      <th>Meaning</th>
    </tr>
    <tr>
      <td>High</td>
      <td>3+ independent sources, peer-reviewed or large-sample primary data</td>
    </tr>
    <tr>
      <td>Medium</td>
      <td>1–2 sources, plausible but not independently confirmed</td>
    </tr>
    <tr>
      <td>Low</td>
      <td>Single secondary source, methodology unclear, or extrapolated</td>
    </tr>
  </table>

  <p style="margin-top: 24px;"><strong>Overall Report Confidence ({r['confidence']}%):</strong> This score reflects a weighted assessment of three factors: (1) the strength of individual evidence — how many claims are [E]videnced vs. [I]nterpretation or [J]udgment, (2) source quality — diversity, recency, and independence of sources, and (3) framework originality — whether the report's central framework has been externally validated. {r['evidence_note']} The score is an honest signal, not a mathematical output.</p>

  <p style="margin-top: 16px;">This report was produced using a <strong>multi-agent research pipeline</strong>. Full methodology and limitations are in the Transparency Note (Section {r['transparency_section_num']}).</p>
</div>

"""


def make_part2(r):
    """Generate Transparency Note HTML (Part 2)."""
    limitations_html = "\n".join(f"    <li>{l}</li>" for l in r["limitations"])
    return f"""
<!-- ==================== TRANSPARENCY NOTE ==================== -->
<div class="page" id="transparency">
  <h2>{r['transparency_section_num']}. Transparency Note</h2>

  <p class="transparency-intro" style="font-style: italic; color: #666; margin-bottom: 24px;">This section provides full methodology, known limitations, and conflict of interest disclosure.</p>

  <table class="how-to-read-table">
    <tr>
      <td><strong>Overall Confidence</strong></td>
      <td>{r['confidence']}% ({r['confidence_label']}). Justification: {r['evidence_note']}</td>
    </tr>
    <tr>
      <td><strong>Sources</strong></td>
      <td>{r['sources_desc']}</td>
    </tr>
    <tr>
      <td><strong>Strongest Evidence</strong></td>
      <td>{r['strongest']}</td>
    </tr>
    <tr>
      <td><strong>Weakest Point</strong></td>
      <td>{r['weakest']}</td>
    </tr>
    <tr>
      <td><strong>What Would Invalidate</strong></td>
      <td>{r['invalidation']}</td>
    </tr>
  </table>

  <h3 style="margin-top: 2rem;">Methodology</h3>

  <p>This report followed the A+ Research Pipeline: independent research, source diversity audit, thesis development, and synthesis. {r['sources_total']} sources were collected and claims were extracted and classified using the [E]/[I]/[J]/[A] framework. The pipeline is a multi-agent system where research, validation, thesis development, and writing are performed by specialized agents that operate independently.</p>

  <h3>Limitations</h3>

  <ul>
{limitations_html}
  </ul>

  <h3>Conflict of Interest</h3>

  <p>The publisher of this report researches, builds, and advises on AI agent systems — and has a commercial interest in the conclusions presented here. Evaluate evidence independently; claims marked [J] reflect judgment, not evidence.</p>
</div>

"""


# Check if badge styles exist
def ensure_badge_styles(html):
    """Add badge styles if not present."""
    if ".badge-e" not in html:
        badge_css = """
  /* Evidence type badges */
  .badge { display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 0.7rem; font-weight: 700; color: #fff; vertical-align: middle; }
  .badge-e { background: #2d8a4e; }
  .badge-i { background: #2563eb; }
  .badge-j { background: #d97706; }
  .badge-a { background: #dc2626; }"""
        # Insert before closing </style>
        html = html.replace("</style>", badge_css + "\n</style>", 1)
    return html


for r in reports:
    filepath = f"{BASE}/{r['dir']}/index.html"
    with open(filepath, "r") as f:
        html = f.read()

    # Ensure badge styles
    html = ensure_badge_styles(html)

    # Insert Part 1 (before exec summary / first content section)
    if r.get("has_how_to_read"):
        # AR-033 already has a how-to-read, we need to augment it
        # Find the existing how-to-read section and add confidence framework after it
        # Actually, let's insert our version before exec-summary and the existing one will be replaced
        # Better: just add the confidence score + multi-agent note to existing how-to-read
        # Find end of existing how-to-read div
        pass  # Handle below
    
    part1 = make_part1(r)
    part2 = make_part2(r)

    if r.get("has_how_to_read"):
        # AR-033: already has how-to-read, just add confidence score paragraph before exec-summary
        confidence_addition = f"""
<!-- ==================== CONFIDENCE FRAMEWORK (added) ==================== -->
<div class="page" id="confidence-framework">
  <h2>Confidence Framework</h2>

  <table class="how-to-read-table" style="margin-top: 16px;">
    <tr>
      <th>Confidence</th>
      <th>Meaning</th>
    </tr>
    <tr>
      <td>High</td>
      <td>3+ independent sources, peer-reviewed or large-sample primary data</td>
    </tr>
    <tr>
      <td>Medium</td>
      <td>1–2 sources, plausible but not independently confirmed</td>
    </tr>
    <tr>
      <td>Low</td>
      <td>Single secondary source, methodology unclear, or extrapolated</td>
    </tr>
  </table>

  <p style="margin-top: 24px;"><strong>Overall Report Confidence ({r['confidence']}%):</strong> This score reflects a weighted assessment of three factors: (1) the strength of individual evidence — how many claims are [E]videnced vs. [I]nterpretation or [J]udgment, (2) source quality — diversity, recency, and independence of sources, and (3) framework originality — whether the report's central framework has been externally validated. {r['evidence_note']} The score is an honest signal, not a mathematical output.</p>

  <p style="margin-top: 16px;">This report was produced using a <strong>multi-agent research pipeline</strong>. Full methodology and limitations are in the Transparency Note (Section {r['transparency_section_num']}).</p>
</div>

"""
        html = html.replace(r["part1_before"], confidence_addition + r["part1_before"], 1)
    else:
        html = html.replace(r["part1_before"], part1 + r["part1_before"], 1)

    # Insert Part 2 before back-cover
    html = html.replace(r["part2_before"], part2 + r["part2_before"], 1)

    # Add TOC entry for Transparency Note if not present
    # We won't modify TOC to keep it simple - the sections are navigable by scrolling

    with open(filepath, "w") as f:
        f.write(html)

    print(f"✅ {r['id']} ({r['dir']}): confidence={r['confidence']}%, {r['sources_total']} sources")

print("\nDone! All 6 reports updated.")

"""
CV Generator — HOF Design Template
Generates customized CVs per fund from a single source of truth.
"""
import subprocess
from pathlib import Path

WORKSPACE = Path("/Users/florianziesche/.openclaw/workspace")
JOBS = WORKSPACE / "job-applications"

# ── Source of truth: Florian's CV data ──

CONTACT = {
    "name": "Florian Ziesche",
    "location": "New York, NY",
    "phone": "+1 347 740 1465",
    "email": "florian@ainaryventures.com",
    "linkedin": "https://linkedin.com/in/florianziesche",
    "website": "https://ainaryventures.com",
    "github": "https://github.com/florianziesche",
    "substack": "https://finitematter.substack.com",
}

EXPERIENCE = [
    {
        "title": "Operating Founder Advisor &amp; AI Consultant",
        "date": "2025 – Present",
        "company": '<a href="https://ainaryventures.com">Ainary Ventures</a> · U.S. &amp; Germany',
        "company_url": None,
        "bullets": [
            ("<strong>AI Agent Systems:</strong>", "Building open-source trust scoring framework for AI agents: calibration, self-evaluation, governance. Designing agent execution workflows with autonomous planning, memory, and end-to-end task completion."),
            ("<strong>Fundraising Advisory:</strong>", "Raised $300K in initial capital for an early-stage startup. Term sheet advisory, due diligence, data room preparation."),
            ("<strong>Go-to-Market:</strong>", "US market entry strategy and business plan coaching for international founders entering the American market."),
        ]
    },
    {
        "title": "VC Lab Fellow, Founder Institute",
        "date": "2026 – Present",
        "company": '<a href="https://decilegroup.com/">Decile Group</a>, Cohort 6 · New York',
        "company_url": None,
        "bullets": [
            ("<strong>Fund Thesis:</strong>", "AI-native companies + vertical AI. Core belief: agent capability is commoditizing fast. The winners build trust, governance, and compound systems. Thesis informed by building agent systems daily."),
            ("<strong>Deal Flow:</strong>", "Sourcing, screening, and conducting due diligence on early-stage AI startups. Portfolio construction modeling."),
        ]
    },
    {
        "title": "Co-Founder &amp; CEO | CRO",
        "date": "2019 – 2024",
        "company": '<a href="https://36zerovision.com">36ZERO Vision GmbH</a> · Munich, Germany',
        "company_url": None,
        "bullets": [
            ("<strong>Fundraising:</strong>", "Raised €3.5M equity (Pre-Seed &amp; Seed) from European and US investors plus €1.5M in non-dilutive grants. Managed 12+ institutional and angel investors."),
            ("<strong>AI Product:</strong>", "Led product from prototype to production-grade AI visual inspection system deployed on automotive production lines. Real-time inference, edge deployment, continuous learning."),
            ("<strong>Revenue Growth:</strong>", "Grew signed annual contract value from €240K to €1M+ within one year (327%). Maintained 9% monthly pipeline growth through enterprise sales motions."),
            ("<strong>Enterprise Sales:</strong>", "Closed BMW, Siemens, Bosch, Magna, Linamar. Built strategic partnerships with SAP, Bosch Rexroth, and Siemens for channel distribution."),
            ("<strong>Team &amp; Governance:</strong>", "Built international team from 0 to 15+. Board member. Drove enterprise compliance documentation and AI governance practices for customer onboarding (GDPR, data security)."),
        ]
    },
]

OTHER_EXP = "Deutschdata GmbH (AI Consulting, Co-Founder), BNP Paribas Consors Finanz (ML Risk Scoring), Celgene Corporation, BMW AG, BMW Canada."

EDUCATION = [
    {"degree": "M.Sc. &amp; B.Sc. Business Administration, Technology &amp; Management", "year": "2012 – 2019",
     "school": "Technical University of Munich (TUM)",
     "detail": 'Focus: Finance · Engineering / ML',
     "thesis": 'Thesis: "Human Interpretable ML for Risk Scoring at BNP Paribas Consors Finanz"'},
]

# ── Fund-specific customizations ──

FUND_CONFIG = {
    "_universal": {
        "subtitle": "AI Operator · Founder",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Built production-grade AI systems for manufacturing, navigated enterprise sales cycles, and led international teams. Now at the intersection of operating and investing: evaluating AI-native companies, supporting founders with hands-on experience, and building open-source tools for AI agent trust &amp; governance. German-born, built companies in Munich, based in New York.",
        "proficiencies": [
            ("AI/ML", "Computer Vision · LLMs &amp; Agentic AI · RAG · Edge AI · Trust &amp; Governance · MLOps"),
            ("Business", "Venture Creation (0 to 1) · Fundraising (€5M) · Enterprise GTM · Financial Modeling · Rapid Prototyping"),
            ("Venture", "Deal Sourcing · Due Diligence · Portfolio Support · Thesis Development"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "betaworks": {
        "subtitle": "AI Operator · Founder",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Now building agent systems: an open-source trust framework for AI agents (calibration, self-evaluation, governance) and designing agent execution workflows with autonomous planning, memory, and end-to-end task completion. German-born, built companies in Munich, based in New York.",
        "proficiencies": [
            ("AI/ML", "Agent Systems · LLMs &amp; Agentic AI · Self-Evaluation &amp; Trust Scoring · RAG · Computer Vision · Edge AI"),
            ("Fundraising", "€5M raised (Pre-Seed &amp; Seed) · IR · Due Diligence · Data Room · Term Sheets"),
            ("Business", "Venture Creation (0 to 1) · Enterprise Sales (BMW, Siemens, Bosch) · Financial Modeling · Rapid Prototyping"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "bloomberg-beta": {
        "subtitle": "AI-Native Operator — Bloomberg Beta",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Obsessed with how AI changes work: built production AI systems, navigated enterprise adoption cycles, and saw firsthand how teams integrate (or resist) AI tools. Now applying that lens to venture — evaluating how AI reshapes industries, supporting portfolio founders with operational depth, and building open-source tools for AI agent trust. German-born, built in Munich, based in New York.",
        "proficiencies": [
            ("AI/ML", "LLMs &amp; Agentic AI · Computer Vision · RAG · Human-AI Collaboration · Trust Frameworks"),
            ("Business", "Venture Creation (0 to 1) · Fundraising (€5M) · Enterprise GTM · Financial Modeling"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Venture", "Deal Sourcing · Due Diligence · Portfolio Support · Thesis Development"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "lux": {
        "subtitle": "AI Operator · Founder",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Hands-on operator who built production-grade AI systems for manufacturing, closed enterprise deals, and scaled teams internationally. Now bringing that operational experience to portfolio support: helping deep-tech founders navigate enterprise sales, fundraising, go-to-market, and AI governance. German-born, built companies in Munich, based in New York.",
        "proficiencies": [
            ("Portfolio Ops", "Enterprise GTM Strategy · Fundraising Support · Go-to-Market · Founder Coaching"),
            ("AI/ML", "Computer Vision · LLMs &amp; Agentic AI · Edge AI · MLOps · Trust &amp; Governance"),
            ("Business", "Venture Creation (0 to 1) · Fundraising (€5M) · Financial Modeling · Rapid Prototyping"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Manufacturing AI"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    # PRIMARY v1 "ECHT" — nur was heute wahr ist
    "primary": {
        "subtitle": "Operator-In-Residence: Agents, Primary",
        "summary": "Operator-founder. Built an AI company from zero to €1M+ ACV (BMW, Siemens, Bosch). €5M raised, team of 15. Now building full-time on agents: trust-as-a-currency framework, layered memory architecture, outcome-based execution UI. Testing emerging frameworks as they launch. Thinking in systems that compound. Based in New York.",
        "experience_override": [
            {
                "title": "Founder Operator &amp; Consultant",
                "date": "2025 – Present",
                "company": '<a href="https://ainaryventures.com">Ainary Ventures</a> · U.S. &amp; Germany',
                "company_url": None,
                "bullets": [
                    ("<strong>Consulting:</strong>", "Founder-operator advisory for German/US startups. Helped raise $700K, YC admission. Automated workflows. MVP."),
                    ("<strong>OS:</strong>", "Built on OpenClaw. 30+ tool integrations, layered memory, execution workflows. Anti-entropy rules, verified knowledge base. Flywheel UI combining OS + trust scoring + outcome tracking."),
                    ("<strong>Trust &amp; Evals:</strong>", "Trust-as-a-currency: confidence-scored outputs, threshold-based autonomy (own research). Testing and evaluating emerging agent frameworks."),
                ]
            },
            {
                "title": "VC Lab Fellow, Founder Institute",
                "date": "2026 – Present",
                "company": '<a href="https://decilegroup.com/">Decile Group</a>, Cohort 6 · New York',
                "company_url": None,
                "bullets": [
                    ("<strong>Fund Thesis:</strong>", "AI-native companies + vertical AI. Core belief: agent capability is commoditizing fast. The winners build trust, governance, and compound systems. Thesis informed by building agent systems daily."),
                    ("<strong>Deal Flow:</strong>", "Sourcing and evaluating early-stage AI startups. Due diligence, deal memos."),
                ]
            },
            {
                "title": "Co-Founder &amp; CEO | CRO",
                "date": "2019 – 2024",
                "company": '<a href="https://36zerovision.com">36ZERO Vision GmbH</a> · Munich, Germany',
                "company_url": None,
                "bullets": [
                    ("<strong>Fundraising:</strong>", "Raised €3.5M equity (Pre-Seed &amp; Seed) plus €1.5M non-dilutive grants. Managed 12+ institutional and angel investors."),
                    ("<strong>AI Product to Production:</strong>", "Led product from prototype to production-grade AI visual inspection on automotive lines. Real-time inference, edge deployment, continuous learning. Shipped to BMW, Siemens, Bosch."),
                    ("<strong>Revenue &amp; GTM:</strong>", "Grew ACV from €240K to €1M+ in one year (327%). Built channel partnerships (SAP, Bosch Rexroth, Siemens)."),
                    ("<strong>Tech to Company:</strong>", "Translated prototype into production-grade product and venture-scale business. Built international team from 0 to 15+."),
                ]
            },
        ],
        "proficiencies": [
            ("Agents", "OpenClaw · Trust-Scored Autonomy · Compound Memory Architecture · Agent Self-Evaluation"),
            ("AI/ML", "LLMs · Agent Evals &amp; Benchmarks · RAG · Embeddings · Computer Vision · Prompt Engineering"),
            ("Operator", "Venture Creation (0 to 1) · Enterprise Sales (0 to 1) · Team Building (0 to 15) · Fundraising (€5M) · Rapid Prototyping"),
            ("Technology", "Python · LangChain · FastAPI · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    # PRIMARY v2 "MORGEN" — nach Ollama/LM Studio testing
    "primary-v2": {
        "subtitle": "Operator-In-Residence: Agents, Primary",
        "summary": "Operator-founder. Built an AI company from zero to BMW, Siemens, Bosch (€5M raised, 15 people). Now building full-time on agents: compound execution OS on OpenClaw, trust-as-a-currency framework, outcome-based flywheel UI. Benchmarking local models (Ollama, LM Studio) vs. cloud APIs on Apple Silicon. Running daily experiments. Based in New York.",
        "experience_override": [
            {
                "title": "Founder Operator &amp; Consultant",
                "date": "2025 – Present",
                "company": '<a href="https://ainaryventures.com">Ainary Ventures</a> · U.S. &amp; Germany',
                "company_url": None,
                "bullets": [
                    ("<strong>Consulting:</strong>", "Founder-operator advisory for German/US startups. Helped raise $700K, YC admission. Automated workflows. MVP."),
                    ("<strong>OS:</strong>", "Running OpenClaw as compound execution layer — multi-device (Mac, iPhone), 30+ tool integrations, persistent memory, autonomous task orchestration. Built on top: CV generation system, research pipelines, real-time WebSocket dashboards."),
                    ("<strong>Local AI &amp; Evals:</strong>", "Running Ollama and LM Studio on Apple Silicon. Benchmarking local models vs. cloud APIs for agent task completion — latency, quality, cost. Building open-source agent trust framework: confidence scoring, self-evaluation, outcome tracking."),
                    ("<strong>Execution:</strong>", "Building execution workflows where every task makes the next one better — memory that persists, connections that compound, research that feeds content that feeds revenue. Outcome-based, not tool-based."),
                ]
            },
            {
                "title": "VC Lab Fellow, Founder Institute",
                "date": "2026 – Present",
                "company": '<a href="https://decilegroup.com/">Decile Group</a>, Cohort 6 · New York',
                "company_url": None,
                "bullets": [
                    ("<strong>Fund Thesis:</strong>", "AI-native companies + vertical AI. Core belief: agent capability is commoditizing fast. The winners build trust, governance, and compound systems. Thesis informed by building agent systems daily."),
                    ("<strong>Deal Flow:</strong>", "Sourcing and evaluating early-stage AI startups. Due diligence, deal memos."),
                ]
            },
            {
                "title": "Co-Founder &amp; CEO | CRO",
                "date": "2019 – 2024",
                "company": '<a href="https://36zerovision.com">36ZERO Vision GmbH</a> · Munich, Germany',
                "company_url": None,
                "bullets": [
                    ("<strong>Fundraising:</strong>", "Raised €3.5M equity (Pre-Seed &amp; Seed) plus €1.5M non-dilutive grants. Managed 12+ institutional and angel investors."),
                    ("<strong>AI Product to Production:</strong>", "Led product from prototype to production-grade AI visual inspection on automotive lines. Real-time inference, edge deployment, continuous learning. Shipped to BMW, Siemens, Bosch."),
                    ("<strong>Revenue &amp; GTM:</strong>", "Grew ACV from €240K to €1M+ in one year (327%). Built channel partnerships (SAP, Bosch Rexroth, Siemens)."),
                    ("<strong>Tech to Company:</strong>", "Translated prototype into production-grade product and venture-scale business. Built international team from 0 to 15+."),
                ]
            },
        ],
        "proficiencies": [
            ("Agents", "OpenClaw · Ollama · LM Studio · Trust-Scored Autonomy · Compound Memory · Agent Self-Evaluation"),
            ("AI/ML", "LLMs · Agent Evals &amp; Benchmarks · RAG · Embeddings · Computer Vision · Prompt Engineering · Apple Silicon"),
            ("Operator", "Venture Creation (0 to 1) · Enterprise Sales (0 to 1) · Team Building (0 to 15) · Fundraising (€5M) · Rapid Prototyping"),
            ("Technology", "Python · LangChain · FastAPI · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "futuresight": {
        "subtitle": "Founding CEO — FutureSight",
        "summary": "Five years as CEO of an AI startup — from zero to BMW, Siemens, Bosch. €5M raised, €1M+ ACV, 327% revenue growth. Built the GTM engine from first cold call to enterprise partnerships. Now building AI agent systems for trust &amp; governance — ready to take a validated problem, ship V1, win customers, and raise the seed.",
        "proficiencies": [
            ("GTM", "Enterprise Sales (BMW, Siemens, Bosch) · Channel Partnerships · Pricing &amp; Packaging · Pipeline Growth (9% MoM)"),
            ("AI/ML", "LLMs &amp; Agentic AI · Computer Vision · RAG · Production AI Deployment · Edge &amp; Cloud"),
            ("Founder", "0 to 1 Company Building · Fundraising (€5M) · Team Building (0 to 15) · Rapid Prototyping"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "glasswing": {
        "subtitle": "AI-Native Operator — Glasswing Ventures",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Built production-grade AI systems for manufacturing, navigated enterprise sales cycles, and led technical teams. Now applying that operator lens to venture: evaluating AI infrastructure deals, supporting portfolio companies from the trenches, and building open-source tools for AI agent trust &amp; governance. German-born, built companies in Munich, based in New York.",
        "proficiencies": [
            ("AI/ML", "Computer Vision · LLMs &amp; Agentic AI · RAG · Trust &amp; Governance Frameworks · Edge AI · MLOps"),
            ("Business", "Venture Creation (0 to 1) · Fundraising (€5M) · Enterprise GTM · Financial Modeling · Rapid Prototyping"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Vibe Coding (Claude, Cursor)"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
    "ibm-ventures": {
        "subtitle": "Venture Principal — IBM Ventures",
        "summary": "Five years building an AI startup from zero to BMW, Siemens, Bosch — €5M raised, €1M+ ACV. Built production-grade AI systems integrated with enterprise IT stacks (SAP, Siemens MindSphere). Deep understanding of how large enterprises evaluate, procure, and deploy AI — from proof-of-concept to production. Now applying that enterprise AI operator perspective to venture: evaluating AI infrastructure and vertical AI deals, and helping portfolio companies land enterprise customers. German-born, built in Munich, based in New York.",
        "proficiencies": [
            ("Enterprise AI", "Computer Vision · LLMs · Edge AI · MLOps · Enterprise Integration (SAP, Siemens)"),
            ("Business", "Venture Creation (0 to 1) · Fundraising (€5M) · Enterprise Sales (BMW, Siemens, Bosch)"),
            ("Venture", "Deal Sourcing · Technical Due Diligence · Portfolio Support · Thesis Development"),
            ("Technology", "Python · LangChain · Cloud (AWS, GCP) · CI/CD · Manufacturing AI"),
            ("Affiliations", "Alchemist Accelerator · VC Lab (Decile Group) · UnternehmerTUM"),
            ("Languages", "German (native) · English (fluent)"),
        ],
        "footer": "Florian Ziesche · February 2026",
    },
}


def generate_cv_html(fund_id: str) -> str:
    """Generate a complete CV HTML for a specific fund."""
    cfg = FUND_CONFIG.get(fund_id, FUND_CONFIG["_universal"])
    
    c = CONTACT
    
    # Build experience HTML (fund can override)
    exp_html = ""
    roles = cfg.get("experience_override", EXPERIENCE)
    for role in roles:
        bullets = "\n".join(f'      <li>{b[0]} {b[1]}</li>' for b in role["bullets"])
        company_line = f'<a href="{role["company_url"]}">{role["company"]}</a>' if role.get("company_url") else role["company"]
        exp_html += f"""
  <div class="role">
    <div class="role-header">
      <span class="role-title">{role["title"]}</span>
      <span class="role-date">{role["date"]}</span>
    </div>
    <div class="role-company">{company_line}</div>
    <ul class="role-bullets">
{bullets}
    </ul>
  </div>"""
    
    # Build education HTML
    edu_html = ""
    for edu in EDUCATION:
        edu_html += f"""
  <div class="edu-block">
    <div class="edu-header">
      <span class="edu-degree">{edu["degree"]}</span>
      <span class="edu-year">{edu["year"]}</span>
    </div>
    <div class="edu-school">{edu["school"]}</div>
    <div class="edu-focus">{edu["detail"]}</div>
    <div class="edu-detail">{edu.get("thesis","")}</div>
  </div>"""
    
    # Build proficiencies
    prof_html = ""
    for label, value in cfg["proficiencies"]:
        prof_html += f"""
    <span class="prof-label">{label}</span>
    <span class="prof-value">{value}</span>"""
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Florian Ziesche — CV</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
  *{{margin:0;padding:0;box-sizing:border-box}}
  @page{{size:A4;margin:0}}
  body{{font-family:'Inter',-apple-system,sans-serif;font-size:9.5pt;line-height:1.45;color:#1a1a1a;background:white;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .page{{width:210mm;min-height:297mm;max-height:297mm;overflow:hidden;padding:18mm 22mm 15mm 22mm;margin:0 auto;}}
  .header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;padding-bottom:10px;border-bottom:2px solid #1a1a1a}}
  .header-left h1{{font-size:22pt;font-weight:700;letter-spacing:-0.5px;margin-bottom:2px}}
  .header-left .subtitle{{font-size:9.5pt;font-weight:500;color:#444;letter-spacing:0.8px;text-transform:uppercase}}
  .header-right{{text-align:right;font-size:8.5pt;color:#444;line-height:1.6}}
  .header-right a{{color:#2563eb;text-decoration:none}}
  .summary{{font-size:9pt;color:#333;margin:10px 0 8px 0;line-height:1.5;padding:8px 12px;background:#f8f8f8;border-left:3px solid #c8aa50;text-align:justify;hyphens:auto;-webkit-hyphens:auto}}
  .section-title{{font-size:9pt;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#1a1a1a;margin-top:14px;margin-bottom:6px;padding-bottom:3px;border-bottom:1px solid #ddd}}
  .role{{margin-bottom:0}}
  .role-header{{display:flex;justify-content:space-between;align-items:baseline}}
  .role-title{{font-size:10pt;font-weight:600}}
  .role-date{{font-size:8.5pt;font-weight:500;color:#555;white-space:nowrap}}
  .role-company{{font-size:8.5pt;color:#666;font-style:italic;margin-bottom:3px}}
  .role-company a{{color:#2563eb;text-decoration:none}}
  .role-bullets{{padding-left:16px;font-size:9pt}}
  .role-bullets li{{margin-bottom:2px;color:#2a2a2a;text-align:justify;hyphens:auto;-webkit-hyphens:auto}}
  .role-bullets li strong{{font-weight:600}}
  .other-exp{{font-size:8.5pt;color:#666;margin-top:8px;padding-top:6px;border-top:1px solid #eee}}
  .edu-block{{margin-bottom:4px}}
  .edu-header{{display:flex;justify-content:space-between;align-items:baseline}}
  .edu-degree{{font-size:9.5pt;font-weight:600}}
  .edu-year{{font-size:8.5pt;color:#555}}
  .edu-school{{font-size:8.5pt;color:#444}}
  .edu-focus{{font-size:8.5pt;color:#555}}
  .edu-detail{{font-size:8.5pt;color:#555;font-style:italic}}
  .prof-grid{{display:grid;grid-template-columns:95px 1fr;gap:6px 12px;font-size:8.5pt;margin-bottom:0}}
  .prof-label{{font-weight:600;color:#333}}
  .prof-value{{color:#2a2a2a}}
  .footer-line{{font-size:8pt;color:#555;margin-top:6px;padding-top:5px;border-top:1px solid #ddd;display:flex;justify-content:space-between}}
  @media print{{body{{background:white}}.page{{box-shadow:none}}}}
  @media screen{{.page{{box-shadow:0 0 20px rgba(0,0,0,0.1);margin:20px auto}}}}
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="header-left">
      <h1>{c["name"]}</h1>
      <div class="subtitle">{cfg["subtitle"]}</div>
    </div>
    <div class="header-right">
      {c["location"]} · {c["phone"]}<br>
      <a href="mailto:{c["email"]}">{c["email"]}</a><br>
      <a href="{c["linkedin"]}">LinkedIn</a> · 
      <a href="{c["github"]}">GitHub</a> · 
      <a href="{c["website"]}">Ainary</a>
    </div>
  </div>
  
  <div class="summary">{cfg["summary"]}</div>
  
  <div class="section-title">Experience</div>
  {exp_html}
  
  <div class="other-exp">
    <strong>Other Experience:</strong> {OTHER_EXP}
  </div>
  
  <div class="section-title">Education</div>
  {edu_html}
  
  <div class="section-title">Proficiencies</div>
  <div class="prof-grid">{prof_html}
  </div>

  <div class="footer-line">
    <span>{cfg["footer"]}</span>
  </div>
</div>
</body>
</html>"""


def generate_cv(fund_id: str) -> dict:
    """Generate CV HTML + PDF for a fund. Returns paths."""
    cfg = FUND_CONFIG.get(fund_id, FUND_CONFIG["_universal"])
    
    # Determine output dir
    fund_dir = JOBS / fund_id
    fund_dir.mkdir(parents=True, exist_ok=True)
    
    html_path = fund_dir / f"CV_{fund_id}_Ziesche.html"
    pdf_path = fund_dir / "CV.pdf"
    
    # Generate HTML
    html = generate_cv_html(fund_id)
    html_path.write_text(html)
    
    # Generate PDF via Chrome headless
    try:
        result = subprocess.run([
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless", "--disable-gpu", "--no-margins",
            f"--print-to-pdf={pdf_path}",
            f"file://{html_path}"
        ], capture_output=True, text=True, timeout=30)
        
        if pdf_path.exists():
            size = pdf_path.stat().st_size
            return {
                "status": "ok",
                "html": str(html_path.relative_to(WORKSPACE)),
                "pdf": str(pdf_path.relative_to(WORKSPACE)),
                "size": size,
                "fund": fund_id,
                "subtitle": cfg["subtitle"],
            }
        else:
            return {"error": f"PDF generation failed: {result.stderr[:200]}"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import sys
    fund = sys.argv[1] if len(sys.argv) > 1 else "betaworks"
    result = generate_cv(fund)
    print(result)

"""
DepoDigest Pro - LLM Prompts
Carefully engineered prompts for deposition analysis
"""

SYSTEM_PROMPT = """You are DepoDigest Pro, an expert legal AI assistant specialized in analyzing deposition transcripts for personal injury litigation. 

Your analysis must be:
1. PRECISE - Always cite page and line numbers
2. ACTIONABLE - Focus on what matters for trial preparation
3. STRATEGIC - Identify leverage points for settlement negotiations
4. THOROUGH - Don't miss any significant admissions or contradictions

You are analyzing depositions primarily for PLAINTIFF attorneys in personal injury cases. Your goal is to help them build the strongest possible case by identifying:
- Admissions of liability, negligence, or fault
- Evidence supporting damages claims
- Credibility issues with defense witnesses
- Contradictions that can be exploited at trial
- Settlement value indicators

Always maintain objectivity in your analysis while focusing on elements favorable to the plaintiff's case."""


EXTRACTION_PROMPT = """Analyze this deposition transcript and extract the following information in JSON format:

TRANSCRIPT:
{transcript}

Provide a JSON response with this exact structure:
{{
    "case_info": {{
        "case_name": "Plaintiff v. Defendant(s)",
        "case_number": "extracted from transcript",
        "deposition_date": "YYYY-MM-DD format",
        "witness_name": "full name",
        "witness_role": "defendant/plaintiff/expert/fact_witness"
    }},
    "executive_summary": "2-3 paragraph summary of the most important takeaways for trial preparation",
    "narrative_summary": "Detailed chronological narrative of the testimony (500-800 words)",
    "key_admissions": [
        {{
            "quote": "exact quote from transcript",
            "type": "liability|damages|negligence|causation|credibility",
            "severity": "critical|significant|moderate|minor",
            "page": number,
            "line_start": number,
            "line_end": number,
            "context": "what was being discussed",
            "impeachment_value": "why this matters for cross-exam or settlement"
        }}
    ],
    "timeline": [
        {{
            "date": "YYYY-MM-DD or description",
            "time": "HH:MM or null",
            "description": "what happened",
            "page": number,
            "line_start": number,
            "line_end": number,
            "significance": "why this matters"
        }}
    ],
    "contradictions": [
        {{
            "statement_1": "first statement",
            "statement_1_page": number,
            "statement_1_line_start": number,
            "statement_1_line_end": number,
            "statement_2": "contradicting statement",
            "statement_2_page": number,
            "statement_2_line_start": number,
            "statement_2_line_end": number,
            "explanation": "how these contradict",
            "severity": "critical|significant|moderate|minor"
        }}
    ],
    "witness_assessment": {{
        "credibility": "assessment of witness credibility with reasoning",
        "demeanor": "notes on how witness responded to difficult questions",
        "weaknesses": ["list of exploitable weaknesses"],
        "strengths": ["aspects that help the defense"]
    }}
}}

Be thorough and identify ALL significant admissions and contradictions. Focus on elements that affect liability and damages."""


SETTLEMENT_IMPACT_PROMPT = """Based on this deposition analysis, assess the impact on settlement value:

CASE SUMMARY:
{case_summary}

KEY ADMISSIONS:
{admissions}

CONTRADICTIONS:
{contradictions}

Provide a JSON response:
{{
    "overall_score": <1-100, where 100 = extremely strong for plaintiff>,
    "liability_strength": <1-100>,
    "damages_support": <1-100>,
    "credibility_issues": <1-100, higher = more problems for defense witness>,
    "key_factors": [
        "List the 3-5 most important factors affecting settlement value"
    ],
    "settlement_range_adjustment": "<percentage adjustment, e.g., '+20-30%'>",
    "reasoning": "Detailed explanation of how this testimony affects case value (200-300 words)"
}}

Consider:
- Strength of liability admissions
- Whether defendant acknowledged negligent conduct
- Credibility damage from contradictions
- Emotional impact of remorseful statements
- Documentary evidence corroborating plaintiff's theory"""


CROSS_EXAM_PROMPT = """Generate cross-examination questions based on this deposition testimony:

KEY ADMISSIONS:
{admissions}

CONTRADICTIONS:
{contradictions}

WITNESS WEAKNESSES:
{weaknesses}

For each significant finding, provide strategic cross-examination questions in JSON format:
{{
    "questions": [
        {{
            "question": "The exact question to ask",
            "purpose": "What you're trying to establish",
            "based_on_page": number,
            "based_on_line": number,
            "follow_up_if_admits": "Next question if witness admits",
            "follow_up_if_denies": "How to impeach if witness denies"
        }}
    ],
    "impeachment_points": [
        "Bullet points summarizing key impeachment opportunities"
    ],
    "recommended_sequence": "Strategic advice on order of questioning"
}}

Questions should be:
1. Leading (answerable with yes/no)
2. Built on established facts from the deposition
3. Designed to box the witness in
4. Ready with impeachment if witness changes story"""


COMPARISON_PROMPT = """Compare these two depositions to identify contradictions between witnesses:

DEPOSITION 1 ({witness1}):
{depo1_summary}

Key Statements:
{depo1_statements}

DEPOSITION 2 ({witness2}):
{depo2_summary}

Key Statements:
{depo2_statements}

Identify all contradictions between the witnesses:
{{
    "cross_deposition_contradictions": [
        {{
            "topic": "subject matter of contradiction",
            "witness_1_statement": "what witness 1 said",
            "witness_1_reference": "page/line",
            "witness_2_statement": "what witness 2 said",
            "witness_2_reference": "page/line",
            "significance": "why this contradiction matters",
            "exploitation_strategy": "how to use this at trial"
        }}
    ],
    "corroborating_statements": [
        "Statements where witnesses agree (useful for establishing facts)"
    ],
    "credibility_comparison": "Which witness is more credible and why",
    "strategic_implications": "How these contradictions affect the case"
}}"""

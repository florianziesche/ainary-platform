#!/usr/bin/env python3
"""
DepoDigest Pro - Core Analysis Engine
Processes deposition transcripts using Claude API
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

try:
    import anthropic
except ImportError:
    print("Installing anthropic package...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "anthropic", "-q"])
    import anthropic

from models import (
    DepositionAnalysis, WitnessSummary, KeyAdmission, TimelineEvent,
    Contradiction, CrossExamQuestion, SettlementImpact, PageLineRef,
    AdmissionType, SeverityLevel
)
from prompts import SYSTEM_PROMPT, EXTRACTION_PROMPT, SETTLEMENT_IMPACT_PROMPT, CROSS_EXAM_PROMPT


class DepoDigestAnalyzer:
    """Main analysis engine for DepoDigest Pro"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found. Set environment variable or pass api_key.")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-20250514"
    
    def _call_claude(self, prompt: str, system: str = SYSTEM_PROMPT) -> str:
        """Make API call to Claude"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=8192,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Extract JSON from Claude's response"""
        # Try to find JSON in the response
        try:
            # First try direct parsing
            return json.loads(response)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown code block
            import re
            json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(1))
            
            # Try to find JSON object directly
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response[start:end])
            
            raise ValueError(f"Could not parse JSON from response: {response[:500]}...")
    
    def analyze_deposition(self, transcript: str) -> DepositionAnalysis:
        """
        Main analysis pipeline for a deposition transcript
        
        Args:
            transcript: Full text of the deposition transcript
            
        Returns:
            DepositionAnalysis object with complete analysis
        """
        print("Starting deposition analysis...")
        
        # Step 1: Extract core information
        print("  [1/3] Extracting testimony data...")
        extraction_prompt = EXTRACTION_PROMPT.format(transcript=transcript)
        extraction_response = self._call_claude(extraction_prompt)
        extracted = self._parse_json_response(extraction_response)
        
        # Step 2: Assess settlement impact
        print("  [2/3] Analyzing settlement impact...")
        settlement_prompt = SETTLEMENT_IMPACT_PROMPT.format(
            case_summary=extracted.get("executive_summary", ""),
            admissions=json.dumps(extracted.get("key_admissions", []), indent=2),
            contradictions=json.dumps(extracted.get("contradictions", []), indent=2)
        )
        settlement_response = self._call_claude(settlement_prompt)
        settlement_data = self._parse_json_response(settlement_response)
        
        # Step 3: Generate cross-exam questions
        print("  [3/3] Generating cross-examination strategy...")
        cross_exam_prompt = CROSS_EXAM_PROMPT.format(
            admissions=json.dumps(extracted.get("key_admissions", []), indent=2),
            contradictions=json.dumps(extracted.get("contradictions", []), indent=2),
            weaknesses=json.dumps(extracted.get("witness_assessment", {}).get("weaknesses", []), indent=2)
        )
        cross_exam_response = self._call_claude(cross_exam_prompt)
        cross_exam_data = self._parse_json_response(cross_exam_response)
        
        # Build the analysis object
        analysis = self._build_analysis(extracted, settlement_data, cross_exam_data)
        
        print("Analysis complete!")
        return analysis
    
    def _build_analysis(
        self, 
        extracted: Dict, 
        settlement: Dict, 
        cross_exam: Dict
    ) -> DepositionAnalysis:
        """Build DepositionAnalysis from raw API responses"""
        
        case_info = extracted.get("case_info", {})
        witness_data = extracted.get("witness_assessment", {})
        
        # Build witness summary
        witness = WitnessSummary(
            name=case_info.get("witness_name", "Unknown"),
            role=case_info.get("witness_role", "unknown"),
            credibility_assessment=witness_data.get("credibility", ""),
            demeanor_notes=witness_data.get("demeanor", ""),
            key_weaknesses=witness_data.get("weaknesses", []),
            key_strengths=witness_data.get("strengths", [])
        )
        
        # Build key admissions
        admissions = []
        for a in extracted.get("key_admissions", []):
            try:
                admissions.append(KeyAdmission(
                    quote=a.get("quote", ""),
                    admission_type=AdmissionType(a.get("type", "liability")),
                    severity=SeverityLevel(a.get("severity", "moderate")),
                    reference=PageLineRef(
                        page=a.get("page", 0),
                        line_start=a.get("line_start", 0),
                        line_end=a.get("line_end", 0)
                    ),
                    context=a.get("context", ""),
                    impeachment_value=a.get("impeachment_value", "")
                ))
            except (ValueError, KeyError) as e:
                print(f"  Warning: Skipping malformed admission: {e}")
        
        # Build timeline
        timeline = []
        for t in extracted.get("timeline", []):
            try:
                timeline.append(TimelineEvent(
                    date=t.get("date", ""),
                    time=t.get("time"),
                    description=t.get("description", ""),
                    reference=PageLineRef(
                        page=t.get("page", 0),
                        line_start=t.get("line_start", 0),
                        line_end=t.get("line_end", 0)
                    ),
                    significance=t.get("significance", "")
                ))
            except (ValueError, KeyError) as e:
                print(f"  Warning: Skipping malformed timeline event: {e}")
        
        # Build contradictions
        contradictions = []
        for c in extracted.get("contradictions", []):
            try:
                contradictions.append(Contradiction(
                    statement_1=c.get("statement_1", ""),
                    statement_1_ref=PageLineRef(
                        page=c.get("statement_1_page", 0),
                        line_start=c.get("statement_1_line_start", 0),
                        line_end=c.get("statement_1_line_end", 0)
                    ),
                    statement_2=c.get("statement_2", ""),
                    statement_2_ref=PageLineRef(
                        page=c.get("statement_2_page", 0),
                        line_start=c.get("statement_2_line_start", 0),
                        line_end=c.get("statement_2_line_end", 0)
                    ),
                    explanation=c.get("explanation", ""),
                    severity=SeverityLevel(c.get("severity", "moderate"))
                ))
            except (ValueError, KeyError) as e:
                print(f"  Warning: Skipping malformed contradiction: {e}")
        
        # Build cross-exam questions
        questions = []
        for q in cross_exam.get("questions", []):
            try:
                questions.append(CrossExamQuestion(
                    question=q.get("question", ""),
                    purpose=q.get("purpose", ""),
                    based_on=PageLineRef(
                        page=q.get("based_on_page", 0),
                        line_start=q.get("based_on_line", 0),
                        line_end=q.get("based_on_line", 0)
                    ),
                    follow_up_if_admits=q.get("follow_up_if_admits", ""),
                    follow_up_if_denies=q.get("follow_up_if_denies", "")
                ))
            except (ValueError, KeyError) as e:
                print(f"  Warning: Skipping malformed question: {e}")
        
        # Build settlement impact
        settlement_impact = SettlementImpact(
            overall_score=settlement.get("overall_score", 50),
            liability_strength=settlement.get("liability_strength", 50),
            damages_support=settlement.get("damages_support", 50),
            credibility_issues=settlement.get("credibility_issues", 50),
            key_factors=settlement.get("key_factors", []),
            settlement_range_adjustment=settlement.get("settlement_range_adjustment", "0%"),
            reasoning=settlement.get("reasoning", "")
        )
        
        # Build final analysis
        return DepositionAnalysis(
            case_name=case_info.get("case_name", "Unknown Case"),
            case_number=case_info.get("case_number", "Unknown"),
            deposition_date=case_info.get("deposition_date", ""),
            witness=witness,
            executive_summary=extracted.get("executive_summary", ""),
            narrative_summary=extracted.get("narrative_summary", ""),
            key_admissions=admissions,
            timeline=timeline,
            contradictions=contradictions,
            cross_exam_questions=questions,
            impeachment_points=cross_exam.get("impeachment_points", []),
            settlement_impact=settlement_impact
        )
    
    def analyze_file(self, filepath: str) -> DepositionAnalysis:
        """Analyze a deposition from a file"""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        transcript = path.read_text(encoding='utf-8')
        return self.analyze_deposition(transcript)
    
    def save_analysis(self, analysis: DepositionAnalysis, output_path: str):
        """Save analysis to JSON file"""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(analysis.to_json(), encoding='utf-8')
        print(f"Analysis saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="DepoDigest Pro - Deposition Analysis Engine")
    parser.add_argument("transcript", help="Path to deposition transcript file")
    parser.add_argument("-o", "--output", help="Output JSON file path", default=None)
    parser.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY)", default=None)
    
    args = parser.parse_args()
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        input_path = Path(args.transcript)
        output_path = input_path.parent / f"{input_path.stem}_analysis.json"
    
    # Run analysis
    try:
        analyzer = DepoDigestAnalyzer(api_key=args.api_key)
        analysis = analyzer.analyze_file(args.transcript)
        analyzer.save_analysis(analysis, str(output_path))
        
        # Print summary
        print("\n" + "="*60)
        print("ANALYSIS SUMMARY")
        print("="*60)
        print(f"Case: {analysis.case_name}")
        print(f"Witness: {analysis.witness.name} ({analysis.witness.role})")
        print(f"Key Admissions: {len(analysis.key_admissions)}")
        print(f"Contradictions: {len(analysis.contradictions)}")
        print(f"Settlement Impact Score: {analysis.settlement_impact.overall_score}/100")
        print(f"Settlement Adjustment: {analysis.settlement_impact.settlement_range_adjustment}")
        print("="*60)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

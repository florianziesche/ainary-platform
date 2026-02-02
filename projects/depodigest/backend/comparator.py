#!/usr/bin/env python3
"""
DepoDigest Pro - Multi-Deposition Comparator
Compares testimony across multiple depositions to find contradictions and corroborations
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

try:
    import anthropic
except ImportError:
    print("anthropic package required. Run: pip install anthropic")
    sys.exit(1)

from prompts import SYSTEM_PROMPT, COMPARISON_PROMPT


@dataclass
class CrossDepoContradiction:
    """Contradiction between two different witnesses"""
    topic: str
    witness_1_name: str
    witness_1_statement: str
    witness_1_reference: str
    witness_2_name: str
    witness_2_statement: str
    witness_2_reference: str
    significance: str
    exploitation_strategy: str
    severity: str  # critical, significant, moderate
    
    def to_dict(self):
        return {
            "topic": self.topic,
            "witness_1": {
                "name": self.witness_1_name,
                "statement": self.witness_1_statement,
                "reference": self.witness_1_reference
            },
            "witness_2": {
                "name": self.witness_2_name,
                "statement": self.witness_2_statement,
                "reference": self.witness_2_reference
            },
            "significance": self.significance,
            "exploitation_strategy": self.exploitation_strategy,
            "severity": self.severity
        }


@dataclass
class Corroboration:
    """Statement corroborated by multiple witnesses"""
    topic: str
    fact_established: str
    witnesses: List[Dict[str, str]]  # [{name, statement, reference}]
    strength: str  # strong, moderate, weak
    trial_value: str
    
    def to_dict(self):
        return {
            "topic": self.topic,
            "fact_established": self.fact_established,
            "witnesses": self.witnesses,
            "strength": self.strength,
            "trial_value": self.trial_value
        }


@dataclass
class WitnessCredibilityComparison:
    """Comparison of credibility between witnesses"""
    more_credible: str
    less_credible: str
    reasoning: str
    factors: List[str]
    
    def to_dict(self):
        return {
            "more_credible": self.more_credible,
            "less_credible": self.less_credible,
            "reasoning": self.reasoning,
            "factors": self.factors
        }


@dataclass
class MultiDepositionAnalysis:
    """Complete multi-deposition comparison analysis"""
    case_name: str
    case_number: str
    depositions_compared: List[Dict[str, str]]  # [{witness_name, date, role}]
    
    # Key findings
    contradictions: List[CrossDepoContradiction]
    corroborations: List[Corroboration]
    credibility_comparison: WitnessCredibilityComparison
    
    # Strategic recommendations
    recommended_witness_order: List[str]
    key_impeachment_opportunities: List[str]
    strategic_summary: str
    
    # Metadata
    analyzed_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self):
        return {
            "metadata": {
                "case_name": self.case_name,
                "case_number": self.case_number,
                "analyzed_at": self.analyzed_at,
                "depositions_compared": self.depositions_compared
            },
            "contradictions": [c.to_dict() for c in self.contradictions],
            "corroborations": [c.to_dict() for c in self.corroborations],
            "credibility_comparison": self.credibility_comparison.to_dict(),
            "recommended_witness_order": self.recommended_witness_order,
            "key_impeachment_opportunities": self.key_impeachment_opportunities,
            "strategic_summary": self.strategic_summary
        }
    
    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent)


class MultiDepositionComparator:
    """Compares multiple depositions for contradictions and corroborations"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-20250514"
    
    def _call_claude(self, prompt: str) -> str:
        """Make API call to Claude"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
    def compare_depositions(
        self, 
        depo1_analysis: Dict, 
        depo2_analysis: Dict
    ) -> MultiDepositionAnalysis:
        """
        Compare two deposition analyses to find contradictions and corroborations
        
        Args:
            depo1_analysis: JSON analysis of first deposition
            depo2_analysis: JSON analysis of second deposition
            
        Returns:
            MultiDepositionAnalysis with comparison results
        """
        print("Comparing depositions...")
        
        # Build comparison prompt
        prompt = COMPARISON_PROMPT.format(
            witness1=depo1_analysis["witness"]["name"],
            depo1_summary=depo1_analysis["executive_summary"],
            depo1_statements=json.dumps(depo1_analysis["key_admissions"], indent=2),
            witness2=depo2_analysis["witness"]["name"],
            depo2_summary=depo2_analysis["executive_summary"],
            depo2_statements=json.dumps(depo2_analysis.get("key_statements", []), indent=2)
        )
        
        response = self._call_claude(prompt)
        comparison_data = self._parse_json_response(response)
        
        return self._build_analysis(depo1_analysis, depo2_analysis, comparison_data)
    
    def _parse_json_response(self, response: str) -> Dict:
        """Extract JSON from response"""
        import re
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(1))
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response[start:end])
            raise ValueError("Could not parse JSON")
    
    def _build_analysis(
        self,
        depo1: Dict,
        depo2: Dict,
        comparison: Dict
    ) -> MultiDepositionAnalysis:
        """Build MultiDepositionAnalysis from comparison data"""
        
        depositions = [
            {
                "witness_name": depo1["witness"]["name"],
                "date": depo1["metadata"]["deposition_date"],
                "role": depo1["witness"]["role"]
            },
            {
                "witness_name": depo2["witness"]["name"],
                "date": depo2["metadata"]["deposition_date"],
                "role": depo2["witness"]["role"]
            }
        ]
        
        # Build contradictions
        contradictions = []
        for c in comparison.get("cross_deposition_contradictions", []):
            contradictions.append(CrossDepoContradiction(
                topic=c.get("topic", ""),
                witness_1_name=depo1["witness"]["name"],
                witness_1_statement=c.get("witness_1_statement", ""),
                witness_1_reference=c.get("witness_1_reference", ""),
                witness_2_name=depo2["witness"]["name"],
                witness_2_statement=c.get("witness_2_statement", ""),
                witness_2_reference=c.get("witness_2_reference", ""),
                significance=c.get("significance", ""),
                exploitation_strategy=c.get("exploitation_strategy", ""),
                severity=c.get("severity", "moderate")
            ))
        
        # Build corroborations
        corroborations = []
        for c in comparison.get("corroborating_statements", []):
            if isinstance(c, dict):
                corroborations.append(Corroboration(
                    topic=c.get("topic", ""),
                    fact_established=c.get("fact", ""),
                    witnesses=c.get("witnesses", []),
                    strength=c.get("strength", "moderate"),
                    trial_value=c.get("trial_value", "")
                ))
        
        # Build credibility comparison
        cred_data = comparison.get("credibility_comparison", {})
        if isinstance(cred_data, str):
            credibility = WitnessCredibilityComparison(
                more_credible="",
                less_credible="",
                reasoning=cred_data,
                factors=[]
            )
        else:
            credibility = WitnessCredibilityComparison(
                more_credible=cred_data.get("more_credible", ""),
                less_credible=cred_data.get("less_credible", ""),
                reasoning=cred_data.get("reasoning", ""),
                factors=cred_data.get("factors", [])
            )
        
        return MultiDepositionAnalysis(
            case_name=depo1["metadata"]["case_name"],
            case_number=depo1["metadata"]["case_number"],
            depositions_compared=depositions,
            contradictions=contradictions,
            corroborations=corroborations,
            credibility_comparison=credibility,
            recommended_witness_order=comparison.get("recommended_witness_order", []),
            key_impeachment_opportunities=comparison.get("key_impeachment_opportunities", []),
            strategic_summary=comparison.get("strategic_implications", "")
        )


def main():
    parser = argparse.ArgumentParser(description="Compare multiple deposition analyses")
    parser.add_argument("depo1", help="Path to first deposition analysis JSON")
    parser.add_argument("depo2", help="Path to second deposition analysis JSON")
    parser.add_argument("-o", "--output", help="Output file path", default=None)
    
    args = parser.parse_args()
    
    # Load analyses
    with open(args.depo1) as f:
        depo1 = json.load(f)
    with open(args.depo2) as f:
        depo2 = json.load(f)
    
    # Compare
    comparator = MultiDepositionComparator()
    result = comparator.compare_depositions(depo1, depo2)
    
    # Save
    output_path = args.output or "comparison_analysis.json"
    Path(output_path).write_text(result.to_json())
    print(f"Comparison saved to: {output_path}")


if __name__ == "__main__":
    main()

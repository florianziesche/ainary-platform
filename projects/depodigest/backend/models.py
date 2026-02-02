"""
DepoDigest Pro - Data Models
Structured output schemas for deposition analysis
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum
import json
from datetime import datetime


class AdmissionType(Enum):
    LIABILITY = "liability"
    DAMAGES = "damages"
    NEGLIGENCE = "negligence"
    CAUSATION = "causation"
    CREDIBILITY = "credibility"


class SeverityLevel(Enum):
    CRITICAL = "critical"      # Case-changing admission
    SIGNIFICANT = "significant" # Strong support for claim
    MODERATE = "moderate"       # Helpful but not decisive
    MINOR = "minor"            # Marginal relevance


@dataclass
class PageLineRef:
    """Reference to specific location in transcript"""
    page: int
    line_start: int
    line_end: int
    
    def __str__(self):
        if self.line_start == self.line_end:
            return f"Page {self.page}, Line {self.line_start}"
        return f"Page {self.page}, Lines {self.line_start}-{self.line_end}"
    
    def to_dict(self):
        return {
            "page": self.page,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "formatted": str(self)
        }


@dataclass
class KeyAdmission:
    """A significant admission by the witness"""
    quote: str
    admission_type: AdmissionType
    severity: SeverityLevel
    reference: PageLineRef
    context: str
    impeachment_value: str  # Why this matters for cross-exam
    
    def to_dict(self):
        return {
            "quote": self.quote,
            "type": self.admission_type.value,
            "severity": self.severity.value,
            "reference": self.reference.to_dict(),
            "context": self.context,
            "impeachment_value": self.impeachment_value
        }


@dataclass
class TimelineEvent:
    """A chronological event mentioned in testimony"""
    date: str
    time: Optional[str]
    description: str
    reference: PageLineRef
    significance: str
    
    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "description": self.description,
            "reference": self.reference.to_dict(),
            "significance": self.significance
        }


@dataclass
class Contradiction:
    """An internal contradiction in testimony"""
    statement_1: str
    statement_1_ref: PageLineRef
    statement_2: str
    statement_2_ref: PageLineRef
    explanation: str
    severity: SeverityLevel
    
    def to_dict(self):
        return {
            "statement_1": self.statement_1,
            "statement_1_ref": self.statement_1_ref.to_dict(),
            "statement_2": self.statement_2,
            "statement_2_ref": self.statement_2_ref.to_dict(),
            "explanation": self.explanation,
            "severity": self.severity.value
        }


@dataclass
class CrossExamQuestion:
    """Suggested cross-examination question"""
    question: str
    purpose: str
    based_on: PageLineRef
    follow_up_if_admits: str
    follow_up_if_denies: str
    
    def to_dict(self):
        return {
            "question": self.question,
            "purpose": self.purpose,
            "based_on": self.based_on.to_dict(),
            "follow_up_if_admits": self.follow_up_if_admits,
            "follow_up_if_denies": self.follow_up_if_denies
        }


@dataclass
class SettlementImpact:
    """Assessment of how testimony affects settlement value"""
    overall_score: int  # 1-100, higher = stronger for plaintiff
    liability_strength: int  # 1-100
    damages_support: int  # 1-100
    credibility_issues: int  # 1-100, higher = more credibility problems for defense
    key_factors: List[str]
    settlement_range_adjustment: str  # e.g., "+15-25%"
    reasoning: str
    
    def to_dict(self):
        return {
            "overall_score": self.overall_score,
            "liability_strength": self.liability_strength,
            "damages_support": self.damages_support,
            "credibility_issues": self.credibility_issues,
            "key_factors": self.key_factors,
            "settlement_range_adjustment": self.settlement_range_adjustment,
            "reasoning": self.reasoning
        }


@dataclass
class WitnessSummary:
    """Summary profile of the deposed witness"""
    name: str
    role: str  # defendant, plaintiff, expert, fact witness
    credibility_assessment: str
    demeanor_notes: str
    key_weaknesses: List[str]
    key_strengths: List[str]
    
    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "credibility_assessment": self.credibility_assessment,
            "demeanor_notes": self.demeanor_notes,
            "key_weaknesses": self.key_weaknesses,
            "key_strengths": self.key_strengths
        }


@dataclass
class DepositionAnalysis:
    """Complete analysis of a deposition"""
    # Metadata
    case_name: str
    case_number: str
    deposition_date: str
    witness: WitnessSummary
    
    # Core Analysis
    executive_summary: str
    narrative_summary: str
    
    # Extracted Intelligence
    key_admissions: List[KeyAdmission]
    timeline: List[TimelineEvent]
    contradictions: List[Contradiction]
    
    # Trial Prep
    cross_exam_questions: List[CrossExamQuestion]
    impeachment_points: List[str]
    
    # Settlement Impact
    settlement_impact: SettlementImpact
    
    # Metadata
    analyzed_at: str = field(default_factory=lambda: datetime.now().isoformat())
    version: str = "1.0"
    
    def to_dict(self):
        return {
            "metadata": {
                "case_name": self.case_name,
                "case_number": self.case_number,
                "deposition_date": self.deposition_date,
                "analyzed_at": self.analyzed_at,
                "version": self.version
            },
            "witness": self.witness.to_dict(),
            "executive_summary": self.executive_summary,
            "narrative_summary": self.narrative_summary,
            "key_admissions": [a.to_dict() for a in self.key_admissions],
            "timeline": [t.to_dict() for t in self.timeline],
            "contradictions": [c.to_dict() for c in self.contradictions],
            "cross_exam_questions": [q.to_dict() for q in self.cross_exam_questions],
            "impeachment_points": self.impeachment_points,
            "settlement_impact": self.settlement_impact.to_dict()
        }
    
    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent)

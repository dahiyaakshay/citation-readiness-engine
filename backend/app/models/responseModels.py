from pydantic import BaseModel
from typing import Dict, List


class SectionScore(BaseModel):
    heading: str
    fact_density: float
    entity_clarity: float
    tone_neutrality: float


class AuditResponse(BaseModel):
    citation_readiness_index: float
    dom_score: float
    fact_density: float
    entity_clarity: float
    tone_neutrality: float
    retrieval_simulation: float
    sections_analyzed: int
    section_breakdown: List[SectionScore]

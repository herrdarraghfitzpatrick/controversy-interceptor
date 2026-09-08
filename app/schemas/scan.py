import uuid
from datetime import datetime

from pydantic import BaseModel, Field

from app.models.case import RiskCategory, Severity


class ScanRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Campaign copy or brief to scan")
    target_markets: list[str] = Field(..., min_length=1, description="ISO country codes, e.g. ['IE', 'KR', 'US']")
    industry: str = Field(..., description="e.g. fintech, FMCG, healthcare")
    content_type: str = Field(..., description="e.g. PR blog post, paid social ad, press release")
    imagery_description: str | None = Field(
        default=None, description="Optional freeform description of visuals, used by the imagery lens only"
    )


class Finding(BaseModel):
    span: str = Field(..., description="The flagged text/phrase")
    category: RiskCategory
    target_market: str = Field(..., description="The market this finding applies to, e.g. Ireland")
    severity: Severity
    confidence: float = Field(..., ge=0.0, le=1.0)
    explanation: str
    precedent: str | None = Field(default=None, description="The real-world case this echoes, with a link")
    suggested_fix: str | None = Field(default=None, description="Optional rewrite or mitigation")


class ScanResponse(BaseModel):
    scan_id: uuid.UUID
    scope_applied: str
    findings: list[Finding]
    checked_against_library_version: str
    live_search_performed: bool


class ScanHistoryItem(BaseModel):
    scan_id: uuid.UUID
    scope_applied: str
    created_at: datetime
    finding_count: int

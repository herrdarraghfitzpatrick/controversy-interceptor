import uuid
from datetime import datetime

from pydantic import BaseModel, Field

from app.models.case import RiskCategory, Severity

# "Campaign copy or brief" per spec section 5 - generous enough for a long
# press release or blog post (roughly 3,000-4,000 words), but bounded so a
# pasted report/whitepaper doesn't turn one scan into a huge, slow, costly
# Claude call (this pipeline runs the text through Claude up to twice - the
# lens 1-3/5 pass, and again if check_recent_events is set).
MAX_TEXT_LENGTH = 20_000
MAX_IMAGERY_DESCRIPTION_LENGTH = 2_000


class ScanRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=MAX_TEXT_LENGTH,
        description="Campaign copy or brief to scan",
    )
    target_markets: list[str] = Field(..., min_length=1, description="ISO country codes, e.g. ['IE', 'KR', 'US']")
    industry: str = Field(..., description="e.g. fintech, FMCG, healthcare")
    content_type: str = Field(..., description="e.g. PR blog post, paid social ad, press release")
    imagery_description: str | None = Field(
        default=None,
        max_length=MAX_IMAGERY_DESCRIPTION_LENGTH,
        description="Optional freeform description of visuals, used by the imagery lens only",
    )
    check_recent_events: bool = Field(
        default=False,
        description=(
            "Opt in to the recent-event collision lens (lens 4), which uses live web search "
            "and is slower/costlier than the rest of the scan - gated per spec section 7 Phase 2. "
            "Recommended for high-stakes scans (e.g. paid ads, press releases) rather than every scan."
        ),
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

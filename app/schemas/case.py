import uuid
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from app.models.case import RiskCategory, Severity


class CaseLibraryEntryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    phrase_or_concept: str
    region: str
    category: RiskCategory
    industry_tags: list[str] = []
    content_type_tags: list[str] = []
    description: str
    source_url: str
    date_occurred: date | None = None
    severity_baseline: Severity
    active: bool
    created_at: datetime
    updated_at: datetime


class CaseLibraryEntryCreate(BaseModel):
    phrase_or_concept: str
    region: str
    category: RiskCategory
    industry_tags: list[str] = []
    content_type_tags: list[str] = []
    description: str
    source_url: str
    date_occurred: date | None = None
    severity_baseline: Severity
    active: bool = True

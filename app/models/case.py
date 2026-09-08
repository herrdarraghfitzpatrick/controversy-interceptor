import enum
import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Enum, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class RiskCategory(str, enum.Enum):
    linguistic = "linguistic"
    historical = "historical"
    brand = "brand"
    recent_event = "recent_event"
    imagery = "imagery"


class Severity(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class CaseLibraryEntry(Base):
    """A known controversy in the curated case library (spec section 4)."""

    __tablename__ = "case_library_entries"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phrase_or_concept: Mapped[str] = mapped_column(Text, nullable=False)
    region: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    category: Mapped[RiskCategory] = mapped_column(Enum(RiskCategory, name="risk_category"), nullable=False, index=True)
    industry_tags: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True, default=list)
    content_type_tags: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True, default=list)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    source_url: Mapped[str] = mapped_column(Text, nullable=False)
    date_occurred: Mapped[date | None] = mapped_column(Date, nullable=True)
    severity_baseline: Mapped[Severity] = mapped_column(Enum(Severity, name="severity_level"), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

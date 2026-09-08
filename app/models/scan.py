import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Scan(Base):
    """A single scan request/report (spec section 5)."""

    __tablename__ = "scans"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    text: Mapped[str] = mapped_column(Text, nullable=False)
    target_markets: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    industry: Mapped[str] = mapped_column(String(128), nullable=False)
    content_type: Mapped[str] = mapped_column(String(128), nullable=False)
    imagery_description: Mapped[str | None] = mapped_column(Text, nullable=True)

    scope_applied: Mapped[str] = mapped_column(Text, nullable=False)
    findings: Mapped[list[dict]] = mapped_column(JSONB, nullable=False, default=list)
    checked_against_library_version: Mapped[str] = mapped_column(String(32), nullable=False)
    live_search_performed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), index=True)

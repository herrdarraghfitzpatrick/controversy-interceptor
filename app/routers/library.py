from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.case import CaseLibraryEntry, RiskCategory
from app.schemas.case import CaseLibraryEntryOut

router = APIRouter(tags=["library"])


@router.get("/library", response_model=list[CaseLibraryEntryOut])
def browse_library(
    region: str | None = None,
    category: RiskCategory | None = None,
    active_only: bool = True,
    db: Session = Depends(get_db),
) -> list[CaseLibraryEntry]:
    """Internal/admin browse of the case library (spec section 5)."""
    query = db.query(CaseLibraryEntry)

    if active_only:
        query = query.filter(CaseLibraryEntry.active.is_(True))
    if category is not None:
        query = query.filter(CaseLibraryEntry.category == category)
    if region is not None:
        region_upper = region.strip().upper()
        query = query.filter(CaseLibraryEntry.region.ilike(f"%{region_upper}%"))

    return query.order_by(CaseLibraryEntry.region, CaseLibraryEntry.category).all()

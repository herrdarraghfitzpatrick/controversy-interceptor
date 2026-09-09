import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.scan import Scan
from app.schemas.scan import Finding, ScanRequest, ScanResponse
from app.services import library_matcher
from app.services.claude_pipeline import run_claude_pass
from app.services.recent_event_pipeline import run_recent_event_pass
from app.services.scope import build_scope_applied

router = APIRouter(tags=["scan"])


@router.post("/scan", response_model=ScanResponse)
def create_scan(request: ScanRequest, db: Session = Depends(get_db)) -> ScanResponse:
    scope_applied = build_scope_applied(request.target_markets, request.industry, request.content_type)

    library_findings, matched_entries = library_matcher.match_library(
        db,
        text=request.text,
        target_markets=request.target_markets,
        industry=request.industry,
        content_type=request.content_type,
        imagery_description=request.imagery_description,
    )

    claude_findings = run_claude_pass(
        text=request.text,
        target_markets=request.target_markets,
        industry=request.industry,
        content_type=request.content_type,
        imagery_description=request.imagery_description,
        scope_applied=scope_applied,
        already_matched=matched_entries,
    )

    findings: list[Finding] = library_findings + claude_findings

    live_search_performed = False
    if request.check_recent_events:
        recent_event_findings, live_search_performed = run_recent_event_pass(
            text=request.text,
            target_markets=request.target_markets,
            industry=request.industry,
            content_type=request.content_type,
            scope_applied=scope_applied,
        )
        findings += recent_event_findings

    scan = Scan(
        text=request.text,
        target_markets=request.target_markets,
        industry=request.industry,
        content_type=request.content_type,
        imagery_description=request.imagery_description,
        scope_applied=scope_applied,
        findings=[f.model_dump(mode="json") for f in findings],
        checked_against_library_version=library_matcher.get_library_version(db),
        live_search_performed=live_search_performed,
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)

    return ScanResponse(
        scan_id=scan.id,
        scope_applied=scan.scope_applied,
        findings=findings,
        checked_against_library_version=scan.checked_against_library_version,
        live_search_performed=scan.live_search_performed,
    )


@router.get("/scan/{scan_id}", response_model=ScanResponse)
def get_scan(scan_id: uuid.UUID, db: Session = Depends(get_db)) -> ScanResponse:
    scan = db.get(Scan, scan_id)
    if scan is None:
        raise HTTPException(status_code=404, detail="Scan not found")

    return ScanResponse(
        scan_id=scan.id,
        scope_applied=scan.scope_applied,
        findings=[Finding(**f) for f in scan.findings],
        checked_against_library_version=scan.checked_against_library_version,
        live_search_performed=scan.live_search_performed,
    )

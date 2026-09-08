"""Library-first matching against the curated case library (spec section 4).

Per section 3: each lens is matched first against the curated case library,
then a Claude pass covers anything the library doesn't catch. This module
implements the library side for all five lenses; app.services.claude_pipeline
implements the Claude side for lenses 1-3 and 5 (lens 4, recent-event
collision, needs live web search and is out of scope for Phase 1).
"""

import re
from datetime import UTC, date, datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.case import CaseLibraryEntry, RiskCategory, Severity
from app.schemas.scan import Finding
from app.services.scope import market_name, severity_adjustment

_SEVERITY_ORDER = [Severity.low, Severity.medium, Severity.high]


def _adjust_severity(baseline: Severity, content_type: str) -> Severity:
    idx = _SEVERITY_ORDER.index(baseline)
    idx = max(0, min(len(_SEVERITY_ORDER) - 1, idx + severity_adjustment(content_type)))
    return _SEVERITY_ORDER[idx]


def _region_matches(entry_region: str, target_market: str) -> bool:
    entry_codes = {code.strip().upper() for code in entry_region.split(",")}
    return target_market.strip().upper() in entry_codes or "GLOBAL" in entry_codes


def _words(value: str) -> set[str]:
    return {w for w in re.split(r"[^a-z0-9]+", value.lower()) if len(w) >= 2}


def _tags_overlap(tags: list[str], target_words: set[str]) -> bool:
    """Industry/content-type tags on library entries (e.g. "pr", "advertising")
    and the freeform strings scan requests actually send (e.g. "PR blog post",
    "paid social ad") don't share a controlled vocabulary. Word-level overlap,
    with prefix matching for short tokens, is a pragmatic Phase 1 stand-in for
    real taxonomy/semantic matching - it's deliberately permissive, since
    over-including an entry here only means it's *considered* for matching
    against the actual scan text, not reported as a finding.
    """
    for tag in tags:
        for tag_word in _words(tag):
            for target_word in target_words:
                if tag_word == target_word or tag_word.startswith(target_word) or target_word.startswith(tag_word):
                    return True
    return False


def query_relevant_entries(
    db: Session,
    target_markets: list[str],
    industry: str,
    content_type: str,
) -> list[CaseLibraryEntry]:
    """Filters the library to region-relevant, industry-relevant (or
    industry-agnostic), format-relevant (or format-agnostic) active entries.
    """
    candidates = db.query(CaseLibraryEntry).filter(CaseLibraryEntry.active.is_(True)).all()

    relevant = []
    industry_words = _words(industry)
    content_type_words = _words(content_type)

    for entry in candidates:
        if not any(_region_matches(entry.region, market) for market in target_markets):
            continue

        if entry.industry_tags and not _tags_overlap(entry.industry_tags, industry_words):
            continue

        if entry.content_type_tags and not _tags_overlap(entry.content_type_tags, content_type_words):
            continue

        relevant.append(entry)

    return relevant


_QUOTED_PHRASE = re.compile(r'"([^"]{2,60})"')


def _candidate_phrases(phrase_or_concept: str) -> list[str]:
    """`phrase_or_concept` is often a descriptive concept summary rather than
    a literal trigger (e.g. `"Tank Day" tumbler promotion on the anniversary
    of the Gwangju massacre`), which a straight substring match against the
    full string would essentially never catch in real campaign copy. Quoted
    sub-phrases are usually the actual literal slogan/name/hashtag, so try
    those too, longest first, in addition to the full string.
    """
    quoted = sorted(_QUOTED_PHRASE.findall(phrase_or_concept), key=len, reverse=True)
    return [phrase_or_concept, *quoted]


def _find_span(text: str, phrase_or_concept: str) -> str | None:
    """Case-insensitive substring match against the full phrase/concept or
    any literal quoted sub-phrase within it. Returns the matched span from
    the original text (preserving its casing) or None.
    """
    for candidate in _candidate_phrases(phrase_or_concept):
        pattern = re.escape(candidate.strip())
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(0)
    return None


def match_library(
    db: Session,
    text: str,
    target_markets: list[str],
    industry: str,
    content_type: str,
    imagery_description: str | None,
) -> tuple[list[Finding], list[CaseLibraryEntry]]:
    """Returns (findings, matched_entries). matched_entries is used to avoid
    asking Claude to re-flag the same ground the library already covered.
    """
    entries = query_relevant_entries(db, target_markets, industry, content_type)

    findings: list[Finding] = []
    matched_entries: list[CaseLibraryEntry] = []

    for entry in entries:
        haystack = imagery_description if entry.category == RiskCategory.imagery else text
        if not haystack:
            continue

        span = _find_span(haystack, entry.phrase_or_concept)
        if span is None:
            continue

        matched_entries.append(entry)

        applicable_market = next(
            (m for m in target_markets if _region_matches(entry.region, m)),
            target_markets[0],
        )

        findings.append(
            Finding(
                span=span,
                category=entry.category,
                target_market=market_name(applicable_market),
                severity=_adjust_severity(entry.severity_baseline, content_type),
                confidence=0.9,
                explanation=entry.description,
                precedent=f"{entry.description} ({entry.source_url})",
                suggested_fix=None,
            )
        )

    return findings, matched_entries


def get_library_version(db: Session) -> str:
    """A coarse "version" for the active case library, used in scan reports
    so a report can be traced back to the library state it was checked
    against. Derived from the most recent update among active entries.
    """
    latest: date | None = db.query(func.max(CaseLibraryEntry.updated_at)).filter(
        CaseLibraryEntry.active.is_(True)
    ).scalar()
    if latest is None:
        return datetime.now(UTC).date().isoformat()
    return latest.date().isoformat() if hasattr(latest, "date") else str(latest)

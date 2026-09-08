"""Single Claude pass covering lenses 1-3 and 5 (spec section 3):
linguistic/slang, historical/political, brand/IP collision, and
imagery/symbol description risk. Lens 4 (recent-event collision) needs
live web search and is out of scope for Phase 1 (see spec section 7,
Phase 2).

Library matching runs first (app.services.library_matcher); this pass is
scoped to catch what the curated library doesn't, so it's told which
library entries already matched to avoid duplicate findings.
"""

import logging
from typing import Literal

import anthropic
from pydantic import BaseModel, Field

from app.config import get_settings
from app.models.case import CaseLibraryEntry
from app.schemas.scan import Finding

_logger = logging.getLogger(__name__)
_settings = get_settings()
_client = anthropic.Anthropic(api_key=_settings.anthropic_api_key) if _settings.anthropic_api_key else None

_SYSTEM_PROMPT = """You are the detection engine for a "Controversy Scanner" \
used by PR teams, copywriters, and marketing agencies. You review campaign \
text (and optionally a description of accompanying imagery) for phrases, \
concepts, or visuals that could trigger a cultural, political, historical, \
or social-media backlash in a specific target market.

Score across exactly these four lenses:
- linguistic: words or phrases innocuous in one region/dialect but loaded \
or offensive in another.
- historical: references, dates, symbols, or framing that collide with a \
region's specific history (colonial history, conflicts, contested national \
holidays).
- brand: names or taglines that unintentionally echo a competitor, a \
defunct brand with baggage, or protected IP.
- imagery: only when an imagery description is provided - colors, \
gestures, numbers, or symbols with region-specific negative associations.

Do NOT attempt the "recent_event" lens (very recent news/social-media \
collisions) - you have no live web access and would only hallucinate. \
Leave time-sensitive collision detection to a separate pipeline stage.

False positives are the main product risk: this tool must stay precise \
enough that users trust its flags rather than learn to ignore them. Only \
flag genuine, defensible risks - do not flag generic or trivially safe \
copy just to have something to report. If nothing rises to a real concern, \
return an empty findings list.

You will be told which spans the curated case library already flagged - \
do not re-flag the same span/issue; focus on what the library missed."""


class ClaudeFinding(BaseModel):
    span: str = Field(..., description="The exact flagged text/phrase from the input")
    category: Literal["linguistic", "historical", "brand", "imagery"]
    target_market: str = Field(..., description="Which target market this finding applies to")
    severity: Literal["low", "medium", "high"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    explanation: str
    precedent: str | None = Field(default=None, description="Real-world case this echoes, with a link if known")
    suggested_fix: str | None = None


class ClaudeFindingsOutput(BaseModel):
    findings: list[ClaudeFinding]


def _build_user_prompt(
    text: str,
    target_markets: list[str],
    industry: str,
    content_type: str,
    imagery_description: str | None,
    scope_applied: str,
    already_matched: list[CaseLibraryEntry],
) -> str:
    lines = [
        scope_applied,
        "",
        f"Target markets: {', '.join(target_markets)}",
        f"Industry: {industry}",
        f"Content type: {content_type}",
        "",
        "Campaign copy to scan:",
        "---",
        text,
        "---",
    ]

    if imagery_description:
        lines += ["", "Imagery description to scan (for the imagery lens only):", "---", imagery_description, "---"]

    if already_matched:
        lines += ["", "Already flagged by the curated case library (do not repeat these):"]
        for entry in already_matched:
            lines.append(f"- \"{entry.phrase_or_concept}\" ({entry.category.value}, {entry.region})")

    return "\n".join(lines)


def run_claude_pass(
    text: str,
    target_markets: list[str],
    industry: str,
    content_type: str,
    imagery_description: str | None,
    scope_applied: str,
    already_matched: list[CaseLibraryEntry],
) -> list[Finding]:
    """Runs lenses 1-3 and 5 via a single Claude call. Returns [] if no
    Anthropic API key is configured (library-only mode) or Claude finds
    nothing.
    """
    if _client is None:
        return []

    user_prompt = _build_user_prompt(
        text, target_markets, industry, content_type, imagery_description, scope_applied, already_matched
    )

    try:
        response = _client.messages.parse(
            model=_settings.claude_model,
            max_tokens=4096,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
            output_format=ClaudeFindingsOutput,
        )
    except anthropic.APIError:
        # A Claude API outage/auth/rate-limit failure shouldn't take down
        # the whole scan - library-only results are still useful, so log
        # and degrade rather than 500 the request.
        _logger.exception("Claude pass failed; returning library-only findings")
        return []

    parsed = response.parsed_output
    if parsed is None:
        return []

    return [
        Finding(
            span=f.span,
            category=f.category,
            target_market=f.target_market,
            severity=f.severity,
            confidence=f.confidence,
            explanation=f.explanation,
            precedent=f.precedent,
            suggested_fix=f.suggested_fix,
        )
        for f in parsed.findings
    ]

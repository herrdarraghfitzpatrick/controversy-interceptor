"""Phase 2 pipeline stage: lens 4, recent-event collision (spec section 3,
lens 4; section 7, Phase 2).

This is the one lens that cannot be solved from the static case library -
it needs live web search to catch copy that's fine in isolation but lands
badly next to a very recent news story or social-media moment in the
target market (the "Starbucks Korea" case is this category). It's slower
and costs more per call than the library+single-Claude-pass pipeline in
app.services.claude_pipeline, so per the spec it's gated separately and
only runs when a scan opts in (ScanRequest.check_recent_events).
"""

import logging
from typing import Literal

import anthropic
from pydantic import BaseModel, Field

from app.config import get_settings
from app.schemas.scan import Finding

_logger = logging.getLogger(__name__)
_settings = get_settings()
_client = anthropic.Anthropic(api_key=_settings.anthropic_api_key) if _settings.anthropic_api_key else None

_WEB_SEARCH_TOOL = {"type": "web_search_20260209", "name": "web_search", "max_uses": 5}

_SYSTEM_PROMPT = """You are the recent-event collision detector for a \
"Controversy Scanner" used by PR teams, copywriters, and marketing \
agencies. Campaign copy can be completely fine in isolation but land badly \
because it collides with a very recent news story or social-media moment \
in the target market - the canonical example is Starbucks Korea launching \
a "Tank Day" tumbler promotion on May 18, the anniversary of the Gwangju \
massacre, where the date and imagery were fine on their own but toxic in \
context.

Use the web_search tool to check the campaign copy - its key phrases, \
dates, imagery references, hashtags, and named entities - against current \
news and social media in each target market. Search for each target \
market specifically; a collision in one market may not exist in another.

False positives are the main product risk: this tool must stay precise \
enough that users trust its flags rather than learn to ignore them. Only \
flag a genuine, verifiable collision you found evidence for via search - \
never speculate about "recent" events from memory, since your training \
data is not current. If search turns up nothing relevant, return an empty \
findings list rather than inventing a plausible-sounding risk.

For every finding, `precedent` must include a real URL from your search \
results as evidence."""


class RecentEventFinding(BaseModel):
    span: str = Field(..., description="The exact flagged text/phrase/date/reference from the input")
    target_market: str = Field(..., description="Which target market this finding applies to")
    severity: Literal["low", "medium", "high"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    explanation: str
    precedent: str = Field(..., description="The recent news/social-media event this collides with, with a URL")
    suggested_fix: str | None = None


class RecentEventFindingsOutput(BaseModel):
    findings: list[RecentEventFinding]


def _build_user_prompt(
    text: str,
    target_markets: list[str],
    industry: str,
    content_type: str,
    scope_applied: str,
) -> str:
    return "\n".join(
        [
            scope_applied,
            "",
            f"Target markets: {', '.join(target_markets)}",
            f"Industry: {industry}",
            f"Content type: {content_type}",
            "",
            "Campaign copy to check against recent news/social-media events:",
            "---",
            text,
            "---",
        ]
    )


def run_recent_event_pass(
    text: str,
    target_markets: list[str],
    industry: str,
    content_type: str,
    scope_applied: str,
) -> tuple[list[Finding], bool]:
    """Runs lens 4 via a single Claude call with the web_search tool.

    Returns (findings, live_search_performed). live_search_performed is
    True only if a web_search_tool_result block actually appears in the
    response - i.e. Claude actually searched, not just that we asked it
    to. Returns ([], False) if no Anthropic API key is configured or the
    call fails.
    """
    if _client is None:
        return [], False

    user_prompt = _build_user_prompt(text, target_markets, industry, content_type, scope_applied)

    try:
        response = _client.messages.parse(
            model=_settings.claude_model,
            max_tokens=4096,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
            tools=[_WEB_SEARCH_TOOL],
            output_format=RecentEventFindingsOutput,
        )
    except anthropic.APIError:
        _logger.exception("Recent-event pass failed; skipping lens 4 for this scan")
        return [], False

    live_search_performed = any(block.type == "web_search_tool_result" for block in response.content)

    parsed = response.parsed_output
    if parsed is None:
        return [], live_search_performed

    findings = [
        Finding(
            span=f.span,
            category="recent_event",
            target_market=f.target_market,
            severity=f.severity,
            confidence=f.confidence,
            explanation=f.explanation,
            precedent=f.precedent,
            suggested_fix=f.suggested_fix,
        )
        for f in parsed.findings
    ]
    return findings, live_search_performed

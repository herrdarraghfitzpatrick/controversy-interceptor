"""Builds the "scope" that scopes both the case-library query and the Claude
prompt, per spec section 3.0: target_market + industry + content_type combine
into a single lens description rather than a freeform context string.
"""

# Content types that raise severity: public, durable, and attributable to the
# company. Internal/ephemeral formats stay at baseline severity.
HIGH_DURABILITY_CONTENT_TYPES = {
    "pr blog post",
    "press release",
    "paid social ad",
    "social media post",
    "billboard",
    "tv ad",
    "print ad",
    "website copy",
    "product packaging",
}

LOW_DURABILITY_CONTENT_TYPES = {
    "internal comms",
    "internal memo",
    "draft",
    "employee newsletter",
}

# ISO 3166-1 alpha-2 -> readable market name, for common launch markets.
# Falls back to the raw code for anything not listed.
MARKET_NAMES: dict[str, str] = {
    "IE": "Ireland",
    "GB": "United Kingdom",
    "UK": "United Kingdom",
    "US": "United States",
    "KR": "South Korea",
    "JP": "Japan",
    "CN": "China",
    "FR": "France",
    "DE": "Germany",
    "IN": "India",
    "AU": "Australia",
    "CA": "Canada",
    "BR": "Brazil",
    "MX": "Mexico",
    "ES": "Spain",
    "IT": "Italy",
    "NL": "Netherlands",
    "SE": "Sweden",
    "ZA": "South Africa",
    "NG": "Nigeria",
    "AE": "United Arab Emirates",
    "SA": "Saudi Arabia",
    "SG": "Singapore",
}


def market_name(code: str) -> str:
    return MARKET_NAMES.get(code.strip().upper(), code.strip())


def content_type_durability(content_type: str) -> str:
    """Returns 'high', 'low', or 'standard' durability/visibility for the format."""
    normalized = content_type.strip().lower()
    if normalized in HIGH_DURABILITY_CONTENT_TYPES:
        return "high"
    if normalized in LOW_DURABILITY_CONTENT_TYPES:
        return "low"
    return "standard"


def build_scope_applied(target_markets: list[str], industry: str, content_type: str) -> str:
    """Human-readable scope string, e.g.
    "Irish market / fintech / PR blog post — weigh regional historical
    sensitivities and financial-trust language more heavily; treat findings
    as higher-severity given the public/durable format."
    """
    markets = " & ".join(f"{market_name(code)} market" for code in target_markets)
    durability = content_type_durability(content_type)

    severity_note = {
        "high": "treat findings as higher-severity given the public/durable format",
        "low": "treat findings as lower-severity given the private/ephemeral format",
        "standard": "apply standard severity scoring for this format",
    }[durability]

    return f"Scanning as: {markets} / {industry} / {content_type} — {severity_note}."


def severity_adjustment(content_type: str) -> int:
    """Signed adjustment applied to a lens/library baseline severity ordinal
    (low=0, medium=1, high=2), clamped by the caller.
    """
    durability = content_type_durability(content_type)
    if durability == "high":
        return 1
    if durability == "low":
        return -1
    return 0

from datetime import date

from app.models.case import CaseLibraryEntry, RiskCategory, Severity
from app.services import library_matcher


def _make_entry(
    db_session,
    phrase="Black and Tans",
    region="IE,GB",
    category=RiskCategory.linguistic,
    industry_tags=None,
    content_type_tags=None,
    severity=Severity.high,
):
    entry = CaseLibraryEntry(
        phrase_or_concept=phrase,
        region=region,
        category=category,
        industry_tags=industry_tags or [],
        content_type_tags=content_type_tags or [],
        description="Term with a loaded paramilitary history in Ireland.",
        source_url="https://en.wikipedia.org/wiki/Black_and_Tans",
        date_occurred=date(1920, 1, 1),
        severity_baseline=severity,
        active=True,
    )
    db_session.add(entry)
    db_session.commit()
    db_session.refresh(entry)
    return entry


def test_match_library_finds_case_insensitive_span(db_session):
    _make_entry(db_session)

    findings, matched = library_matcher.match_library(
        db_session,
        text="Our new campaign channels the spirit of the black and tans.",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )

    assert len(findings) == 1
    assert len(matched) == 1
    assert findings[0].span == "black and tans"
    assert findings[0].category == RiskCategory.linguistic
    assert findings[0].target_market == "Ireland"
    assert findings[0].confidence == 0.9


def test_match_library_filters_out_wrong_region(db_session):
    _make_entry(db_session, region="KR")

    findings, matched = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )

    assert findings == []
    assert matched == []


def test_match_library_filters_by_industry_tag(db_session):
    _make_entry(db_session, industry_tags=["fintech"])

    no_match, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="healthcare",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert no_match == []

    match, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert len(match) == 1


def test_industry_agnostic_entry_matches_any_industry(db_session):
    _make_entry(db_session, industry_tags=[])

    match, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="healthcare",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert len(match) == 1


def test_severity_adjusted_up_for_high_durability_content_type(db_session):
    _make_entry(db_session, severity=Severity.medium)

    findings, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert findings[0].severity == Severity.high


def test_severity_adjusted_down_for_low_durability_content_type(db_session):
    _make_entry(db_session, severity=Severity.medium)

    findings, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="internal comms",
        imagery_description=None,
    )
    assert findings[0].severity == Severity.low


def test_imagery_category_only_matches_imagery_description(db_session):
    _make_entry(db_session, phrase="Nazi salute", category=RiskCategory.imagery, severity=Severity.high)

    no_match, _ = library_matcher.match_library(
        db_session,
        text="Our model does a Nazi salute in the copy text.",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert no_match == []

    match, _ = library_matcher.match_library(
        db_session,
        text="unrelated copy",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description="A model raises an arm in a Nazi salute pose.",
    )
    assert len(match) == 1


def test_inactive_entries_are_excluded(db_session):
    entry = _make_entry(db_session)
    entry.active = False
    db_session.commit()

    findings, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert findings == []


def test_get_library_version_returns_date_string(db_session):
    assert library_matcher.get_library_version(db_session) is not None
    _make_entry(db_session)
    version = library_matcher.get_library_version(db_session)
    assert len(version) == 10  # YYYY-MM-DD


def test_quoted_phrase_within_a_descriptive_concept_is_matchable(db_session):
    """Many real cases are concept summaries, not literal triggers - e.g.
    '"Tank Day" tumbler promotion on the anniversary of the Gwangju
    massacre'. Only the quoted "Tank Day" would ever appear verbatim in
    real campaign copy, so it must be checked as its own candidate span.
    """
    _make_entry(
        db_session,
        phrase='"Tank Day" tumbler promotion on the anniversary of the Gwangju massacre',
        region="KR",
        category=RiskCategory.historical,
    )

    findings, _ = library_matcher.match_library(
        db_session,
        text="Grab your tumbler and celebrate Tank Day with us!",
        target_markets=["KR"],
        industry="food_beverage",
        content_type="paid social ad",
        imagery_description=None,
    )

    assert len(findings) == 1
    assert findings[0].span == "Tank Day"


def test_content_type_tag_matches_freeform_content_type_via_word_overlap(db_session):
    """Entry content_type_tags (e.g. ["pr"]) and the freeform content_type a
    scan sends (e.g. "PR blog post") aren't the same controlled vocabulary -
    word-level overlap should bridge them instead of requiring exact
    membership.
    """
    _make_entry(db_session, content_type_tags=["pr"])

    findings, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="PR blog post",
        imagery_description=None,
    )
    assert len(findings) == 1


def test_content_type_tag_mismatch_still_filters_unrelated_format(db_session):
    _make_entry(db_session, content_type_tags=["internal"])

    findings, _ = library_matcher.match_library(
        db_session,
        text="black and tans",
        target_markets=["IE"],
        industry="fintech",
        content_type="paid social ad",
        imagery_description=None,
    )
    assert findings == []

from datetime import date

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.case import CaseLibraryEntry, RiskCategory, Severity


@pytest.fixture(autouse=True)
def _no_claude_call(monkeypatch):
    """Prevent real Claude API calls in tests; the Claude pass is exercised
    separately via unit tests on library_matcher and mocked here."""
    monkeypatch.setattr("app.routers.scan.run_claude_pass", lambda **kwargs: [])


@pytest.fixture
def client():
    return TestClient(app)


def test_scan_returns_200_with_expected_shape(client):
    response = client.post(
        "/scan",
        json={
            "text": "Some perfectly safe campaign copy.",
            "target_markets": ["IE"],
            "industry": "fintech",
            "content_type": "PR blog post",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert "scan_id" in body
    assert body["scope_applied"].startswith("Scanning as: Ireland market / fintech / PR blog post")
    assert body["findings"] == []
    assert body["live_search_performed"] is False
    assert "checked_against_library_version" in body


def test_scan_flags_library_match(client, db_session):
    entry = CaseLibraryEntry(
        phrase_or_concept="Black and Tans",
        region="IE,GB",
        category=RiskCategory.linguistic,
        industry_tags=[],
        content_type_tags=[],
        description="Loaded paramilitary history term in Ireland.",
        source_url="https://en.wikipedia.org/wiki/Black_and_Tans",
        date_occurred=date(1920, 1, 1),
        severity_baseline=Severity.high,
        active=True,
    )
    db_session.add(entry)
    db_session.commit()

    response = client.post(
        "/scan",
        json={
            "text": "This campaign brings back the black and tans energy.",
            "target_markets": ["IE"],
            "industry": "fintech",
            "content_type": "PR blog post",
        },
    )
    assert response.status_code == 200
    findings = response.json()["findings"]
    assert len(findings) == 1
    assert findings[0]["category"] == "linguistic"
    assert findings[0]["span"] == "black and tans"


def test_get_scan_round_trips(client):
    create_response = client.post(
        "/scan",
        json={
            "text": "Safe copy.",
            "target_markets": ["US"],
            "industry": "fmcg",
            "content_type": "internal comms",
        },
    )
    scan_id = create_response.json()["scan_id"]

    get_response = client.get(f"/scan/{scan_id}")
    assert get_response.status_code == 200
    assert get_response.json()["scan_id"] == scan_id


def test_get_scan_404_for_unknown_id(client):
    response = client.get("/scan/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_scan_requires_at_least_one_target_market(client):
    response = client.post(
        "/scan",
        json={
            "text": "Safe copy.",
            "target_markets": [],
            "industry": "fintech",
            "content_type": "PR blog post",
        },
    )
    assert response.status_code == 422

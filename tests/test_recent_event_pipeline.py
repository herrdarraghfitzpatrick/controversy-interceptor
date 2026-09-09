from app.services import recent_event_pipeline


def test_run_recent_event_pass_without_api_key_returns_empty_and_false():
    """No ANTHROPIC_API_KEY configured -> library-only/no-Claude behavior:
    lens 4 is skipped entirely rather than attempting a call."""
    findings, live_search_performed = recent_event_pipeline.run_recent_event_pass(
        text="Celebrate Tank Day with us!",
        target_markets=["KR"],
        industry="food_beverage",
        content_type="paid social ad",
        scope_applied="Scanning as: South Korea market / food_beverage / paid social ad",
    )
    assert findings == []
    assert live_search_performed is False

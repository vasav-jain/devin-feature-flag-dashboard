"""
Tests for analytics module.
"""
from src.analytics import track_event, track_event_v1, track_event_v2

def test_track_event():
    """Test tracking event with feature flag."""
    result = track_event("page_view", {"page": "/home"})
    assert result == True

def test_track_event_v1():
    """Test v1 tracking."""
    result = track_event_v1("test_event", {})
    assert result == True

def test_track_event_v2():
    """Test v2 tracking."""
    result = track_event_v2("test_event", {})
    assert result == True


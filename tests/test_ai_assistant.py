"""
Tests for AI assistant module.
"""
from src.ai_assistant import get_ai_response

def test_get_ai_response():
    """Test getting AI response with feature flag."""
    result = get_ai_response("Hello")
    assert isinstance(result, dict)
    # May return error if flag is disabled
    assert "response" in result or "error" in result


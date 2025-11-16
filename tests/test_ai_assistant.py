"""
Tests for AI assistant module.
"""
from src.ai_assistant import get_ai_response

def test_get_ai_response():
    """Test getting AI response."""
    result = get_ai_response("Hello")
    assert isinstance(result, dict)
    assert "response" in result
    assert result["status"] == "success"


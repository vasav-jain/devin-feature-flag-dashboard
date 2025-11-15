"""
Tests for pricing module.
"""
from src.pricing import get_pricing_page

def test_get_pricing_page():
    """Test getting pricing page."""
    result = get_pricing_page("user123")
    assert "plans" in result
    assert "user_id" in result
    assert result["user_id"] == "user123"
    assert result["plans"] == ["basic", "pro", "enterprise"]


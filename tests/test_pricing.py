"""
Tests for pricing module.
"""
from src.pricing import get_pricing_page

def test_get_pricing_page():
    """Test getting pricing page."""
    result = get_pricing_page("user123")
    assert "plans" in result
    assert "show_legacy_banner" in result


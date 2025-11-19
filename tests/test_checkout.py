"""
Tests for checkout module.
"""
from src.checkout import process_checkout

def test_process_checkout():
    """Test checkout processing uses new checkout flow."""
    result = process_checkout("user123", ["item1", "item2"])
    assert result["status"] == "success"
    assert result["flow"] == "new"
    assert result["user_id"] == "user123"
    assert result["items"] == ["item1", "item2"]
    assert result["message"] == "Using new checkout experience"


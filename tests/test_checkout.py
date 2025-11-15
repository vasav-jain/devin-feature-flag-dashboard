"""
Tests for checkout module.
"""
from src.checkout import process_checkout, new_checkout_flow, legacy_checkout_flow

def test_process_checkout():
    """Test checkout processing with feature flag."""
    result = process_checkout("user123", ["item1", "item2"])
    assert result["status"] == "success"
    assert "flow" in result

def test_new_checkout_flow():
    """Test new checkout flow."""
    result = new_checkout_flow("user123", ["item1"])
    assert result["flow"] == "new"
    assert result["message"] == "Using new checkout experience"

def test_legacy_checkout_flow():
    """Test legacy checkout flow."""
    result = legacy_checkout_flow("user123", ["item1"])
    assert result["flow"] == "legacy"
    assert result["message"] == "Using legacy checkout flow"


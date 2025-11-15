"""
Tests for payments module.
"""
from src.payments import process_payment, process_payment_basic, process_payment_with_retry

def test_process_payment():
    """Test payment processing with feature flag."""
    result = process_payment(100.0, "credit_card")
    assert result["status"] == "success"
    assert "retry_enabled" in result

def test_process_payment_basic():
    """Test basic payment processing."""
    result = process_payment_basic(100.0, "credit_card")
    assert result["retry_enabled"] == False

def test_process_payment_with_retry():
    """Test payment processing with retry."""
    result = process_payment_with_retry(100.0, "credit_card")
    assert result["retry_enabled"] == True
    assert result["max_retries"] == 3


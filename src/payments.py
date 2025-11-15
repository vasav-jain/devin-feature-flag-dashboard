"""
Payments module with feature flag support.
"""
from .feature_flags import is_enabled

def process_payment(amount: float, payment_method: str) -> dict:
    """
    Process a payment.
    Uses improved retry logic if flag is enabled.
    """
    if is_enabled("payment_retry_logic"):
        return process_payment_with_retry(amount, payment_method)
    else:
        return process_payment_basic(amount, payment_method)

def process_payment_basic(amount: float, payment_method: str) -> dict:
    """Basic payment processing without retry logic."""
    return {
        "status": "success",
        "amount": amount,
        "method": payment_method,
        "retry_enabled": False
    }

def process_payment_with_retry(amount: float, payment_method: str) -> dict:
    """Payment processing with improved retry mechanism."""
    return {
        "status": "success",
        "amount": amount,
        "method": payment_method,
        "retry_enabled": True,
        "max_retries": 3
    }


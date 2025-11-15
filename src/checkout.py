"""
Checkout module with feature flag support.
"""
from .feature_flags import is_enabled

def process_checkout(user_id: str, cart_items: list) -> dict:
    """
    Process a checkout request.
    Uses feature flag to determine which checkout flow to use.
    """
    if is_enabled("checkout_new_flow"):
        return new_checkout_flow(user_id, cart_items)
    else:
        return legacy_checkout_flow(user_id, cart_items)

def new_checkout_flow(user_id: str, cart_items: list) -> dict:
    """New checkout flow with improved UX."""
    return {
        "status": "success",
        "flow": "new",
        "user_id": user_id,
        "items": cart_items,
        "message": "Using new checkout experience"
    }

def legacy_checkout_flow(user_id: str, cart_items: list) -> dict:
    """Legacy checkout flow for backwards compatibility."""
    return {
        "status": "success",
        "flow": "legacy",
        "user_id": user_id,
        "items": cart_items,
        "message": "Using legacy checkout flow"
    }


"""
Checkout module.
"""

def process_checkout(user_id: str, cart_items: list) -> dict:
    """
    Process a checkout request using the new checkout flow.
    """
    return {
        "status": "success",
        "flow": "new",
        "user_id": user_id,
        "items": cart_items,
        "message": "Using new checkout experience"
    }


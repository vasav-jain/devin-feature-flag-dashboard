"""
Pricing module.
"""

def get_pricing_page(user_id: str) -> dict:
    """
    Get pricing page content.
    """
    content = {
        "user_id": user_id,
        "plans": ["basic", "pro", "enterprise"]
    }
    
    return content


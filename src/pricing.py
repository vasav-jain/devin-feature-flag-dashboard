"""
Pricing module with feature flag support.
"""
from .feature_flags import is_enabled

def get_pricing_page(user_id: str) -> dict:
    """
    Get pricing page content.
    Shows legacy pricing banner if flag is enabled.
    """
    content = {
        "user_id": user_id,
        "plans": ["basic", "pro", "enterprise"],
        "show_legacy_banner": False
    }
    
    if is_enabled("legacy_pricing_banner"):
        content["show_legacy_banner"] = True
        content["legacy_banner_message"] = "Special pricing for legacy customers"
    
    return content


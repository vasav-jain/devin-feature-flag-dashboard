"""
Notifications module with feature flag support.
"""
from .feature_flags import is_enabled

def send_notification(user_id: str, message: str) -> bool:
    """
    Send a notification to a user.
    Uses new notification system if flag is enabled.
    """
    if is_enabled("new_notification_system"):
        return send_notification_v2(user_id, message)
    else:
        return send_notification_v1(user_id, message)

def send_notification_v1(user_id: str, message: str) -> bool:
    """Legacy notification delivery system."""
    print(f"[v1] Sending notification to {user_id}: {message}")
    return True

def send_notification_v2(user_id: str, message: str) -> bool:
    """New notification delivery system."""
    print(f"[v2] Sending notification to {user_id}: {message}")
    return True


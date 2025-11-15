"""
Analytics module with feature flag support.
"""
from .feature_flags import is_enabled

def track_event(event_name: str, properties: dict) -> bool:
    """
    Track an analytics event.
    Uses v2 tracking if flag is enabled.
    """
    if is_enabled("analytics_tracking_v2"):
        return track_event_v2(event_name, properties)
    else:
        return track_event_v1(event_name, properties)

def track_event_v1(event_name: str, properties: dict) -> bool:
    """Legacy analytics tracking."""
    # Simulate tracking
    print(f"[v1] Tracking: {event_name} with {properties}")
    return True

def track_event_v2(event_name: str, properties: dict) -> bool:
    """New analytics tracking implementation."""
    # Simulate tracking
    print(f"[v2] Tracking: {event_name} with {properties}")
    return True


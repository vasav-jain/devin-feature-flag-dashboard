"""
Cache module with feature flag support.
"""
from .feature_flags import is_enabled

_cache = {}

def get(key: str) -> any:
    """
    Get value from cache.
    Uses new caching layer if flag is enabled.
    """
    if is_enabled("caching_layer_enabled"):
        return get_from_new_cache(key)
    else:
        return get_from_legacy_cache(key)

def get_from_new_cache(key: str) -> any:
    """New caching layer implementation."""
    return _cache.get(key)

def get_from_legacy_cache(key: str) -> any:
    """Legacy cache implementation."""
    return _cache.get(key)

def set(key: str, value: any) -> bool:
    """Set value in cache."""
    _cache[key] = value
    return True


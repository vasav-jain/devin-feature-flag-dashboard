"""
Feature flag utility module.
Provides functions to check if feature flags are enabled.
"""
import json
from pathlib import Path

# Load feature flags from config file
FLAGS_FILE = Path(__file__).parent.parent / "feature_flags.json"

def _load_flags():
    """Load feature flags from JSON file."""
    try:
        with open(FLAGS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

_flags_cache = None

def _get_flags():
    """Get flags with caching."""
    global _flags_cache
    if _flags_cache is None:
        _flags_cache = _load_flags()
    return _flags_cache

def is_enabled(flag_name: str) -> bool:
    """
    Check if a feature flag is enabled.
    
    Args:
        flag_name: Name of the feature flag
        
    Returns:
        True if flag is enabled, False otherwise
    """
    flags = _get_flags()
    flag_config = flags.get(flag_name, {})
    return flag_config.get("enabled", False)

def get_flag(flag_name: str) -> dict:
    """
    Get full flag configuration.
    
    Args:
        flag_name: Name of the feature flag
        
    Returns:
        Dictionary with flag configuration or empty dict if not found
    """
    flags = _get_flags()
    return flags.get(flag_name, {})

def list_flags() -> dict:
    """
    List all feature flags.
    
    Returns:
        Dictionary of all feature flags
    """
    return _get_flags()


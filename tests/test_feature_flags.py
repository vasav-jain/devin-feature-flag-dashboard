"""
Tests for feature flag functionality.
"""
import pytest
from src.feature_flags import is_enabled, get_flag, list_flags

def test_analytics_tracking_v2_enabled():
    """Test that analytics_tracking_v2 flag is enabled."""
    result = is_enabled("analytics_tracking_v2")
    assert result == True

def test_get_flag_config():
    """Test getting full flag configuration."""
    flag = get_flag("analytics_tracking_v2")
    assert "enabled" in flag
    assert "description" in flag

def test_list_all_flags():
    """Test listing all flags."""
    flags = list_flags()
    assert isinstance(flags, dict)
    assert len(flags) > 0

def test_nonexistent_flag():
    """Test that nonexistent flag returns False."""
    result = is_enabled("nonexistent_flag")
    assert result == False


"""
Tests for notifications module.
"""
from src.notifications import send_notification, send_notification_v1, send_notification_v2

def test_send_notification():
    """Test sending notification with feature flag."""
    result = send_notification("user123", "Test message")
    assert result == True

def test_send_notification_v1():
    """Test v1 notification."""
    result = send_notification_v1("user123", "Test")
    assert result == True

def test_send_notification_v2():
    """Test v2 notification."""
    result = send_notification_v2("user123", "Test")
    assert result == True


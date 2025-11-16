"""
Tests for search module.
"""
from src.search import search, search_v3, search_legacy

def test_search():
    """Test search with feature flag."""
    result = search("test query")
    assert "results" in result
    assert "algorithm" in result

def test_search_v3():
    """Test v3 search algorithm."""
    result = search_v3("test")
    assert result["algorithm"] == "v3"

def test_search_legacy():
    """Test legacy search algorithm."""
    result = search_legacy("test")
    assert result["algorithm"] == "legacy"


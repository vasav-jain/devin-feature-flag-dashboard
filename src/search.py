"""
Search module with feature flag support.
"""
from .feature_flags import is_enabled

def search(query: str) -> dict:
    """
    Perform a search query.
    Uses v3 algorithm if flag is enabled.
    """
    if is_enabled("search_alg_v3"):
        return search_v3(query)
    else:
        return search_legacy(query)

def search_v3(query: str) -> dict:
    """New search algorithm version 3."""
    return {
        "query": query,
        "algorithm": "v3",
        "results": [f"Result for {query}"],
        "count": 1
    }

def search_legacy(query: str) -> dict:
    """Legacy search algorithm."""
    return {
        "query": query,
        "algorithm": "legacy",
        "results": [f"Legacy result for {query}"],
        "count": 1
    }

def experimental_search(query: str) -> dict:
    """
    Experimental search features.
    Only available if flag is enabled.
    """
    if not is_enabled("experimental_search"):
        return {"error": "Experimental search not enabled"}
    
    return {
        "query": query,
        "algorithm": "experimental",
        "results": [f"Experimental result for {query}"],
        "features": ["autocomplete", "suggestions"]
    }


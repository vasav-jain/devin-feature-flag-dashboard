"""
AI Assistant module with feature flag support.
"""
from .feature_flags import is_enabled

def get_ai_response(prompt: str) -> dict:
    """
    Get response from AI assistant.
    Only available if beta flag is enabled.
    """
    if not is_enabled("beta_ai_assistant"):
        return {
            "error": "AI assistant is not available",
            "message": "This feature is in beta and not enabled for your account"
        }
    
    return {
        "response": f"AI response to: {prompt}",
        "model": "beta",
        "status": "success"
    }


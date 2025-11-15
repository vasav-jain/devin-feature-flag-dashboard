import os
import httpx
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

DEVIN_API_BASE = "https://api.devin.ai/v1"

# Load API key from environment
def get_api_key():
    """Get the Devin API key from environment."""
    api_key = os.environ.get("DEVIN_API_KEY")
    if not api_key:
        raise ValueError(
            "DEVIN_API_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return api_key


async def create_devin_session(prompt: str) -> dict:
    """Create a new Devin session with the given prompt."""
    api_key = get_api_key()
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{DEVIN_API_BASE}/sessions",
            json={"prompt": prompt},
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()


async def get_devin_session(session_id: str) -> dict:
    """Get the status of a Devin session by session_id."""
    api_key = get_api_key()
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DEVIN_API_BASE}/sessions/{session_id}",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()


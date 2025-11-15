import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import FLAGS
from workflows import trigger_flag_removal
from devin_client import get_devin_session

# Load .env file from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

app = FastAPI(title="Devin Feature Flag Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default port
        "http://127.0.0.1:5173",  # Alternative localhost
    ],
    allow_origin_regex=r"http://localhost:\d+",  # Allow any localhost port for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Devin Feature Flag Dashboard API"}


@app.get("/flags")
async def get_flags():
    """Get all feature flags."""
    return FLAGS


@app.post("/flags/{flag_name}/remove")
async def remove_flag(flag_name: str):
    """Trigger Devin to remove a feature flag."""
    try:
        result = await trigger_flag_removal(flag_name)
        return {
            "session_id": result["session_id"],
            "message": f"Devin session started for flag {flag_name}",
            "flag": result["flag"]
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        # Handle Devin API errors
        raise HTTPException(
            status_code=500,
            detail=f"Failed to start Devin session: {str(e)}"
        )


@app.get("/sessions/{session_id}")
async def get_session(session_id: str):
    """Get the status of a Devin session."""
    try:
        session_data = await get_devin_session(session_id)
        return session_data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get session status: {str(e)}"
        )


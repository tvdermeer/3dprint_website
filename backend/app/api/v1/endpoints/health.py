"""
Health check endpoint for API status monitoring.
"""

from datetime import datetime

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict:
    """
    Health check endpoint.

    Returns current server status and timestamp.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "3D Print Shop API",
        "version": "0.1.0",
    }


@router.get("/ping")
def ping() -> dict:
    """Simple ping endpoint to verify server is running."""
    return {"message": "pong"}

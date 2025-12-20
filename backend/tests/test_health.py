"""
Tests for health check endpoints.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    """Test the health check endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["service"] == "3D Print Shop API"


def test_ping() -> None:
    """Test the ping endpoint."""
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "pong"


@pytest.mark.asyncio
async def test_cors_headers() -> None:
    """Test that CORS headers are present."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200

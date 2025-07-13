"""
Tests for the main FastAPI application.
"""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_root_endpoint(client):
    """Test the root endpoint returns correct information."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Uruguay News API"
    assert data["version"] == "0.1.0"
    assert data["docs"] == "/docs"
    assert data["health"] == "/health"


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "uruguay-news-api"
    assert "status" in data
    assert "firestore" in data
    assert "redis" in data
    assert "ai_models" in data


def test_analyze_endpoint(client):
    """Test the analyze endpoint placeholder."""
    response = client.post("/analyze")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_batch_analyze_endpoint(client):
    """Test the batch analyze endpoint placeholder."""
    response = client.post("/batch-analyze")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

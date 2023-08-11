"""
Tests for the measurements API.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check_successful():
    """Test health check success."""
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {'healthy': True}

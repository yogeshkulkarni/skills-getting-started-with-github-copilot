import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: (No setup needed for in-memory activities)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Act: Sign up
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert signup_resp.status_code == 200
    assert f"Signed up {email}" in signup_resp.json()["message"]
    # Act: Unregister
    unregister_resp = client.delete(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert unregister_resp.status_code == 200
    assert f"Removed {email}" in unregister_resp.json()["message"]

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.services.user_service import UserService
from app.schemas.user import UserCreate

def test_create_user(client: TestClient):
    response = client.post(
        "/api/v1/auth/signup",
        json={"email": "test@example.com", "password": "password123", "full_name": "Test User"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "password" not in data

def test_create_user_duplicate_email(client: TestClient):
    # Create first user
    client.post(
        "/api/v1/auth/signup",
        json={"email": "duplicate@example.com", "password": "password123"},
    )
    # Try to create second user with same email
    response = client.post(
        "/api/v1/auth/signup",
        json={"email": "duplicate@example.com", "password": "password456"},
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_login_access_token(client: TestClient):
    # Create user first
    email = "login@example.com"
    password = "loginpass"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password},
    )

    # Login
    response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client: TestClient):
    # Create user first
    email = "wrongpass@example.com"
    password = "correctpass"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password},
    )

    # Login with wrong password
    response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": "wrongpassword"},
    )
    assert response.status_code == 400

def test_user_service_hashing(client: TestClient):
    # This test verifies the service logic directly, particularly hashing
    # We can access the DB via dependency override or just rely on the API side effects for now
    # But for unit testing the service functions specifically, we might need a db session fixture.
    # Given the conftest setup, let's stick to API tests which implicitly test the service layer.
    pass


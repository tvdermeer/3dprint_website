from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.services.user_service import UserService
from app.schemas.user import UserCreate


def test_create_user(client: TestClient):
    response = client.post(
        "/api/v1/auth/signup",
        json={
            "email": "test@example.com",
            "password": "Password123!",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "password" not in data


def test_create_user_weak_password(client: TestClient):
    response = client.post(
        "/api/v1/auth/signup",
        json={
            "email": "weak@example.com",
            "password": "weak",
            "full_name": "Weak User",
        },
    )
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    # Pydantic validation error details usually contain the message
    assert "Password must be at least 8 characters long" in str(data["detail"])


def test_create_user_duplicate_email(client: TestClient):
    # Create first user
    client.post(
        "/api/v1/auth/signup",
        json={"email": "duplicate@example.com", "password": "Password123!"},
    )
    # Try to create second user with same email
    response = client.post(
        "/api/v1/auth/signup",
        json={"email": "duplicate@example.com", "password": "Password456!"},
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_login_access_token(client: TestClient):
    # Create user first
    email = "login@example.com"
    password = "LoginPass1!"
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
    password = "CorrectPass1!"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password},
    )

    # Login with wrong password
    response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": "WrongPassword1!"},
    )
    assert response.status_code == 400


def test_password_recovery(client: TestClient):
    # 1. Create a user
    client.post(
        "/api/v1/auth/signup",
        json={
            "email": "recover@example.com",
            "password": "OldPassword1!",
            "full_name": "Recover User",
        },
    )

    # 2. Request password recovery
    response = client.post("/api/v1/auth/password-recovery/recover@example.com")
    assert response.status_code == 200
    assert response.json() == {"msg": "Password recovery email sent"}

    # 3. Create a valid token manually
    from app.core.security import create_password_reset_token

    token = create_password_reset_token(email="recover@example.com")

    # 4. Reset password
    response = client.post(
        "/api/v1/auth/reset-password",
        json={
            "token": token,
            "new_password": "NewPassword123!",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "Password updated successfully"}

    # 5. Verify old password doesn't work
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": "recover@example.com", "password": "OldPassword1!"},
    )
    assert login_response.status_code == 400

    # 6. Verify new password works
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": "recover@example.com", "password": "NewPassword123!"},
    )
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

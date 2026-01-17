from fastapi.testclient import TestClient


def test_get_users_me(client: TestClient) -> None:
    # 1. Signup
    email = "test_me@example.com"
    password = "password123"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password, "full_name": "Test User"},
    )

    # 2. Login to get token
    response = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": password},
    )
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Get /users/me
    response = client.get("/api/v1/users/me", headers=headers)
    assert response.status_code == 200
    current_user = response.json()
    assert current_user
    assert current_user["is_active"] is True
    assert current_user["email"] == email
    assert current_user["full_name"] == "Test User"


def test_get_users_me_unauthorized(client: TestClient) -> None:
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401

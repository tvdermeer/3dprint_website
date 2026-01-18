from fastapi.testclient import TestClient


def test_update_user_me(client: TestClient) -> None:
    # 1. Signup and Login
    email = "update_user@example.com"
    password = "Password123!"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password, "full_name": "Original Name"},
    )

    login_res = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": password},
    )
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Update User
    new_name = "Updated Name"
    response = client.put(
        "/api/v1/users/me",
        json={
            "full_name": new_name,
            "email": email,
        },  # Email is required by schema inheritance but kept same
        headers=headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == new_name
    assert data["email"] == email

    # 3. Verify Persistence
    response = client.get("/api/v1/users/me", headers=headers)
    assert response.json()["full_name"] == new_name

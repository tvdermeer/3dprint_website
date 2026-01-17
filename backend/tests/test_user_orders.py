from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.core.config import settings


def test_create_order_with_user(client: TestClient) -> None:
    # 1. Signup and Login
    email = "order_user@example.com"
    password = "password123"
    client.post(
        "/api/v1/auth/signup",
        json={"email": email, "password": password, "full_name": "Order User"},
    )

    login_res = client.post(
        "/api/v1/auth/login/access-token",
        data={"username": email, "password": password},
    )
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Order as User
    order_data = {
        "customer_email": email,
        "customer_name": "Order User",
        "total_amount": 100.0,
        "items": [{"product_id": 1, "quantity": 1, "price_at_purchase": 100.0}],
    }

    # Need to create a product first or mock it, assuming product id 1 exists or using foreign key checks
    # Since we are using sqlite in memory for tests, we might need to create a product first if FK constraints are enforced.
    # Let's verify if product exists. In test environment, usually tables are empty.

    # Create a product
    client.post(
        "/api/v1/products",
        json={
            "name": "Test Product",
            "description": "Desc",
            "price": 100.0,
            "stock": 10,
            "sku": "TEST-SKU",
            "image_url": "http://example.com/image.png",
        },
    )
    # The product will have ID 1

    response = client.post("/api/v1/orders/", json=order_data, headers=headers)
    assert response.status_code == 201
    created_order = response.json()
    assert created_order["user_id"] is not None

    # 3. Get User Orders
    response = client.get("/api/v1/users/me/orders", headers=headers)
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) == 1
    assert orders[0]["id"] == created_order["id"]


def test_create_order_guest(client: TestClient) -> None:
    # Create product for order
    client.post(
        "/api/v1/products",
        json={
            "name": "Guest Product",
            "description": "Desc",
            "price": 50.0,
            "stock": 10,
            "sku": "GUEST-SKU",
            "image_url": "http://example.com/image.png",
        },
    )
    # Product ID 2 likely

    order_data = {
        "customer_email": "guest@example.com",
        "customer_name": "Guest User",
        "total_amount": 50.0,
        "items": [{"product_id": 2, "quantity": 1, "price_at_purchase": 50.0}],
    }

    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == 201
    created_order = response.json()
    assert created_order["user_id"] is None

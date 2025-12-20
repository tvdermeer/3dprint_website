"""
Tests for order endpoints.
"""
import uuid

def create_test_order(client, sku_suffix=""):
    # First create a product with unique SKU
    sku = f"ORDER-SKU-{uuid.uuid4()}"
    prod_response = client.post(
        "/api/v1/products/",
        json={
            "name": f"Order Product {sku}",
            "price": 50.00,
            "stock": 100,
            "sku": sku
        },
    )
    # If product already exists (from previous test run in same session), try to get it
    if prod_response.status_code == 400:
         # Try to find it or just assume it failed. 
         # Since we use uuid, collision is unlikely.
         pass
         
    if prod_response.status_code != 201:
        # Fallback for debugging, though with UUID it should be fine
        print(f"Failed to create product: {prod_response.json()}")
        
    product_id = prod_response.json()["id"]

    # Create order
    response = client.post(
        "/api/v1/orders/",
        json={
            "customer_email": "test@example.com",
            "customer_name": "Test User",
            "total_amount": 100.00,
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2,
                    "price_at_purchase": 50.00
                }
            ]
        },
    )
    return response

def test_create_order_endpoint(client):
    response = create_test_order(client)
    assert response.status_code == 201
    data = response.json()
    assert data["customer_email"] == "test@example.com"
    assert data["status"] == "pending"
    assert "order_number" in data
    assert "id" in data

def test_get_order(client):
    # Create order first
    response = create_test_order(client)
    order_id = response.json()["id"]

    # Get by ID
    response = client.get(f"/api/v1/orders/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_get_order_by_number(client):
    # Create order first
    response = create_test_order(client)
    order_number = response.json()["order_number"]

    # Get by number
    response = client.get(f"/api/v1/orders/number/{order_number}")
    assert response.status_code == 200
    assert response.json()["order_number"] == order_number

def test_update_order_status(client):
    # Create order first
    response = create_test_order(client)
    order_id = response.json()["id"]

    # Update status
    response = client.post(f"/api/v1/orders/{order_id}/status/paid")
    assert response.status_code == 200
    assert response.json()["status"] == "paid"

    # Invalid status
    response = client.post(f"/api/v1/orders/{order_id}/status/invalid_status")
    assert response.status_code == 400

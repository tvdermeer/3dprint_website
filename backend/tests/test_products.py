"""
Tests for product endpoints.
"""

def test_create_product(client):
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Test Product",
            "description": "A test product",
            "price": 19.99,
            "stock": 10,
            "sku": "TEST-SKU-001",
            "is_active": 1
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert "id" in data
    return data["id"]

def test_read_product(client):
    # First create a product
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Read Me Product",
            "price": 29.99,
            "stock": 5,
            "sku": "READ-SKU-001"
        },
    )
    product_id = response.json()["id"]

    # Read it back
    response = client.get(f"/api/v1/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Read Me Product"
    assert data["price"] == 29.99

def test_read_products_list(client):
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_product(client):
    # Create product
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Update Me Product",
            "price": 10.00,
            "stock": 5,
            "sku": "UPDATE-SKU-001"
        },
    )
    product_id = response.json()["id"]

    # Update it
    response = client.put(
        f"/api/v1/products/{product_id}",
        json={
            "price": 15.00,
            "name": "Updated Product"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 15.00
    assert data["name"] == "Updated Product"

def test_delete_product(client):
    # Create product
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Delete Me Product",
            "price": 5.00,
            "stock": 1,
            "sku": "DELETE-SKU-001"
        },
    )
    product_id = response.json()["id"]

    # Delete it
    response = client.delete(f"/api/v1/products/{product_id}")
    assert response.status_code == 204
    
    # Verify it's gone (or inactive) - Implementation uses soft delete or hard delete?
    # Based on Summary: "Delete (soft)"
    # Let's check if it's inactive or 404
    response = client.get(f"/api/v1/products/{product_id}")
    # Typically API might return 404 for soft deleted items or return them with active=0
    # Let's see what happens. If 200, check is_active.
    if response.status_code == 200:
        data = response.json()
        assert data["is_active"] == 0
    else:
        assert response.status_code == 404

def test_check_stock(client):
    # Create product
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Stock Product",
            "price": 100.00,
            "stock": 10,
            "sku": "STOCK-SKU-001"
        },
    )
    product_id = response.json()["id"]

    # Check stock - sufficient
    response = client.post(
        f"/api/v1/products/{product_id}/check-stock",
        json={"quantity": 5}
    )
    assert response.status_code == 200
    assert response.json()["has_sufficient_stock"] is True

    # Check stock - insufficient
    response = client.post(
        f"/api/v1/products/{product_id}/check-stock",
        json={"quantity": 15}
    )
    assert response.status_code == 200
    assert response.json()["has_sufficient_stock"] is False

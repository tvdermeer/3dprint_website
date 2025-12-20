# API Test Plan

## Overview
This document outlines the testing strategy for the 3D Print Shop API.

## Scope
- **Health Checks**: Verify service availability (Already implemented).
- **Products API**: Verify CRUD operations for products.
- **Orders API**: Verify order creation, retrieval, and status updates.

## Test Cases

### 1. Health Checks (Completed)
- `GET /api/v1/health`: Returns 200 OK with service status.
- `GET /api/v1/ping`: Returns 200 OK with "pong".

### 2. Products API
- **List Products**
  - `GET /api/v1/products`: Returns list of products.
  - Pagination check (limit/skip).
- **Get Product**
  - `GET /api/v1/products/{id}`: Returns product details.
  - `GET /api/v1/products/{invalid_id}`: Returns 404.
- **Create Product**
  - `POST /api/v1/products`: Creates a new product.
  - Validation check (missing fields).
- **Update Product**
  - `PUT /api/v1/products/{id}`: Updates product details.
- **Delete Product**
  - `DELETE /api/v1/products/{id}`: Soft deletes product.
- **Check Stock**
  - `POST /api/v1/products/{id}/check-stock`: Verifies stock availability.

### 3. Orders API
- **Create Order**
  - `POST /api/v1/orders`: Creates a new order with items.
  - Verifies stock reduction (if implemented) or just order creation.
- **Get Order**
  - `GET /api/v1/orders/{id}`: Returns order details.
  - `GET /api/v1/orders/number/{order_number}`: Returns order by number.
- **Update Status**
  - `POST /api/v1/orders/{id}/status/{status}`: Updates order status.

## Execution
Tests will be implemented using `pytest` and `fastapi.testclient.TestClient`.

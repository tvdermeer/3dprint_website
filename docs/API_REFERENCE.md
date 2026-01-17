# 📡 API Reference - 3D Print Shop

Complete reference for all API endpoints.

## Base URL

```
http://localhost:8000/api/v1
```

## Documentation

- **Interactive (Swagger UI)**: http://localhost:8000/docs
- **Read-only (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

## 🏥 Health & Status

### Health Check
```
GET /health
```

**Response** (200 OK)
```json
{
  "status": "healthy",
  "timestamp": "2025-12-20T16:51:17.123456",
  "service": "3D Print Shop API",
  "version": "0.1.0"
}
```

### Ping
```
GET /ping
```

**Response** (200 OK)
```json
{
  "message": "pong"
}
```

---

## 📦 Products

### List Products

```
GET /products
```

**Query Parameters**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | integer | 0 | Number of products to skip |
| limit | integer | 100 | Max products to return (max: 100) |

**Response** (200 OK)
```json
[
  {
    "id": 1,
    "name": "3D Miniature",
    "description": "Detailed miniature figure",
    "price": 19.99,
    "stock": 50,
    "sku": "MINI-001",
    "image_url": "https://example.com/mini.jpg",
    "is_active": true
  }
]
```

### Get Product by ID

```
GET /products/{product_id}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| product_id | integer | Product ID |

**Response** (200 OK)
```json
{
  "id": 1,
  "name": "3D Miniature",
  "description": "Detailed miniature figure",
  "price": 19.99,
  "stock": 50,
  "sku": "MINI-001",
  "image_url": "https://example.com/mini.jpg",
  "is_active": true
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Product not found |

### Create Product

```
POST /products
```

**Request Body**
```json
{
  "name": "3D Miniature",
  "description": "Detailed miniature figure",
  "price": 19.99,
  "stock": 50,
  "sku": "MINI-001",
  "image_url": "https://example.com/mini.jpg",
  "is_active": true
}
```

**Response** (201 Created)
```json
{
  "id": 1,
  "name": "3D Miniature",
  "description": "Detailed miniature figure",
  "price": 19.99,
  "stock": 50,
  "sku": "MINI-001",
  "image_url": "https://example.com/mini.jpg",
  "is_active": true
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 400 | Product with this SKU already exists |
| 422 | Validation error |

### Update Product

```
PUT /products/{product_id}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| product_id | integer | Product ID |

**Request Body** (all fields optional)
```json
{
  "name": "Updated Name",
  "description": "Updated description",
  "price": 24.99,
  "stock": 100,
  "sku": "MINI-002",
  "image_url": "https://example.com/new.jpg",
  "is_active": true
}
```

**Response** (200 OK)
```json
{
  "id": 1,
  "name": "Updated Name",
  "description": "Updated description",
  "price": 24.99,
  "stock": 100,
  "sku": "MINI-002",
  "image_url": "https://example.com/new.jpg",
  "is_active": true
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Product not found |
| 422 | Validation error |

### Delete Product

```
DELETE /products/{product_id}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| product_id | integer | Product ID |

**Response** (204 No Content)

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Product not found |

### Check Stock

```
POST /products/{product_id}/check-stock
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| product_id | integer | Product ID |

**Query Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| quantity | integer | Quantity to check |

**Response** (200 OK)
```json
{
  "product_id": 1,
  "requested_quantity": 10,
  "available_stock": 50,
  "has_sufficient_stock": true
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Product not found |

---

## 🛒 Orders

### List Orders

```
GET /orders
```

**Query Parameters**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | integer | 0 | Number of orders to skip |
| limit | integer | 100 | Max orders to return (max: 100) |

**Response** (200 OK)
```json
[
  {
    "id": 1,
    "order_number": "ORD-20251220-A1B2C3D4",
    "customer_email": "john@example.com",
    "customer_name": "John Doe",
    "total_amount": 99.99,
    "status": "pending",
    "stripe_payment_id": null,
    "created_at": "2025-12-20T16:51:17.123456",
    "updated_at": "2025-12-20T16:51:17.123456"
  }
]
```

### Get Order by ID

```
GET /orders/{order_id}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_id | integer | Order ID |

**Response** (200 OK)
```json
{
  "id": 1,
  "order_number": "ORD-20251220-A1B2C3D4",
  "customer_email": "john@example.com",
  "customer_name": "John Doe",
  "total_amount": 99.99,
  "status": "pending",
  "stripe_payment_id": null,
  "created_at": "2025-12-20T16:51:17.123456",
  "updated_at": "2025-12-20T16:51:17.123456"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Order not found |

### Get Order by Number

```
GET /orders/number/{order_number}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_number | string | Order number (e.g., ORD-20251220-A1B2C3D4) |

**Response** (200 OK)
```json
{
  "id": 1,
  "order_number": "ORD-20251220-A1B2C3D4",
  "customer_email": "john@example.com",
  "customer_name": "John Doe",
  "total_amount": 99.99,
  "status": "pending",
  "stripe_payment_id": null,
  "created_at": "2025-12-20T16:51:17.123456",
  "updated_at": "2025-12-20T16:51:17.123456"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Order not found |

### Get Customer Orders

```
GET /orders/customer/{email}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| email | string | Customer email address |

**Query Parameters**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | integer | 0 | Number of orders to skip |
| limit | integer | 50 | Max orders to return (max: 100) |

**Response** (200 OK)
```json
[
  {
    "id": 1,
    "order_number": "ORD-20251220-A1B2C3D4",
    "customer_email": "john@example.com",
    "customer_name": "John Doe",
    "total_amount": 99.99,
    "status": "pending",
    "stripe_payment_id": null,
    "created_at": "2025-12-20T16:51:17.123456",
    "updated_at": "2025-12-20T16:51:17.123456"
  }
]
```

### Create Order

```
POST /orders
```

**Request Body**
```json
{
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "total_amount": 99.99,
  "status": "pending"
}
```

**Response** (201 Created)
```json
{
  "id": 1,
  "order_number": "ORD-20251220-A1B2C3D4",
  "customer_email": "john@example.com",
  "customer_name": "John Doe",
  "total_amount": 99.99,
  "status": "pending",
  "stripe_payment_id": null,
  "created_at": "2025-12-20T16:51:17.123456",
  "updated_at": "2025-12-20T16:51:17.123456"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 422 | Validation error (invalid email, etc.) |

### Update Order

```
PUT /orders/{order_id}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_id | integer | Order ID |

**Request Body** (all fields optional)
```json
{
  "status": "paid",
  "stripe_payment_id": "pi_1234567890"
}
```

**Response** (200 OK)
```json
{
  "id": 1,
  "order_number": "ORD-20251220-A1B2C3D4",
  "customer_email": "john@example.com",
  "customer_name": "John Doe",
  "total_amount": 99.99,
  "status": "paid",
  "stripe_payment_id": "pi_1234567890",
  "created_at": "2025-12-20T16:51:17.123456",
  "updated_at": "2025-12-20T16:51:17.123456"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Order not found |
| 422 | Validation error |

### Update Order Status

```
POST /orders/{order_id}/status/{new_status}
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_id | integer | Order ID |
| new_status | string | Status: pending, paid, shipped, delivered, cancelled |

**Response** (200 OK)
```json
{
  "id": 1,
  "order_number": "ORD-20251220-A1B2C3D4",
  "customer_email": "john@example.com",
  "customer_name": "John Doe",
  "total_amount": 99.99,
  "status": "shipped",
  "stripe_payment_id": null,
  "created_at": "2025-12-20T16:51:17.123456",
  "updated_at": "2025-12-20T16:51:17.123456"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Order not found |
| 400 | Invalid status |

### Process Payment

```
POST /orders/{order_id}/process-payment
```

**Path Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_id | integer | Order ID |

**Request Body**
```json
{
  "stripe_payment_id": "pi_1234567890"
}
```

**Response** (200 OK)
```json
{
  "status": "success",
  "message": "Payment processed",
  "order_id": 1,
  "payment_id": "pi_1234567890"
}
```

**Errors**
| Status | Description |
|--------|-------------|
| 404 | Order not found |
| 400 | Order not in pending status |

---

## 🔄 Data Models

### Product
```json
{
  "id": "integer",
  "name": "string (required, 1-255 chars)",
  "description": "string or null (max 2000 chars)",
  "price": "float (required, > 0)",
  "stock": "integer (required, >= 0)",
  "sku": "string (required, unique, 1-100 chars)",
  "image_url": "string or null (max 500 chars)",
  "is_active": "boolean (default: true)"
}
```

### Order
```json
{
  "id": "integer",
  "order_number": "string (unique, auto-generated)",
  "customer_email": "string (required, valid email)",
  "customer_name": "string (required, 1-255 chars)",
  "total_amount": "float (required, > 0)",
  "status": "string (pending, paid, shipped, delivered, cancelled)",
  "stripe_payment_id": "string or null",
  "created_at": "ISO8601 datetime",
  "updated_at": "ISO8601 datetime"
}
```

---

## 🔧 Testing with cURL

### Test Health Check
```bash
curl http://localhost:8000/api/v1/health
```

### Create a Product
```bash
curl -X POST "http://localhost:8000/api/v1/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "sku": "TEST-001",
    "price": 29.99,
    "stock": 100
  }'
```

### List Products
```bash
curl "http://localhost:8000/api/v1/products"
```

### Create an Order
```bash
curl -X POST "http://localhost:8000/api/v1/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "total_amount": 99.99
  }'
```

### Get Customer Orders
```bash
curl "http://localhost:8000/api/v1/orders/customer/john@example.com"
```

### Update Order Status
```bash
curl -X POST "http://localhost:8000/api/v1/orders/1/status/paid"
```

---

## 📊 Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created |
| 204 | No Content - Successful with no body |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource doesn't exist |
| 422 | Validation Error - Data validation failed |
| 500 | Internal Server Error |

---

## ⏱️ Rate Limiting

Currently no rate limiting. Will be added in future phases.

---

## 🔐 Authentication

Currently not implemented. JWT authentication will be added in Phase 5.

---

## 📝 Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

Example:
```json
{
  "detail": "Product with ID 999 not found"
}
```

---

## 🔄 Pagination

List endpoints support pagination via query parameters:

- `skip`: Number of items to skip (default: 0)
- `limit`: Maximum items to return (default: 100, max: 100)

Example:
```
GET /products?skip=10&limit=20
```

Returns items 11-30.

---

## 📅 Timestamps

All timestamps are in ISO 8601 format with UTC timezone:
```
2025-12-20T16:51:17.123456
```

---

## 🎯 Common Use Cases

### Scenario 1: Display Products
1. `GET /products` - Fetch all products
2. Display in frontend

### Scenario 2: Create an Order
1. `POST /orders` - Create new order
2. Store order_number and order_id
3. Display to customer

### Scenario 3: Check Order Status
1. `GET /orders/{order_id}` or
2. `GET /orders/number/{order_number}`
3. Display current status

### Scenario 4: Process Payment
1. Create order with `POST /orders`
2. Get payment ID from Stripe
3. `POST /orders/{id}/process-payment` - Update payment
4. `POST /orders/{id}/status/paid` - Mark as paid

---

## 📚 Full Documentation

See `backend/README.md` for comprehensive documentation.

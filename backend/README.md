# 3D Print Shop API Backend

FastAPI-based REST API for a 3D printing e-commerce platform.

## Quick Start

### Prerequisites

- Python 3.10+
- Virtual environment (venv)

### Installation

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   python main.py
   # Or with uvicorn directly:
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── health.py       # Health check endpoints
│   │           ├── products.py     # Product CRUD endpoints
│   │           ├── orders.py       # Order management endpoints
│   │           └── __init__.py
│   ├── models/
│   │   ├── product.py             # Product ORM model
│   │   ├── order.py               # Order ORM model
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── product.py             # Product Pydantic schemas
│   │   ├── order.py               # Order Pydantic schemas
│   │   └── __init__.py
│   ├── services/
│   │   ├── product_service.py     # Product business logic
│   │   ├── order_service.py       # Order business logic
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py              # Configuration management
│   │   ├── database.py            # Database setup
│   │   ├── security.py            # JWT and password utilities
│   │   └── __init__.py
│   ├── main.py                     # FastAPI app factory
│   └── __init__.py
├── tests/
│   ├── test_health.py             # Health check tests
│   └── __init__.py
├── main.py                         # Entry point
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
└── README.md
```

## API Documentation

### Interactive Docs

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Endpoints

#### Health Check

- `GET /api/v1/health` - Health check with timestamp
- `GET /api/v1/ping` - Simple ping

#### Products

- `GET /api/v1/products` - List all products
- `GET /api/v1/products/{id}` - Get product by ID
- `POST /api/v1/products` - Create new product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product (soft delete)
- `POST /api/v1/products/{id}/check-stock` - Check stock availability

#### Orders

- `GET /api/v1/orders` - List all orders
- `GET /api/v1/orders/{id}` - Get order by ID
- `GET /api/v1/orders/number/{order_number}` - Get order by number
- `GET /api/v1/orders/customer/{email}` - Get orders by customer email
- `POST /api/v1/orders` - Create new order
- `PUT /api/v1/orders/{id}` - Update order
- `POST /api/v1/orders/{id}/status/{new_status}` - Update order status
- `POST /api/v1/orders/{id}/process-payment` - Process payment

## Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Application
APP_NAME=3D Print Shop API
DEBUG=True
ENVIRONMENT=development

# Database
DATABASE_URL=sqlite:///./ecommerce.db

# Security
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]
```

## Database

### SQLite (Development)

SQLite is used by default for development. The database file (`ecommerce.db`) is created automatically.

### Migrations

Migrations are managed with Alembic (future implementation).

## Testing

Run tests with pytest:

```bash
pip install pytest pytest-asyncio httpx
pytest
```

## Code Quality

### Linting and Formatting

```bash
# Format code with Black
black app tests

# Check style with Flake8
flake8 app tests

# Type checking with mypy
mypy app --strict
```

## Features

### ✅ Implemented

- RESTful API with FastAPI
- SQLAlchemy ORM with SQLite
- Product management (CRUD)
- Order management
- Health check endpoints
- CORS middleware
- Automatic API documentation (Swagger UI)
- Type hints with Pydantic
- Security utilities (JWT tokens, password hashing)

### 🚧 In Progress

- Authentication endpoints
- Payment processing (Stripe integration)
- Database migrations (Alembic)

### 📋 Planned

- WebSocket for real-time updates
- Email notifications
- Inventory management
- Admin dashboard endpoints
- Comprehensive error handling
- Request logging and monitoring

## Common Tasks

### Create a Product

```bash
curl -X POST "http://localhost:8000/api/v1/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Model X",
    "sku": "MOD-X-001",
    "price": 29.99,
    "stock": 50,
    "description": "High quality 3D printed model",
    "is_active": true
  }'
```

### Get All Products

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
    "total_amount": 99.99,
    "status": "pending"
  }'
```

## Troubleshooting

### Port Already in Use

```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

### Database Locked

SQLite can lock the database if multiple processes access it. For production, migrate to PostgreSQL.

### Import Errors

Ensure you're in the virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Contributing

1. Create a feature branch
2. Write tests for new features
3. Run linters and tests before committing
4. Follow the existing code style

## License

MIT

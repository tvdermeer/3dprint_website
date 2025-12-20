# 🚀 Quick Start Guide

Get the 3D Print Shop API and Frontend up and running in minutes!

## Backend Setup (FastAPI)

### 1. Install Dependencies

```bash
cd backend

# Create virtual environment (if not already created)
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Create Environment File

```bash
# The .env file will use default values for local development
# These defaults are defined in app/core/config.py
# For custom configuration, create a .env file in the backend directory
```

### 3. Run the Backend Server

```bash
# From backend directory
python main.py

# Or use uvicorn directly for more control
uvicorn app.main:app --reload --port 8000
```

You should see:
```
🚀 Starting 3D Print Shop API v0.1.0
Environment: development
Debug: True
```

The API is now running at: **http://localhost:8000**

### 4. Explore the API

Open your browser and visit the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Try these endpoints:
- `GET /api/v1/ping` - Test the server
- `GET /api/v1/health` - Check server status
- `GET /api/v1/products` - List products (empty initially)

---

## Frontend Setup (Vue 3)

### 1. Install Dependencies

```bash
cd frontend

# Install npm packages
npm install
```

### 2. Run the Frontend Server

```bash
# From frontend directory
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
```

The frontend is now running at: **http://localhost:5173**

### 3. Access the Application

Open your browser and visit: http://localhost:5173

---

## Testing the Full Stack

### 1. Create a Product (via API)

```bash
curl -X POST "http://localhost:8000/api/v1/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "3D Printed Miniature",
    "sku": "MINI-001",
    "price": 19.99,
    "stock": 100,
    "description": "High quality 3D printed miniature",
    "is_active": true
  }'
```

Or use Swagger UI: http://localhost:8000/docs

### 2. View Products in API

```bash
curl "http://localhost:8000/api/v1/products"
```

### 3. Fetch Products from Frontend (Next Step)

We'll create a Vue component to fetch and display products from the API.

---

## Verify Everything Works

### Backend Health Check

```bash
curl http://localhost:8000/api/v1/health

# Expected response:
# {
#   "status": "healthy",
#   "timestamp": "2025-12-20T16:50:00.000000",
#   "service": "3D Print Shop API",
#   "version": "0.1.0"
# }
```

### Frontend is Running

Visit: http://localhost:5173

You should see the Vue.js app (currently just says "You did it!")

---

## Common Issues & Solutions

### Backend Port Already in Use

```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

### Frontend Port Already in Use

```bash
# Vite will automatically use the next available port
# Or specify explicitly
npm run dev -- --port 3000
```

### Import Errors in Backend

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### CORS Errors from Frontend

The CORS is already configured to allow `localhost:5173`. If you get CORS errors:

1. Check that the backend is running on port 8000
2. Check your frontend is on port 5173
3. Restart the backend server

---

## Next Steps

### 1. Setup Frontend API Client
Create `frontend/src/api/client.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1';

export const fetchProducts = async () => {
  const response = await fetch(`${API_BASE_URL}/products`);
  return response.json();
};

export const createOrder = async (orderData) => {
  const response = await fetch(`${API_BASE_URL}/orders`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(orderData),
  });
  return response.json();
};
```

### 2. Create Product Component
Create a Vue component to display products:
- Fetch products on mount
- Display in grid or list
- Add to cart functionality

### 3. Create Order Component
Create a checkout component to:
- Display cart items
- Collect customer info
- Submit order to backend

### 4. Test Frontend-Backend Integration
- Fetch and display products
- Create orders
- Check order status

---

## Development Workflow

### Terminal 1: Backend
```bash
cd backend
source .venv/bin/activate
python main.py
```

### Terminal 2: Frontend
```bash
cd frontend
npm run dev
```

### Terminal 3: Optional - Test Commands
```bash
# View products
curl http://localhost:8000/api/v1/products

# Create product
curl -X POST http://localhost:8000/api/v1/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","sku":"TEST-1","price":9.99,"stock":10}'

# Create order
curl -X POST http://localhost:8000/api/v1/orders \
  -H "Content-Type: application/json" \
  -d '{"customer_name":"John","customer_email":"john@example.com","total_amount":99.99}'
```

---

## API Endpoints Reference

### Products
- `GET /api/v1/products` - List all products
- `POST /api/v1/products` - Create product
- `GET /api/v1/products/{id}` - Get product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product

### Orders
- `GET /api/v1/orders` - List all orders
- `POST /api/v1/orders` - Create order
- `GET /api/v1/orders/{id}` - Get order
- `GET /api/v1/orders/customer/{email}` - Get customer orders

### Health
- `GET /api/v1/health` - Server status
- `GET /api/v1/ping` - Simple ping

---

## Full API Documentation

See the comprehensive guides:
- **Backend**: `backend/README.md`
- **Frontend**: `frontend/README.md`
- **Project Setup**: `BACKEND_SETUP.md`

---

**You're all set! The backend and frontend are ready to communicate. Start with Phase 4: Integration.** 🎉

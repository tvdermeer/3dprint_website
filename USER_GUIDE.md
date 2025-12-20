# AXYS E-Commerce - User Guide

This guide explains how to run the full stack application (Frontend + Backend) for development.

## Prerequisites
- Node.js 18+
- Python 3.10+
- `uv` (Python package manager)

## 1. Backend Setup

The backend is built with FastAPI and SQLite.

### Installation
```bash
cd backend
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Database Seeding
Initialize the database with the default product:
```bash
uv run python seed_db.py
```

### Running the Server
```bash
# Runs on http://localhost:8000
uv run uvicorn app.main:app --reload
```
API Documentation is available at http://localhost:8000/docs.

## 2. Frontend Setup

The frontend is built with Vue 3 and Vite.

### Installation
```bash
cd frontend
npm install
```

### Configuration
Ensure `.env` exists with the correct API URL:
```ini
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

### Running the Development Server
```bash
# Runs on http://localhost:5173
npm run dev
```

## 3. Usage Flow

1. **Start Backend**: Ensure port 8000 is active.
2. **Start Frontend**: Open http://localhost:5173.
3. **Browse**: Go to the Product page. You should see "AXYS Premium Golf Cleaner" loaded from the backend.
4. **Cart**: Add items to cart.
5. **Checkout**: Proceed to checkout and fill in the form (mock payment).
6. **Order**: Click "Place Order".
   - Frontend sends `POST` to backend.
   - Backend creates order in SQLite.
   - Frontend clears cart and shows success message.

## 4. Deployment (Production)

### Backend
- Use a production WSGI/ASGI server like Gunicorn with Uvicorn workers.
- Set `DEBUG=False` in environment.
- Use PostgreSQL instead of SQLite.

### Frontend
- Build static files:
  ```bash
  npm run build
  ```
- Serve the `dist/` directory using Nginx, Apache, or a static host (Netlify, Vercel).

## 5. Troubleshooting

- **CORS Errors**: Check `backend/.env` (or config) `CORS_ORIGINS`. It must match the frontend URL.
- **Connection Refused**: Ensure Backend is running on port 8000.
- **Empty Product Page**: Ensure `seed_db.py` was run to populate the database.

# 3D Print Shop Codebase Guide

This document provides essential instructions for AI agents operating in this repository.

## 1. Project Overview

This is a full-stack e-commerce application for 3D printed products.
- **Backend:** Python (FastAPI, SQLAlchemy, Pydantic)
- **Frontend:** Vue 3 (Vite, Tailwind CSS, Pinia)
- **Database:** SQLite (dev), Alembic migrations

## 2. Build, Test, and Lint Commands

### Backend (`/backend`)
Run these commands from the `backend/` directory.

- **Install Dependencies:**
  ```bash
  # Using pip
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  
  # Using uv (if available)
  uv pip install -r requirements.txt
  ```

- **Run Server:**
  ```bash
  python main.py
  # OR
  uvicorn app.main:app --reload
  ```

- **Run Tests:**

  use the test-execution skill to run tests
  ```bash
  pytest
  
  # Run a specific test file
  pytest tests/test_health.py
  
  # Run a specific test case
  pytest tests/test_health.py::test_health_check
  ```

- **Linting & Formatting:**
  ```bash
  black app tests
  isort app tests
  flake8 app tests
  mypy app --strict
  ```

### Frontend (`/frontend`)
Run these commands from the `frontend/` directory.

- **Install Dependencies:**
  ```bash
  npm install
  ```

- **Run Development Server:**
  ```bash
  npm run dev
  ```

- **Build for Production:**
  ```bash
  npm run build
  ```

- **Run Tests (E2E):**
  use the test-execution skill to run tests

  ```bash
  # Run all Playwright tests
  npx playwright test
  
  # Run specific test file
  npx playwright test tests/example.spec.js
  ```

## 3. Code Style & Conventions

### Backend (Python)
- **Architecture:** Follow the layered architecture: `api` -> `services` -> `models/schemas`.
- **Type Hints:** strictly enforced. Use `Pydantic` models for schemas and `SQLAlchemy` models for DB.
- **Formatting:** Code **must** be formatted with `Black`.
- **Imports:** Use absolute imports (e.g., `from app.core.config import settings`).
- **Async:** Use `async/await` for all route handlers and DB operations.
- **Error Handling:** Use `HTTPException` for API errors. Avoid bare `try/except`.

### Frontend (Vue.js)
- **Component Style:** Use **Composition API** with `<script setup>`.
- **Styling:** Use **Tailwind CSS** utility classes. Avoid custom CSS unless necessary.
- **State Management:** Use **Pinia** for global state.
- **Routing:** Use **Vue Router**.
- **Icons:** Use `lucide-vue-next`.
- **Naming:**
  - Components: PascalCase (e.g., `ProductCard.vue`).
  - Composables: camelCase with use prefix (e.g., `useCart.js`).
  - Files: camelCase for non-components.

### General
- **Pathing:** Always use **absolute paths** when reading/writing files in tool calls.
- **Testing:** Write tests for new features. Backend: `pytest` (unit/integration). Frontend: `playwright` (e2e).
- **Secrets:** Never commit secrets. Use `.env` files (see `backend/README.md`).

## 4. Documentation
- **Backend API:** Available at `http://localhost:8000/docs` (Swagger UI).
- **Component Docs:** See `frontend/COMPONENT_DOCS.md` (if available).

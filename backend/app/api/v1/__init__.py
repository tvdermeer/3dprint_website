"""
API v1 router combining all endpoints.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health, orders, products

# Create main API router
api_router = APIRouter(prefix="/api/v1")

# Include all endpoint routers
api_router.include_router(health.router)
api_router.include_router(products.router)
api_router.include_router(orders.router)

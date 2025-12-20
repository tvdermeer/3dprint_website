"""
Product API endpoints.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[ProductResponse])
def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> List[ProductResponse]:
    """
    List all active products with pagination.

    - **skip**: Number of products to skip (default: 0)
    - **limit**: Maximum products to return (default: 100, max: 100)
    """
    if limit > 100:
        limit = 100
    products = ProductService.get_all_products(db, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    """Get a product by ID."""
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
    return product


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
) -> ProductResponse:
    """Create a new product."""
    # Check if product with same SKU exists
    existing = ProductService.get_product_by_sku(db, product.sku)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product with SKU {product.sku} already exists",
        )

    new_product = ProductService.create_product(db, product)
    return new_product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
) -> ProductResponse:
    """Update an existing product."""
    product = ProductService.update_product(db, product_id, product_update)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)) -> None:
    """Delete (soft delete) a product by ID."""
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )


from pydantic import BaseModel, Field


class CheckStockRequest(BaseModel):
    quantity: int = Field(..., gt=0, description="Quantity to check")


@router.post("/{product_id}/check-stock")
def check_stock(
    product_id: int,
    request: CheckStockRequest,
    db: Session = Depends(get_db),
) -> dict:
    """Check if a product has sufficient stock."""
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )

    has_stock = ProductService.check_stock(db, product_id, request.quantity)
    return {
        "product_id": product_id,
        "requested_quantity": request.quantity,
        "available_stock": product.stock,
        "has_sufficient_stock": has_stock,
    }

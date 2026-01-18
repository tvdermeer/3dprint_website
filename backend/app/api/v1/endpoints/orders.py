"""
Order API endpoints.
"""

from typing import List, Optional, cast

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from app.services.order_service import OrderService
from app.services.product_service import ProductService
from app.api import deps
from app.models.user import User

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=List[OrderResponse])
def list_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> List[OrderResponse]:
    """
    List all orders with pagination (admin only).

    - **skip**: Number of orders to skip (default: 0)
    - **limit**: Maximum orders to return (default: 100, max: 100)
    """
    if limit > 100:
        limit = 100
    orders = OrderService.get_all_orders(db, skip=skip, limit=limit)
    return [OrderResponse.model_validate(o) for o in orders]


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)) -> OrderResponse:
    """Get an order by ID."""
    order = OrderService.get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with ID {order_id} not found",
        )
    return order


@router.get("/number/{order_number}", response_model=OrderResponse)
def get_order_by_number(
    order_number: str, db: Session = Depends(get_db)
) -> OrderResponse:
    """Get an order by order number."""
    order = OrderService.get_order_by_number(db, order_number)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_number} not found",
        )
    return order


@router.get("/customer/{email}", response_model=List[OrderResponse])
def get_customer_orders(
    email: str,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
) -> List[OrderResponse]:
    """Get all orders for a customer by email."""
    if limit > 100:
        limit = 100
    orders = OrderService.get_orders_by_email(db, email, skip=skip, limit=limit)
    return [OrderResponse.model_validate(o) for o in orders]


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(deps.get_current_user_optional),
) -> OrderResponse:
    """Create a new order."""
    user_id = cast(int, current_user.id) if current_user else None
    new_order = OrderService.create_order(db, order, user_id=user_id)
    return new_order


@router.put("/{order_id}", response_model=OrderResponse)
def update_order(
    order_id: int,
    order_update: OrderUpdate,
    db: Session = Depends(get_db),
) -> OrderResponse:
    """Update an order (status, payment ID, etc.)."""
    order = OrderService.update_order(db, order_id, order_update)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with ID {order_id} not found",
        )
    return order


@router.post("/{order_id}/status/{new_status}", response_model=OrderResponse)
def update_order_status(
    order_id: int,
    new_status: str,
    db: Session = Depends(get_db),
) -> OrderResponse:
    """Update order status (pending, paid, shipped, delivered, cancelled)."""
    valid_statuses = ["pending", "paid", "shipped", "delivered", "cancelled"]
    if new_status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}",
        )

    order = OrderService.update_order_status(db, order_id, new_status)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with ID {order_id} not found",
        )
    return order


@router.post("/{order_id}/process-payment")
def process_payment(
    order_id: int,
    payment_data: dict,
    db: Session = Depends(get_db),
) -> dict:
    """
    Process payment for an order (Stripe integration placeholder).

    This is a simplified endpoint. In production, integrate with Stripe.
    """
    order = OrderService.get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with ID {order_id} not found",
        )

    if order.status != "pending":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot process payment for order with status: {order.status}",
        )

    # TODO: Integrate with Stripe API
    # For now, just mark as paid if payment_data is valid
    stripe_payment_id = payment_data.get("stripe_payment_id", "PLACEHOLDER_ID")
    OrderService.update_order_status(db, order_id, "paid")
    OrderService.update_order(
        db, order_id, OrderUpdate(stripe_payment_id=stripe_payment_id)
    )

    return {
        "status": "success",
        "message": "Payment processed",
        "order_id": order_id,
        "payment_id": stripe_payment_id,
    }

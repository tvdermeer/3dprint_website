"""
User API endpoints.
"""

from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.core.database import get_db
from app.models.user import User
from app.schemas.order import OrderResponse
from app.schemas.user import UserResponse, UserUpdate
from app.services.order_service import OrderService
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
def read_user_me(
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.get("/me/orders", response_model=List[OrderResponse])
def read_user_orders(
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(deps.get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Get current user's orders.
    """
    return OrderService.get_orders_by_user_id(
        db, user_id=current_user.id, skip=skip, limit=limit
    )


@router.put("/me", response_model=UserResponse)
def update_user_me(
    user_in: UserUpdate,
    current_user: User = Depends(deps.get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Update own user.
    """
    user = UserService.update_user(db, current_user, user_in)
    return user

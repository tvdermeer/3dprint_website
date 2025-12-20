"""
Pydantic schemas for Order request/response validation.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class OrderItemBase(BaseModel):
    """Base schema for order items."""

    product_id: int = Field(..., description="ID of the product purchased")
    quantity: int = Field(..., gt=0, description="Quantity purchased")
    price_at_purchase: float = Field(..., gt=0, description="Price per unit at time of purchase")


class OrderItemCreate(OrderItemBase):
    """Schema for creating an order item."""

    pass


class OrderItemResponse(OrderItemBase):
    """Schema for order item response."""

    id: int = Field(..., description="Unique item ID")
    # We could include product details here if needed, but keeping it simple for now

    class Config:
        """Pydantic config."""

        from_attributes = True


class OrderBase(BaseModel):
    """Base order schema with common fields."""

    customer_email: EmailStr = Field(..., description="Customer email address")
    customer_name: str = Field(..., min_length=1, max_length=255, description="Customer name")
    total_amount: float = Field(..., gt=0, description="Order total in USD")


class OrderCreate(OrderBase):
    """Schema for creating a new order."""

    status: str = Field(default="pending", description="Initial order status")
    items: List[OrderItemCreate] = Field(..., description="List of items in the order")
    stripe_payment_id: Optional[str] = Field(None, description="Stripe payment intent ID")


class OrderUpdate(BaseModel):
    """Schema for updating an existing order."""

    status: Optional[str] = Field(None, description="Order status")
    stripe_payment_id: Optional[str] = Field(None, description="Stripe payment intent ID")


class OrderResponse(OrderBase):
    """Schema for order responses from API."""

    id: int = Field(..., description="Unique order ID")
    order_number: str = Field(..., description="Human-readable order number")
    status: str = Field(..., description="Current order status")
    stripe_payment_id: Optional[str] = Field(None, description="Stripe payment ID")
    created_at: datetime = Field(..., description="Order creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    items: List[OrderItemResponse] = Field(default=[], description="List of items in the order")

    class Config:
        """Pydantic config."""

        from_attributes = True

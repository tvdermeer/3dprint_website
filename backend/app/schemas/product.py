"""
Pydantic schemas for Product request/response validation.
"""

from typing import Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    """Base product schema with common fields."""

    name: str = Field(..., min_length=1, max_length=255, description="Product name")
    description: Optional[str] = Field(None, max_length=2000, description="Product description")
    price: float = Field(..., gt=0, description="Product price in USD")
    stock: int = Field(default=0, ge=0, description="Available stock quantity")
    sku: str = Field(..., min_length=1, max_length=100, description="Stock keeping unit")
    image_url: Optional[str] = Field(None, max_length=500, description="Product image URL")
    is_active: bool = Field(default=True, description="Whether product is active")


class ProductCreate(ProductBase):
    """Schema for creating a new product."""

    pass


class ProductUpdate(BaseModel):
    """Schema for updating an existing product."""

    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    sku: Optional[str] = Field(None, min_length=1, max_length=100)
    image_url: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    """Schema for product responses from API."""

    id: int = Field(..., description="Unique product ID")

    class Config:
        """Pydantic config."""

        from_attributes = True

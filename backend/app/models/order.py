"""
Order model for SQLAlchemy ORM.
"""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Order(Base):
    """Order model representing a customer purchase."""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, index=True, nullable=False)
    customer_email = Column(String(255), index=True, nullable=False)
    customer_name = Column(String(255), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(
        String(50), default="pending"
    )  # pending, paid, shipped, delivered, cancelled
    stripe_payment_id = Column(String(255), nullable=True, unique=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship to items
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Order(id={self.id}, order_number={self.order_number}, status={self.status})>"


class OrderItem(Base):
    """OrderItem model representing a line item in an order."""

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Float, nullable=False)

    # Relationships
    order = relationship("Order", back_populates="items")
    product = relationship("app.models.product.Product")

    def __repr__(self) -> str:
        return f"<OrderItem(id={self.id}, product_id={self.product_id}, quantity={self.quantity})>"

"""
Business logic for order operations.
"""

from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate, OrderUpdate


class OrderService:
    """Service for order operations."""

    @staticmethod
    def generate_order_number() -> str:
        """Generate a unique order number."""
        # Format: ORD-YYYYMMDD-XXXXX
        timestamp = datetime.now().strftime("%Y%m%d")
        unique_id = str(uuid4())[:8].upper()
        return f"ORD-{timestamp}-{unique_id}"

    @staticmethod
    def create_order(db: Session, order: OrderCreate) -> Order:
        """Create a new order with items."""
        # Create the order
        db_order = Order(
            order_number=OrderService.generate_order_number(),
            customer_email=order.customer_email,
            customer_name=order.customer_name,
            total_amount=order.total_amount,
            status=order.status,
        )
        db.add(db_order)
        db.flush()  # Flush to get the ID for the order

        # Create order items
        for item_data in order.items:
            db_item = OrderItem(
                order_id=db_order.id,
                product_id=item_data.product_id,
                quantity=item_data.quantity,
                price_at_purchase=item_data.price_at_purchase,
            )
            db.add(db_item)

        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def get_order_by_id(db: Session, order_id: int) -> Optional[Order]:
        """Get an order by ID."""
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_order_by_number(db: Session, order_number: str) -> Optional[Order]:
        """Get an order by order number."""
        return db.query(Order).filter(Order.order_number == order_number).first()

    @staticmethod
    def get_orders_by_email(db: Session, email: str, skip: int = 0, limit: int = 50) -> list[
        Order
    ]:
        """Get all orders for a customer email."""
        return (
            db.query(Order)
            .filter(Order.customer_email == email)
            .order_by(Order.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def update_order_status(db: Session, order_id: int, new_status: str) -> Optional[Order]:
        """Update order status."""
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            return None

        db_order.status = new_status
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def update_order(db: Session, order_id: int, order_update: OrderUpdate) -> Optional[Order]:
        """Update an order."""
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            return None

        update_data = order_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_order, key, value)

        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def get_all_orders(db: Session, skip: int = 0, limit: int = 100) -> list[Order]:
        """Get all orders with pagination."""
        return db.query(Order).order_by(Order.created_at.desc()).offset(skip).limit(limit).all()

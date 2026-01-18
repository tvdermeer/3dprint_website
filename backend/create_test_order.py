import asyncio
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.order_service import OrderService
from app.schemas.order import OrderCreate, OrderItemCreate


def create_test_order():
    db: Session = SessionLocal()
    try:
        payment_id = "pi_LOCALTEST"
        order_data = OrderCreate(
            customer_email="test@example.com",
            customer_name="Test User",
            total_amount=53.18,
            stripe_payment_id=payment_id,
            items=[OrderItemCreate(product_id=1, quantity=1, price_at_purchase=39.99)],
        )

        order = OrderService.create_order(db, order_data)
        print(
            f"Successfully created order {order.order_number} with status '{order.status}' and payment ID '{order.stripe_payment_id}'"
        )

    finally:
        db.close()


if __name__ == "__main__":
    create_test_order()

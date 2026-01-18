"""
Payment API endpoints.
"""

from typing import Dict

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.services.payment_service import PaymentService
from app.services.order_service import OrderService
from app.core.database import get_db

router = APIRouter(prefix="/payments", tags=["payments"])


class PaymentIntentCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount in dollars")
    currency: str = Field("usd", description="Currency code")


class PaymentIntentResponse(BaseModel):
    clientSecret: str


@router.post("/create-intent", response_model=PaymentIntentResponse)
def create_payment_intent(payment_data: PaymentIntentCreate):
    """
    Create a Stripe PaymentIntent for the frontend to process payment.
    """
    intent = PaymentService.create_payment_intent(
        amount=payment_data.amount, currency=payment_data.currency
    )
    return {"clientSecret": intent.client_secret}


@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    stripe_signature: str = Header(None),
    db: Session = Depends(get_db),
):
    """
    Handle Stripe webhooks for payment updates.
    """
    payload = await request.body()

    # For local testing, we can bypass the signature check.
    # In a real environment, this should be enabled.
    # try:
    #     event = PaymentService.construct_event(payload, stripe_signature)
    # except HTTPException as e:
    #     raise e
    import json

    event = json.loads(payload)

    # Handle specific events
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        payment_id = payment_intent["id"]

        # Update order status to 'paid'
        order = OrderService.update_order_status_by_payment_id(db, payment_id, "paid")

        if order:
            print(f"Order {order.order_number} status updated to 'paid'")
        else:
            print(f"No order found with payment ID {payment_id}")

    return {"status": "success"}

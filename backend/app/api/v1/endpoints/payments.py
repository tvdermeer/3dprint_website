"""
Payment API endpoints.
"""

from typing import Dict

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from pydantic import BaseModel, Field

from app.services.payment_service import PaymentService

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
        amount=payment_data.amount,
        currency=payment_data.currency
    )
    return {"clientSecret": intent.client_secret}


@router.post("/webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    """
    Handle Stripe webhooks for payment updates.
    """
    payload = await request.body()
    
    try:
        event = PaymentService.construct_event(payload, stripe_signature)
    except HTTPException as e:
        raise e

    # Handle specific events
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        # TODO: Update order status here
        print(f"Payment for {payment_intent['amount']} succeeded")
        
    return {"status": "success"}

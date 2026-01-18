"""
Payment service handling Stripe integration.
"""

from typing import Any
import stripe
import stripe.error
from fastapi import HTTPException

from app.core.config import settings

# Initialize Stripe
stripe.api_key = settings.stripe_secret_key


class PaymentService:
    @staticmethod
    def create_payment_intent(amount: float, currency: str = "usd") -> Any:
        """
        Create a Stripe PaymentIntent.

        Args:
            amount: Amount in dollars (will be converted to cents)
            currency: Currency code (default: usd)

        Returns:
            dict: PaymentIntent object from Stripe
        """
        try:
            # Convert to cents
            amount_cents = int(amount * 100)

            intent = stripe.PaymentIntent.create(
                amount=amount_cents,
                currency=currency,
                automatic_payment_methods={"enabled": True},
            )
            return intent
        except stripe.error.StripeError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def construct_event(payload: bytes, sig_header: str):
        """
        Verify and construct a Stripe webhook event.
        """
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.stripe_webhook_secret
            )
            return event
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Invalid payload")
        except stripe.error.SignatureVerificationError as e:
            raise HTTPException(status_code=400, detail="Invalid signature")

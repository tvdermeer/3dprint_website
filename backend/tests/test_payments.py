import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

def test_create_payment_intent(client: TestClient):
    # Mock stripe.PaymentIntent.create
    with patch("stripe.PaymentIntent.create") as mock_create:
        # Setup mock return value
        mock_intent = MagicMock()
        mock_intent.client_secret = "pi_123_secret_456"
        mock_create.return_value = mock_intent

        response = client.post(
            "/api/v1/payments/create-intent",
            json={"amount": 39.99, "currency": "usd"},
        )

        assert response.status_code == 200
        assert response.json()["clientSecret"] == "pi_123_secret_456"
        
        # Verify stripe was called with cents
        mock_create.assert_called_once()
        call_kwargs = mock_create.call_args[1]
        assert call_kwargs["amount"] == 3999
        assert call_kwargs["currency"] == "usd"

def test_create_payment_intent_invalid_amount(client: TestClient):
    response = client.post(
        "/api/v1/payments/create-intent",
        json={"amount": -10, "currency": "usd"},
    )
    assert response.status_code == 422

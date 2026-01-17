from typing import Any


def send_password_reset_email(to_email: str, token: str) -> None:
    """
    Mock sending a password reset email by printing to console.
    In a real app, this would use SMTP or an email service provider.
    """
    reset_link = f"http://localhost:5173/reset-password?token={token}"
    print(f"\n[MOCK EMAIL] Password reset requested for {to_email}")
    print(f"[MOCK EMAIL] Link: {reset_link}\n")

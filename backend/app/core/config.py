"""
Application configuration settings.
Loads from environment variables using pydantic-settings.
"""

from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration settings."""

    # Application metadata
    app_name: str = "3D Print Shop API"
    app_version: str = "0.1.0"
    debug: bool = True
    environment: str = "development"

    # Database configuration
    database_url: str = "sqlite:///./ecommerce.db"

    # Security settings
    secret_key: str = "your-super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS settings
    cors_origins: List[str] = [
        "http://localhost:5173",  # Vite frontend
        "http://localhost:3000",  # Alternative frontend port
        "http://127.0.0.1:5173",
    ]

    # Stripe configuration (optional)
    stripe_secret_key: str
    stripe_publishable_key: str 
    stripe_webhook_secret: str 

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = False


# Create global settings instance
settings = Settings()

"""
Product model for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Float, Integer, String, Text

from app.core.database import Base


class Product(Base):
    """Product model representing a 3D printable item."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    sku = Column(String(100), unique=True, index=True, nullable=False)
    image_url = Column(String(500), nullable=True)
    is_active = Column(Integer, default=1)  # 1 = active, 0 = inactive

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"

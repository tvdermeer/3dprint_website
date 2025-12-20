"""
Business logic for product operations.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    """Service for product operations."""

    @staticmethod
    def get_all_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        """Get all active products with pagination."""
        return db.query(Product).filter(Product.is_active == 1).offset(skip).limit(limit).all()

    @staticmethod
    def get_product_by_id(db: Session, product_id: int) -> Optional[Product]:
        """Get a product by ID."""
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def get_product_by_sku(db: Session, sku: str) -> Optional[Product]:
        """Get a product by SKU."""
        return db.query(Product).filter(Product.sku == sku).first()

    @staticmethod
    def create_product(db: Session, product: ProductCreate) -> Product:
        """Create a new product."""
        db_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            sku=product.sku,
            image_url=product.image_url,
            is_active=1 if product.is_active else 0,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Optional[
        Product
    ]:
        """Update an existing product."""
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            return None

        update_data = product_update.model_dump(exclude_unset=True)
        if "is_active" in update_data:
            update_data["is_active"] = 1 if update_data["is_active"] else 0

        for key, value in update_data.items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def delete_product(db: Session, product_id: int) -> bool:
        """Soft delete a product by marking it inactive."""
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            return False

        db_product.is_active = 0
        db.commit()
        return True

    @staticmethod
    def check_stock(db: Session, product_id: int, quantity: int) -> bool:
        """Check if sufficient stock is available."""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return False
        return product.stock >= quantity

    @staticmethod
    def reduce_stock(db: Session, product_id: int, quantity: int) -> bool:
        """Reduce product stock by quantity."""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product or product.stock < quantity:
            return False

        product.stock -= quantity
        db.commit()
        return True

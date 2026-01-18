from app.core.database import SessionLocal
from app.models.product import Product
from app.services.product_service import ProductService
from app.schemas.product import ProductCreate


def seed():
    db = SessionLocal()
    try:
        # Check if we already have products
        if db.query(Product).count() == 0:
            print("Seeding database with initial product...")
            product_data = ProductCreate(
                name="AXYS Premium Golf Cleaner",
                description="The ultimate golf club cleaning solution in a premium, durable container. Designed to attach directly to your golf cart for convenient access throughout your round.",
                price=39.99,
                stock=100,
                sku="AXYS-GC-001",
                image_url=None,  # Placeholder for now
                is_active=True,
            )

            ProductService.create_product(db, product_data)
            print("Product created successfully!")
        else:
            print("Database already seeded.")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()

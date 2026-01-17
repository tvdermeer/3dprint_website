"""add user_id to orders

Revision ID: c24fec326076
Revises: 755b0cd12f97
Create Date: 2026-01-17 21:50:14.602818

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c24fec326076"
down_revision: Union[str, None] = "755b0cd12f97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Add column
    op.add_column("orders", sa.Column("user_id", sa.Integer(), nullable=True))

    # 2. Add foreign key
    # Note: SQLite has limited support for ALTER TABLE ADD CONSTRAINT,
    # but Alembic handles the batch operation for SQLite if configured (which it typically is in env.py).
    # If not, we might need batch_alter_table context.
    # Given the standard setup, let's try standard op first, but usually batch is safer for SQLite.

    with op.batch_alter_table("orders") as batch_op:
        batch_op.create_foreign_key("fk_orders_users", "users", ["user_id"], ["id"])

    # 3. Data Migration: Link existing orders to users based on email
    # This raw SQL works for SQLite and most standard SQL DBs
    op.execute("""
        UPDATE orders 
        SET user_id = (SELECT id FROM users WHERE users.email = orders.customer_email)
        WHERE user_id IS NULL
    """)


def downgrade() -> None:
    with op.batch_alter_table("orders") as batch_op:
        batch_op.drop_constraint("fk_orders_users", type_="foreignkey")
        batch_op.drop_column("user_id")

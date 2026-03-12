"""create cart_product mm table

Revision ID: 1b7f9676490c
Revises: 1fa8a16388e7
Create Date: 2026-03-12 13:41:15.278085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b7f9676490c'
down_revision: Union[str, Sequence[str], None] = '9eca61c324de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "cart_product",
        sa.Column("id", sa.UUID, nullable=False),
        sa.Column("cart_id", sa.UUID, sa.ForeignKey("cart.id"), nullable=False),
        sa.Column("product_id", sa.UUID, sa.ForeignKey("product.id"), nullable=False),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table("cart_product")

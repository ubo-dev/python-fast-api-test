"""drop cart_id from product

Revision ID: ac59614e7681
Revises: 1b7f9676490c
Create Date: 2026-03-12 14:51:17.680990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac59614e7681'
down_revision: Union[str, Sequence[str], None] = '1b7f9676490c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("product", "cart_id")


def downgrade() -> None:
    op.add_column(
        "cart",
        sa.Column("cart_id", sa.UUID, nullable=True)
    )
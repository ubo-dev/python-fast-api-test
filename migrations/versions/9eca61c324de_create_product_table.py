"""create product table

Revision ID: 9eca61c324de
Revises: 2b55624b8ad6
Create Date: 2026-03-12 12:06:41.782165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9eca61c324de'
down_revision: Union[str, Sequence[str], None] = '1fa8a16388e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    product_type_enum = sa.Enum('CARPET', 'WALL_CARPET', 'TSHIRT', name='producttype')
    op.create_table(
        "product",
        sa.Column("id", sa.UUID, nullable=False),
        sa.Column("name", sa.String(55), nullable=False),
        sa.Column('product_type', product_type_enum, nullable=False),
        sa.Column('cart_id', sa.UUID, sa.ForeignKey('cart.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table("product")
    sa.Enum(name='producttype').drop(bind=op.get_bind())
"""create cart table

Revision ID: 1fa8a16388e7
Revises: 9eca61c324de
Create Date: 2026-03-12 12:14:02.311806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fa8a16388e7'
down_revision: Union[str, Sequence[str], None] = '2b55624b8ad6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_primary_key("users_pk", "users", ["id"])
    
    op.create_table(
        "cart",
        sa.Column("id", sa.UUID, nullable=False),
        sa.Column("user_id", sa.UUID, sa.ForeignKey("users.id"), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table("cart")

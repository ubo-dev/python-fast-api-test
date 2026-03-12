
from typing import List
import uuid

from sqlalchemy import ForeignKey
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.product import Product
from app.models.user import User

class Cart(Base):
    __tablename__ = "cart"
    
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    # one to many
    products: Mapped[List["Product"]] = relationship("Product", back_populates="cart")
    
    # one to one
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="cart")
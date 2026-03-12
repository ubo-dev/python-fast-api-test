import uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        nullable=False
    )
    
    adress: Mapped[str] = mapped_column(
        nullable=False
    )
    
    has_advertisement_perm: Mapped[bool] = mapped_column(
        nullable=False
    )
    
    gender: Mapped[int] = mapped_column(
        nullable=True
    )
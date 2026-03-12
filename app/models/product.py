from app.db.base import Base
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from app.models.enums.product_type import ProductType

class Product(Base):
    __tablename__ = "product"
    
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    
    product_type: Mapped[ProductType] = mapped_column(
        nullable=False,
        index=True
    )
from asyncio import Event
from datetime import datetime
import enum
import uuid
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.modules.participant.repository import Participant


class PhotoStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    

class Photo(Base):
    __tablename__ = "photo"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"), nullable=False)
    participant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("participant.id"), nullable=False)
    
    url: Mapped[str] = mapped_column(nullable=False)        # S3/R2 URL
    storage_key: Mapped[str] = mapped_column(nullable=False) # raw key in object storage
    file_size: Mapped[int | None] = mapped_column(nullable=True)  # bytes
    
    status: Mapped[PhotoStatus] = mapped_column(PhotoStatus, default="pending", nullable=False)
    # "pending" → "approved" or "rejected"
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    event: Mapped["Event"] = relationship(back_populates="photos")
    uploaded_by: Mapped["Participant"] = relationship(back_populates="photos")
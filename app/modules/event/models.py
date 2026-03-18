from datetime import datetime
import enum
import uuid
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.modules.participant.repository import Participant
from app.modules.photo.models import Photo
from app.modules.user.models import User


class EventStatus(str, enum.Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    ARCHIVED = "archived"

class Event(Base):
    __tablename__ = "event"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # when the event takes place
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    # controls whether new people can still join
    status: Mapped[EventStatus] = mapped_column(EventStatus, default="active", nullable=False)  
    # e.g. "active", "closed", "archived"
    
    # unique code people use to join the event
    invite_code: Mapped[str] = mapped_column(unique=True, nullable=False)

    owner: Mapped["User"] = relationship()
    participants: Mapped[list["Participant"]] = relationship(back_populates="event")
    photos: Mapped[list["Photo"]] = relationship(back_populates="event")
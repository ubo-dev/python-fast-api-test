from asyncio import Event
from datetime import datetime
import enum
import uuid
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.modules.photo.models import Photo
from app.modules.user.models import User


class ParticipantRole(str, enum.Enum):
    OWNER = "owner"
    MEMBER = "member"

class Participant(Base):
    __tablename__ = "participant"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"), nullable=False)
    role: Mapped[ParticipantRole] = mapped_column(ParticipantRole, default="member", nullable=False)
    # e.g. "owner", "member"
    joined_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    user: Mapped["User"] = relationship(back_populates="participants")
    event: Mapped["Event"] = relationship(back_populates="participants")
    photos: Mapped[list["Photo"]] = relationship(back_populates="uploaded_by")
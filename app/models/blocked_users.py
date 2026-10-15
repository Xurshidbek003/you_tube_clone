from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class BlockedUser(Base):
    __tablename__ = "blocked_users"

    blocker_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    blocked_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    reason: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
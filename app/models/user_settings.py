from datetime import datetime
from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class UserSettings(Base):
    __tablename__ = "user_settings"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    theme: Mapped[str] = mapped_column(String(20), default="light", nullable=False)
    autoplay_next: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    restricted_mode: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    default_quality: Mapped[str] = mapped_column(String(20), default="720p", nullable=False)
    pause_watch_history: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    pause_search_history: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    push_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
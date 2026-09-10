from datetime import datetime
from sqlalchemy import BigInteger, Boolean, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class ChannelStats(Base):
    __tablename__ = "channel_stats"

    channel_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("channels.id"), primary_key=True, autoincrement=True)
    subscriber_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    video_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    total_view_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    hide_subscriber_count: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
from datetime import datetime
from pydantic import BaseModel


class ChannelStatsCreate(BaseModel):
    channel_id: int
    subscriber_count: int = 0
    video_count: int = 0
    total_view_count: int = 0
    hide_subscriber_count: bool = False


class ChannelStatsUpdate(BaseModel):
    subscriber_count: int | None = None
    video_count: int | None = None
    total_view_count: int | None = None
    hide_subscriber_count: bool | None = None


class ChannelStatsResponse(BaseModel):
    channel_id: int
    subscriber_count: int
    video_count: int
    total_view_count: int
    hide_subscriber_count: bool
    updated_at: datetime

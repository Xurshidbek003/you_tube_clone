from datetime import datetime
from pydantic import BaseModel, Field


class ChannelCreate(BaseModel):
    handle: str = Field(min_length=1, max_length=30)
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    avatar_url: str | None = None
    banner_url: str | None = None
    country_code: str | None = Field(default=None, min_length=2, max_length=2)


class ChannelUpdate(BaseModel):
    handle: str | None = Field(default=None, min_length=1, max_length=30)
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    avatar_url: str | None = None
    banner_url: str | None = None
    country_code: str | None = Field(default=None, min_length=2, max_length=2)


class ChannelResponse(BaseModel):
    id: int
    user_id: int
    handle: str
    name: str
    description: str | None
    avatar_url: str | None
    banner_url: str | None
    country_code: str | None
    is_verified: bool
    featured_video_id: int | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

from pydantic import BaseModel,  Field


class ChannelLinkCreate(BaseModel):
    title: str = Field(max_length=60)
    url: str
    position: int


class ChannelLinkUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=60)
    url: str | None = None
    position: int | None = None


class ChannelLinkResponse(BaseModel):
    id: int
    channel_id: int
    title: str
    url: str
    position: int

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SubscriptionCreate(BaseModel):
    channel_id: int
    notification_level: str = "personalized"


class SubscriptionUpdate(BaseModel):
    notification_level: str | None = None


class SubscriptionResponse(BaseModel):
    id: int
    subscriber_id: int
    channel_id: int
    notification_level: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
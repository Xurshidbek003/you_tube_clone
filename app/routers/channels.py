from fastapi import APIRouter, status
from sqlalchemy import select
from app.database.base import MyDb
from app.models.channels import Channel
from app.schemas.channels import ChannelCreate


router = APIRouter(tags=["Channels"], prefix="/channels")


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_channel(channel: ChannelCreate, db: MyDb):
    obj = Channel(
        **channel.model_dump()
    )
    db.add(obj)
    await db.commit()
    return {"msg": "Channel created successfully!"}


@router.get('/')
async def get_channels(db: MyDb):
    result = await db.execute(select(Channel))
    return result.scalars().all()




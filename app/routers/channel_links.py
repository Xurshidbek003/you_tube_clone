from fastapi import status, APIRouter
from sqlalchemy import select
from app.database.base import MyDb
from app.models.channel_links import ChannelLink
from app.models.channels import Channel
from app.schemas.channel_links import ChannelLinkCreate, ChannelLinkResponse, \
    ChannelLinkUpdate
from app.utils.check_ident import checked_id


router = APIRouter(tags=["Channel Links"], prefix='/channel_links')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_channel_link(channel_link: ChannelLinkCreate, db: MyDb):

    await checked_id(db, Channel, channel_link.channel_id)

    obj = ChannelLink(
        **channel_link.model_dump()
    )

    db.add(obj)
    await db.commit()

    return {"msg": "Channel linkga qoshildi !!!"}



@router.get('/', response_model=list[ChannelLinkResponse])
async def get_channel_links(db: MyDb):
    result = await db.execute(select(ChannelLink))
    return result.scalars().all()



@router.put('/{channel_link_id}')
async def update_channel_link(channel_link_id: int, channel_link: ChannelLinkUpdate, db: MyDb):
    channel_link_result = await checked_id(db, ChannelLink, channel_link_id)

    await checked_id(db, Channel, channel_link.channel_id)

    channel_link_result.title = channel_link.title
    channel_link_result.url = channel_link.url
    channel_link_result.channel_id = channel_link.channel_id
    channel_link_result.position = channel_link.position

    await db.commit()
    return {"msg": "Channel link updated !!!"}


@router.delete('/{channel_link_id}')
async def delete_channel_link(channel_link_id: int, db: MyDb):
    channel_link_result = await checked_id(db, ChannelLink, channel_link_id)
    await db.delete(channel_link_result)
    await db.commit()
    return {"msg": "Channel link deleted !!!"}

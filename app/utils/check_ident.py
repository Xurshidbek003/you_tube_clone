from fastapi import HTTPException
from sqlalchemy import select


async def checked_id(db, model, ident):
    result = await db.execute(select(model).where(model.id == ident))
    obj = result.scalars().first()
    if not obj:
        raise HTTPException(404, f"Id {ident} not found")

    return obj


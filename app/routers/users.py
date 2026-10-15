import os
from fastapi import APIRouter, Request, HTTPException
from fastapi_sso.sso.google import GoogleSSO
from sqlalchemy import select
from app.database.base import MyDb
from app.models.users import User
from app.utils.security import create_access_token

router = APIRouter(prefix="/auth/google", tags=["Google Auth"])

sso = GoogleSSO(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    redirect_uri="http://localhost:8000/auth/google/callback",
    allow_insecure_http=True
)


@router.get("/login")
async def google_login():
    with sso:
        return await sso.get_login_redirect()


@router.get("/callback")
async def google_callback(request: Request, db: MyDb):
    with sso:
        google_user = await sso.verify_and_process(request)

    if not google_user:
        raise HTTPException(status_code=400,
                            detail="Google avtorizatsiyasi bekor qilindi.")

    query = select(User).where(
        (User.google_id == google_user.id) | (User.email == google_user.email)
    )
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            email=google_user.email,
            full_name=google_user.display_name,
            avatar_url=google_user.picture,
            google_id=google_user.id
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

    elif not user.google_id:
        user.google_id = google_user.id
        await db.commit()

    access_token = create_access_token(user_id=user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
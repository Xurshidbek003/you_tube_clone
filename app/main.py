from fastapi import FastAPI
from app.routers.channels import router as channel_router
from app.routers.channel_links import router as channel_link_router
from app.routers.users import router as auth_router


app = FastAPI(title="You Tube Clone API", version="1.0.0", docs_url='/')


app.include_router(auth_router)
app.include_router(channel_router)
app.include_router(channel_link_router)
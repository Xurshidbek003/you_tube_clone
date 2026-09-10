from fastapi import FastAPI
from app.routers.channels import router as channel_router


app = FastAPI(title="You Tube Clone API", version="1.0.0", docs_url='/')


app.include_router(channel_router)
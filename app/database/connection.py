from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, \
    AsyncSession
import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USERNAME = os.getenv("DB_USERNAME")


engine = create_async_engine(f"mysql+aiomysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}")


SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    async with engine.begin() as conn:
        yield conn

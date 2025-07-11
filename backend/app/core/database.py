from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.settings import SettingsProducao


DATABASE_URL = SettingsProducao().DATABASE_URL


class Database:
    Base = declarative_base()

    def __init__(self, database_url: str = DATABASE_URL):
        self.engine = create_async_engine(database_url, echo=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

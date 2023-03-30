from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.bcraft.config import settings


class DatabaseSession:
    """
    Инициализация синхронной сессии
    """
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

    def __init__(self):
        self._engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            echo=settings.DEBUG,
        )

        self._session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
            class_=Session,
            expire_on_commit=False,
        )

    def get_session(self):
        session = self._session()
        try:
            yield session
        except Exception:
            session.rollback()
        finally:
            session.close()


db_session = DatabaseSession()

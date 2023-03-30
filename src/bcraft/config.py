import functools
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Настройки проекта и окружений
    """

    # Project
    PROJECT_NAME: str = "Krestovsky"
    PROJECT_VERSION: str = "1.0.0"
    TITLE: str = "Bcraft test task"
    DESCRIPTION: str = "Microservice for statistics counters"
    DEBUG: bool = True

    # DB
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Tests
    DB_TEST_USER = os.getenv("DB_TEST_USER", "postgres")
    DB_TEST_PASS = os.getenv("DB_TEST_PASS", "postgres")
    DB_TEST_HOST = os.getenv("DB_TEST_HOST", "localhost")
    DB_TEST_PORT = os.getenv("DB_TEST_PORT", 5432)
    DB_TEST_NAME = os.getenv("DB_TEST_NAME", "tests")
    DATABASE_TEST_URL = f"postgresql://{DB_TEST_USER}:{DB_TEST_PASS}@{DB_TEST_HOST}:{DB_TEST_PORT}/{DB_TEST_NAME}"


@functools.lru_cache()
def _build_settings() -> Settings:
    return Settings()


settings = _build_settings()

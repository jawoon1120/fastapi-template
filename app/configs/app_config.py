import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    POSTGRESQL_HOST: str
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DATABASE: str
    
    model_config = SettingsConfigDict(
        env_file=f'app/configs/.{os.getenv("ENV_STATE") or "local"}.env'
    )

@lru_cache()
def get_postgres_connection() -> str:
    settings = Settings()
    return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{str(settings.DB_PORT)}/{settings.DB_NAME}"


@lru_cache()
def get_postgres_migrate_connection() -> str:
    settings = Settings()
    return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{str(settings.DB_PORT)}/{settings.DB_NAME}"


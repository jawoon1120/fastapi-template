import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    POSTGRESQL_HOST: str
    POSTGRESQL_USER: str
    POSTGRESQL_PORT: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DATABASE: str
    
    model_config = SettingsConfigDict(
        env_file=f'app/configs/.{os.getenv("ENV_STATE") or "local"}.env'
    )

@lru_cache()
def get_postgres_connection() -> str:
    settings = Settings()
    return f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{str(settings.POSTGRESQL_PORT)}/{settings.POSTGRESQL_DATABASE}"

@lru_cache()
def get_postgres_test_connection() -> str:
    settings = Settings()
    return f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{str(settings.POSTGRESQL_PORT)}/{settings.POSTGRESQL_DATABASE}_test"

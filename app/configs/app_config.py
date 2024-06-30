import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    POSTGRESQL_HOST: str
    POSTGRESQL_USER: str
    POSTGRESQL_PORT: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DATABASE: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    model_config = SettingsConfigDict(
        env_file=f'app/configs/.{os.getenv("ENV_STATE") or "local"}.env'
    )

settings = Settings()

@lru_cache()
def get_postgres_connection() -> str:
    return f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{str(settings.POSTGRESQL_PORT)}/{settings.POSTGRESQL_DATABASE}"

@lru_cache()
def get_postgres_test_connection() -> str:
    return f"postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{str(settings.POSTGRESQL_PORT)}/{settings.POSTGRESQL_DATABASE}_test"

@lru_cache()
def get_token_secret_key() -> str:
    return settings.SECRET_KEY

@lru_cache()
def get_algorithm() -> str:
    return settings.ALGORITHM

@lru_cache()
def get_token_expire_minutes() -> int:
    return settings.ACCESS_TOKEN_EXPIRE_MINUTES
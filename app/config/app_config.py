import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name  : str = "Python Redis FastAPI Nginx Docker Compose"
    author    : str = "Hugo Lin"
    app_mode  : str = os.getenv("APP_MODE")
    host      : str = os.getenv("HOST")
    port      : int = int(os.getenv("PORT"))
    redis_host: str = os.getenv("REDIS_HOST")
    redis_port: int = int(os.getenv("REDIS_PORT"))
    reload    : bool = os.getenv("RELOAD")

@lru_cache()
def get_app_config(app_mode=f".env.{os.getenv('APP_MODE')}") -> Settings:
    load_dotenv(app_mode)
    return Settings()


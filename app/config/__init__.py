import os

from app.config.app_config import get_app_config

app_settings = get_app_config(
    app_mode=f".env.{os.getenv('APP_MODE')}")


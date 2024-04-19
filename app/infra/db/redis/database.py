import redis

from app.config import app_settings


def initialize_db():
    redis_cli = redis.Redis(
        host=app_settings.redis_host, 
        port=int(app_settings.redis_port), 
        decode_responses=True
    )

    return redis_cli

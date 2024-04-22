from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.config import app_settings

info_routes = APIRouter(tags=["info"], prefix="/info")

@info_routes.get("/", status_code=status.HTTP_200_OK)
def get_infor():
    try:
        return {
            "app_name"  : app_settings.app_name,
            "author"    : app_settings.author,
            "app_mode"  : app_settings.app_mode,
            "host"      : app_settings.host,
            "port"      : app_settings.port,
            "reload"    : app_settings.reload,
            "redis_host": app_settings.redis_host,
            "redis_port": app_settings.redis_port
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )


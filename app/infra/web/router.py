from fastapi import FastAPI

from app.adapters.controllers.info_controller import info_routes
from app.adapters.controllers.items_controller import items_routes


def setup_routers(app: FastAPI) -> None:
    app.include_router(items_routes)
    app.include_router(info_routes)

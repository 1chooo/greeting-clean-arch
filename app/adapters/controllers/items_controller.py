from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.infra.db.redis import redis_cli


class Item(BaseModel):
    name: str

items_routes = APIRouter(tags=["items"], prefix="/items")

@items_routes.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    # Add item to the Redis list
    redis_cli.rpush("items", item.name)
    return {"message": "Item added successfully"}


@items_routes.get("/", status_code=status.HTTP_200_OK)
async def get_items():
    # Retrieve items from the Redis list
    items = redis_cli.lrange("items", 0, -1)
    return {"items": items}


@items_routes.delete("/{item_name}", status_code=status.HTTP_200_OK)
async def delete_item(item_name: str):
    # Delete a specific item from the Redis list
    if item_name not in redis_cli.lrange("items", 0, -1):
        raise HTTPException(status_code=404, detail="Item not found")
    redis_cli.lrem("items", 0, item_name)
    return {"message": f"Item '{item_name}' deleted successfully"}



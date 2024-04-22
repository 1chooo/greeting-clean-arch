from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.infra.db.redis import redis_cli


class Item(BaseModel):
    name: str

items_routes = APIRouter(tags=["items"], prefix="/items")

@items_routes.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    try:
        redis_cli.rpush("items", item.name)
        return {"message": "Item added successfully"}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )



@items_routes.get("/", status_code=status.HTTP_200_OK)
async def get_items():
    try:
        items = redis_cli.lrange("items", 0, -1)
        return {"items": items}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )


@items_routes.delete("/{item_name}", status_code=status.HTTP_200_OK)
async def delete_item(item_name: str):
    try:
        items_list = redis_cli.lrange("items", 0, -1)
        if item_name.encode() not in items_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Item not found"
            )
        redis_cli.lrem("items", 0, item_name)
        return {"message": f"Item '{item_name}' deleted successfully"}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )

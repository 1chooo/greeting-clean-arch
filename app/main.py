import os

import redis
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

# Connect to Redis
_ = load_dotenv(find_dotenv())
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
redis_cli = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, 
    decode_responses=True)


class Item(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    # Add item to the Redis list
    redis_cli.rpush("items", item.name)
    return {"message": "Item added successfully"}


@app.get("/items/")
async def get_items():
    # Retrieve items from the Redis list
    items = redis_cli.lrange("items", 0, -1)
    return {"items": items}


@app.delete("/items/")
async def delete_items():
    # Delete all items from the Redis list
    redis_cli.delete("items")
    return {"message": "Items deleted successfully"}


@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    # Delete a specific item from the Redis list
    if item_name not in redis_cli.lrange("items", 0, -1):
        raise HTTPException(status_code=404, detail="Item not found")
    redis_cli.lrem("items", 0, item_name)
    return {"message": f"Item '{item_name}' deleted successfully"}
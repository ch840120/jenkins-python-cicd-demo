# app/main.py
from fastapi import FastAPI, Request, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Simple Test REST API (no Pydantic, no typing)")

# in-memory 暫存
_items = []

class Item(BaseModel):
    id: int
    name: str

@app.get("/ping")
async def ping():
    return {"msg": "pong1"}

@app.get("/items")
async def list_items():
    return _items

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    _items.append(item)
    return item

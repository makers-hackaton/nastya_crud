from typing import List
from fastapi import FastAPI, HTTPException
from apps.serializers import ItemSerializer, ItemCreateUpdateSerializer
from db import SessionLocal
from apps.models import Item

app = FastAPI()

db = SessionLocal()

@app.get("/items", response_model=List[ItemSerializer], status_code=200)
def get_all():
    items = db.query(Item).all()
    return items

@app.get("/items/{id}", response_model=ItemSerializer, status_code=200)
def get_one(id:int):
    item = db.query(Item).filter(Item.id==id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=ItemCreateUpdateSerializer, status_code=201)
def create(item:ItemCreateUpdateSerializer):
    # в сериализаторе убрать id
    new_item = Item(
        name = item.name,
        description = item.description
    )

    db_item = db.query(Item).filter(item.name==new_item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item with this name already exists")

    db.add(new_item)
    db.commit()
    return new_item

@app.patch("/items/{id}", response_model=ItemCreateUpdateSerializer, status_code=200)
def update(id:int, item:ItemCreateUpdateSerializer):
    item_to_update = db.query(Item).filter(Item.id==id).first()
    if item_to_update is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item_to_update.name = item.name
    item_to_update.description = item.description
    db.commit()
    return item_to_update

@app.delete("/items/{id}", status_code=204)
def delete(id:int):
    item = db.query(Item).filter(Item.id==id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()

import pika, json, sys, os
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.db import models
from app.db.engine import SessionLocal, engine

from fastapi.encoders import jsonable_encoder



from dotenv import load_dotenv
from app.models.item_model import Item
from app.models.user_model import Purchase

from app.rabbitmq.engine import rabbitmq
from app.db import models, schemas, crud

load_dotenv()

router = APIRouter(prefix="/api")

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-item/")
async def purchase(
    item: Item,
    db: Session = Depends(get_db)
    ):
    db_item = crud.get_item_by_name(db, name=item.name)
    if db_item:
        raise HTTPException(status_code=400, detail="item name already existed")
    crud.create_item(db=db, name=item.name, price=item.price, amount=item.amount)
    return

@router.post("/purchase/")
async def purchase(purchase_detail: Purchase):
    rabbitmq.send_data(queue_name='from.backend', data=json.dumps(purchase_detail.model_dump()))
    return


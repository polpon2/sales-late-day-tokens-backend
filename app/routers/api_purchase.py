import json
from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from app.db import crud
from app.db.engine import SessionLocal
from app.models.user_model import Purchase
from app.rabbitmq.engine import rabbitmq
from sqlalchemy.orm import Session

load_dotenv()

router = APIRouter(prefix="/api")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/purchase/")
async def purchase(purchase_detail: Purchase):
    rabbitmq.send_data(queue_name='from.backend', data=json.dumps(purchase_detail.model_dump()))
    return

@router.post("/deliver-completed")
async def processComplete(purchase_detail: Purchase):
    print("processing completed for: "+ purchase_detail.amount +" of "+ purchase_detail.token_name + " for " + purchase_detail.username)
    return

@router.get("/all-transaction")
async def get_all_transaction(
    db: Session = Depends(get_db)
):
    arr = crud.get_all(db)
    print(arr)
    return arr



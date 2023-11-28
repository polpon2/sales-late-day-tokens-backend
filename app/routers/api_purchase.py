import pika, json, sys, os
from typing import Annotated

from fastapi import APIRouter



from dotenv import load_dotenv

from app.models.user_model import Purchase

from app.rabbitmq.engine import rabbitmq

load_dotenv()

router = APIRouter(prefix="/api")

@router.post("/purchase/")
async def purchase(purchase_detail: Purchase):
    rabbitmq.send_data(queue_name='from.backend', data=json.dumps(purchase_detail.model_dump()))
    return

@router.post("/deliver-completed")
async def processComplete(purchase_detail: Purchase):
    print("processing completed for: "+ purchase_detail.amount +" of "+ purchase_detail.token_name + " for " + purchase_detail.username)
    return



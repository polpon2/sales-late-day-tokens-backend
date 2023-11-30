import json
from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from app.db import crud
from app.db.engine import SessionLocal
from app.models.user_model import Purchase
from app.rabbitmq.engine import rabbitmq
from sqlalchemy.orm import Session

load_dotenv()

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

# Sets provider
provider = TracerProvider()

# Sets processor for span
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

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
    rabbitmq.send_data(queue_name='from.backend', data=(json.dumps(purchase_detail.model_dump())))
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



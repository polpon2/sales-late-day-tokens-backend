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
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator


provider = TracerProvider()
trace.set_tracer_provider(provider)
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

    with tracer.start_as_current_span("kick-start-from-backend"):
        carrier = {}

       
        # Write the current context into the carrier.
        TraceContextTextMapPropagator().inject(carrier)
        send_data = {
            # username: str
            # price: int
            # amount: int
            "username": purchase_detail.username,
            "price": purchase_detail.price,
            "amount": purchase_detail.amount,
            "traceparent": carrier['traceparent']
        }

        rabbitmq.send_data(queue_name='from.backend', data=(json.dumps(send_data)))
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





from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import api_purchase


app = FastAPI()
app.include_router(api_purchase.router)

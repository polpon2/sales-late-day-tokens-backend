# import os

# from datetime import timedelta
# from typing import Annotated

# from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
# from fastapi.security.utils import get_authorization_scheme_param
# from fastapi.security import OAuth2PasswordRequestForm

# from sqlalchemy.orm import Session



# from app.models.user_model import UserCreate

# from app.db.engine import SessionLocal, engine
# from app.db import models, schemas, crud



# from dotenv import load_dotenv
# models.Base.metadata.create_all(bind=engine)

# load_dotenv()
# router = APIRouter(prefix="/api")
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/register/")
# def create_user(
#     user: UserCreate,
#     db: Session = Depends(get_db)
#     ):

#     db_user = crud.get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="username already existed")
#     crud.create_user(db=db, username=user.username)

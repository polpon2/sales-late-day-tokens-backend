# from sqlalchemy.orm import Session
# from sqlalchemy.sql.expression import func
# from sqlalchemy.exc import NoResultFound

# from . import models, schemas
# from datetime import datetime


# def create_user(db: Session, username):
#     db_user = models.User(username=username, credits=100)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def create_item(db: Session, name: str, price: int, amount: int):
#     db_item = models.Inventory(uuid=name, price=price, amount=amount)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def get_item_by_name(db: Session, name: str):
#     return db.query(models.Inventory).filter(models.Inventory.uuid == name).first()


# def get_item(db: Session, item_id: int):
#     return db.query(models.Inventory).filter(models.Inventory.id == item_id).first()

# from sqlalchemy import Boolean, Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# from .engine import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(255), unique=True, index=True)
#     credits = Column(Integer, default=100)


# class Inventory(Base):
#     __tablename__ = "inventories"

#     id = Column(Integer, primary_key=True, index=True)
#     uuid = Column(String(255), unique=True, index=True)
#     price = Column(Integer, default=0)
#     amount = Column(Integer, default=0)
    

# class Order(Base):
#     __tablename__ = "orders"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.username"))
#     inventory_uuid = Column(String(255), ForeignKey("inventories.uuid"))
#     purchase_amount = Column(Integer, default=0)


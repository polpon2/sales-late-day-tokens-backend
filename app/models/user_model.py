from pydantic import BaseModel

class User(BaseModel):
    username: str
    credit: int

class Purchase(BaseModel):
    username: str
    price: int
    amount: int

class UserCreate(BaseModel):
    username: str

class Debug(Purchase):
    kill_create: bool = False
    kill_payment: bool = False
    kill_inventory: bool = False
    kill_deliver: bool = False
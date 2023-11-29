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


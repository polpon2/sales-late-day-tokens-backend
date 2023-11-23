from pydantic import BaseModel

class User(BaseModel):
    username: str
    credit: int
    
class Purchase(BaseModel):
    username: str
    user_credit: int
    inventory_id: int
    pirce: int
    amout: int

class UserCreate(BaseModel):
    username: str


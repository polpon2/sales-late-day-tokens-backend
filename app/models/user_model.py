from pydantic import BaseModel

class User(BaseModel):
    username: str
    credit: int
    
class Purchase(BaseModel):
    username: str
    token_name: str
    amount: int

class UserCreate(BaseModel):
    username: str


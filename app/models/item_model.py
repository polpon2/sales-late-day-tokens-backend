from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int
    amount: int
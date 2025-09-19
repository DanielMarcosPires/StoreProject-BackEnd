from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    name:str
    image:Optional[str]
    category:str
    quantity:int
    price:float
   

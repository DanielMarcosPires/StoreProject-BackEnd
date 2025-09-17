from pydantic import BaseModel

class Product(BaseModel):
    Name:str
    Category:str
    Quantity:int
    PriceUnity:float
   
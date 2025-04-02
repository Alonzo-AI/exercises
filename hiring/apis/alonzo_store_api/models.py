from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    image: Optional[str]
    category: str
    price: float
    description: Optional[str]
    stock_available: int

class ProductCreate(BaseModel):
    name: str
    image: Optional[str]
    category: str
    price: float
    description: Optional[str]
    stock_available: int

class Category(BaseModel):
    id: int
    name: str

class CategoryCreate(BaseModel):
    name: str
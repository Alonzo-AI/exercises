from pydantic import BaseModel
from typing import List, Optional


class Ingredient(BaseModel):
    ingredient: str
    quantity: float
    unit: Optional[str]

class Recipe(BaseModel):
    id: int
    title: str
    description: Optional[str]
    image: Optional[str]
    category: Optional[str]
    prep_time_minutes: Optional[int]
    cook_time_minutes: Optional[int]
    ingredients: List[Ingredient]
    instructions: List[str]
    dietary: List[str]

class RecipeCreate(BaseModel):
    title: str
    description: Optional[str]
    image: Optional[str]
    category: Optional[str]
    prep_time_minutes: Optional[int]
    cook_time_minutes: Optional[int]
    ingredients: List[Ingredient]
    instructions: List[str]
    dietary: List[str]

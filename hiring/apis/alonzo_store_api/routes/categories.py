from fastapi import APIRouter, HTTPException
from models import Category, CategoryCreate
from storage import categories, save_categories, get_next_id

router = APIRouter()

@router.get("/")
def list_categories():
    return categories

@router.post("/")
def create_category(data: CategoryCreate):
    new_id = get_next_id(categories)
    category = Category(id=new_id, name=data.name)
    categories.append(category.dict())
    save_categories()
    return category
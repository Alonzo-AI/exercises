from fastapi import APIRouter, HTTPException
from models import Product, ProductCreate
from storage import products, save_products, get_next_id
from typing import Optional, List
from fastapi import Query


router = APIRouter()

@router.get("/")
def list_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    name_prefix: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
):
    filtered = products

    if category:
        filtered = [p for p in filtered if p["category"].lower() == category.lower()]
    if min_price is not None:
        filtered = [p for p in filtered if p["price"] >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    if name_prefix:
        filtered = [p for p in filtered if p["name"].lower().startswith(name_prefix.lower())]

    return filtered[skip : skip + limit]

@router.post("/")
def create_product(data: ProductCreate):
    new_id = get_next_id(products)
    product = Product(id=new_id, **data.dict())
    products.append(product.dict())
    save_products()
    return product

@router.put("/{product_id}")
def update_product(product_id: int, data: ProductCreate):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            updated = Product(id=product_id, **data.dict())
            products[i] = updated.dict()
            save_products()
            return updated
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            products.pop(i)
            save_products()
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

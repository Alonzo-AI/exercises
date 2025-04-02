from fastapi import APIRouter, HTTPException
from typing import Optional, List
from models import Recipe, RecipeCreate
from storage import recipes, save_recipes, get_next_id
from fastapi import Query


router = APIRouter()

@router.get("/")
def list_recipes(
    category: Optional[str] = None,
    title_prefix: Optional[str] = None,
    max_prep_time: Optional[int] = None,
    max_cook_time: Optional[int] = None,
    ingredients: Optional[List[str]] = Query(None),
    dietary: Optional[List[str]] = Query(None),
    skip: int = 0,
    limit: int = 10
):
    filtered = recipes

    if category:
        filtered = [r for r in filtered if r.get("category", "").lower() == category.lower()]
    if title_prefix:
        filtered = [r for r in filtered if r.get("title", "").lower().startswith(title_prefix.lower())]
    if max_prep_time is not None:
        filtered = [r for r in filtered if r.get("prep_time_minutes") is not None and r["prep_time_minutes"] <= max_prep_time]
    if max_cook_time is not None:
        filtered = [r for r in filtered if r.get("cook_time_minutes") is not None and r["cook_time_minutes"] <= max_cook_time]
    if ingredients:
        filtered = [
            r for r in filtered
            if all(
                any(ing.lower() in i.lower() for i in r.get("ingredients", []))
                for ing in ingredients
            )
        ]
    if dietary:
        filtered = [
            r for r in filtered
            if all(diet.lower() in [d.lower() for d in r.get("dietary", [])] for diet in dietary)
        ]

    return filtered[skip: skip + limit]

@router.post("/")
def create_recipe(data: RecipeCreate):
    new_id = get_next_id(recipes)
    recipe = Recipe(id=new_id, **data.dict())
    recipes.append(recipe.dict())
    save_recipes()
    return recipe

@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, data: RecipeCreate):
    for i, r in enumerate(recipes):
        if r["id"] == recipe_id:
            updated = Recipe(id=recipe_id, **data.dict())
            recipes[i] = updated.dict()
            save_recipes()
            return updated
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int):
    for i, r in enumerate(recipes):
        if r["id"] == recipe_id:
            recipes.pop(i)
            save_recipes()
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/categories")
def list_categories():
    return sorted(list({r.get("category", "").strip() for r in recipes if r.get("category")}))


@router.get("/dietary")
def list_dietary_preferences():
    dietary_set = set()
    for r in recipes:
        for tag in r.get("dietary", []):
            dietary_set.add(tag.strip().lower())
    return sorted(list(dietary_set))

@router.get("/ingredients")
def list_ingredients():
    print(recipes)
    return sorted({i["ingredient"].lower() for r in recipes for i in r.get("ingredients", [])})

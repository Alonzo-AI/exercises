# 🍳 Alonzo Recipes API

A mock FastAPI backend for managing recipes. Made for evaluating React applicants.

## 🚀 Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📚 Features

- No database – stores recipes in `data/recipes.json`
- Fully supports CRUD operations on recipes
- Each recipe includes:
  - Title, description, category
  - Ingredients (list of strings)
  - Instructions (list of steps)
  - Optional image and timing info

## 🧪 Example API Calls

### GET /recipes
Returns all recipes

### POST /recipes
Creates a new recipe

### PUT /recipes/{id}
Updates a recipe

### DELETE /recipes/{id}
Deletes a recipe

## 🗃️ Storage
Data is stored in:
- `data/recipes.json`

## 🧰 Use Case
This is used for evaluating React frontend devs on building CRUD UIs with FastAPI backend.

MIT License.
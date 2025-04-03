# 🍳 Alonzo Recipes — React Evaluation Task

## 🧾 Title
Build a Recipe Directory UI in React to browse, create, and filter recipes.

## 🎯 Introduction & Objective
This task evaluates your ability to build forms, filters, and detailed views using the Alonzo Recipes API. Each recipe includes ingredients, dietary tags, and cooking instructions.

## 🚀 Getting Started

1. Clone or unzip the API project: `alonzo_recipes_api` (https://github.com/Alonzo-AI/exercises)
2. Follow instructions on installing the api and running it.
3. Run the API:

```bash
uvicorn main:app --reload
```

4. Open `http://localhost:8000/docs` for all endpoints.

## 📦 Scope of Evaluation

### 🔹 Recipe Management

- [ ] Display a list of recipes with title, dietary, and category
- [ ] Filter recipes by category, ingredients, and dietary tags
- [ ] Create a new recipe with ingredients and instructions
- [ ] View full recipe detail page
- [ ] Delete recipe
- [ ] Search bar for title/content

### 🔹 Metadata Views

- [ ] Dropdowns or chips for dietary, category, ingredients
- [ ] Use `/recipes/dietary`, `/recipes/ingredients`, `/recipes/categories`

### 🔹 UI Expectations

- [ ] Use React forms effectively
- [ ] Responsive UI
- [ ] Client-side filtering with dropdowns
- [ ] Minimal clean design

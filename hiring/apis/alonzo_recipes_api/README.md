
```markdown
# 🍳 Alonzo Recipes API

A mock FastAPI backend for managing recipes, designed to evaluate frontend developers on React + API integration skills.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at:
**http://localhost:8000**

---

## 📚 Features

- ✅ No database — uses `recipes.json` for persistent file storage
- ✅ Fully supports CRUD for recipes
- ✅ Structured ingredients with quantity and unit
- ✅ Dietary tags (e.g., vegetarian, vegan, gluten-free)
- ✅ Metadata-based filtering (category, prep time, ingredient, dietary, etc.)
- ✅ List categories, dietary preferences, and ingredients separately

---

## 🥣 Recipe Structure

```json
{
  "id": 1,
  "title": "Spaghetti Aglio e Olio",
  "description": "Simple and flavorful Italian pasta.",
  "image": "https://example.com/spaghetti.jpg",
  "category": "Italian",
  "prep_time_minutes": 10,
  "cook_time_minutes": 15,
  "ingredients": [
    {
      "ingredient": "spaghetti",
      "quantity": 200,
      "unit": "g"
    }
  ],
  "instructions": [
    "Boil pasta until al dente.",
    "Sauté garlic in olive oil.",
    "Mix pasta with oil and garnish."
  ],
  "dietary": ["vegetarian"]
}
```

---

## 🔌 API Reference

### 📦 `GET /recipes`

Filter recipes using query parameters:

| Parameter         | Type     | Description                                      |
|-------------------|----------|--------------------------------------------------|
| `category`        | string   | Filter by recipe category                        |
| `title_prefix`    | string   | Filter by recipe title starting with             |
| `max_prep_time`   | integer  | Maximum prep time in minutes                     |
| `max_cook_time`   | integer  | Maximum cook time in minutes                     |
| `ingredients`     | list     | Must include all listed ingredients              |
| `dietary`         | list     | Must include all listed dietary tags             |
| `skip` / `limit`  | integer  | Pagination controls                              |

Example:
```
/recipes?category=Italian&ingredients=garlic&ingredients=olive oil&dietary=vegetarian
```

---

### ➕ `POST /recipes`

Create a new recipe using the full structure.

---

### ✏️ `PUT /recipes/{id}`

Update a recipe by ID.

---

### ❌ `DELETE /recipes/{id}`

Delete a recipe by ID.

---

### 🧠 Metadata Endpoints

| Endpoint               | Method | Description                         |
|------------------------|--------|-------------------------------------|
| `/recipes/categories`  | GET    | List all unique categories          |
| `/recipes/dietary`     | GET    | List all unique dietary tags        |
| `/recipes/ingredients` | GET    | List all unique ingredient names    |

---

## 🧰 Use Case

This mock backend is intended to:
- ✅ Evaluate frontend developers on REST API integration
- ✅ Simulate a realistic recipe management system
- ✅ Allow search, filters, and forms for CRUD interfaces

---

## 🪪 License

MIT — by Alonzo AI for candidate evaluations and internal projects.
```

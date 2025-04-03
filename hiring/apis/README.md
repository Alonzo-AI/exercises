# 🧪 Alonzo Mock API Suite

A collection of **mock FastAPI backends** designed by **Alonzo AI** for evaluating frontend developers.

These APIs simulate real-world applications using **file-based storage** (no databases), RESTful endpoints, and realistic data models.

---

## 📦 Available Projects

### 1. 🛒 Alonzo Store API

**Use Case**: Admin product management dashboard

- CRUD for products and categories
- Filter by category, price, and name
- Pagination support
- File-backed persistence (`products.json`, `categories.json`)

📁 Folder: `alonzo_store_api`

---

### 2. 🍳 Alonzo Recipes API

**Use Case**: Recipe catalog with ingredients and cooking steps

- CRUD for recipes
- Structured ingredients (`ingredient`, `quantity`, `unit`)
- Instructions as steps
- Filter by dietary tags, prep time, ingredients
- List available ingredients, categories, dietary options

📁 Folder: `alonzo_recipes_api`

---

### 3. 📝 Alonzo Microblog API

**Use Case**: Microblog with tagging, filtering, and comments

- CRUD for posts
- Filter by author, tags, and search text
- Commenting support (nested in posts)
- Tag listing
- Pagination

📁 Folder: `alonzo_microblog_api`

---

### 4. 🎓 Alonzo Courses API

**Use Case**: Online course platform with enrollment tracking

- CRUD for courses and lessons
- Add lessons dynamically to courses
- Enroll students by name
- Track completed lessons
- Filter by category, level, instructor, tags
- List all instructors and course categories

📁 Folder: `alonzo_courses_api`

---

## 🛠 Common Features

- ✅ Built with **FastAPI**
- ✅ No external database — uses local `.json` files
- ✅ RESTful design with proper request/response schemas
- ✅ CORS enabled (for frontend integration)
- ✅ Ready to use with `fetch`/`axios` in React/Vue/Next.js apps
- ✅ Interactive API docs via `/docs`

---

## 🧪 Ideal For

- Evaluating frontend candidates (React/Vue)
- Building test dashboards
- Prototyping without DB setup
- Teaching API integration

---

## 📜 License

MIT License — developed by [Alonzo AI](https://alonzo.ai)
Use freely for internal testing, evaluations, and learning.

---

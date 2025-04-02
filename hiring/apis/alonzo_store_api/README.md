

### 📘 `README.md` — Alonzo Store Admin API (Mock)

---

## 🛍️ Overview

This is a mock **FastAPI backend** for the **Alonzo Store Admin** panel.
It is built to help frontend developers build and test admin interfaces for managing products and categories.

- ✅ No database required
- ✅ Uses local JSON files for persistent storage
- ✅ Filter, pagination, and CRUD support
- ✅ Easily extendable and React-friendly

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the server

```bash
uvicorn main:app --reload
```

Server will start at `http://localhost:8000`

---

## 📦 Project Structure

```
alonzo_store_api/
├── main.py                  # App entrypoint
├── models.py                # Pydantic models
├── routes/
│   ├── products.py          # Product APIs
│   └── categories.py        # Category APIs
├── storage.py               # Persistent file-based storage
├── data/
│   ├── products.json        # Product data
│   └── categories.json      # Category data
├── requirements.txt         # Dependencies
└── README.md                # You're here!
```

---

## 🔧 API Usage

### 🌐 Base URL: `http://localhost:8000`

---

### 📦 Product Endpoints

#### `GET /products`

Fetch products with optional filters and pagination:

| Query Param     | Type   | Description                         |
|-----------------|--------|-------------------------------------|
| `category`      | string | Filter by category name             |
| `min_price`     | float  | Minimum price                       |
| `max_price`     | float  | Maximum price                       |
| `name_prefix`   | string | Filter by name starting with prefix |
| `skip`          | int    | Pagination offset (default: 0)      |
| `limit`         | int    | Pagination limit (default: 10)      |

Example:

```
GET /products?category=Shoes&min_price=20&limit=5
```

---

#### `POST /products`

Create a new product

```json
{
  "name": "New Product",
  "image": "https://example.com/image.png",
  "category": "Shoes",
  "price": 49.99,
  "description": "Cool shoes",
  "stock_available": 10
}
```

---

#### `PUT /products/{product_id}`

Update an existing product

---

#### `DELETE /products/{product_id}`

Delete a product by ID

---

### 🗂️ Category Endpoints

#### `GET /categories`

List all product categories

---

#### `POST /categories`

Create a new category

```json
{
  "name": "New Category"
}
```

---

## 📁 Mock Data Preloaded

### Categories

- Shoes
- Clothing
- Accessories

### Products

- Running Shoes
- Graphic T-Shirt
- Baseball Cap

---

## 🛠️ Extras

### 🔒 No Authentication
This mock API is fully open and requires no auth headers.

### 💾 Persistence
All data is stored in:
- `data/products.json`
- `data/categories.json`

You can manually edit these files or reset them anytime.

---

## 🤝 License

MIT — built for educational/demo purposes by **Alonzo AI**.

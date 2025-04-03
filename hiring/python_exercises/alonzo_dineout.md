## 🍽️ **Evaluation Task: Alonzo Dineout**

### 🧠 Context
You are building the backend for **Alonzo Dineout**, a restaurant recommendation platform where users can:

- Discover restaurants
- View dishes offered by them
- Submit reviews
- Search and filter based on cuisine, dish, rating, location, and more

This project must use **FastAPI** and **JSON files** for all data persistence — no databases.

---

### 📦 Entities

#### 🏢 `Restaurant`
```json
{
  "id": "uuid",
  "name": "Tandoori Delight",
  "location": "Hyderabad",
  "cuisine": ["Indian", "Tandoori"],
  "rating": 4.4,
  "dish_ids": ["uuid1", "uuid2"],
  "review_ids": ["uuidA", "uuidB"]
}
```

#### 🍛 `Dish`
```json
{
  "id": "uuid",
  "restaurant_id": "uuid",
  "name": "Paneer Tikka",
  "description": "Grilled cottage cheese with spices",
  "price": 280.0,
  "is_vegetarian": true
}
```

#### ✍️ `Review`
```json
{
  "id": "uuid",
  "restaurant_id": "uuid",
  "reviewer": "ganesh@example.com",
  "rating": 5,
  "comment": "Amazing flavor and service!",
  "created_at": "2025-04-03T12:30:00Z"
}
```

---

### 🔌 API Endpoints

#### 🏢 Restaurant APIs

- `GET /restaurants`: List all restaurants
  - Optional filters: `cuisine`, `location`, `rating_gt`, `rating_lt`, `dish`
  - Optional sort: `rating`, `name`
- `GET /restaurants/{id}`: Get details of a restaurant, including its dishes and reviews
- `POST /restaurants`: Add a new restaurant
- `PUT /restaurants/{id}`: Edit a restaurant (name, location, cuisine)
- `DELETE /restaurants/{id}`: Delete a restaurant

---

#### 🍛 Dish APIs

- `GET /dishes`: List all dishes
  - Optional filters: `is_vegetarian`, `price_lt`, `price_gt`, `restaurant_id`
- `POST /restaurants/{restaurant_id}/dishes`: Add dish to a restaurant
- `PUT /dishes/{id}`: Edit a dish
- `DELETE /dishes/{id}`: Remove dish

---

#### ✍️ Review APIs

- `POST /restaurants/{restaurant_id}/reviews`: Add a review
- `GET /restaurants/{restaurant_id}/reviews`: Get all reviews for a restaurant
- `DELETE /reviews/{review_id}`: Delete a review
- Automatically recalculate average `rating` of a restaurant after review changes

---

### 🗃️ JSON File Storage

- `restaurants.json` → stores restaurant records
- `dishes.json` → stores all dishes
- `reviews.json` → stores all reviews

All file reads/writes should be concurrency-safe using a utility layer.

---

### 🔐 Auth / User Handling

- Not implemented — `reviewer` field is just a string
- Assume user identity is passed with the payload

---
Got it! Here's the **updated and simplified file structure** for the **Alonzo Dineout** project — no `services/`, no `utils/`, and includes a `requirements.txt` file.

---

## 📁 Final Folder Structure — *Alonzo Dineout*

```
alonzo_dineout/
├── main.py                        # FastAPI app entrypoint
├── requirements.txt              # Python dependencies
├── models/
│   ├── restaurant.py              # Pydantic models for Restaurant
│   ├── dish.py                    # Pydantic models for Dish
│   └── review.py                  # Pydantic models for Review
├── routers/
│   ├── restaurants.py             # Restaurant CRUD and search APIs
│   ├── dishes.py                  # Dish endpoints per restaurant
│   └── reviews.py                 # Review management endpoints
├── data/
│   ├── restaurants.json           # Stores restaurant objects
│   ├── dishes.json                # Stores dish objects
│   └── reviews.json               # Stores review objects
└── README.md                      # Setup and API documentation
```

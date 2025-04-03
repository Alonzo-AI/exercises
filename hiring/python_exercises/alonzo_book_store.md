## 📘 **Evaluation Task: Alonzo Books**

### 🧠 Context
Alonzo Books is a mock online bookstore API. You are tasked with building its backend using **FastAPI**, with **file-based JSON storage** (no databases). The system must support:

- Book and Review management
- Metadata-based search (e.g., by author, price range, tags, rating)
- RESTful APIs for everything

---

### 🔧 Tech Requirements

- **Framework**: FastAPI
- **Storage**: JSON files (for books & reviews)
- **Data Models**: Use Pydantic
- **No database or ORM**
- **No UI** — API-only project
- Well-structured code with separation of concerns (e.g., routers, services)
- Keep a perfect requirements.txt

---

### 📦 Entities

#### 📚 `Book`
```json
{
  "id": "uuid",
  "title": "string",
  "author": "string",
  "genre": "string",
  "price": float,
  "tags": ["string", ...],
  "published_year": 2023,
  "isbn": "string",
  "rating": float (avg of all reviews)
}
```

#### ✍️ `Review`
```json
{
  "id": "uuid",
  "book_id": "uuid",
  "reviewer": "string",
  "rating": int (1-5),
  "comment": "string"
}
```

---

### 🔌 Required APIs

#### 📘 Book APIs
- `GET /books`: List all books
- `GET /books/{id}`: Get book by ID
- `POST /books`: Add a new book
- `PUT /books/{id}`: Update a book
- `DELETE /books/{id}`: Delete a book
- `GET /genres`: List all generes
- `GET /authors`: List all authors



#### 🔎 Search API
- `GET /books/search`: Metadata search with query params:
  - `author`, `genre`, `price_lt`, `price_gt`, `tag`, `published_year`

#### ✍️ Review APIs
- `POST /books/{book_id}/reviews`: Add review for a book
- `GET /books/{book_id}/reviews`: Get all reviews for a book
- `DELETE /reviews/{review_id}`: Delete a review

---

### 📁 JSON Storage Structure

#### `books.json`
```json
[
  {
    "id": "uuid",
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "genre": "Programming",
    "price": 25.99,
    "tags": ["clean-code", "best-practices"],
    "published_year": 2008,
    "isbn": "9780132350884",
    "rating": 4.6
  }
]
```

#### `reviews.json`
```json
[
  {
    "id": "uuid",
    "book_id": "uuid",
    "reviewer": "Jane",
    "rating": 5,
    "comment": "Loved it!"
  }
]
```

---

### ✨ Additional Requirements
- Pagination in list/search endpoints
- Sort by price, rating, published year
- Basic tests using `pytest`

---
### Folder Structure
alonzo_books/
├── main.py                        # FastAPI app entrypoint
├── models/
│   ├── book.py                    # Pydantic models for Book
│   └── review.py                  # Pydantic models for Review
├── routers/
│   ├── books.py                   # API routes for books (CRUD + search)
│   └── reviews.py                 # API routes for reviews
├── data/
│   ├── books.json                 # Persistent book data
│   └── reviews.json               # Persistent review data
│- requirements.txt
└── README.md                      # Project setup & usage instructions

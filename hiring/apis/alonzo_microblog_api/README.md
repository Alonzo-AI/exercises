# 📝 Alonzo Microblog API

**Alonzo Microblog** is a mock backend built with FastAPI, simulating a microblogging platform.
It is designed to evaluate frontend developers by providing realistic API interaction scenarios.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs on:
📍 `http://localhost:8000`

Interactive API Docs:
🔍 `http://localhost:8000/docs`

---

## 🧠 Key Features

- 🗃️ File-based persistence (`posts.json`) — **no database needed**
- 🧾 Full CRUD for blog posts
- 💬 Commenting support (nested per post)
- 🔍 Powerful filtering: by `author`, `tags`, `search` (title/content)
- 🏷️ Tags endpoint to assist with post discovery
- 🔢 Pagination support with `skip` and `limit`
- 🧪 Comes preloaded with **5 sample posts** and **2 comments** per post
- 🔓 CORS enabled for frontend integration (React-ready)

---

## 🗃️ Post Structure

Each post includes:

```json
{
  "id": 1,
  "author": "ganesh",
  "title": "Post #1 - Intro",
  "content": "This is the content for post number 1, discussing intro and more.",
  "tags": ["intro", "alonzo"],
  "timestamp": "2025-04-01T10:00:00Z",
  "likes": 25,
  "comments": [
    {
      "id": 1,
      "author": "manish",
      "content": "Great thoughts on intro!",
      "timestamp": "2025-04-01T09:00:00Z"
    },
    {
      "id": 2,
      "author": "alice",
      "content": "Thanks for writing this!",
      "timestamp": "2025-04-01T08:30:00Z"
    }
  ]
}
```

---

## 🔌 API Overview

### 📦 Posts

| Method | Endpoint         | Description                              |
|--------|------------------|------------------------------------------|
| GET    | `/posts`         | List all posts with filters              |
| POST   | `/posts`         | Create a new post                        |
| PUT    | `/posts/{id}`    | Update a post by ID                      |
| DELETE | `/posts/{id}`    | Delete a post by ID                      |
| GET    | `/posts/tags`    | Get all unique tags                      |

#### 🔍 Filtering Query Params for `GET /posts`

| Param     | Type     | Description                         |
|-----------|----------|-------------------------------------|
| `author`  | string   | Filter posts by author              |
| `tags`    | list     | Filter posts that include all tags  |
| `search`  | string   | Match in title or content           |
| `skip`    | integer  | Pagination offset                   |
| `limit`   | integer  | Pagination size (default: 10)       |

Example:
```
/posts?author=ganesh&tags=fastapi&search=hello&limit=5
```

---

### 💬 Comments

Each post has its own list of comments. You can:

| Method | Endpoint                             | Description               |
|--------|--------------------------------------|---------------------------|
| GET    | `/posts/{id}/comments`               | List comments on a post   |
| POST   | `/posts/{id}/comments`               | Add a comment to a post   |
| DELETE | `/posts/{id}/comments/{comment_id}`  | Delete a comment by ID    |

Comment model:

```json
{
  "id": 1,
  "author": "alice",
  "content": "This is a great read!",
  "timestamp": "2025-04-01T09:30:00Z"
}
```

---

## 🧪 Ideal Use Case for Frontend Evaluation

Frontend developers can:
- Build blog UIs and post lists
- Implement advanced filtering with query params
- Build comment threads per post
- Use pagination and tag-based views
- Handle POST/PUT/DELETE operations

---

## 📁 Project Structure

```
alonzo_microblog_api/
├── main.py              # FastAPI entrypoint
├── models.py            # Pydantic models
├── routes/
│   └── posts.py         # All routes for posts + comments
├── storage.py           # File-based data handling
├── data/
│   └── posts.json       # Persistent storage
├── requirements.txt     # FastAPI, Uvicorn
└── README.md            # You're here!
```

---

## 🪪 License

MIT License — maintained by **Alonzo AI**
Crafted for candidate evaluations, mock integrations, and rapid prototyping.

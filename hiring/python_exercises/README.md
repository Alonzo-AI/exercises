
# 🐍 Alonzo Python Developer Evaluation Exercises

Welcome! This repository contains a collection of Python backend development exercises designed to evaluate real-world software engineering and API design skills.

Each project simulates a real-world backend scenario using **FastAPI** and **JSON file-based storage** — no database or frontend required.

---

## 📋 Instructions

Please read this document carefully before starting.

### First Things
1. Read FastAPI documentation
2. Install dependencies


### 🧑‍💻 Your Task
- Choose the assigned project folder (e.g., `alonzo_books`, `alonzo_quicktest`, etc.)
- Follow the instructions in the project's **README.md** file
- Complete the task within the time window provided (typically 2.5–3 hours)
- You may add any libraries you need in `requirements.txt`

---

## 🛠 Setup Guide

1. Clone the repo or download the ZIP file
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
5. Visit the interactive API docs at:
   ```
   http://localhost:8000/docs
   ```

---

## 🧪 Testing Your APIs

Use any of the following to test your endpoints:

- [FastAPI Swagger UI](http://localhost:8000/docs)
---

## 🚀 Project Expectations

- Clean, well-structured code (use routers and models as needed)
- Functional, working APIs that meet the spec
- Proper use of JSON file read/write operations
- Safe file handling (read-modify-write)
- No use of databases or external storage services

---

## 📁 Folder Structure (General Guideline)

```
project_name/
├── main.py                # FastAPI entrypoint
├── requirements.txt
├── models/                # Pydantic models
├── routers/               # API route definitions
├── data/                  # JSON files for persistence
└── README.md              # Project-specific instructions
```

---

## Testing

It is must to write unit tests with pytest.


## 🧑‍🔧 Submitting Your Work

- Put your code in a repo and share the URL

---

## ❓ Questions?

If you're unsure about the task or need clarification:
- Reach out to your point of contact immediately
- Clearly mention which project and part you're asking about

---

Happy hacking! 🚀
— *The Alonzo AI Team*
```

---

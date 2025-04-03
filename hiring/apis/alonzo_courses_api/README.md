
# 🎓 Alonzo Courses API

A mock **FastAPI backend** for managing online courses, lessons, and student progress.

Built to evaluate frontend developers — no database required, fully file-based, and easy to work with using `fetch` or `axios`.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

📍 Runs at: http://localhost:8000
📘 Interactive docs: http://localhost:8000/docs

---

## 📦 Project Structure

```
alonzo_courses_api/
├── main.py
├── models.py
├── routes/
│   ├── courses.py
│   └── enrollments.py
├── storage.py
├── data/
│   ├── courses.json
│   └── enrollments.json
├── requirements.txt
└── README.md
```

---

## 🧠 Features

- ✅ File-based persistence (no DB)
- ✅ Create, read, update, delete courses
- ✅ Each course contains structured lessons
- ✅ Students can enroll by name
- ✅ Track lesson completion per student
- ✅ Filter courses by category, instructor, level, tags
- ✅ List all course categories and instructors
- ✅ Add lessons to an existing course
- ✅ Sample data included with 3 courses and 3 lessons each

---

## 📘 Course Model

```json
{
  "id": 1,
  "title": "Intro to React",
  "description": "Learn the basics of React.js.",
  "instructor": "Alice",
  "tags": ["frontend", "react"],
  "category": "Web Development",
  "level": "beginner",
  "duration": 10,
  "image": "https://example.com/images/courses/react.png",
  "lessons": [
    {
      "id": 1,
      "title": "React Components",
      "content": "Understanding components in React.",
      "image": "https://example.com/images/lessons/components.png"
    }
  ]
}
```

---

## 🔌 API Reference

### 📚 Courses

| Method | Endpoint                  | Description                            |
|--------|---------------------------|----------------------------------------|
| GET    | `/courses`                | List all courses with filters          |
| GET    | `/courses/{id}`           | Get course by ID                       |
| POST   | `/courses`                | Create a course                        |
| PUT    | `/courses/{id}`           | Update a course                        |
| DELETE | `/courses/{id}`           | Delete a course                        |
| GET    | `/courses/categories`     | List unique categories                 |
| GET    | `/courses/instructors`    | List unique instructors                |
| POST   | `/courses/{id}/lessons`   | Add a new lesson to a course           |

#### Query Params for `/courses`

| Param      | Type     | Description                          |
|------------|----------|--------------------------------------|
| `category` | string   | Filter by course category            |
| `instructor` | string | Filter by instructor                 |
| `level`    | string   | Filter by course level               |
| `tags`     | list     | Filter courses that include all tags |
| `skip`     | int      | Pagination offset                    |
| `limit`    | int      | Pagination limit                     |

Example:
```
/courses?category=AI&tags=ethics&instructor=manish
```

---

### 👥 Enrollments

| Method | Endpoint                                       | Description                              |
|--------|------------------------------------------------|------------------------------------------|
| GET    | `/enrollments`                                | List all enrollments                     |
| GET    | `/enrollments/student/{name}`                 | Get enrollments by student name          |
| GET    | `/enrollments/course/{course_id}`             | Get enrollments by course ID             |
| POST   | `/enrollments`                                | Enroll a student                         |
| POST   | `/enrollments/{enrollment_id}/complete/{lesson_id}` | Mark a lesson as complete for a student |

#### Enrollment Model

```json
{
  "id": 1,
  "student_name": "Ganesh",
  "course_id": 1,
  "completed_lessons": [1, 2]
}
```

---

## 📁 Sample Data

Pre-loaded in `data/`:
- 3 courses in different categories
- 3 lessons per course
- 3 sample enrollments

---

## 🪪 License

MIT — by **Alonzo AI** for internal use and candidate evaluation.

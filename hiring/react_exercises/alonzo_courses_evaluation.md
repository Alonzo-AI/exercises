# 🎓 Alonzo Courses — React Evaluation Task

## 🧾 Title
Build an online course dashboard to browse, enroll, and track progress in courses.

## 🎯 Introduction & Objective
Build a student-facing interface to display courses and track lesson completion using the Alonzo Courses API. This evaluates form handling, progress management, and relational data views.

## 🚀 Getting Started

1. Clone or unzip the API project: `alonzo_courses_api` (https://github.com/Alonzo-AI/exercises)
2. Follow instructions on installing the api and running it.
3. Run the API:

```bash
uvicorn main:app --reload
```

4. Use the docs at: `http://localhost:8000/docs`

## 📦 Scope of Evaluation

### 🔹 Course Browser

- [ ] List courses with filters for category, instructor, level
- [ ] Search courses by tags
- [ ] Add, Update and Delete courses
- [ ] Add lessons under a course
- [ ] View course details with lessons
- [ ] Show course image and duration

### 🔹 Enrollment Flow

- [ ] Enroll in a course by entering a student name
- [ ] Display enrolled courses per student
- [ ] View progress: completed vs total lessons
- [ ] Mark lessons complete for each enrollment

### 🔹 Extra Views

- [ ] Use `/courses/categories` and `/courses/instructors` for filters
- [ ] Add a lesson to an existing course

---

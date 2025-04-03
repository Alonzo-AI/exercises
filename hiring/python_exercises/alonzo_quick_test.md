Here is the **complete and final FastAPI evaluation spec** for **Alonzo QuickTest**, fully aligned with your requirement of **question-by-question answer submission**, using **JSON-based storage**, and includes detailed API definitions.

---

# 🧠 **Alonzo QuickTest**

> A FastAPI-powered quiz authoring platform where users answer quizzes **one question at a time**. All data is stored in JSON files — no databases.

---

## 📦 Data Models

### 📝 `Quiz`
```json
{
  "id": "uuid",
  "title": "Python Basics",
  "description": "A quiz to test your Python fundamentals",
  "question_ids": ["q1", "q2", "q3"],
  "created_at": "2025-04-03T10:00:00Z"
}
```

---

### ❓ `Question`
```json
{
  "id": "uuid",
  "quiz_id": "uuid",
  "text": "What is the output of print(2 ** 3)?",
  "options": ["5", "6", "8", "9"],
  "correct_index": 2
}
```

---

### 🧾 `Submission`
Each answer is recorded independently in `submissions.json`.

```json
{
  "id": "uuid",
  "quiz_id": "uuid",
  "question_id": "q1",
  "user_name": "Alice",
  "answer": 2,
  "submitted_at": "2025-04-03T12:00:00Z"
}
```

---

## 🔌 API Endpoints

### 📘 Quiz APIs

#### `POST /quizzes`
Create a new quiz.

**Request Body:**
```json
{
  "title": "Python Basics",
  "description": "A simple Python quiz"
}
```

**Response:**
```json
{
  "id": "uuid",
  "title": "Python Basics",
  "description": "A simple Python quiz",
  "question_ids": [],
  "created_at": "..."
}
```

---

#### `GET /quizzes`
List all quizzes.

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Python Basics",
    "description": "A simple Python quiz"
  }
]
```

---

#### `GET /quizzes/{quiz_id}`
Get quiz details with all its questions.

**Response:**
```json
{
  "id": "uuid",
  "title": "Python Basics",
  "description": "...",
  "questions": [
    {
      "id": "q1",
      "text": "...",
      "options": ["A", "B", "C", "D"]
    }
  ]
}
```

---

#### `DELETE /quizzes/{quiz_id}`
Deletes a quiz and its associated questions.

**Response:**
`204 No Content`

---

### ❓ Question APIs

#### `POST /quizzes/{quiz_id}/questions`
Add a question to a quiz.

**Request Body:**
```json
{
  "text": "What does len([1,2,3]) return?",
  "options": ["2", "3", "4", "error"],
  "correct_index": 1
}
```

**Response:**
```json
{
  "id": "q1",
  "quiz_id": "uuid",
  "text": "...",
  "options": [...],
  "correct_index": 1
}
```

---

#### `PUT /questions/{question_id}`
Update a question.

**Request Body:**
```json
{
  "text": "Updated?",
  "options": ["Yes", "No", "Maybe"],
  "correct_index": 0
}
```

**Response:** Updated question object

---

#### `DELETE /questions/{question_id}`
Deletes a question.

**Response:**
`204 No Content`

---

### 🧾 Submission APIs (Question-by-Question)

#### `POST /submit`
Submit an answer for one question in a quiz.

**Request Body:**
```json
{
  "quiz_id": "quiz-uuid",
  "question_id": "q1",
  "user_name": "Alice",
  "answer": 2
}
```

**Response:**
```json
{
  "message": "Answer recorded",
  "submission_id": "sub-uuid"
}
```

---

#### `GET /progress/{quiz_id}/{user_name}`
Get the current progress and score of a user in a quiz.

**Response:**
```json
{
  "user_name": "Alice",
  "quiz_id": "quiz-uuid",
  "answered_questions": 2,
  "total_questions": 3,
  "score": 2,
  "completed": false,
  "progress": "2/3 answered"
}
```

---

#### `GET /submissions/{quiz_id}`
Get **all** submissions (individual question attempts) for a quiz.

**Response:**
```json
[
  {
    "id": "uuid",
    "user_name": "Alice",
    "question_id": "q1",
    "answer": 2,
    "submitted_at": "..."
  }
]
```

---

#### `GET /submissions/{quiz_id}/{user_name}`
Get all of a user’s answers to a quiz.

**Response:**
```json
[
  {
    "question_id": "q1",
    "answer": 2,
    "submitted_at": "..."
  },
  {
    "question_id": "q2",
    "answer": 0,
    "submitted_at": "..."
  }
]
```

---

#### `GET /submissions/score/{quiz_id}/{user_name}/`
Get user's score for that quiz

**Response:**
```json
{
  "score" : 5,
  "num_questions" : 10
}
```

---

## 🗃️ JSON Files

| File | Description |
|------|-------------|
| `quizzes.json` | Quiz metadata |
| `questions.json` | All quiz questions |
| `submissions.json` | Individual user answers |

---

## 🗂️ Folder Structure

```
alonzo_quicktest/
├── main.py
├── requirements.txt
├── models/
│   ├── quiz.py
│   ├── question.py
│   └── submission.py
├── routers/
│   ├── quizzes.py
│   ├── questions.py
│   └── submissions.py
├── data/
│   ├── quizzes.json
│   ├── questions.json
│   └── submissions.json
└── README.md
```

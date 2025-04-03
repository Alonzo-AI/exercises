from pydantic import BaseModel
from typing import List, Optional

class Lesson(BaseModel):
    id: int
    title: str
    content: str
    image: Optional[str]  # URL to lesson image

class Course(BaseModel):
    id: int
    title: str
    description: str
    instructor: str
    tags: List[str]
    category: str
    level: str
    duration: int
    image: Optional[str]  # URL to course image
    lessons: List[Lesson]

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor: str
    tags: List[str]
    category: str
    level: str
    duration: int
    image: Optional[str]
    lessons: List[Lesson]


class Enrollment(BaseModel):
    id: int
    student_name: str
    course_id: int
    completed_lessons: List[int]

class EnrollmentCreate(BaseModel):
    student_name: str
    course_id: int

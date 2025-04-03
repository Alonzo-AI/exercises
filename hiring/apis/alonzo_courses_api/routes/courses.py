from fastapi import APIRouter, HTTPException, Query
from models import Course, CourseCreate
from storage import courses, save_courses, get_next_id
from typing import Optional, List

router = APIRouter()

@router.get("/")
def list_courses(
    category: Optional[str] = None,
    instructor: Optional[str] = None,
    level: Optional[str] = None,
    tags: Optional[List[str]] = Query(None),
    skip: int = 0,
    limit: int = 10
):
    filtered = courses

    if category:
        filtered = [c for c in filtered if c.get("category", "").lower() == category.lower()]
    if instructor:
        filtered = [c for c in filtered if c.get("instructor", "").lower() == instructor.lower()]
    if level:
        filtered = [c for c in filtered if c.get("level", "").lower() == level.lower()]
    if tags:
        filtered = [c for c in filtered if all(tag in c.get("tags", []) for tag in tags)]

    return filtered[skip : skip + limit]


@router.get("/categories")
def list_categories():
    return sorted({c.get("category", "").strip() for c in courses if c.get("category")})


@router.get("/instructors")
def list_instructors():
    return sorted({c.get("instructor", "").strip() for c in courses if c.get("instructor")})



@router.get("/{course_id}")
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

@router.post("/")
def create_course(data: CourseCreate):
    new_id = get_next_id(courses)
    course = Course(id=new_id, **data.dict())
    courses.append(course.dict())
    save_courses()
    return course

@router.put("/{course_id}")
def update_course(course_id: int, data: CourseCreate):
    for i, course in enumerate(courses):
        if course["id"] == course_id:
            courses[i] = Course(id=course_id, **data.dict()).dict()
            save_courses()
            return courses[i]
    raise HTTPException(status_code=404, detail="Course not found")


@router.delete("/{course_id}")
def delete_course(course_id: int):
    for i, course in enumerate(courses):
        if course["id"] == course_id:
            courses.pop(i)
            save_courses()
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Course not found")


from fastapi import Body

@router.post("/{course_id}/lessons")
def add_lesson(course_id: int, lesson: dict = Body(...)):
    for course in courses:
        if course["id"] == course_id:
            existing_ids = [l["id"] for l in course.get("lessons", [])]
            lesson["id"] = max(existing_ids, default=0) + 1
            course.setdefault("lessons", []).append(lesson)
            save_courses()
            return lesson
    raise HTTPException(status_code=404, detail="Course not found")

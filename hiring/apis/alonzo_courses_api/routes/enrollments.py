from fastapi import APIRouter, HTTPException
from models import Enrollment, EnrollmentCreate
from storage import enrollments, save_enrollments, get_next_id

router = APIRouter()

@router.get("/")
def list_enrollments():
    return enrollments

@router.get("/student/{student_name}")
def get_enrollments_by_student(student_name: str):
    return [e for e in enrollments if e["student_name"].lower() == student_name.lower()]

@router.get("/course/{course_id}")
def get_enrollments_by_course(course_id: int):
    return [e for e in enrollments if e["course_id"] == course_id]

@router.post("/")
def enroll_student(data: EnrollmentCreate):
    new_id = get_next_id(enrollments)
    enrollment = Enrollment(id=new_id, completed_lessons=[], **data.dict())
    enrollments.append(enrollment.dict())
    save_enrollments()
    return enrollment

@router.post("/{enrollment_id}/complete/{lesson_id}")
def complete_lesson(enrollment_id: int, lesson_id: int):
    for e in enrollments:
        if e["id"] == enrollment_id:
            if lesson_id not in e["completed_lessons"]:
                e["completed_lessons"].append(lesson_id)
                save_enrollments()
            return e
    raise HTTPException(status_code=404, detail="Enrollment not found")

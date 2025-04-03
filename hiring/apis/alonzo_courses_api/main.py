from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import courses, enrollments

app = FastAPI(title="Alonzo Courses API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["Enrollments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Alonzo Courses API"}
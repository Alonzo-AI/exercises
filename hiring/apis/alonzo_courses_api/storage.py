import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
COURSES_FILE = DATA_DIR / "courses.json"
ENROLLMENTS_FILE = DATA_DIR / "enrollments.json"

def load_json(path):
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return []

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

courses = load_json(COURSES_FILE)
enrollments = load_json(ENROLLMENTS_FILE)

def get_next_id(items):
    return max((item["id"] for item in items), default=0) + 1

def save_courses():
    save_json(COURSES_FILE, courses)

def save_enrollments():
    save_json(ENROLLMENTS_FILE, enrollments)
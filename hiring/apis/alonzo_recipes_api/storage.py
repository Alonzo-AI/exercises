import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

RECIPES_FILE = DATA_DIR / "recipes.json"

def load_json(file_path):
    if file_path.exists():
        with file_path.open("r") as f:
            return json.load(f)
    return []

def save_json(file_path, data):
    with file_path.open("w") as f:
        json.dump(data, f, indent=2)

recipes = load_json(RECIPES_FILE)

def get_next_id(items):
    if not items:
        return 1
    return max(item['id'] for item in items) + 1

def save_recipes():
    save_json(RECIPES_FILE, recipes)
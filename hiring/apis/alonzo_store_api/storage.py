import json
from pathlib import Path
from models import Product, Category

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

PRODUCTS_FILE = DATA_DIR / "products.json"
CATEGORIES_FILE = DATA_DIR / "categories.json"

def load_json(file_path):
    if file_path.exists():
        with file_path.open("r") as f:
            return json.load(f)
    return []

def save_json(file_path, data):
    with file_path.open("w") as f:
        json.dump(data, f, indent=2)

products = load_json(PRODUCTS_FILE)
categories = load_json(CATEGORIES_FILE)

def get_next_id(items):
    if not items:
        return 1
    return max(item['id'] for item in items) + 1

def save_products():
    save_json(PRODUCTS_FILE, products)

def save_categories():
    save_json(CATEGORIES_FILE, categories)
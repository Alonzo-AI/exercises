import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
POSTS_FILE = DATA_DIR / "posts.json"
DATA_DIR.mkdir(exist_ok=True)

def load_json(file_path):
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

posts = load_json(POSTS_FILE)

def get_next_post_id():
    return max((p["id"] for p in posts), default=0) + 1

def get_next_comment_id(post):
    return max((c["id"] for c in post.get("comments", [])), default=0) + 1

def save_posts():
    save_json(POSTS_FILE, posts)
from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models import Post, PostCreate, PostUpdate, CommentCreate
from storage import posts, save_posts, get_next_post_id, get_next_comment_id

router = APIRouter()

@router.get("/")
def list_posts(
    author: Optional[str] = None,
    tags: Optional[List[str]] = Query(None),
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
):
    filtered = posts

    if author:
        filtered = [p for p in filtered if p["author"].lower() == author.lower()]
    if tags:
        filtered = [p for p in filtered if all(tag in p.get("tags", []) for tag in tags)]
    if search:
        filtered = [
            p for p in filtered
            if search.lower() in p["title"].lower() or search.lower() in p["content"].lower()
        ]

    return filtered[skip : skip + limit]

@router.post("/")
def create_post(data: PostCreate):
    new_id = get_next_post_id()
    post = Post(id=new_id, comments=[], likes=0, **data.dict())
    posts.append(post.dict())
    save_posts()
    return post

@router.put("/{post_id}")
def update_post(post_id: int, data: PostUpdate):
    for i, p in enumerate(posts):
        if p["id"] == post_id:
            updated = {**p, **{k: v for k, v in data.dict().items() if v is not None}}
            posts[i] = updated
            save_posts()
            return updated
    raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/{post_id}")
def delete_post(post_id: int):
    for i, p in enumerate(posts):
        if p["id"] == post_id:
            posts.pop(i)
            save_posts()
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@router.get("/tags")
def list_tags():
    tag_set = set()
    for p in posts:
        tag_set.update(p.get("tags", []))
    return sorted(tag_set)

@router.get("/{post_id}/comments")
def list_comments(post_id: int):
    for p in posts:
        if p["id"] == post_id:
            return p.get("comments", [])
    raise HTTPException(status_code=404, detail="Post not found")

@router.post("/{post_id}/comments")
def add_comment(post_id: int, data: CommentCreate):
    for p in posts:
        if p["id"] == post_id:
            new_comment_id = get_next_comment_id(p)
            comment = {
                "id": new_comment_id,
                "author": data.author,
                "content": data.content,
                "timestamp": data.timestamp
            }
            p.setdefault("comments", []).append(comment)
            save_posts()
            return comment
    raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/{post_id}/comments/{comment_id}")
def delete_comment(post_id: int, comment_id: int):
    for p in posts:
        if p["id"] == post_id:
            comments = p.get("comments", [])
            for i, c in enumerate(comments):
                if c["id"] == comment_id:
                    comments.pop(i)
                    save_posts()
                    return {"message": "Comment deleted"}
            raise HTTPException(status_code=404, detail="Comment not found")
    raise HTTPException(status_code=404, detail="Post not found")

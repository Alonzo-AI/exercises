from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    author: str
    content: str
    timestamp: str

class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str
    tags: List[str]
    timestamp: str
    likes: int = 0
    comments: List[Comment] = []

class PostCreate(BaseModel):
    author: str
    title: str
    content: str
    tags: List[str]
    timestamp: str

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    tags: Optional[List[str]]

class CommentCreate(BaseModel):
    author: str
    content: str
    timestamp: str
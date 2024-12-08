from dataclasses import dataclass
from typing import Any, Dict, List
from pydantic import BaseModel

Tag = str

class Reactions(BaseModel):
    likes: int
    dislikes: int

class BlogPost(BaseModel):
    id: int
    title: str
    body: str
    userId: int
    views: int
    tags: List[Tag]
    reactions: Reactions

BlogPostResponse = List[Dict[str, Any]]
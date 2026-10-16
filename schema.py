from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class PostUpdate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str]
    createdAt: datetime 
    updatedAt: datetime
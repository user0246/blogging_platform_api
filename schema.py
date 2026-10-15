from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list

class PostResponse(BaseModel):
    title: str
    content: str
    category: str
    tags: list
    createdAt: datetime 
    updatedAt: datetime
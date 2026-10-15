from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from base import Base, engine, get_db
from schema import PostCreate, PostResponse
from models import Post

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/posts")
def all_posts():
    pass

@app.post("/posts", response_model=PostResponse)
def create_post(article: PostCreate, db: Session = Depends(get_db)):
    data = Post(
        title = article.title,
        content = article.content,
        category = article.category,
        tags = article.tags
    )

    db.add(data)
    db.commit()

    return data
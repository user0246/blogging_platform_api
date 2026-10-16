from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from sqlalchemy import or_
from base import Base, engine, get_db
from schema import PostCreate, PostResponse, PostUpdate
from models import Post
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/posts", response_model=list[PostResponse])
def all_posts(term: str | None = None, db: Session = Depends(get_db)):
    if term:
        post = db.query(Post).filter(or_(
            Post.title.ilike(f"%{term}%"),
            Post.content.ilike(f"%{term}%"),
            Post.category.ilike(f"%{term}%")
            )).all()
        return post
    else:
        posts = db.query(Post).all() 
        return posts

@app.get("/posts/{id}", response_model=PostResponse)
def post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post


@app.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(article: PostCreate, db: Session = Depends(get_db)):
    data = Post(
        title = article.title,
        content = article.content,
        category = article.category,
        tags = article.tags
    )

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

@app.put("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def update_post(id: int, article: PostUpdate, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post.title = article.title
    post.content = article.content
    post.category = article.category
    post.tags = article.tags

    db.commit()
    db.refresh(post)

    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    db.delete(post)
    db.commit()

    return None
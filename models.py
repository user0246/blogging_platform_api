from base import Base
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy import DateTime, JSON
from datetime import datetime

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False) 
    content: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    tags: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now, nullable=False)
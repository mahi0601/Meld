from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class ReviewHistory(Base):
    __tablename__ = "review_history"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String, nullable=True)
    stars = Column(Integer)
    review_id = Column(String, index=True)
    tone = Column(String, nullable=True)
    sentiment = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

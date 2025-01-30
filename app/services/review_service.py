from sqlalchemy.orm import Session
from sqlalchemy.sql import func, desc
from app.models.review_history import ReviewHistory
from app.models.category import Category

def get_reviews_by_category(db: Session, category_id: int, limit=15, offset=0):
    return (
        db.query(ReviewHistory)
        .filter(ReviewHistory.category_id == category_id)
        .order_by(desc(ReviewHistory.created_at))
        .offset(offset)
        .limit(limit)
        .all()
    )

def get_top_trending_categories(db: Session):
    subquery = (
        db.query(ReviewHistory.review_id, func.max(ReviewHistory.created_at).label("latest"))
        .group_by(ReviewHistory.review_id)
        .subquery()
    )
    return (
        db.query(Category.id, Category.name, Category.description, 
                 func.avg(ReviewHistory.stars).label("average_stars"), 
                 func.count(ReviewHistory.id).label("total_reviews"))
        .join(ReviewHistory, Category.id == ReviewHistory.category_id)
        .group_by(Category.id)
        .order_by(desc(func.avg(ReviewHistory.stars)))
        .limit(5)
        .all()
    )
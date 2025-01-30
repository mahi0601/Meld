
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.core.database import get_db
from app.models.category import Category
from app.models.review_history import ReviewHistory
from app.tasks.log_task import save_access_log

router = APIRouter()
@router.get("/reviews/trends")
def get_review_trends(db: Session = Depends(get_db)):
    save_access_log.delay("GET /reviews/trends") 

    latest_reviews = (
        db.query(ReviewHistory.review_id, func.max(ReviewHistory.created_at).label("latest"))
        .group_by(ReviewHistory.review_id)
        .subquery()
    )

    results = (
        db.query(
            Category.id,
            Category.name,
            Category.description,
            func.avg(ReviewHistory.stars).label("average_stars"),
            func.count(ReviewHistory.review_id).label("total_reviews"),
        )
        .join(ReviewHistory, Category.id == ReviewHistory.category_id)
        .join(latest_reviews, ReviewHistory.review_id == latest_reviews.c.review_id)
        .group_by(Category.id)
        .order_by(func.avg(ReviewHistory.stars).desc())
        .limit(5)
        .all()
    )

    
    response_data = [
        {
            "id": row.id,
            "name": row.name,
            "description": row.description,
            "average_stars": round(row.average_stars, 2) if row.average_stars else 0,
            "total_reviews": row.total_reviews,
        }
        for row in results
    ]

    
    return response_data

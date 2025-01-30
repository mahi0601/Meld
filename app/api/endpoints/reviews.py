
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.review_history import ReviewHistory
from datetime import datetime

router = APIRouter()

@router.get("/reviews/", response_model=dict)
async def get_reviews(
    category_id: int,
    cursor: str = Query(None),
    db: Session = Depends(get_db),
):
    page_size = 15  

    cursor_date = datetime.fromisoformat(cursor) if cursor else None

    query = (
        db.query(ReviewHistory)
        .filter(ReviewHistory.category_id == category_id)
        .filter(ReviewHistory.text != None)
        .order_by(ReviewHistory.created_at.desc())
    )

    if cursor_date:
        query = query.filter(ReviewHistory.created_at < cursor_date)

    query = query.limit(page_size)

    compiled_query = str(query.statement.compile(compile_kwargs={"literal_binds": True}))
    print(f"Executing SQL Query:\n{compiled_query}")

    reviews = list(query) 

    print(f"Fetched {len(reviews)} reviews from the database.")
    for review in reviews:
        print(f"Review ID: {review.id}, Review Text: {review.text}, Stars: {review.stars}, Created At: {review.created_at}")


    next_cursor = reviews[-1].created_at.isoformat() if reviews else None

    return {
        "reviews": [
            {
                "id": r.id,
                "review_id": r.review_id,
                "text": r.text,
                "stars": r.stars,
                "created_at": r.created_at.isoformat(),
                "tone": r.tone,
                "sentiment": r.sentiment,
                "category_id": r.category_id,
            }
            for r in reviews
        ],
        "next_cursor": next_cursor
    }

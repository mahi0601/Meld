from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReviewBase(BaseModel):
    text: Optional[str] = None
    stars: int = Field(..., ge=1, le=10)  # Stars must be between 1 and 10
    review_id: str
    tone: Optional[str] = None
    sentiment: Optional[str] = None
    category_id: int

class ReviewCreate(ReviewBase):
    pass  # Used for creating new reviews

class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

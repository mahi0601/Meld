# Inside migrations/env.py
from app.models.category import Category
from app.models.review_history import ReviewHistory
from app.models.access_log import AccessLog
from sqlalchemy.orm import declarative_base

Base = declarative_base()

target_metadata = Base.metadata

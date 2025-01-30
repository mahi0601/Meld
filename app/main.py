from fastapi import FastAPI
from app.api.endpoints import reviews, trends

app = FastAPI()
from app.core.database import Base, engine


Base.metadata.create_all(bind=engine)

app.include_router(reviews.router, prefix="/api")
app.include_router(trends.router, prefix="/api")

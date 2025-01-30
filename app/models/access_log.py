from sqlalchemy import Column, Integer, String
from app.core.database import Base

class AccessLog(Base):
    __tablename__ = "access_log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
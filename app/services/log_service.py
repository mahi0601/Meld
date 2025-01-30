from sqlalchemy.orm import Session
from app.models.access_log import AccessLog

def log_access(db: Session, text: str):
    log_entry = AccessLog(text=text)
    db.add(log_entry)
    db.commit()
    db.close()

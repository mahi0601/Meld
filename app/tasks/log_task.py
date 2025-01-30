
from celery import Celery
from app.core.database import SessionLocal
from app.models.access_log import AccessLog

celery_app = Celery("log_task", backend="redis://localhost", broker="redis://localhost")

@celery_app.task
def save_access_log(request_text: str):
    db = SessionLocal()
    log_entry = AccessLog(text=request_text)
    db.add(log_entry)
    db.commit()
    db.close()

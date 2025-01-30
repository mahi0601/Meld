from celery import Celery

celery = Celery(
    "worker",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0"
)

@celery.task
def log_access_log(log_entry: str):
    from app.database import SessionLocal
    from app.models import AccessLog

    db = SessionLocal()
    new_log = AccessLog(text=log_entry)
    db.add(new_log)
    db.commit()
    db.close()

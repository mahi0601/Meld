from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


celery.conf.imports = ["app.tasks.log_task"]
celery.autodiscover_tasks(["app.tasks"])

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
# This scans all directories for task.py files
celery_app.autodiscover_tasks()

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

app = Celery("settings", broker="redis://localhost:6379/0")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.broker_url = 'redis://localhost:6379/0'

app.autodiscover_tasks()

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"

app.conf.beat_schedule = {
    "get_the_quote_of_the_day": {
        "task": "warehouses.tasks.get_the_quote_of_the_day",
        "schedule": crontab(minute="*/1"),  # run daily at midnight
    },
}

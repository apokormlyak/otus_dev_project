import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

app = Celery("settings")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': 'warehouses.utils.get_the_quote_of_the_day',
        'schedule': crontab(minute="*/2"),
        'options': {'queue': 'quick'}
    },

}
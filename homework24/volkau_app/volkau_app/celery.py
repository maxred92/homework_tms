import os

from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volkau_app.settings')

app = Celery('volkau_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


#testing mailing list
# app.conf.beat_schedule = {
#     'testing_celery_beat': {
#         'task': 'volkau_app.volkau_store.tasks.weekly_newsletter',
#         'schedule': 10,
#     },
# }

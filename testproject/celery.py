import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

app = Celery('testproject')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
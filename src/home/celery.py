import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# Create a Celery instance with the project name as the app name.
app = Celery('home')

# Load configuration from Django settings using CELERY namespace.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover and register tasks from all Django app configs.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

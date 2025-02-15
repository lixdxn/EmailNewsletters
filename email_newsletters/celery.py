from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_newsletters.settings')
app = Celery('email_newsletters')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
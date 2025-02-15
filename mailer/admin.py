from django.contrib import admin
from .models import Subscriber, Mailing, EmailOpenTracking


admin.site.register(Subscriber)
admin.site.register(Mailing)
admin.site.register(EmailOpenTracking)
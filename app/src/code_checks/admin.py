from django.contrib import admin

from .models import Check, PeriodicTaskRun

admin.site.register(Check)
admin.site.register(PeriodicTaskRun)

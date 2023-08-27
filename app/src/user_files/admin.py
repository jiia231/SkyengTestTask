from django.contrib import admin

from .models import UserFile


class FileAdmin(admin.ModelAdmin):
    list_display = ("user", "file_name", "file")


admin.site.register(UserFile, FileAdmin)

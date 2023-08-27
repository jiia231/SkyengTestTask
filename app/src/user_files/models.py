from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


def file_path_handler(instance, filename):
    return f"user_files/{instance.user.id}/{filename}"


class UserFile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file = models.FileField(
        upload_to=file_path_handler,
        validators=[FileExtensionValidator(allowed_extensions=["py"])],
        blank=False,
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    def get_absolute_url(self):
        return reverse("file_detail", args=[str(self.id)])

from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M"
        FEMALE = "F"
        UNKNOWN = "U"

    gender = models.CharField(
        max_length=1, choices=Gender.choices, default=Gender.UNKNOWN
    )

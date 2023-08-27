from django.db import models


class PeriodicTaskRun(models.Model):
    task = models.CharField(max_length=200, verbose_name="Task Name")
    created = models.DateTimeField(auto_now_add=True)


class Check(models.Model):
    class StatusEnum(models.TextChoices):
        NEW = "new"
        RUNNING = "running"
        DONE = "done"
        ERROR = "error"

    class ResultEnum(models.TextChoices):
        SUCCESS = "success"
        FAIL = "fail"

    file = models.OneToOneField(
        "user_files.UserFile", on_delete=models.CASCADE, related_name="lint_check"
    )
    status = models.CharField(
        max_length=8, choices=StatusEnum.choices, default=StatusEnum.NEW
    )
    result = models.CharField(
        max_length=7, choices=ResultEnum.choices, default=None, null=True
    )
    logs = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

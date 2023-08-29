from datetime import datetime, timezone
from logging import getLogger

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from flake8.api import legacy as flake8
from flake8.formatting.default import Default as DefaultFormatter
from pathlib import Path
from user_files.models import UserFile

from .models import Check, PeriodicTaskRun

logger = getLogger(__name__)


@shared_task
def send_notification(email: str, result: Check.ResultEnum, log: str):
    subject = (
        "Your code looks good!"
        if result == Check.ResultEnum.SUCCESS
        else "We found issues in your code!"
    )
    message = (
        "Hello,\nWe've ran some checks on your code and here are the results:\n\n" + log
    )
    send_mail(
        subject,
        message,
        "from@example.com",
        [email],
        fail_silently=False,
    )
    logger.info("Message to %s sent", email)


@shared_task(bind=True)
def run_flake8_checks(self):
    in_memory_log = []

    class CustomFormatter(DefaultFormatter):
        def _write(self, output: str) -> None:
            in_memory_log.append(output)

    try:
        last_run_obj = (
            PeriodicTaskRun.objects.filter(task=self.name)
            .order_by("-created")[:1]
            .get()
        )
        last_run = last_run_obj.created
    except ObjectDoesNotExist:
        last_run = datetime(1970, 1, 1, tzinfo=timezone.utc)
    PeriodicTaskRun.objects.create(task=self.name)

    files = UserFile.objects.filter(updated__gt=last_run).all()
    for file in files:
        check = Check.objects.create(file=file)
        try:
            check.status = Check.StatusEnum.RUNNING
            style_guide = flake8.get_style_guide()
            style_guide.init_report(CustomFormatter)
            file_path = file.file.name
            output_file = Path(f"/tmp/{file_path}")
            output_file.parent.mkdir(exist_ok=True, parents=True)
            output_file.write_bytes(file.file.read())
            report = style_guide.input_file(f"/tmp/{file_path}")

            if report.total_errors == 0:
                check.logs = "Linting successful. No issues found."
                check.result = Check.ResultEnum.SUCCESS
                check.status = Check.StatusEnum.DONE
            else:
                check.logs = (
                    f"Linting failed. Issues found.\n"
                    f"Total errors: {report.total_errors}\n" + "\n".join(in_memory_log)
                )
                check.result = Check.ResultEnum.FAIL
                check.status = Check.StatusEnum.DONE
            check.save()
            send_notification.delay(file.user.email, check.result, check.logs)
        except Exception as exc:  # pylint: disable=broad-except
            print(exc)
            check.logs = str(exc)
            check.status = Check.StatusEnum.ERROR
            check.save()

from unittest.mock import Mock, patch

import pytest

from code_checks.models import Check, PeriodicTaskRun
from code_checks.tasks import run_flake8_checks, send_notification


def test_send_notification():
    email = "test@example.com"
    result = Check.ResultEnum.SUCCESS
    log = "Linting successful. No issues found."

    mock_send_email = Mock()
    with patch("code_checks.tasks.send_mail", mock_send_email):
        send_notification(email, result, log)

    mock_send_email.assert_called_once_with(
        "Your code looks good!",
        "Hello,\nWe've ran some checks on your code and here are the results:\n\n"
        + log,
        "from@example.com",
        [email],
        fail_silently=False,
    )


@pytest.mark.django_db
def test_run_flake8_checks(user_file):
    mock_send_notification = Mock()
    with patch("code_checks.tasks.send_notification.delay", mock_send_notification):
        # pylint: disable=no-value-for-parameter
        run_flake8_checks()

    checks = Check.objects.filter(file=user_file)
    assert checks.exists()

    check = checks.first()
    assert check.status == Check.StatusEnum.DONE
    assert check.result == Check.ResultEnum.SUCCESS

    assert mock_send_notification.called
    assert mock_send_notification.call_args[0][1] == Check.ResultEnum.SUCCESS
    assert (
        "Linting successful. No issues found." in mock_send_notification.call_args[0][2]
    )


@pytest.mark.django_db
def test_run_flake8_checks_exception(user_file):
    # pylint: disable=unused-argument
    mock_send_notification = Mock()
    mock_get_style_guide = Mock()
    mock_style_guide = Mock()
    mock_get_style_guide.return_value = mock_style_guide
    mock_style_guide.check_files.side_effect = Exception("Something went wrong")

    with patch("code_checks.tasks.flake8.get_style_guide", mock_get_style_guide), patch(
        "code_checks.tasks.send_notification.delay", mock_send_notification
    ):
        # pylint: disable=no-value-for-parameter
        run_flake8_checks()

    assert PeriodicTaskRun.objects.count() == 1
    assert PeriodicTaskRun.objects.first().task == "code_checks.tasks.run_flake8_checks"

    assert Check.objects.count() == 1
    assert Check.objects.first().status == Check.StatusEnum.ERROR
    assert "Something went wrong" in Check.objects.first().logs


@pytest.mark.django_db
def test_run_flake8_checks_no_user_files():
    mock_send_notification = Mock()
    with patch("code_checks.tasks.send_notification.delay", mock_send_notification):
        # pylint: disable=no-value-for-parameter
        run_flake8_checks()

    assert PeriodicTaskRun.objects.count() == 1
    assert Check.objects.count() == 0

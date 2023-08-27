import pytest
from django.urls import reverse

import conftest
from accounts.forms import CustomLoginForm


@pytest.mark.django_db
def test_custom_login_form_render(client):
    """
    Test that the CustomLoginForm renders correctly.
    """
    response = client.get(reverse("account_login"))
    form = response.context["form"]

    assert isinstance(form, CustomLoginForm)


@pytest.mark.django_db
def test_custom_login_form_valid_submission(client, user):
    # pylint: disable=unused-argument
    """
    Test that a valid form submission works correctly.
    """
    response = client.post(
        reverse("account_login"),
        data={
            "login": conftest.EMAIL,
            "password": conftest.PASSWORD,
        },
    )

    assert response.status_code == 302  # Successful login should result in a redirect.


@pytest.mark.django_db
def test_custom_login_form_invalid_submission(client):
    """
    Test that an invalid form submission shows errors.
    """
    response = client.post(
        reverse("account_login"),
        data={
            "login": "your_username",
            "password": "",
        },
    )

    assert (
        response.status_code == 200
    )  # Invalid submission should return to the login page.
    assert (
        b"This field is required." in response.content
    )  # Assuming this error message is displayed.

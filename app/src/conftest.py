import pytest

# https://github.com/celery/celery/issues/4511#issuecomment-741877597
from celery.fixups.django import DjangoWorkerFixup
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client

from user_files.models import UserFile

DjangoWorkerFixup.install = lambda x: None


User = get_user_model()

USERNAME = "testuser"
EMAIL = "test@example.com"
PASSWORD = "testpassword"
FILE_NAME = "test_file"
FILE_CONTENT = b"def my_function():\n    return 42\n"


@pytest.fixture
def user():
    return User.objects.create_user(username=USERNAME, email=EMAIL, password=PASSWORD)


@pytest.fixture
def user_file(user):
    # pylint: disable=redefined-outer-name
    file = SimpleUploadedFile(FILE_NAME, FILE_CONTENT)
    return UserFile.objects.create(user=user, file_name=FILE_NAME, file=file)


@pytest.fixture
def authenticated_client(user):
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    client = Client()
    client.login(email=EMAIL, password=PASSWORD)
    return client

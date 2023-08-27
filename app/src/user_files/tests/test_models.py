import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

import conftest
from user_files.models import UserFile


@pytest.mark.django_db
def test_user_file_creation(user):
    """
    Test UserFile model creation.
    """
    file = SimpleUploadedFile(conftest.FILE_NAME, conftest.FILE_CONTENT)
    user_file = UserFile.objects.create(
        user=user, file_name=conftest.FILE_NAME, file=file
    )

    assert user_file.id is not None
    assert user_file.user == user
    assert f"user_files/{user.id}/{conftest.FILE_NAME}" in str(user_file.file.name)


@pytest.mark.django_db
def test_invalid_extension(user):
    """
    Test that an invalid file extension raises a ValidationError.
    """
    file = SimpleUploadedFile("file.jar", conftest.FILE_CONTENT)
    with pytest.raises(ValidationError):
        # Django does not run the validators when saving the item,
        # only the ModelForms do, likely for performance reasons
        # That's why we explicitly call full_clean()
        UserFile.objects.create(
            user=user, file_name="Invalid File", file=file
        ).full_clean()

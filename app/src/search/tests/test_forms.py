import pytest
from django.urls import reverse

from search.forms import SearchForm


@pytest.mark.django_db
def test_search_form_render(authenticated_client):
    """
    Test that the SearchForm renders correctly.
    """
    response = authenticated_client.get(reverse("search_base_page"))
    form = response.context["form"]

    assert isinstance(form, SearchForm)
    assert form.helper.form_show_labels is False

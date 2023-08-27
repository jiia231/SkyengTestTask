import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_search_results_view(authenticated_client, user_file):
    """
    Test that the SearchResultsListView returns correct
    results for an authenticated user.
    """
    response = authenticated_client.get(reverse("search_results"), {"q": "test"})

    assert response.status_code == 200
    assert user_file.file_name.encode() in response.content


@pytest.mark.django_db
def test_search_results_view_unauthenticated(client):
    """
    Test that the SearchResultsListView redirects
    to the login page for an unauthenticated user.
    """
    response = client.get(reverse("search_results"), {"q": "test"})

    assert response.status_code == 302
    assert "login" in response.url


@pytest.mark.django_db
def test_search_results_view_no_query(authenticated_client):
    """
    Test that the SearchResultsListView handles no query parameter correctly.
    """
    response = authenticated_client.get(reverse("search_results"))

    assert response.status_code == 200
    assert b"No results found" in response.content

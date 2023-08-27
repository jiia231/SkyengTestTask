from django.urls import path

from .views import SearchBasePage, SearchResultsListView

extra_context = {"active_section": "search"}

urlpatterns = [
    path(
        "results/",
        SearchResultsListView.as_view(extra_context=extra_context),
        name="search_results",
    ),
    path(
        "", SearchBasePage.as_view(extra_context=extra_context), name="search_base_page"
    ),
]

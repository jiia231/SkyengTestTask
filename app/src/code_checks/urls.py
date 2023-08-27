from django.urls import path

from .views import ChecksDetailView, ChecksListView

extra_context = {"active_section": "checks"}

urlpatterns = [
    path("", ChecksListView.as_view(extra_context=extra_context), name="checks_list"),
    path(
        "<int:pk>/",
        ChecksDetailView.as_view(extra_context=extra_context),
        name="check_detail",
    ),
]

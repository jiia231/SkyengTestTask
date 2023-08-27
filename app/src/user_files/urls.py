from django.urls import path

from .views import (
    UserFilesCreateView,
    UserFilesDeleteView,
    UserFilesDetailView,
    UserFilesListView,
    UserFilesUpdateView,
)

extra_context = {"active_section": "files"}

urlpatterns = [
    path("", UserFilesListView.as_view(extra_context=extra_context), name="files_list"),
    path(
        "<int:pk>/",
        UserFilesDetailView.as_view(extra_context=extra_context),
        name="file_detail",
    ),
    path(
        "<int:pk>/update/",
        UserFilesUpdateView.as_view(extra_context=extra_context),
        name="file_update",
    ),
    path(
        "<int:pk>/delete/",
        UserFilesDeleteView.as_view(extra_context=extra_context),
        name="file_delete",
    ),
    path(
        "upload/",
        UserFilesCreateView.as_view(extra_context=extra_context),
        name="file_upload",
    ),
]

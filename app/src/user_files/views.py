from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import UserFile


class UserFilesListView(LoginRequiredMixin, ListView):
    context_object_name = "file_list"
    template_name = "user_files/user_files_list.html"

    def get_queryset(self):
        return UserFile.objects.filter(user=self.request.user)


class UserFilesDetailView(LoginRequiredMixin, DetailView):
    model = UserFile
    context_object_name = "userfile"
    template_name = "user_files/user_file_detail.html"


class UserFilesCreateView(LoginRequiredMixin, CreateView):
    model = UserFile
    fields = ("file_name", "file")
    context_object_name = "userfile"
    template_name = "user_files/user_file_create_or_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserFilesUpdateView(LoginRequiredMixin, UpdateView):
    model = UserFile
    fields = ("file_name", "file")
    context_object_name = "userfile"
    template_name = "user_files/user_file_create_or_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserFilesDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("files_list")

    def get_object(self, queryset=None):
        primary_key = self.kwargs.get("pk")
        obj = get_object_or_404(UserFile, pk=primary_key)
        if obj.user != self.request.user:
            raise Http404()
        return obj

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Check


class ChecksListView(LoginRequiredMixin, ListView):
    context_object_name = "check_list"
    template_name = "checks/checks_list.html"

    def get_queryset(self):
        return Check.objects.filter(file__user=self.request.user)


class ChecksDetailView(LoginRequiredMixin, DetailView):
    model = Check
    context_object_name = "lint_check"
    template_name = "checks/check_detail.html"

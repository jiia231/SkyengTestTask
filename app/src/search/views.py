from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import FormView, ListView

from user_files.models import UserFile

from .forms import SearchForm


class SearchBasePage(LoginRequiredMixin, FormView):
    template_name = "search/base_page.html"
    form_class = SearchForm
    success_url = "search_results"


class SearchResultsListView(LoginRequiredMixin, ListView, FormView):
    form_class = SearchForm
    context_object_name = "file_list"
    template_name = "search/results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is None:
            return None
        return UserFile.objects.filter(user=self.request.user).filter(
            Q(file_name__icontains=query) | Q(lint_check__logs__icontains=query)
        )

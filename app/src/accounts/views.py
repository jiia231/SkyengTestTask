from allauth.account.forms import ChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = "account/change_password.html"
    form_class = ChangePasswordForm

from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "login",
            "password",
            Field(
                "remember",
                wrapper_class="flex gap-2 items-center",
                css_class="mb-2",
            ),
        )
